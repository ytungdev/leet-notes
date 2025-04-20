# [0781. Rabbits in Forest](https://leetcode.com/problems/rabbits-in-forest)


> Medium

- array
- hash-table
- math
- greedy



## Question


<p>There is a forest with an unknown number of rabbits. We asked n rabbits <strong>&quot;How many rabbits have the same color as you?&quot;</strong> and collected the answers in an integer array <code>answers</code> where <code>answers[i]</code> is the answer of the <code>i<sup>th</sup></code> rabbit.</p>

<p>Given the array <code>answers</code>, return <em>the minimum number of rabbits that could be in the forest</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> answers = [1,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
The two rabbits that answered &quot;1&quot; could both be the same color, say red.
The rabbit that answered &quot;2&quot; can&#39;t be red or the answers would be inconsistent.
Say the rabbit that answered &quot;2&quot; was blue.
Then there should be 2 other blue rabbits in the forest that didn&#39;t answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn&#39;t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> answers = [10,10,10]
<strong>Output:</strong> 11
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= answers.length &lt;= 1000</code></li>
	<li><code>0 &lt;= answers[i] &lt; 1000</code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(U)$, where `U` is the number of unique element, worst case `U=N`

---

- hash-map, single loop

- Idea:
	- there are 3 situation:
		- `answer == 0` : unique color rabbit
		- `answer != 0` : rabbit in certain color group
		- `count(answer) > answer` : more than one group have the same answer
- Implementation:
	- Store remaining quota for each group in `grp`
	- Store minimum number of rabbit(return value) as `ret`
	- For each answer `i`:
		- if the answer is `0`:
			- this rabbit is with unique color, `ret++`
		- else:
			- if `i` not in `grp`:
				- this is the first rabbit of its group
				- update quota for this group, `grp[i] = i`
				- update answer `ret += i+1`
			- else:
				- this rabbit belongs to certain group
				- update quota `grp[i]--`
				- if `grp[i] == 0`:
					- all rabbit in the group added, remaining rabbit with same answer is in different group
					- `del grp[i]`


