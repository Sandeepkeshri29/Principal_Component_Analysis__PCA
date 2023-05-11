# Principal_Component_Analysis__PCA
PCA[Theory]

Principle Component Analysis
Probably the most known one. It is based on eigen decomposition.
Let's consider the set of vectors { 
 } that represent our data
 

Step 1 : Compute the mean and substract it to get data with null Esperance

Step 2 : Compute the covariance matrix

Step 3 : Eigen decomposition
For a matrix M, an eigen value 
 with the associated eigen vector 
 verify 
.
Recall: (Spectral theorem) For a symmetric matrix M, there is an eigen decomposition:

where 
 is the i-th eigen value with 
 the associated eigen vector. Furthermore, the eigen values are real.
The covariance matrix 
 is symmetric, so we can apply the eigen decomposition 
 with 
Step 4 : Projection onto eigenvectors
Let's consider that we want to reduce the dimension from n to m. We just need to project the data onto the m first eigen vectors because they have the highest eigen values. We then get the result:

But what about Kernel?
Let's consider a kernel with the expression 
. For instance a gaussian kernel can be written as 
We can define 
 and consider the matrix 
You may be able to better understand the PCA now.
