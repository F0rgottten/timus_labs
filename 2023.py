def get_key(d, value):
    for k, v in d.items():
        if value in v:
            return k


boxes = {1: ["Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"],
         2: ["Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"],
         3: ["Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"]}
n = int(input())
res = 0
current_box = 1
for i in range(n):
    post = input()
    box = get_key(boxes, post)
    res += abs(box - current_box)
    current_box = box
print(res)
