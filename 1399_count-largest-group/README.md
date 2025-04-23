# [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group)


> Easy

- hash-table
- math



## Question


<p>You are given an integer <code>n</code>.</p>

<p>Each number from <code>1</code> to <code>n</code> is grouped according to the sum of its digits.</p>

<p>Return <em>the number of groups that have the largest size</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 groups [1], [2] of size 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>



## Solution

- Given:
	- `digit_sum(num) = (num % 10) + digit_sum(num//10)`
	- `1 <= n <= 104`, therefore at most 36 group

#### Method 1 - Space for Time :

- time  : $O(N)$
- space : $O(N)$

---

- Technique : bottom-up dp
- Idea:
	- Store `grp` of each `num` as `dp[num] = grp`
	- We can find `grp` of `num` by : `grp(num) = (num % 10) + grp(num // 10)` -- $O(N)$
		- `dp[num] = num%10 + dp[num//10]`
			- using `%` and `//` is faster than `divmod()`
	- Store frequency of each group as `freq[grp] = freq`
	- return number of group with `max(freq)` -- $O(1)$

#### Method 2 - Time for Space :

- time  : $O(N \times log N)$
- space : $O(log N)$

---

- Idea:
	- Store frequency of each group as `freq[grp] = freq`
	- Find `grp` of `num` by : -- $O(N \times log N)$
		- while `num`:
			- `grp += num%10` and `num //= 10`
	- return number of group with `max(freq)` -- $O(1)$