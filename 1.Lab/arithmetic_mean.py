
def my_function():
    file_data = input("Enter file name for data: ").strip()
    with open(file_data, "r") as f:
        read_strings = f.read().splitlines()
        x = list(map(int, read_strings))
    frequency_file = input("Enter frequency file name: ").strip()
    with open(frequency_file, "r") as g:
        read_strings = g.read().splitlines()
        f = list(map(int, read_strings))
    return x, f


def calculate_function(x, f):
    sum_of_frequencies = 0
    sum_of_xf = 0
    if len(x) == len(f):
        for i in range(len(x)):
            sum_of_xf += x[i] * f[i]
            sum_of_frequencies += f[i]
    else:
        print("Files are not the same size")
        exit(1)
    print(sum_of_xf / sum_of_frequencies)


def main():
    if input("Is it for labs; [y]es [n]o? ").strip() == 'y':
        x = [24, 12, 7, 15, 4, 4, 9, 5]
        f = [17000, 6000, 6000, 1000, 5000, 2000, 3000, 1000]
    else:
        x, f = my_function()

    calculate_function(x, f)


if __name__ == "__main__":
    main()
