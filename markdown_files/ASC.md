<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ASC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ASC rootpage-ASC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ASC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>ASC</b> statement allows a program to change a character at any position of a <a href="STRING" title="STRING">STRING</a> variable.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">ASC</a>(<i>stringExpression$</i>[, <i>position%</i>]) = <i>code%</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><b>Note:</b> The statement variant of <b>ASC</b> is not available in QBasic/QuickBASIC, but in <b>QB64 only</b>.</li>
<li>The <i>stringExpression$</i> variable's value must have been previously defined and cannot be an empty string ("").</li>
<li><i>position%</i> is optional. If no position is used, the leftmost character at position 1 is assumed.</li>
<li><i>position%</i> cannot be zero or greater than the string's length or an <a href="ERROR_Codes" title="ERROR Codes">Illegal function call</a> error will occur.</li>
<li>The <a href="ASCII" title="ASCII">ASCII</a> replacement <i>code%</i> value can be any <a href="INTEGER" title="INTEGER">INTEGER</a> value from 0 to 255.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Demonstrates how to change existing text characters one letter at a time.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a$ = "YZC"
<a class="mw-selflink selflink"><span style="color:#4593D8;">ASC</span></a>(a$) = 65                 ' CHR$(65) = "A"
<a class="mw-selflink selflink"><span style="color:#4593D8;">ASC</span></a>(a$, 2) = 66              ' CHR$(66) = "B"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
<a class="mw-selflink selflink"><span style="color:#4593D8;">ASC</span></a>(a$, 2) = 32              ' CHR$(32) = " "
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
<a class="mw-selflink selflink"><span style="color:#4593D8;">ASC</span></a>(a$, 2) = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("S")        ' get code value from ASC function
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">ABC
A C
ASC
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1149" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="MID$" title="MID$">MID$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="ASCII" title="ASCII">ASCII</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034022
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 109/1000000
Post‐expand include size: 1219/2097152 bytes
Template argument size: 142/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.109      1 -total
 10.94%    2.529      1 Template:CodeEnd
 10.09%    2.332      1 Template:PageSeeAlso
  8.93%    2.063      1 Template:OutputStart
  8.79%    2.030      1 Template:OutputEnd
  8.72%    2.015      1 Template:PageSyntax
  8.61%    1.990      1 Template:PageNavigation
  8.36%    1.931      8 Template:Cl
  7.95%    1.837      7 Template:Parameter
  7.12%    1.645      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:396-0!canonical and timestamp 20240715034022 and revision id 8892.
 -->
</div>
</div>
</div>
</div>
</body>
</html>