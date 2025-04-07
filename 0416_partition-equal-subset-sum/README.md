# [0416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)


> Medium

- array
- dynamic-programming



## Question


<p>Given an integer array <code>nums</code>, return <code>true</code> <em>if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,11,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be partitioned as [1, 5, 5] and [11].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> The array cannot be partitioned into equal sum subsets.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>



## Solution

- time  : $O(N \times Target)$
- space : $O(Target)$

---


- Idea
	- Cannot be partition if sum of nums is odd
	- If array can be partition, each subarray will have sum equal `sum(nums)//2`
		- return `True` if sum of certain subarray equal `target=sum(nums)//2`
	- Use array `dp` to keep track if cummulative sum `i` is possible with certain subarray
		- `dp[i] = True` imply sum `i` is possible
		- `dp[0]` is always `True`
	- for `num` in `nums`:
		- for `currSum` from `target` to `num` in descending order (target, target-1, ... , num)
			- `dp[currSum]` = `dp[currSum]` or `dp[currSum-num]`
			- `currSum` is possible if it is tested already or `currSum - num` is possible
	- return `dp[target]`

```
nums = [1, 2, 2, 5] 
target = 5

dp = [True, False, False, False, False, False]

num:1
	curr:5 , (currSum-num):4,
		dp[5]=False, dp[4]=False
	curr:4 , (currSum-num):3,
		dp[4]=False, dp[3]=False
	curr:3 , (currSum-num):2,
		dp[3]=False, dp[2]=False
	curr:2 , (currSum-num):1,
		dp[2]=False, dp[1]=False
	curr:1 , (currSum-num):0,
		dp[1]=False, dp[0]=True
		[True, True, False, False, False, False]
num:2
	curr:5 , (currSum-num):3,
		dp[5]=False, dp[3]=False
	curr:4 , (currSum-num):2,
		dp[4]=False, dp[2]=False
	curr:3 , (currSum-num):1,
		dp[3]=False, dp[1]=True
		[True, True, False, True, False, False]
	curr:2 , (currSum-num):0,
		dp[2]=False, dp[0]=True
		[True, True, True, True, False, False]
num:2
	curr:5 , (currSum-num):3,
		dp[5]=False, dp[3]=True
		[True, True, True, True, False, True]
	curr:4 , (currSum-num):2,
		dp[4]=False, dp[2]=True
		[True, True, True, True, True, True]
	curr:3 , (currSum-num):1,
		dp[3]=True, dp[1]=True
	curr:2 , (currSum-num):0,
		dp[2]=True, dp[0]=True
nums:5
	curr:5 , (currSum-num):0,
		dp[5]=True, dp[0]=True
		[True, True, True, True, True, True]
```