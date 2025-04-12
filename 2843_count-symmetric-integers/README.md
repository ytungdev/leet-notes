# [2843.   Count Symmetric Integers](https://leetcode.com/problems/count-symmetric-integers)


> Easy

- math
- enumeration



## Question


<p>You are given two positive integers <code>low</code> and <code>high</code>.</p>

<p>An integer <code>x</code> consisting of <code>2 * n</code> digits is <strong>symmetric</strong> if the sum of the first <code>n</code> digits of <code>x</code> is equal to the sum of the last <code>n</code> digits of <code>x</code>. Numbers with an odd number of digits are never symmetric.</p>

<p>Return <em>the <strong>number of symmetric</strong> integers in the range</em> <code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 1, high = 100
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 1200, high = 1230
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
</ul>



## Solution

- Objective:
	- Iterate from `low` to `high`, for each `num` -- $O(N)$
		- if sum of first half of digits in `num` equals second half, `count++`

#### Method 2 : number range (consider constraint)

- time  : $O(high - low)$
- space : $O(1)$

---

- Given:
	- 1 <= `low` <= `high` <= $10^4$
	- $G(a,b) = G(0,b) - G(0, a-1)$

- Idea:
	- for `1 <= x <= 99` (`high` <= 100):
		- only multiple of 11 is symmetric
		- return `high`//11 - (`low`-1)//11 -- $O(1)$
		- max `count` is 9
	- for `100 <= x <= 1000`:
		- none of the number from this range is symmetric
		- all number aree with odd length (except 1000, which is not symmetric)
	- for `1001 <= x <= 10000`:
		- if `low < 100`:
			- $G(low, high) = G(100, high) + G(99, low)$
			- $G(low, high) = G(100, high) + [G(0, 99) - G(0, low-1)]$
			- $G(low, high) = G(100, high) + [9 - G(0, low-1)]$
			- `count` = `9` - (`low`-1)//11
		- for `n` from `max(low,1001)` to `high+1` -- $O(high - low)$
			- calculate sum `L` of digit in thousands and hundres
			- calculate sum `R` of digit in tens and ones
			- if `L` == `R`, `count++`
		- return `count`


#### Method 1 : digit array

- time  : $O(N \log_{10}(high))$
- space : $O(\log_{10}(high))$

---

- Single loop, digit array
- Idea:
	- Iterate from `low` to `high`, for each `num` -- $O(N)$
		- Iterate each digit and append to array `digits` -- $O(\log_{10} (num))$
		- `continue` if `digits.length` is not even number
		- if sum of first half of `digits` equals sum of second half of `digits`, `count++`
	- return `count`