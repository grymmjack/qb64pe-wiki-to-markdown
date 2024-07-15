<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ERRORLINE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERRORLINE rootpage-ERRORLINE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ERRORLINE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ERRORLINE</a> function returns the source code line number that caused the most recent runtime error.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>e%</i> = <a class="mw-selflink selflink">_ERRORLINE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used in program error troubleshooting.</li>
<li>Does not require that the program use line numbers as it counts the actual lines of code.</li>
<li>The code line can be found using the QB64 IDE (Use the shortcut <b>Ctrl+G</b> to go to a specific line) or any other text editor such as Notepad.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displaying the current program line using a simulated <a href="ERROR" title="ERROR">ERROR</a> code.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> DebugLine <span style="color:#919191;">'can't use GOSUB</span>
<a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> <span style="color:#F580B1;">250</span> <span style="color:#919191;">'simulated error code</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
DebugLine:
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ERRORLINE</span></a>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="INCLERRORLINE" title="INCLERRORLINE">_INCLERRORLINE</a>, <a href="INCLERRORFILE$" title="INCLERRORFILE$">_INCLERRORFILE$</a></li>
<li><a href="ERR" title="ERR">ERR</a>, <a href="ERL" title="ERL">ERL</a></li>
<li><a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062327
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 108/1000000
Post‐expand include size: 1253/2097152 bytes
Template argument size: 184/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 37/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.343      1 -total
 11.38%    2.315      1 Template:CodeEnd
 10.79%    2.195      3 Template:Text
 10.17%    2.069      1 Template:PageSyntax
 10.13%    2.060      1 Template:PageSeeAlso
  9.80%    1.994      8 Template:Cl
  9.43%    1.919      1 Template:PageNavigation
  8.25%    1.679      1 Template:PageDescription
  7.92%    1.612      1 Template:Parameter
  7.65%    1.557      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:133-0!canonical and timestamp 20240715062327 and revision id 8328.
 -->
</div>
</div>
</div>
</div>
</body>
</html>