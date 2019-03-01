
import xlrd
import xlwt
import random


# 读取文件
def readFile(filename):
    workbook = xlrd.open_workbook(filename)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    return sheet

# 数据格式化为二维数组
def getMoiveInfo(sheet):
    moivelist = []
    for i in range(1,sheet.nrows):
        moive_tybe = sheet.row_values(i)
        moivelist.append([int(moive_tybe[0]),int(moive_tybe[1])])
    return moivelist

# 生成用户评分数据结构
def getUseritemDataStructure(moivelist):
    # userDict[10001]=[1,4,8,9].... 表示用户2看过影视1，4，8，9
    #itemUser[1]=[10001,10038,10158].....表示电影4被用户10001，10038，10158看过
    userDict = {}
    itemUser = {}
    moivelist1=[]
    for moive in moivelist:
        if moive not in moivelist1:
            moivelist1.append(moive)
    for k in moivelist1:
        if k[0] in userDict:
            userDict[k[0]].append(k[1])
        else:
            userDict[k[0]] = [k[1]]
        if k[1] in itemUser:
            itemUser[k[1]].append(k[0])
        else:
            itemUser[k[1]] = [k[0]]
    return userDict, itemUser

#为一个用户做推荐
def evalate(userId,userDict,itemUser):
    command=[]
    for item in userDict[userId]:
        neighbors = []
        a=len(itemUser[item])
        for neighbor in itemUser[item]:
            if neighbor != userId and neighbor not in neighbors:
                neighbors.append(neighbor)
        movie = []
        movie_number = {}
        for neighbor in neighbors:
            for item in userDict[neighbor]:
                if item not in movie and item not in userDict[userId]:
                    movie.append(item)
                    movie_number[item] = 1
                else:
                    if item  in movie_number:
                        movie_number[item] += 1
        for item in movie:
            command.append([movie_number[item] / a , item])
    command.sort(reverse=True)
    commands=[]
    for item in command:
        if item not in commands:
            commands.append(item)
            for items in commands:
                if items[1] == item[1]:
                    if item[0] > items[0]:
                        commands.remove(items)
                    if item[0] < items[0]:
                        commands.remove(item)
    commands.sort(reverse=True)
    return commands

# 使用UseritemCF进行推荐，输入：文件名,用户ID,推荐影视数量
def recommendByUseritemCF(filename, userId,k = 10):
    sheet = readFile(filename)
    moivelist = getMoiveInfo(sheet)
    userDict, itemUser = getUseritemDataStructure(moivelist)
    command_dict= evalate(userId, userDict, itemUser)[:k]#找出排序在前的10个影视【【相似值5，电影1】，【3，电影3】··】

    return command_dict

# 获取电影的列表
def getMovieList(filename):
    sheet = readFile(filename)
    movies_info = {}
    for i in range(1,sheet.nrows):
        single_info = sheet.row_values(i)
        movies_info[int(single_info[0])] = single_info[1]
    return movies_info

if __name__ == '__main__':

    # 获取所有电影的列表
    movies = getMovieList("...\data\完整版表4.xlsx")
    users = []
    sheet1 = readFile("...\data\用户.xlsx")
    for i in range(1, sheet1.nrows):
        if sheet1.row_values(i)[0] not in users:
            users.append(sheet1.row_values(i)[0])
    j = 0
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    sum = 0
    for userId in users:
        command_dict = recommendByUseritemCF("...\data\用户.xlsx", userId, 10)
        for movie_id in command_dict:
            sheet.write(j, 0, userId)
            sheet.write(j, 1, movies[movie_id[1]])
            sheet.write(j, 2, movie_id[0])
            j += 1
    book.save(r'...\问题一推荐结果.xls')    #将推荐结果写入文档


