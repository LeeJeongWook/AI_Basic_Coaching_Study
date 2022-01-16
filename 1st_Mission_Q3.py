score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    for i in range(len(score)):
        print("{0} 번, 평균 : {1}".format(i+1, (score[i][0] + score[i][1]) / 2))

get_avg(score)