from os import path
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

current_dir = path.dirname(__file__)
fav_text = open('11000fav.txt', 'r')
fav_lines = fav_text.read().split('|')
rt_text = open('11000rt.txt', 'r')
rt_lines = rt_text.read().split('|')
#purpose_text = open('10000rt.txt', 'r')
#purpose_lines = purpose_text.read().split('|')

def word_analysis(word):

    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(word)

    result = []

    while node:
        str = node.feature.split(',')
        tmp = str[0].split(',')
        if tmp[0] == "名詞":
            result.append(str[6])
        if tmp[0] == "助詞":
            result.append(str[7])
        if tmp[0] == "動詞":
            result.append(str[7])

        node = node.next

    box = ' '.join(result);
    #print("-------------")
    #print(result)
    #print(box)

    a = []
    a.append(box)
    return a

def TFIDF(train_data,group_data,count,teach_group_data):
    vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
    vecs = vectorizer.fit_transform(train_data)

    model = LinearSVC()
    model.fit(vecs[0:(len(group_data))],group_data)

    num = 0
    mnumber = 0
    while num < count:
        if model.predict(vecs[len(group_data)+num]) != "0":
            mnumber += 1
        num += 1 

    print(mnumber)
    print("train score:",model.score(vecs[0:(len(group_data))],group_data))
    print("test score:",model.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    print(count)

def main():

    sentence = []
    train_data = []
    group_data = []
    teach_data = []
    teach_group_data = []
    count = 0
    num1 = 0

    # fav : "0", rt : "1"                                                                   
    for fav_line in fav_lines:
         if num1+1 <= 10000:
             train_data += word_analysis(fav_line)
             group_data += "0"
             num1 += 1
         else:
            train_data += word_analysis(fav_line)
            teach_group_data += "0"
            count += 1


    num2 = 0
    for rt_line in rt_lines:
        train_data += word_analysis(rt_line)
        group_data += "1"
        num2 += 1
        if num2+1 > 10000:
            break

    print(num1)
    print(num2)
    print(len(group_data))
#    teach_data = []
#    teach_group_data = []
#    count = 0
#    for purpose_line in purpose_lines:
#        train_data += word_analysis(purpose_line)
#        teach_group_data += "1"
#        count += 1
      #  if count > 1000:
      #      break


    a = []
    print()
    a = TFIDF(train_data,group_data,count,teach_group_data)

    

main()
