# [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element)


> Medium

- array
- dynamic-programming
- sliding-window



## Question


<p>Given a binary array <code>nums</code>, you should delete one element from it.</p>

<p>Return <em>the size of the longest non-empty subarray containing only </em><code>1</code><em>&#39;s in the resulting array</em>. Return <code>0</code> if there is no such subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1&#39;s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,1,0,1,1,0,1]
<strong>Output:</strong> 5
<strong>Explanation:</strong> After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1&#39;s is [1,1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You must delete one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(1)$

---

- Objective:
	- Return max length of subarray containing only `1` after deleting 1 element.

- Intuition:
	- There will be 3 scenario for the final subarray before deleting:
		- Case 1 : No `1` in subarray : return `0`
		- Case 2 : All `1` in subarray : return `len(arr)-1`
		- Case 3 : Contain 1 `0` in subarray : return `len(arr)`
	- Maintain window `arr = nums[L:R+1]` and keep track of `last_zero`
	- Final subarray have max length when two segment of `1` splited by 1 `0`
		- `[seg1]=[1]*x`
		- `[seg2]=[1]*y`
		- `arr = seg1 + [0] + seg2`
	- Update `ret` and `seg1,seg2` when encountering `0`
- Implementation:
	- Iterate each `num`:
		- If `nums[R] == 1`(expand window):
			- `curr+=1`, continue (`R+=1`)
		- If `nums[R] == 0 and last_zero == -1`(first zero, keep expanding): 
			- `last_zero = R`, continue (`R+=1`)
		- If `nums[R] == 0 and last_zero != -1`(zero, update window):
			- While `L<= last_zero`, `curr -= 1` and `L+=1`
			- `last_zero = R`
	- If `last_zero` remain unchage, return `n-1` (case 2)
	- Else return `ret` (case 1/3)
- Optimisation:
	- Iterate `num` in `nums` instead of `L,R`:
		- `curr,prev = 0,0`
		- If `num` : `curr+=1`
		- Else : `ret = max(ret, curr+prev)`, `prev=curr`, `curr=0`