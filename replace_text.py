import pandas as pd

df1 = pd.read_csv('log1.csv', index_col=0)
df2 = pd.read_csv('log2.csv', index_col=0)
df = pd.concat([df1, df2],axis=1)
df.head()

cols_original = list(df1.columns) + list(df2.columns)
cols_rename = ['col_' + str(i+1) for i in range(4)]
dic = dict(zip(cols_original, cols_rename))
dic

# テキストの置換
def text_replace(text, dic):
    for original, rename in dic.items():
        text = text.replace(original, rename)
    return text

# テキスト読込
with open('text.txt') as f:
    text = f.read()
replaced_text = text_replace(text, dic)

# テキスト書き込み
with open('new.txt', mode='w') as f:
    f.write(replaced_text)

# カラムの書き換え
