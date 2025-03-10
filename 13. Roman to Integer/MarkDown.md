<div class="description__24sA"><div class="css-101rr4k"><div data-cy="question-title" class="css-v3d350">13. Roman to Integer</div><div class="css-10o4wqw"><div diff="easy" class="css-14oi08n">Easy</div><button class="btn__r7r7 css-1rdgofi"><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M7 19v-8H4v8h3zM7 9c0-.55.22-1.05.58-1.41L14.17 1l1.06 1.05c.27.27.44.65.44 1.06l-.03.32L14.69 8H21c1.1 0 2 .9 2 2v2c0 .26-.05.5-.14.73l-3.02 7.05C19.54 20.5 18.83 21 18 21H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h3zm2 0v10h9l3-7v-2h-9l1.34-5.34L9 9z"></path></svg><span>14783</span></button><button class="btn__r7r7 css-1rdgofi"><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 3v12c0 .55-.22 1.05-.58 1.41L9.83 23l-1.06-1.05c-.27-.27-.44-.65-.44-1.06l.03-.32.95-4.57H3c-1.1 0-2-.9-2-2v-2c0-.26.05-.5.14-.73l3.02-7.05C4.46 3.5 5.17 3 6 3h11zm-2 12V5H6l-3 7v2h9l-1.34 5.34L15 15zm2-2h3V5h-3V3h3a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-3v-2z"></path></svg><span>992</span></button><button class="btn__r7r7 css-1rdgofi"><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3 4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5 22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1-.1-.1C7.14 14.24 4 11.39 4 8.5 4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z"></path></svg><span>Add to List</span></button><button class="btn__r7r7 css-1rdgofi"><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M17 5V2l5 5h-9a2 2 0 0 0-2 2v8H9V9a4 4 0 0 1 4-4h4zm3 14V9h2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3v2H4v14h16z"></path></svg><span>Share</span></button></div></div><div class="content__u3I1 question-content__JfgR"><div><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two ones added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given a roman numeral, convert it to an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "III"
<strong>Output:</strong> 3
<strong>Explanation:</strong> III = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "LVIII"
<strong>Output:</strong> 58
<strong>Explanation:</strong> L = 50, V= 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "MCMXCIV"
<strong>Output:</strong> 1994
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 15</code></li>
	<li><code>s</code> contains only&nbsp;the characters <code>('I', 'V', 'X', 'L', 'C', 'D', 'M')</code>.</li>
	<li>It is <strong>guaranteed</strong>&nbsp;that <code>s</code> is a valid roman numeral in the range <code>[1, 3999]</code>.</li>
</ul>
</div></div><div style="position: relative;"><div class="css-q9155n"><div class="css-oqu510"><div class="css-y3si18">Accepted</div><div class="css-jkjiwi">4,142,818</div></div><div class="css-oqu510"><div class="css-y3si18">Submissions</div><div class="css-jkjiwi">6,578,819</div></div></div><div class="erd_scroll_detection_container erd_scroll_detection_container_animation_active" style="visibility: hidden; display: inline; width: 0px; height: 0px; z-index: -1; overflow: hidden; margin: 0px; padding: 0px;"><div dir="ltr" class="erd_scroll_detection_container" style="position: absolute; flex: 0 0 auto; overflow: hidden; z-index: -1; visibility: hidden; width: 100%; height: 100%; left: 0px; top: 0px;"><div class="erd_scroll_detection_container" style="position: absolute; flex: 0 0 auto; overflow: hidden; z-index: -1; visibility: hidden; inset: -11px -10px -10px -11px;"><div style="position: absolute; flex: 0 0 auto; overflow: scroll; z-index: -1; visibility: hidden; width: 100%; height: 100%;"><div style="position: absolute; left: 0px; top: 0px; width: 546px; height: 71px;"></div></div><div style="position: absolute; flex: 0 0 auto; overflow: scroll; z-index: -1; visibility: hidden; width: 100%; height: 100%;"><div style="position: absolute; width: 200%; height: 200%;"></div></div></div></div></div></div><div class="header__28Cb"><div class="title__3BS7" data-size="md">Seen this question in a real interview before?</div><div class="btn-wrapper__19Tg"><button class="btn__1z2C btn-xs__3fYh btn-info__3EMF action-btn__DKeo" data-no-border="false"><div class="btn-content-container__2HVS"><span class="btn-content__2V4r">Yes</span></div></button></div><div class="btn-wrapper__19Tg"><button class="btn__1z2C btn-xs__3fYh btn-info__3EMF action-btn__DKeo" data-no-border="false"><div class="btn-content-container__2HVS"><span class="btn-content__2V4r">No</span></div></button></div></div><div class="css-isal7m"><div class="css-blecvm e5i1odf0"><div class="css-1jqueqk"><div class="header__2X5E">Companies<svg viewBox="0 0 1024 1024" width="1em" height="1em" class="icon__1Md2 lock-icon__1hmE"><path fill-rule="evenodd" d="M512 0a269.474 269.474 0 0 1 269.474 269.474v107.79h53.894a161.684 161.684 0 0 1 161.685 161.683v323.369A161.684 161.684 0 0 1 835.368 1024H188.632A161.684 161.684 0 0 1 26.947 862.316V538.947a161.684 161.684 0 0 1 161.685-161.684h53.894v-107.79A269.474 269.474 0 0 1 512 0zm.647 618.119a80.842 80.842 0 1 0 0 161.684 80.842 80.842 0 0 0 0-161.684zM350.316 377.263h323.368v-107.79a161.684 161.684 0 0 0-323.368 0v107.79z"></path></svg></div></div><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2 css-1ehpd12"><path fill-rule="evenodd" d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></div><div class="css-1hky5w4"></div></div><div class="css-isal7m"><div class="css-blecvm e5i1odf0"><div class="css-1jqueqk"><div class="header__2RZv">Related Topics</div></div><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2 css-1ehpd12"><path fill-rule="evenodd" d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></div><div class="css-1hky5w4"><a class="topic-tag__1jni" href="/tag/hash-table/"><span data-size="xs" class="tag__24Rd">Hash Table</span></a><a class="topic-tag__1jni" href="/tag/math/"><span data-size="xs" class="tag__24Rd">Math</span></a><a class="topic-tag__1jni" href="/tag/string/"><span data-size="xs" class="tag__24Rd">String</span></a></div></div><div class="css-isal7m"><div class="css-blecvm e5i1odf0"><div class="css-1jqueqk"><div class="header__qVrK">Similar Questions</div></div><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2 css-1ehpd12"><path fill-rule="evenodd" d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></div><div class="css-1hky5w4"><div class="question__25Pw"><a class="title__1kvt" href="/problems/integer-to-roman/">Integer to Roman</a><div class="difficulty__ES5S">Medium</div></div></div></div><div class="css-isal7m"><div class="css-blecvm e5i1odf0"><div class="css-1jqueqk"><div class="header__f9p6">Show Hint 1</div></div><svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2 css-1ehpd12"><path fill-rule="evenodd" d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></div><div class="css-1hky5w4"><div>Problem is simpler to solve by working the string from back to front and using a map.</div></div></div></div>
