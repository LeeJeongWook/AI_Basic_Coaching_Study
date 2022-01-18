num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    new_num_list = []
    for i in num_list:
        if i % 2 != 0:
            new_num_list.append(i)
    return new_num_list     #return 값이 없을 경우 None 출력

print(get_odd_num(num_list))