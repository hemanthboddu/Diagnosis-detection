import numpy as np

# class Training_Data(object):
#    def __init__(self, category):
#        self.category = category

Training_data_Category1 = []
Training_data_Category2 = []

Training_data_parameter1_Category1 = []
Training_data_parameter2_Category1 = []
Training_data_parameter1_Category2 = []
Training_data_parameter2_Category2 = []

data_points1 = len(Training_data_Category1)
data_points2 = len(Training_data_Category2)

for parameters_1 in range(data_points1):
    Training_data_parameter1_Category1.append(Training_data_Category1[parameters_1][0])
    Training_data_parameter2_Category1.append(Training_data_Category1[parameters_1][1])

for parameters_2 in range(data_points2):
    Training_data_parameter1_Category2.append(Training_data_Category2[parameters_2][0])
    Training_data_parameter2_Category2.append(Training_data_Category2[parameters_2][1])

matrix_mean_1 = np.matrix([np.mean(Training_data_parameter1_Category1), np.mean(Training_data_parameter2_Category1)])
matrix_mean_2 = np.matrix([np.mean(Training_data_parameter1_Category2), np.mean(Training_data_parameter2_Category2)])


def CoVariance_Matrix(Training_data_parameter1, Training_data_parameter2):
    x = np.vstack((Training_data_parameter1, Training_data_parameter2))
    k = np.cov(x)

    return k


p_matrix = np.add(CoVariance_Matrix(Training_data_parameter1_Category1, Training_data_parameter2_Category1),
                  CoVariance_Matrix(Training_data_parameter1_Category2, Training_data_parameter2_Category2))


def Optimum_Vector(covar_matrix, mean_matrix1, mean_matrix2):
    mean_matrix_diff = np.subtract(mean_matrix1, mean_matrix2)
    pinv = np.linalg.inv(covar_matrix)
    a = np.matmul(pinv, np.transpose(mean_matrix_diff))
    return a


print Optimum_Vector(p_matrix, matrix_mean_1, matrix_mean_2)
print matrix_mean_2
print matrix_mean_1
print np.subtract(matrix_mean_1, matrix_mean_2)
print np.linalg.inv(p_matrix)
print np.shape(np.subtract(matrix_mean_1, matrix_mean_2))
print np.shape(Optimum_Vector(p_matrix, matrix_mean_1, matrix_mean_2))


def feature(sample_data):
    a_matrix = [Optimum_Vector(p_matrix, matrix_mean_1, matrix_mean_2)[0][0],
                Optimum_Vector(p_matrix, matrix_mean_1, matrix_mean_2)[1][0]]
    y_feature = np.matmul(np.transpose(a_matrix), sample_data)
    return y_feature

# print feature(Training_data_Category2[2])
