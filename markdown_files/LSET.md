<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LSET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LSET rootpage-LSET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LSET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">LSET</a> left-justifies a fixed length string expression based on the size of the <a href="STRING" title="STRING">STRING</a> variable and string expression.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LSET</a> {stringVariable = stringExpression | stringExpression1 = stringExpression2}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the string expression is longer than a fixed length string variable the value is truncated from the right side in LSET or <a href="RSET" title="RSET">RSET</a>.</li>
<li>If the LSET string expression is smaller, spaces will occupy the extra positions to the right in the string.</li>
<li>LSET can be used with a <a href="FIELD" title="FIELD">FIELD</a> or <a href="TYPE" title="TYPE">TYPE</a> definition to set the buffer position before a <a href="PUT" title="PUT">PUT</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Using LSET with a <a href="FIELD" title="FIELD">FIELD</a> definition. Note: May create an empty (unchanged) file that can be deleted.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "testfile.dat" FOR <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> AS #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = 15
<a href="FIELD" title="FIELD"><span style="color:#4593D8;">FIELD</span></a> 1, 6 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> a$, 9 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> other$
<a href="FIELD" title="FIELD"><span style="color:#4593D8;">FIELD</span></a> 1, 2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> b$, 13 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> another$
<a class="mw-selflink selflink"><span style="color:#4593D8;">LSET</span></a> a$ = "1234567890"
<a class="mw-selflink selflink"><span style="color:#4593D8;">LSET</span></a> other$ = "1234567890"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$, b$, other$, another$
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">123456            12         123456789     3456123456789
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> How LSET can define two different string length values in one statement.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
<a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> ninestring
head <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 9
<a class="mw-redirect" href="END_TYPE" title="END TYPE"><span style="color:#4593D8;">END TYPE</span></a>
<a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> fivestring
head AS <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 5
<a class="mw-redirect" href="END_TYPE" title="END TYPE"><span style="color:#4593D8;">END TYPE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> me <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> ninestring, you <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> fivestring
me.head = "ACHES NOT"
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">LSET</span></a> you.head = me.head
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "me.head: "; me.head
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "you.head: "; you.head
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">me.head: ACHES NOT
you.head: ACHES
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RSET" title="RSET">RSET</a>, <a href="RTRIM$" title="RTRIM$">RTRIM$</a></li>
<li><a href="FIELD" title="FIELD">FIELD</a>, <a href="TYPE" title="TYPE">TYPE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061339
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 220/1000000
Post‐expand include size: 2189/2097152 bytes
Template argument size: 222/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.809      1 -total
 13.62%    2.290     27 Template:Cl
 10.29%    1.730      1 Template:PageSyntax
  8.61%    1.448      2 Template:CodeStart
  8.52%    1.433      1 Template:PageSeeAlso
  8.41%    1.413      1 Template:PageDescription
  8.32%    1.398      1 Template:PageExamples
  8.07%    1.357      1 Template:PageNavigation
  7.66%    1.288      2 Template:OutputStart
  7.62%    1.281      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:556-0!canonical and timestamp 20240715061339 and revision id 6084.
 -->
</div>
</div>
</div>
</div>
</body>
</html>