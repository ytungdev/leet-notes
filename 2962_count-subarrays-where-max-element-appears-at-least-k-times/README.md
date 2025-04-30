# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times)


> Medium

- array
- sliding-window



## Question


<p>You are given an integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>Return <em>the number of subarrays where the <strong>maximum</strong> element of </em><code>nums</code><em> appears <strong>at least</strong> </em><code>k</code><em> times in that subarray.</em></p>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,3,3], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,2,1], k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> No subarray contains the element 4 at least 3 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>



## Solution

#### Method 1 - sliding window

- time  : $O(2N)$, worst case `L` and `R` have `N` iteration
- space : $O(1)$

---

- Technique : sliding window
- Intuition:
	- For each index `R`, find shortest subarray `nums[L:R]` with `k` max element `x` ending at `R`:
		- if `max_count` of current window less than `k`: 
			- expand window by `R++`
			- add `next` element to window by updaing `max_count` if `next==x`
		- if `max_count` == `k`:
			- shrink window to by `L++` while `max_count` still equal `k`
			- remove `last` from window by updaing `max_count` if `last==x`
		- once reaching shortest possible subarray, count subarray with strating index <= `L`
			- `ret+=L+1`

#### Method 2 - index calculation

- time  : $O(N+m)$, where `m` is the frequency of `max`
- space : $O(1)$

---

- Technique : sliding window
- Intuition:
	- Find all index of element `max` in `nums` as `maxi`
	- For each window ending at index `R=maxi[i]`, `L=maxi[i-k+1]`
		- no. of possible subarray = possibility of left * possibility of right
			- possibility of left  = no. of element with index < `L` +1
			- possibility of right = no. of element with index `R+1` and `max(maxi.next, len(nums))` + 1
		- e.g. nums=`[1,(2),(2),1,(2),(2),1]`, k=`2`
			- maxi=`[1,2,4,5]`
			- R=2: L=1, window=`[2,2]`, 
				- left=`[1]`, right=`[1]`
				- ret += `2*2=4`
			- R=4: L=2, window=[2,1,2], 
				- left=`[1,2]`, right=`[]`
				- ret += `3*1=3`
			- R=5: L=4, L=window=[2,2], 
				- left=`[1,2,2,1]`, right=`[1]`
				- ret += `5*2=8`




		- if `max_count` of current window less than `k`: 
			- expand window by `R++`
			- add `next` element to window by updaing `max_count` if `next==x`
		- if `max_count` == `k`:
			- shrink window to by `L++` while `max_count` still equal `k`
			- remove `last` from window by updaing `max_count` if `last==x`
		- once reaching shortest possible subarray, count subarray with strating index <= `L`
			- `ret+=L+1`