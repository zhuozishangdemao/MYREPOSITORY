#linear_regression practice1
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