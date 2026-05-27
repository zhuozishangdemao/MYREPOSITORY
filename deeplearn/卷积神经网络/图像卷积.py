import torch
from torch import nn
def corr2d(X,K):
    """计算二维互相关系运算"""
    h,w = K.shape
    Y = torch.zeros((X.shape[0]-h+1,X.shape[1]-w+1))
    for i in range (Y.shape[0]):
        for j in range((Y.shape[1])):
            Y[i,j] = (X[i:i+h,j:j+w]*K).sum()
    return Y
class Conv2D(nn.Module):
    def __init__(self,kernel_size):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(kernel_size))
        self.bias = nn.Parameter(torch.zeros(1))
    def forward(self,X):
        return corr2d(X,self.weight)+self.bias
kernel_try = torch.rand((1,2))
conv2d = nn.Conv2d(1,1,kernel_size=(1,2),bias = False)
X = torch.ones((6, 8))
X[:, 2:6] = 0
K = torch.tensor([[1.0, -1.0]])
Y = corr2d(X, K)
X = X.reshape(1,1,6,8)
Y = Y.reshape(1,1,6,7)
lr = 3e-2
max_turn = 5
my_conv2d = Conv2D((1,2))
loss = (my_conv2d(X)-Y)**2
my_conv2d.zero_grad()
loss.sum().backward()
print(my_conv2d.weight.grad)
# for epoch in range(max_turn):
#     loss = (conv2d(X)-Y)**2
#     conv2d.zero_grad()
#     loss.sum().backward()
#     conv2d.weight.data[:]-=lr*conv2d.weight.grad
#     print(f'epoch:{epoch},loss:{loss.sum():.3f}')
# print(conv2d.weight.data)
# h,w = 7,7
# X = torch.zeros((h,w))
# threshold = (h+w)/2
# for i in range (h):
#     for j in range(w):
#         if i+j<threshold:
#             X[i,j] = 1.0
# print(corr2d(X,K))
# X = X.T
# print(corr2d(X,K))
# X =X.T
# K=K.T
# print(corr2d(X,K))
"""
二阶导数的核（一维情况）
中心差分近似
"""