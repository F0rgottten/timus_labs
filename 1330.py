import sys #для оптимизации, задачу тормозит input/print
N = int(sys.stdin.readline())
k = []
for i in range(N):
    k.append(int(sys.stdin.readline()))
prefix_sum = [0] * (N + 1)
#вычисляем префиксную сумму
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + k[i - 1]
Q = Q = int(sys.stdin.readline())
for q in range(Q):
    i, j = map(int, sys.stdin.readline().split())
    # используем префиксную сумму для вычисления суммы элементов в диапазоне i..j
    sys.stdout.write(str(prefix_sum[j] - prefix_sum[i - 1]) + '\n')