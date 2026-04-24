import re

ans = 0

with open("input.txt") as f:
    muls = re.findall(r'mul\((\d+),(\d+)\)', f.read())
    for mul in muls:
        a, b = map(int, mul)
        ans += a * b

print(ans)
