#操作参数：访问参数，用于调试诊断和可视化
#参数初始化
#在不同模型组件之间共享参数
import torch
from torch import nn

net = nn.Sequential(nn.Linear(4,8),nn.ReLU(),nn.Linear(8,1))
X = torch.rand(size=(2,4))
print(net[2].state_dict())#.state_dict() 访问参数
#每个参数都是参数类的实例torch.nn.parameter.Parameter
#net如果是块：可以用.named_parameters(),返回(参数名，参数张量)的元组或者state_dict()方法访问，返回参数唯一名称的字典
#net如何是底层的Module：包含weight和bias属性，可以用named_parameters()方法访问
# Sequential(
#   (0): Sequential(
#     (block 0): Sequential(
#       (0): Linear(in_features=4, out_features=8, bias=True)
#       (1): ReLU()
#       (2): Linear(in_features=8, out_features=4, bias=True)
#       (3): ReLU()
#     )
#     (block 1): Sequential(
#       (0): Linear(in_features=4, out_features=8, bias=True)
#       (1): ReLU()
#       (2): Linear(in_features=8, out_features=4, bias=True)
#       (3): ReLU()
#     )
#     (block 2): Sequential(
#       (0): Linear(in_features=4, out_features=8, bias=True)
#       (1): ReLU()
#       (2): Linear(in_features=8, out_features=4, bias=True)
#       (3): ReLU()
#     )
#     (block 3): Sequential(
#       (0): Linear(in_features=4, out_features=8, bias=True)
#       (1): ReLU()
#       (2): Linear(in_features=8, out_features=4, bias=True)
#       (3): ReLU()
#     )
#   )
#   (1): Linear(in_features=4, out_features=1, bias=True)
# )
#可以用rgnet[0][1][0].bias.data访问

#参数初始化
#nn.init
def init_normal(m):
    if type(m)==nn.Linear:
        nn.init.normal_(m.weight,mean=0,std=0.01)
        nn.init.zeros_(m.bias)
net.apply(init_normal)
def init_constant(m):
    if type(m) == nn.Linear:
        nn.init.constant_(m.weight,1)
        nn.init.zeros_(m.bias)
net.apply(init_constant)
def init_xavier(m):
    if type(m) == nn.Linear:
        nn.init.xavier_uniform_(m.weight)
def init_42(m):
    if type(m)==nn.Linear:
        nn.init.constant_(m.weight,42)

#自定义初始化
def my_init(m):
    if type(m) ==nn.Linear:
        print("Init",*[(name,param.shape) for name,param in m.named_parameters()][0])
        nn.init.uniform_(m.weight,-10,10)
        m.weight.data*=m.weight.data.abs()>=5
net.apply(my_init)

#参数绑定
shared = nn.Linear(8,8)
net = nn.Sequential(nn.Linear(4,8),
                    nn.ReLU(),
                    shared,nn.ReLU,shared,nn.ReLU,nn.Linear(8,1))
#梯度计算时会叠加