import matplotlib.pyplot as plt


def main():
    with open("input.txt", "r") as inputData:
        data = inputData.read()
        x, y = data.split("\n")
        x = list(map(float, x.split(",")))
        y = list(map(float, y.split(",")))

    mid_line, act_line, warn_line, neg_act_line, neg_warn_line = lines()

    plt.plot(x, y, "o-")
    plt.plot(x, mid_line, "-", label="Средняя линия")
    plt.plot(x, warn_line, "-", label="Линия предупреждение")
    plt.plot(x, neg_warn_line, "-", label="Линия предупреждение отрицательная")
    plt.plot(x, act_line, "-", label="Линия действия")
    plt.plot(x, neg_act_line, "-", label="Линия действия отрицательная")
    plt.title("Контрольная карта Шухарта для контроля внутрилабораторной прецизионности")
    plt.xlabel("Номер контрольной процедуры")
    plt.ylabel("Результат контрольной процедуры")
    plt.legend()
    plt.grid()
    plt.show()
    # plt.savefig('plot-delta.png')


def lines():
    mid = 0.0
    act = 0.11618
    warn = 0.17427
    mid_arr = []
    act_arr = []
    neg_act_arr = []
    warn_arr = []
    neg_warn_arr = []
    for _ in range(0, 25):
        mid_arr.append(mid)
        act_arr.append(act)
        neg_act_arr.append(-act)
        warn_arr.append(warn)
        neg_warn_arr.append(-warn)

    return mid_arr, act_arr, warn_arr, neg_act_arr, neg_warn_arr


if __name__ == '__main__':
    main()
