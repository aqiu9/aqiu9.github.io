
# 第六讲：列空间和零空间

对向量子空间S和T，有$$S \cap T$$也是向量子空间。

对$$m \times n$$矩阵A，$$n \times 1$$矩阵x，$$m \times 1$$矩阵b，运算Ax=b：

$$
\begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1(n-1)} & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2(n-1)} & a_{2n} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{m(n-1)} & a_{mn} \\
\end{bmatrix}
\cdot
\begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n-1} \\
x_{n} \\
\end{bmatrix}
=
\begin{bmatrix}
b_{1} \\
b_{2} \\
\vdots \\
b_{m} \\
\end{bmatrix}
$$

由A的列向量生成的子空间为A的列空间；

Ax=b有非零解当且仅当b属于A的列空间

A的零空间是Ax=0中x的解组成的集合。
