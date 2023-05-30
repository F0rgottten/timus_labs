
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def find_missing_number(s):
    n = len(s)
    pi = prefix_function(s)
    for i in range(n):
        k = pi[i]
        if k > 0 and (i + 1) % (i + 1 - k) == 0:
            m = (i + 1) // (i + 1 - k)
            if str(m) not in s:
                return m
    return n


print(find_missing_number(input()))
