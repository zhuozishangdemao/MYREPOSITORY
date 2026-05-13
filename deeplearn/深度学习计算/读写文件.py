#加载存储权重向量和整个模型，便于保存训练的中间结果

import torch
from torch import nn
from torch.nn import functional as F
#加载和保存张量
x = torch.arange(4)
# torch.save(dict/list/tensor,'filename')
#加载和保存模型参数
#模型参数不等于模型，我们需要单独指定其架构
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20,256)
        self.output = nn.Linear(256,10)
    def forward(self,X):
        return self.output(F.relu(self.hidden(X)))

net = MLP()
# torch.save(net.state_dict(),'mlp.param')
clone = MLP()#手动说明架构
clone.load_state_dict(torch.load('mlp.param'))
print(clone.eval())