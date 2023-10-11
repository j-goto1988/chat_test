## 前提条件
Python: 3.11.6
pip:23.2.1（最新バージョン）

## 参考URL
https://self-development.info/%E3%83%81%E3%83%A3%E3%83%83%E3%83%88%E3%83%9C%E3%83%83%E3%83%88%E3%82%92%E4%BD%9C%E3%82%8B%E3%81%9F%E3%82%81%E3%81%ABchatterbot%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99/

## 公式サイト
https://github.com/gunthercox/ChatterBot
https://chatterbot.readthedocs.io/en/stable/

## 環境構築手順
### 1.pytzのインストール
```
pip install pytz
```

### 2.spacyのインストール
下記URLを参考にし、今回はWindowsの例<br>
https://spacy.io/usage
```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download ja_core_news_sm
```

### 3.ChatterBotのインストール
最新バージョンや1.0.5ではエラーで動かないので要注意
```
pip install chatterbot==1.0.4
```

### 4.下記ファイルをダウンロード
https://github.com/gunthercox/chatterbot-corpus/archive/refs/heads/master.zip

### 5.4でダウンロードしたjapaneseフォルダを下記に移動する
japaneseフォルダを下記にコピー
AppData/Local/Programs/Python/Python311/Lib/site-packages/chatterbot_corpus/data

### 6.test.pyを実行すると、下記のエラーがでる
```
AttributeError: module 'time' has no attribute 'clock'
```
#### 修正ファイル
AppData/Local/Programs/Python/Python311/Lib/site-packages/sqlalchemy/util/compat.py
#### 修正前
```py
if win32 or jython:
    time_func = time.clock
else:
    time_func = time.time
```
#### 修正後
```py
if win32 or jython:
    #time_func = time.clock
    try: # Python 3.4+
        preferred_clock = time.perf_counter
    except AttributeError: # Earlier than Python 3.
        preferred_clock = time.clock
else:
    time_func = time.time
```

### 7.test.pyを実行すると、下記のエラーがでる
```
AttributeError: module 'collections' has no attribute 'Hashable'
```
下記を実行する
```
pip install --upgrade PyYaml
```

### 8.test.pyを実行すると、下記のエラーがでる
```
TypeError: load() missing 1 required positional argument: 'Loader'
```
#### 修正ファイル
AppData/Local/Programs/Python/Python311/Lib/site-packages/chatterbot/corpus.py
#### 修正前
```py
return yaml.load(data_file)
```
#### 修正後
```py
return yaml.load(data_file, Loader=yaml.Loader)
```

