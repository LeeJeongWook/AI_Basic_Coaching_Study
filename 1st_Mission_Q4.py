# ditc형 전역 변수 선언
dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

# dict_first를 기준으로 dict_second에 동일한 key가 있을 경우 value값을 더하고 없을 경우(key, value)를 추가한다
def merge_dict(dict_first, dict_second):
    for i in dict_second.keys():    # dict_second를 key값을 통해 순회(사과 -> 감 -> 배 -> 귤), i = key
        if i in dict_first:     # dict_second의 key값이 dict_first에도 존재할 경우
            dict_first[i] = dict_first.get(i) + dict_second.get(i)  # dict_first[i]의 value = 두 value의 합
        else:   # dict_second의 key값이 dict_first에도 존재할 경우
            dict_first[i] = dict_second.get(i)  # dict_second의 (key, value)를 추가한다

    dict_first = sorted(dict_first.items())     # 과제 답안과 동일하게 만들기(사전순 정렬)위해 정렬
                                                # dict형 변수는 sort()를 사용 할 수 없으므로 sorted()를 사용한다.
                                                # 이 때 dict_first는 dict -> list로 자료형이 바뀐다
    return dict_first   # 결과 리턴

# 그냥 print()할 경우 list 형태로 출력되므로(답안과 동일한 출력을 위해) dict로 자료형 변환 후 출력 한다
print(dict(merge_dict(dict_first, dict_second)))    # merge_dict함수 호출 및 결과 print()