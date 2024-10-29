![Static Badge](https://img.shields.io/badge/python-3.11-blue)

# GradeMate
副手採点業務補助システム
## できること
- MD5によるコピーjavaファイルの検出
- javaファイルのpackage宣言一括変更
- DB授業課題の自動採点

## MD5によるコピーjavaファイルの検出
### できること
- コピーが疑われるjavaファイルを検出し、それらのファイルパスをターミナルに表示
- MD5によるハッシュ値が同一＝コードの一字一句が完全に同一である（空白文字とかパッケージ宣言とかも含めて）


## javaファイルのpackage宣言一括変更
### できること
- 指定フォルダ内を再帰的に探索し、現状のディレクトリ構造に対して適切なフォルダ名に一括変更
- javaファイル内のpackageに関する記述の一括変更 　
  → 既存のpackage記述の削除  
  → 授業フォルダをそのままIDEに入れるだけでjavaファイルを動かせるようにpackage宣言を変更
### 使い方
1. python環境の構築
- (mac/venvの例)  
`[YOUR_ENV_NAME]`←好きな名前をつけてね！
```shell
python3 -m venv [YOUR_ENV_NAME]
source [YOUR_ENV_NAME]/bin/activate
```
```py
pip3 install -r requirements.txt
```
- (win/venvの例)  
`[YOUR_ENV_NAME]`←好きな名前をつけてね！  
**powershellの場合**  
PowerShellでのスクリプト実行を許可する（つまりこれは一回だけ実行すればよい）
```shell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
```shell
python -m venv [YOUR_ENV_NAME]
[YOUR_ENV_NAME]\Scripts\activate.ps1
```
```py
pip install -r requirements.txt
```
**コマンドプロンプトの場合**
```shell
python -m venv [YOUR_ENV_NAME]
[YOUR_ENV_NAME]\Scripts\activate.bat
```
2. データの用意
- dataの中に"第01回"の形式のフォルダを全部入れてね．
3. スクリプトの実行
```py
python3 rename_java_package.py
```
4. dataフォルダを見てごらんなさい...





# やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！やったー！

1. python環境の構築(win/venvの例)
`[YOUR_ENV_NAME]`←好きな名前をつけてね！
- powershwllの場合
PowerShellでスクリプトの実行を許可（つまり一回だけ実行すればよい）
```shell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
```shell
python -m venv [YOUR_ENV_NAME]
[YOUR_ENV_NAME]\Scripts\activate.ps1
```
```py
pip install -r requirements.txt
```

## DBの自動採点
### できること
- docxファイルが提出されていれば3点
- excelファイルへの自動一括出力
