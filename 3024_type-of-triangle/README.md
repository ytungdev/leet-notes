# [3024. Type of Triangle](https://leetcode.com/problems/type-of-triangle)


> Easy

- array
- math
- sorting



## Question


<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>3</code> which can form the sides of a triangle.</p>

<ul>
	<li>A triangle is called <strong>equilateral</strong> if it has all sides of equal length.</li>
	<li>A triangle is called <strong>isosceles</strong> if it has exactly two sides of equal length.</li>
	<li>A triangle is called <strong>scalene</strong> if all its sides are of different lengths.</li>
</ul>

<p>Return <em>a string representing</em> <em>the type of triangle that can be formed </em><em>or </em><code>&quot;none&quot;</code><em> if it <strong>cannot</strong> form a triangle.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3]
<strong>Output:</strong> &quot;equilateral&quot;
<strong>Explanation:</strong> Since all the sides are of equal length, therefore, it will form an equilateral triangle.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5]
<strong>Output:</strong> &quot;scalene&quot;
<strong>Explanation:</strong> 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == 3</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>



## Solution

- Objectives:
	- Check whether the 3 given side can form a triangle
	- Check the type of triangle formed by the sides

## Approach 1 : count unique side with set()

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- Feasibility:
		- without sorting `nums`, we need to compare 3 inequality:
			- `a+b <= c`
        	- `a+c <= b`
        	- `b+c <= a`
	- Triangle type:
		- Check number of unique side with `len(set(nums))`

## Approach 2 : sort sides

- time  : $O(1)$
- space : $O(1)$

---

- Intuition:
	- Sorting `nums` to `a,b,c` where side `a<=b<=c`
		- There are only 6 case.
		- At most 3 `swap()` is needed to sort `nums`
			- `abc-abc-abc-abc`
			- `acb-acb-abc-abc`
			- `bca-bca-bac-abc`
			- `bac-abc-abc-abc`
			- `cab-acb-abc-abc`
			- `cba-bca-bac-abc`
	- Feasibility:
		- With sorted sides, feasible when `a+b > c` 
	- Triangle type:
		- "equilateral" : `a==c`(implies `a==b==c`)
		- "isosceles" : `a==b`(obtuse) or `b==c`(acute)
		- "scalene" : `a<b<c`
