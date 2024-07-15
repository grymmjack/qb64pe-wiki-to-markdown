<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ERR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERR rootpage-ERR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ERR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ERR</a> function returns the last QBasic error code number.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>errorNum%</i> = <a class="mw-selflink selflink">ERR</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If there is no error, the function returns 0</li>
<li>Can be used in an error handling routine to report the last error code number.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Simulating an error to test a program error handler that looks for a "Subscript out of range" error.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> handler
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 111  'simulate an error code that does not exist
x = x + 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 9        'simulate array boundary being exceeded
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
handler:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">ERR</span></a>, <a href="ERRORLINE" title="ERRORLINE"><span style="color:#4593D8;">_ERRORLINE</span></a>
<a href="BEEP" title="BEEP"><span style="color:#4593D8;">BEEP</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">ERR</span></a> = 9 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "The program has encountered an error and needs to close! Press a key!"
  K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
  <a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>               'RESUME can only be used in error handlers
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a>, <a href="RESUME" title="RESUME">RESUME</a></li>
<li><a href="ERL" title="ERL">ERL</a></li>
<li><a href="ERRORLINE" title="ERRORLINE">_ERRORLINE</a>, <a href="INCLERRORLINE" title="INCLERRORLINE">_INCLERRORLINE</a>, <a href="INCLERRORFILE$" title="INCLERRORFILE$">_INCLERRORFILE$</a></li>
<li><a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061306
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 178/1000000
Post‐expand include size: 1788/2097152 bytes
Template argument size: 232/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.061      1 -total
 13.28%    2.930     22 Template:Cl
 12.03%    2.653      1 Template:PageSeeAlso
 10.54%    2.326      1 Template:CodeEnd
 10.43%    2.300      1 Template:CodeStart
 10.29%    2.271      1 Template:PageSyntax
 10.05%    2.216      1 Template:PageNavigation
  9.67%    2.134      1 Template:PageExamples
  8.34%    1.841      1 Template:Parameter
  7.72%    1.702      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:314-0!canonical and timestamp 20240715061306 and revision id 5979.
 -->
</div>
</div>
</div>
</div>
</body>
</html>