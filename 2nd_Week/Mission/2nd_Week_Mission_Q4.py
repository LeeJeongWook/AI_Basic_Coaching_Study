# 파일의 경로를 file_path로 설정
# ex) file_path = ".data-01-test-score.csv"

import string

class ReadCSV(object):
    read_data = []
    merge_data = []
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path) as file_data:
            while True:
                data = file_data.readline().strip()
                if not data: break
                data_list = list(map(int, data.split(",")))
                ReadCSV.read_data.append(data_list)
        return ReadCSV.read_data
    
    def merge_list(self):
        for i in ReadCSV.read_data:
            ReadCSV.merge_data.append(sum(i))
        return ReadCSV.merge_data

filepath = "..\Reference\data-01-test-score.csv"
read_csv = ReadCSV(filepath)

print(read_csv.read_file())
print(read_csv.merge_list())