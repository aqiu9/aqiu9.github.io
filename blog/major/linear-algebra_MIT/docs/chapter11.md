
# 第十一讲：矩阵空间、秩1矩阵和小世界图

## 矩阵空间

接上一讲，使用$$3 \times 3$$矩阵举例，其矩阵空间记为M。

则M的一组基为：
$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 1 \\
0 & 0 & 0 \\
0 & 0 & 0 \\
\end{bmatrix} \\
\begin{bmatrix}
0 & 0 & 0 \\
1 & 0 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0 \\
\end{bmatrix} \\
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
1 & 0 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 1 & 0 \\
\end{bmatrix}
\begin{bmatrix}
0 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 1 \\
\end{bmatrix} \\
$$

易得，dim M=9。

所以可以得出，对上讲中的三阶对称矩阵空间有dim S=6、上三角矩阵空间有dim U=6、对角矩阵空间有dim D=3

求并（intersect）：$$S \cup U=D, dim(S \cup U)=9$$；

求交（sum）：$$S \cap U=M, dim(S \cap U)=3$$；

可以看出：$$dim S + dim U=12=dim(S \cup U) + dim(S \cap U)$$。

另一个例子来自微分方程：

$$\frac{d^2y}{dx^2}+y=0$$，即y''+y=0

方程的解有：$$y=\cos{x}, \quad y=\sin{x}, \quad y=e^{ix}, \quad y=e^{-ix}$$等等（$$e^{ix}=\cos{x}+i\sin{x}, \quad e^{-ix}=\cos{x}-i\sin{x}$$）

而该方程的所有解：$$y=c_1 \cos{x} + c_2 \sin{x}$$。

所以，该方程的零空间的一组基为$$\cos{x}, \sin{x}$$，零空间的维数为2。同理$$e^{ix}, e^{-ix}$$可以作为另一组基。

## 秩一矩阵

$$2 \times 3$$矩阵$$A=\begin{bmatrix}1&4&5\\2&8&10\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}\begin{bmatrix}1&4&5\end{bmatrix}$$。

且$$dimC(A)=1=dimC(A^T)$$，所有的秩一矩阵都可以划为$$A=UV^T$$的形式，这里的U, V均为列向量。

秩一矩阵类似“积木”，可以搭建任何矩阵，如对于一个$$5 \times 17$$秩为4的矩阵，只需要4个秩一矩阵就可以组合出来。

令M代表所有$$5 \times 17$$，M中所有秩4矩阵组成的集合并不是一个子空间，通常两个秩四矩阵相加，其结果并不是秩四矩阵。

现在，在$$\mathbb{R}^4$$空间中有向量$$v=\begin{bmatrix}v_1\\v_2\\v_3\\v_4\end{bmatrix}$$，取$$\mathbb{R}^4$$中满足$$v_1+v_2+v_3+v_4=0$$的所有向量组成一个向量空间S，则S是一个向量子空间。

易看出，不论是使用系数乘以该向量，或是用两个满足条件的向量相加，其结果仍然落在分量和为零的向量空间中。

求S的维数：

从另一个角度看，$$v_1+v_2+v_3+v_4=0$$等价于$$\begin{bmatrix}1&1&1&1\end{bmatrix}\begin{bmatrix}v_1\\v_2\\v_3\\v_4\end{bmatrix}=0$$，则S就是$$A=\begin{bmatrix}1&1&1&1\end{bmatrix}$$的零空间。

rank(A)=1，则对其零空间有rank(N(A))=n-r=3=dim N(A)，则S的维数是3。

顺便看一下$$1 \times 4$$矩阵A的四个基本子空间：

行空间：$$dim C(A^T)=1$$，其中的一组基是$$\begin{bmatrix}1\\1\\1\\1\end{bmatrix}$$；

零空间：dim N(A)=3，其中的一组基是$$\begin{bmatrix}-1\\1\\0\\0\end{bmatrix}\begin{bmatrix}-1\\0\\1\\0\end{bmatrix}\begin{bmatrix}-1\\0\\0\\1\end{bmatrix}$$

列空间：dim C(A)=1，其中一组基是$$\begin{bmatrix}1\end{bmatrix}$$，可以看出列空间就是整个$$\mathbb{R}^1$$空间。

左零空间：$$dim N(A^T)=0$$，因为A转置后没有非零的v可以使Av=0成立，就是$$\begin{bmatrix}0\end{bmatrix}$$。

综上，$$dim C(A^T)+dim N(A)=4=n, dim C(A)+dim N(A^T)=1=m$$

## 小世界图

图（graph）由节点（node）与边（edge）组成。

假设，每个人是图中的一个节点，如果两个人为朋友关系，则在这两个人的节点间添加一条边，通常来说，从一个节点到另一个节点只需要不超过6步（即六条边）即可到达。
