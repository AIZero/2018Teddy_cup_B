
import xlrd

#根据频道判断是否喜好体育，根据频道判断是否有小孩
workbook = xlrd.open_workbook("...\data\附件1：用户收视信息（图+清洗）.xlsx")
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])
f = open(r"...\用户部分标签.txt","w+")
for i in range(1,sheet.nrows):
    if sheet.row_values(i)[3] == "金鹰卡通" or sheet.row_values(i)[3] == "卡酷动画" or sheet.row_values(i)[3] == "南方少儿" or sheet.row_values(i)[3] == "嘉佳卡通" or sheet.row_values(i)[3] == "优漫卡通" or sheet.row_values(i)[3] == "动漫秀场":
        f.write(str(sheet.row_values(i)[0])+" "+"收视偏好"+" "+"娱乐"+" "+"动画"+"\n")
        f.write(str(sheet.row_values(i)[0]) + " " + "基本特征" + " " + "家庭成员" +" "+"儿童"+ "\n")
    if sheet.row_values(i)[3] == "广东新闻" or sheet.row_values(i)[3] == "中央新闻" or sheet.row_values(i)[3] == "广州新闻广播" or sheet.row_values(i)[3] == "广州新闻" or sheet.row_values(i)[3] == "凤凰中文":
        f.write(str(sheet.row_values(i)[0]) + " " + "收视偏好" + " " + "新闻" + "\n")
    if sheet.row_values(i)[3] == "中央5台" or sheet.row_values(i)[3] == "广东体育" or sheet.row_values(i)[3] == "CCTV5" or sheet.row_values(i)[3] == "篮球频道":
        if sheet.row_values(i)[6] < 0.0070:
            f.write(str(sheet.row_values(i)[0])+" "+"收视偏好"+" "+"新闻"+" "+"体育"+"\n")
        else:
            f.write(str(sheet.row_values(i)[0]) + " " + "收视偏好" + " " + "体育" + "\n")
f.close()