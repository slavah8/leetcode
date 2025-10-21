<h2><a href="https://leetcode.com/problems/sort-array-by-absolute-value">4029. Sort Array By Absolute Value</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Rearrange elements of <code>nums</code> in <strong>non-decreasing</strong> order of their absolute value.</p>

<p>Return <strong>any</strong> rearranged array that satisfies this condition.</p>

<p><strong>Note</strong>: The absolute value of an integer x is defined as:</p>

<ul>
	<li><code>x</code> if <code>x &gt;= 0</code></li>
	<li><code>-x</code> if <code>x &lt; 0</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,-1,-4,1,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,1,3,-4,5]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The absolute values of elements in <code>nums</code> are 3, 1, 4, 1, 5 respectively.</li>
	<li>Rearranging them in increasing order, we get 1, 1, 3, 4, 5.</li>
	<li>This corresponds to <code>[-1, 1, 3, -4, 5]</code>. Another possible rearrangement is <code>[1, -1, 3, -4, 5].</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-100,100]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-100,100]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The absolute values of elements in <code>nums</code> are 100, 100 respectively.</li>
	<li>Rearranging them in increasing order, we get 100, 100.</li>
	<li>This corresponds to <code>[-100, 100]</code>. Another possible rearrangement is <code>[100, -100]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>
