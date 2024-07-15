<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SHELLHIDE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SHELLHIDE rootpage-SHELLHIDE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SHELLHIDE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SHELLHIDE</a> function hides the console window and returns any <a href="INTEGER" title="INTEGER">INTEGER</a> code sent when a program exits.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>returnCode%</i> = <a class="mw-selflink selflink">_SHELLHIDE</a>(<i>externalCommand$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The literal or variable <a href="STRING" title="STRING">STRING</a> <i>externalCommand$</i> parameter can be any external command or call to another program.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>A QB64 program can return codes specified after <a href="END" title="END">END</a> or <a href="SYSTEM" title="SYSTEM">SYSTEM</a> calls.</li>
<li>The <i>returnCode%</i> is usually 0 when the external program ends with no errors.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Shelling to another QB64 program will return the exit code when one is set in the  program that is run.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">returncode% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SHELLHIDE</span></a>("DesktopSize") 'replace call with your program EXE
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> returncode%
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> To set a program exit code use an <a href="INTEGER" title="INTEGER">INTEGER</a> parameter value after <a href="END" title="END">END</a> or <a href="SYSTEM" title="SYSTEM">SYSTEM</a> in the called program.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL_(function)" title="SHELL (function)">SHELL (function)</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a>, <a href="HIDE" title="HIDE">_HIDE</a></li>
<li><a href="CONSOLE" title="CONSOLE">_CONSOLE</a>, <a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a></li>
<li><a href="SYSTEM" title="SYSTEM">SYSTEM</a>, <a href="END" title="END">END</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035824
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 61/1000000
Post‐expand include size: 918/2097152 bytes
Template argument size: 90/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.031      1 -total
 11.36%    2.843      1 Template:CodeStart
 11.01%    2.757      1 Template:PageSyntax
 10.05%    2.515      3 Template:Cl
  9.15%    2.291      1 Template:PageNavigation
  9.09%    2.275      1 Template:PageParameters
  9.02%    2.257      1 Template:PageSeeAlso
  9.01%    2.255      1 Template:PageExamples
  8.66%    2.167      1 Template:CodeEnd
  8.63%    2.159      4 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:326-0!canonical and timestamp 20240715035824 and revision id 6534.
 -->
</div>
</div>
</div>
</div>
</body>
</html>