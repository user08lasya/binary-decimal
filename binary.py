def binary_to_decimal(binary_str):
    decimal_number = 0
    power = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** power
        power += 1

    return decimal_number

def main():
    binary_str = input("Enter a binary number: ")
    decimal_number = binary_to_decimal(binary_str)
    print(f"The decimal representation of {binary_str} is {decimal_number}")

if __name__ == "__main__":
    main()
