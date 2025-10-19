import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 3. 从 sklearn 导入各种模块
# 数据集
from sklearn.datasets import load_iris, load_breast_cancer, make_regression
from sklearn.model_selection import train_test_split

# 预处理
from sklearn.preprocessing import StandardScaler


from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA

# 评估指标
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix, silhouette_score

#1 Classifier
iris = load_iris()
X = iris.data
y = iris.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#'逻辑回归（可分类）'
lr_model = LogisticRegression(random_state=42)
#SVC（）需要标准化数据!这里省略，因为这个程序不会运行
svc_model=SVC(kernel='rbf', random_state=42)
#决策树
dt_model = DecisionTreeClassifier(max_depth=3, random_state=42)
#随机森林
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
#k近邻
knn_model = KNeighborsClassifier(n_neighbors=5)
#素数贝叶斯
nb_model = GaussianNB()


#2 Regression
#正则化强度1
#岭回归
ridge_reg = Ridge(alpha=1.0)
#SVR
svr_model = SVR(kernel='rbf')
#随机森岭
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)

#3 无监督学习
#K-means
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans_labels = kmeans.fit_predict(X_cancer_scaled)
R=silhouette_score(X_cancer_scaled, kmeans_labels)
pca = PCA(n_components=2)#pca可视化
X_pca = pca.fit_transform(X_cancer_scaled)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans_labels, cmap='viridis')
plt.title("K-Means Clustering (Visualized with PCA)")
plt.show()
#dbscan无需指定k
dbscan = DBSCAN(eps=0.5, min_samples=5) # eps和min_samples是关键参数
dbscan_labels = dbscan.fit_predict(X_cancer_scaled)
    # 查看分成了几类（-1代表噪声点）
n_clusters = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
print(f"DBSCAN 发现的簇数量: {n_clusters}")
print(f"DBSCAN 轮廓系数: {silhouette_score(X_cancer_scaled, dbscan_labels):.4f}")

'''
对于svm(svc/svr,):归一化！！！
kernel='linear'
        ='poly'
        ='rbf'
gamma_high:over,complex
gamma_low:less,simple
C_high:over,less wrong
C_low:less,more wrong
default:gamma='scale',C=1.0

最优参数：
param_grid = {
    'C': [0.1, 1, 10, 100],           # 尝试更宽容和更严格的惩罚
    'gamma': [1, 0.1, 0.01, 0.001],   # 尝试更复杂和平滑的边界
    'kernel': ['rbf', 'linear']       # 尝试不同的核
}
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(random_state=42), param_grid, refit=True, verbose=2, cv=5)
grid.fit(X_train_scaled, y_train)

print("最佳参数：", grid.best_params_)
best_svm_model = grid.best_estimator_
'''