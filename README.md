# 最強言語AIO
Cの型とRubyの混ぜてスパイスにJavaScriptを隠し味にPythonを加えた言語
## AIOの特徴
複数言語に変換可能

型がある

定数も勿論ある

今までにない~~気持ち悪い~~クールな書き方が可能

セミコンが必須

## チュートリアル
### Hello World
```text
log("Hello");
/*or*/
("Hello");
/*or*/
l"Hello"
```

### 変数
定数にする時は先頭にconst
```text
char s = "Hello"
int age = 10
float num = 13.1

//定数
const char s = "Hello"
const int age = 10
const float num = 13.1
```

### 見にくいコード禁止!
処理は一行に一つ
```text
//bat
log("Hello");("World");

//good
log("Hello");
("World");
```