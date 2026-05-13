#块：描述单个层，多个层组成的组件或整个模型本身
#块由类表示，任何一个子类都必须定义一个将其输入转换为输出的前向传播函数和存储必要的参数
import torch
from torch import nn
from torch.nn import functional as F

# net = nn.Sequential(
#     nn.Linear(20,256),
#     nn.ReLu,
#     nn.Linear(256,10)
# )
X = torch.rand(2,20)
#块的功能
#1.输入参数计算前向传播结果2.计算梯度 3.访问参数 4.初始化参数
class MLP(nn.Module):
    #用模型参数声明层。这里，声明两个全连接层
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20,256)
        self.out = nn.Linear(256,10)
    
    def forward(self,X):
        return self.out(F.relu(self.hidden(X)))
    #ReLu的函数版本，在nn.functional模块定义
class MySequential(nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for idx,module in enumerate(args):
            self._modules[str(idx)] = module
    def forward(self,X):
        for block in self._modules.values():
            X = block(X)
        return X
# net = MySequential(nn.Linear(20,256),nn.ReLU(),nn.Linear(256,10))
# net(X)
# 为了实现在层中和并一些既不是上:
# 一次结果也不可更新的常数参数constant parameter
class FixedHiddenMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.rand_weight = torch.rand((20,20),requires_grad=False)
        self.linear = nn.Linear(20,20)

    def forward(self,X):
        X = self.linear(X)
        X = F.relu(torch.mm(X,self.rand_weight)+1)
        X = self.linear(X)
        while X.abs().sum()>1:
            X/=2
        return X.sum()
class NestMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(20,64),nn.ReLU(),
                                 nn.Linear(64,32),nn.ReLU())
        self.linear = nn.Linear(32,16)

    def forward(self,X):
        return self.linear(self.net(X))
chimera = nn.Sequential(NestMLP(),nn.Linear(16,20),FixedHiddenMLP())

class parallel_two_net(nn.Module):
    def __init__(self,net1,net2):
        super().__init__()
        self.net1 = net1
        self.net2 = net2
        self.add_module('net1',net1)
        self.add_module('net2',net2)
    def forward(self,X):
        out1 = self.net1(X)
        out2 = self.net2(X)
        return torch.cat((out1,out2),dim=1)
class Parallel(nn.Module):
    def __init__(self,*agrs):
        super().__init__()
        for idx,module in enumerate(agrs):
            self.add_module(str(idx),module)
    def forward(self,X):
        outputs = [module(X) for module in self._modules.values()]
        return torch.cat(outputs,dim=1)
def multiply_module(block_constrcutor,num_repeats,connection_type = 'sequential'):
    """
        参数:
        block_constructor: 一个可调用对象，每次调用返回一个 nn.Module 实例。
        num_repeats: 重复次数
        connection_type: 'sequential' (串联) 或 'parallel' (并联)
    返回:
        一个由 num_repeats 个独立块组成的大网络。
    """
    blocks = [block_constrcutor() for _ in range(num_repeats)]

    if connection_type =='sequential':
        return nn.Sequential(*blocks)
    elif connection_type =='parrallel':
        return Parallel(*blocks)
    else:
        raise ValueError
    