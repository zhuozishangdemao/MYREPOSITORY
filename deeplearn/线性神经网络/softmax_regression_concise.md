### 初始化模型参数
```py
# PyTorch不会隐式地调整输入的形状。因此，
# 我们在线性层前定义了展平层（flatten），来调整网络输入的形状
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))
#由于Sequential可以理解为从左到右的执行参数的内容，nn.flatten作为内置函数将输入展平为一维向量例如，将(batch_size,28,28)展平为(batch_size,784)
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)
#m.weight为层的权重参数，检查m是不是nn.Linear层，也就是对所有全连接层进行操作
net.apply(init_weights)#遍历网络中的所有模块将函数1应用与网络的每一层
```
### 重新审视softmax的实现
问题$\mathbf{o}$可能过大超过数据类型允许储存的最大值  
解决方式：对于所有ok减去最大值
问题2：减法后可能ok为较大的负值，exp后趋近于0，  
解决方式：直接进行对数计算不通过exp计算
loss = nn.CrossEntropyLoss(reduction='none')
### 优化算法
trainer = torch.optim.SGD(net.parameters(), lr=0.1)
