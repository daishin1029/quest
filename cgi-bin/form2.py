#! /usr/bin/python3
# -*- coding: utf-8 -*-

import cgi # CGIモジュールのインポート
import cgitb
import sys

cgitb.enable() # デバッグに使うので、本番環境では記述しない

form = cgi.FieldStorage() # フォームデータを取得する

print("Content-Type: text/html; charset=UTF-8") # HTMLを記述するためのヘッダ
print("")

A = form.getvalue("text")

def　FB(X):
    def fizzbuzz(i):
        if i > 100 or i < 0:
            return("エラー：0以上100以下の数を入力してください")
        else:
            if i % 15 == 0:
                return("FizzBuzz")
            elif i % 3 == 0:
                return("Fizz")
            elif i % 5 == 0:
                return("Buzz")
            else: 
                return(i)

    if X.isdecimal():
        fizzbuzz(int(X))
    else:
        return("エラー：数字以外の文字を入力しないでください。")

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
'''%(FB(A)) # 入力値の結果を%sの箇所に埋める
print( htmlText.encode("cp932", 'ignore').decode('cp932') )