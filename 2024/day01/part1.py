def main():
    list1, list2 = [], []

    with open("input.txt") as f:
        for line in f:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))

    list1.sort()
    list2.sort()

    distance = 0

    for a, b in zip(list1, list2):
        distance += abs(a - b)

    print(distance)

if __name__ == "__main__":
    main()