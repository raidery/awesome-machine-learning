

# NumPy - 算数运算

用于执行算术运算（如`add()`，`subtract()`，`multiply()`和`divide()`）的输入数组必须具有相同的形状或符合数组广播规则。

### 示例

```
import numpy as np 
a = np.arange(9, dtype = np.float_).reshape(3,3)  
print  '第一个数组：'  
print a 
print  '\n'  
print  '第二个数组：' 
b = np.array([10,10,10])  
print b 
print  '\n'  
print  '两个数组相加：'  
print np.add(a,b)  
print  '\n'  
print  '两个数组相减：'  
print np.subtract(a,b)  
print  '\n'  
print  '两个数组相乘：'  
print np.multiply(a,b)  
print  '\n'  
print  '两个数组相除：'  
print np.divide(a,b)
```

输出如下：

```
第一个数组：
[[ 0. 1. 2.]
 [ 3. 4. 5.]
 [ 6. 7. 8.]]

第二个数组：
[10 10 10]

两个数组相加：
[[ 10. 11. 12.]
 [ 13. 14. 15.]
 [ 16. 17. 18.]]

两个数组相减：
[[-10. -9. -8.]
 [ -7. -6. -5.]
 [ -4. -3. -2.]]

两个数组相乘：
[[ 0. 10. 20.]
 [ 30. 40. 50.]
 [ 60. 70. 80.]]

两个数组相除：
[[ 0. 0.1 0.2]
 [ 0.3 0.4 0.5]
 [ 0.6 0.7 0.8]]

```

让我们现在来讨论 NumPy 中提供的一些其他重要的算术函数。

## `numpy.reciprocal()`

此函数返回参数逐元素的倒数，。 由于 Python 处理整数除法的方式，对于绝对值大于 1 的整数元素，结果始终为 0， 对于整数 0，则发出溢出警告。

### 示例

```
import numpy as np 
a = np.array([0.25,  1.33,  1,  0,  100])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 reciprocal 函数：'  
print np.reciprocal(a)  
print  '\n' 
b = np.array([100], dtype =  int)  
print  '第二个数组：'  
print b 
print  '\n'  
print  '调用 reciprocal 函数：'  
print np.reciprocal(b)  
```

输出如下：

```
我们的数组是：                                                               
[   0.25    1.33    1.      0.    100.  ]                                     

调用 reciprocal 函数：                                         
main.py:9: RuntimeWarning: divide by zero encountered in reciprocal           
  print np.reciprocal(a)                                                      
[ 4.         0.7518797  1.               inf  0.01     ]                      

第二个数组：                                                      
[100]                                                                         

调用 reciprocal 函数：                                        
[0]                         

```

## `numpy.power()`

此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。

```
import numpy as np 
a = np.array([10,100,1000])  
print  '我们的数组是；'  
print a 
print  '\n'  
print  '调用 power 函数：'  
print np.power(a,2)  
print  '\n'  
print  '第二个数组：' 
b = np.array([1,2,3])  
print b 
print  '\n'  
print  '再次调用 power 函数：'  
print np.power(a,b)
```

输出如下：

```
我们的数组是；                                                              
[  10  100 1000]                                                              

调用 power 函数：                                                    
[    100   10000 1000000]                                                     

第二个数组：                                                              
[1 2 3]                                                                       

再次调用 power 函数：                                              
[        10      10000 1000000000] 

```

## `numpy.mod()`

此函数返回输入数组中相应元素的除法余数。 函数`numpy.remainder()`也产生相同的结果。

```
import numpy as np 
a = np.array([10,20,30]) 
b = np.array([3,5,7])  
print  '第一个数组：'  
print a 
print  '\n'  
print  '第二个数组：'  
print b 
print  '\n' 
print  '调用 mod() 函数：'  
print np.mod(a,b)  
print  '\n'  
print  '调用 remainder() 函数：'  
print np.remainder(a,b)  
```

输出如下：

```
第一个数组：
[10 20 30]

第二个数组：
[3 5 7]

调用 mod() 函数：                                                     
[1 0 2]

调用 remainder() 函数：                                              
[1 0 2]

```

以下函数用于对含有复数的数组执行操作。

* `numpy.real()` 返回复数类型参数的实部。

* `numpy.imag()` 返回复数类型参数的虚部。

* `numpy.conj()` 返回通过改变虚部的符号而获得的共轭复数。

* `numpy.angle()` 返回复数参数的角度。 函数的参数是`degree`。 如果为`true`，返回的角度以角度制来表示，否则为以弧度制来表示。

```
import numpy as np 
a = np.array([-5.6j,  0.2j,  11.  ,  1+1j])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 real() 函数：'  
print np.real(a)  
print  '\n'  
print  '调用 imag() 函数：'  
print np.imag(a)  
print  '\n'  
print  '调用 conj() 函数：'  
print np.conj(a)  
print  '\n'  
print  '调用 angle() 函数：'  
print np.angle(a)  
print  '\n'  
print  '再次调用 angle() 函数（以角度制返回）：'  
print np.angle(a, deg =  True)
```

输出如下：

```
我们的数组是：
[ 0.-5.6j 0.+0.2j 11.+0.j 1.+1.j ]

调用 real() 函数：
[ 0. 0. 11. 1.]

调用 imag() 函数：
[-5.6 0.2 0. 1. ]

调用 conj() 函数：
[ 0.+5.6j 0.-0.2j 11.-0.j 1.-1.j ]

调用 angle() 函数：
[-1.57079633 1.57079633 0. 0.78539816]

再次调用 angle() 函数（以角度制返回）：
[-90. 90. 0. 45.]

```



# NumPy - 统计函数

NumPy 有很多有用的统计函数，用于从数组中给定的元素中查找最小，最大，百分标准差和方差等。 函数说明如下：

## `numpy.amin()` 和 `numpy.amax()`

这些函数从给定数组中的元素沿指定轴返回最小值和最大值。

### 示例

```
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 amin() 函数：'  
print np.amin(a,1)  
print  '\n'  
print  '再次调用 amin() 函数：'  
print np.amin(a,0)  
print  '\n'  
print  '调用 amax() 函数：'  
print np.amax(a)  
print  '\n'  
print  '再次调用 amax() 函数：'  
print np.amax(a, axis =  0)
```

输出如下：

```
我们的数组是：
[[3 7 5]
[8 4 3]
[2 4 9]]

调用 amin() 函数：
[3 3 2]

再次调用 amin() 函数：
[2 4 3]

调用 amax() 函数：
9

再次调用 amax() 函数：
[8 7 9]

```

## `numpy.ptp()`

`numpy.ptp()`函数返回沿轴的值的范围（最大值 - 最小值）。

```
import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 ptp() 函数：'  
print np.ptp(a)  
print  '\n'  
print  '沿轴 1 调用 ptp() 函数：'  
print np.ptp(a, axis =  1)  
print  '\n'  
print  '沿轴 0 调用 ptp() 函数：'  
print np.ptp(a, axis =  0)  
```

输出如下：

```
我们的数组是：
[[3 7 5]
[8 4 3]
[2 4 9]]

调用 ptp() 函数：
7

沿轴 1 调用 ptp() 函数：
[4 5 7]

沿轴 0 调用 ptp() 函数：
[6 3 6]

```

## `numpy.percentile()`

百分位数是统计中使用的度量，表示小于这个值得观察值占某个百分比。 函数` numpy.percentile()`接受以下参数。

```
numpy.percentile(a, q, axis)

```

其中：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `a` 输入数组 |
| 2. | `q` 要计算的百分位数，在 0 ~ 100 之间 |
| 3. | `axis` 沿着它计算百分位数的轴 |

### 示例

```
import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 percentile() 函数：'  
print np.percentile(a,50)  
print  '\n'  
print  '沿轴 1 调用 percentile() 函数：'  
print np.percentile(a,50, axis =  1)  
print  '\n'  
print  '沿轴 0 调用 percentile() 函数：'  
print np.percentile(a,50, axis =  0)
```

输出如下：

```
我们的数组是：
[[30 40 70]
 [80 20 10]
 [50 90 60]]

调用 percentile() 函数：
50.0

沿轴 1 调用 percentile() 函数：
[ 40. 20. 60.]

沿轴 0 调用 percentile() 函数：
[ 50. 40. 60.]

```

## `numpy.median()`

**中值**定义为将数据样本的上半部分与下半部分分开的值。 `numpy.median()`函数的用法如下面的程序所示。

### 示例

```
import numpy as np 
a = np.array([[30,65,70],[80,95,10],[50,90,60]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 median() 函数：'  
print np.median(a)  
print  '\n'  
print  '沿轴 0 调用 median() 函数：'  
print np.median(a, axis =  0)  
print  '\n'  
print  '沿轴 1 调用 median() 函数：'  
print np.median(a, axis =  1)
```

输出如下：

```
我们的数组是：
[[30 65 70]
 [80 95 10]
 [50 90 60]]

调用 median() 函数：
65.0

沿轴 0 调用 median() 函数：
[ 50. 90. 60.]

沿轴 1 调用 median() 函数：
[ 65. 80. 60.]

```

## `numpy.mean()`

算术平均值是沿轴的元素的总和除以元素的数量。 ` numpy.mean()`函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。

### 示例

```
import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 mean() 函数：'  
print np.mean(a)  
print  '\n'  
print  '沿轴 0 调用 mean() 函数：'  
print np.mean(a, axis =  0)  
print  '\n'  
print  '沿轴 1 调用 mean() 函数：'  
print np.mean(a, axis =  1)
```

输出如下：

```
我们的数组是：
[[1 2 3]
 [3 4 5]
 [4 5 6]]

调用 mean() 函数：
3.66666666667

沿轴 0 调用 mean() 函数：
[ 2.66666667 3.66666667 4.66666667]

沿轴 1 调用 mean() 函数：
[ 2. 4. 5.]

```

## `numpy.average()`

加权平均值是由每个分量乘以反映其重要性的因子得到的平均值。 ` numpy.average()`函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。 该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。

考虑数组`[1,2,3,4]`和相应的权重`[4,3,2,1]`，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。

```
加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)
```

### 示例

```
import numpy as np 
a = np.array([1,2,3,4])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 average() 函数：'  
print np.average(a)  
print  '\n'  
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])  
print  '再次调用 average() 函数：'  
print np.average(a,weights = wts)  
print  '\n'  
# 如果 returned 参数设为 true，则返回权重的和  
print  '权重的和：'  
print np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True)
```

输出如下：

```
我们的数组是：
[1 2 3 4]

调用 average() 函数：
2.5

再次调用 average() 函数：
2.0

权重的和：
(2.0, 10.0)

```

在多维数组中，可以指定用于计算的轴。

### 示例

```
import numpy as np 
a = np.arange(6).reshape(3,2)  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '修改后的数组：' 
wt = np.array([3,5])  
print np.average(a, axis =  1, weights = wt)  
print  '\n'  
print  '修改后的数组：'  
print np.average(a, axis =  1, weights = wt, returned =  True)
```

输出如下：

```
我们的数组是：
[[0 1]
 [2 3]
 [4 5]]

修改后的数组：
[ 0.625 2.625 4.625]

修改后的数组：
(array([ 0.625, 2.625, 4.625]), array([ 8., 8., 8.]))

```

## 标准差

标准差是与均值的偏差的平方的平均值的平方根。 标准差公式如下：
```
std = sqrt(mean((x - x.mean())**2))

```

如果数组是`[1，2，3，4]`，则其平均值为`2.5`。 因此，差的平方是`[2.25,0.25,0.25,2.25]`，并且其平均值的平方根除以4，即`sqrt(5/4)`是`1.1180339887498949`。

### 示例

```
import numpy as np 
print np.std([1,2,3,4])
```

输出如下：

```
1.1180339887498949 

```

## 方差

方差是偏差的平方的平均值，即`mean((x - x.mean())** 2)`。 换句话说，标准差是方差的平方根。

### 示例

```
import numpy as np 
print np.var([1,2,3,4])
```

输出如下：

```
1.25

```




# NumPy - 排序、搜索和计数函数

NumPy中提供了各种排序相关功能。 这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。 下表显示了三种排序算法的比较。

| 种类 | 速度 | 最坏情况 | 工作空间 | 稳定性 |
| --- | --- | --- | --- | --- |
| `'quicksort'`（快速排序） | 1 | `O(n^2)` | 0 | 否 |
| `'mergesort'`（归并排序） | 2 | `O(n*log(n))` | ~n/2 | 是 |
| `'heapsort'`（堆排序） | 3 | `O(n*log(n))` | 0 | 否 |

## `numpy.sort()`

`sort()`函数返回输入数组的排序副本。 它有以下参数：

```
numpy.sort(a, axis, kind, order)

```

其中：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `a` 要排序的数组 |
| 2. | `axis` 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序 |
| 3. | `kind` 默认为`'quicksort'`（快速排序） |
| 4. | `order` 如果数组包含字段，则是要排序的字段 |

### 示例

```
import numpy as np  
a = np.array([[3,7],[9,1]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 sort() 函数：'  
print np.sort(a)  
print  '\n'  
print  '沿轴 0 排序：'  
print np.sort(a, axis =  0)  
print  '\n'  
# 在 sort 函数中排序字段 
dt = np.dtype([('name',  'S10'),('age',  int)]) 
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '按 name 排序：'  
print np.sort(a, order =  'name')
```

输出如下：

```
我们的数组是：
[[3 7]
 [9 1]]

调用 sort() 函数：
[[3 7]
 [1 9]]

沿轴 0 排序：
[[3 1]
 [9 7]]

我们的数组是：
[('raju', 21) ('anil', 25) ('ravi', 17) ('amar', 27)]

按 name 排序：
[('amar', 27) ('anil', 25) ('raju', 21) ('ravi', 17)]

```

## `numpy.argsort()`

`numpy.argsort()`函数对输入数组沿给定轴执行间接排序，并使用指定排序类型返回数据的索引数组。 这个索引数组用于构造排序后的数组。

### 示例

```
import numpy as np 
x = np.array([3,  1,  2])  
print  '我们的数组是：'  
print x 
print  '\n'  
print  '对 x 调用 argsort() 函数：' 
y = np.argsort(x)  
print y 
print  '\n'  
print  '以排序后的顺序重构原数组：'  
print x[y]  
print  '\n'  
print  '使用循环重构原数组：'  
for i in y:  
    print x[i],
```

输出如下：

```
我们的数组是：
[3 1 2]

对 x 调用 argsort() 函数：
[1 2 0]

以排序后的顺序重构原数组：
[1 2 3]

使用循环重构原数组：
1 2 3

```

## `numpy.lexsort()`

函数使用键序列执行间接排序。 键可以看作是电子表格中的一列。 该函数返回一个索引数组，使用它可以获得排序数据。 注意，最后一个键恰好是 sort 的主键。

### 示例

```
import numpy as np 

nm =  ('raju','anil','ravi','amar') 
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.') 
ind = np.lexsort((dv,nm))  
print  '调用 lexsort() 函数：'  
print ind 
print  '\n'  
print  '使用这个索引来获取排序后的数据：'  
print  [nm[i]  +  ", "  + dv[i]  for i in ind]  
```

输出如下：

```
调用 lexsort() 函数：
[3 1 0 2]

使用这个索引来获取排序后的数据：
['amar, f.y.', 'anil, s.y.', 'raju, f.y.', 'ravi, s.y.']

```

NumPy 模块有一些用于在数组内搜索的函数。 提供了用于找到最大值，最小值以及满足给定条件的元素的函数。

## `numpy.argmax()` 和 `numpy.argmin()`

这两个函数分别沿给定轴返回最大和最小元素的索引。

### 示例

```
import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 argmax() 函数：'  
print np.argmax(a)  
print  '\n'  
print  '展开数组：'  
print a.flatten()  
print  '\n'  
print  '沿轴 0 的最大值索引：' 
maxindex = np.argmax(a, axis =  0)  
print maxindex 
print  '\n'  
print  '沿轴 1 的最大值索引：' 
maxindex = np.argmax(a, axis =  1)  
print maxindex 
print  '\n'  
print  '调用 argmin() 函数：' 
minindex = np.argmin(a)  
print minindex 
print  '\n'  
print  '展开数组中的最小值：'  
print a.flatten()[minindex]  
print  '\n'  
print  '沿轴 0 的最小值索引：' 
minindex = np.argmin(a, axis =  0)  
print minindex 
print  '\n'  
print  '沿轴 1 的最小值索引：' 
minindex = np.argmin(a, axis =  1)  
print minindex
```

输出如下：

```
我们的数组是：
[[30 40 70]
 [80 20 10]
 [50 90 60]]

调用 argmax() 函数：
7

展开数组：
[30 40 70 80 20 10 50 90 60]

沿轴 0 的最大值索引：
[1 2 0]

沿轴 1 的最大值索引：
[2 0 1]

调用 argmin() 函数：
5

展开数组中的最小值：
10

沿轴 0 的最小值索引：
[0 1 1]

沿轴 1 的最小值索引：
[0 2 0]

```

## `numpy.nonzero()`

`numpy.nonzero()`函数返回输入数组中非零元素的索引。

### 示例

```
import numpy as np 
a = np.array([[30,40,0],[0,20,10],[50,0,60]])  
print  '我们的数组是：'  
print a 
print  '\n'  
print  '调用 nonzero() 函数：'  
print np.nonzero (a)
```

输出如下：

```
我们的数组是：
[[30 40 0]
 [ 0 20 10]
 [50 0 60]]

调用 nonzero() 函数：
(array([0, 0, 1, 1, 2, 2]), array([0, 1, 1, 2, 0, 2]))

```

## `numpy.where()`

`where()`函数返回输入数组中满足给定条件的元素的索引。

### 示例

```
import numpy as np 
x = np.arange(9.).reshape(3,  3)  
print  '我们的数组是：'  
print x 
print  '大于 3 的元素的索引：' 
y = np.where(x >  3)  
print y 
print  '使用这些索引来获取满足条件的元素：'  
print x[y]
```

输出如下：

```
我们的数组是：
[[ 0. 1. 2.]
 [ 3. 4. 5.]
 [ 6. 7. 8.]]

大于 3 的元素的索引：
(array([1, 1, 2, 2, 2]), array([1, 2, 0, 1, 2]))

使用这些索引来获取满足条件的元素：
[ 4. 5. 6. 7. 8.]

```

## `numpy.extract()`

`extract()`函数返回满足任何条件的元素。

```
import numpy as np 
x = np.arange(9.).reshape(3,  3)  
print  '我们的数组是：'  
print x 
# 定义条件 
condition = np.mod(x,2)  ==  0  
print  '按元素的条件值：'  
print condition 
print  '使用条件提取元素：'  
print np.extract(condition, x)
```

输出如下：

```
我们的数组是：
[[ 0. 1. 2.]
 [ 3. 4. 5.]
 [ 6. 7. 8.]]

按元素的条件值：
[[ True False True]
 [False True False]
 [ True False True]]

使用条件提取元素：
[ 0. 2. 4. 6. 8.]

```



# NumPy - 字节交换

我们已经看到，存储在计算机内存中的数据取决于 CPU 使用的架构。 它可以是小端（最小有效位存储在最小地址中）或大端（最小有效字节存储在最大地址中）。

## `numpy.ndarray.byteswap()`

`numpy.ndarray.byteswap()`函数在两个表示：大端和小端之间切换。

```
import numpy as np 
a = np.array([1,  256,  8755], dtype = np.int16)  
print  '我们的数组是：'  
print a 
print  '以十六进制表示内存中的数据：'  
print map(hex,a)  
# byteswap() 函数通过传入 true 来原地交换 
print  '调用 byteswap() 函数：'  
print a.byteswap(True)  
print  '十六进制形式：'  
print map(hex,a)  
# 我们可以看到字节已经交换了
```

输出如下：

```
我们的数组是：
[1 256 8755]

以十六进制表示内存中的数据：
['0x1', '0x100', '0x2233']

调用 byteswap() 函数：
[256 1 13090]

十六进制形式：
['0x100', '0x1', '0x3322']

```




# NumPy - 副本和视图

在执行函数时，其中一些返回输入数组的副本，而另一些返回视图。 当内容物理存储在另一个位置时，称为**副本**。 另一方面，如果提供了相同内存内容的不同视图，我们将其称为**视图**。

## 无复制

简单的赋值不会创建数组对象的副本。 相反，它使用原始数组的相同`id()`来访问它。 `id()`返回 Python 对象的通用标识符，类似于 C 中的指针。

此外，一个数组的任何变化都反映在另一个数组上。 例如，一个数组的形状改变也会改变另一个数组的形状。

### 示例

```
import numpy as np 
a = np.arange(6)  
print  '我们的数组是：'  
print a 
print  '调用 id() 函数：'  
print id(a)  
print  'a 赋值给 b：' 
b = a 
print b 
print  'b 拥有相同 id()：'  
print id(b)  
print  '修改 b 的形状：' 
b.shape =  3,2  
print b 
print  'a 的形状也修改了：'  
print a
```

输出如下：

```
我们的数组是：
[0 1 2 3 4 5]

调用 id() 函数：
139747815479536

a 赋值给 b：
[0 1 2 3 4 5]
b 拥有相同 id()：
139747815479536

修改 b 的形状：
[[0 1]
 [2 3]
 [4 5]]

a 的形状也修改了：
[[0 1]
 [2 3]
 [4 5]]

```

## 视图或浅复制

NumPy 拥有`ndarray.view()`方法，它是一个新的数组对象，并可查看原始数组的相同数据。 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。

### 示例

```
import numpy as np 
# 最开始 a 是个 3X2 的数组
a = np.arange(6).reshape(3,2)  
print  '数组 a：'  
print a 
print  '创建 a 的视图：' 
b = a.view()  
print b 
print  '两个数组的 id() 不同：'  
print  'a 的 id()：'  
print id(a)  
print  'b 的 id()：'  
print id(b)  
# 修改 b 的形状，并不会修改 a
b.shape =  2,3  
print  'b 的形状：'  
print b 
print  'a 的形状：'  
print a
```

输出如下：

```
数组 a：
[[0 1]
 [2 3]
 [4 5]]

创建 a 的视图：
[[0 1]
 [2 3]
 [4 5]]

两个数组的 id() 不同：
a 的 id()：
140424307227264
b 的 id()：
140424151696288

b 的形状：
[[0 1 2]
 [3 4 5]]

a 的形状：
[[0 1]
 [2 3]
 [4 5]]

```

数组的切片也会创建视图：

### 示例

```
import numpy as np 
a = np.array([[10,10],  [2,3],  [4,5]])  
print  '我们的数组：'  
print a 
print  '创建切片：' 
s = a[:,  :2]  
print s 
```

输出如下：

```
我们的数组：
[[10 10]
 [ 2 3]
 [ 4 5]]

创建切片：
[[10 10]
 [ 2 3]
 [ 4 5]]

```

## 深复制

`ndarray.copy()`函数创建一个深层副本。 它是数组及其数据的完整副本，不与原始数组共享。

### 示例

```
import numpy as np 
a = np.array([[10,10],  [2,3],  [4,5]])  
print  '数组 a：'  
print a 
print  '创建 a 的深层副本：' 
b = a.copy()  
print  '数组 b：'  
print b 
# b 与 a 不共享任何内容  
print  '我们能够写入 b 来写入 a 吗？'  
print b is a 
print  '修改 b 的内容：' 
b[0,0]  =  100  
print  '修改后的数组 b：'  
print b 
print  'a 保持不变：'  
print a
```

输出如下：

```
数组 a：
[[10 10]
 [ 2 3]
 [ 4 5]]

创建 a 的深层副本：
数组 b：
[[10 10]
 [ 2 3]
 [ 4 5]]
我们能够写入 b 来写入 a 吗？
False

修改 b 的内容：
修改后的数组 b：
[[100 10]
 [ 2 3]
 [ 4 5]]

a 保持不变：
[[10 10]
 [ 2 3]
 [ 4 5]]

```




# NumPy - 矩阵库

NumPy 包包含一个 Matrix库`numpy.matlib`。此模块的函数返回矩阵而不是返回`ndarray`对象。


## `matlib.empty()`

`matlib.empty()`函数返回一个新的矩阵，而不初始化元素。 该函数接受以下参数。

```
numpy.matlib.empty(shape, dtype, order)

```

其中：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `shape` 定义新矩阵形状的整数或整数元组 |
| 2. | `Dtype` 可选，输出的数据类型 |
| 3. | `order` `C` 或者 `F` |

### 示例

```
import numpy.matlib 
import numpy as np 
print np.matlib.empty((2,2))  
# 填充为随机数据
```

输出如下：

```
[[ 2.12199579e-314,   4.24399158e-314] 
 [ 4.24399158e-314,   2.12199579e-314]] 

```

## `numpy.matlib.zeros()`

此函数返回以零填充的矩阵。

```
import numpy.matlib 
import numpy as np 
print np.matlib.zeros((2,2))  
```

输出如下：

```
[[ 0.  0.] 
 [ 0.  0.]]) 

```

## `numpy.matlib.ones()`

此函数返回以一填充的矩阵。

```
import numpy.matlib 
import numpy as np 
print np.matlib.ones((2,2))
```

输出如下：

```
[[ 1.  1.] 
 [ 1.  1.]] 

```

## `numpy.matlib.eye()`

这个函数返回一个矩阵，对角线元素为 1，其他位置为零。 该函数接受以下参数。

```
numpy.matlib.eye(n, M,k, dtype)

```

其中：

| 序号 | 参数及描述 |
| --- | --- |
| 1. | `n` 返回矩阵的行数 |
| 2. | `M` 返回矩阵的列数，默认为`n` |
| 3. | `k` 对角线的索引 |
| 4. | `dtype` 输出的数据类型 |

### 示例

```
import numpy.matlib 
import numpy as np 
print np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float)
```

输出如下：

```
[[ 1.  0.  0.  0.] 
 [ 0.  1.  0.  0.] 
 [ 0.  0.  1.  0.]]) 

```

## `numpy.matlib.identity()`

`numpy.matlib.identity()`函数返回给定大小的单位矩阵。单位矩阵是主对角线元素都为 1 的方阵。

```
import numpy.matlib 
import numpy as np 
print np.matlib.identity(5, dtype =  float)
```

输出如下：

```
[[ 1.  0.  0.  0.  0.] 
 [ 0.  1.  0.  0.  0.] 
 [ 0.  0.  1.  0.  0.] 
 [ 0.  0.  0.  1.  0.] 
 [ 0.  0.  0.  0.  1.]] 

```

## `numpy.matlib.rand()`

·numpy.matlib.rand()`函数返回给定大小的填充随机值的矩阵。

### 示例

```
import numpy.matlib 
import numpy as np 
print np.matlib.rand(3,3)
```

输出如下：

```
[[ 0.82674464  0.57206837  0.15497519] 
 [ 0.33857374  0.35742401  0.90895076] 
 [ 0.03968467  0.13962089  0.39665201]]

```

注意，矩阵总是二维的，而`ndarray`是一个 n 维数组。 两个对象都是可互换的。

### 示例

```
import numpy.matlib 
import numpy as np  

i = np.matrix('1,2;3,4')  
print i 
```

输出如下：

```
[[1  2] 
 [3  4]]

```

### 示例

```
import numpy.matlib 
import numpy as np  

j = np.asarray(i)  
print j 
```

输出如下：

```
[[1  2] 
 [3  4]] 

```

### 示例

```
import numpy.matlib 
import numpy as np  

k = np.asmatrix (j)  
print k
```

输出如下：

```
[[1  2] 
 [3  4]]

```



# NumPy - 线性代数

NumPy 包包含`numpy.linalg`模块，提供线性代数所需的所有功能。 此模块中的一些重要功能如下表所述。

| 序号 | 函数及描述 |
| --- | --- |
| 1. | `dot` 两个数组的点积 |
| 2. | `vdot` 两个向量的点积 |
| 3. | `inner` 两个数组的内积 |
| 4. | `matmul` 两个数组的矩阵积 |
| 5. | `determinant` 数组的行列式 |
| 6. | `solve` 求解线性矩阵方程 |
| 7. | `inv` 寻找矩阵的乘法逆矩阵 |

## `numpy.dot()`

此函数返回两个数组的点积。 对于二维向量，其等效于矩阵乘法。 对于一维数组，它是向量的内积。 对于 N 维数组，它是`a`的最后一个轴上的和与`b`的倒数第二个轴的乘积。

```
import numpy.matlib 
import numpy as np 

a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
np.dot(a,b)
```

输出如下：

```
[[37  40] 
 [85  92]] 
```

要注意点积计算为：

```
[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
```

## `numpy.vdot()`

此函数返回两个向量的点积。 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数`id`是多维数组，它会被展开。

例子

```
import numpy as np 
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print np.vdot(a,b)
```

输出如下：

```
130
```

注意：`1*11 + 2*12 + 3*13 + 4*14 = 130`。

## `numpy.inner()`

此函数返回一维数组的向量内积。 对于更高的维度，它返回最后一个轴上的和的乘积。

例子

```
import numpy as np 
print np.inner(np.array([1,2,3]),np.array([0,1,0])) 
# 等价于 1*0+2*1+3*0
```

输出如下：

```
2
```

例子

```
# 多维数组示例 
import numpy as np 
a = np.array([[1,2], [3,4]]) 

print '数组 a：' 
print a 
b = np.array([[11, 12], [13, 14]]) 

print '数组 b：' 
print b 

print '内积：' 
print np.inner(a,b)
```

输出如下：

```
数组 a：
[[1 2]
[3 4]]

数组 b：
[[11 12]
[13 14]]

内积：
[[35 41]
[81 95]]
```

上面的例子中，内积计算如下：


```
1*11+2*12, 1*13+2*14 
3*11+4*12, 3*13+4*14 
```

## `numpy.matmul`

`numpy.matmul()`函数返回两个数组的矩阵乘积。 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。

另一方面，如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除。

例子

```
# 对于二维数组，它就是矩阵乘法
import numpy.matlib 
import numpy as np 

a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print np.matmul(a,b)
```

输出如下：

```
[[4  1] 
 [2  2]] 
```

例子

```
# 二维和一维运算
import numpy.matlib 
import numpy as np 

a = [[1,0],[0,1]] 
b = [1,2] 
print np.matmul(a,b) 
print np.matmul(b,a)
```

输出如下：

```
[1  2] 
[1  2] 
```

例子

```
# 维度大于二的数组 
import numpy.matlib 
import numpy as np 

a = np.arange(8).reshape(2,2,2) 
b = np.arange(4).reshape(2,2) 
print np.matmul(a,b)
```

输出如下：

```
[[[2   3] 
   [6   11]] 
  [[10  19] 
   [14  27]]]
```

## `numpy.linalg.det()`

行列式在线性代数中是非常有用的值。 它从方阵的对角元素计算。 对于 2×2 矩阵，它是左上和右下元素的乘积与其他两个的乘积的差。

换句话说，对于矩阵`[[a，b]，[c，d]]`，行列式计算为`ad-bc`。 较大的方阵被认为是 2×2 矩阵的组合。

`numpy.linalg.det()`函数计算输入矩阵的行列式。

例子

```
import numpy as np
a = np.array([[1,2], [3,4]]) 
print np.linalg.det(a)
```

输出如下：

```
-2.0
```

例子

```
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
print b 
print np.linalg.det(b) 
print 6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2)
```

输出如下：

```
[[ 6 1 1]
 [ 4 -2 5]
 [ 2 8 7]]

-306.0

-306
```

## `numpy.linalg.solve()`

`numpy.linalg.solve()`函数给出了矩阵形式的线性方程的解。

考虑以下线性方程：

```
x + y + z = 6

2y + 5z = -4

2x + 5y - z = 27
```

可以使用矩阵表示为：

![](http://upload-images.jianshu.io/upload_images/118142-7ab3daa7f65551e6.jpg)

如果矩阵成为`A`、`X`和`B`，方程变为：

```
AX = B  
```

或

```
X = A^(-1)B 
```

## `numpy.linalg.inv()`

我们使用`numpy.linalg.inv()`函数来计算矩阵的逆。 矩阵的逆是这样的，如果它乘以原始矩阵，则得到单位矩阵。

例子

```
import numpy as np 

x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print x 
print y 
print np.dot(x,y)
```

输出如下：

```
[[1 2]                                                                        
 [3 4]]                                                                       
[[-2.   1. ]                                                                  
 [ 1.5 -0.5]]                                                                 
[[  1.00000000e+00   1.11022302e-16]                                          
 [  0.00000000e+00   1.00000000e+00]]
```

例子

现在让我们在示例中创建一个矩阵A的逆。

```
import numpy as np 
a = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 

print '数组 a：'
print a 
ainv = np.linalg.inv(a) 

print 'a 的逆：' 
print ainv  

print '矩阵 b：' 
b = np.array([[6],[-4],[27]]) 
print b 

print '计算：A^(-1)B：' 
x = np.linalg.solve(a,b) 
print x  
# 这就是线性方向 x = 5, y = 3, z = -2 的解
```

输出如下：

```
数组 a：
[[ 1 1 1]
 [ 0 2 5]
 [ 2 5 -1]]

a 的逆：
[[ 1.28571429 -0.28571429 -0.14285714]
 [-0.47619048 0.14285714 0.23809524]
 [ 0.19047619 0.14285714 -0.0952381 ]]

矩阵 b：
[[ 6]
 [-4]
 [27]]

计算：A^(-1)B：
[[ 5.]
 [ 3.]
 [-2.]]
```

结果也可以使用下列函数获取

```
x = np.dot(ainv,b)
```


