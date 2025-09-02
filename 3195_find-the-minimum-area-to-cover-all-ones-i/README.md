# [3195. Find the Minimum Area to Cover All Ones I](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i)


> Medium

- array
- matrix



## Question


<p>You are given a 2D <strong>binary</strong> array <code>grid</code>. Find a rectangle with horizontal and vertical sides with the<strong> smallest</strong> area, such that all the 1&#39;s in <code>grid</code> lie inside this rectangle.</p>

<p>Return the <strong>minimum</strong> possible area of the rectangle.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,0],[1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 279px; height: 198px;" /></p>

<p>The smallest rectangle has a height of 2 and a width of 3, so it has an area of <code>2 * 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0],[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 204px; height: 201px;" /></p>

<p>The smallest rectangle has both height and width 1, so its area is <code>1 * 1 = 1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> is either 0 or 1.</li>
	<li>The input is generated such that there is at least one 1 in <code>grid</code>.</li>
</ul>



## Solution

- Objective:
	- `r_max` and `r_min` of `1` with highest/lowest `row` value in `grid`
	- `c_max` and `c_min` of `1` with highest/lowest `col` value in `grid`
	- Return `(r_max - r_min + 1)*(c_max - c_min + 1)`

## Approach 1 - Finding first `1` in 4 direction

- time  : $O(2n*m)$
- space : $O(1)$

---

- Intuition:
	- Scan `grid` with nested loop of `row` and `col` in 4 direction:
		- `row` : `0..n`
		- `row` : `n..0`
		- `col` : `0..m`
		- `col` : `m..0`
		- Break when first `1` appeared
	- Worst case : only 1 `1` in `(m,n)` -- $\Theta (2 \times nm)$
	- Best case : only 2 `1` in `(0,0)`, `(m,n)` -- $\Theta (1)$


## Approach 2 - 1-pass scanning

- time  : $O(n*m)$
- space : $O(1)$

---

- Intuition:
	- Scan all cell in `grid` updating `r_max`, `r_min`, `c_max` and `c_min`
	- `max_y` is always increasing
	- All case : $O(m \times n)$