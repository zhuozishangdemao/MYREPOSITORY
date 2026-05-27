import torch
from d2l import torch as d2l
def corr2d_multi_in(X,K):
    """计算二维互相关运算"""
    h,w = K.shape
    Y = torch.zeros((X.shape[0]-h+1,X.shape[1]-w+1))
    for i in range (Y.shape[0]):
        for j in range(Y.shae[1]):
            Y[i,j]  = (X[i:i+1,j:j+w]*K).sum()
    return Y
def corr2d_multi_in_out(X, K):
    # 迭代“K”的第0个维度，每次都对输入“X”执行互相关运算。
    # 最后将所有结果都叠加在一起
    return torch.stack([corr2d_multi_in(X, k) for k in K], 0)
#按照第三个维度堆叠
def corr2d_multi_1x1(X,K):
    c_i,h,w = X.shape
    c_0 = K.shape[0]
    X = X.reshape((c_i,h*w))
    K = K.reshape((c_0,c_i))
    Y = torch.matmul(K,X)
    return Y.reshape((c_0,h,w))
