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

## サンプルリポジトリの設定
本リポジトリをクローンする

PowerShellを起動する（以後```で囲まれた箇所はPowerShellで実行）
```
git clone https://github.com/cm-koga/anomalib-workshop-202606
cd anomalib-workshop-202606
```

初期設定処理を行う
```
setup.ps1
```

## サンプル画像のダウンロード
以下を実行してサンプル画像（木材データ）をダウンロードします。
```
python .\download_dataset.py
```

以下のようなフォルダ構成になります

```
anomalib-workshop-202606/
  data/
    wood/
      test/
      test_gt/
      train/
```

# サンプルコードの実行前に
サンプルコードを実行する前に、ルートフォルダ（anomalib-workshop-202606フォルダ）に移動し以下を実行してください。

```
.\init.ps1
```

# トラブルシューティング
## ModuleNotFoundError: No module named FrEIA
Pythonスクリプト実行時に表題のエラーメッセージが出たとき、FrEIAを再インストール
```
pip uninstall FrEIA
pip install FrEIA --no-cache-dir --force-reinstall
```
