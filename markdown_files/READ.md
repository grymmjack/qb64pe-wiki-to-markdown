<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>READ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-READ rootpage-READ skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">READ</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>READ</b> statement reads values from a <a href="DATA" title="DATA">DATA</a> field and assigns them to one or a comma separated list of variables.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><dl><dd><a class="mw-selflink selflink">READ</a> value1$[, value2!, value3%, ...]</dd></dl></dd></dl></dd></dl>
<p>
</p>
<ul><li>READ statements assign variables to <a href="DATA" title="DATA">DATA</a> statement values on a one-to-one basis sequentially.</li>
<li>A single READ statement may access one or more <a href="DATA" title="DATA">DATA</a> values. They are accessed in the order set.</li>
<li>Several READ statements may access the same <a href="DATA" title="DATA">DATA</a> statement block at the following sequential position.</li>
<li><a href="DATA" title="DATA">DATA</a> can be READ using <a href="STRING" title="STRING">STRING</a> or numerical <a href="TYPE" title="TYPE">TYPE</a> variables singularly or in a comma separated list:</li></ul>
<dl><dd><dl><dd><a href="STRING" title="STRING">STRING</a> READ variables can read quoted or unquoted text or numerical DATA values!</dd>
<dd>Numerical type READ variables can only read <b>unquoted</b> numerical DATA values!</dd>
<dd><b>If they do not agree, a <a href="ERROR_Codes" title="ERROR Codes">"Syntax error"</a> may result when run reading string data as numerical values!</b></dd></dl></dd></dl>
<ul><li>If the number of variables specified is fewer than the number of elements in the DATA statement(s), subsequent READ statements begin reading data at the next unread element. If there are no subsequent READ statements, the extra data is ignored.</li>
<li>If variable reads exceed the number of elements in the DATA field(s), an <a href="ERROR_Codes" title="ERROR Codes">"Out of data" error</a> will occur!</li>
<li>Use the <a href="RESTORE" title="RESTORE">RESTORE</a> statement to reread DATA statements from the start, with or without a line label as required.</li>
<li><a class="mw-redirect" href="ACCESS" title="ACCESS">ACCESS</a> READ can be used in an <a href="OPEN" title="OPEN">OPEN</a> statement to limit file access to read only, preserving file data.</li>
<li><b>WARNING! Do not place DATA fields after <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures! QB64 will FAIL to compile properly!</b></li></ul>
<dl><dd>QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.</dd></dl>
<p>
<i>Example 1:</i> Placing data into an array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> A(10) AS <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> I = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
   <a class="mw-selflink selflink"><span style="color:#4593D8;">READ</span></a> A(I)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> I
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> J = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
   <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> A(J);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 3.08, 5.19, 3.12, 3.98, 4.24
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 5.08, 5.55, 4.00, 3.16, 3.37
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 3.08  5.19  3.12  3.98  4.24  5.08  5.55  4  3.16  3.37
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> This program reads the values from the DATA statements into array A. After execution, the value of A(1) is 3.08, and so on. The DATA statements may be placed anywhere in the program; they may even be placed ahead of the READ statement.</dd></dl>
<p>
<i>Example 2:</i> Reading three pieces of data at once.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> PRINT " CITY ", " STATE  ", " ZIP"
 PRINT <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(30, "-")  'divider
   <a class="mw-selflink selflink"><span style="color:#4593D8;">READ</span></a> C$, S$, Z&amp;
 PRINT C$, S$, Z&amp;
 <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "DENVER,", COLORADO, 80211
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">  CITY        STATE       ZIP
 ------------------------------
 DENVER,     COLORADO     80211
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> String DATA values do not require quotes unless they contain commas, end spaces or QBasic keywords.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DATA" title="DATA">DATA</a>, <a href="RESTORE" title="RESTORE">RESTORE</a></li>
<li><a href="$EMBED" title="$EMBED">$EMBED</a>. <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a></li></ul>
<!-- 
NewPP limit report
Cached time: 20240715031659
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.028 seconds
Preprocessor visited node count: 137/1000000
Post‐expand include size: 1577/2097152 bytes
Template argument size: 138/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   13.529      1 -total
 14.82%    2.005     16 Template:Cl
 13.74%    1.859      1 Template:PageSyntax
 11.78%    1.594      2 Template:CodeStart
 10.13%    1.371      1 Template:PageSeeAlso
 10.07%    1.362      1 Template:PageNavigation
 10.00%    1.353      2 Template:OutputStart
  9.89%    1.338      2 Template:CodeEnd
  9.70%    1.312      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:240-0!canonical and timestamp 20240715031659 and revision id 8698.
 -->
</div>
</div>
</div>
</div>
</body>
</html>