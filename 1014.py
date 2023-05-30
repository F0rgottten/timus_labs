def find_q(n):
    if n == 0:
        return 10
    elif n < 10:
        return n
    else:
        q = ""
        for i in range(9, 1, -1):
            while n % i == 0:
                q = str(i) + q
                n //= i
        if n != 1:
            return -1
        else:
            return int(q)


n = int(input())
q = find_q(n)
print(q)
