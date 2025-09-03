# [0498. Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse)


> Medium

- array
- matrix
- simulation



## Question


<p>Given an <code>m x n</code> matrix <code>mat</code>, return <em>an array of all the elements of the array in a diagonal order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,4,7,5,3,6,8,9]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2],[3,4]]
<strong>Output:</strong> [1,2,3,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= mat[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>



## Solution

- time  : $O(M \times N)$
- space : $O(1)$, constant space apart from $O(N)$ return value

---

- Intuition: 
	- Simulate the process by traversing the grid in sprecified pattern
	- Starting from `(0,0)` to `(n,m)`
	- Let `lvl` be the level of diagonals starting at `lvl=1` for `(0,0)`:
		- For `lvl%2==1` : traverse from bottom left (BL) to top right (TR)
		- For `lvl%2==0` : traverse from TR to BL
	- When reaching border, change direction and `lvl+=1`
		- For `lvl%2==1` : when `r==0 or c==m-1`, if possible, move right > move down > return
		- For `lvl%2==0` : when `c==0 or r==n-1`, if possible, move down > move right > return
