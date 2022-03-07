def convert_int_to_bin(value):
    """Convert an integer to binary."""
    if value > 1:
        convert_int_to_bin(value // 2)

    print(value%2, end='')


if __name__ == "__main__":
    value = int(input("Digite um número inteiro: "))
    convert_int_to_bin(value)
