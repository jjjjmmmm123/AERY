import numpy as np
import pandas as pd
import random

riasec = ["Realistic", "Investigate", "Artistic", "Social", "Enterprising", "Conventional"]
intelligence = ["Naturalist", "Spatial", "Linguistic", "Intrapersonal", "Bodily-Kinesthetic", "Musical",
                "Logical-mathematical", "Interpersonal"]
grades = ["Math", "English", "Science", "Social Science"]
classes = ["STEM", "ABM", "HUMMS", "GAS"]

labels = riasec + intelligence + grades + ["Class"]
# for riasec and intelligence top three only

total_data = 1020

data = []

for x in range(total_data):
    _riasec = [1, 1, 1, 0, 0, 0]
    _intelligence = [1, 1, 1, 0, 0, 0, 0, 0]
    _grades = [random.randint(80, 100) for _ in range(4)]
    _output = [random.randint(0, 2)]
    random.shuffle(_riasec)
    random.shuffle(_intelligence)
    data.append(_riasec + _intelligence + _grades + _output)

data_numpy = np.asarray(data)
print(data_numpy[3])

# transform in to pandas
# data_dictionary = {}
# for index, label in enumerate(labels):
#     data_dictionary[label] = data_numpy[:, index]
#
# df = pd.DataFrame(data_dictionary)
# print(df)
# df.to_csv('out.csv', index=False)
