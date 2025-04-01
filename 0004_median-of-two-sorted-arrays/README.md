# [0004. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

> Hard

<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution 1

- time  : O(M+N)
- space : O(M+N)

---

- use two pointer `i` and `j` to track current index of both array starting from 0
- for each pair `nums1[i]` and `nums2[j]`: **O(M+N)**
	- append the smaller one to merged array`nums`, 
	- then move to next element in that array
- if length of merged array is even: return average of `nums[mid_1]` and `nums[mid_2]`
- else : return `nums[mid]`


## Solution 2

- time  : O(Log(Min(M,N)))
- space : O(1)

---

- use binary search without actually merging two array

- Given:
	- two array `A` and `B` is sorted
	- median always exist and only one solution exist
	- size of two array namely `m` and `n` is known
	- index of median `mid` in merged array `I` is `(m+n)//2`

- Idea:
	- if we split array `I` at index `mid`, both subarray is with size `half`
		- `median = I[mid]`
		- `len(I[0:mid])` == `len(I(mid+1:(m+n)))` == `half` == `(m+n)//2`
	- find partition point `i` and `j` in subarray `A` and `B` so that:
		- element to the left of `i/j` maps to element left to `mid` in `I`
			- `sorted(A[0:i] + B[0:j]) == I[0:mid]`
		- element to the right of `i/j` maps to element right to `mid` in `I`
			- `sorted(A[i+1:m] + B[j+1:n]) == I[mid+1:(m+n)]`
	- By finding partition `i` in smaller array `A`, we can deduce `j` by `half-i-2`
		- `half` is size of subarray, therefore converting to index require `-2`
		- `j+1 + i+1 = half`
	- If the partition is right:
		- `A[i] <= B[j+1]` and `B[j] <= A[i+1]`
		- `I[mid]` = `max(A[i], B[j])`
		- `I[mid+1]` = `min(A[i+1], B[j+1])`
		- return depending on length `m+n`
	- Use binary search on smaller array `A` with `L,R = 0,m-1` **O(logM)**

- Implementation:
	- for easier operation, make `A` always have a smaller size than `B`
		- `A,B = nums1,nums2 if len(nums1) <= len(nums2) else nums2,nums1`
	- Start binary search on array `A` with `L,R = 0,m-1` that satisfy `A[i] <= B[j+1]` and `B[j] <= A[i+1]`
		- if `A[i]` and `B[j]` out of bound, set them to `float(-inf)` to make it comparable
		- if `A[i+1]` and `B[j+1]` out of bound, set them to `float(inf)` to make it comparable
	- if `A[i] > B[j+1]`, partition `i` is too right, binary search `A.left` `L,R = 0,i-1`
	- if `B[j] > A[i+1]`, partition `i` is too left, binary search `A.right` `L,R = i+1,m`

```
The following case show 3 scenario of partitioning with 
I = [a,b,c,d,e,f,g]
m = 3
n = 4
total = 3+4 = 7
half = 7//2 = 3		# total of 3 element in I.left
i = (0+3)//2 = 1
j = (3-1-2) = 0
---------------------------------------------------------
# A[i] <= B[j+1] and B[j] <= A[i+1]

A = [a,c,e]
B = [b,d,f,g]

    0       1 |     2
A	a       c |     e
B       b     | d       f   g
        0     | 1       2   3

c<d and b<e, right partitioning
---------------------------------------------------------
# A[i] > B[j+1]

A = [a,d,e]
B = [b,c,f,g]

    0           1 | 2
A	a           d | e
B       b | c           f   g
        0 | 1           2   3

d > c, search left
---------------------------------------------------------
# B[j] > A[i+1]

A = [a,d,e]
B = [b,c,f,g]

    0   1 | 2
A	a   b | c        
B               d | e   f   g
                0 | 1   2   3

d > c, search right
```