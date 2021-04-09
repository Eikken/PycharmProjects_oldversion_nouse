import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs  # 导入产生模拟数据的方法
from sklearn.cluster import KMeans

# 1. 产生模拟数据
k = 5
X, Y = make_blobs(n_samples=1000, n_features=2, centers=k, random_state=1)

# 2. 模型构建
km = KMeans(n_clusters=k, init='k-means++', max_iter=30)
km.fit(X)

# 获取簇心
centroids = km.cluster_centers_
# 获取归集后的样本所属簇对应值
y_kmean = km.predict(X)

# 呈现未归集前的数据
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.yticks(())
plt.show()

plt.scatter(X[:, 0], X[:, 1], c=y_kmean, s=50, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=100, alpha=0.5)
plt.savefig('png/5点聚类.png')
plt.show()


# # 生成随机点,经纬度中:
# #  20 < x < 30
# #  160 < y < 170
# def randX():
#     x1 = random.randint(20,30)
#     x2 = random.randint(20,30)
#     x3 = random.randint(20,30)
#     x4 = random.randint(20,30)
#     return x1,x2,x3,x4
# def randY():
#     y1 = random.randint(160,170)
#     y2 = random.randint(160,170)
#     y3 = random.randint(160,170)
#     y4 = random.randint(160,170)
#     return y1,y2,y3,y4
#
# sspData = pd.read_excel(r'ssp_all.xlsx')
# latLonData = pd.read_csv(r'LatLon_all.txt')
#
# # 经度为x,纬度为y，时间为z，我们暂时不先加入时间
# # 选取k-means 中 k = 4生成四个聚类试试
#
# x1, x2, x3, x4 = randX()
# y1, y2, y3, y4 = randY()
