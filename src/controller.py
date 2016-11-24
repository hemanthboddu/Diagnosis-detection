import numpy as np

from ui import app
from disease_model import *

assert isinstance(app.Training_data1, list)
Training_data_Category1 = app.Training_data1

assert isinstance(app.Training_data2, list)
Training_data_Category2 = app.Training_data2

feature_dataset = []

for each in range(data_points1):
    feature1_value = feature(Training_data_Category1[each])
    feature_dataset.append((1, feature1_value))

for every in range(data_points2):
    feature2_value = feature(Training_data_Category2[every])
    feature_dataset.append((2, feature2_value))

assert isinstance(app.Patients_dataEntry, list)
patient_feature = feature(app.Patients_dataEntry)

sorted_feature_dataset = sorted(feature_dataset, key=lambda x: x[1])

nearest_value = 0

for near in range(len(sorted_feature_dataset)):
    if patient_feature >= sorted_feature_dataset[near][1]:
        nearest_value = near
        break

abs_nearest_feature = []

for i in range(nearest_value - 5, nearest_value + 6):
    abs_nearest_feature.append(
        (sorted_feature_dataset[i][0], np.abs(sorted_feature_dataset[nearest_value][1] - sorted_feature_dataset[i][1])))

sorted_abs_nearest_feature = sorted(abs_nearest_feature, key=lambda x: x[1])

one_counter = 0

for iterate in range(1, 7):
    if sorted_abs_nearest_feature[iterate][0] == 1:
        one_counter += 1
    else:
        pass

if one_counter > 2:

    diagnosis = " There is a high chance that you are positive"
else:

    diagnosis = " There is a high chance that you are negative"
