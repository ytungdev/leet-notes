# [2438. Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers)


> Medium

- array
- bit-manipulation
- prefix-sum



## Question


<p>Given a positive integer <code>n</code>, there exists a <strong>0-indexed</strong> array called <code>powers</code>, composed of the <strong>minimum</strong> number of powers of <code>2</code> that sum to <code>n</code>. The array is sorted in <strong>non-decreasing</strong> order, and there is <strong>only one</strong> way to form the array.</p>

<p>You are also given a <strong>0-indexed</strong> 2D integer array <code>queries</code>, where <code>queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>. Each <code>queries[i]</code> represents a query where you have to find the product of all <code>powers[j]</code> with <code>left<sub>i</sub> &lt;= j &lt;= right<sub>i</sub></code>.</p>

<p>Return<em> an array </em><code>answers</code><em>, equal in length to </em><code>queries</code><em>, where </em><code>answers[i]</code><em> is the answer to the </em><code>i<sup>th</sup></code><em> query</em>. Since the answer to the <code>i<sup>th</sup></code> query may be too large, each <code>answers[i]</code> should be returned <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 15, queries = [[0,1],[2,2],[0,3]]
<strong>Output:</strong> [2,4,64]
<strong>Explanation:</strong>
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 10<sup>9</sup> + 7 yields the same answer, so [2,4,64] is returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, queries = [[0,0]]
<strong>Output:</strong> [2]
<strong>Explanation:</strong>
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 10<sup>9</sup> + 7 is the same, so [2] is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; powers.length</code></li>
</ul>



## Solution

- Objective:
	- Find binary decomposition `powers` of `n` 
		- $n = \sum_{i=0}^{N-1} 2^i \cdot b_i$, where $b_i$ is the bit value of i-th place (LSb0)
	- For each query, find the product of elements in range `[l,r]` of `powers`

#### Appraoch 2 - Prefix sum of power

- time  : $O(log N + q)$
- space : $O(log N + q)$

- Intuition:
	- Construct `powers`, where `powers[i]` is the power of i-th bits in `bin(n)`
	- Construct `pref_sum` ($O(logN)$) 
		- `pref_sum[i] = accum + powers[i]`
	- Process queries ($O(1) for each query, total `q` queries$)
        - `query(l,r) = 2**(pref_prod[r] - pref_prod[l-1])`
- Optimization:
	- `pref_sum` can be constructed on-the-fly without constructing `powers`
	- `query(l,r) = ( 1 << (pref_prod[r] - pref_prod[l-1]) ) % mod`


#### Appraoch 2 - Prefix product

- time  : $O(log N + q)$
- space : $O(log N + q)$

---

- Intuition:
	- Construct `pref_prod`, where 
		- `pref_prod[0] = powers[0]`
        - `pref_prod[i] = pref_prod[i-1]*powers[i]`
        - `product(arr[l],...,arr[r]) = pref_prod[r] // pref_prod[l-1]`
	- Process queries ($O(1) for each query, total `q` queries$)
