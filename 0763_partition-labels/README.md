# [0763. Partition Labels](https://leetcode.com/problems/partition-labels)


> Medium

- hash-table
- two-pointers
- string
- greedy



## Question


<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string <code>&quot;ababcc&quot;</code> can be partitioned into <code>[&quot;abab&quot;, &quot;cc&quot;]</code>, but partitions such as <code>[&quot;aba&quot;, &quot;bcc&quot;]</code> or <code>[&quot;ab&quot;, &quot;ab&quot;, &quot;cc&quot;]</code> are invalid.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resultant string should be <code>s</code>.</p>

<p>Return <em>a list of integers representing the size of these parts</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababcbacadefegdehijhklij&quot;
<strong>Output:</strong> [9,7,8]
<strong>Explanation:</strong>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits s into less parts.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;eccbbbbdec&quot;
<strong>Output:</strong> [10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>



## Solution

- time  : O(N)
- space : O(N)

- Implementation:
	- for each character in string `s`, store the starting and ending index in `hash` : `hash[c] = [i_c0, i_cn]` **O(N)**
	- for each character(key in `hash`), 
		- update last range `last` if range `last` and `current` overlap
		- else append `last.length` into `res` and set `last` to `current`
	- append `last.length` to `res` after all iteration
	- return `res`

- Enhancement:
	- improve memory usage:
		- only keep track of last index of each char instead of start and end : `hash[c] = i_cn`
		- keep track of size of current range
		- keep track of expected ending index `end` of current range and update it if overlap
		- if expected end `end` is reached, append size to `res`, reset `size` to 0 and continue
