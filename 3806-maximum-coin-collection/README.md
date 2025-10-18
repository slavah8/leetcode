<h2><a href="https://leetcode.com/problems/maximum-coin-collection">3806. Maximum Coin Collection </a></h2><h3>Medium</h3><hr><p>Mario drives on a two-lane freeway with coins every mile. You are given two integer arrays, <code>lane1</code> and <code>lane2</code>, where the value at the <code>i<sup>th</sup></code> index represents the number of coins he <em>gains or loses</em> in the <code>i<sup>th</sup></code> mile in that lane.</p>

<ul>
	<li>If Mario is in lane 1 at mile <code>i</code> and <code>lane1[i] &gt; 0</code>, Mario gains <code>lane1[i]</code> coins.</li>
	<li>If Mario is in lane 1 at mile <code>i</code> and <code>lane1[i] &lt; 0</code>, Mario pays a toll and loses <code>abs(lane1[i])</code> coins.</li>
	<li>The same rules apply for <code>lane2</code>.</li>
</ul>

<p>Mario can enter the freeway anywhere and exit anytime after traveling <strong>at least</strong> one mile. Mario always enters the freeway on lane 1 but can switch lanes <strong>at most</strong> 2 times.</p>

<p>A <strong>lane switch</strong> is when Mario goes from lane 1 to lane 2 or vice versa.</p>

<p>Return the <strong>maximum</strong> number of coins Mario can earn after performing <strong>at most 2 lane switches</strong>.</p>

<p><strong>Note:</strong> Mario can switch lanes immediately upon entering or just before exiting the freeway.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">lane1 = [1,-2,-10,3], lane2 = [-5,10,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Mario drives the first mile on lane 1.</li>
	<li>He then changes to lane 2 and drives for two miles.</li>
	<li>He changes back to lane 1 for the last mile.</li>
</ul>

<p>Mario collects <code>1 + 10 + 0 + 3 = 14</code> coins.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">lane1 = [1,-1,-1,-1], lane2 = [0,3,4,-5]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Mario starts at mile 0 in lane 1 and drives one mile.</li>
	<li>He then changes to lane 2 and drives for two more miles. He exits the freeway before mile 3.</li>
</ul>

<p>He collects <code>1 + 3 + 4 = 8</code> coins.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">lane1 = [-5,-4,-3], lane2 = [-1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Mario enters at mile 1 and immediately switches to lane 2. He stays here the entire way.</li>
</ul>

<p>He collects a total of <code>2 + 3 = 5</code> coins.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">lane1 = [-3,-3,-3], lane2 = [9,-2,4]</span></p>

<p><strong>Output:</strong> 11</p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Mario starts at the beginning of the freeway and immediately switches to lane 2. He stays here the whole way.</li>
</ul>

<p>He collects a total of <code>9 + (-2) + 4 = 11</code> coins.</p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">lane1 = [-10], lane2 = [-2]</span></p>

<p><strong>Output:</strong> <span class="example-io">-2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since Mario must ride on the freeway for at least one mile, he rides just one mile in lane 2.</li>
</ul>

<p>He collects a total of -2 coins.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= lane1.length == lane2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= lane1[i], lane2[i] &lt;= 10<sup>9</sup></code></li>
</ul>
