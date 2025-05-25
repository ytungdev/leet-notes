# [2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words)


> Medium

- array
- hash-table
- string
- greedy
- counting



## Question


<p>You are given an array of strings <code>words</code>. Each element of <code>words</code> consists of <strong>two</strong> lowercase English letters.</p>

<p>Create the <strong>longest possible palindrome</strong> by selecting some elements from <code>words</code> and concatenating them in <strong>any order</strong>. Each element can be selected <strong>at most once</strong>.</p>

<p>Return <em>the <strong>length</strong> of the longest palindrome that you can create</em>. If it is impossible to create any palindrome, return <code>0</code>.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forward and backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;lc&quot;,&quot;cl&quot;,&quot;gg&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> One longest palindrome is &quot;lc&quot; + &quot;gg&quot; + &quot;cl&quot; = &quot;lcggcl&quot;, of length 6.
Note that &quot;clgglc&quot; is another longest palindrome that can be created.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;ab&quot;,&quot;ty&quot;,&quot;yt&quot;,&quot;lc&quot;,&quot;cl&quot;,&quot;ab&quot;]
<strong>Output:</strong> 8
<strong>Explanation:</strong> One longest palindrome is &quot;ty&quot; + &quot;lc&quot; + &quot;cl&quot; + &quot;yt&quot; = &quot;tylcclyt&quot;, of length 8.
Note that &quot;lcyttycl&quot; is another longest palindrome that can be created.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;cc&quot;,&quot;ll&quot;,&quot;xx&quot;]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One longest palindrome is &quot;cc&quot;, of length 2.
Note that &quot;ll&quot; is another longest palindrome that can be created, and so is &quot;xx&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>words[i].length == 2</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>



## Solution

#### Approach 1 - Counter

- time  : $O(N+2L)$
	- `Counter` construction take $O(N)$
	- `L` is the number of unique word in `words`
		- Loop for `counter.keys()` take $O(N)$ if all key are unique, max at $26^2$ possible key
	- `reverse(word)` take $O(2)$
- space : $O(N)$

---

- Intuition:
	- Use `Counter` to store occurence of each word in hashmap `cnt` -- $O(N)$
	- `word` contain two identical letter are candidate to place in the center.
		- We can add `cnt[word]//2` pair into `res`
		- At most 1 `word` can be the center, therefore we track existance of center with `center`
		- If `center == 0` and `cnt[word]%2`, `res+=2` and `center = 1`
	- `word` with two different letter are candidate to place on both side
		- If counterpart of word `drow = reverse(word)` exist in `cnt`, -- $O(2)$
			- We can add `min(cnt[word], cnt[drow])` pair into `res`
			- Skip `drow` in coming iteration
	- For each `word` in `words`, handle accordingly. -- $O(N)$



#### Approach 2 - matrix

- time  : $O(N)$
- space : $O(N^2)$

---

- Inuition:
	- Store occurence of the 2 letter word in matrix `cnt`
	- For each `word` in `words`
		- Convert both letter to index `i,j` in `cnt`
		- If counterpart found in matrix(`cnt[j][i] > 0`)
			- Consume the counterpart and add it to `res`
			- `cnt[j][i] -= 1` and `res+=4`.
			- If `word` is center candidate, `center-=1`
		- else:
			- `cnt[i][j] += 1`
			- If `word` is center candidate, `center+=1`
	- For word that contain same letter, they are candidate to place in the center.
	- If any of `cnt[a][a] .. cnt[z][z]` == 1 after iterating all `words`, `res+=2` 
