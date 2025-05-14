# [3337. Total Characters in String After Transformations II](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii)


> Hard

- hash-table
- math
- string
- dynamic-programming
- counting



## Question


<p>You are given a string <code>s</code> consisting of lowercase English letters, an integer <code>t</code> representing the number of <strong>transformations</strong> to perform, and an array <code>nums</code> of size 26. In one <strong>transformation</strong>, every character in <code>s</code> is replaced according to the following rules:</p>

<ul>
	<li>Replace <code>s[i]</code> with the <strong>next</strong> <code>nums[s[i] - &#39;a&#39;]</code> consecutive characters in the alphabet. For example, if <code>s[i] = &#39;a&#39;</code> and <code>nums[0] = 3</code>, the character <code>&#39;a&#39;</code> transforms into the next 3 consecutive characters ahead of it, which results in <code>&quot;bcd&quot;</code>.</li>
	<li>The transformation <strong>wraps</strong> around the alphabet if it exceeds <code>&#39;z&#39;</code>. For example, if <code>s[i] = &#39;y&#39;</code> and <code>nums[24] = 3</code>, the character <code>&#39;y&#39;</code> transforms into the next 3 consecutive characters ahead of it, which results in <code>&quot;zab&quot;</code>.</li>
</ul>

<p>Return the length of the resulting string after <strong>exactly</strong> <code>t</code> transformations.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcyy&quot;, t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>
	<p><strong>First Transformation (t = 1):</strong></p>
	<ul>
		<li><code>&#39;a&#39;</code> becomes <code>&#39;b&#39;</code> as <code>nums[0] == 1</code></li>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;c&#39;</code> as <code>nums[1] == 1</code></li>
		<li><code>&#39;c&#39;</code> becomes <code>&#39;d&#39;</code> as <code>nums[2] == 1</code></li>
		<li><code>&#39;y&#39;</code> becomes <code>&#39;z&#39;</code> as <code>nums[24] == 1</code></li>
		<li><code>&#39;y&#39;</code> becomes <code>&#39;z&#39;</code> as <code>nums[24] == 1</code></li>
		<li>String after the first transformation: <code>&quot;bcdzz&quot;</code></li>
	</ul>
	</li>
	<li>
	<p><strong>Second Transformation (t = 2):</strong></p>
	<ul>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;c&#39;</code> as <code>nums[1] == 1</code></li>
		<li><code>&#39;c&#39;</code> becomes <code>&#39;d&#39;</code> as <code>nums[2] == 1</code></li>
		<li><code>&#39;d&#39;</code> becomes <code>&#39;e&#39;</code> as <code>nums[3] == 1</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&#39;ab&#39;</code> as <code>nums[25] == 2</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&#39;ab&#39;</code> as <code>nums[25] == 2</code></li>
		<li>String after the second transformation: <code>&quot;cdeabab&quot;</code></li>
	</ul>
	</li>
	<li>
	<p><strong>Final Length of the string:</strong> The string is <code>&quot;cdeabab&quot;</code>, which has 7 characters.</p>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;azbk&quot;, t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>
	<p><strong>First Transformation (t = 1):</strong></p>
	<ul>
		<li><code>&#39;a&#39;</code> becomes <code>&#39;bc&#39;</code> as <code>nums[0] == 2</code></li>
		<li><code>&#39;z&#39;</code> becomes <code>&#39;ab&#39;</code> as <code>nums[25] == 2</code></li>
		<li><code>&#39;b&#39;</code> becomes <code>&#39;cd&#39;</code> as <code>nums[1] == 2</code></li>
		<li><code>&#39;k&#39;</code> becomes <code>&#39;lm&#39;</code> as <code>nums[10] == 2</code></li>
		<li>String after the first transformation: <code>&quot;bcabcdlm&quot;</code></li>
	</ul>
	</li>
	<li>
	<p><strong>Final Length of the string:</strong> The string is <code>&quot;bcabcdlm&quot;</code>, which has 8 characters.</p>
	</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= t &lt;= 10<sup>9</sup></code></li>
	<li><code><font face="monospace">nums.length == 26</font></code></li>
	<li><code><font face="monospace">1 &lt;= nums[i] &lt;= 25</font></code></li>
</ul>



## Solution

- time  : $O(N + 26^3 \times \log_2 t)$
	- Each multiplication in Exponentiation by squaring takes $26^3)$ time
	- $\log_2 t$ multiplication in Exponentiation
- space : $O(26^2)$

---

- Represent the resulting length of character `c` after `i` transformations as `f(c,i)`.
- Represent relation between `i,j` in transformation as `T(i,j)`
	- If `j` is included in `i` transformation: `T(i,j)=1`
	- Else : `T(i,j)=0`
- `f(i,t) = f(i+1,t-1)+..+f(i+n+1,t-1)`
	- e.g. For `t=2,nums=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]`
	- `f(0,2)` = `f(1,1)` + `f(2,1)` = (`f(2,0)`+`f(3,0)`) + (`f(3,0)`+`f(4,0)`)
    - $f(c,t) = \sum_{c'=0}^{25} [f(c',t-1) \times T(c,c')]$
- Use matrix to represent objective function of all characters for `i` transformation.
$$
\begin{pmatrix} f(0,i) \\\ f(1,i) \\\ \vdots \\\ f(25,i) \end{pmatrix}
=
\begin{bmatrix} 
    T(0,0) & T(0,1) & ... & T(0,25) \\\ 
    T(1,0) & T(1,1) & ... & T(1,25) \\\ 
    \vdots \\\ 
    T(25,0) & T(25,1) & ... & T(25,25)
\end{bmatrix}
\times

\begin{pmatrix} f(0,i-1) \\\ f( 1,i-1) \\\ \vdots \\\ f(25,i-1) \end{pmatrix}
$$
- Therefore, objective function of all characters after `t` transformation:
$$
\begin{pmatrix} f(0,t) \\\ f(1,t) \\\ \vdots \\\ f(25,t) \end{pmatrix}
=
\begin{bmatrix} 
    T(0,0) & T(0,1) & ... & T(0,25) \\\ 
    T(1,0) & T(1,1) & ... & T(1,25) \\\ 
    \vdots \\\ 
    T(25,0) & T(25,1) & ... & T(25,25)
\end{bmatrix}^{\!t}
\times

\begin{pmatrix} f(0,0) \\\ f( 1,0) \\\ \vdots \\\ f(25,0) \end{pmatrix}
$$
- Use "Exponentiation by squaring" to calculate $M^t$ efficiently
- `resM = mat_product(freq,expo_by_sq(T, t))` and `res=sum(resM[0])`