## 多层感知机从0实现
### 初始化模型参数
记录权重矩阵和偏置向量，为算是关于这些参数的梯度分配内存
```py
num_inputs, num_outputs, num_hiddens = 784, 10, 256

W1 = nn.Parameter(torch.randn(
    num_inputs, num_hiddens, requires_grad=True) * 0.01)
b1 = nn.Parameter(torch.zeros(num_hiddens, requires_grad=True))
W2 = nn.Parameter(torch.randn(
    num_hiddens, num_outputs, requires_grad=True) * 0.01)
b2 = nn.Parameter(torch.zeros(num_outputs, requires_grad=True))
##nn.Parameter方法,直接把该对象注册到Module的参数列表中，在model.parameters()可以被迭代
params = [W1, b1, W2, b2]
```
### 激活函数
```py
def relu(x):
    a = torch.zeros_like(x)
    return torch.max(x,a)
```

### 模型
```py
def net(x):
x= x.reshape((-1,num_inputs))
H= relue(x@W1+b1)
return (H@W2+b2)#@为矩阵乘法
```

### 损失函数
nn.CrossEntripyLoss(redunction='none')
### 训练