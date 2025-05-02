# [0838. Push Dominoes](https://leetcode.com/problems/push-dominoes)


> Medium

- two-pointers
- string
- dynamic-programming



## Question


<p>There are <code>n</code> dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.</p>

<p>After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.</p>

<p>When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.</p>

<p>For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.</p>

<p>You are given a string <code>dominoes</code> representing the initial state where:</p>

<ul>
	<li><code>dominoes[i] = &#39;L&#39;</code>, if the <code>i<sup>th</sup></code> domino has been pushed to the left,</li>
	<li><code>dominoes[i] = &#39;R&#39;</code>, if the <code>i<sup>th</sup></code> domino has been pushed to the right, and</li>
	<li><code>dominoes[i] = &#39;.&#39;</code>, if the <code>i<sup>th</sup></code> domino has not been pushed.</li>
</ul>

<p>Return <em>a string representing the final state</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dominoes = &quot;RR.L&quot;
<strong>Output:</strong> &quot;RR.L&quot;
<strong>Explanation:</strong> The first domino expends no additional force on the second domino.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png" style="height: 196px; width: 512px;" />
<pre>
<strong>Input:</strong> dominoes = &quot;.L.R...LR..L..&quot;
<strong>Output:</strong> &quot;LL.RR.LLRRLL..&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == dominoes.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>dominoes[i]</code> is either <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, or <code>&#39;.&#39;</code>.</li>
</ul>



## Solution

#### Approach 1 - calculate force

- time  : $O(N)$
- space : $O(N)$

---

- Techinique: two-pointer
- Intuition:
	- There are only 4 type of boundary:
		- `L..R`
		- `R..L` or `R...L`
		- `L..L`
		- `R..R`
	- To handle edge case, we add virtual boundaries:
		- `dominoes = 'L'+dominoes+'R'`
	- Handling each case:
		- `L..R` : do nothing
		- `R..L`/`R...L` : convert to `RRLL`/`RR.LL`
			- use two pointer `l=L` and `r=R` and shrink the window
			- while `l<r`:`
				- `dominoes[l]='R'`, `l++`
				- `dominoes[r]='L'`, `r--`
		- `L..L`/`R..R` : convert to `LLLL`/`RRRR`
			- while `L<R`: `dominoes[L] = dominoes[R]`, `L++`
	- move to next boundary untill reaching the end

#### Approach 2 - calculate force

- time  : $O(2N)$
- space : $O(N)$

---

- Technique: 3-pass or 2-pass iteration
- Intuition:
	- store resulting force of all `n=len(dominoes)` element as `forces[i]`
	- Calculate right-pushing force for each element.
		- traverse from `i=0` to `i=n`
		- Each `'R'` provide `force=n`
			- a single `'R'` can make all dominoes `'R'`
			- continuos `'R'` do not provide extra force
		- Each `'.'` will reduce force by `1`
		- Force become `0` when encountering `'L'`
	- Calculate left-pushing force for each element.
		- traverse from `i=n` to `i=0`
		- Each `'L'` provide `force=-n`
		- Each `'.'` will reduce force by `1`
		- Force become `0` when encountering `'R'`
	- Determine resulting string `ret` by comparing each `forces[i]`
		- `'.'` if `force[i] == 0` 
		- `'R'` if `force[i] > 0` 
		- `'L'` if `force[i] < 0` 