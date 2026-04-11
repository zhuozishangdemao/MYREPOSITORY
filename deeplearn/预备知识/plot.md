plot实现函数呈现  
```py
def use_svg_display():
    set_matplotlib_formats('svg')
def set_figsize(figsize=(3.5,2,5)):
    use_svg_display()
    plt.rcparams['figure.figsize'] = figsize#rcparams是matplotb的全局配置字典，存储了所有默认的样式参数
def set_axes(axes,xlabl,ylabel,xlim,ylim,xscale,yscale,legend):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()
##Axe是matlib中的对象，为子图，axes为要操作的子图对象，对应由很多方法可以改变子图的参数，set_axes就是为了便捷的修改这些参数
#@save
def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear',
         fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):#X为主数据，Y如果提供为纵坐标，axes如果没有就自动获取
    """绘制数据点"""
    if legend is None:
        legend = []

    set_figsize(figsize)
    axes = axes if axes else d2l.plt.gca()#plt.gca()获取当前激活的Axes对象，在没有子图的时候会自动创建

    # 如果X有一个轴，输出True
    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], "__len__"))
    #如果x由ndim属性，且维度为1，返回True，或者X是列表且第一个元素没有len方法：也就是元素本身不是一个列表或者元组
    if has_one_axis(X):
        X = [X]
    if Y is None:#表示只传入Y值，将X转化为Y，X定义为默认序列（这种情况是普遍的，我们往往只输入Y的值而不定义X）
        X, Y = [[]] * len(X), X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)#保证每个Y都能分到横坐标
    axes.cla()#擦除Axes对象上已经绘制的内容
    for x, y, fmt in zip(X, Y, fmts):#zip：在最短的序列结束时停止，保证标签的数量够用
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
```
实现500组实验多项式分布输出
```py
counts = multinomial.Multinomial(10, fair_probs).sample((500,))
cum_counts = counts.cumsum(dim=0)
estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)

d2l.set_figsize((6, 4.5))
for i in range(6):
    d2l.plt.plot(estimates[:, i].numpy(),#每次取一列，默认y轴
                 label=("P(die=" + str(i + 1) + ")"))
d2l.plt.axhline(y=0.167, color='black', linestyle='dashed')#对图上画一条水平参考线
d2l.plt.gca().set_xlabel('Groups of experiments')#.gca()可以获取当前坐标轴对象
d2l.plt.gca().set_ylabel('Estimated probability')
d2l.plt.legend();
```
plt操作逻辑  
fig：一张画布，axes：多张画纸（可以通过axes的索引来访问任意一张画纸）  
创建方式：  
fig, axes = plt.subplots(2, 3)  # 2行3列，共6个子图  
┌─────────────┬─────────────┬─────────────┐
│ axes[0, 0]  │ axes[0, 1]  │ axes[0, 2]  │
├─────────────┼─────────────┼─────────────┤
│ axes[1, 0]  │ axes[1, 1]  │ axes[1, 2]  │
└─────────────┴─────────────┴─────────────┘
       Figure (fig) 是整张桌子
ax的操作就是对子图进行操作，每个子图可以有独立的xy，标题，图例，刻度  
```py
fig, axes = plt.subplots(1, 2)
axes[0].plot([1,2,3], [1,2,3])  # 只在左边子图画线
axes[1].scatter([1,2,3], [3,2,1])  # 只在右边子图画散点
axes[0].set_title("Left")       # 只给左边加标题
```
fig的操作就是对于整个画布进行操作例如：  
fig.suptitle('main title')#给整个画布加上title  
fig.tight_layout#自动调整子图间距防止重叠  
fig.savefig('output.png')#保存整张图  

对于plt操作实际上是对当前激活的子图AXe进行操作  
实现激活的方法是函数subplot（nrows，ncols，index）index为激活的子图编号，nrows和ncols表示将当前画布划分为几行几列  
也可以使用.gca()得到当前处于激活的axes对象