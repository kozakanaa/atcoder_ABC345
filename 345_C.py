# モノグサプログラミングコンテスト2024（AtCoder Beginner Contest 345）

# C問題

# 問題文
# 文字列Sが与えられます。次の操作をちょうど1回行った後の文字列としてあり得るものがいくつあるか求めてください。
# Sの長さをNとする。1≤i<j≤Nをみたす整数の組(i,j)を選び、Sのi文字目とj文字目を入れ替える。
# なお、この問題の制約下で操作を必ず行うことができることが証明できます。

# 制約
# Sは英小文字からなる長さ10^(6)以下の文字列

#概要
# Sのi文字目とj文字目が違う文字なら、その2文字を入れ替えてできる文字列はSと異なる。
# そのようにして作られる文字列は(i, j)の選び方が違えば異なるものになる。
# なので、大体「Sのi文字目とj文字目が違う文字であるような組(i, j)は何個あるか？」が求められればよい。
# 同じ文字が2つ以上ある場合は自分自身をプラスする

# memo
# atcoderの実行時間は2sec.
# よってpythonでは探索は10^(7)程度が限界らしい(10^(6)くらいまでは安定)
# 異なる{i,j}を全探索すると二重ループで　N*(N+1)/2　回計算　→ Ｏ(N^(2))程度
# よって全探索はできない

# sample_1

# from collections import Counter   <-- Pythonの標準ライブラリの一部であるcollectionsモジュールからCounterクラスをインポート

# S = input()
# c = list(Counter(S).values())
# ans = 1 if any(x > 1 for x in c) else 0   <-- 何か一つでも重複した文字がある場合は1足す
# for i in range(len(c)):   <--　アルファベットの種類、重複のない文字列に置き換えている(最大でも26種類)
#     for j in range(i + 1, len(c)):　 <--　13 * 27　回のループで済む
#         ans += c[i] * c[j] <-- 重複数を考えて計算
# print(ans)

# from collections import Counterについて

# # 文字列内の文字の出現回数をカウントする例
# char_count = Counter("banana")
# print(char_count)  # 出力: Counter({'a': 3, 'n': 2, 'b': 1})

# # リスト内の要素の出現回数をカウントする例
# list_count = Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
# print(list_count)  # 出力: Counter({4: 4, 3: 3, 2: 2, 1: 1})

