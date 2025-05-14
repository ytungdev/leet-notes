# [3335. Total Characters in String After Transformations I](https://leetcode.com/problems/total-characters-in-string-after-transformations-i)


> Medium

- hash-table
- math
- string
- dynamic-programming
- counting



## Question


<p>You are given a string <code>s</code> and an integer <code>t</code>, representing the number of <strong>transformations</strong> to perform. In one <strong>transformation</strong>, every character in <code>s</code> is replaced according to the following rules:</p>

<ul>
	<li>If the character is <code>&#39;z&#39;</code>, replace it with the string <code>&quot;ab&quot;</code>.</li>
	<li>Otherwise, replace it with the <strong>next</strong> character in the alphabet. For example, <code>&#39;a&#39;</code> is replaced with <code>&#39;b&#39;</code>, <code>&#39;b&#39;</code> is replaced with <code>&#39;c&#39;</code>, and so on.</li>
</ul>

<p>Return the <strong>length</strong> of the resulting string after <strong>exactly</strong> <code>t</code> transformations.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong><!-- notionvc: eb142f2b-b818-4064-8be5-e5a36b07557a --> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcyy&quot;, t = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>First Transformation (t = 1)</strong>:
	<ul>
		<li><code>&#39;a&#39;</code> becomes <code>&#39;b&#39;</code></li>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;c&#39;</code></li>
		<li><code>&#39;c&#39;</code> becomes <code>&#39;d&#39;</code></li>
		<li><code>&#39;y&#39;</code> becomes <code>&#39;z&#39;</code></li>
		<li><code>&#39;y&#39;</code> becomes <code>&#39;z&#39;</code></li>
		<li>String after the first transformation: <code>&quot;bcdzz&quot;</code></li>
	</ul>
	</li>
	<li><strong>Second Transformation (t = 2)</strong>:
	<ul>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;c&#39;</code></li>
		<li><code>&#39;c&#39;</code> becomes <code>&#39;d&#39;</code></li>
		<li><code>&#39;d&#39;</code> becomes <code>&#39;e&#39;</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&quot;ab&quot;</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&quot;ab&quot;</code></li>
		<li>String after the second transformation: <code>&quot;cdeabab&quot;</code></li>
	</ul>
	</li>
	<li><strong>Final Length of the string</strong>: The string is <code>&quot;cdeabab&quot;</code>, which has 7 characters.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;azbk&quot;, t = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>First Transformation (t = 1)</strong>:
	<ul>
		<li><code>&#39;a&#39;</code> becomes <code>&#39;b&#39;</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&quot;ab&quot;</code></li>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;c&#39;</code></li>
		<li><code>&#39;k&#39;</code> becomes <code>&#39;l&#39;</code></li>
		<li>String after the first transformation: <code>&quot;babcl&quot;</code></li>
	</ul>
	</li>
	<li><strong>Final Length of the string</strong>: The string is <code>&quot;babcl&quot;</code>, which has 5 characters.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= t &lt;= 10<sup>5</sup></code></li>
</ul>



## Solution

#### Apporach 1 - DP tracking transformation of a single character

- time  : $O(N + t)$, where `N` is the length of `s`.
- space : $O(t)$

---

- Intuition:
	- Construct array `dp`, where `dp[i]` is the number of character at state `i`
		- At most `t+26` state, when undergo `t` transformation for a letter `z`.
		- After `t` transformation for `letter[i]`, number of character is `dp[i+t]`
		- For `i` in range `0-25`
			- Transforming a non-z character will result in the next character
			- `dp[i] = len(letter[i]) = 1`
			- Hence, `dp[i]=1 for i in range(26)`
		- For `i` == `26` and onward:
			- Transforming character from `z` onward will include two part
				- `dp[25](z) = 1`
				- `dp[26](ab) = dp[0](a) + dp[0+1](b) = 1+1=2`
				- `dp[27](bc) = dp[1](b) + dp[1+1](c) = 1+1=2`
				- `dp[34](ij) = dp[8](i) + dp[8+1](j) = 1+1=2`
				- `dp[50](yz) = dp[24](y) + dp[24+1](z) = 1+1=2`
				- `dp[51](zab) = dp[25](z) + dp[25+1](ab) = 1+2=3`
				- `dp[60](ijjk) = dp[34](ij) + dp[34+1](jk) = 2+2=4`
			- Hence, `dp[i]=dp[i-26]+dp[i-25] for i>= 26`
	- Update `res` for each character `char` in `s`:
		- Final length for character `char` after `t` transformation : `dp[ord(char) - ord('a') + t]`
- Implementation:
	- Initiate `dp` with two part: `[1]*26`+`[0]*t`
	- For each state `i` from `26` to `26+t`:
		- `dp[i]=dp[i-26]+dp[i-25]`
	- For each `char` in `s`:
		- `res += dp[ord(char) - 97 + t]`
	- return `res % 10**9+7`

#### Apporach 2 - freq array

- time  : $O(N + t \times 26)$, where `N` is the length of `s`.
- space : $O(26)$

---

- Intuition:
	- Use 1-D array `counter` with size 26 to track occurance of each character.
		- Represent letter `a-z` with index `0-25` in `counter`
	- Update `counter` after each transformation until `t` transformation is done
- Implementation:
	- Represent `s` as array `counter` containing frequency of each character
	- For each transformation from `[0-t)`:
		- create temporary `temp`
		- for letter `a-y`(index `0-24`): `temp[i+1] = counter[i]`
		- for letter `z`(index`25`): `temp[0] += counter[25]` and `temp[1]+=counter[25]`
		- `counter=temp`
	- return `sum(counter) % 10**9+7`