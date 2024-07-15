<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>WRITE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WRITE rootpage-WRITE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">WRITE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">WRITE</a> statement writes a <a href="Comma" title="Comma">comma</a>-separated list of values to the screen without spacing.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">WRITE</a> [<i>expression, List</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>expressionList</i> is a comma-separated list of variable or literal values to be written to the screen.</li>
<li>Write statement separates displayed values using <a href="Comma" title="Comma">comma</a> separators(required) that will display on the screen.</li>
<li>Leading and trailing number spaces are omitted when displaying numerical values.</li>
<li><a href="STRING" title="STRING">String</a> <a href="Quotation_mark" title="Quotation mark">quotation marks</a> will also be displayed.</li>
<li><a href="Semicolon" title="Semicolon">Semicolons</a> cannot be used in or following the WRITE statement!</li></ul>
<p>
<i>Example:</i> Comparing WRITE to the same PRINT statement.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a% = 123
b$ = "Hello"
c! = 3.1415
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a%, b$, c!   'commas display tab spaced data
<a class="mw-selflink selflink"><span style="color:#4593D8;">WRITE</span></a> a%, b$, c!   'displays commas between values, strings retain end quotes
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">123        Hello      3.1415
123,"Hello",3.1415
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="WRITE_(file_statement)" title="WRITE (file statement)">WRITE #</a></li>
<li><a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT #</a></li>
<li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a></li>
<li><a href="PRINT_USING" title="PRINT USING">PRINT USING</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035607
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.040 seconds
Preprocessor visited node count: 44/1000000
Post‐expand include size: 824/2097152 bytes
Template argument size: 50/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.753      1 -total
 17.19%    4.772      1 Template:PageDescription
 15.59%    4.326      1 Template:CodeStart
 13.75%    3.817      1 Template:PageSyntax
 12.35%    3.428      2 Template:Parameter
  8.08%    2.241      2 Template:Cl
  7.27%    2.018      1 Template:CodeEnd
  6.29%    1.746      1 Template:OutputStart
  5.38%    1.492      1 Template:OutputEnd
  5.10%    1.416      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:547-0!canonical and timestamp 20240715035607 and revision id 6632.
 -->
</div>
</div>
</div>
</div>
</body>
</html>