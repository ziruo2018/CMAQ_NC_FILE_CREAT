# coding: utf-8

###################################################PM行业分类##########################################################
#industry_list = ['电力和热力供应','钢铁','石油化工','水泥工业','焦化','玻璃制造','耐火材料','石墨碳素（炭黑）','干洗',\
                 #'工业锅炉（烧煤）','非工业锅炉','生物质锅炉','民用燃烧','采选及石料加工','冶炼（铝）','冶炼（铜）']
##################################################PM行业分类###########################################################


import pandas as pd
######################################################
# AERO5分配，如果是AER6分配的话需要将PMFINE物种重新的细化 #
######################################################
def get_PM_spec(industry = '工业锅炉（烧煤）', grid_file = './网格分配.xls'):
    file_spe = pd.read_excel(grid_file)
    file_pm25_coefficient = pd.read_excel("./CB05_AERO5_PM25/AERO5_不同行业分配系数.xlsx",index_col='物种')
    # file_pm25_coefficient['工业锅炉（烧煤）']
    #新建DATAFRAME
    file = pd.DataFrame()
    file['PM2_5'] = file_spe['PM2_5']
    file['PM10'] = file_spe['PM10']
    file['PMC'] = file['PM10']-file['PM2_5']
    for name in file_pm25_coefficient[industry].index:
        file[name]=file['PM2_5']*file_pm25_coefficient[industry][name]
    file[['PEC','PMFINE','PNO3','POC','PSO4','PMC']].to_excel('./PM_Spec.xlsx',index=None)

if __name__ == '__main__':
    get_PM_spec(industry = '工业锅炉（烧煤）', grid_file = './网格分配1.xls')
    print('>------------PM Program Completed--------------<')






