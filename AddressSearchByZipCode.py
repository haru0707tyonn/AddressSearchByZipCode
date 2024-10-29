import tkinter as tk
import requests
import json

# Tkinterでメインウィンドウを作る基本記述。
canvas = tk.Tk()
#### アプリのサイズを決めている。
canvas.geometry('1000x400')
# タイトルを設定
canvas.title('郵便番号で住所検索')


# 住所入力文字フォント
a = ('Arial black', 40, 'bold')
# 任意の郵便番号を受け取る

# 関数名getWeatherで、上で書いたcanvasを入れる
def getzyuusyo(canvas):
    yuubinbangou = textField.get()
    
    # エンドポイント
    api_endpoint = 'https://zipcloud.ibsnet.co.jp/api/search'    

    # クエリパラメータ
    params = {
        'zipcode' : yuubinbangou,
    }

    # HTTPリクエストを生成
    res = requests.get(api_endpoint, params)


    # 取得したデータを出力
    for result in res.json()['results']:
        add = (result['address1'] + result['address2'] + result['address3'])
        kencode = (result['prefcode'])
        
    final_info = "住所： " + add
    seconddate = '\n' + "都道府県コード： " + kencode
    
    label1.config(text=final_info)
    label2.config(text=seconddate)
# メインウィンドウ示すcanvas, 文字列が中央揃え、 font=aと示すことで、上に書いた文字列を再度書く必要はない。
textField = tk.Entry(canvas, justify='center', width=15, font=a, bg="pink")
# pady=外側の縦の隙間　テキストボックスの余白
textField.pack(pady=30)
# APIの住所、都道府県コードを返す(表示する)　アプリ上で行われるイヴィントを設定することができる。
# bindメソッドを書いて () の因数にreturn, returnするものはgetzyuusyoですと示す
textField.bind('<Return>', getzyuusyo)

label1 = tk.Label(canvas, font=a)
label1.pack()
label2 = tk.Label(canvas, font=a)
label2.pack()


# メインウィインドをアプリに配置してmainloopで動作を待機する。
canvas.mainloop()
