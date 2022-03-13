import matplotlib.pyplot as plt


def main():
    with open("input.txt", "r") as inputData:
        data = inputData.read()
        x, y = data.split("\n")
        x = list(map(float, x.split(",")))
        y = list(map(float, y.split(",")))

    ty = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
          0.3, 0.3, 0.3]
    plt.plot(x, y, 'o-')
    plt.plot(x, ty, '-', label="Средняя линия")
    plt.title("Контрольная карта Шухарта для контроля погрешностей")
    plt.xlabel("Номер контрольной процедуры")
    plt.ylabel("Результат контрольной процедуры")
    plt.legend()
    plt.grid()
    # plt.show()
    plt.savefig('plot-delta.png')


if __name__ == '__main__':
    main()
