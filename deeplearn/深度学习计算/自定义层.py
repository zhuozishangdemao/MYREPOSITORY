#层的特殊性：专门处理图像，文本，序列数据和执行动态规划的层
##不带参数的层
import torch 
import torch.nn.functional as F
from torch import nn

class CenteredLayer(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self,X):
        return X-X.mean()
# layer = CenteredLayer()
# print(layer(torch.FloatTensor([1, 2, 3, 4, 5])))
# ##带参数的层
class MyLinear(nn.Module):
    def __init__(self,in_units,units):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_units,units))
        self.bias = nn.Parameter(torch.randn(in_units,units))
    def forward(self,X):
        linear = torch.matmul(X,self.weight.data)+self.bias.data
        return F.relu(linear)
class down_grade(nn.Module):
    def __init__(self,in_units,units):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(units,in_units,in_units))
    def forward(self,X):
        return torch.einsum('bi,bj,kij->bk',X,X,self.weight)
#einsum爱因斯坦求和约定
#重复出现且不在输出的下标会自动求和
# torch.einsum('下标字符串',*tensor)
# torch.einsum()
#规则：
# 1.字母是自由索引(出现在输出中)，不求和
# 2.字母是求和索引(在输入中出现多次，但不出现在输出中)，被求和消去
# 3.字母只出现一次且不在输出中：隐式求和

#torch.unsqueeze(dim)在指定位置插入一个大小为1的新维度的方法

#practice
#2.切片或者部分摘取旧的模型进行拼接
#3.保存整个模型对象torch.save(model,'model.pth')
#使用TorchScript序列化torch.jit.script(model)