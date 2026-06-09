# anomalib-workshop-202606
Anomalibワークショップの教材です

# 環境条件
* Windows 11
* Python 3.12以上

# セットアップ
## Pythonのインストール
以下URLからPython 3.12.10をダウンロードしてください
https://www.python.org/downloads/windows/

* Download Windows installer (64-bit)

## git clone
本リポジトリをクローンする

PowerShellを起動する（以後```で囲まれた箇所はPowerShellで実行）
```
git clone https://github.com/cm-koga/anomalib-workshop-202606
cd anomalib-workshop-202606
```

Python仮想環境を作成
```
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Pythonパッケージをインストール
```
pip install -r requirements.txt
```

