# [2929. Distribute Candies Among Children II](https://leetcode.com/problems/distribute-candies-among-children-ii)


> Medium

- math
- combinatorics
- enumeration



## Question


<p>You are given two positive integers <code>n</code> and <code>limit</code>.</p>

<p>Return <em>the <strong>total number</strong> of ways to distribute </em><code>n</code> <em>candies among </em><code>3</code><em> children such that no child gets more than </em><code>limit</code><em> candies.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5, limit = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, limit = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution

#### Approach - Maths (Inclusion-Exclusion Principle)

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- Inclusion-Exclusion Principle : 
		- $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
	- Objective is to find number of way to:
		- split `n` candies among 3 children
		- All children have `0 <= x <= limit` candies
	- Denote :
		- `|U|` : universal set, all possible way to split `n` into 3 group
		- `|A|` : set of combination where A do not exceed limit
        - `|A'|` : set of combination where A exceed limit
		- `|ABC|` : set of combination where A,B,C do not exceed limit
		- `|A'BC|==|A'|` : set of combination where A exceed limit and B,C do not exceed limit
		- `n(|A|)` : number of combination in set `|A|`
		- `|ABC| = |U| - 3x|A'BC| + 3x|A'B'C| - |A'B'C'|`
			- 3 set of which only 1 child exceed limit
			- 3 set of which only 2 childred exceed limit
			- 1 set of which all 3 childred exceed limit
	- Number of ways to split `n` among 3 group = $\frac{(n+1)(n+2)}{2} = C^{n+2}_2$
		- Undetstanding as combination:
			- `n+2` location to place first line to split (for n=3 :`| |1|1|1|`, as `||111` is an option)
    		- `n+1` location to place second line right to first
    		- e.g. n=3, 5 option to place first line, then 4 option for second line, $C^{5}_2$
		- Alternatively, understanding as sum of sequence:
			- `n+1` location to place first split line `l1` (for n=3 :`|1|1|1|`, as `|111` is an option)
			- for every `l1` at position `i`, there are `n+1-i` way to place second line `l2` right `l1`
			- Total way = `(n+1)+(n)+(n-1)+..+1` = $\frac{(1 + n+1)(n+1)}{2}=\frac{(n+2)(n+1)}{2}$
			- e.g. n=3, 4 option to place first line, then option for second line is 4,3,2,1
	- Compute result:
		- `n(U)` : spliting `n` without constraint = $C^{n+2}_2$
		- `n(A'BC)` : spliting `n` with 1 exceeding limit = $C^{n+2-(limit+1)}_2$
			- assign `limit+1` candy to 1 child, then split the remaining `n+2-(limit+1)` candy
		- `n(A'B'C)` : spliting `n` with 2 exceeding limit = $C^{n+2-2*(limit+1)}_2$
			- assign `limit+1` candy to 2 children, then split the remaining candy
		- `n(A'B'C')` : spliting `n` with 3 exceeding limit = $C^{n+2-3*(limit+1)}_2$
			- assign `limit+1` candy to each child, then split the remaining candy
		- `res = n(U) - 3*n(A'BC) + 3*n(A'B'C) - n(A'B'C')`

#### Approach - Enumeration

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- To enumerate all possible combination of `A,B,C`:
		- Bound for `A`:
			- Upper = `min(limit,n)`
			- Lower = `max(0, n-2*limit)` : make sure `A+B+C = n`
		- Bound for `B`:
			- Upper = `min(limit, n-a)`
			- Lower = `max(0, n-a-limit)` : make sure `A+B+C = n`
		- `C = n-A-B`
	- Optimization : instead of 3 loop, we can loop only `A`
		- For `A` in `bound`:
			- `res += min(limit, n-a)+1 - max(0, n-a-limit)`