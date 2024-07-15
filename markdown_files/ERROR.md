<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ERROR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERROR rootpage-ERROR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ERROR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ERROR</a> statement is used to simulate a program error or to troubleshoot error handling procedures.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">ERROR</a> <i>codeNumber%</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can be used to test an error handling routine by simulating an error.</li>
<li>Error code 97 can be used to invoke the error handler for your own use, no real error in the program will trigger error 97.</li>
<li>Use error codes between 100 and 200 for custom program errors that will not be responded to by QB64.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Creating custom error codes for a program that can be handled by an <a href="ON_ERROR" title="ON ERROR">ON ERROR</a> handling routine.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> handler
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">ERROR</span></a> 123
x = x + 1
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">ERROR</span></a> 111
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
handler:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="ERR" title="ERR"><span style="color:#4593D8;">ERR</span></a>, <a href="ERRORLINE" title="ERRORLINE"><span style="color:#4593D8;">_ERRORLINE</span></a>
<a href="BEEP" title="BEEP"><span style="color:#4593D8;">BEEP</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><b>Note: Don't use error codes under 97 or over 200 as QB64 may respond to those errors and interrupt the program.</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="ERR" title="ERR">ERR</a>, <a href="ERL" title="ERL">ERL</a></li>
<li><a href="ERRORLINE" title="ERRORLINE">_ERRORLINE</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a> (list)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061307
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.043 seconds
Real time usage: 0.074 seconds
Preprocessor visited node count: 129/1000000
Post‐expand include size: 1432/2097152 bytes
Template argument size: 163/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   51.869      1 -total
 20.03%   10.389     15 Template:Cl
 13.64%    7.076      1 Template:CodeEnd
 13.61%    7.060      1 Template:PageDescription
 11.90%    6.172      1 Template:Parameter
  8.74%    4.534      1 Template:PageSeeAlso
  7.08%    3.673      1 Template:PageExamples
  7.04%    3.649      1 Template:PageSyntax
  6.14%    3.185      1 Template:PageNavigation
  5.93%    3.076      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:313-0!canonical and timestamp 20240715061307 and revision id 5980.
 -->
</div>
</div>
</div>
</div>
</body>
</html>