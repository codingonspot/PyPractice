import re


def classifySwitch(modelNumber):
    if 'C' not in modelNumber:
        print("Invalid model number")

    else:
        str_numerics = re.findall(r'\d+', modelNumber)
        num = list(map(int, str_numerics))
        if num[0] in [5200, 5250, 5270] and num[1] <= 24:
            print(num[1])
            print("Type 1")
        elif num[0] in [5200, 5250, 5270, 5300, 5350, 5370] and num[1] > 24 or num[0] == 5400:
            print(num[1])
            print("Type 2")
        elif "-S" in modelNumber or modelNumber.endswith("X"):
            print(num[1])
            print("Core")
        else:
            print("Invalid model number")


if __name__ == '__main__':
    modelNumber = input("Enter the model number: ")
    classifySwitch(modelNumber)
