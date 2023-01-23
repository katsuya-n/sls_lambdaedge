### 内容

リクエストのuriを書き換える。
"/hello.json"ならそのまま、それ以外の場合は"/not_found.json"にする。


### デプロイ方法

```
$ sls deploy
```

AWSコンソール画面からLambda@Edgeへのデプロイをポチる

### 関連リポジトリ

https://github.com/katsuya-n/cloudfront_lambdaedge_s3_tf

### Unit Test

```
$ pip install -U pytest

$ pytest
```
