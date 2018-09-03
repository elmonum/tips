# Powershell

### 1. ファイルの行数カウント
```
$filepath = './test.csv'
(get-content $filepaht | measure-object -line).lines
```

### 2. 複数ファイルの結合
 headerがない場合
```S
get-content sample/*.csv > sample.txt
```
