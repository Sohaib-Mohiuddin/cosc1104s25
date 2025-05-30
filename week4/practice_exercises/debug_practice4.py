def find_max(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    return max

if __name__ == "__main__":
    print(find_max(4, 10, 2))
    print(find_max(7, 3, 9))
    print(find_max(5, 5, 5))