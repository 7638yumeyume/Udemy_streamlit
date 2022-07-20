# 実装するWebアプリ本文
import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("プレグレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)
 
"Done!!"
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

#実施したコード
#import streamlit as st
#import time
#import numpy as np
#import pandas as pd
#from PIL import Image

#st.title("Streamlit 超入門") # "Streamlit 超入門"という文をstreamlitでタイトルとして表示する

    #st.write("DataFrame") # "DataFrame"という文をstreamlitで本文として表示する

        # データセットの作成
            #df = pd.DataFrame({
            #    "1列目" : [1, 2, 3, 4],
            #    "2列目" : [10, 20, 30, 40]
            #})　# DataFrameを使って表データを作成

            #st.dataframe(df.style.highlight_max(axis=0)) #dfで定義した表をstreamlitで表示

        # グラフの作成
            #df = pd.DataFrame(
            #    np.random.rand(20, 3),
            #    columns=["a", "b", "c"]
            #) # pdで乱数を獲得してそれぞれa,b,cの項に追加する

            #st.line_chart(df) # dfで獲得した乱数をチャートグラフで表示する
            #st.area_chart(df)  # エリアチャート
            #st.bar_chart(df) #棒チャート

        # マッピング関数
            #df = pd.DataFrame(
            #    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
            #   columns=["lat", "lon"]
            #) # pdで乱数を獲得して新宿付近の緯度経度として利用

            #st.map(df) 

        # """で文字を表示する
        # #を複数使用することで文字の大きさが変わる
        # ```を使うことでコードとして表示できる 
            #"""

            # 章
            ## 節
            ### 項

            #```python
            #import streamlit as st
            #import numpy as np
            #import pandas as pd
            #```

            #"""

    #st.write("Display Image") # "Display Image"という文をstreamlitで本文として表示する

        # selectboxの作成
            #option = st.selectbox(
            #    "あなたの好きな数字を教えてください。",
            #    list(range(1,11)) #選択肢の作成(rangeを用いて1~10)

            #)
            #"あなたの好きな数字は、", option, "です。" #出力

        #if st.checkbox("Show Image"): #チェックBoxを追加して画像の表示・非表示の切り替えができるようにする
            # 画像データの表示
                #img = Image.open("SpaceCat.jpeg")
                #st.image(img, caption="宇宙猫", use_column_width=True)


    #st.write("Interactive Widgets") # "Interactive Widgets"という文をstreamlitで本文として表示する

        #テキストとスライドバー
            #text = st.text_input("あなたの趣味を教えてください。") #入力boxを作成
            #"あなたの趣味:", text

            #condition = st.slider("あなたの今の調子は？", 0, 100, 50) #スライドバーを作成(数字は最小値、最大値、デフォルト値の順)
            #"コンディション:", condition

        # テキストとスライドバーをサイドバーで表示
            #text = st.sidebar.text_input("あなたの趣味を教えてください。")
            #condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)

            #"あなたの趣味:", text
            #"コンディション", condition

        #左右で表示させる

            #left_column, right_column = st.columns(2) #左右で2分割のcolumnを作成
            #button = left_column.button("右カラムに文字を表示") #ボタンを作成
            #if button:
            #    right_column.write("ここは右カラムです") #ボタンを押すと右カラムに"ここは右カラムです"と表示されるif文

        # expanderでタブを作成(使用例:Q&Aなど)
            #expander1 = st.expander("問い合わせ1")
            #expander1.write("問い合わせ1の回答")
            #expander2 = st.expander("問い合わせ2")
            #expander2.write("問い合わせ2の回答")
            #expander3 = st.expander("問い合わせ3")
            #expander3.write("問い合わせ3の回答")

    #st.write("プレグレスバーの表示") # "プレグレスバーの表示"という文をstreamlitで本文として表示する
    #"Start!!"

    # プレグレスバーを作成
        #latest_iteration = st.empty()
        #bar = st.progress(0)

        #for i in range(100):
        #    latest_iteration.text(f"Iteration {i + 1}")
        #    bar.progress(i + 1)
        #    time.sleep(0.1)
        
        #"Done!!"
    # プレグレスバーが100になった段階で先に作成したbuttonとexpanderを表示する
    # buttonの処理は再度プレグレスバーが作動する
        #left_column, right_column = st.columns(2)
        #button = left_column.button("右カラムに文字を表示")
        #if button:
        #    right_column.write("ここは右カラムです")

        #expander1 = st.expander("問い合わせ1")
        #expander1.write("問い合わせ1の回答")
        #expander2 = st.expander("問い合わせ2")
        #expander2.write("問い合わせ2の回答")
        #expander3 = st.expander("問い合わせ3")
        #expander3.write("問い合わせ3の回答")