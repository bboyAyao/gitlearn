import numpy as np
import datetime


'''
现有一份期货交易的盈利亏损记录表（csv格式，见gain_and_los表格），每条记录均为单次的盈亏记录。
计算最大盈利（数值）、
最大亏损（数值）、
最大盈利时间（时间）、
最大亏损时间（时间）、
最大持续盈利次数（数值）、
最大持续盈利时间（时间段）、
最大持续亏损次数（数值）、
最大持续亏损时间（时间段）。
'''

filename = "./gain_and_loss.csv"
data_arr = np.loadtxt(filename,
    delimiter = ",",#按，分割
    skiprows = 1, #跳过第一行
    dtype=str,
    usecols = (0,1),
    encoding='utf-8'
    )

#抽取盈亏数据
float_money = data_arr[:,1].astype(np.float64)
max_gain = np.max(float_money)
max_loss = np.min(float_money)
print("最大盈利：",max_gain)
print("最大盈利时间：",data_arr[:,0][float_money == max_gain][0])
print("最大亏损：",max_loss)
print("最大亏损时间：",data_arr[:,0][float_money == max_loss][0])
print('-----------------------------')

print(data_arr)

#初始化
gain_num=0
loss_num=0
gain_temp = 0
loss_temp = 0
total_gain_days = 0
total_loss_days = 0
start_loss_time = ''
start_gain_time = ''
alist = {}

for each_sub in range(len(float_money)):
    if float_money[each_sub] > 0:
        # 盈利开始时间
        if gain_temp == 0:
            start_gain_time = data_arr[:, 0][each_sub]
        if start_loss_time != '':
            #最大亏损时间计算
            start_loss_date = datetime.datetime.strptime(str(start_loss_time), '%Y-%m-%d')
            end_loss_time = data_arr[:, 0][each_sub - 1]
            end_loss_date = datetime.datetime.strptime(str(end_loss_time), '%Y-%m-%d')
            total_date_loss_temp = (end_loss_date - start_loss_date).days
            # print("亏损", start_loss_time, end_loss_time)
            # print("亏损天数", total_date_loss_temp)
            # print('---------------------------------')

            # 存储最大持续亏损时间
            if total_loss_days < total_date_loss_temp:
                total_loss_days = total_date_loss_temp
                alist['start_loss_time'] = start_loss_time
                alist['end_loss_time'] = end_loss_time
            start_loss_time = ''

        #最大盈利次数计数：
        gain_temp += 1
        if loss_temp  > loss_num:
            loss_num = loss_temp

        loss_temp = 0
    else:
        # 亏损开始时间
        if loss_temp == 0:
            start_loss_time = data_arr[:, 0][each_sub]
        if start_gain_time != '':
            #最大盈利时间计算
            start_gain_date = datetime.datetime.strptime(str(start_gain_time), '%Y-%m-%d')
            end_gain_time = data_arr[:, 0][each_sub-1]
            end_gain_date = datetime.datetime.strptime(str(end_gain_time), '%Y-%m-%d')
            total_date_gain_temp = (end_gain_date - start_gain_date).days
            # print("盈利", start_gain_time, end_gain_time)
            # print("盈利天数", total_date_gain_temp)
            # print('-----------------------------')

            #存储最大持续盈利时间
            if total_gain_days < total_date_gain_temp:
                total_gain_days = total_date_gain_temp
                alist['start_gain_time'] = start_gain_time
                alist['end_gain_time'] = end_gain_time
            start_gain_time = ''

        #最大亏损次数计数
        loss_temp += 1
        if gain_temp > gain_num:
            gain_num = gain_temp

        gain_temp = 0

print('最大持续盈利次数：',gain_num)
print('最大持续盈利开始时间：',alist['start_gain_time'])
print('最大持续盈利结束时间：',alist['end_gain_time'])
print("盈利总时长：",total_gain_days)
print('-----------------------------')
print('最大持续亏损次数：',loss_num)
print('最大持续亏损开始时间：',alist['start_loss_time'])
print('最大持续亏损结束时间：',alist['end_loss_time'])
print("亏损总时长：",total_loss_days)
