# [1857. Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph)


> Hard

- hash-table
- dynamic-programming
- graph
- topological-sort
- memoization
- counting



## Question


<p>There is a <strong>directed graph</strong> of <code>n</code> colored nodes and <code>m</code> edges. The nodes are numbered from <code>0</code> to <code>n - 1</code>.</p>



<p>You are given a string <code>colors</code> where <code>colors[i]</code> is a lowercase English letter representing the <strong>color</strong> of the <code>i<sup>th</sup></code> node in this graph (<strong>0-indexed</strong>). You are also given a 2D array <code>edges</code> where <code>edges[j] = [a<sub>j</sub>, b<sub>j</sub>]</code> indicates that there is a <strong>directed edge</strong> from node <code>a<sub>j</sub></code> to node <code>b<sub>j</sub></code>.</p>



<p>A valid <strong>path</strong> in the graph is a sequence of nodes <code>x<sub>1</sub> -&gt; x<sub>2</sub> -&gt; x<sub>3</sub> -&gt; ... -&gt; x<sub>k</sub></code> such that there is a directed edge from <code>x<sub>i</sub></code> to <code>x<sub>i+1</sub></code> for every <code>1 &lt;= i &lt; k</code>. The <strong>color value</strong> of the path is the number of nodes that are colored the <strong>most frequently</strong> occurring color along that path.</p>



<p>Return <em>the <strong>largest color value</strong> of any valid path in the given graph, or </em><code>-1</code><em> if the graph contains a cycle</em>.</p>



<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>



<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet1.png" style="width: 400px; height: 182px;" /></p>



<pre>

<strong>Input:</strong> colors = &quot;abaca&quot;, edges = [[0,1],[0,2],[2,3],[3,4]]

<strong>Output:</strong> 3

<strong>Explanation:</strong> The path 0 -&gt; 2 -&gt; 3 -&gt; 4 contains 3 nodes that are colored <code>&quot;a&quot; (red in the above image)</code>.

</pre>



<p><strong class="example">Example 2:</strong></p>



<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet2.png" style="width: 85px; height: 85px;" /></p>



<pre>

<strong>Input:</strong> colors = &quot;a&quot;, edges = [[0,0]]

<strong>Output:</strong> -1

<strong>Explanation:</strong> There is a cycle from 0 to 0.

</pre>



<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>



<ul>
	<li><code>n == colors.length</code></li>
	<li><code>m == edges.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>colors</code> consists of lowercase English letters.</li>
	<li><code>0 &lt;= a<sub>j</sub>, b<sub>j</sub>&nbsp;&lt; n</code></li>
</ul>


## Solution

## Approach 1 - Kahn's algorithm

- time  : $O(V+E)$
- space : $O(V+E)$

---

- Intuition:
	- Define `dp[v][c]` as the maximum number of color `c` in the path ending at `v`
	- Objective is to find `max_c` after processing all vertices in the graph.
	- Traverse each vertex in topolofical orders:
		- Create adjacent list `adj[v]` and indegree `idg[v]` for each vertex `v`
		- Add all vertices with `idg[v] ==0` to queue `q`
	- Process first element `v` of `q` until `q` is empty:
		- Increment color count for `v` : `dp[v][colors[v]] += 1`
		- Update `max_c` : `max_c = max(max_c, dp[v][colors[v]])`
		- Process all adjacent vertex `a`:
			- Update `idg[a] -= 1`
			- If `idg==0`, add `a` to `q`
			- Pass forward color count from `v` to `a`
				- `dp[a][c]` can come from mulitple branch, only update if value increased
				- `dp[a][c] = max(dp[a][c], dp[v][c])`
	- If number of vertices processed != number of vertices, cycle exist in graph.
- Optimisation:
	- Instead of using array with length 26 to store color count, use `dict`
		- `dp = [[0]*26 for v in range(n)]`, `dp[v][c] += 1`
		- `dp = [{} for v in range(n)]`, `if c in dp[v] : dp[v][c]+=1 else dp[v][c]=1`
	- Instead of looping throguh all 26 possible colors, only loop and memorise existing colors.
		- `for a in adj[v] : for c in range(26): ...`
		- `for a in adj[v] : for c in dp[v].keys(): ...`

## Approach 2 - DFS with 3-state

- time  : $O(V+E)$
- space : $O(V+E)$

---

- Intuition:
	- Use post-order DFS to process each vertices `dfs(v)`.
	- Topological sort with post-order DFS will not visit a vertex once its visited, however we need to compare color count for all branch, there for we need 3 state instead of 2(unvisted/visited):
		- 0 : unprocessed - can be visited, process as usual
		- 1 : processing - cannot be visited, incomplete process and cycle detected if encountered
		- 2 : processed - can be visited but skip processing
	- For each vertex `v`, call `dfs(v)` if `v` is unprocessed
		- To make sure isolated tree are processed
		- Return `-1` if cycle detected in `dfs(v)`
	- In each `dfs(v)` call:
		- If `state(v)` is processing : end and return `cycle = True`
		- If `state(v)` is processed : skip process`
		- Change state of `v` : `state[v] = 1`
		- For all vertex `a` in `adj(v)`:
			- Process `a` by `dfs(a)` 
			- return `cycle = True` if cycle detected
			- Update `dp[v][c]` for all color `c` : `dp[v][c] = max(dp[a][c], dp[v][c])`
		- Update `dp[v][colors[v]] += 1`
		- Change state of `v` : `state[v] = 2`
	- Return `max(dp)`


