import math
from numpy import log as ln


def my_function():
    file_data = input("Enter file name for data: ").strip()
    with open(file_data, "r") as f:
        read_strings = f.read().splitlines()
        x = list(map(float, read_strings))
    return x


def geometric_function(x):
    g = math.exp(sum(ln(x)) / len(x))
    return g


def main():
    if input("Is it for labs; [y]es [n]o? ").strip() == 'y':
        x = [331.1, 592.8, 649.7, 733.7, 849.3, 961.7, 1054.0, 1140.1, 1149.6, 1191.9, 1260.7, 1337.7, 1466.6, 1604.9,
             1726.1]
    else:
        x = my_function()
    print(geometric_function(x))


if __name__ == "__main__":
    main()
