#归一化，标准化
#模型（非树形）有时会对数据的尺度scale很敏感，scale可以决定权重
from sklearn import preprocessing
import numpy as np
X=np.arange(12).reshape(6,2)
min_max_scaler = preprocessing.MinMaxScaler()# 也可以指定范围 feature_range=(-1, 1)
X_=min_max_scaler.fit_transform(X)
print(X,'\n',X_)
#X_的两列数据都以最小值和最大值的相对值为数值

#正态分布(均值为0，标准差为1)
standard_scaler = preprocessing.StandardScaler()
X__=standard_scaler.fit_transform(X)
print(X__)

#或者直接除法公式计算，如在'综合运用.py'内一样