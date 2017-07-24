# NumPy Tutorial

# NumPy - 简介

NumPy 是一个 Python 包。 它代表 “Numeric Python”。 它是一个由多维数组对象和用于处理数组的例程集合组成的库。

**Numeric**，即 NumPy 的前身，是由 Jim Hugunin 开发的。 也开发了另一个包 Numarray ，它拥有一些额外的功能。 2005年，Travis Oliphant 通过将 Numarray 的功能集成到 Numeric 包中来创建 NumPy 包。 这个开源项目有很多贡献者。

## NumPy 操作

使用NumPy，开发人员可以执行以下操作：

+   数组的算数和逻辑运算。

+   傅立叶变换和用于图形操作的例程。

+   与线性代数有关的操作。 NumPy 拥有线性代数和随机数生成的内置函数。

## NumPy – MatLab 的替代之一

NumPy 通常与 **SciPy**（Scientific Python）和 **Matplotlib**（绘图库）一起使用。 这种组合广泛用于替代 MatLab，是一个流行的技术计算平台。 但是，Python 作为 MatLab 的替代方案，现在被视为一种更加现代和完整的编程语言。

NumPy 是开源的，这是它的一个额外的优势。


[https://www.tutorialspoint.com/numpy/index.htm](https://www.tutorialspoint.com/numpy/index.htm)

https://github.com/wizardforcel/ts-numpy-tut-zh

# NumPy - 环境

> ### 在线尝试
> 
> 我们已经在线设置了 NumPy 编程环境，以便在线编译和执行所有可用的示例。 它向你提供了信心，并使您能够使用不同的选项验证程序， 随意修改任何示例并在线执行。
> 
> 使用我们的在线编译器尝试一下示例，它位于 [CodingGround](https://www.tutorialspoint.com/codingground.htm)
> 
> ```
> import numpy as np 
> a =  'hello world'  
> print a
> ```
> 
> 对于本教程中给出的大多数示例，你会在我们的网站代码部分的右上角找到一个`Try it`选项，这会把你带到在线编译器。 所以快来使用它，享受你的学习吧。

标准的 Python 发行版不会与 NumPy 模块捆绑在一起。 一个轻量级的替代方法是使用流行的 Python 包安装程序 **pip** 来安装 NumPy。

```
pip install numpy

```

启用 NumPy 的最佳方法是使用特定于您的操作系统的可安装的二进制包。 这些二进制包含完整的 SciPy 技术栈（包括 NumPy，SciPy，matplotlib，IPython，SymPy 以及 Python 核心自带的其它包）。

## Windows

Anaconda (from [www.continuum.io](https://www.continuum.io)) 是一个带有 SciPy 技术栈的免费 Python 发行版。 它也可用于 Linux 和 Mac.

Canopy ([www.enthought.com/products/canopy/](https://www.enthought.com/products/canopy/)) 是可用的免费和商业发行版，带有完整的 SciPy 技术栈，可用于 Windows, Linux and Mac。

Python (x,y): 是个免费的 Python 发行版，带有 SciPy 技术栈和 Spyder IDE，可用于 Windows。 (从这里下载：[www.python-xy.github.io/](https://python-xy.github.io/))

## Linux

Linux 发行版的相应软件包管理器可用于安装一个或多个 SciPy 技术栈中的软件包。

## 对于 Ubuntu

```
sudo apt-get install python-numpy 
python-scipy python-matplotlibipythonipythonnotebook python-pandas 
python-sympy python-nose

```

## 对于 Fedora

```
sudo yum install numpyscipy python-matplotlibipython 
python-pandas sympy python-nose atlas-devel

```

## 从源码构建

核心 Python（2.6.x，2.7.x 和 3.2.x 起）必须安装`distutils`，`zlib`模块应该启用。

GNU gcc（4.2及以上）C 编译器必须可用。

要安装 NumPy，请运行以下命令。

```
Python setup.py install

```

要测试 NumPy 模块是否正确安装，请尝试从 Python 提示符导入它。

如果未安装，将显示以下错误消息。


```
Traceback (most recent call last): 
   File "<pyshell#0>", line 1, in <module> 
      import numpy 
ImportError: No module named 'numpy'

```

或者，使用以下语法导入NumPy包。



# NumPy - Ndarray 对象

NumPy 中定义的最重要的对象是称为 `ndarray` 的 N 维数组类型。 它描述相同类型的元素集合。 可以使用基于零的索引访问集合中的项目。

`ndarray`中的每个元素在内存中使用相同大小的块。 `ndarray`中的每个元素是数据类型对象的对象（称为 `dtype`）。

从`ndarray`对象提取的任何元素（通过切片）由一个数组标量类型的 Python 对象表示。 下图显示了`ndarray`，数据类型对象（`dtype`）和数组标量类型之间的关系。

![Ndarray](https://www.tutorialspoint.com//numpy/images/ndarray.jpg)

`ndarray`类的实例可以通过本教程后面描述的不同的数组创建例程来构造。 基本的`ndarray`是使用 NumPy 中的数组函数创建的，如下所示：

```
numpy.array 

```

它从任何暴露数组接口的对象，或从返回数组的任何方法创建一个ndarray。

```
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

```

上面的构造器接受以下参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `object` 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列。 |
| 2. | `dtype` 数组的所需数据类型，可选。 |
| 3. | `copy` 可选，默认为`true`，对象是否被复制。 |
| 4. | `order` `C`（按行）、`F`（按列）或`A`（任意，默认）。 |
| 5. | `subok` 默认情况下，返回的数组被强制为基类数组。 如果为`true`，则返回子类。 |
| 6. | `ndimin` 指定返回数组的最小维数。 |

看看下面的例子来更好地理解。

## 示例 1

```
import numpy as np 
a = np.array([1,2,3])  
print a
```

输出如下：

```
[1, 2, 3]

```

## 示例 2

```
# 多于一个维度  
import numpy as np 
a = np.array([[1,  2],  [3,  4]])  
print a
```

输出如下：

```
[[1, 2] 
 [3, 4]]

```

## 示例 3

```
# 最小维度  
import numpy as np 
a = np.array([1,  2,  3,4,5], ndmin =  2)  
print a
```

输出如下：

```
[[1, 2, 3, 4, 5]]

```

## 示例 4

```
# dtype 参数  
import numpy as np 
a = np.array([1,  2,  3], dtype = complex)  
print a
```

输出如下：

```
[ 1.+0.j,  2.+0.j,  3.+0.j]

```

**ndarray ** 对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。 内存块以按行（C 风格）或按列（FORTRAN 或 MatLab 风格）的方式保存元素。




# NumPy - 数据类型

NumPy 支持比 Python 更多种类的数值类型。 下表显示了 NumPy 中定义的不同标量数据类型。

| 序号 | 数据类型及描述 |
| --- | --- |
| 1. | `bool_` 存储为一个字节的布尔值（真或假） |
| 2. | `int_` 默认整数，相当于 C 的`long`，通常为`int32`或`int64` |
| 3. | `intc` 相当于 C 的`int`，通常为`int32`或`int64` |
| 4. | `intp` 用于索引的整数，相当于 C 的`size_t`，通常为`int32`或`int64` |
| 5. | `int8` 字节（-128 ~ 127） |
| 6. | `int16` 16 位整数（-32768 ~ 32767） |
| 7. | `int32` 32 位整数（-2147483648 ~ 2147483647） |
| 8. | `int64` 64 位整数（-9223372036854775808 ~ 9223372036854775807） |
| 9. | `uint8` 8 位无符号整数（0 ~ 255） |
| 10. | `uint16` 16 位无符号整数（0 ~ 65535） |
| 11. | `uint32` 32 位无符号整数（0 ~ 4294967295） |
| 12. | `uint64` 64 位无符号整数（0 ~ 18446744073709551615） |
| 13. | `float_` `float64`的简写 |
| 14. | `float16` 半精度浮点：符号位，5 位指数，10 位尾数 |
| 15. | `float32` 单精度浮点：符号位，8 位指数，23 位尾数 |
| 16. | `float64` 双精度浮点：符号位，11 位指数，52 位尾数 |
| 17. | `complex_` `complex128`的简写 |
| 18. | `complex64` 复数，由两个 32 位浮点表示（实部和虚部） |
| 19. | `complex128` 复数，由两个 64 位浮点表示（实部和虚部） |

NumPy 数字类型是`dtype`（数据类型）对象的实例，每个对象具有唯一的特征。 这些类型可以是`np.bool_`，`np.float32`等。

## 数据类型对象 (`dtype`)

数据类型对象描述了对应于数组的固定内存块的解释，取决于以下方面：

*   数据类型（整数、浮点或者 Python 对象）

*   数据大小

*   字节序（小端或大端）

*   在结构化类型的情况下，字段的名称，每个字段的数据类型，和每个字段占用的内存块部分。

*   如果数据类型是子序列，它的形状和数据类型。

字节顺序取决于数据类型的前缀`<`或`>`。 `<`意味着编码是小端（最小有效字节存储在最小地址中）。 `>`意味着编码是大端（最大有效字节存储在最小地址中）。

`dtype`可由一下语法构造：

```
numpy.dtype(object, align, copy)

```

参数为：

*   `Object`：被转换为数据类型的对象。

*   `Align`：如果为`true`，则向字段添加间隔，使其类似 C 的结构体。

*   `Copy` ? 生成`dtype`对象的新副本，如果为`flase`，结果是内建数据类型对象的引用。

### 示例 1

```
# 使用数组标量类型  
import numpy as np 
dt = np.dtype(np.int32)  
print dt
```

输出如下：

```
int32

```

### 示例 2

```
#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。  
import numpy as np 

dt = np.dtype('i4')  
print dt 
```

输出如下：

```
int32

```

### 示例 3

```
# 使用端记号  
import numpy as np 
dt = np.dtype('>i4')  
print dt
```

输出如下：

```
>i4

```

下面的例子展示了结构化数据类型的使用。 这里声明了字段名称和相应的标量数据类型。

### 示例 4

```
# 首先创建结构化数据类型。  
import numpy as np 
dt = np.dtype([('age',np.int8)])  
print dt 
```

输出如下：

```
[('age', 'i1')] 

```

### 示例 5

```
# 现在将其应用于 ndarray 对象  
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt)  
print a
```

输出如下：

```
[(10,) (20,) (30,)]

```

### 示例 6

```
# 文件名称可用于访问 age 列的内容  
import numpy as np 

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt)  
print a['age']
```

输出如下：

```
[10 20 30]

```

### 示例 7

以下示例定义名为 **student** 的结构化数据类型，其中包含字符串字段`name`，**整数字段**`age`和**浮点字段**`marks`。 此`dtype`应用于`ndarray`对象。

```
import numpy as np 
student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')])  
print student
```

输出如下：

```
[('name', 'S20'), ('age', 'i1'), ('marks', '<f4')])

```

### 示例 8

```
import numpy as np 

student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')]) 
a = np.array([('abc',  21,  50),('xyz',  18,  75)], dtype = student)  
print a
```

输出如下：

```
[('abc', 21, 50.0), ('xyz', 18, 75.0)]

```

每个内建类型都有一个唯一定义它的字符代码：

*   `'b'`：布尔值

*   `'i'`：符号整数

*   `'u'`：无符号整数

*   `'f'`：浮点

*   `'c'`：复数浮点

*   `'m'`：时间间隔

*   `'M'`：日期时间

*   `'O'`：Python 对象

*   `'S', 'a'`：字节串

*   `'U'`：Unicode

*   `'V'`：原始数据（`void`）




# NumPy - 数组属性

这一章中，我们会讨论 NumPy 的多种数组属性。

## `ndarray.shape`

这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。

### 示例 1

```
import numpy as np 
a = np.array([[1,2,3],[4,5,6]])  
print a.shape
```

输出如下：

```
(2, 3)

```

### 示例 2

```
# 这会调整数组大小  
import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) a.shape =  (3,2)  
print a 
```

输出如下：

```
[[1, 2] 
 [3, 4] 
 [5, 6]]

```

### 示例 3

NumPy 也提供了`reshape`函数来调整数组大小。

```
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2)  
print b
```

输出如下：

```
[[1, 2] 
 [3, 4] 
 [5, 6]]

```

## `ndarray.ndim`

这一数组属性返回数组的维数。

### 示例 1

```
# 等间隔数字的数组  
import numpy as np 
a = np.arange(24)  print a
```

输出如下：

```
[0 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 17 18 19 20 21 22 23] 

```

### 示例 2

```
# 一维数组  
import numpy as np 
a = np.arange(24) a.ndim 
# 现在调整其大小
b = a.reshape(2,4,3)  
print b 
# b 现在拥有三个维度
```

输出如下：

```
[[[ 0,  1,  2] 
  [ 3,  4,  5] 
  [ 6,  7,  8] 
  [ 9, 10, 11]]  
  [[12, 13, 14] 
   [15, 16, 17]
   [18, 19, 20] 
   [21, 22, 23]]] 

```

## `numpy.itemsize`

这一数组属性返回数组中每个元素的字节单位长度。

### 示例 1

```
# 数组的 dtype 为 int8（一个字节）  
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.int8)  
print x.itemsize
```

输出如下：

```
1

```

### 示例 2

```
# 数组的 dtype 现在为 float32（四个字节）  
import numpy as np 
x = np.array([1,2,3,4,5], dtype = np.float32)  
print x.itemsize
```

输出如下：

```
4

```

## `numpy.flags`

`ndarray`对象拥有以下属性。这个函数返回了它们的当前值。

| 序号 | 属性及描述 |
| --- | --- |
| 1. | `C_CONTIGUOUS (C)` 数组位于单一的、C 风格的连续区段内 |
| 2. | `F_CONTIGUOUS (F)` 数组位于单一的、Fortran 风格的连续区段内 |
| 3. | `OWNDATA (O)` 数组的内存从其它对象处借用 |
| 4. | `WRITEABLE (W)` 数据区域可写入。 将它设置为`flase`会锁定数据，使其只读 |
| 5. | `ALIGNED (A)` 数据和任何元素会为硬件适当对齐 |
| 6. | `UPDATEIFCOPY (U)` 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新 |

### 示例

下面的例子展示当前的标志。

```
import numpy as np 
x = np.array([1,2,3,4,5])  
print x.flags
```

输出如下：

```
C_CONTIGUOUS : True 
F_CONTIGUOUS : True 
OWNDATA : True 
WRITEABLE : True 
ALIGNED : True 
UPDATEIFCOPY : False

```



# NumPy - 数组创建例程

新的`ndarray`对象可以通过任何下列数组创建例程或使用低级`ndarray`构造函数构造。

## `numpy.empty`

它创建指定形状和`dtype`的未初始化数组。 它使用以下构造函数：

```
numpy.empty(shape, dtype = float, order = 'C')

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `Shape` 空数组的形状，整数或整数元组 |
| 2. | `Dtype` 所需的输出数组类型，可选 |
| 3. | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |

### 示例

下面的代码展示空数组的例子：

```
import numpy as np 
x = np.empty([3,2], dtype =  int)  
print x
```

输出如下：

```
[[22649312    1701344351] 
 [1818321759  1885959276] 
 [16779776    156368896]]

```

**注意**：数组元素为随机值，因为它们未初始化。

## `numpy.zeros`

返回特定大小，以 0 填充的新数组。

```
numpy.zeros(shape, dtype = float, order = 'C')

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `Shape` 空数组的形状，整数或整数元组 |
| 2. | `Dtype` 所需的输出数组类型，可选 |
| 3. | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |

### 示例 1

```
# 含有 5 个 0 的数组，默认类型为 float  
import numpy as np 
x = np.zeros(5)  
print x
```

输出如下：

```
[ 0.  0.  0.  0.  0.]

```

### 示例 2

```
import numpy as np 
x = np.zeros((5,), dtype = np.int)  
print x
```

输出如下：

```
[0  0  0  0  0]

```

### 示例 3

```
# 自定义类型 
import numpy as np 
x = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'i4')])  
print x
```

输出如下：


```
[[(0,0)(0,0)]
 [(0,0)(0,0)]]         

```

## `numpy.ones`

返回特定大小，以 1 填充的新数组。

```
numpy.ones(shape, dtype = None, order = 'C')

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `Shape` 空数组的形状，整数或整数元组 |
| 2. | `Dtype` 所需的输出数组类型，可选 |
| 3. | `Order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |

### 示例 1

```
# 含有 5 个 1 的数组，默认类型为 float  
import numpy as np 
x = np.ones(5)  print x
```

输出如下：

```
[ 1.  1.  1.  1.  1.]

```

### 示例 2

```
import numpy as np 
x = np.ones([2,2], dtype =  int)  
print x
```

输出如下：

```
[[1  1] 
 [1  1]]

```



# NumPy - 来自现有数据的数组

这一章中，我们会讨论如何从现有数据创建数组。

## `numpy.asarray`

此函数类似于`numpy.array`，除了它有较少的参数。 这个例程对于将 Python 序列转换为`ndarray`非常有用。

```
numpy.asarray(a, dtype = None, order = None)

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `a` 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表 |
| 2. | `dtype` 通常，输入数据的类型会应用到返回的`ndarray` |
| 3. | `order` `'C'`为按行的 C 风格数组，`'F'`为按列的 Fortran 风格数组 |

下面的例子展示了如何使用`asarray`函数：

### 示例 1

```
# 将列表转换为 ndarray 
import numpy as np 

x =  [1,2,3] 
a = np.asarray(x)  
print a
```

输出如下：

```
[1  2  3] 

```

### 示例 2

```
# 设置了 dtype  
import numpy as np 

x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print a
```

输出如下：

```
[ 1.  2.  3.] 

```

### 示例 3

```
# 来自元组的 ndarray  
import numpy as np 

x =  (1,2,3) 
a = np.asarray(x)  
print a
```

输出如下：

```
[1  2  3]

```

### 示例 4

```
# 来自元组列表的 ndarray
import numpy as np 

x =  [(1,2,3),(4,5)] 
a = np.asarray(x)  
print a
```

输出如下：

```
[(1, 2, 3) (4, 5)]

```

## `numpy.frombuffer`

此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回`ndarray`。

```
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `buffer` 任何暴露缓冲区借口的对象 |
| 2. | `dtype` 返回数组的数据类型，默认为`float` |
| 3. | `count` 需要读取的数据数量，默认为`-1`，读取所有数据 |
| 4. | `offset` 需要读取的起始位置，默认为`0` |

### 示例

下面的例子展示了`frombuffer`函数的用法。

```
import numpy as np 
s =  'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print a
```

输出如下：

```
['H'  'e'  'l'  'l'  'o'  ' '  'W'  'o'  'r'  'l'  'd']

```

## `numpy.fromiter`

此函数从任何可迭代对象构建一个`ndarray`对象，返回一个新的一维数组。

```
numpy.fromiter(iterable, dtype, count = -1)

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `iterable` 任何可迭代对象 |
| 2. | `dtype` 返回数组的数据类型 |
| 3. | `count` 需要读取的数据数量，默认为`-1`，读取所有数据 |

以下示例展示了如何使用内置的`range()`函数返回列表对象。 此列表的迭代器用于形成` ndarray`对象。

### 示例 1

```
# 使用 range 函数创建列表对象  
import numpy as np 
list = range(5)  
print list
```

输出如下：

```
[0,  1,  2,  3,  4]

```

### 示例 2

```
# 从列表中获得迭代器  
import numpy as np 
list = range(5) 
it = iter(list)  
# 使用迭代器创建 ndarray 
x = np.fromiter(it, dtype =  float)  
print x
```

输出如下：

```
[0.   1.   2.   3.   4.]

```





# NumPy - 来自数值范围的数组

这一章中，我们会学到如何从数值范围创建数组。

## `numpy.arange`

这个函数返回`ndarray`对象，包含给定范围内的等间隔值。

```
numpy.arange(start, stop, step, dtype)

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `start` 范围的起始值，默认为`0` |
| 2. | `stop` 范围的终止值（不包含） |
| 3. | `step` 两个值的间隔，默认为`1` |
| 4. | `dtype` 返回`ndarray`的数据类型，如果没有提供，则会使用输入数据的类型。 |

下面的例子展示了如何使用该函数：

### 示例 1

```
import numpy as np
x = np.arange(5)  
print x
```

输出如下：

```
[0  1  2  3  4]

```

### 示例 2

```
import numpy as np
# 设置了 dtype
x = np.arange(5, dtype =  float)  
print x
```

输出如下：

```
[0.  1.  2.  3.  4.]

```

### 示例 3

```
# 设置了起始值和终止值参数  
import numpy as np
x = np.arange(10,20,2)  
print x
```

输出如下：

```
[10  12  14  16  18]

```

## `numpy.linspace`

此函数类似于`arange()`函数。 在此函数中，指定了范围之间的均匀间隔数量，而不是步长。 此函数的用法如下。

```
numpy.linspace(start, stop, num, endpoint, retstep, dtype)

```

构造器接受下列参数：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `start` 序列的起始值 |
| 2. | `stop` 序列的终止值，如果`endpoint`为`true`，该值包含于序列中 |
| 3. | `num` 要生成的等间隔样例数量，默认为`50` |
| 4. | `endpoint` 序列中是否包含`stop`值，默认为`ture` |
| 5. | `retstep` 如果为`true`，返回样例，以及连续数字之间的步长 |
| 6. | `dtype` 输出`ndarray`的数据类型 |

下面的例子展示了`linspace`函数的用法。

### 示例 1

```
import numpy as np
x = np.linspace(10,20,5)  
print x
```

输出如下：

```
[10.   12.5   15.   17.5  20.]

```

### 示例 2

```
# 将 endpoint 设为 false
import numpy as np
x = np.linspace(10,20,  5, endpoint =  False)  
print x
```

输出如下：

```
[10.   12.   14.   16.   18.]

```

### 示例 3

```
# 输出 retstep 值  
import numpy as np

x = np.linspace(1,2,5, retstep =  True)  
print x
# 这里的 retstep 为 0.25
```

输出如下：

```
(array([ 1.  ,  1.25,  1.5 ,  1.75,  2.  ]), 0.25)

```

## `numpy.logspace`

此函数返回一个`ndarray`对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10。

```
numpy.logscale(start, stop, num, endpoint, base, dtype)

```

`logspace`函数的输出由以下参数决定：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `start` 起始值是`base ** start` |
| 2. | `stop` 终止值是`base ** stop` |
| 3. | `num` 范围内的数值数量，默认为`50` |
| 4. | `endpoint` 如果为`true`，终止值包含在输出数组当中 |
| 5. | `base` 对数空间的底数，默认为`10` |
| 6. | `dtype` 输出数组的数据类型，如果没有提供，则取决于其它参数 |

下面的例子展示了`logspace`函数的用法。

### 示例 1

```
import numpy as np
# 默认底数是 10
a = np.logspace(1.0,  2.0, num =  10)  
print a
```

输出如下：

```
[ 10.           12.91549665     16.68100537      21.5443469  27.82559402      
  35.93813664   46.41588834     59.94842503      77.42636827    100.    ]

```

### 示例 2

```
# 将对数空间的底数设置为 2  
import numpy as np
a = np.logspace(1,10,num =  10,  base  =  2)  
print a
```

输出如下：

```
[ 2.     4.     8.    16.    32.    64.   128.   256.    512.   1024.]

```



# NumPy - 切片和索引

`ndarray`对象的内容可以通过索引或切片来访问和修改，就像 Python 的内置容器对象一样。

如前所述，`ndarray`对象中的元素遵循基于零的索引。 有三种可用的索引方法类型： **字段访问，基本切片**和**高级索引**。

基本切片是 Python 中基本切片概念到 n 维的扩展。 通过将`start`，`stop`和`step`参数提供给内置的`slice`函数来构造一个 Python `slice`对象。 此`slice`对象被传递给数组来提取数组的一部分。

## 示例 1

```
import numpy as np
a = np.arange(10)
s = slice(2,7,2)  
print a[s]
```

输出如下：

```
[2  4  6]

```

在上面的例子中，`ndarray`对象由`arange()`函数创建。 然后，分别用起始，终止和步长值`2`，`7`和`2`定义切片对象。 当这个切片对象传递给`ndarray`时，会对它的一部分进行切片，从索引`2`到`7`，步长为`2`。

通过将由冒号分隔的切片参数（`start:stop:step`）直接提供给`ndarray `对象，也可以获得相同的结果。

## 示例 2

```
import numpy as np
a = np.arange(10)
b = a[2:7:2]  
print b
```

输出如下：

```
[2  4  6]

```

如果只输入一个参数，则将返回与索引对应的单个项目。 如果使用`a:`，则从该索引向后的所有项目将被提取。 如果使用两个参数（以`:`分隔），则对两个索引（不包括停止索引）之间的元素以默认步骤进行切片。

## 示例 3

```
# 对单个元素进行切片  
import numpy as np

a = np.arange(10)
b = a[5]  
print b
```

输出如下：

```
5

```

## 示例 4

```
# 对始于索引的元素进行切片  
import numpy as np
a = np.arange(10)  
print a[2:]
```

输出如下：

```
[2  3  4  5  6  7  8  9]

```

## 示例 5

```
# 对索引之间的元素进行切片  
import numpy as np
a = np.arange(10)  
print a[2:5]
```

输出如下：

```
[2  3  4]

```

上面的描述也可用于多维`ndarray`。

## 示例 6

```
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print a
# 对始于索引的元素进行切片  
print  '现在我们从索引 a[1:] 开始对数组切片'  
print a[1:]
```

输出如下：

```
[[1 2 3]
 [3 4 5]
 [4 5 6]]

现在我们从索引 a[1:] 开始对数组切片
[[3 4 5]
 [4 5 6]]

```

切片还可以包括省略号（`...`），来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的`ndarray`。

## 示例 7

```
# 最开始的数组  
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print  '我们的数组是：'  
print a
print  '\n'  
# 这会返回第二列元素的数组：  
print  '第二列的元素是：'  
print a[...,1]  
print  '\n'  
# 现在我们从第二行切片所有元素：  
print  '第二行的元素是：'  
print a[1,...]  
print  '\n'  
# 现在我们从第二列向后切片所有元素：
print  '第二列及其剩余元素是：'  
print a[...,1:]
```

输出如下：

```
我们的数组是：
[[1 2 3]
 [3 4 5]
 [4 5 6]]

第二列的元素是：
[2 4 5]

第二行的元素是：
[3 4 5]

第二列及其剩余元素是：
[[2 3]
 [4 5]
 [5 6]]

```



# NumPy - 高级索引

如果一个`ndarray`是非元组序列，数据类型为整数或布尔值的`ndarray`，或者至少一个元素为序列对象的元组，我们就能够用它来索引`ndarray`。高级索引始终返回数据的副本。 与此相反，切片只提供了一个视图。

有两种类型的高级索引：整数和布尔值。

## 整数索引

这种机制有助于基于 N 维索引来获取数组中任意元素。 每个整数数组表示该维度的下标值。 当索引的元素个数就是目标`ndarray`的维度时，会变得相当直接。

以下示例获取了`ndarray`对象中每一行指定列的一个元素。 因此，行索引包含所有行号，列索引指定要选择的元素。

### 示例 1

```
import numpy as np 

x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  
print y
```

输出如下：

```
[1  4  5]

```

该结果包括数组中`(0,0)`，`(1,1)`和`(2,0)`位置处的元素。

下面的示例获取了 4X3 数组中的每个角处的元素。 行索引是`[0,0]`和`[3,3]`，而列索引是`[0,2]`和`[0,2]`。


### 示例 2

```
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print  '我们的数组是：'  
print x 
print  '\n' 
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  '这个数组的每个角处的元素是：'  
print y
```

输出如下：

```
我们的数组是：                                                                 
[[ 0  1  2]                                                                   
 [ 3  4  5]                                                                   
 [ 6  7  8]                                                                   
 [ 9 10 11]]

这个数组的每个角处的元素是：                                      
[[ 0  2]                                                                      
 [ 9 11]] 

```

返回的结果是包含每个角元素的`ndarray`对象。

高级和基本索引可以通过使用切片`:`或省略号`...`与索引数组组合。 以下示例使用`slice`作为列索引和高级索引。 当切片用于两者时，结果是相同的。 但高级索引会导致复制，并且可能有不同的内存布局。

### 示例 3

```
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print  '我们的数组是：'  
print x 
print  '\n'  
# 切片
z = x[1:4,1:3]  
print  '切片之后，我们的数组变为：'  
print z 
print  '\n'  
# 对列使用高级索引 
y = x[1:4,[1,2]] 
print  '对列使用高级索引来切片：'  
print y
```

输出如下：

```
我们的数组是：
[[ 0  1  2] 
 [ 3  4  5] 
 [ 6  7  8]
 [ 9 10 11]]

切片之后，我们的数组变为：
[[ 4  5]
 [ 7  8]
 [10 11]]

对列使用高级索引来切片：
[[ 4  5]
 [ 7  8]
 [10 11]] 

```

## 布尔索引

当结果对象是布尔运算（例如比较运算符）的结果时，将使用此类型的高级索引。

### 示例 1

这个例子中，大于 5 的元素会作为布尔索引的结果返回。

```
import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print  '我们的数组是：'  
print x 
print  '\n'  
# 现在我们会打印出大于 5 的元素  
print  '大于 5 的元素是：'  
print x[x >  5]
```

输出如下：

```
我们的数组是：
[[ 0  1  2] 
 [ 3  4  5] 
 [ 6  7  8] 
 [ 9 10 11]] 

大于 5 的元素是：
[ 6  7  8  9 10 11] 

```

### 示例 2

这个例子使用了`~`（取补运算符）来过滤`NaN`。

```
import numpy as np 
a = np.array([np.nan,  1,2,np.nan,3,4,5])  
print a[~np.isnan(a)]
```

输出如下：

```
[ 1.   2.   3.   4.   5.] 

```

### 示例 3

以下示例显示如何从数组中过滤掉非复数元素。

```
import numpy as np 
a = np.array([1,  2+6j,  5,  3.5+5j])  
print a[np.iscomplex(a)]
```

输出如下：

```
[2.0+6.j  3.5+5.j] 

```




# NumPy - 广播

术语**广播**是指 NumPy 在算术运算期间处理不同形状的数组的能力。 对数组的算术运算通常在相应的元素上进行。 如果两个阵列具有完全相同的形状，则这些操作被无缝执行。

## 示例 1

```
import numpy as np 

a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print c
```

输出如下：

```
[10   40   90   160]

```

如果两个数组的维数不相同，则元素到元素的操作是不可能的。 然而，在 NumPy 中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能。 较小的数组会**广播**到较大数组的大小，以便使它们的形状可兼容。

如果满足以下规则，可以进行广播：

*   `ndim`较小的数组会在前面追加一个长度为 1 的维度。

*   输出数组的每个维度的大小是输入数组该维度大小的最大值。

*   如果输入在每个维度中的大小与输出大小匹配，或其值正好为 1，则在计算中可它。

*   如果输入的某个维度大小为 1，则该维度中的第一个数据元素将用于该维度的所有计算。

如果上述规则产生有效结果，并且满足以下条件之一，那么数组被称为**可广播的**。

*   数组拥有相同形状。

*   数组拥有相同的维数，每个维度拥有相同长度，或者长度为 1。

*   数组拥有极少的维度，可以在其前面追加长度为 1 的维度，使上述条件成立。

下面的例称展示了广播的示例。

## 示例 2

```
import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
print  '第一个数组：'  
print a 
print  '\n'  
print  '第二个数组：'  
print b 
print  '\n'  
print  '第一个数组加第二个数组：'  
print a + b
```

输出如下：

```
第一个数组：
[[ 0. 0. 0.]
 [ 10. 10. 10.]
 [ 20. 20. 20.]
 [ 30. 30. 30.]]

第二个数组：
[ 1. 2. 3.]

第一个数组加第二个数组：
[[ 1. 2. 3.]
 [ 11. 12. 13.]
 [ 21. 22. 23.]
 [ 31. 32. 33.]]

```

下面的图片展示了数组`b`如何通过广播来与数组`a`兼容。

![array](https://www.tutorialspoint.com//numpy/images/array.jpg) 
