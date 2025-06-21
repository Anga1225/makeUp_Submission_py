import math

# 設定 x = 1，展開前五項 (從 n=0 到 n=4)
x = 1
n_terms = 5

taylor_sum = 0

for n in range(n_terms):
    term = (x ** n) / math.factorial(n)
    taylor_sum += term

print(f"\nApproximation of e^{x} using {n_terms} terms: {taylor_sum}")
