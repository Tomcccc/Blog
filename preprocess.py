import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv("profess.csv")

#数据变换
def convert_currency(d):
    new_value = str(d).replace(",","").replace("$","")
    return float(new_value)

#数据归约
def section(d):
    if 50000 > d:
        return "50000以下"
    if  100000 > d >= 5000:
        return "50000-100000"
    if  d > 100000:
        return "100000以上"


#数据清洗
#处理缺失值
data.dropna(inplace=True)
print(data.isnull().sum())


print(data['Age'].replace(np.NaN,data['Age'].median()))


salaryMean = data['Salary'].apply(convert_currency).mean()
data['Salary'] = data['Salary'].apply(convert_currency).replace(np.NaN,salaryMean)


data['level'] =  data['Salary'].apply(lambda x: section(x))

print(data['level'])


