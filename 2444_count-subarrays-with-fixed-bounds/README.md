# [2444. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds)


> Hard

- array
- queue
- sliding-window
- monotonic-queue



## Question


<p>You are given an integer array <code>nums</code> and two integers <code>minK</code> and <code>maxK</code>.</p>

<p>A <strong>fixed-bound subarray</strong> of <code>nums</code> is a subarray that satisfies the following conditions:</p>

<ul>
	<li>The <strong>minimum</strong> value in the subarray is equal to <code>minK</code>.</li>
	<li>The <strong>maximum</strong> value in the subarray is equal to <code>maxK</code>.</li>
</ul>

<p>Return <em>the <strong>number</strong> of fixed-bound subarrays</em>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,2,7,5], minK = 1, maxK = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1], minK = 1, maxK = 1
<strong>Output:</strong> 10
<strong>Explanation:</strong> Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], minK, maxK &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(1)$

---

- Technique : sliding window
- Idea:
	- Treat array as subarrays seperated by out-of-bound element
		- for `nums=[3,1,3,5,2,7,5,1]`,`minK=1`,`maxK=5`: `[3,1,3,5,2] 7 [5,1]`
	- For each subarray `sub` , 
		- find index of `minK` and `maxK` as `minI` and `maxI`.
			- `loI = min(minI, maxI)` and `hiI = max(minI, maxI)`, `bound = nums[loI:hiI+1]`
		- Count possible subarray that contain `bound` and `sub[hiI+1:i]`
			- number of combination equals number of element in subarray before `loI` + 1
			- for `[a,b,bound,c]`, possible way is `bound,c`, `b,bound,c` and `a,b,bound,c`
		- `count += loI - startI + 1`
- Implementation:
	- Use a single loop from `R=0` to `R=len(nums)`
	- set `count=0`, `L=0`, `minI,maxI = -1,-1`
	- For each index `R`:
		- if `nums[R]` out of bound:
			- reset and ready for next subarray : `L=R+1`, `minI,maxI = -1,-1`
			- continue next iteration
		- if `nums[R]` equal bound:
			- `minI = R` and/or `maxI = R`
		- if both `minI` and `maxI` is set,
			- this subarray is fixed-bound, `count += min(minI,maxI) - L + 1`