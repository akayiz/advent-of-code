import re

ans = 0

with open("input.txt") as f:
    memory = "do()" + f.read()
    dos = re.finditer(r'do\(\)', memory)
    dos_positions = []
    for match in dos:
        dos_positions.append(match.start())
    
    donts = re.finditer(r'don\'t\(\)', memory)
    donts_positions = []
    for match in donts:
        donts_positions.append(match.start())

    muls = re.finditer(r'mul\((\d+),(\d+)\)', memory)
    for mul in muls:
        closest_do_idx = max([i for i in dos_positions if i < mul.start()], default=-1)
        closest_dont_idx = max([i for i in donts_positions if i < mul.start()], default=-1)

        if closest_do_idx > closest_dont_idx:
            a, b = int(mul.group(1)), int(mul.group(2))
            ans += a * b

print(ans)
