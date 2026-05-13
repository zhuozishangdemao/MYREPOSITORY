#pytorch每个数组由一个device称之为环境context，默认为cpu
import torch
from torch import nn
# torch.device('cpu'),torch.device('cuda')
# torch.cuda.device_count()#返回可用GPU数量
# def try_gpu(i=0):
#     """如果存在返回gpu（i），否则返回cpu（）"""
#     if torch.cuda.device_count() >=i+1:
#         return torch.device(f'cuda:{i}')
#     return torch.device('cpu')
# def try_all_gpus():
#     """返回所有可用的GPU，如果没有GPU，返回[cpu(),]"""
#     devices = [torch.device(f'cuda:{i}')for i in range(torch.cuda.device_count())]
#     return devices if devices else [torch.device('cpu')]

# #存储张量在GPU上
# X = torch.ones(2,3,device = try_gpu(0))
# #复制：如果要进行张量之间的运算我们需要决定在哪里执行擦做
# # Z = X.cuda(1)
# #旁注：多个小操作比一个大操作糟糕的多。打印张量和转化为NumPy格式，话要复制在内存当作


# #神经网络与GPU
# net  = nn.Sequential(nn.Linear(3,1))
# net = net.to(device = try_gpu())
# import time
# n =5000
# a_cpu = torch.randn(n,n)
# b_cpu = torch.randn(n,n)

# start = time.time()
# c_cpu = a_cpu @ b_cpu
# torch.cuda.synchronize()
# cpu_time = time.time()-start
# print(f'CPU矩阵乘法耗时{cpu_time:.4f}s')

# a_gpu = a_cpu.cuda()
# b_gpu = b_cpu.cuda()
# start = time.time()
# c_gpu = a_gpu @ b_gpu
# torch.cuda.synchronize()
# gpu_time = time.time()-start
# print(f'GPU时间{gpu_time:.4f}s')


#2.GPU读写参数：模型移动，参数移动
#3.。frobenious范数计算时间
import time

N = 1000
size = 100
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"使用设备: {device}")

# 生成 1000 对矩阵（都在 GPU 上，减少逐个传输开销）
A = torch.randn(N, size, size, device=device)
B = torch.randn(N, size, size, device=device)

# 计时
start = time.time()
frobenius_norms = []
norms_gpu = torch.zeros(N,device = device)
for i in range(N):
    C = A[i] @ B[i]                      # 矩阵乘法，结果在 GPU
    norm = torch.norm(C, p='fro')        # 计算 Frobenius 范数，标量（GPU）
    norms_gpu[i] = norm  # .item() 将 GPU 标量传回 CPU
norms_cpu = norms_gpu.cpu().tolist()
torch.cuda.synchronize()
elapsed = time.time() - start

print(f"完成 {N} 次乘法并记录范数，总耗时: {elapsed:.4f} 秒")
print(f"平均每次耗时: {elapsed/N*1000:.2f} 毫秒")
print(f"前 5 个 Frobenius 范数: {norms_cpu[:5]}")