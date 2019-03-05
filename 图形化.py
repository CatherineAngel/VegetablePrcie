# -*-coding:UTF-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
#我们将使用plt.style指令为我们的数字选择合适的美学风格。在这里，我们将设置经典样式，确保我们创建的图使用经典的Matplotlib样式：
import pymongo
from datetime import datetime

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.shucaiwang   #指定数据库
collection=db['yangguang']      #连接指定name的集合
def tubiao(name,type):
    a=collection.find({'品种':name})
    dates=[]
    price=[]
    for i in a:
        dates.append(i['日期'][1:-1])
        price.append(float(i[type][1:]))
    print(dates,price)



    # xs = [datetime.strptime(d, '%Y-%b-%d').date() for d in dates]
    xs = [datetime.strptime(
        date,
        "%Y-%m-%d"
    ) for date in dates]
    print(xs)

    ys = [x for x in price]
    print(ys)


    plt.title('日期和价格走向')
    plt.xlabel("日期")
    plt.ylabel(type)
    plt.plot(xs,ys,'r')

    plt.show()

tubiao('小白菜','最高价格')
