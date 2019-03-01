import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score

my_tags = [u'爱情', u'其他']

def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    #画图的
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(my_tags))
    target_names = my_tags
    plt.xticks(tick_marks, target_names, rotation=90)
    plt.yticks(tick_marks, target_names)
    # plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def evaluate_prediction(predictions, target, title="Confusion matrix"):
    #  下面那些都是sklearn的模型评估函数
    print('accuracy %s' % accuracy_score(target, predictions))
    print('precision %s' % precision_score(target, predictions,pos_label=u'喜剧'))
    print('recall %s' % recall_score(target, predictions,pos_label=u'喜剧'))
    print('f-measure %s' % f1_score(target, predictions,pos_label=u'喜剧'))

    cm = confusion_matrix(target, predictions)
    print('confusion matrix\n %s' % cm)
    print('(row=expected, col=predicted)')

    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.figure()
    plot_confusion_matrix(cm_normalized, title + ' Normalized')
    plt.show()


def predict(vectorizer, classifier, data):
    data_features = vectorizer.transform(data['plot'])
    predictions = classifier.predict(data_features)
    target = data['tags']
    evaluate_prediction(predictions, target)


def getTags(genre, sheet):
    tagVector = []
    for i in range(1,sheet.nrows):
        if sheet.row_values(i)[2] == genre:
            tagVector.append(genre)
        else:
            tagVector.append('其他')

    return tagVector

def predict1(vectorizer, classifier, data):
    data_features = vectorizer.transform(data['plot'])
    predictions = classifier.predict(data_features)
    return  predictions