# coding: utf-8
#author:liu
import pandas as pd
import datetime

year = 2018
month = 12
day = 20
weekday = '周'+str(datetime.date(year,month,day).weekday()+1)
#每月的天数是多少？
month_days = 30

##########################第25个小时的数据，用于模拟的初始#####################
year_25_hour = 2018
month_25_hour = 12
next_day = 21
weekday_25_hour = '周'+str(datetime.date(year,month,day).weekday()+1)
month_days_25_hour = 31
#####################################################################



#########################################月分配###########################################################
month_file = pd.read_excel('./时间分配/月分配.xls',index_col='时间')
month_factor = month_file['分配系数'][str(month)+'月']
#########################################月分配###########################################################



#########################################周分配###########################################################
def get_week_rate_factor(month_days = month_days,year = year,month = month,weekday = weekday):
    week_file = pd.read_excel('./时间分配/周分配.xls',index_col='时间')
    #周分配系数
    ll = [1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7]
    mf = datetime.date(year,month,1).weekday()+1
    #判断本月每天是周几
    yy = ll[mf-1:month_days+7-mf]
#     print(yy)
    week_facrors_list = [week_file['分配系数']['周'+str(i)] for i in yy]
    #求周分配银子的加和
    def get_add(list1 = week_facrors_list):
        num= 0
        for i in list1:
            num=num+i
        return num
    week_factor = week_file['分配系数'][weekday]/get_add()
    return week_factor
#########################################周分配###########################################################


#########################################时分配###########################################################
hour_file = pd.read_excel('./时间分配/时分配.xls',index_col='时间')
hour_factor = hour_file['分配系数']

#########################################时分配###########################################################




hour_list = [str(i)+'时' for i in range(24)]
for hour in hour_list:
    GridFile = pd.read_excel('./网格分配.xls',index_col='FID')#读取年网格分配数据
    GridFile = GridFile*month_factor*get_week_rate_factor()*hour_factor[hour]
    GridFile.to_excel('./网格分配_'+hour+'_.xls',index=None)



###############################第25H数据，下一天的初始条件#################################

GridFile = pd.read_excel('./网格分配.xls',index_col='FID')#读取年网格分配数据
hour_25_hour = get_week_rate_factor(month_days = month_days_25_hour,year = year_25_hour,month = month_25_hour,weekday = weekday_25_hour)
GridFile = GridFile*month_factor*hour_25_hour*hour_factor['0时']
GridFile.to_excel('./网格分配_24时_.xls',index=None)

print('>------------time allocator Program Completed--------------<')


