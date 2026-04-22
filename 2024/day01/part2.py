def main():
    list1, list2 = [], []

    with open("input.txt") as f:
        for line in f:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))
    
    similarity = 0
    freq = {}

    for a in list1:
        freq[a] = freq.get(a, 0) + 1

    for b in list2:
        similarity += b * freq.get(b, 0)
    
    print(similarity)

if __name__ == "__main__":
    main()