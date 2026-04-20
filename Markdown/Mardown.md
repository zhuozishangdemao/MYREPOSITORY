# 标题语法
#的数量x就是x级标题  
***#之后之后要有空格***
## 一级标题
### 二级标题
#### 三级标题
******

# 段落语法
使用空白行进行文本分割<br>
不要在段落前留有空格以防formatting problem 

# 换行语法
方法1：两个空格加换行符  
方法2：结尾加上 <br>

# 强调语法
加粗：`**bold text**`  
斜体：`*italic text*`  
斜体且加粗`***text***`  

# 引用语法
在需要引用的段落添加><br>
`>he like us`  
引用可以包含多个段落，只需在段落之间的空白行用>连接
>I used to love her --Tony  
>
>me too 

嵌套块的引用
>tommy and his girlfrined is heading to auditorium for a show
>
>>though he didn't want to pay the bill by himself
>
>>>and i was sure he  was alluding you

带有其他元素的块引用
>#### The quarterly results look great
>
> - revenue was off the chart
> - Profits was higher than ever <br>
>
>*Everything*   is going according to the **plan**

# 列表语法
数字加上英文句点，数字可以没有顺序但必须从开始

1. first item
2. second item
3. third item
    1. itemo
    2. item2

无序列表

- first item
- second item
    * item
    * lifelike
        + dffen

在列表中嵌套其他元素   
需要将该元素缩进一个tab  

* This is list item .
* here is second list item.

    >I need to learn chinese 

        `int i=0;  
        print (i)`

* and here is the third list item

1. open the file containing the linux mascot  
2. marvel at its beauty
    ![Tux,the linux mascot](/asser/images/tux.png)

#分割线语法

单独一行上使用三个（***）且不能包含其他内容

***

# 链接语法

超链接语法 [Markdown语法](超链接地址 "超链接title")

这是一个链接  [markdown语法](https://markdown.com.cn "最好的markdown教程")

注意title和网站之间要用空格分开

使用尖括号可以直接渲染网址和邮箱

<https://youtube.com>

<sjc147258@qq.com>

强调链接

在链接的语法前后加上*号

I love supporting the **[EEF](https://eff.org)*

This is the *[Markdown guide](https://www.markdownguide.org)*

引用类型链接<br>
参考样式链接分为两部分：与文本内联的部分机器存储在文件其他位置的部分，以便于文本阅读  
* 链接的第一部分格式<br> 
    [hobbit-hole][1]
* 链接的第二部分格式<br>
    [1]: https//:en.wikipedia.org/wiki/Hobbit#lifesyle "hobbitlifestle"
 
 
 [hobbit-hole][1]

 [1]: https://en.wikipedia.org/wiki/Hobbit#lifestyle "hobbit lifestyle"

***

# 图片语法
插入图片的语法：！[图片alt](图片链接 "图片titile”)

![this picture](images/philly-magic-garden.9c0b4415.jpg "how beautifufl!!!")

给图片添加链接  
格式：将之前的语法全部框在[]中，并且将链接写在圆括号中

[![a picture](images/philly-magic-garden.9c0b4415.jpg "big")](https://en.wikipeadia.org)


# 转义字符语法

对于原本需要格式化markdown文档的字符，在字符前加入反斜杠

\*without the backslash,this would be a bullet in an unodered list.

- [x] write the press release\


:smile:

|a|b|
|---|---|
|1|2|
|>|2|












