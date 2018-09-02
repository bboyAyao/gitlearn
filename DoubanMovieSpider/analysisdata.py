import numpy as np

filename = "./Movie.csv"
data_arr = np.loadtxt(filename,
                      delimiter = ",",
                      skiprows=1,
                      dtype=str,
                      usecols=(0,3),
                      encoding="utf-8"
                      )

score_arr = data_arr[:,1]
score_arr = score_arr.astype(np.float64)
print('--------------------------')
print("平均分",np.mean(score_arr))
print('----------------------------')
max_sco = np.max(score_arr)
for each in data_arr[score_arr==max_sco]:
    print("评分最高的电影:",each[0],"评分：",each[1])
print('-----------------------------')
for each in data_arr[score_arr>=9]:
    print("评分大于等于9的电影：",each[0],"评分：",each[1])


