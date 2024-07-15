<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SPC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SPC rootpage-SPC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SPC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">SPC</a> function is used in <a href="PRINT" title="PRINT">PRINT</a> and <a href="LPRINT" title="LPRINT">LPRINT</a> statements to print or output a number of space characters.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>SPC(<i>count%</i>)</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>count</i> designates the number of column spaces to move the cursor in a <a href="PRINT" title="PRINT">PRINT</a> statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>When used in a <a href="PRINT" title="PRINT">PRINT</a> statement,
<ul><li><i>count%</i> is the number of space characters to print, overwriting existing characters.</li>
<li>If <i>count%</i> is greater than the number of columns left in the current row, remaining space characters are printed on the next row.</li></ul></li>
<li>When used in a <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a> statement,
<ul><li><i>count%</i> is the number of space characters to output.</li>
<li>If <i>count%</i> is less than or equal to zero, the function has no effect.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Using SPC to space a text print.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "123456789"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "abc" ; <a class="mw-selflink selflink"><span style="color:#4593D8;">SPC</span></a>(3) ; "123"</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">123456789
abc   123
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a></li>
<li><a href="LPRINT" title="LPRINT">LPRINT</a>, <a href="STRING$" title="STRING$">STRING$</a></li>
<li><a href="TAB" title="TAB">TAB</a>, <a href="SPACE$" title="SPACE$">SPACE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035543
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 69/1000000
Post‐expand include size: 959/2097152 bytes
Template argument size: 56/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   54.656      1 -total
 22.52%   12.311      1 Template:PageSyntax
 19.82%   10.833      5 Template:Parameter
 10.94%    5.981      1 Template:PageParameters
  5.21%    2.845      1 Template:PageDescription
  5.10%    2.787      3 Template:Cl
  4.98%    2.720      1 Template:CodeStart
  4.81%    2.628      1 Template:PageExamples
  4.57%    2.498      1 Template:CodeEnd
  4.54%    2.483      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:566-0!canonical and timestamp 20240715035543 and revision id 7420.
 -->
</div>
</div>
</div>
</div>
</body>
</html>