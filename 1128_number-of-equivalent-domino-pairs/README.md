# [1128. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs)


> Easy

- array
- hash-table
- counting



## Question


<p>Given a list of <code>dominoes</code>, <code>dominoes[i] = [a, b]</code> is <strong>equivalent to</strong> <code>dominoes[j] = [c, d]</code> if and only if either (<code>a == c</code> and <code>b == d</code>), or (<code>a == d</code> and <code>b == c</code>) - that is, one domino can be rotated to be equal to another domino.</p>

<p>Return <em>the number of pairs </em><code>(i, j)</code><em> for which </em><code>0 &lt;= i &lt; j &lt; dominoes.length</code><em>, and </em><code>dominoes[i]</code><em> is <strong>equivalent to</strong> </em><code>dominoes[j]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dominoes = [[1,2],[2,1],[3,4],[5,6]]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= dominoes.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>dominoes[i].length == 2</code></li>
	<li><code>1 &lt;= dominoes[i][j] &lt;= 9</code></li>
</ul>



## Solution

- Given:
	- Two domino can form a pair when they are the same after sorting its values.
		- e.g `[2,1] -> [1,2] == [1,2]`
	- $C^n_r = \frac{n!}{r!*(n-r)!} = \frac{n(n-1)...(n-r-1)}{r!}$
		- $C^n_2 = \frac{n(n-1)}{2}$ -- $eq(1)$
		- With certain count `n` of the same domino, `pair = (count*(count-1))//2`. -- $(1)$
	- If domino `d` have a count of `n`, 
		- `d` can form `n-1` pair with other domino.
		- No. of possible pair : $pair = \sum_1^n(n-1)$ -- $eq(2)$
			- Consistent to $eq(1)$ according to sum of sequence $S_n = \frac{(a_1+a_n)\times n}{2}$.
		- e.g. if there are 4 domino `(1,2)`
			- for the 1st `(1,2)`, it can form `0` pair
			- for the 2nd `(1,2)`, it can form `1` pair
			- for the 3rd `(1,2)`, it can form `2` pair
			- for the 4th `(1,2)`, it can form `3` pair
			- `pair = sum(0,1,2,3) = 6`
	- `1 <= domin.val <= 9` -- $(3)$

#### Approach 1 - Hash Table(`dict`) with `id`

- time  : $O(N)$
- space : $O(d)$, where `d` is the number of distinct domino (max:100)

---

- Intuition:
	- For each domino `d=(x,y)`, calcualte `id` by `x*10+y` if `x>y` else `y*10+x`.
		- There are only `99` possible `id`. -- $(3)$
	- create `freq={}` to store count of each `id`
	- For each domino `d`:
		- `pair` = `freq[id]` or `0`
		- `res += pair` -- $eq(2)$
		- `freq[id] = pair + 1`

#### Approach 2 - Array with `id`

- time  : $O(N)$
- space : $O(100)$

---

- Intuition:
	- For each domino `d=(x,y)`, calcualte `id` by `x*10+y` if `x>y` else `y*10+x`.
		- There are only `99` possible `id`. -- $(3)$
	- Two domino can form pair if they have same `id`
	- create `freq=[0]*100` to store count of each `id` from `id=0` to `id=99`
	- For each domino `d`:
		- `res += freq[id]` -- $eq(2)$
		- `freq[id] += 1`

#### Approach 3 - python.collections.Counter

- time  : $O(2N+d)$, where `d` is the number of distinct domino (max:100)
- space : $O(N)$, input of `Counter()` cached the sorted tuple of each dominoes

---

- Intuition:
	- Modify `dominoes` for `Counter()` input: -- $O(N)$
		- `Counter()` can work with tuple but not list
		- For each domino `dominoes[i]=[x,y]`, swap `x,y` if `x > y`
			- `dominoes = [(x,y) if x<=y else (y,x) for x,y in dominoes]`
	- Use `collections.Counter` to count occurence of each domino. -- $O(N)$
		- `counter = Counter(dominoes)`
	- For each domino `d` in `counter`: -- $O(d)$
		- If `counter[d] > 1`, it can form at least one pair
		- `res += (count*(count-1))//2` -- $(1)$