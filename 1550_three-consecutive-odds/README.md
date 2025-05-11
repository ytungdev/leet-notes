# [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds)


> Easy

- array



## Question


Given an integer array <code>arr</code>, return <code>true</code>&nbsp;if there are three consecutive odd numbers in the array. Otherwise, return&nbsp;<code>false</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,6,4,1]
<strong>Output:</strong> false
<b>Explanation:</b> There are no three consecutive odds.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,34,3,4,5,7,23,12]
<strong>Output:</strong> true
<b>Explanation:</b> [5,7,23] are three consecutive odds.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(1)$

---

- Intuition:
	- Start with count of odd number `odd` equal `0`
	- For each number `num` in `arr`:
		- If `num` is odd : `odd++`
			- Return `True` if `odd=3`
		- Else : reset `odd` to `0`
	-  Return `False` at the end of loop