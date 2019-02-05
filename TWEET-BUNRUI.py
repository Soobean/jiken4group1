from os import path
import MeCab
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

current_dir = path.dirname(__file__)
# ファボに関するファイル読み込み
fav_text = open('fav5.txt', 'r')
fav_lines = fav_text.read().split('|')

# リツイートに関するファイル読み込み
rt_text = open('rt5.txt', 'r')
rt_lines = rt_text.read().split('|')

#purpose_text = open('10000rt.txt', 'r')
#purpose_lines = purpose_text.read().split('|')

# Mecabによって品詞の種類を調べ、リストを作成する
def word_analysis(word):

    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(word)

    result = []
    
    # リストを作成する
    while node:
        str = node.feature.split(',')
        tmp = str[0].split(',')
        if tmp[0] == "名詞":
            result.append(str[6])
        if tmp[0] == "助詞":
            result.append(str[7])
        if tmp[0] == "動詞":
            result.append(str[7])
        if tmp[0] == "副詞":
            result.append(str[7])
        if tmp[0] == "形容詞":
            result.append(str[8])
        if tmp[0] == "助動詞":
            result.append(str[8])
        node = node.next

    box = ' '.join(result);

    a = []
    a.append(box)
    return a

# 先ほど作成したリストをベクトル化し、分類にかける
def TFIDF(train_data,group_data,count,teach_group_data):
    # TFIDFによってベクトル化する
    vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
    vecs = vectorizer.fit_transform(train_data)

    # K-NN
    model1 = DecisionTreeClassifier()
    model1.fit(vecs[0:(len(group_data))],group_data)

    # SVM
    model2 = LinearSVC()
    model2.fit(vecs[0:(len(group_data))],group_data)

    # LOGISTIC
    model3 = LogisticRegression()
    model3.fit(vecs[0:(len(group_data))],group_data)
    
    # TREECLASS
    model4 = DecisionTreeClassifier(max_depth=3)
    model4.fit(vecs[0:(len(group_data))],group_data)

    # MLPClassは学習の処理が重いため、データ数を減らして行う必要がありそう                                                                   
    #model5 = MLPClassifier(solver="sgd",random_state=0,max_iter=5)
    #model5.fit(vecs[0:(len(group_data))],group_data)

    # 以下はそれぞれの正解率の表示
    #print("K-NN train score:",model1.score(vecs[0:(len(group_data))],group_data))
    print("K-NN test score:",model1.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    #print("SVM train score:",model2.score(vecs[0:(len(group_data))],group_data))
    print("SVM test score:",model2.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    #print("LOGISTIC train score:",model3.score(vecs[0:(len(group_data))],group_data))
    print("LOGISTIC test score:",model3.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    #print("TREECLASS train score:",model4.score(vecs[0:(len(group_data))],group_data))
    print("TREECLASS test score:",model4.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    #print("MLPCLASS train score:",model4.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))                                         
    #print("MLPECLASS test score:",model5.score(vecs[(len(group_data)):(len(group_data)+count)],teach_group_data))
    print(count)

def main():

    sentence = []
    train_data = []
    group_data = []
    teach_data = []
    teach_group_data = []
    count = 0
    num1 = 0
    
    # グループを０と１で分ける
    # fav : "0", rt : "1"     
    # 以下はファボのファイルを品詞ごとに分け、リストを作成している
    for fav_line in fav_lines:
         if num1+1 <= 13000:
             train_data += word_analysis(fav_line)
             group_data += "0"
             num1 += 1
         else:
             #train_data += word_analysis(fav_line)
             #teach_group_data += "0"
             #count += 1
             break

    num2 = 0
    # 以下はリツイートのファイルを品詞ごとに分け、リストを作成している
    for rt_line in rt_lines:
        if num2+1 <= 13000:
            train_data += word_analysis(rt_line)
            group_data += "1"
            num2 += 1
        else:
            #train_data += word_analysis(rt_line)
            #teach_group_data += "1"
            #count += 1
            break

    print(num1)
    print(num2)
    print(len(group_data))

    # 以下はファボのテストデータ作成している
    for purpose_line in fav_lines[13000:]:
        train_data += word_analysis(purpose_line)
        teach_group_data += "0"
        count += 1
        if count >= 1000:
            break

    # 以下はリツイートのテストデータ作成している
    for purpose2_line in rt_lines[13000:]:
        train_data += word_analysis(purpose2_line)
        teach_group_data += "1"
        count += 1
        if count >= 2000:
            break

    a = []
    print()
    # 最後にベクトル化し、分類にかける
    a = TFIDF(train_data,group_data,count,teach_group_data)

    

main()
