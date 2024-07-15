<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RSET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RSET rootpage-RSET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RSET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>RSET</b> statement right-justifies a string according to length of the string expression.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>RSET string_variable = string_expression</dd></dl></dd></dl>
<p>
</p>
<ul><li>If the <i>string_expression</i> is longer than a fixed length string variable the value is truncated from the right side in <a href="LSET" title="LSET">LSET</a> or RSET.</li>
<li>If the <i>string_expression</i> is smaller than the fixed length, spaces will occupy the extra positions in the string.</li>
<li>RSET can be used with a <a href="FIELD" title="FIELD">FIELD</a> or <a href="TYPE" title="TYPE">TYPE</a> string definition to set the buffer position before a <a href="PUT" title="PUT">PUT</a>.</li></ul>
<p>
<i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> thestring <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 10
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "12345678901234567890"
<a class="mw-selflink selflink"><span style="color:#4593D8;">RSET</span></a> thestring = "Hello!"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> thestring
anystring$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(20)
<a class="mw-selflink selflink"><span style="color:#4593D8;">RSET</span></a> anystring$ = "Hello again!"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> anystring$
<a class="mw-selflink selflink"><span style="color:#4593D8;">RSET</span></a> thestring = "Over ten characters long"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> thestring
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">12345678901234567890
    Hello!
        Hello Again!
Over ten c
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Notice how "Hello!" ends at the tenth position because the length of <i>thestring</i> is 10. When we used SPACE$(20) the length of <i>anystring$</i> became 20 so "Hello Again!" ended at the 20th position. That is right-justified. The last line "Over ten c" is truncated as it didn't fit into <i>thestring'</i>s length of only 10 characters.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RTRIM$" title="RTRIM$">RTRIM$</a>, <a href="FIELD" title="FIELD">FIELD</a></li>
<li><a href="LSET" title="LSET">LSET</a>, <a href="LTRIM$" title="LTRIM$">LTRIM$</a></li>
<li><a href="PUT" title="PUT">PUT</a>, <a href="GET" title="GET">GET</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061411
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 103/1000000
Post‐expand include size: 1240/2097152 bytes
Template argument size: 104/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.471      1 -total
 16.47%    3.702      1 Template:PageSeeAlso
 14.81%    3.327     12 Template:Cl
 12.29%    2.762      1 Template:PageNavigation
 12.21%    2.744      1 Template:PageSyntax
 10.57%    2.375      1 Template:CodeStart
  9.28%    2.086      1 Template:OutputStart
  9.19%    2.066      1 Template:CodeEnd
  9.02%    2.028      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:262-0!canonical and timestamp 20240715061411 and revision id 7393.
 -->
</div>
</div>
</div>
</div>
</body>
</html>