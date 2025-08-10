# [0869. Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2)


> Medium

- hash-table
- math
- sorting
- counting
- enumeration



## Question


<p>You are given an integer <code>n</code>. We reorder the digits in any order (including the original order) such that the leading digit is not zero.</p>

<p>Return <code>true</code> <em>if and only if we can do this so that the resulting number is a power of two</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>



## Solution

#### Approach 1 - serialization

- time  : $O(log d)$, where `d` is the number of digits of `n`, max at 9
- space : $O(30)$

---

- Intuition:
	- Max value of `n` is $2^29$, therefore they are 30 power of 2 with in solution space
	- `n` can form a power of 2 value iff `serialize(n) in power_of_2`
	- We can serialize a number by sorting its digits

#### Approach 2 - permutation 

- time  : $O(d \cdot d!)$, where `d` is the number of digits of `n`, max at 9
- space : $O(d)$

---

- Intuition:
	- Find all peermutation of `n` (at most 9! permutation)
		- Use `dfs()` with `Counter()`
	- For each permutation check if it is a power of 2 in $O(1)$
		- `return n & (n-1) == 0`