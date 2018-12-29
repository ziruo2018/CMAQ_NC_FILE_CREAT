# coding: utf-8

import pandas as pd 
from PM_Spec import get_PM_spec
from VOCs_Spec import get_VOCs_spec
from OTHER_Spec import get_OTHER_spec
for i in range(25):
    file_ending = '_'+str(i)+'时_'
    get_PM_spec(industry='工业锅炉（烧煤）', grid_file='./网格分配'+file_ending+'.xls')
    print('>------------PM Program Completed--------------<')
    get_VOCs_spec(industry="./工艺过程源和溶剂使用/工业生产/燃煤.xlsx", grid_file='./网格分配'+file_ending+'.xls')
    print('>------------VOC Program Completed--------------<')
    get_OTHER_spec(grid_file='./网格分配'+file_ending+'.xls', SULF_rate=0.02, HONO_rate=0.008, NO_rate=0.9, NOX_rate=0.1)
    print('>------------OTHER Program Completed--------------<')


    file_1 = pd.read_excel("./PM_Spec.xlsx")
    file_2 = pd.read_excel("./VOCs_Spec.xlsx")
    file_3 = pd.read_excel("./OTHER_Spec.xlsx")
    file_together = pd.concat([file_1,file_2,file_3],axis=1)

    file_together.to_excel('./SPEC_'+str(i)+'.xlsx',index=None)

print('>------------together Program Completed--------------<')
