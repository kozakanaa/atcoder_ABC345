# モノグサプログラミングコンテスト2024（AtCoder Beginner Contest 345）

# A問題

# 問題文
# <, =, > のみからなる文字列Sが与えられます。Sが双方向矢印型の文字列であるか判定してください。
# ただし、文字列Sが双方向矢印型の文字列であるとは、ある正整数kが存在して、
# Sが1個の<、k個の=、1個の>をこの順に連結した長さ(k+2)の文字列であることをいいます。

# 制約
# Sは<, =, >のみからなる長さ3以上100以下の文字列


# 自分のコード

def flag(S):
    if len(S) < 3:
        return "No"
    elif S[0] != "<" or S[-1] != ">":
        return "No"
    else:
        for char in S[1:-1]:
            if char != "=":
                return "No"
        return "Yes"

S = input()
print(flag(S))

# 同じ方向性でリファクタ
  # def flag(S):
  #     return "Yes" if len(S) >= 3 and S[0] == "<" and S[-1] == ">" and all(char == "=" for char in S[1:-1]) else "No"


  # S = input()
  # print(flag(S))

# review
  #and演算子でつながれているため、一行に多くの情報が含まれ、コードが少し読みずらい
  #この程度なら関数を使う必要はないかも
  #ただ世界トップは事前に用意して最速化できるようなコピペformatを用いて関数を使っていた笑
  #all関数が短絡評価を行うため、"=" 以外の文字が中間部分に現れた瞬間に評価が停止するので効率的


# sample_1
  # S = input()
  # k = len(S) - 2
  # T = "<" + "="*k + ">"
  # if S == T:
  #     print("Yes")
  # else:
  #     print("No")

# review
  # 両端が<と>という条件は強いので=の処理をどうシンプルに書くかがポイント
  # =の繰り返しの数を抜き出し、理想の形と現実を照らし合わせるという手法はコードを他社が見ても理解しやすい
  # print("="*3)これで文字の繰り返しができる


# sample_2
  # S = input()
  # print("Yes" if S == "<" + "=" * (len(S) - 2) + ">" else "No")

#review
  # sample_1のリファクタしたかのようなコード
  # 短絡評価も含みかつコードも理解しやすい、競プロという世界では自分が思うベストコード
  # 美しいし、他の問題でも結構使えそう
