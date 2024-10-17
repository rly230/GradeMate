# compass
副手採点業務補助システム
## javaファイル採点の前処理
### できること
- 指定フォルダ内を再帰的に探索し、なんやかんやで適切なものに一括変更
- javaファイル内のpackageに関する記述の一括変更  
  → 既存のpackageについての記述の削除  
  → 授業フォルダをそのままIDEに入れるだけで動かせるようにjavaファイルのpackage宣言を変更
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
採点対象のフォルダを用意してね．
- /compassに`data`フォルダを用意
```shell
cd path/to/compass
mkdir data
```
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
- docxファイルの自動採点
- excelファイルへの自動一括出力
