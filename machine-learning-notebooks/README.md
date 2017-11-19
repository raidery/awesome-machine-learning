## Machine learning notebooks

This project contains solutions to the [Stanford Machine Learning](https://www.coursera.org/learn/machine-learning) 
course exercises implemented with [Python](https://www.python.org/) and [scikit-learn](http://scikit-learn.org/). The scikit-learn 
machine learning library provides optimized implementations for all algorithms presented in the course and needed in 
the course exercises. Instead of writing low-level [Octave](https://www.gnu.org/software/octave/) code, as required by 
the course, the solutions presented here demonstrate how to use scikit-learn to solve these exercises on a much higher 
level. It is a level that is closer to that of real-world machine learning projects. This project respects the 
[Coursera Honor Code](https://learner.coursera.help/hc/en-us/articles/209818863-Coursera-Honor-Code) as the presented 
solutions can't be used to derive the lower-level Octave code that must be written to complete the assignments. 

I developed these solutions while learning Python and its 
[scientific programming libraries](https://www.scipy.org/) such as [NumPy](http://www.numpy.org/), 
[SciPy](https://scipy.org/scipylib/index.html), [pandas](http://pandas.pydata.org/) and 
[matplotlib](http://matplotlib.org/) in a machine learning context. The solutions are provided as 
[Jupyter](http://jupyter.org/) Python notebooks. Developers new to scikit-learn hopefully find them useful to see how 
the machine learning topics covered in the course relate to the 
[scikit-learn API](http://scikit-learn.org/stable/modules/classes.html). In their current state, the notebooks neither 
explain machine learning basics nor introduce the used libraries. For learning machine learning basics I highly 
recommend attending the course lectures. For an introduction to the used libraries the following tutorials are a good 
starting point: 

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [NumPy tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
- [SciPy tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/index.html)
- [Pandas tutorial](http://pandas.pydata.org/pandas-docs/stable/10min.html)
- [Pyplot tutorial](http://matplotlib.org/users/pyplot_tutorial.html)
- [Scikit-learn tutorials](http://scikit-learn.org/stable/tutorial/index.html)

### Course exercises

- [Exercise 1 notebook](ml-ex1.ipynb): Linear regression ([ex1.pdf](data/ml-ex1/ex1.pdf))
- [Exercise 2 notebook](ml-ex2.ipynb): Logistic regression ([ex2.pdf](data/ml-ex2/ex2.pdf))
- [Exercise 3 notebook](ml-ex3.ipynb): Multi-class classification and neural networks ([ex3.pdf](data/ml-ex3/ex3.pdf))
- [Exercise 4 notebook](ml-ex4.ipynb): Neural networks learning ([ex4.pdf](data/ml-ex4/ex4.pdf))
- [Exercise 5 notebook](ml-ex5.ipynb): Regularized linear regression and bias vs. variance ([ex5.pdf](data/ml-ex5/ex5.pdf))
- [Exercise 6 notebook](ml-ex6.ipynb): Support vector machines ([ex6.pdf](data/ml-ex6/ex6.pdf))
- [Exercise 7 notebook](ml-ex7.ipynb): K-means clustering and principal component analysis ([ex7.pdf](data/ml-ex7/ex7.pdf))
- [Exercise 8 notebook](ml-ex8.ipynb): Anomaly detection and recommender systems ([ex8.pdf](data/ml-ex8/ex8.pdf))


https://github.com/krasserm/machine-learning-notebooks

# 机器学习笔记

## 简介

**作者：子实**

机器学习笔记，使用 `jupyter notebook (ipython notebook)` 编写展示。

`Github` 加载 `.ipynb` 的速度较慢，建议在 [Nbviewer](http://nbviewer.jupyter.org/github/zlotus/notes-LSJU-machine-learning/blob/master/ReadMe.ipynb?flush_cache=true) 中查看该项目。

----

## 目录

来自斯坦福网络课程《机器学习》的笔记，可以在[斯坦福大学公开课：机器学习课程](http://open.163.com/special/opencourse/machinelearning.html)观看。

根据视频内容，对每一讲的名称可能会有所更改（以更好的体现各讲的教学内容）。

- 【第1讲】 机器学习的动机与应用（主要是课程要求与应用范例，没有涉及机器学习的具体计算内容）
- 【第2讲】 [监督学习应用-线性回归](chapter02.ipynb)
- 【第3讲】 [线性回归的概率解释、局部加权回归、逻辑回归](chapter03.ipynb)
- 【第4讲】 [牛顿法、一般线性模型](chapter04.ipynb)
- 【第5讲】 [生成学习算法、高斯判别分析、朴素贝叶斯算法](chapter05.ipynb)
- 【第6讲】 [事件模型、函数间隔与几何间隔](chapter06.ipynb)
- 【第7讲】 [最优间隔分类器、拉格朗日对偶、支持向量机](chapter07.ipynb)
- 【第8讲】 [核方法、序列最小优化算法](chapter08.ipynb)
- 【第9讲】 [经验风险最小化](chapter09.ipynb)
- 【第10讲】 [交叉验证、特征选择](chapter10.ipynb)
- 【第11讲】 [贝叶斯统计、机器学习应用建议](chapter11.ipynb)
- 【第12讲】 [$k$-means算法、高斯混合模型及最大期望算法](chapter12.ipynb)
- 【第13讲】 [最大期望算法及其应用、因子分析模型](chapter13.ipynb)
- 【第14讲】 [因子分析的EM算法、主成分分析](chapter14.ipynb)
- 【第15讲】 [PCA的奇异值分解、独立成分分析](chapter15.ipynb)
- 【第16讲】 [马尔可夫决策过程](chapter16.ipynb)
- 【第17讲】 [解连续状态的MDP](chapter17.ipynb)
- 【第18讲】 [线性二次调节](chapter18.ipynb)
- 【第19讲】 [微分动态规划及线性二次型高斯](chapter19.ipynb)
- 【第20讲】 [策略搜索算法](chapter20.ipynb)

----

- 【参考笔记1】 线性代数复习及参考
- 【参考笔记2】 [概率论复习](sn02.ipynb)
- 【参考笔记3】 MATLAB入门
- 【参考笔记4】 凸优化概述1
- 【参考笔记5】 凸优化概述2
- 【参考笔记6】 [隐式马尔可夫模型](sn06.ipynb)
- 【参考笔记7】 [多元高斯分布](sn07.ipynb)
- 【参考笔记8】 [更多关于多元高斯分布的知识](sn08.ipynb)
- 【参考笔记9】 高斯过程

笔记格式借鉴[Jin Li](https://github.com/lijin-THU/)的[机器学习笔记](https://github.com/lijin-THU/notes-machine-learning)。
