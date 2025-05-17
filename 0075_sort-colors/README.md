# [0075. Sort Colors](https://leetcode.com/problems/sort-colors)


> Medium

- array
- two-pointers
- sorting



## Question


<p>Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> </strong>so that objects of the same color are adjacent, with the colors in the order red, white, and blue.</p>

<p>We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent the color red, white, and blue, respectively.</p>

<p>You must solve this problem without using the library&#39;s sort function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,0,1]
<strong>Output:</strong> [0,1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> is either <code>0</code>, <code>1</code>, or <code>2</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Could you come up with a one-pass algorithm using only&nbsp;constant extra space?</p>



## Solution

#### Approach 1 - Three pointer

- time  : $O(N)$
- space : $O(1)$

---

- Intuition:
	- This is "Dutch national flag problem".
	- Use 3 pointer `L,M,R` to track 3 subarray
		- `LEFT` : `arr[0:L]` where all element are `0` and are sorted
		- `MID` : `arr[L:M]` where all element are `1` and are sorted
		- `UNKNOWN` : `arr[M:R]` where all element unsorted
		- `RIGHT` : `arr[R:n]` where all element are `2` and are sorted
		- `[0..0{L}1..1{M}?..?{R}2..2]`
	- Start with `L=0`, `M=0` and `R=n-1` when all element are unsorted
	- While `UNKNOWN` is not empty(`M<=R`), there will be 3 case:
		- `arr[M]` == `0` : `swap(L,M)`, `L++`, `M++`
		- `arr[M]` == `1` : `M++`
		- `arr[M]` == `2` : `swap(M,R)`, `R--`


#### Approach 2 - Insertion sort

- time  : $O(\frac{N(N-1)}{2}), \Omega(N)$
- space : $O(1)$

---

- Bring each element leftward until reaching correct place by `swap(i,i-1)`.