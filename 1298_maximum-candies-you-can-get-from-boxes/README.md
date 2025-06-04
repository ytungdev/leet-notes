# [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes)


> Hard

- array
- breadth-first-search
- graph



## Question


<p>You have <code>n</code> boxes labeled from <code>0</code> to <code>n - 1</code>. You are given four arrays: <code>status</code>, <code>candies</code>, <code>keys</code>, and <code>containedBoxes</code> where:</p>

<ul>
	<li><code>status[i]</code> is <code>1</code> if the <code>i<sup>th</sup></code> box is open and <code>0</code> if the <code>i<sup>th</sup></code> box is closed,</li>
	<li><code>candies[i]</code> is the number of candies in the <code>i<sup>th</sup></code> box,</li>
	<li><code>keys[i]</code> is a list of the labels of the boxes you can open after opening the <code>i<sup>th</sup></code> box.</li>
	<li><code>containedBoxes[i]</code> is a list of the boxes you found inside the <code>i<sup>th</sup></code> box.</li>
</ul>

<p>You are given an integer array <code>initialBoxes</code> that contains the labels of the boxes you initially have. You can take all the candies in <strong>any open box</strong> and you can use the keys in it to open new boxes and you also can use the boxes you find in it.</p>

<p>Return <em>the maximum number of candies you can get following the rules above</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
<strong>Output:</strong> 16
<strong>Explanation:</strong> You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == status.length == candies.length == keys.length == containedBoxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>status[i]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>1 &lt;= candies[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= keys[i].length &lt;= n</code></li>
	<li><code>0 &lt;= keys[i][j] &lt; n</code></li>
	<li>All values of <code>keys[i]</code> are <strong>unique</strong>.</li>
	<li><code>0 &lt;= containedBoxes[i].length &lt;= n</code></li>
	<li><code>0 &lt;= containedBoxes[i][j] &lt; n</code></li>
	<li>All values of <code>containedBoxes[i]</code> are unique.</li>
	<li>Each box is contained in one box at most.</li>
	<li><code>0 &lt;= initialBoxes.length &lt;= n</code></li>
	<li><code>0 &lt;= initialBoxes[i] &lt; n</code></li>
</ul>



## Solution

- time  : $O(N)$
	- Visit each reachable box once, at most `N` reachable box
- space : $O(N)$

---

- Intuition:
	- Sequence of event : `select box > if opened > take candy > take key&box > next`
	- We can use BFS with a queue
		- We will travel each box in the solution space at most once
		- It is not guaranteed that we can visit child of a box, some keys/boxes are unreachable
		- Use two queue to prevent infinite loop
			- `q` : store boxes obtained with key
			- `waitlist` : store boxes obtained without key
	- We can open box `i` if `haveBox[i]` and `haveKey[i]`
- Implmentation:
	- Initial setup : `q`, `waillist`, `boxInv`, `keyInv`
	- Put initial keys, for each `status[i]`:
		- Add `i` to `keyInv`
	- Get initial boxes, for each `i` in `initialBoxes`:
		- Add `i` to `boxInv`
		- If `haveKey[i]` : add `i` to `q`
		- Else : add `i` to `waitlist`
	- While `q` is not empty, for `i = q.popleft()`:
		- Get candy : `res+=candies[i]`
		- Get key : Add `j` in `keys[i]` to `keyInv`
			- Update `q/waitlist` : If `j` in `waitlist` : add `j` to `q` and remove from `waitlist`
		- Get box : Add `j` in `containedBoxes[i]` to `boxInv`
			- Update `q/waitlist` : If `j` in `keyInv` : add `j` to `q`, else : add `j` to`waitlist`
