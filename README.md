# wsw
Wall of Sheep for WOWHoneypot

# これは何?
WOWHoneypot のログをベースにした、Wall of Sheep の HTML を作成する Python スクリプトです。アクセスログに含まれる Basic 認証の情報などを抽出して、味気ないログを、カッコよく見せることができます。

# 設定
プログラム中に自由に設定できる項目が2つあります。
- MAX_DISPLAY_NUM: 画面に表示するログの上限です。デフォルトは15になっています。ただしこの数値よりも少ないログしかない場合は、そのログ分だけ表示します。
- DIFFERENT_IP: 表示する IP アドレスに関する設定です。すべて異なる IP アドレスにする場合は True、同じ IP アドレスを許容する場合は False を指定してください。デフォルトは True です。

# 使い方
Python3 で作成し、動作確認をしたスクリプトです。WOWHoneypot のアクセスログが必要です。Apache やその他の一般的な Web サービスのログでは動作しません。
```
$ python3 ./make-wsw.py access_log
```
正常終了した場合、実行したプログラムと同じディレクトリに index.html ファイルが作成されます。このファイルをブラウザで表示すると、Wall of Sheep のような情報を見ることができます。

# 表示される情報
- Attacker IP: 攻撃者の IP アドレスです。
- Target Port: アクセス対象のホストのポート番号です。
- Path: アクセス対象のパスです。
- Account Name: 入力されたアカウント名です。
- Account Password: 入力されたパスワードです。

# At your own risk
改変や機能追加など、ご自由にどうぞ。

## Author
- [morihi-soc.net](https://www.morihi-soc.net/)
- [@morihi_soc](https://twitter.com/morihi_soc)
