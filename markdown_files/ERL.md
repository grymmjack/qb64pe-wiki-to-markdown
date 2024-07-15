<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ERL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERL rootpage-ERL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ERL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ERL</a> function returns the closest previous line number before the last error.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>lastErrorLine&amp;</i> = <a class="mw-selflink selflink">ERL</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used in an error handler to report the last line number used before the error.</li>
<li>If the program does not use line numbers, then ERL returns 0.</li>
<li>Use <a href="ERRORLINE" title="ERRORLINE">_ERRORLINE</a> to return the actual code line position of an error in a QB64 program.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Using a fake error code to return the line number position in a program.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> errorfix
1
<a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 250
<a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 250
5 <a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 250
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
errorfix:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">ERL</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">1
1
5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ERR" title="ERR">ERR</a></li>
<li><a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="ERRORLINE" title="ERRORLINE">_ERRORLINE</a>, <a href="INCLERRORLINE" title="INCLERRORLINE">_INCLERRORLINE</a>, <a href="INCLERRORFILE$" title="INCLERRORFILE$">_INCLERRORFILE$</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061306
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 95/1000000
Post‐expand include size: 1227/2097152 bytes
Template argument size: 96/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.354      1 -total
 12.32%    2.630      1 Template:PageSyntax
 10.71%    2.286     10 Template:Cl
 10.18%    2.173      1 Template:PageExamples
  9.22%    1.968      1 Template:OutputEnd
  8.82%    1.884      1 Template:CodeStart
  8.81%    1.881      1 Template:OutputStart
  8.73%    1.864      1 Template:PageDescription
  8.32%    1.777      1 Template:CodeEnd
  8.28%    1.769      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:315-0!canonical and timestamp 20240715061306 and revision id 5978.
 -->
</div>
</div>
</div>
</div>
</body>
</html>