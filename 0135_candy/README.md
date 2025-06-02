# [0135. Candy](https://leetcode.com/problems/candy)


> Hard

- array
- greedy



## Question


<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return <em>the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>



## Solution

## Approach 1 -- One-pass : counting ups and downs

- time  : $O(N)$
- space : $O(1)$

---

- Intuition:
	- Each child have at least 1 candy, `res` is at least `n`
	- We can split `ratings` in to multiple segments, each contain only up, down or flat trend
	- Calculate minimum candies for segment according to trend:
		- `flat`:
			- Equal rating will not affect candies of neigbors
			- Skip segment and proceed
		- `up` : 
			- Start with `up=0`, count total step of continuous up trend
			- `up+=1` and `res+=up` for each while-loop iteration
			- e.g. For `[1,2,3]`, `up=2` and `res+0+1+2`
		- `down` : 
			- Start with `down=0`, count total step of continuous down trend
			- `down+=1` and `res+=down` for each while-loop iteration
				- `res` is updating in reverse order in terms of `down`
				- After the whole down trend, result remain correct
			- e.g. For `[3,2,1]`, `down=2` and 
				- `res+2+1+0` in theory
				- `res+0+1+2` in runtime
		- After a `up` trend and a `down` trend:
			- `res -= min(up,down)`
			- A up trend and a down trend share the same peak
			- Candy of peak is overlapped in calculation of both `up` and `down`
			- e.g. For [1,2,4,3,2,1], 
				- `up=2` and `res+0+1+2`
				- `down=3` and `res+3+2+1+0`
				- At `i=2, ratings[2]=4` : `res+=2` in `up`, `res+=3` in `down`
				- Therefore we need to `res-=min(up,down) == res-=2`
- Optimization:
	- We can return `res` earlier when calculating `up` trend when `i==n`

## Approach 2 -- Two-pass : Trend in both direction

- time  : $O(2N)$
- space : $O(N)$

---

- Intuition:
	- Default candy for each children to 1 : `candies[n] = 1`
	- First iteration (L to R): For `i` in `[1..n)`:
		- If `rating[i]` > `rating[i-1]`: `candies[i] = candies[i-1] + 1`
	- Second iteration (R to L): For `i` in `(n..1]`:
		- If `rating[i]` > `rating[i+1]`: `candies[i] = candies[i+1] + 1`
	- For each children `i`: `candies[i] = max(LR[i], RL[i])`
- Optimization:
	- Instead of using 3 loop(LR, RL, res), we can compare result in second loop
	- Instead of using 2 array (LR,RL), we can store and update only 1 array (candies)


