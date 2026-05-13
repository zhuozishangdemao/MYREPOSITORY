import torch
from torch import nn
from d2l import torch as d2l

# def dropout_layer(X,dropout):
#     assert 0<=dropout<=1
#     if dropout==1:
#         return torch.zeros_like(X)
#     if dropout==0:
#         return X
#     mask = (torch.rand(X.shape)>dropout).float()
#     return mask*X/(1.0-dropout)

num_inputs,num_outputs,num_hiddens1,num_hiddens2 = 784,10,256,256
dropout1 ,dropout2 = 0.2,0.5
# class Net(nn.Module):
#     def __init__(self,num_inputs,num_outputs,num_hiddens1,num_hiddens2,is_training = True):
#         super(Net,self).__init__()
#         self.num_inputs = num_inputs
#         self.training = is_training
#         self.lin1 = nn.Linear(num_inputs,num_hiddens1)
#         self.lin2 = nn.Linear(num_hiddens1,num_hiddens2)
#         self.lin3 = nn.Linear(num_hiddens2,num_outputs)
#         self.relu = nn.ReLU()
#     def forward(self,X):
#         H1 = self.relu(self.lin1(X.reshape(-1,self.num_inputs)))

#         if self.training == True :
#             H1 = dropout_layer(H1,dropout1)
#         H2 = self.relu(self.lin2(H1))
#         if self.training == True :
#             H2 = dropout_layer(H2,dropout2)
#         out = self.lin3(H2)
#         return out
# net = net = Net(num_inputs, num_outputs, num_hiddens1, num_hiddens2)
import matplotlib.pyplot as plt
net = nn.Sequential(
    nn.Flatten(),
    nn.Linear(784,256),
    nn.ReLU(),
    nn.Dropout(dropout1),
    nn.Linear(256,256),
    nn.ReLU(),
    nn.Dropout(dropout2),
    nn.Linear(256,10)
)
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight,std=0.6)

net.apply(init_weights);

# num_epochs, lr, batch_size = 10, 0.5, 256
# trainer = torch.optim(net.parameters,lr=lr)
num_epochs, lr, batch_size = 10, 0.5, 256
loss = loss = nn.CrossEntropyLoss(reduction='none')
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)
from IPython import display
def accuracy(y_hat, y):  #@save
    """计算预测正确的数量"""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())
def evaluate_accuracy(net, data_iter):  #@save
    """计算在指定数据集上模型的精度"""
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    device = next(net.parameters()).device
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            X,y = X.to(device),y.to(device)
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]
class Accumulator:  #@save
    """在n个变量上累加"""
    def __init__(self, n):
        self.data = [0.0] * n

    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
activation = None
def hook_fn(module,input,output):
    global activation
    activation = output.detach()
def train_epoch_ch3(net, train_iter, loss, updater):  #@save
    """训练模型一个迭代周期（定义见第3章）"""
    # 将模型设置为训练模式
    activation =None
    handle = net[6].register_forward_hook(hook_fn)
    if isinstance(net, torch.nn.Module):
        net.train()
    
    # 训练损失总和、训练准确度总和、样本数
    device =next(net.parameters()).device
    metric = Accumulator(3)
    activation_metric = Accumulator(2)
    for X, y in train_iter:
        # 计算梯度并更新参数
        X,y = X.to(device),y.to(device)
        y_hat = net(X)
        l = loss(y_hat, y)
        activation_metric.add(torch.var(activation,unbiased = False),1)
        if isinstance(updater, torch.optim.Optimizer):
            # 使用PyTorch内置的优化器和损失函数
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            # 使用定制的优化器和损失函数
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    handle.remove()
    # 返回训练损失和训练精度
    return metric[0] / metric[2], metric[1] / metric[2],activation_metric[0]/activation_metric[1]
class Animator:  #@save
    """在动画中绘制数据"""
    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        # 增量地绘制多条线
        if legend is None:
            legend = []
        plt.ion()
        self.fig, self.axes = d2l.plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes, ]
        # 使用lambda函数捕获参数
        self.config_axes = lambda: d2l.set_axes(
            self.axes[0], xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        # 向图表中添加多个数据点
        if not hasattr(y, "__len__"):
            y = [y]
        n = len(y)
        if not hasattr(x, "__len__"):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla()
        for x, y, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x, y, fmt)
        self.config_axes()
        self.fig.canvas.draw()
        plt.pause(0.001)
def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):  #@save
    """训练模型（定义见第3章）"""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = net.to(device)
    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc
trainer = torch.optim.SGD(net.parameters(), lr=lr)
train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)