<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DONTWAIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DONTWAIT rootpage-DONTWAIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DONTWAIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_DONTWAIT</a> is used with the <a href="SHELL" title="SHELL">SHELL</a> statement in <b>QB64</b> to specify that the program shouldn't wait until the external command/program is finished (which it otherwise does by default).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="SHELL" title="SHELL">SHELL</a> [[[_DONTWAIT] [<i>commandLine$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Runs the command/program specified in <i>commandline$</i> and lets the calling program continue at the same time in its current screen format.</li>
<li>Especially useful when CMD /C or START is used in a SHELL command line to run another program.</li>
<li><b>QB64</b> automatically uses CMD /C or COMMAND /C when using SHELL.</li>
<li><b>QB64</b> program screens will not get distorted or minimized like QBasic fullscreen modes would.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_DONTWAIT</span></a> <span style="color:#FFB100;">"notepad "</span> + filename$
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">1</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<p>(opens up notepad at the same time as counting to 5)
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1
 2
 3
 4
 5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SHELL" title="SHELL">SHELL</a>, <a href="HIDE" title="HIDE">_HIDE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035659
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 114/1000000
Post‐expand include size: 1289/2097152 bytes
Template argument size: 157/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 10/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   21.732      1 -total
  9.20%    1.999      1 Template:PageSyntax
  8.82%    1.916      7 Template:Cl
  8.73%    1.898      4 Template:Text
  8.08%    1.757      1 Template:PageExamples
  7.89%    1.714      1 Template:PageNavigation
  7.68%    1.668      1 Template:PageDescription
  7.61%    1.653      1 Template:CodeStart
  7.29%    1.584      2 Template:Parameter
  7.27%    1.581      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:127-0!canonical and timestamp 20240715035659 and revision id 8316.
 -->
</div>
</div>
</div>
</div>
</body>
</html>