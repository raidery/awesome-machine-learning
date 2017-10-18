
# 机器学习笔记

## 简介

> 作者：李金 <br>
> 版本：0.0.1<br>
> 邮件：lijinwithyou@gmail.com

机器学习笔记，使用 `jupyter notebook (ipython notebook)` 进行展示。

`Github` 加载 `.ipynb` 的速度较慢，建议在 [Nbviewer](http://nbviewer.jupyter.org/github/lijin-THU/notes-machine-learning/blob/master/ReadMe.ipynb) 中查看该项目。

----

## 目录

第一部分来自 `Bishop` 的经典书籍 `Pattern Recognition and Machine Learning`。

第二部分来自 `Bengio` 的最新书籍 `Deep Learning`。

### 第一部分 PRML 笔记

- [1. 简介](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction)
    - [1.1. 例子：多项式拟合](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-01-Example-Polynomial-Curve-Fitting.ipynb)
    - [1.2. 概率论](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb)
        - [1.2.1. 概率密度函数](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.1-概率密度函数)
        - [1.2.2. 期望和方差](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.2-期望和方差)
        - [1.2.3. Bayes 概率](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.3-Bayes-概率)
        - [1.2.4. 高斯分布](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.4-高斯分布)
        - [1.2.5. 重新理解曲线拟合](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.5-重新理解曲线拟合)
        - [1.2.6. Bayes 曲线拟合](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-02-Probability-Theory.ipynb#1.2.6-Bayes-曲线拟合)
    - [1.3. 模型选择](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-03-Model-Selection.ipynb)
    - [1.4. 维数灾难](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-04-The-Curse-of-Dimensionality.ipynb)
    - [1.5. 决策理论](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb)
        - [1.5.1. 最小错误率决策](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb#1.5.1-最小错误率决策)
        - [1.5.2. 最小风险决策](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb#1.5.2-最小风险决策)
        - [1.5.3. 拒绝选项](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb#1.5.3-拒绝选项)
        - [1.5.4. 推断和决策](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb#1.5.4-推断和决策)
        - [1.5.5. 回归问题的损失函数](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-05-Decision-Theory.ipynb#1.5.5-回归问题的损失函数)
    - [附录 D 变分法](Pattern-Recognition-and-Machine-Learning/Appendix/Appendix-D-Calculus-of-Variations.ipynb)
    - [1.6. 信息论](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-06-Information-Theory.ipynb)
        - [1.6.1. 相对熵和互信息](Pattern-Recognition-and-Machine-Learning/Chap-01-Introduction/01-06-Information-Theory.ipynb#1.6.1-相对熵和互信息)
    - [附录 E Lagrange 乘子](Pattern-Recognition-and-Machine-Learning/Appendix/Appendix-E-Lagrange-Multipliers.ipynb)
- [2. 概率分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions)
    - [2.1. 二元变量](PRML/Chap-02-Probability-Distributions/02-01-Binary-Variables.ipynb)
        - [2.1.1. Beta 分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-01-Binary-Variables.ipynb#2.1.1-Beta-分布)
    - [2.2. 多元变量](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-02-Multinomial-Variables.ipynb)
        - [2.2.1. 狄利克雷分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-02-Multinomial-Variables.ipynb#2.2.1-狄利克雷分布)
    - [2.3. 高斯分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb)
        - [2.3.1. 条件高斯分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.1-条件高斯分布)
        - [2.3.2. 边缘高斯分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.2-边缘高斯分布)
        - [2.3.3. 高斯变量的贝叶斯理论](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.3-高斯变量的贝叶斯理论)
        - [2.3.4. 高斯分布最大似然](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.4-高斯分布最大似然)
        - [2.3.5. 序列估计](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.5-序列估计)
        - [2.3.6. 高斯分布的贝叶斯估计](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.6-高斯分布的贝叶斯估计)
        - [2.3.7. 学生 t 分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.7-学生-t-分布)
        - [2.3.8. 周期变量和 von Mises 分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.8-周期变量和-von-Mises-分布)
        - [2.3.9. 高斯混合模型](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-03-The-Gaussian-Distribution.ipynb#2.3.9-高斯混合模型)
    - [2.4. 指数族分布](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-04-The-Exponential-Family.ipynb)
        - [2.4.1. 最大似然和充分统计量](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-04-The-Exponential-Family.ipynb#2.4.1-最大似然和充分统计量)
        - [2.4.2. 共轭先验](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-04-The-Exponential-Family.ipynb#2.4.2-共轭先验)
        - [2.4.3. 无信息先验](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-04-The-Exponential-Family.ipynb#2.4.3-无信息先验)
    - [2.5. 非参数方法](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-05-Nonparametric-Methods.ipynb)
        - [2.5.1. 核密度估计量](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-05-Nonparametric-Methods.ipynb#2.5.1-核密度估计量)
        - [2.5.2. 近邻方法](Pattern-Recognition-and-Machine-Learning/Chap-02-Probability-Distributions/02-05-Nonparametric-Methods.ipynb#2.5.2-近邻方法)
- [3. 线性回归模型](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression)        
    - [3.1. 线性基函数回归模型](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb)
        - [3.1.1. 最大似然和最小二乘](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb#3.1.1-最大似然和最小二乘)
        - [3.1.2. 最小二乘的几何表示](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb#3.1.2-最小二乘的几何表示)
        - [3.1.3. 序贯学习](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb#3.1.3-序贯学习)
        - [3.1.4. 带正则的最小二乘](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb#3.1.4-带正则的最小二乘)
        - [3.1.5. 多维输出](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-01-Linear-Basis-Function-Models.ipynb#3.1.5-多维输出)
    - [3.2 Bias-Variance 分解](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-02-The-Bias-Variance-Decomposition.ipynb)
    - [3.3 Bayes 线性回归](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-03-Bayesian-Linear-Regression.ipynb)
        - [3.3.1. 参数的分布](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-03-Bayesian-Linear-Regression.ipynb#3.3.1-参数的分布)
        - [3.3.2. 预测值的分布](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-03-Bayesian-Linear-Regression.ipynb#3.3.2-预测值的分布)
        - [3.3.3. 等价核](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-03-Bayesian-Linear-Regression.ipynb#3.3.3-等价核)
    - [3.4 贝叶斯模型的比较](Pattern-Recognition-and-Machine-Learning/Chap-03-Linear-Models-for-Regression/03-04-Bayesian-Model-Comparison.ipynb)
- [4. 线性分类模型](Pattern-Recognition-and-Machine-Learning/Chap-04-Linear-Models-for-Classification)
    - [4.1 判别函数](Pattern-Recognition-and-Machine-Learning/Chap-04-Linear-Models-for-Classification/04-01-Discriminant-Functions.ipynb)

### 第二部分 DP 笔记

- [I 数学和机器学习基础](Deep-Learning/Part-I)
    - [2. 线性代数](Deep-Learning/Part-I/Chap-02-Linear-Algebra)
        - [2.1 标量，向量，矩阵和张量](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-01-Scalars-Vectors-Matrices-and-Tensors.ipynb)
        - [2.2 矩阵乘法](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-02-Multiplying-Matrices-and-Vectors.ipynb)
        - [2.2 单位矩阵和逆](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-03-Identity-and-Inverse-Matrices.ipynb)
        - [2.4 线性无关和生成空间](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-04-Linear-Dependence-and-Span.ipynb)
        - [2.5 范数](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-05-Norms.ipynb)
        - [2.6 特殊矩阵和向量](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-06-Special-Kinds-of-Matrices-and-Vectors.ipynb)
        - [2.7 特征值分解](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-07-Eigendecomposition.ipynb)
        - [2.8 奇异值分解](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-08-Singular-Value-Decomposition.ipynb)
        - [2.9 Moore-Penrose 伪逆](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-09-The-Moore-Penrose-Pseudoinverse.ipynb)
        - [2.10 矩阵的迹](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-10-The-Trace-Operator.ipynb)
        - [2.11 行列式](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-11-The-Determinant.ipynb)
        - [2.12 例子：主成分分析](Deep-Learning/Part-I/Chap-02-Linear-Algebra/02-12-Example-Principal-Components-Analysis.ipynb)

----

## 参考资料和文献：

[1] Christopher, M. Bishop. "Pattern recognition and machine learning." Company New York 16.4 (2006): 049901.

[2] Goodfellow I, Bengio Y, Courville A. Deep learning[J]. 2015, 2016.
