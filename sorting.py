import os
import csv

from setuptools.dist import sequence


# def read_data(file_name):
#     """
#     Reads csv file and returns numeric data.
#
#     :param file_name: (str), name of CSV file
#     :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
#     """
#     cwd_path = os.getcwd()
#     file_path = os.path.join(cwd_path, file_name)
#     with open(file_path, 'r') as csv_file:
#         reader = csv.reader(csv_file)
#
#         for row in reader:
#             row
#             else:
#                 data[keys] = row
#             row_idx = row_idx + 1
#     return reader

def selection_sort(seznam, direction):
    for i in range(len(seznam)):
        min_idx = i
        for idx in range(i+1,len(seznam)):
            if direction == "ascend":
                if seznam[idx] < seznam[min_idx]:
                    min_idx = idx
            else:
                if seznam[idx] > seznam[min_idx]:
                    min_idx = idx
        seznam[i], seznam[min_idx] = seznam[min_idx],seznam[i]


    return seznam

def bubble_sort(seznam):
    for j in range(len(seznam)-1):
        for i in range(len(seznam)-j - 1):
            a = i
            b =  i+1
            if seznam[a] > seznam[b]:
                seznam[a], seznam[b] = seznam[b],seznam[a]
    return seznam
def main():
    a = bubble_sort([84, 12,17,45,23])
    print(a)

if __name__ == '__main__':
    main()
