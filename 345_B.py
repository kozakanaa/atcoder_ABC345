# モノグサプログラミングコンテスト2024（AtCoder Beginner Contest 345）

# B問題

# 問題文
# -10^(18)以上10^(18)以下の整数Xが与えられるので[X/10]を出力してください。
# ここで[a]はa以上の整数のうち最小のものを意味します

# 制約
# -10^(18)<=X<=10^(18)
# Xは整数

#自分のコード

# def keisan(X):
#     if X >= 0:
#         return (X + 9) // 10
#     else:
#         if X % 10 == 0:
#             return X // 10
#         else:
#             return X // 10 + 1


# X = int(input())
# print(keisan(X))

#review
  # 負の数の場合の条件を分けなきゃと考えているが、最初の(X + 9) // 10 これで全て対応できてる笑
  # 無駄多すぎ
  # 負の数の剰余について全くきちんと考えられていないコード、落ち着いてとこう
  # -1 ÷ 10 = 1 余り9だよ笑笑

# リファクタ

# X = int(input())
# print((X + 9) // 10)

#memo
# 10進数で19桁まで対応できるようにしなければならないので、途中でfloatに変換後、mathモジュールをインポートしmath.ceil()で切り上げると精度不足になる
# print(123456789123456789 / 10)
# 10進数でfloatはpythonだと約15桁程度なので全然足りず不正解になる
# リファクタしたコードはintで計算してるので桁数が足りる
# 切り上げ手法はイディオムとして覚える

import math

def keisan(x):
    return math.ceil(x / 10)
    # else:
    #     tyousei = x // 10
    #     if x % 10 != 0:
    #         tyousei += 1
    #     return tyousei


x = int(input())
print(keisan(x))

