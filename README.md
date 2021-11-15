# Log

- ログレベル
  - debug
  - info
  - warn
  - error
  - critical

- 設定ファイル

  settings.jsonをLogディレクトリ直下に作成
  ```json
  {
    "MODE": "dev",
    "TEST": {
      "FILE": "test.log"
    }
  }
  ```
  
  MODE: MODEをdevにするとログレベルがdebugになる。それ以外を入れるとinfoレベルになる

  上記のTESTの部分: 各ログファイルのセクション<br>
  ex) aaa.py, bbb.pyで実行したログを分けて出力したい場合
  ```json
  {
    "MODE": "",
    "aaa": {
      "FILE": "aaa.log"
    },
    "bbb": {
      "FILE": "bbb.log"
    }
  }
  ```

  FILE: ログファイル出力先