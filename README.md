# Grade2ilearn

自動將 google sheet 中的成績自動匯入到 ilearn

### 設定

```yaml
TA:
  username: # 設定 ilearn 學號，用來登入。
  password: # 密碼

worksheet:
  url: # google sheet 的網址
  title: # 想要匯入的工作表名稱
  start: # 起始欄位 (第一欄需包含學號)
  end: # 結束欄位

course:
  import_url: 'https://ilearn.fcu.edu.tw/grade/import/csv/index.php?id=999999' # 複製該課程匯入成績的網址
```

### 使用

#### 安裝依賴庫
```bash
pip install -r requirements.txt
```

#### 執行
```bash
cd src
python main.py
```