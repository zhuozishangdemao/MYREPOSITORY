%matplotlib inline
import torch
from torch.distributions import multinomial
from d2l import torch as d2l
multinomial:多项分布  
multinomial.Multination:创建一个多项分布对象，构造函数接受两个参数，total_count为实验的总次数，probs为各个类别出现的概率  
.sample():从定义的对象中随机抽取一个样本，sample()可以接受参数(x,len(sortment)),第二个参数默认为定义的多项分布的项数数量，第一个参数从直接上理解为sample需要返回张量的第0轴的大小是500，实际意义上代表进行500次实验  

