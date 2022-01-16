from collections import Counter

dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dict(dict_first, dict_second):
    d = dict(dict_first, **dict_second)


print(merge_dict(dict_first, dict_second))