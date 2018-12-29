# coding: utf-8

from netCDF4 import Dataset
import numpy as np
import pandas as pd




################################创建空数组及TFLAG变量二进制文件################################
data11 = np.zeros((25,32,1))
data11.dtype = 'int32'
for i in range(24):
    for j in range(32):
        data11[i][j][0]=2017215#>>>>>生成新文件需修改
        data11[i][j][1]=i*10000
for j in range(32):
    data11[24][j][0]=2017216#>>>>>>>生成新文件需修改
    data11[24][j][1]=0
np.save("./SPECS/TFLAG.npy",data11)
################################创建空数组及TFLAG变量二进制文件################################



################################创建空数组及物种变量二进制文件################################
#此处的GS_SPECS数组如果修改，需要修改out.nc空文件，所以一般不做修改（此处没有CL，HCL，SESQ变量需要注意，如果添加需要修改out.nc的变量）
#因为python语言本身的原因（“-”不能用与文件名），所以无法修改
GS_SPECS = ['CO','HONO','NO','NO2','ALD2','ALDX','BENZENE','CH4','ETH','ETHA','ETOH','FORM','IOLE','ISOP','MEOH','NVOL','OLE','PAR','TERP','TOL','UNK','UNR','XYL','NH3','SO2','SULF']
PM_SPECS = ['PEC','PMFINE','PNO3','POC','PSO4','PMC']

#物种每小时生成函数（此处逻辑为：先生成逐小时文件，然后根据逐小时文件生成（25，9，ncols，nrows）文件
def get_specs_each_hour(file = "./SPECS.xlsx" ,specise = 'PAR'):
    file1 = pd.read_excel(file)
    #最下面一层的数组（地面）
    # ?????判断是否是从下往上累加的？（此代码没有判断，后续有时间需要确定一下）
    layer_0 = np.array(file1[specise]).reshape(28,28) #>>>>>>>>>生成新文件需修改
    #生成一个完全是0的空数组
    data = np.zeros(((9,28,28))) #>>>>>>>>>生成新文件需修改
    Zero = np.zeros((28,28)) #>>>>>>>>>生成新文件需修改
    #垂直分层为9层
    data[0]=layer_0
    data[1]=Zero #????有些变量需要修改第二层数据?????
    data[2]=Zero
    data[3]=Zero
    data[4]=Zero
    data[5]=Zero
    data[6]=Zero
    data[7]=Zero
    data[8]=Zero
    return data

#创建25个小时的空数组，用于创建某一变量
data1 = np.zeros((((25,9,28,28))))  #>>>>>>>>>生成新文件需修改

for spec in GS_SPECS+PM_SPECS:
    for i in range(25):#时间循环
        data1[i]= get_specs_each_hour(file = "./SPEC_"+str(i)+".xlsx", specise = spec)

    np.save("./SPECS/"+spec+".npy",data1)
    print(spec+' Have Done')


print('>------------GetSpecBinary Program Completed--------------<')

################################创建空数组及TFLAG变量################################
#np.load("./SPECS/CO.npy").shape

