from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from utils import predict,predict1
from preprocess import preprocess

leixing = [ "爱情","喜剧","恐怖","悬疑","奇幻","科幻","动画","动作","犯罪","古装","真人秀","冒险","历史","战争"]
data_features = []
vectorizer = []
lin_clf = []
for i in range(0,len(leixing)):
    data_features.append(preprocess("...\data\影视简介.xlsx",leixing[i]))
    train_data, test_data = train_test_split(data_features[i], test_size=0.1, random_state=42)
    vectorizer.append(TfidfVectorizer(min_df=2, tokenizer=None, preprocessor=None, stop_words=None))
    train_data_features = vectorizer[i].fit_transform(train_data['plot'])
    train_data_features = train_data_features.toarray()
    lin_clf.append(svm.LinearSVC())
    lin_clf[i].fit(train_data_features, train_data['tags'])
    #predict(vectorizer[i], lin_clf[i], test_data)

lujin = [ "...\爱情.txt","...\喜剧.txt","...\恐怖.txt","...\悬疑.txt","...\奇幻.txt",
          "...\科幻.txt","...\动画.txt","...\动作.txt","...\犯罪.txt","...\古装.txt",
          "...\真人秀.txt","...\冒险.txt","...\历史.txt","...\战争.txt"]
for i in range(0,len(lujin)):
    label_data_features = preprocess("...\data\附件2：电视产品信息数据（贴标签）.xlsx")
    str = predict1(vectorizer[i], lin_clf[i], label_data_features)
    f = open(lujin[i], "w+")
    for str1 in str:
        f.write(str1 + "\n")
    f.close()
print("预测完毕！")
