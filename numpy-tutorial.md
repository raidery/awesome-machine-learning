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


