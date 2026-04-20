#linear_regression practice1
#region
import torch

# 生成一些模拟数据
torch.manual_seed(42)#设计随机数种子
x = torch.randn(100) * 2 + 5  # 100个点，真实均值为5#torch.randn(x)会返回形状为(100,)的张量

# 初始化参数 b，并设置需要梯度
b = torch.randn(1, requires_grad=True)

# 定义优化器（这里用简单的 SGD）
optimizer = torch.optim.SGD([b], lr=0.001)#SGD为随机梯度下降优化器
#torch.SGD([b],lr=0.1)[b]为可迭代对象，包含需要被迭代器优化的参数，且每个参数必须requires_grad = True在调用step()会根据这些参数的.grad更新
#lr为learning rate控制每一步的参数更新幅度
#optimizer为我们封装了参数更新逻辑：b = b - lr* b .grad
# 迭代优化
for epoch in range(100):
    # 前向传播：计算损失 L = sum((x - b)^2)
    loss = torch.sum((x - b) ** 2)
    
    # 反向传播：自动计算梯度 dL/db
    loss.backward()
    
    # 更新参数
    optimizer.step()
    
    # 清零梯度（重要！否则梯度会累加）
    optimizer.zero_grad()#清理优化器记录的所有变量的梯度
    
    if (epoch + 1) % 20 == 0:
        print(f'Epoch {epoch+1:3d}, b = {b.item():.4f}, loss = {loss.item():.2f}')

print(f'\nPyTorch 优化结果: b = {b.item():.4f}')
print(f'解析解（样本均值）: {x.mean().item():.4f}')

# endregion
#linear_regression practice2
#region
#解析解的好处在于直接得到权重的结果，但缺点是在大规模数据时对算
#力要求很高，随机梯度下降方法可以对大规模数据处理，但最终得到的
#是近似解，还需要保证训练次数让权重收敛
#endregion
#linear_regression_scratch practice
#region
#4计算量过大，要解决d^2个导数的计算，二阶导数可能极大或者极小解
#方法是避免直接计算出海森矩阵本身，而是计算乘积结果
#7可能会抛出一个小于batch_size的batch，后续处理由于除了batch的大小没有影响
#5保证正确广播，反之生成一个label*label大小的矩阵
#endregion
#linear_regression_concise
#1，由于对应的backward结果为原来的1/batch_size，学习率应当乘以batch_size
#2.Huber损失
#3.net.weight.grad net.bias.grad