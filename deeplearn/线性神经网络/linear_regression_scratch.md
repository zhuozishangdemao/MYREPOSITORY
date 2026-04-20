### 生成数据集
```py
def synthetic_data(w, b, num_examples):  #@save#num_example指的是生成样本的数量
    """生成y=Xw+b+噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))
    #torch.normal(mean,std,size)从均值mean，标准差为std生成指定size的张量
    y = torch.matmul(X, w) + b#torch.matunal计算矩阵乘法，b作为偏置，广播为(num_example,1)大小
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))#将y形状变为(n,1)-1参数表示不变
```

### 读取数据集
定义一个函数，打乱数据集并且以小批量的方式获取数据
```py
def data_iter(batch_size, features, labels):
    num_examples = len(features)#返回第0轴的长度
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]#张量的高级索引：当使用整数张量作为索引的时候，会按照索引张量的每一个元素，去原张量的第0维选取对应的行，返回一个这些行堆叠起来的新张量
        #feature[batch_indices]返回大小为(batch_size,num_feaetures)的张量，labels[bath_indices]返回(batch_size,1)大小
    #yield返回一个生成器对象，该对象可以被迭代。
    #在定义过程中 gen =data_iter()只会让gen成为一个生成器对象，函数不会执行任何语句，也就没有任何开销
    #在调用过程中，函数在遇到yield时暂停执行保留所有变量并且返回给调用对象。可以再次通过for循环从暂停处继续执行，直到下次遇到yield。此为惰性序列，适合处理大的数据流
```
实际操作时获取小批量的迭代器始终会占用内存，真实情况会用内置的迭代器，可以处理存储在文件中的数据和数据流提供的数据

### 初始化模型参数
```py
w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
```
### 定义模型
```py
def linreg(X, w, b):  #@save
    """线性回归模型"""
    return torch.matmul(X, w) + b
```
#### 定义损失函数
```py
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2#根据y_hat.shape返回的列表进行y的大小转化
```
#### 定义优化算法
```py
def sgd(params, lr, batch_size):  #@save
    """小批量随机梯度下降"""
    with torch.no_grad():#上下文管理器：在with语句内部，计算图不会记录任何计算操作以构建计算图，我们实际只希望更新参数但是不参与到计算图的构建中
        for param in params:
            param -= lr * param.grad / batch_size#给予小批次数据大小，防止因为批次数据大小影响结果
            param.grad.zero_()
```
### 训练模型
```py
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
        # 并以此计算关于[w,b]的梯度
        l.sum().backward()#backward()只能对标量操作
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad():#输出结果的过程不可以记录到计算图中
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')