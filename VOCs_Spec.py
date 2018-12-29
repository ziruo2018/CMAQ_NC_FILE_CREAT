
# coding: utf-8

import pandas as pd 
import numpy as np
def get_VOCs_spec(industry = "./工艺过程源和溶剂使用/工业生产/燃煤.xlsx",grid_file = './网格分配.xls'):
    file_spe = pd.read_excel(grid_file)
    file_VOCs_coefficient = pd.read_excel(industry,index_col = 'name')

    #自变量MASS为实际每个网格的VOCs排放量
    def get_VOCs_mol_value(MASS = 100):
        #选取VOCs物种列，并生成矩阵
        matrix = file_VOCs_coefficient.iloc[:,2:-2].values
        #转置
        Matrix = matrix.transpose()
        #质量
        mass = MASS*file_VOCs_coefficient['mass percent']
        #摩尔数
        mol_num = np.array([i/j for i ,j in zip(mass,file_VOCs_coefficient['MW'])])
        #VOCs CB05物种摩尔值
        value = np.dot(Matrix,mol_num)
        return value

    #生成目标大小数组
    #len(file['VOCs']) 表示网格数，16，为VOCs的16个物种
    nn = np.zeros(shape=(len(file_spe['VOCs']),16))

    for num,value in enumerate(file_spe['VOCs']):
        nn[num] = get_VOCs_mol_value(MASS = value)
    data = pd.DataFrame(nn,columns=['PAR','OLE','TOL','XYL','FORM','ALD2','ETH','ISOP','MEOH','ETOH','UNR','CH4','ETHA','IOLE','ALDX','TERP'])

    #添加两个物种，纯属无奈之举,因为out.nc文件里面有，gloable变量里面有此数据
    data['NVOL']=0
    data['UNK']=0
    data.to_excel('./VOCs_Spec.xlsx',index=None)

if __name__ == '__main__':
    get_VOCs_spec(industry="./工艺过程源和溶剂使用/工业生产/燃煤.xlsx", grid_file='./网格分配.xls')
    print('>------------VOC Program Completed--------------<')