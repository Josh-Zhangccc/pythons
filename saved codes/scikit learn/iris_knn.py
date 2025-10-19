from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
#knn是k近邻算法，适合分类和回归，核心思想是：对于一个新的数据点，找到距离它最近的k个点，看看这k个点中哪个类别最多，就把这个新数据点分到哪个类别
#物以类聚
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt
#数据拆分

iris=load_iris()
#iris是sklearn里的bunch对象，可以用法bunch.key来访问，也可以像dict一样用dict['key']
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#random_state是随机种子，填入固定值后可以保证每一次的拆分结果都一样
#test_size是测试集所占的比例
'''!无论用bunch,list,还是dataframe,最后train_test_split函数都会转化为numpy.array'''
accuracy=[]
#开始训练
for k in range(1,20):
    knn=KNeighborsClassifier(n_neighbors=k)#n_neighbors是k值,默认值是5,作用是选择距离最近的k个点
    knn.fit(X_train,y_train)#训练

#开始预测+评估
    y_pred=knn.predict(X_test)
    a=knn.score(X_test,y_test)
    accuracy.append(a)
   # accuracy1=accuracy_score(y_test,y_pred)
    #accuracy2=knn.score(X_test,y_test)
    #print(f'accuracy:,{accuracy1:.2f}\n {accuracy2:.2f}')
    scores=cross_val_score(knn,X,y,cv=5,scoring='accuracy')#'accuracy' for calssification
    #mean_squared_error for regression
    print(scores.mean())

plt.figure()
plt.plot(range(1,20),accuracy)
plt.show()
'''
#如果想保存模型
joblib.dump(knn,'name.joblib')
#如果想加载模型
knn2=joblib.load('name.joblib')
'''