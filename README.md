# jiken4group1
popular twet trend predictor
 動作環境
    MacOS
 環境構築
    Python 3
    mecab
    tweepy
 tweepy
 
 pip install tweepy
 
 tweepy を使ってツイッターデータを受け取る。
 
 データセット（教師なしデータ）
 
    ツイッターAPIの許可を受け,もらった自分のAccess key(token)を利用してpythonでAPIをもらえる。
    
    ツイッターメッセージを受け取ってくる。受け取ったデータをキーワード欄に
    
    min_favesとmin_retweet を入力してメッセージを受け取る。
    
    (lang :jaで検索すると日本語になるメッセージをもらうのができる。）
    
    
    
 構築方法
 
    Tweet-SVM(BOW).pyでデータセットに受け取る。
    
    SVMとBOWの形態素解析を行なってK近傍法、決定木分類、SVM、路地ステック解析を行う。
    
    その後それぞれの分類のトレーニングデータとテストデータの値を出力している。
 分析方法
 
   K近傍法　：k-近傍法とはデータが入力された時に、それに最も近いk個のデータのラベルで多数決を取る方法です。
   
   決定木分類　：決定木分析とは、YES/NOで答えられる質問で構成された階層的に木構造を学習する方法です。
   
   SVM　：SVMとはクラスの集合環の境界に位置するデータを基準として、距離が最も大きくなるように境界線を引き分類する方法です
   
   路地ステック解析　：ロジスティック回帰分析とは、どのクラスに属するの確率を計算するアプローチです。
   
　実行結果
 
 
 　0.55だけ予測
