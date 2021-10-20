
def assign_dictionary():
    file_data = input("Enter file name for data: ").strip()
    a = {}
    with open(file_data, "r") as f:
        for line in f:
            (key, val) = line.split()
            if key in a:
                a[key] += int(val)
            else:
                a[key] = int(val)
    return a


def median_func(a):
    total = sum(a.values())
    d = {}
    for key in a:
        d[key] = a.get(key) / total
    res_key = min(d.items(), key=lambda x: abs(0.5 - x[1]))
    print(res_key)


def main():
    if input("Is it for labs; [y]es [n]o? ").strip() == 'y':
        x = {'1h': 15, '2h': 38, '3h': 50, '4h': 150, '5h': 302, '6h': 200, '7h': 81, '8h': 30,
             '9h': 26, '10h': 20, '11h': 15,
             '12h': 18, '13h': 14, '14h': 9, '15h': 7, '16h': 6, '17h': 8}
    else:
        x = assign_dictionary()
    median_func(x)


if __name__ == "__main__":
    main()
