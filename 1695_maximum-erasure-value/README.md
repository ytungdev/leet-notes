# [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value)


> Medium

- array
- hash-table
- sliding-window



## Question


<p>You are given an array of positive integers <code>nums</code> and want to erase a subarray containing&nbsp;<strong>unique elements</strong>. The <strong>score</strong> you get by erasing the subarray is equal to the <strong>sum</strong> of its elements.</p>

<p>Return <em>the <strong>maximum score</strong> you can get by erasing <strong>exactly one</strong> subarray.</em></p>

<p>An array <code>b</code> is called to be a <span class="tex-font-style-it">subarray</span> of <code>a</code> if it forms a contiguous subsequence of <code>a</code>, that is, if it is equal to <code>a[l],a[l+1],...,a[r]</code> for some <code>(l,r)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,4,5,6]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The optimal subarray here is [2,4,5,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,2,1,2,5,2,1,2,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The optimal subarray here is [5,2,1] or [1,2,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>



## Solution

- Objectives:
	- Find subarray with unique elemenet and max sum
- Intuitiions:
	- Use two pointer to keep track of subarray while keeping all element unique
	- Use sliding window to keep track of sum of subarray

#### Method 1 - set()

- time  : $O(N)$
- space : $O(N)$

---

- Implementation:
	- For each `num` in `nums`:
		- If `num` in `sub`:
			- Move `L` until `nums[L] == num`
			- while `nums[L] != num`
				- remove `nums[L]` from `sub`
				- remove `nums[L]` from `curr`
				- `L++`
			- `L++`
			- e.g. `OOXOOOX` > `XOOOX` > `OOOX`
		- If `num` not in `sub`:
			- add `num` to `sub` and `curr`
			- Update `ret`

#### Method 2 - keep track of index of last occurence

- time  : $O(N)$
- space : $O(N)$

---

- Implementation:
	- Use `sub = {val:idx}` to keep track of last index of each element
	- Add first element to `sub`, `curr` and `ret`
	- For each `num` in `nums[1:]`:
		- If `num` in `sub`:
			- Move `L` to `sub[num] + 1`
			- while `L <= sub[num]`
				- Remove element `nums[L]` from `curr`
				- `L++`
			- e.g. `sub[num] = 3`, `L=4`
		- Add `num` to `curr`
		- Update `sub`
		- Update `ret`
