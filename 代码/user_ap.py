

import xlrd
from sklearn.cluster import AffinityPropagation

# 获取特征向量
def getUserVector(user):
    # userDict[2] = [[1, 4, 6, 8], ["爱情", "动画", "古装", "惊悚", "犯罪", "冒险", "战争"]] ,则 user_vector =[1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0]
    user_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(user[1])):
        if user[1][i] == "爱情":
            user_vector[0] = 1
        elif user[1][i] == "喜剧" or user[1][i] == "搞笑":
            user_vector[1] = 1
        elif user[1][i] == '动作':
            user_vector[2] = 1
        elif user[1][i] == "科幻":
            user_vector[3] = 1
        elif user[1][i] == "动画" or user[1][i] == "益智" or user[1][i] == "童话" or user[1][i] == "儿童":
            user_vector[4] = 1
        elif user[1][i] == "古装" or user[1][i] == "武侠":
            user_vector[5] = 1
        elif user[1][i] == "悬疑":
            user_vector[6] = 1
        elif user[1][i] == "真人秀" or user[1][i] == "脱口秀" or user[1][i] == "综艺" or user[1][i] == "中国大陆":
            user_vector[7] = 1
        elif user[1][i] == "历史" or user[1][i] == "纪录片" or user[1][i] == "传记":
            user_vector[8] = 1
        elif user[1][i] == "惊悚" or user[1][i] == "恐怖":
            user_vector[9] = 1
        elif user[1][i] == "犯罪":
            user_vector[10] = 1
        elif user[1][i] == "奇幻":
            user_vector[11] = 1
        elif user[1][i] == "冒险":
            user_vector[12] = 1
        elif user[1][i] == "战争":
            user_vector[13] = 1
        elif user[1][i] == "音乐" or user[1][i] == "家庭":
            user_vector[14] = 1
        elif user[1][i] == "青春" or user[1][i] == "少女" or user[1][i] == "校园" or user[1][i] == "情感":
            user_vector[15] = 1
        else:
            continue
    return user_vector

# 读取文件
def readFile(filename):
    workbook = xlrd.open_workbook(filename)
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    return sheet

# 数据格式化为二维数组
def getMoiveInfo(sheet1, sheet2):
    moive = [i for i in range(0, sheet2.nrows)]
    for i in range(1, sheet2.nrows):
        moive[int(sheet2.row_values(i)[0])] = sheet2.row_values(i)[2]
    moivelist = []
    for i in range(1, sheet1.nrows):
        moive_tybe = sheet1.row_values(i)
        moivelist.append([int(moive_tybe[0]), int(moive_tybe[1]), moive[int(moive_tybe[1])]])
    return moivelist

# 统计用户看过那些影视及其类型
def getUserPreferenceTybeDataStructure(moivelist):
    # userDict[2]=[ [ 1,4,6,8],[ "爱情","动画","古装","惊悚","犯罪","冒险","战争"]]    表示用户2看过序号为1，4，6，8的影视，它们总体由"爱情","动画","古装","惊悚","犯罪","冒险","战争"这几种类型构成
    userDict = {}
    for k in moivelist:
        if k[0] in userDict:
            if k[1] in userDict[k[0]][0]:
                continue
            userDict[k[0]][0].append(k[1])
            moive_tybe = k[2].split('/')
            for i in range(0, len(moive_tybe)):
                if moive_tybe[i] not in userDict[k[0]][1]:
                    userDict[k[0]][1].append(moive_tybe[i])
        else:
            moive_tybe = k[2].split('/')
            userDict[k[0]] = [[k[1]], [moive_tybe[0]]]
            for i in range(1, len(moive_tybe)):
                userDict[k[0]][1].append(moive_tybe[i])
    return userDict

# 生成用户矩阵
def getUserMatrix(filename1, filename2):
    X = []
    users = []
    sheet1 = readFile(filename1)
    sheet2 = readFile(filename2)
    moivelist = getMoiveInfo(sheet1, sheet2)
    userDict = getUserPreferenceTybeDataStructure(moivelist)
    for k in moivelist:
        if k[0] not in users:
            users.append(k[0])
    for user in users:
        x = getUserVector(userDict[user])
        X.append(x)
    return X


if __name__ == '__main__':
    X = getUserMatrix("...\data\用户.xlsx", "...\data\完整版表4.xlsx")
    # 计算AP
    ap = AffinityPropagation(max_iter=150).fit(X)
    cluster_centers_indices = ap.cluster_centers_indices_  # 预测出的中心点的索引，如[123,23,34]
    labels = ap.labels_  # 预测出的每个数据的类别标签,labels是一个NumPy数组
    # print(labels)
    n_clusters_ = len(cluster_centers_indices)  # 预测聚类中心的个数

    # print('预测的聚类中心个数：%d' % n_clusters_)

    X1 = [X[i] for i in cluster_centers_indices]
    # 再次计算AP
    ap = AffinityPropagation().fit(X1)
    cluster_centers_indices1 = ap.cluster_centers_indices_
    # print(cluster_centers_indices1)
    labels1 = ap.labels_
    # print(labels)
    n_clusters_ = len(cluster_centers_indices1)

    print('预测的聚类中心个数：%d' % n_clusters_)
    #打印中心坐标
    for j in cluster_centers_indices1:
        print(X1[j])
    moive_type = ["爱情", "喜剧", '动作', "科幻", "动画", "古装", "悬疑", "真人秀", "历史", "惊悚", "犯罪", "奇幻", "冒险", "战争", "家庭", "青春"]
    #打印出中心所代表的类型聚类
    for j in cluster_centers_indices1:
        julei = []
        for z in range(0, 15):
            if X1[j][z] == 1:
                julei.append(moive_type[z])
        print(julei)
    #获得用户聚类，并打印出来
    point = {}
    for indexes in cluster_centers_indices1:
        point[indexes] = []

    for i in range(0, len(labels)):
        labels[i] = labels1[labels[i]]
        for indexes in cluster_centers_indices1:
            if cluster_centers_indices1[labels[i]] == indexes:
                point[indexes].append(i)

    user_point = {}
    for indexes in cluster_centers_indices1:
        user_point[indexes] = []

    sheet = readFile("...\data\用户.xlsx")
    users = []
    for i in range(1, sheet.nrows):
        if sheet.row_values(i)[0] not in users:
            users.append(sheet.row_values(i)[0])
    # print(len(user))
    for indexes in cluster_centers_indices1:
        for i in point[indexes]:
            user_point[indexes].append(users[i])

    for indexes in cluster_centers_indices1:
        print(user_point[indexes])