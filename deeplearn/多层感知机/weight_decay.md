## 权重衰减
介绍正则化模型的技术
### 范数与权重衰减
#### 权重衰减：L2正则化
描述函数和0之间的距离
#### 使用pytorch中集成的权重衰减
在trainer中增加参数列表：
 trainer = torch.optim.SGD([
        {"params":net[0].weight,'weight_decay': wd},
        {"params":net[0].bias}], lr=lr)