# coding: utf-8

import pandas as pd

def get_OTHER_spec(grid_file = "./网格分配.xls",SULF_rate = 0.02,HONO_rate = 0.008,NO_rate = 0.9,NOX_rate = 0.1):
    #OTHER内容为SO2,SULF,NH3,CO,HONO,NO,NO2,BENZENE
    file_spe = pd.read_excel(grid_file)

    file = pd.DataFrame()
    file['SO2'] = file_spe['SO2']
    #0.02来自SMOKE含有SULF的均值，后续可能会根据不同的行业修改
    file['SULF'] = file['SO2']*SULF_rate
    file['NH3'] = file_spe['NH3']
    file['CO'] = file_spe['CO']
    ##0.008来自SMOKE含有HONO的均值
    file['HONO'] = file_spe['NOx']*HONO_rate
    file['NO'] = file_spe['NOx']*NO_rate
    file['NO2'] = file_spe['NOx']*NOX_rate
    file['BENZENE'] = 0
    # 输出文件名不变
    file.to_excel('./OTHER_Spec.xlsx',index=None)

if __name__ =='__main__':
    get_OTHER_spec(grid_file = "./网格分配.xls",SULF_rate = 0.02,HONO_rate = 0.008,NO_rate = 0.9,NOX_rate = 0.1)
    print('>------------OTHER Program Completed--------------<')