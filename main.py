from math import sqrt

#  Topsis function

def Topsis_solution(names_array, source_matrix, weightage_array, assesment_array):

    squared_quadro_sum = 0
    source_matrix_len = len(source_matrix)
    column_len = len(source_matrix[0])
    final_array = []
    final_array.append(names_array)
    P_array = []

    #  normalizing
    for column in range(source_matrix_len):
        for elem in range(column_len):
            squared_quadro_sum += source_matrix[column][elem] ** 2
        for elem in range(column_len):
            source_matrix[column][elem] /= sqrt(squared_quadro_sum)
        squared_quadro_sum = 0
    #  applying weghts
    iter = 0
    for column in range(source_matrix_len):
        for elem in range(column_len):
            source_matrix[column][elem] *= weightage_array[iter]
        iter+= 1

    #  creating ideal values arrays
    ideal_best = []
    ideal_worst = []
    for column in range(0, len(source_matrix)):
        if assesment_array[column] == 1:
            ideal_best.append(max(source_matrix[column]))
            ideal_worst.append(min(source_matrix[column]))
        elif assesment_array[column] == 0:
            ideal_best.append(min(source_matrix[column]))
            ideal_worst.append(max(source_matrix[column]))

    #  calculating S's and P's:


    for row in range(column_len):
        sum_S_plus = 0
        sum_S_minus = 0
        for column in range(source_matrix_len):
            sum_S_plus += (source_matrix[column][row] - ideal_best[column])**2
            sum_S_minus += (source_matrix[column][row] - ideal_worst[column])**2

        sum_S_plus  = sum_S_plus**(1/2)
        sum_S_minus = sum_S_minus**(1/2)
        P_array.append((sum_S_minus)/((sum_S_plus+sum_S_minus)))

    #final_array.append(P_array)
    final_ranking_list = dict(zip(names_array, P_array))
    final_ranking_list = {k: final_ranking_list[k] for k in sorted(final_ranking_list, key = final_ranking_list.get, reverse=True)}
    return final_ranking_list


# На вход, массив имен, матрица столбцов показателей характеристик, массив весов, массив значения характеристики (1-больше лучше, 0 - меньше лучше)
print(Topsis_solution(["Phone1", "Phone2", "Phone3", "Phone4", "Phone5"], [[250,200,300,275,225],[16,16,32,32,16], [12,8,16,8,16], [5,3,4,4,2]],
                      [0.25, 0.25, 0.25, 0.25], [0, 1, 1, 1]))


