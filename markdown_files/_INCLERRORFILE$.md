<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_INCLERRORFILE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INCLERRORFILE rootpage-INCLERRORFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_INCLERRORFILE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_INCLERRORFILE$</a> function returns the name of the original source code <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> module that caused the most recent error.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>errfile$</i> = <a class="mw-selflink selflink">_INCLERRORFILE$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<p>If the last error occurred in the main module, <a class="mw-selflink selflink">_INCLERRORFILE$</a> returns an empty string.
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.1 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> DebugLine
<a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> 250 'simulated error code - an error in the main module leaves _INCLERRORLINE empty (= 0)
'<a href="$INCLUDE" title="$INCLUDE"><span style="color:#4593D8;">$INCLUDE</span></a>:'haserror.bi'
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
DebugLine:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "An error occurred. Please contact support with the following details:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "ERROR "; <a href="ERR" title="ERR"><span style="color:#4593D8;">ERR</span></a>; " ON LINE: "; <a href="ERRORLINE" title="ERRORLINE"><span style="color:#4593D8;">_ERRORLINE</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INCLERRORLINE" title="INCLERRORLINE"><span style="color:#4593D8;">_INCLERRORLINE</span></a> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "    IN MODULE "; <a class="mw-selflink selflink"><span style="color:#4593D8;">_INCLERRORFILE$</span></a>; " (line"; <a href="INCLERRORLINE" title="INCLERRORLINE"><span style="color:#4593D8;">_INCLERRORLINE</span></a>; ")"
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">An error occurred. Please contact support with the following details:
ERROR  250  ON LINE:  6
An error occurred. Please contact support with the following details:
ERROR  250  ON LINE:  9
    IN MODULE haserror.bi ( line 1 )
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INCLERRORLINE" title="INCLERRORLINE">_INCLERRORLINE</a></li>
<li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a>, <a href="ERR" title="ERR">ERR</a></li>
<li><a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li>
<li><a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062345
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 159/1000000
Post‐expand include size: 1761/2097152 bytes
Template argument size: 257/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.591      1 -total
 10.75%    3.612     18 Template:Cl
  9.05%    3.041      1 Template:PageSyntax
  7.82%    2.627      1 Template:CodeEnd
  7.39%    2.483      1 Template:Parameter
  7.31%    2.454      1 Template:OutputStart
  7.19%    2.414      1 Template:PageAvailability
  7.14%    2.400      1 Template:PageNavigation
  7.10%    2.384      1 Template:PageSeeAlso
  7.05%    2.369      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:156-0!canonical and timestamp 20240715062345 and revision id 7310.
 -->
</div>
</div>
</div>
</div>
</body>
</html>