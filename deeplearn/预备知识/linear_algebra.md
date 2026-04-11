x = torch.arrange(4)<br>
len(x):返回向量的长度，第0轴的形状  
A =torch.arrange(20).reshape(5,4)  

A.T:矩阵转置  

tensor:可以具有任意数量轴的数学对象  
A  = torch.arange(24).reshape(2,3,4)  
B = A.clone():分配新内存，将A的新副本给B

Hadamard积:A*B  
对应元素标量相乘

A.sum():求所有元素的和
A_sum_axis0 = A.sum(axis=0):按照0轴来求和，直观的输出结果是把0轴的形状压缩为1  
A.sum(axis=[0,1])=A.sum()  

A.mean():求平均值  
=A.sum()/A.numel()  
A.mean(axis=0):对0轴求平均  
=A.sum(axis=0)/A.shape[0]  

sum_A = A.sum(axis =1,keepdims =True):保持轴的数量不变  

A.cumsum(axis=0):对某个轴求累计总和

torch.dot(X,Y):点积，相同位置按照元素乘积的和，注意数学对象为两个向量  

torch.mv(A,x):向量积，数学对象为metric和vector  
touch.mm(A,B):矩阵乘法  
torch.norm(x):二范数  
torch.abs(x).sum():一范数
torch.norm(A):矩阵的frobenius范数



