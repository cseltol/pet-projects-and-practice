import matplotlib.pyplot as plt

def main():
    with open("input.txt", "r") as inputData:
        data = inputData.read()        
        x, y = data.split("\n")
        x = list(map(float, x.split(",")))
        y = list(map(float, y.split(",")))

    plt.plot(x, y)
    plt.xlabel("Номер контрольной процедуры")
    plt.ylabel("Результат контрольной процедуры")
    plt.show()


if __name__ == '__main__':
    main()
