# モノグサプログラミングコンテスト2024（AtCoder Beginner Contest 345）

# C問題

# 問題文
# 文字列Sが与えられます。次の操作をちょうど1回行った後の文字列としてあり得るものがいくつあるか求めてください。
# Sの長さをNとする。1≤i<j≤Nをみたす整数の組(i,j)を選び、Sのi文字目とj文字目を入れ替える。
# なお、この問題の制約下で操作を必ず行うことができることが証明できます。

# 制約
# Sは英小文字からなる長さ10^(6)以下の文字列

#躓いたところ
# aaddのような(1,3)と(1,4)を重複して数えてしまう点

#

from collections import Counter

S = input()
c = list(Counter(S).values())
ans = 1 if any(x > 1 for x in c) else 0
for i in range(len(c)):
    for j in range(i + 1, len(c)):
        ans += c[i] * c[j]
print(ans)
