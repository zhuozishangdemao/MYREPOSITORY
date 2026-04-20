## 图像分类数据集
minist数据集基准数据过于简单，使用Fashion_mnist
### 导入函数
```py
%matplotlib inline
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l

d2l.use_svg_display()
```
### 读取数据集
```py
# 通过ToTensor实例将图像数据从PIL类型变换成32位浮点数格式，
# 并除以255使得所有像素的数值均在0～1之间
trans = transforms.ToTensor()#一个处理数据方法的实例
mnist_train = torchvision.datasets.FashionMNIST(
    root="../data", train=True, transform=trans, download=True)#root指定存放位置，train=True为训练集，False为测试机，transform对应数据处理方法，返回的是Dataset对象，
mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False, transform=trans, download=True)
```
### 可视化数据集
```py
def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):  #@save
    """绘制图像列表"""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)#n_rows,n_cows指定了子图的行数和列数，此时axes是一个num_rows*num_cols 的数组
    axes = axes.flatten()#扁平化为一维数组
    for i, (ax, img) in enumerate(zip(axes, imgs)):#enumerate同时输出index，zip将多个可迭代对象合成元组
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)#隐藏x和y轴
        if titles:
            ax.set_title(titles[i])
    return axes
```

### 读取小批量
使用函数内置的迭代器，可以随机打乱
 ```py
batch_size = 256

def get_dataloader_workers():  #@save
    """使用4个进程来读取数据"""
    return 4

train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True，  num_workers=get_dataloader_workers())
```
### 整合所有组件
```py
def load_data_fashion_mnist(batch_size, resize=None):  #@save
    """下载Fashion-MNIST数据集，然后将其加载到内存中"""
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))#本质trans是一个列表，第一个元素原本只包含transformes.TOTensor，之后追加了改变size的方法
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(
        root="../data", train=True, transform=trans, download=True)
    mnist_test = torchvision.datasets.FashionMNIST(
        root="../data", train=False, transform=trans, download=True)
    return (data.DataLoader(mnist_train, batch_size, shuffle=True,num_workers=get_dataloader_workers()),
            data.DataLoader(mnist_test, batch_size, shuffle=False,num_workers=get_dataloader_workers()))
```