# aws_lambda_sample

## チュートリアル

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





# 参考

https://qiita.com/Hironsan/items/0eb5578f3321c72637b4

