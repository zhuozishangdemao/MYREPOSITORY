#手动实现所有层的输入输出维度困难，lazyLinear可以只要求输出维度，自动设计输入参数
import torch
from torch import nn
net = nn.Sequential(
    nn.LazyLinear(8),
    nn.ReLU,
    nn.lazyLinear(1)
)
#1.对于不是第一层使用lazyLinear的例子，之后的lazylinear需要知道输入时是什么才会初始化
#更本质的：Pytorch不会在构建的时候进行形状的关系检验和关联，只有在数据流过的时候才会作数据检验
