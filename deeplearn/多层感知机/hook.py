net = nn.Sequential(
    nn.Linear(784, 256),   # 0
    nn.ReLU(),             # 1
    nn.Linear(256, 128),   # 2  ← 想取这一层的激活
    nn.ReLU(),             # 3
    nn.Linear(128, 10)     # 4
)

activation = None#创建全局张量，存储激活值
def hook_fn(module,input,output):#module:挂钩的层
    global activation##声明我们要修改外部定义的变量
    activation = output.detach()#分割

handle = net[2].register_forward_hook(hook_fn)#把钩子挂上，返回RemoveableHandle，可用移除钩子
x = torch.randn(32,784)
y= net(x)
