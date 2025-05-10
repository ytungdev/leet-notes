# [2918. Minimum Equal Sum of Two Arrays After Replacing Zeros](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros)


> Medium

- array
- greedy



## Question


<p>You are given two arrays <code>nums1</code> and <code>nums2</code> consisting of positive integers.</p>

<p>You have to replace <strong>all</strong> the <code>0</code>&#39;s in both arrays with <strong>strictly</strong> positive integers such that the sum of elements of both arrays becomes <strong>equal</strong>.</p>

<p>Return <em>the <strong>minimum</strong> equal sum you can obtain, or </em><code>-1</code><em> if it is impossible</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [3,2,0,1,0], nums2 = [6,5,0]
<strong>Output:</strong> 12
<strong>Explanation:</strong> We can replace 0&#39;s in the following way:
- Replace the two 0&#39;s in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,0,2,0], nums2 = [1,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to make the sum of both arrays equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution

- time  : $O(N+M)$, where `N` and `M` are the length of `nums1` and `nums2`
- space : $O(1)$

---

- Intuition:
	- Minimum value of an array can be achieved by replacing all `0` with `1`
		- `min_val(nums) = sum(nums) + nums.count(0)`
	- If at least one `0` exist in both array, `res=max(sum1+zero1, sum2+zero2)`
		- `[1,0], [0,99]`
	- There are three edge case if at least one array do not contain `0`:
		- `zero1==0` and `zero2!=0` : no solution if `min_val(nums2) > sum1`
			- `[4],[1,0]` : solution exist
			- `[4],[4,0]` : no solution
			- `[1],[4,0]` : no solution
		- `zero1!=0` and `zero2==0` : no solution if `min_val(nums1) > sum2`
			- `[1,0],[4]` : solution exist
			- `[4,0],[4]` : no solution
			- `[4,0],[1]` : no solution
		- `zero1==0` and `zero2==0` : no solution if `sum1 != sum2`
			- `[1],[1]` : solution exist
			- `[1],[4]` : no solution
	- The 3 edge case can be combined to form two condition where there is no solution:
		- `zero1==0` and `min_val(nums2) > sum1`
		- `zero2==0` and `min_val(nums1) > sum2`