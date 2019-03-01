
import math
import xlrd
import random

# 读取文件
def readFile(filename):
    workbook = xlrd.open_workbook(filename)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    return sheet

# 数据格式化为二维数组
def getMoiveInfo(sheet1,sheet2):
    moive = [i for i in range(0,sheet2.nrows)]
    for i in range(1,sheet2.nrows):
        moive[int(sheet2.row_values(i)[0])] = sheet2.row_values(i)[2]
    moivelist = []
    for i in range(1,sheet1.nrows):
        moive_tybe = sheet1.row_values(i)
        moivelist.append([int(moive_tybe[0]),int(moive_tybe[1]),moive[int(moive_tybe[1])]])
    return moivelist

# 生成用户偏好数据结构
def getUserPreferenceWeightDataStructure(moivelist):
    # userDict[2]=[ [1,4,6,8],[ 3,0,0,0,2,1,0,0,0,1,1,0,3,2,0,0] ].... 表示用户2看过序号为1，4，6，8的影视，其中爱情类的有3部，动画类的有2部，古装类的有1部，惊悚类的有1部，犯罪类有1部，冒险类有3部，战争类有2部
    userDict = {}
    #对数据进行遍历，确定每个用户看过那些影视和用户的偏好，每看过一部影视，用户在该影视对应类型的数值上+1
    for k in moivelist:
        if k[0] not in userDict:
            vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            moive_tybe = k[2].split('/')
            for i in range(0, len(moive_tybe)):
                if moive_tybe[i] == "爱情":
                    vector[0] = 1
                elif moive_tybe[i] == "喜剧" or moive_tybe[i] == "搞笑":
                    vector[1] = 1
                elif moive_tybe[i] == "动作":
                    vector[2] = 1
                elif moive_tybe[i] == "科幻":
                    vector[3] = 1
                elif moive_tybe[i] == "动画" or moive_tybe[i] == "益智" or moive_tybe[i] == "童话" or moive_tybe[i] == "儿童":
                    vector[4] = 1
                elif moive_tybe[i] == "古装" or moive_tybe[i] == "武侠":
                    vector[5] = 1
                elif moive_tybe[i] == "悬疑":
                    vector[6] = 1
                elif moive_tybe[i] == "真人秀" or moive_tybe[i] == "中国大陆" or moive_tybe[i] == "综艺" or moive_tybe[
                    i] == "脱口秀":
                    vector[7] = 1
                elif moive_tybe[i] == "历史" or moive_tybe[i] == "纪录片" or moive_tybe[i] == "传记":
                    vector[8] = 1
                elif moive_tybe[i] == "惊悚" or moive_tybe[i] == "恐怖":
                    vector[9] = 1
                elif moive_tybe[i] == "犯罪":
                    vector[10] = 1
                elif moive_tybe[i] == "奇幻":
                    vector[11] = 1
                elif moive_tybe[i] == "冒险":
                    vector[12] = 1
                elif moive_tybe[i] == "战争":
                    vector[13] = 1
                elif moive_tybe[i] == "音乐" or moive_tybe[i] == "家庭":
                    vector[14] = 1
                elif moive_tybe[i] == "青春" or moive_tybe[i] == "少女" or moive_tybe[i] == "校园" or moive_tybe[i] == "都市" or \
                        moive_tybe[i] == "情感":
                    vector[15] = 1
                else:
                    continue
            userDict[k[0]] = [[k[1]], vector]


        else:
            if k[1] not in userDict[k[0]][0]:
                userDict[k[0]][0].append(k[1])
                moive_tybe = k[2].split('/')
                for i in range(0, len(moive_tybe)):
                    if moive_tybe[i] == "爱情":
                        userDict[k[0]][1][0] += 1
                    elif moive_tybe[i] == "喜剧" or moive_tybe[i] == "搞笑":
                        userDict[k[0]][1][1] += 1
                    elif moive_tybe[i] == "动作":
                        userDict[k[0]][1][2] += 1
                    elif moive_tybe[i] == "科幻":
                        userDict[k[0]][1][3] += 1
                    elif moive_tybe[i] == "动画" or moive_tybe[i] == "益智" or moive_tybe[i] == "童话" or moive_tybe[i] == "儿童":
                        userDict[k[0]][1][4] += 1
                    elif moive_tybe[i] == "古装" or moive_tybe[i] == "武侠":
                        userDict[k[0]][1][5] += 1
                    elif moive_tybe[i] == "悬疑":
                        userDict[k[0]][1][6] += 1
                    elif moive_tybe[i] == "真人秀" or moive_tybe[i] == "中国大陆" or moive_tybe[i] == "综艺" or moive_tybe[i] == "脱口秀":
                        userDict[k[0]][1][7] += 1
                    elif moive_tybe[i] == "历史" or moive_tybe[i] == "纪录片" or moive_tybe[i] == "传记":
                        userDict[k[0]][1][8] += 1
                    elif moive_tybe[i] == "惊悚" or moive_tybe[i] == "恐怖":
                        userDict[k[0]][1][9] += 1
                    elif moive_tybe[i] == "犯罪":
                        userDict[k[0]][1][10] += 1
                    elif moive_tybe[i] == "奇幻":
                        userDict[k[0]][1][11] += 1
                    elif moive_tybe[i] == "冒险":
                        userDict[k[0]][1][12] += 1
                    elif moive_tybe[i] == "战争":
                        userDict[k[0]][1][13] += 1
                    elif moive_tybe[i] == "音乐" or moive_tybe[i] == "家庭":
                        userDict[k[0]][1][14] += 1
                    elif moive_tybe[i] == "青春" or moive_tybe[i] == "少女" or moive_tybe[i] == "校园" or moive_tybe[i] == "都市" or moive_tybe[i] == "情感":
                        userDict[k[0]][1][15] += 1
                    else:
                        continue

    return userDict

# 使用UserPerferanceCF进行推荐，输入：用户文件,电影文件,用户号，邻居数量
def recommendByUserPerferenceCF(filename1,filename2, userId):
    sheet1 = readFile(filename1)
    sheet2 = readFile(filename2)
    moivelist= getMoiveInfo(sheet1,sheet2)
    userDict = getUserPreferenceWeightDataStructure(moivelist)
    recommend_list = []
    for i in range(0, 15):
        if userId not in userDict:
            recommend_list.append([0,i])
        else:
            recommend_list.append([userDict[userId][1][i] / len(userDict[userId][0]), i])
    recommend_list.sort(reverse=True)
    return recommend_list

# 获取电影的列表
def getMovieList(filename):
    sheet = readFile(filename)
    movies_info = {}
    for i in range(1,sheet.nrows):
        single_info = sheet.row_values(i)
        movies_info[int(single_info[0])] = single_info[1:]
    return movies_info

if __name__ == '__main__':

    moive_type = ["爱情","喜剧",'动作',"科幻","动画","古装","悬疑","真人秀","历史","惊悚","犯罪","奇幻","冒险","战争","家庭","青春"]
    movies = getMovieList("...\data\完整版表4.xlsx")
    users = []
    sheet1 = readFile("...\data\用户.xlsx")
    for i in range(1,sheet1.nrows):
        if sheet1.row_values(i)[0] not in users:
            users.append(sheet1.row_values(i)[0])
    sum = 0
    f = open(r"...\问题二推荐结果.txt","w+")
    for userId in users:
        recommend_list = recommendByUserPerferenceCF("...data\用户.xlsx","...\data\完整版表4.xlsx",userId)
        d = 0
        for a in recommend_list[:6]:
            if a[0] > 0.18:
                f.write(str(userId) + " " + "基本特征" + " " + moive_type[a[1]] + " " + str(a[0]) + "\n")
    f.close()
