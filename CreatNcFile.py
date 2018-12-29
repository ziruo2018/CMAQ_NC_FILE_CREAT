# coding: utf-8
#Author:Liu


#################################创建空头文件##################################################
# def creat_empty_nc_file(out_file_name = 'out.nc'):#产生空头文件
#     import os
#     if os.path.exists(out_file_name):
#         print('注意：文件'+out_file_name+'已经存在！！！！')
#     else:
#         os.system('ncks -x -v TFLAG,CO,HONO,NO,NO2,ALD2,ALDX,BENZENE, \
# CH4,ETH,ETHA,ETOH,FORM,IOLE,ISOP,MEOH,NVOL,OLE,PAR,TERP,\
# TOL,UNK,UNR,XYL,NH3,SO2,SULF,PEC,PMFINE,PNO3,POC,PSO4,PMC pgt.nc '+out_file_name)
#         print('成功创建'+out_file_name+'空文件!!!!')
# creat_empty_nc_file(out_file_name = 'out.nc')
###############################################################################################



# ###############################给文件赋值#############


import shutil
from netCDF4 import Dataset
shutil.copy('out_base.nc','out.nc')

file1 = Dataset('out.nc','a')


#######################修改维数########################################
#创建TSTEP没有限制的维度
TSTEP = file1.createDimension('TSTEP',None)

DATE_TIME = file1.createDimension('DATE-TIME',2)
LAY = file1.createDimension('LAY',9)#>>>>>生成新文件需修改
VAR = file1.createDimension('VAR',32)#>>>>>生成新文件需修改
ROW = file1.createDimension('ROW',28)#行数#>>>>>生成新文件需修改
COL = file1.createDimension('COL',28)#列数#>>>>>生成新文件需修改
#######################修改维数#########################################


#######################创建变量空间#####################################
#创建TFLAG变量
TFLAG = file1.createVariable('TFLAG','i',('TSTEP','VAR','DATE-TIME',))
TFLAG.units = "<YYYYDDD,HHMMSS>" ;
TFLAG.long_name = "TFLAG" ;
TFLAG.var_desc = "Timestep-valid flags:  (1) YYYYDDD or (2) HHMMSS " 

#创建物种变量及其一些属性值
def creat_nc_variables(spec_name = 'CO',unite = 'moles/s' ):
    spec = file1.createVariable(spec_name,'f',('TSTEP', 'LAY', 'ROW', 'COL',))
    spec.long_name = spec_name
    spec.units = unite
    spec.var_desc = 'Model species '+spec_name

GS_SPECS = ['CO','HONO','NO','NO2','ALD2','ALDX','BENZENE','CH4','ETH','ETHA','ETOH','FORM','IOLE','ISOP','MEOH','NVOL','OLE','PAR','TERP','TOL','UNK','UNR','XYL','NH3','SO2','SULF']
PM_SPECS = ['PEC','PMFINE','PNO3','POC','PSO4','PMC']

# 变量文件名，但不加入数据
for specise in GS_SPECS:
    creat_nc_variables(spec_name = specise, unite = 'moles/s')
for specise in PM_SPECS:
    creat_nc_variables(spec_name = specise, unite = 'g/s')

#######################创建变量空间#####################################################################



#######################给变量赋值（GetSpecBinary.py生成的二进制文件（.npy文件））##########################
#给变量赋值 默认为0
import numpy as np
# arry1 = np.zeros(((25,32,2)))#创建三维空变量（小时数，变量数，DATE-TIME）#值为0
# arry2 = np.zeros((((25,9,28,28))))#创建四维变量（小时数，层数，行数，列数）#值为0
#变量赋值TFLAG
arry1 = np.load("./SPECS/TFLAG.npy")
file1.variables['TFLAG'][:] = arry1

for i in GS_SPECS+PM_SPECS:
    file1.variables[i][:] = np.load("./SPECS/"+i+".npy")
    
#######################给变量赋值（GetSpecBinary.py生成的二进制文件（.npy文件））##########################

######################修改个golabe变量##################################################################
file1.SDATE = 2017215#>>>>>生成新文件需修改
file1.NCOLS = 28#>>>>>生成新文件需修改
file1.NROWS = 28#>>>>>生成新文件需修改
file1.P_ALP = 30.#>>>>>生成新文件需修改
file1.P_BET = 60.#>>>>>生成新文件需修改
file1.P_GAM = 118.3#>>>>>生成新文件需修改
file1.XCENT = 118.3#>>>>>生成新文件需修改
file1.YCENT = 40.#>>>>>生成新文件需修改
file1.NVARS = 32#>>>>>生成新文件需修改
# type(file1.P_GAM)

file1.XORIG = -42000. #ArcGIS渔网确定，可画出渔网后从ArcGIS读取#>>>>>生成新文件需修改
file1.YORIG = -63500. #ArcGIS渔网确定，可画出渔网后从ArcGIS读取#>>>>>生成新文件需修改
file1.XCELL = 3000.#>>>>>生成新文件需修改
file1.YCELL = 3000.#>>>>>生成新文件需修改
file1.GDNAM = "china_27        "#修改GRIDDESC的网格名#>>>>>生成新文件需修改

file1.HISTORY=''
######################修改个golabe变量###################################################################
file1.close()
print('>------------Program Completed--------------<')
