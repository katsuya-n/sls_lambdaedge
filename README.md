### 内容

リクエストのuriを書き換える。
"/hello.json"ならそのまま、それ以外の場合は"/not_found.json"にする。


### デプロイ方法

```
$ sls deploy
```

AWSコンソール画面からLambda@Edgeへのデプロイをポチる

### 検討TODOメモ

- IAM Roleの管理はtfではなく、sls側でやったほうが良さそう。最初のインフラ作成時にエラーになりそうな気がする。
- Dockerコンテナを立てて、Pythonを動かしたが方が良い？