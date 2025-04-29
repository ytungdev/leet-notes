# [2302. Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k)


> Hard

- array
- binary-search
- sliding-window
- prefix-sum



## Question


<p>The <strong>score</strong> of an array is defined as the <strong>product</strong> of its sum and its length.</p>

<ul>
	<li>For example, the score of <code>[1, 2, 3, 4, 5]</code> is <code>(1 + 2 + 3 + 4 + 5) * 5 = 75</code>.</li>
</ul>

<p>Given a positive integer array <code>nums</code> and an integer <code>k</code>, return <em>the <strong>number of non-empty subarrays</strong> of</em> <code>nums</code> <em>whose score is <strong>strictly less</strong> than</em> <code>k</code>.</p>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,4,3,5], k = 10
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1], k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong>
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(1)$

---

- Technique : sliding window
- Idea:
	- Find logest subarray `sub` for each index `i` in `nums` that meet criteria
		- for `nums[i]`
			- add `nums[i]` into window (`accum`)
			- if failed criteria, shrink window untill criteria is met
	- All subarray of `sub` will also meet criteria
- Implementation:
	- Start with `L=0`, return value `ret=0` and running sum `accum=0`
	- For `R` from `i=0` to `i=len(nums)`:
		- add new element to `accum+=nums[R]`
		- while `L<=R` and `accum*(R-L+1) >= k`:
			- remove old element `nums[L]`
			- `L++`
		- `ret += R-L+1`
			- for array with length `n`, there are `n` possbile subarray that include `nums[R]`
			- e.g. `[1,2,3],[2,3],[3]`

```
nums=[2, 1, 11, 4, 3, 5], k=10
(L)-(R)  curr	accum	ret
(0)-(0)  [2] 	2 		1(+1)
(0)-(1)  [2, 1] 3	 	3(+2) ([2,1], [1])
(3)-(2)  [] 	0 		3(+0)
(3)-(3)  [4]	4 		4(+1)
(4)-(4)  [3] 	3 		5(+1)
(5)-(5)  [5] 	5		6(+1)

nums=[5, 2, 6, 8, 9, 7], k=50
(L)-(R)  curr		accum	ret
(0)-(0)  [5]   		5 		 1(+1)
(0)-(1)  [5, 2]   	7 		 3(+2) ([5,2],[2])
(0)-(2)  [5, 2, 6]  13 		 6(+3) ([5,2,6],[2,6],[6])
(1)-(3)  [2, 6, 8]  16 		 9(+3) ([2,6,8],[6,8],[8])
(3)-(4)  [8, 9]  	17 		11(+2) ([8,9],[9])
(4)-(5)  [9, 7]  	16 		13(+2) ([9,7],[7])
```