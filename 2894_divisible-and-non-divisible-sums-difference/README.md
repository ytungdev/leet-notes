# [2894. Divisible and Non-divisible Sums Difference](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference)


> Easy

- math



## Question


<p>You are given positive integers <code>n</code> and <code>m</code>.</p>

<p>Define two integers as follows:</p>

<ul>
	<li><code>num1</code>: The sum of all integers in the range <code>[1, n]</code> (both <strong>inclusive</strong>) that are <strong>not divisible</strong> by <code>m</code>.</li>
	<li><code>num2</code>: The sum of all integers in the range <code>[1, n]</code> (both <strong>inclusive</strong>) that are <strong>divisible</strong> by <code>m</code>.</li>
</ul>

<p>Return <em>the integer</em> <code>num1 - num2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10, m = 3
<strong>Output:</strong> 19
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5, m = 6
<strong>Output:</strong> 15
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5, m = 1
<strong>Output:</strong> -15
<strong>Explanation:</strong> In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
</ul>



## Solution - Sum of Arithmetic Sequence

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- Let `seq0` be the sequence of all integer in range `[1,n]`
	- Let `seq1` be the sequence of all integer in range `[1,n]` that are not divisible by `m`
	- Let `seq2` be the sequence of all integer in range `[1,n]` that are divisible by `m`
	- Let objective function be `fn(n,m) = sum(seq1) - sum(seq2)`
	- `sum(seq1) - sum(seq2)` = `sum(seq0) - 2*sum(seq2)`
	- e.g. for `n=10, m=3`
		- `seq0 = [1 2 3 4 5 6 7 8 9 10]`
		- `seq1 = [1 2   4 5   7 8   10]`
		- `seq2 = [    3     6     9   ]`
		- `fn(10,3) = sum(1..10)-2*sum(3,6,9)`
	- $S_n = \sum^n_{k=1} a_k = \frac{1}{2}n(a_1+a_n)$
	- $fn(n,m) = \{\sum^n_{a=1} a\} - 2 \times \{\sum^k_{b=1} bm\}$, where `km <= n`
	- $fn(n,m) = \{\frac{1}{2}n(n+1)\} - 2 \times \{\frac{1}{2}k(m+km)\}$
	- $fn(n,m) = \{\frac{1}{2}n(n+1)\} - \{k(1+k)m\}$
	- `k = n//m`
