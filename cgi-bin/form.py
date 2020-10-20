#! /usr/bin/python3
# -*- coding: utf-8 -*-

import cgi # CGIモジュールのインポート
import cgitb
import sys

cgitb.enable() # デバッグに使うので、本番環境では記述しない

form = cgi.FieldStorage() # フォームデータを取得する

print("Content-Type: text/html; charset=UTF-8") # HTMLを記述するためのヘッダ
print("")

def fizzbuzz(i):
    try:
        I = int(i)
        if I > 100 or I < 0:
            return("エラー：0以上100以下の数を入力してください")
        else:
            if I % 15 == 0:
                return("FizzBuzz")
            elif I % 3 == 0:
                return("Fizz")
            elif I % 5 == 0:
                return("Buzz")
            else: 
                return(I)
    except ValueError:
        return("エラー：数字以外の文字を入力しないでください。")

A = form.getvalue("text")

htmlText = '''
<!DOCTYPE html>
<html>
    <head><meta charset="shift-jis" /></head>
    <h1>FizzBuzzの結果</h1>
    <p>&nbsp; %s<br/></p>
    <hr/>
    <a href="../index.html">BACK</a>　
</body>
</html>
'''%(fizzbuzz(A)) # 入力値の結果を%sの箇所に埋める
print( htmlText.encode("cp932", 'ignore').decode('cp932') )

