# [0073. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes)


> Medium

- array
- hash-table
- matrix



## Question


<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>&#39;s.</p>

<p>You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;" />
<pre>
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;" />
<pre>
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[0].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>A straightforward solution using <code>O(mn)</code> space is probably a bad idea.</li>
	<li>A simple improvement uses <code>O(m + n)</code> space, but still not the best solution.</li>
	<li>Could you devise a constant space solution?</li>
</ul>



## Solution

- time  : $O(2MN)$
- space : $O(1)$

---

- Intuition:
	- Without additional space, we need to mark columns and rows that contain zero within `matrix`
	- For each cell `matrix[r][c]`, we need to compare it with 2 flag to decide setting it to zero or not.
	- Use first row `matrix[0]` to flag column that contain zero:
		- `matrix[0][c]=0` if column `c` contain zero.
	- Use first col of each row `matrix[r][0]` to flag whether the row contain zero:
		- `matrix[r][0]=0` if row `r` contain zero.
	- This way can transform every cell without additional space, except first row
		- Original data in first row are lost and overwritten by flags
		- We cannot rely on row flag `matrix[r][0]` for `r=0`
	- To handle setting zero in first row, we flag it with additional variable
		- `setFirstRow=True` if first row `matrix[0]` contain zero.
		- Still in $O(1)$ space
- Implementation:
	- Iterate through every cell `matrix[r][c]` to scan and flag for zeros: -- $O(MN)$
		- for `r` in `[0..m)` and `c` in `[0..n)`
		- If `matrix[r][c]==0` and `r==0` : `setFirstRow=True`
		- If `matrix[r][c]==0` and `r!=0` : flag with `matrix[r][0]=0` and `matrix[0][c]=0`
	- Iterate through every cell `matrix[r][c]` to set zero if needed: -- $O(MN)$
		- for `r` in `(m..0)` and `c` in `(n..0]`
			- To set row flag after setting all other element in a row
		- If `matrix[r][0]==0` or `matrix[0][c]==0` : set `matrix[r][c]` to 0
	- If `setFirstRow=True`, set each element in first row to 0 .