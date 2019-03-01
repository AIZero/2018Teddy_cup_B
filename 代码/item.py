
import xlrd
import xlwt

wookbook = xlrd.open_workbook("...\data\附件2：电视产品信息数据标签.xlsx")
sheet_name = wookbook.sheet_names()
sheet = wookbook.sheet_by_name(sheet_name[0])
leixing = ["综艺娱乐","电视剧场","科学教育","生活服务","广告","家庭影院","新闻时事","体育竞技"]
a = ["生活服务","新闻时事","体育竞技"]
b = { '生活服务':"家庭成员",'新闻时事':"家庭成员","体育竞技":"体育爱好者"}
c = { '生活服务':"中年",'新闻时事':"中老年","体育竞技":"青年"}
d = ["真人秀","脱口秀","战争","冒险","音乐","歌舞","悬疑","喜剧","犯罪","家庭","科幻","短片","爱情","儿童","运动",
     "动作","传记","纪录片","奇幻","教育","健康","益智","热血","战斗","幼儿","小品","历史","校园","时装","新闻","言情",
     "都市","情感","访谈","童话","搞笑","体育","励志","青春","偶像","轻喜","抗战","抗日","谍战","惊悚","恐怖","短剧","情景剧",
     "美食","MV","体育新闻","中年","中老年","青年","武侠","古装"," "]
items = []
moive = []
for i in range(1,sheet.nrows):
    for lei in leixing:
        if lei in sheet.row_values(i)[10].split("\\"):
            if sheet.row_values(i)[0] not in moive:
                moive.append(sheet.row_values(i)[0])
                if lei in a:
                    items.append([sheet.row_values(i)[0],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],
                                  sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],
                                  sheet.row_values(i)[10], "适用人群", b[lei], c[lei]])
                    items.append([sheet.row_values(i)[0],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],
                                  sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],
                                  sheet.row_values(i)[10], "基本特征", lei, sheet.row_values(i)[3]])
                else:
                    if lei == "广告":
                        items.append([sheet.row_values(i)[0],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],
                                      sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],
                                      sheet.row_values(i)[10],sheet.row_values(i)[11], "基本特征", lei, " "])
                    else:
                        items.append([sheet.row_values(i)[0],sheet.row_values(i)[3],sheet.row_values(i)[4],sheet.row_values(i)[5],
                                      sheet.row_values(i)[6],sheet.row_values(i)[7],sheet.row_values(i)[8],sheet.row_values(i)[9],
                                      sheet.row_values(i)[10],sheet.row_values(i)[11], "基本特征", lei, sheet.row_values(i)[3]])
j = 0
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('产品数据标签', cell_overwrite_ok=True)
for item in items:
    label = item[11].split("/")
    for type in label:
        if type == "动画":
            sheet.write(j, 0, item[0])
            sheet.write(j, 1, item[1])
            sheet.write(j, 2, item[2])
            sheet.write(j, 3, item[3])
            sheet.write(j, 4, item[4])
            sheet.write(j, 5, item[5])
            sheet.write(j, 6, item[6])
            sheet.write(j, 7, item[7])
            sheet.write(j, 8, item[8])
            sheet.write(j, 9, item[9])
            sheet.write(j, 10, "娱乐")
            sheet.write(j, 11, type)
            j += 1
            sheet.write(j, 0, item[0])
            sheet.write(j, 1, item[1])
            sheet.write(j, 2, item[2])
            sheet.write(j, 3, item[3])
            sheet.write(j, 4, item[4])
            sheet.write(j, 5, item[5])
            sheet.write(j, 6, item[6])
            sheet.write(j, 7, item[7])
            sheet.write(j, 8, item[8])
            sheet.write(j, 9, "适用人群")
            sheet.write(j, 10, "家庭成员")
            sheet.write(j, 11, "儿童")
            j += 1
            print(j)
        if type in d:
            sheet.write(j, 0, item[0])
            sheet.write(j, 1, item[1])
            sheet.write(j, 2, item[2])
            sheet.write(j, 3, item[3])
            sheet.write(j, 4, item[4])
            sheet.write(j, 5, item[5])
            sheet.write(j, 6, item[6])
            sheet.write(j, 7, item[7])
            sheet.write(j, 8, item[8])
            sheet.write(j, 9, item[9])
            sheet.write(j, 10, item[10])
            sheet.write(j, 11, type)
            j += 1

book.save(r'...\产品数据标签.xls')