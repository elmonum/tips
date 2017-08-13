# 正規表現:see_no_evil:

### メタ文字  
**単一の文字**  
'ABC'.match(/./); //["A"]  
'ABC'.match(/../); //["A", "B"]  
'ABCD'.match(/.D/); //["CD"]  
'ABCD'.match(/../g); //["AB", "CD"]  

**数字**  
A12.match(/\d/); //["1"]  
**数字以外(メタ文字は大文字小文字で意味が逆転)**  
A12.match(/\D/); //["A"]  

**半角英数字とアンダースコア（＿）**  
'Aa1_3'.match(/\w\w_/); //["a1_"]  
**上記以外**  
'A!_'.match(/\W/); //["!"]  

**その他**  
改行：\n, タブ：\t  
空白(半角全角、タブ改行も対象)  
"A B".match(/\s/); [" "]  
空白以外：\S   

### 数量詞を用いた検索  
**先頭 ^**  
'This is a apple'.match(/^This\s../); // ["This is"]  
'This is\nThis is a ball'.match(/^This/gm); //["This", "This"] 改行対象時はmが必要  

**末尾$**  
'This is a apple'.match(/apple$\); // ["apple"]  

**特定の値が後に続いている文字列を検索（先読み）**  
'Java java jaVA jaba'.match(/ja(?=va)/gi); //["Ja", "ja", "ja"]  
**否定先読み（上記の逆）**  
'Java java jaVA jaba'.match(/ja(?!va)/gi); //["ja"]  

**値の繰り返し**  
'javaaaScript'.match(/a{2}/); //["aa"]  
※n回以上[{n,}]、n回以上m回以下[{n,m}]  
**一回以上（{1,}と同じ）**  
'JavaaaScript'.match(/a+/); //["a"]  
**0回以上（{0,}と同じ）**  
'JavaScript'.match(/Javaa*/); //["Java"]  
**0回or1回（存在しないか1回だけ）**  
'http:// https:// httpss://'.match(/https?:\/\/g); //["http://", "https://"]  

**OR検索**
'javascript vbscript'.match(/(java|vb)script/);  
'cat cut can'.match(/ca|ut/g/); //["ca", "cu"] グループ化必須！  

**グループ化**  
:exclamation:グループ化を含む場合、マッチした部分のうちさらにそのグループ化した部分だけを個別に取得する  
'aabbccdd'.match(/ab+c/); //["abbc"]  
'aabbccdd'.match(/a(b+)c/); //["abbc", "bb"]  

#### ブラケット[]による検索  
主に範囲指定  
**いずれかの文字**  
'javascript'.match(/[ac]/g); //["a","a","c"]  
**いずれかの文字以外**  
'java'.match(/[^av]/g); //["j"]  

**指定した範囲の値**  
ハイフンの前後はアスキーコード順となる必要があるため、数字→英大文字→英小文字で記述
'01Ac111'.match(/[A-z]/); //["A", "c"]
**指定した範囲以外**  
'0123abc'.match('/^a-b^2-9/gi'); //["c", "1"]  
:exclamation:文字列「^」として検索される  
'0123abc'.match('/a-b^2-9/gi'); //["a", "b", "2", "3"]

**最長マッチと最短マッチ**  
「+」「*」可能な限り長い文字列にマッチ  
「?」最も短い文字列にマッチ  
var url = 'http://hoge.jp/hoge/fuga/boo/';  
url.match(/^http:\/\/hoge.jp\/(.*)\//); //["http://hoge.jp/hoge/fuga/boo/", "/hoge/fuga/boo/"]  
url.match(/^http:\/\/hoge.jp\/(.*?)\//); //["http://hoge.jp/hoge/","hoge"]  

**後方参照**  
グループ化を含んだパターンを指定した場合、マッチした部分のうちにそのグールプ化した部分だけを個別に取得  
検索:mag:「\n」正規表現内で左から数えてn番目のカッコで囲まれたグループにマッチする文字列  
例：基本的なテーブル内のtrとtd又はtrとthの組み合わせのタグを削除  
html.replace(/<(tr)><(th|td)>.*?<\/\2><\/\1>/g, ''); //"＜table＞＜/table＞"  

置換:pencil2:replace関数の第二引数では「$n」  
例：データの並び替え  
var profile = '1,太郎,2016,山田';  
profile.replace(/^(\d),(.*?),(\d+),(.*?)$/g, '$1,$3',$4,$2); 　//1,2016,山田,太郎  

例：見出しタグを＜h1＞に統一  
html.replace(/<h[2-3]>(.*?)<\/\1>/g, '＜h1＞$2＜/h1＞');  

**特定のパターンを含まない行の検索**  
^(?!*<pattern>).*$  パターンを含まない行を検索  
行の先頭(^)から0文字以上の任意文字列(.*)の後ろに特定のパターン([error])が続く文字列、  
ではないものを否定先読み(?!)かつ最長マッチで検索し、  
さらにそれ以降の行末までの文字列を.*$で検索  
例：[error]を含まない行を空行に変換  
var log =  
'[20160101 19:00:00]' start\n'+  
'[20160102 19:00:00]' error process\n'+　....;  
log.replace(/^(?!.*error).*$/gm, '');  

**備考**  
必須でない　＝　0回以上の繰り返し（.*）
