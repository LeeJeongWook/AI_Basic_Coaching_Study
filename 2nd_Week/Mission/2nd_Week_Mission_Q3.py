# 파일의 경로를 file_path로 설정
# ex) file_path = ".data-01-test-score.csv"

class ReadCSV(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        data_output = []
        with open(self.file_path) as file_data:
            while True:
                data = file_data.readline().strip()
                if not data: break
                data_list = data.split(",")
                data_output.append(data_list)

        return data_output

filepath = "..\Reference\data-01-test-score.csv"
read_csv = ReadCSV(filepath)

print(read_csv.read_file())