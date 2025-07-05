# [3304. Find the K-th Character in String Game I](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i)


> Easy

- math
- bit-manipulation
- recursion
- simulation



## Question


<p>Alice and Bob are playing a game. Initially, Alice has a string <code>word = &quot;a&quot;</code>.</p>

<p>You are given a <strong>positive</strong> integer <code>k</code>.</p>

<p>Now Bob will ask Alice to perform the following operation <strong>forever</strong>:</p>

<ul>
	<li>Generate a new string by <strong>changing</strong> each character in <code>word</code> to its <strong>next</strong> character in the English alphabet, and <strong>append</strong> it to the <em>original</em> <code>word</code>.</li>
</ul>

<p>For example, performing the operation on <code>&quot;c&quot;</code> generates <code>&quot;cd&quot;</code> and performing the operation on <code>&quot;zb&quot;</code> generates <code>&quot;zbac&quot;</code>.</p>

<p>Return the value of the <code>k<sup>th</sup></code> character in <code>word</code>, after enough operations have been done for <code>word</code> to have <strong>at least</strong> <code>k</code> characters.</p>

<p><strong>Note</strong> that the character <code>&#39;z&#39;</code> can be changed to <code>&#39;a&#39;</code> in the operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;b&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>word = &quot;a&quot;</code>. We need to do the operation three times:</p>

<ul>
	<li>Generated string is <code>&quot;b&quot;</code>, <code>word</code> becomes <code>&quot;ab&quot;</code>.</li>
	<li>Generated string is <code>&quot;bc&quot;</code>, <code>word</code> becomes <code>&quot;abbc&quot;</code>.</li>
	<li>Generated string is <code>&quot;bccd&quot;</code>, <code>word</code> becomes <code>&quot;abbcbccd&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;c&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 500</code></li>
</ul>



## Solution


#### Approach 1 - simulation

- time  : $O(k)$
	- Require $log_2 k$ operation
	- The i-th operation iteration through $2^{i}$ element
	- Total : $1 + 2 + .. + 2^{log_2 k} = k$
- space : $O(k)$

---

- Intuition:
	- Simulate the process to generate string with length at least `k`

#### Approach 2 - calculation

- time  : $O(log_2 k)$
	- Require at most $log_2 k$ operation
- space : $O(1)$

---

- Intuition:
	- Each operation double the length of string `s`
	- For `k`-th character in `s`:
		- If $k = 2^i$ for some value of `i`(1,2,4,...), `i` operation is performed
		- If $k = 2^i + a$ for some value of `i` and `a`(3,6,7,10,...), `i+1` operation is performed
		- `i=k.bit_length()-1`
	- For $k = 2^i$, `k`-th character equal `a + i`
		- `f(32) = f(2**5)`, therefore `f(32) = a + 5 = f`
	- For $k = 2^i + a$, `k`-th character equal `k - most significant bit`-th character + 1
		- `f(26) = f(2**4 + 10)`
			- `f(26|11010) = f(10|1010) + 1`, 
			- `f(10|1010) = f(2|10) + 1`, 
			- `f(2|10) = f(2**1)`,
			- Therefore `f(26) = f(10)+1 = ((a+1)+1)+1 = d`
		- `f(24) = f(2**4 + 8)`
			- `f(24|11000) = f(8) + 1`,
			- `f(8|1000) = f(2**3)`, 
			- Therefore `f(24) = (a+3)+1 = e`