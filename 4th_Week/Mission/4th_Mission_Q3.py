import pandas as pd

idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"]
data = [[55, 56, 60, 66, 57],
        [64, 77, 71, 79, 67],
        [88, 81, 79, 89, 77],
        [45, 35, 30, 46, 47],
        [91, 96, 90, 97, 99]]

# 위 데이터를 이용해 dataframe을 구성
df = pd.DataFrame(data, index=idx, columns=col)

# df에 새로운 column인 round_6의 데이터 [11, 15, 13, 17, 19] 추가
col_round_6 = pd.Series([11, 15, 13, 17, 19], index=idx)
df["round_6"] = col_round_6
print(df, '\n')

# 각 데이터의 mean, max, min 값을 구해 출력
print(df.describe().loc[["mean", "max", "min"]])