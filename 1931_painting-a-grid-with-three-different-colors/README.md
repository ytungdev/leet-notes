# [1931. Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors)


> Hard

- dynamic-programming



## Question


<p>You are given two integers <code>m</code> and <code>n</code>. Consider an <code>m x n</code> grid where each cell is initially white. You can paint each cell <strong>red</strong>, <strong>green</strong>, or <strong>blue</strong>. All cells <strong>must</strong> be painted.</p>

<p>Return<em> the number of ways to color the grid with <strong>no two adjacent cells having the same color</strong></em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png" style="width: 200px; height: 50px;" />
<pre>
<strong>Input:</strong> m = 1, n = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The three possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> m = 1, n = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The six possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> m = 5, n = 5
<strong>Output:</strong> 580986
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m &lt;= 5</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>



## Solution

- time  : $O(3^{2m} \cdot n)$
- space : $O(3^{2m})$

---

- Objectives:
	- Count number of way to paint a `mxn` grid with 3 colors where:
		- No adjacent cell in a `row` are with the same color -- (1)
		- No adjacent cell in a `col` are with the same color -- (2)

- Intuition:
	- With the constraint of `m<=5`, a single row can have at most $3^5$ permutations
		- In which at most $3 \times 2^{m-1}$ permutation are conforming to (1).
	- If any `grid[i][x] == grid[j][x]` for row `i,j` at col `x`, this pattern do not conform to (2)
	- Let `f[i][mask]` represent the number of ways to color rows 0 through i, where the i-th row's coloring scheme corresponds to the mask `mask`.
		- e.g. `f[2][mask]` denote total number of legit color scheme with `grid[2]==mask`
	- $T(mask,mask')=1$ if `mask` and `mask'` are conforming adjacent row else 0
	- $f[i][mask]= \sum_{mask'=0}^{m^3} \{f[i−1][mask'] \times T(mask,mask')\}$
		- `f[i][mask]` only depend on `f[i-1][mask]`
		- e.g. `f[2][mask]` = `f[1][next(mask)[0]] + .. + f[1][next(mask)[-1]]`
	- To find total number of conbination to row `n`:
		- Generate all conforming permutation for `row=0` (`mask`)
		- Then for each permutation, find all conforming next row (`mask'`)
		- For `i=0`:
			- `f_last = [1]*len(mask)`
		- For `i=1` to `i=n`:
			- `f_this = [0]*len(mask)`
			- For each `mask`:
				- For each `mask' of mask`:
					- `f_this += f_last[mask']`
			- `f_last = f_this`
- Optimizations:
	- Only consider row that conform to (1) in answer space instead of checking all $3^m$ column

		