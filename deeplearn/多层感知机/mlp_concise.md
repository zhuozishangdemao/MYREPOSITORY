唯一区别是增加了两个全连接层
```py
net = nn.Sequnetial(
    nn.Flaten(),
    nn.Linear(784,256),
    nn.Relu()
    nn.Linear(256,10)
)
def init_weight(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight,std = 0.01)

net.apply(init_weights)#对于每个nn.Linear对象的权重部分进行正态分布采样
