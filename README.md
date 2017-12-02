# aws_lambda_sample

aws lamdaはローカルからコンソールが使えない。   
ファイルをアップロードして使うか、webコンソールから修正するしかない。   




## チュートリアル

### webコンソールからデプロイ

テストイベントの設定を作成し、テストを実行する。   


```:lambda_function.py
import json
    
def lambda_handler(event, context):
    # TODO implement
    return 'Hello from Lambda'

```

ハンドラ情報はファイル名とメソッド名を示す。   
関数コードのハンドラを修正する場合はここを修正する必要がある。

lambda_function.lambda_handler   
[ファイル名].[イベント名]   


### ファイルからアップロード

    cd workspace
    pip install requests -t .
    touch lambda_function.py


```:lambda_function.py
import requests

def lambda_handler(event, context):
    res = requests.get("http://www.yahoo.co.jp/")
    return res.status_code
```

    zip -r upload.zip *



## メモ

ここのライブラリも参考になる   
https://github.com/ryfeus/lambda-packs   

AWS_Lambda_in_Action   
https://github.com/danilop/AWS_Lambda_in_Action

# 参考

https://qiita.com/Hironsan/items/0eb5578f3321c72637b4

