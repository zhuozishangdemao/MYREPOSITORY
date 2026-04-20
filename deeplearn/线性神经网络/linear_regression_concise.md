## 线性回归的简介实现
### 读取数据集
可以调用框架中现有的api读取数据
```py
def load_array(data_arrays, batch_size, is_train=True):  #@save
    """构造一个PyTorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    #Tensordataset的作用：将多个张量按照第0轴也就是第一维度对齐，合称一个可索引的数据集对象，*data_arry为解包操作，我们认为出传入的是由feature和label张量组成的元组。
    return data.DataLoader(dataset, batch_size, shuffle=is_train)
    #数据加载器：1.处理对象：一定为TensorDataset对象：dataset对象内部将多个张量视为不同的数据字段，并通过索引**同步**访问，dataset[i]返回一个元组(feature[i],labels[i]),一般只能通过TensorDataset方法创建，也就是代码第7行
               #2.参数语法：    data.DataLoader(dataset, batch_size, shuffle=is_train)和自定义的类似，shuffle决定是否打乱，batch_size决定批次大小
               #3.返回Dataloader对象：区别于自定义的返回是生成器表达式，这里是torch中特定的数据对象，它通过for循环迭代，每次返回一个批次的数据，按批次加载
```
### 定义模型
我们关注哪些层构造模型：net层（是一个sequential类的实例）Seuqential可以将多个层连接在一起，将上一层的输出作为下一层的输入
```py
# nn是神经网络的缩写
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))#linear定义全连接层，前一个参数为输入特征形状，第二个参数为输出特征形状，Sequential方法还可以构建更多层的模型
比如
net = nn.Sequential(
    nn.Linear(2, 5),   # 第一层：输入2维，输出5维
    nn.ReLU(),         # 第二层：ReLU激活函数
    nn.Linear(5, 3),   # 第三层：输入5维，输出3维
    nn.ReLU(),         # 第四层：ReLU激活函数
    nn.Dropout(0.5),   # 第五层：Dropout，防止过拟合
    nn.Linear(3, 1)    # 输出层：输入3维，输出1维
)
此时调用
x = torch.tensor([[1,2]])
output = net(x)就会经过多层的计算zhe
```
### 初始化模型参数
####  定义权重和偏置
构造权重和偏执的初始值可以访问net的每一层进行修改（每一层对应神经网络的每一层）
```py
net[0].weight.data.normal_(0, 0.01)#net[0].weight返回一个torch.Tensor
net[0].bias.data.fill_(0)
#区分.weight.data和.weight的区别：前者返回的是Tesor的数据部分，修改不会记录在计算图中，后者返回可求导的Tensor数据，会被记录在计算图
```
#### 定义损失函数
L2范数MSELoss类
loss = nn.MSELoss()
#### 定义优化算法
我们要
1. 选择优化算法：这里SGD（小批量随机梯度下降已经是torch.optim的一个对象）
2. 选择要优化的参数：可以通过net.parametres()得到，对应返回的是生成器对象，每一个参数都是torch.Tensor，通常是每一层的权重和偏置
3. 选择优化算法需要的超参数：SGD只需要lr
trainer = torch.optim.SGD(net.parameters(), lr=0.03)
### 训练
过程和scratch一致，不过代码不需要手动实现
* forward：调用net（batch）生成预测计算损失l
* backward：反向传播计算梯度
* optim：调用优化器更新模型参数
```py
num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X) ,y)
        trainer.zero_grad()#清空trainer中所有参数的梯度
        l.backward()#对l中的所有参数反向传播计算梯度
        trainer.step()#根据参数的梯度更新模型
    l = loss(net(features), labels)
    print(f'epoch {epoch + 1}, loss {l:f}')
```