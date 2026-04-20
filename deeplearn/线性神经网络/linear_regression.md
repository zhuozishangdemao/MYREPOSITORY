### 小批量随机梯度下降
真实情况中更新参数如果遍历所有元素较慢，可以随机抽取一小批样本  
计算公式为
$$(\mathbf{w},b) \leftarrow (\mathbf{w},b) - \frac{\eta}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \partial_{(\mathbf{w},b)} l^{(i)}(\mathbf{w},b).$$
学习率: $\eta$
每个小批量的样本数:$|\mathcal{B}|$
学习率和每个小批量样本数是手动预先指定，称为**超参数**  
*调参*为选择超参数的过程，往往依据验证集的结果来调整

### 预测和推断
推断指的是通过数据集估计参数，包含学习的动作  
预测值的是估计一个未包含在训练数据中的新房屋的价格

### 矢量化（向量化）加速
希望对计算矢量化，利用线性代数库，而不是在python中使用for循环：把数据组织为张量
为了描述这个时间定义了一个计时器  
```py

class Timer:  #@save
    """记录多次运行时间"""
    def __init__(self):
        self.times = []#初始化时自动创建实例的一个属性为times并且为空列表
        self.start()#初始化时自动执行self.start()也就是开始计时

    def start(self):
        """启动计时器"""
        self.tik = time.time()#动态创建了一个新的实例属性tik，虽然没有在__init__声明，但是python允许在任何方法内通过self.xxx添加新属性

    def stop(self):
        """停止计时器并将时间记录在列表中"""
        self.times.append(time.time() - self.tik)
        return self.times[-1]# 返回最新记录的元素

    def avg(self):
        """返回平均时间"""
        return sum(self.times) / len(self.times)#可以对多次的时间调用取平均

    def sum(self):
        """返回时间总和"""
        return sum(self.times)

    def cumsum(self):
        """返回累计时间"""
        return np.array(self.times).cumsum().tolist()#tolist函数将numpy数组重新转化为listpython对象
```
### 正态分布与平方损失
本部分想要解释：为什么平方损失成为我们选择的损失函数：在噪声符合正态分布的假设下，平方损失是最优的.  
明确我们的假设：X在实际中并不直接的为某个具体的y，由于噪声的扰动，y的值服从某个正态分布
我们假设了观测中包含噪声，其中噪声服从正态分布。
噪声正态分布如下式:

$$y = \mathbf{w}^\top \mathbf{x} + b + \epsilon,$$

其中，$\epsilon \sim \mathcal{N}(0, \sigma^2)$。

我们的所有目标操作都建立在最大化似然上（这不关乎我们是否假设原数据符合任何假设空间）  
可以写出给定$\mathbf{x}$观测到待定$y$的**似然**：
$$P(y \mid \mathbf{x}) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{1}{2\sigma^2}(y-\mathbf{w}^\top\mathbf{x}-b)^2\right).$$
定义一个python函数计算正态分布
```py
def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)
```

### 线性回归到深度网络
事实上线性回归可以看作只有一层的神经网络，这个层满足每个输入和输出相连，称为**全连接层**或者**稠密层**

