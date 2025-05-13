# [2094. Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers)


> Easy

- array
- hash-table
- sorting
- enumeration



## Question


<p>You are given an integer array <code>digits</code>, where each element is a digit. The array may contain duplicates.</p>

<p>You need to find <strong>all</strong> the <strong>unique</strong> integers that follow the given requirements:</p>

<ul>
	<li>The integer consists of the <strong>concatenation</strong> of <strong>three</strong> elements from <code>digits</code> in <strong>any</strong> arbitrary order.</li>
	<li>The integer does not have <strong>leading zeros</strong>.</li>
	<li>The integer is <strong>even</strong>.</li>
</ul>

<p>For example, if the given <code>digits</code> were <code>[1, 2, 3]</code>, integers <code>132</code> and <code>312</code> follow the requirements.</p>

<p>Return <em>a <strong>sorted</strong> array of the unique integers.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [2,1,3,0]
<strong>Output:</strong> [102,120,130,132,210,230,302,310,312,320]
<strong>Explanation:</strong> All the possible integers that follow the requirements are in the output array. 
Notice that there are no <strong>odd</strong> integers or integers with <strong>leading zeros</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [2,2,8,8,2]
<strong>Output:</strong> [222,228,282,288,822,828,882]
<strong>Explanation:</strong> The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [3,7,5]
<strong>Output:</strong> []
<strong>Explanation:</strong> No <strong>even</strong> integers can be formed using the given digits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>



## Solution

- Intuition:
	- For number `num` with digits `[a,b,c]` that satisfy all requirement:
		- In range `100-998`
			- First digit `a` in `[1 - 9]`
			- Second digit `b` in `[0 - 0]`
			- Last digit `c` in `[0,2,4,6,8]`
		- `num.count(a) <= digits.count(a)`
		- `num.count(b) <= digits.count(b)`
		- `num.count(c) <= digits.count(c)`

#### Approach 1 - Form num with digits a,b,c

- time  : $O(M^3)$, where 
	- `M` is the number of distinct digit in `digtis`
	- max at $O(9*10*5) = O(450)$
- space : $O(1)$

---

- Count occurance of `digits` as `freq_d`
- Digit in hundreds place `a` for `range(1,10)` -- $O(9)$
- Digit in tens place `b` for `range(0,10)` -- $O(10)$
- Digit in ones place `c` for `range(0,10)` with `step=2`  -- $O(5)$
- In each of `a,b,c`, loop through the corresponding range:
	- If `digits` have quota for `a/b/c`, hence `freq_d[a/b/c]>0`:
		- Reudce quota : `freq_d[a/b/c]--`
		- Loop for next digit `b/c`
			- If `num` passed `a,b,c` loop, append it to `res`
	- Else : continue
	- After each loop: reset counter by `freq_d[a/b/c]++`


#### Approach 2 - Check feasibility with numbers in range

- time  : $O((max + 1 - min) \times 100 \div 2)$, where 
	- `min` is the smallest digit in `digits` that is larger than 0
	- `max` is the largest digit in `digits`
	- max at $O((9+1-1) \times 100 \div 2) = O(450)$
- space : $O(1)$

---

- Implementation:
	- For each digit in `digtis` : `freq_d[d]++`
	- For every number `num` in range `100-998` with `step=2`
		- Count occurance of digit in `num` as `freq_n`
		- For each digit `d` in `num`:
			- If `freq_d[d] < freq_n[d]`: `num` is not feasible
		- If all `d` passed the check, append `num` to `res`
- Optimisation:
	- During construction of counter `freq_d`, find:
		- `start = min(digits, 1)`
		- `end = max(digits)`
	- Test every number in range `start*100` to `(end+1)*100` with `step=2`

	