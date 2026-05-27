import torch
def pool_2d(X,pool2d,mode:str):
    p_h,p_w = pool2d.shape
    Y = torch.zeros((X.shape[0]-p_h+1,X.shape[1]-p_w+1))
    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):
            if mode =='mean':
                Y[i,j] = X[i:i+p_h,j:j+p_w].mean()
            if mode =='avg':
                Y[i,j] = X[i:i+p_h,j:j+p_w].max()
