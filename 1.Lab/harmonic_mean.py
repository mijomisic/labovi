def power(my_list):
    return [x ** -1 for x in my_list]


def my_function():
    file_data = input("Enter file name for data: ").strip()
    with open(file_data, "r") as f:
        read_strings = f.read().splitlines()
        x = list(map(float, read_strings))
    return x


def harmonic_mean(x):
    f = power(x)
    return len(f) / sum(f)


def main():
    if input("Is it for labs; [y]es [n]o? ").strip() == 'y':
        x = [100, 120, 90, 70, 100, 90]
    else:
        x = my_function()
    print(harmonic_mean(x))


if __name__ == "__main__":
    main()
