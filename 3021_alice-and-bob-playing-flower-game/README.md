# [3021. Alice and Bob Playing Flower Game](https://leetcode.com/problems/alice-and-bob-playing-flower-game)


> Medium

- math



## Question


<p>Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are <code>x</code> flowers in the first lane between Alice and Bob, and <code>y</code> flowers in the second lane between them.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/08/27/3021.png" style="width: 300px; height: 150px;" /></p>

<p>The game proceeds as follows:</p>

<ol>
	<li>Alice takes the first turn.</li>
	<li>In each turn, a player must choose either one of the lane&nbsp;and pick one flower from that side.</li>
	<li>At the end of the turn, if there are no flowers left at all in either lane, the <strong>current</strong> player captures their opponent and wins the game.</li>
</ol>

<p>Given two integers, <code>n</code> and <code>m</code>, the task is to compute the number of possible pairs <code>(x, y)</code> that satisfy the conditions:</p>

<ul>
	<li>Alice must win the game according to the described rules.</li>
	<li>The number of flowers <code>x</code> in the first lane must be in the range <code>[1,n]</code>.</li>
	<li>The number of flowers <code>y</code> in the second lane must be in the range <code>[1,m]</code>.</li>
</ul>

<p>Return <em>the number of possible pairs</em> <code>(x, y)</code> <em>that satisfy the conditions mentioned in the statement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, m = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> No pairs satisfy the conditions described in the statement.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
</ul>



## Solution

- time  : $O(1)$
- space : $O(1)$

---

- Objective:
	- Find number of combination of `x,y` where:
		- `x+y` is odd number (Alice must win)
		- `1 <= x <= m`
		- `1 <= y <= n`
- Intuition:
	- To maintain `x+y % 2 == 1`, either `x` or `y` needs to be odd
	- `res = odd_x * even_y + even_x * odd_y`
	- Number of possible `x`:
		- `m` is odd: `odd_x = m//2+1`, `even_x = m//2`
		- `m` is even: `odd_x = m//2`, `even_x = m//2`
	- Number of possible `y`:
		- `n` is odd: `odd_y = n//2+1`, `even_y = n//2`
		- `n` is even: `odd_y = n//2`, `even_y = n//2`
	- Four possible case:
		- odd `m`, odd `n`   :  `(m//2+1)(n//2) + (m//2)(n//2+1)`
		- odd `m`, even `n`  :  `(m//2+1)(n//2) + (m//2)(n//2)`
		- even `m`, odd `n`  :  `(m//2)(n//2) + (m//2)(n//2+1)`
		- even `m`, even `n` :  `(m//2)(n//2) + (m//2)(n//2)`
	- Generalize:
		- base result : `res = (m//2)(n//2)*2`
		- if `m` is odd : `res += n//2`
		- if `n` is odd : `res += m//2`
- Optimisation:
	- The question can be further generalize, considering:
		- $res = \frac{m+1}{2} \times \frac{n}{2} + \frac{m-1}{2} \times \frac{n}{2}$, if `m` is odd
	- Consider 3 case:
		- both `m,n` are even : 
			- $res = \frac{m}{2} \times \frac{n}{2} = \frac{mn}{2}$
		- both `m,n` are odd : 
			- $res = \frac{m+1}{2} \times \frac{n-1}{2} + \frac{m-1}{2} \times \frac{n+1}{2} = \frac{mn-1}{2}$
		- either `m,n` is odd : 
			- $res = \frac{m+1}{2} \times \frac{n}{2} + \frac{m-1}{2} \times \frac{n}{2} = \frac{mn}{2}$
	- Final equation : `res = (m*n)//2`