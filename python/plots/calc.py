import math

t_pf = 2.3646 # коэф. Стьюдента
P = 0.95
q_tab = 0.55 # при N = 8
F_crit = 3.79 # критерий Фишера

firstRow = sorted([1.02, 1.02, 1.01, 1.03, 1.00, 1.03, 1.02, 1.01])
secondRow = sorted([1.02, 1.00, 1.02, 1.03, 1.03, 1.02, 1.03, 1.02])

# firstRow = sorted([4.85, 4.85, 4.85, 4.85, 4.82, 4.83, 4.86, 4.84])
# secondRow = sorted([4.83, 4.81, 4.82, 4.85, 4.95, 4.85, 4.85, 4.86])

# tasky = [
#     79.20, 79.25, 79.30, 79.35, 79.40, 79.45, 79.50, 79.55,
#     79.60, 79.65, 79.70, 79.80, 79.85, 79.90, 79.95, 80.00,
#     80.05, 80.10, 80.15, 80.20, 80.25, 80.30, 80.35, 80.40,
#     80.45, 80.50, 80.55, 80.60, 80.65, 80.70, 80.75, 80.80,
# ]
# ms = [1, 1, 1, 1, 2, 2, 2, 3, 2, 3, 3, 7, 5, 4, 3, 6, 5, 5, 6, 4, 4, 5, 4, 3, 3, 3, 2, 2, 3, 1, 2, 2]

# def task_5():
#     v_avg = 80.05
#     for i in tasky:
#         for j in ms:
#             std_diff = math.sqrt(((i - v_avg) ** 2) * j / 99)
#     print(std_diff)

    # sum_st = 0
    # for i in tasky:
    #     for j in ms:
    #     sum_st = (i - v_avg)**2 * j

    # std_dif = sum_st

def main():
    # task_5()
    print(f'{firstRow=}\n{secondRow=}', end='\n\n')
    
    q_min = abs((firstRow[0] - firstRow[1])) / abs((firstRow[-1]) - firstRow[0])
    q_max = abs((firstRow[-2] - firstRow[-1])) / abs((firstRow[-1]) - firstRow[0])
    print(f'{q_min=};\n{q_max=};', end='\n\n')
    

    bl = q_tab > q_min and q_tab > q_max
    x_firstRow_avg = 0
    if bl:
        inner = 0
        for i in firstRow:
            inner += i
        x_firstRow_avg = inner / len(firstRow)

    print(f'{x_firstRow_avg=}', end='\n\n')


    despr_out_fisrtRow = []
    for i in firstRow:
        x = abs((i - x_firstRow_avg) ** 2)
        despr_out_fisrtRow.append(x)

    despr_firstRow = sum(despr_out_fisrtRow) / (len(firstRow)-1)
    print(f'{despr_firstRow=}', end='\n\n')

    std_diff_firstRow = math.sqrt(despr_firstRow)
    print(f'{std_diff_firstRow=}', end='\n\n')

    std_diff_avg_firstRow = despr_firstRow / math.sqrt(len(firstRow))
    print(f'{std_diff_avg_firstRow=}', end='\n\n')

    trusted_interval_firstRow = (t_pf * despr_firstRow) / math.sqrt(len(firstRow))
    print(f'{trusted_interval_firstRow=}', end='\n\n')


    q_min_2 = abs((secondRow[0] - secondRow[1])) / abs((secondRow[-1]) - secondRow[0])
    q_max_2 = abs((secondRow[-2] - secondRow[-1])) / abs((secondRow[-1]) - secondRow[0])
    print(f'{q_min_2=};\n{q_max_2=};', end='\n\n')

    bl_2 = q_tab > q_min_2 and q_tab > q_max_2
    x_secondRow_avg = 0
    if bl_2:
        inner = 0
        for i in secondRow:
            inner += i
        x_secondRow_avg = inner / len(secondRow)
    print(f'{x_secondRow_avg=}', end='\n\n')

    despr_out_secondRow = []
    for i in secondRow:
        x = abs((i - x_secondRow_avg) ** 2)
        despr_out_secondRow.append(x)

    despr_secondRow = sum(despr_out_secondRow) / (len(secondRow)-1)
    print(f'{despr_secondRow=}', end='\n\n')

    std_diff_secondRow = math.sqrt(despr_secondRow)
    print(f'{std_diff_secondRow=}', end='\n\n')

    std_diff_avg_secondRow = despr_secondRow / math.sqrt(len(secondRow))
    print(f'{std_diff_avg_secondRow=}', end='\n\n')

    trusted_interval_secondRow = (t_pf * despr_secondRow) / math.sqrt(len(secondRow))
    print(f'{trusted_interval_secondRow=}', end='\n\n')

    F_test(despr_firstRow, despr_secondRow, x_firstRow_avg, x_secondRow_avg)


def F_test(despr_1, despr_2, x_firstRow_avg, x_secondRow_avg):
    print('\n///// F-Test /////\n')
    f = despr_1 / despr_2
    avg_weighted_of_desprs = 0
    t_exp = 0
    if f > F_crit:
        print(f'Большое расхождение между дисперсиями: {f=} < {F_crit=}')
        return
    else:
        avg_weighted_of_desprs = ((len(firstRow)-1) * (despr_1 ** 2)) + ((len(firstRow)-1) * (despr_2 ** 2)) / len(firstRow) + len(secondRow) + 2
        s_avg_weighted_declining = math.sqrt(avg_weighted_of_desprs)
        t_exp = (abs(x_firstRow_avg - x_secondRow_avg) / avg_weighted_of_desprs) * math.sqrt((len(firstRow) * len(secondRow)) / (len(firstRow) + len(secondRow)))

        if t_exp > t_pf:
            print(f'Большое расхождение между средними X: {f=} < {F_crit=}')
            print(f'\t{f=}\n\t{avg_weighted_of_desprs=}\n\t{t_exp=}\n\t{t_exp=}\n')
            return
    print(f'Все услвоия сходяться:\n \t{f=}\n\t{avg_weighted_of_desprs=}\n\t{t_exp=}\n')


if __name__ == '__main__':
    main()
  
