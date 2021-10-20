
def sort_dict(a):
    return sorted(a.items(), key=lambda x: x[1], reverse=True)


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


def main():
    d = {}
    if input("Is it for labs; [y]es [n]o? ").strip() == 'y':
        with open('data.txt', "r") as f:
            for line in f:
                (key, val) = line.split()
                if key in d:
                    d[key] += int(val)
                else:
                    d[key] = int(val)
    else:
        d = assign_dictionary()
    print(sort_dict(d))


if __name__ == "__main__":
    main()
