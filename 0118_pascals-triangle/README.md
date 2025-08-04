# [0118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle)


> Easy

- array
- dynamic-programming



## Question


<p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>



## Solution

- time  : $O(N^2)$
- space : $O(N^2)$

---
```
Pascal's Triangle:
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

- Intuition:
	- let `dp[i][j]` be value of j-th element in i-th row
	- `len(dp[i]) = len(dp[i-1])+1`
	- for `j=0` : `dp[i][j] = 1`
	- for `j=n` : `dp[i][j] = 1`
	- for `0<j<n` : `dp[i][j] = dp[i-1][j] + dp[i-1][j-1]`