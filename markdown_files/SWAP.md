<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SWAP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SWAP rootpage-SWAP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SWAP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SWAP</a> statement is used to exchange two variable or array element values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SWAP</a> <i>variable1</i>, <i>variable2</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>variable1</i> and <i>variable2</i> are any type variables whose values will be exchanged.</li>
<li>If either <i>variable1</i> or <i>variable2</i> is an array, then an element in the array must be designated.</li>
<li><a class="mw-selflink selflink">SWAP</a> can be used with string or number variable values. Both must be of the same type.</li>
<li>SWAP is often used to sort array elements into greater or lesser numerical or cumulative <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> values.</li>
<li>SWAP can be used in page flipping to change between source and destination pages.</li></ul>
<p>
<i>Example 1:</i> A simple SWAP of <a href="STRING" title="STRING">string</a> values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a$ = "one"
b$ = "two"
<a class="mw-selflink selflink"><span style="color:#4593D8;">SWAP</span></a> a$, b$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> b$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">two
one
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Creating Cryptograms by scrambling EVERY capital letter in the alphabet.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Letter$(65 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 90)
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 65 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 90                    'set ASCII codes and letters in order
  Letter$(a) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(a)              'create capitalized characters
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> a
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 65 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 90
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Letter$(i) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>      'find characters the same as the <a href="ASCII" title="ASCII"><span style="color:#4593D8;">ASCII</span></a> code index
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>: j = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 26) + 65: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> j = i    'loop until j &lt;&gt; i
    <a class="mw-selflink selflink"><span style="color:#4593D8;">SWAP</span></a> Letter$(i), Letter$(j)     'swap corresponding letter characters
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(i); " ";               'print normal alphabetical order
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 12, 10
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 65 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 90                    'display new alphabetical order
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Letter$(a); " ";
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
text$ = "This is how a normal sentence would look before being encrypted."
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 5: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$
L = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Code(L)                         'place ASCII code solution into an array
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 22, 5
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> L
  Code(i) = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(<a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(text$), i)   'in QB64, ASC can read by character position
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Code(i) &gt;= 65 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Code(i) &lt;= 90 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Letter$(Code(i)); <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(Code(i));
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i> Explanation:</i> The Letter$ <a href="STRING" title="STRING">STRING</a> <a href="Arrays" title="Arrays">array</a> is first created with the letters matching the <a href="ASCII" title="ASCII">ASCII</a> code index value. Every index is <b>swap</b>ped when the letter matches it's index code until every letter is different. The Code array holds the text code solution.</dd></dl>
<p>
<i>Example 3:</i> A very quick array sorting SUB procedure using recursion sorts 10 thousand numbers in milliseconds.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> swap2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>  'Demo only
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(10000) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> 'array can hold any type of value
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10000
  array(i) = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 1000 'populate array with random values to sort
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
start = <a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(array)  'lowest element
finish = <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(array) 'highest element
swap2 = 0                     'count swaps for demo only
start! = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>(.001)
<a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> QuickSort(start, finish, array())
ending! = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>(.001)
tmp$ = " array(0)= ##.#####     array(5000)= ###.####   array(10000)= ###.####"
<a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> tmp$; array(0); array(5000); array(10000)
<a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> " Elapsed time: #.###### seconds with #######, swaps"; ending! - start!; swap2&amp;
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> n = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10000             'check array sort order
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> array(n) &gt;= max! <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>     'max should match the array type
    max! = array(n)
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="BEEP" title="BEEP"><span style="color:#4593D8;">BEEP</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Bad sort order!"
    <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a>
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> QuickSort (start <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, finish <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, array() <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Hi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, Lo <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>, Middle <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
Hi = finish: Lo = start
Middle = array((Lo + Hi) / 2) 'find middle of array
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> array(Lo) &lt; Middle: Lo = Lo + 1: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> array(Hi) &gt; Middle: Hi = Hi - 1: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Lo &lt;= Hi <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">SWAP</span></a> array(Lo), array(Hi)
    swap2 = swap2 + 1                  'count swaps for demo only
    Lo = Lo + 1: Hi = Hi - 1
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>                               'If homework, you will fail
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> Lo &gt; Hi
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Hi &gt; start <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> QuickSort(start, Hi, array())
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Lo &lt; finish <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="CALL" title="CALL"><span style="color:#4593D8;">CALL</span></a> QuickSort(Lo, finish, array())
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> array(0)= 0.20200    array(5000)= 525.8505   array(10000)= 999.6196
 Elapsed time: 0.023438 seconds with 33,759 swaps
</pre>
</td></tr></tbody></table>
<dl><dd><b>NOTE:</b> The <i>swap2</i> shared value is used to count the swaps for the demo and can be removed from the SUB procedure for speed.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RND" title="RND">RND</a>, <a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a></li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a>, <a href="Arrays" title="Arrays">Arrays</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034229
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.063 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 921/1000000
Post‐expand include size: 7311/2097152 bytes
Template argument size: 1232/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.822      1 -total
 18.53%    7.378    123 Template:Cl
  7.73%    3.080      1 Template:Small
  7.37%    2.936      1 Template:PageSeeAlso
  7.19%    2.863      1 Template:PageSyntax
  6.65%    2.649      6 Template:Parameter
  6.25%    2.489      3 Template:CodeStart
  5.81%    2.313      1 Template:PageDescription
  5.59%    2.228      3 Template:CodeEnd
  5.54%    2.205      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:572-0!canonical and timestamp 20240715034229 and revision id 8171.
 -->
</div>
</div>
</div>
</div>
</body>
</html>