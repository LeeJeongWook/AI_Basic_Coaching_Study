inputs = "cat32dog16cow5"

# string 연산을 이용해서 문자열을 자르는 연산을 사용
def find_string(inputs):
    list_result = []    # 결과값으로 반환시킬 비어있는 list_result 생성
    list_result.append(inputs[0:3]) # 문자열 inputs를 인덱스가0~2 영역을 잘라(slice) list_result에 삽입
    list_result.append(inputs[5:8]) # 문자열 inputs를 인덱스가5~7 영역을 잘라(slice) list_result에 삽입
    list_result.append(inputs[10:13]) # 문자열 inputs를 인덱스가10~12 영역을 잘라(slice) list_result에 삽입

    return list_result  # list_result 반환

string_list = find_string(inputs)   # find_string 호출 후 strging_list에 저장
print(string_list)  # 함수의 반환값이 list형 이므로 list형태로 출력됨

'''
# 과제는 문자열 inputs 을 자르는 연산(slice)을 요구했으나 하기 소스코드는
# 임의의 문자열이 입력될 경우 숫자는 삭제하는 방식으로 동작한다

inputs = "15123123adcasc1das151eqdw1563142"
# test inputs = "15123123adcasc1das151eqdw1563142"
def find_string(inputs):
    flag = False # inputs에서 숫자 발견 시  flag = False /] 
    idx_1 = 0   # inputs slice 시작 인덱스
    idx_2 = 0   # inputs slice 끝 인덱스
    list_result = []

    for i in inputs:
        if i.isdigit() and flag:    # isdigit() : 숫자일 경우 + flag = True일 때 
            list_result.append(inputs[idx_1:idx_2])     # inputs를 idx_1 ~ idx_2 영역을 잘라(slice) list_result에 삽입
            idx_1 = idx_2 + 1   # inputs slice 시작 인덱스 초기화(idx_2 + 1, 잘랐던 문자열 다음 인덱스)
            flag = False
        elif i.isdigit() and not flag:  # flag가 Fasle일 경우 앞서 숫자를 만나 문자열은 자른 상태이므로 inputs slice 시작 인덱스 초기화만 한다
            idx_1 = idx_2 + 1           # 그렇지 않을 경우 앞서 slice했던 숫자를 포함한 문자를 입력하게 된다 (Ex. i = 2일 때 'cat3')
        else:
            flag = True # i가 숫자가 아닐 경우 flag를 True로 둔다
        
        idx_2 += 1  # inputs을 순회 하면서 인덱스 값도 증가

    return list_result  # list_result 반환
            
string_list = find_string(inputs)   # find_string 호출 후 strging_list에 저장
print(string_list)  # 함수의 반환값이 list형 이므로 list형태로 출력됨
'''