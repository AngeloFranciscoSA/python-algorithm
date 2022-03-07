hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
r = []
def convert_int_to_hex(value):
    """Convert an integer to hex."""
    while value > 0:
        print(value % 16)
        r.append(hex[value % 16])
        value = value // 16

    for i in range(len(r)-1, -1, -1):
        print(r[i], end='')

if __name__ == "__main__":
    value = int(input("Digite um número inteiro: "))
    convert_int_to_hex(value)
