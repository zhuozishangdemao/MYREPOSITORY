手动实现微分  
```py
def numerical_lim(f,x,h):
    return (f(x+h)-f(x))/h
```
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
