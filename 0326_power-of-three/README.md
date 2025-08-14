# [0326. Power of Three](https://leetcode.com/problems/power-of-three)


> Easy

- math
- recursion



## Question


<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of three. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of three, if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 27
<strong>Output:</strong> true
<strong>Explanation:</strong> 27 = 3<sup>3</sup>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no x where 3<sup>x</sup> = (-1).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?


## Solution

#### Approach 1 : Logarithm

- time  : $O(log N)$
- space : $O(1)$

---

- Intuition:
	- If `n` is not divisible : return `False`
	- Else: `d//=3` and check again
	- If `n` become `1` in the end, return `True`

#### Approach 2 : Division with largest multiple of 3 within constraint

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- `n <= 2**31 - 1`
    - Max multiple of 3 is `n = 3**19 = 1162261467`
		- $log_3 (2^{31}-1) > 19$
	- If $n = 3^k$, then `3**19 % n == 0` for `n > 0`