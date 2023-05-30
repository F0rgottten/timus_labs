from collections import Counter

s = input()
print(Counter(s).most_common(1)[0][0])  # нужный элемент
print(Counter(s).most_common(1))
print(Counter(s).most_common(1)[0])
