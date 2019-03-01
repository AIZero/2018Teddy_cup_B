import pandas as pd
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from utils import getTags
import jieba
import re
import xlrd


def plotToWords(raw_plot):
    stopwords = [line.strip() for line in open('...data\停用词.txt').readlines()]  # 读取中文停用词表
    word_vector = []
    text = jieba.cut(raw_plot)  # 分词,默认是精确分词
    for word in text:
        # 通过合并所有中文内容得到纯中文内容
        word = ''.join(re.findall(u'[\u4e00-\u9fa5]+', word))  # 去掉不是中文的内容
        word = word.strip()
        if (len(word) != 0 and not stopwords.__contains__(word)):  # 去掉在停用词表中出现的内容
            word_vector.append(word)
    return word_vector

def preprocess(filename,genre = None):
    workbook = xlrd.open_workbook(filename)  # 读取excel文件
    sheet_names = workbook.sheet_names()  # 获取表格名
    sheet = workbook.sheet_by_name(sheet_names[0])  # 获取第i-1张表格数据
    clean_train_reviews = []

    for i in range(1, sheet.nrows):
        if ((i + 1) % 100 == 0):
            print("Review %d of %d\n" % (i + 1, sheet.nrows))
        clean_train_reviews.append(plotToWords(sheet.row_values(i)[1]))

    tagVector = getTags(genre, sheet)
    data = {'plot': clean_train_reviews, 'tags': tagVector}
    df = pd.DataFrame(data)

    return df