<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FILEEXISTS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FILEEXISTS rootpage-FILEEXISTS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FILEEXISTS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_FILEEXISTS</b> function determines if a designated file name exists and returns true (-1) or false (0).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>theFileExists%</i> = <a class="mw-selflink selflink">_FILEEXISTS</a>(<i>filename$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>filename$</i> parameter can be a literal or variable <a href="STRING" title="STRING">string</a> value that can include a path.</li>
<li>The function returns -1 when a file exists and 0 when it does not.</li>
<li>The function reads the system information directly without using a <a href="SHELL" title="SHELL">SHELL</a> procedure.</li>
<li>The function will use the appropriate Operating System path separators. <a href="OS$" title="OS$">_OS$</a> can determine the operating system.</li>
<li><b>This function does not guarantee that a file can be accessed or opened, just that it exists.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checks if a file exists before opening it.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_FILEEXISTS</span></a>(<span style="color:#FFB100;">"mysettings.ini"</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Settings file found."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a>, <a href="OS$" title="OS$">_OS$</a></li>
<li><a href="SHELL" title="SHELL">SHELL</a>, <a href="FILES" title="FILES">FILES</a></li>
<li><a href="KILL" title="KILL">KILL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192716
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.019 seconds
Real time usage: 0.024 seconds
Preprocessor visited node count: 88/1000000
Post‐expand include size: 1095/2097152 bytes
Template argument size: 170/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 38/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.587      1 -total
 11.03%    1.720      1 Template:PageSyntax
  9.95%    1.550      5 Template:Cl
  9.76%    1.522      1 Template:PageDescription
  9.75%    1.519      3 Template:Parameter
  9.43%    1.470      2 Template:Text
  8.82%    1.374      1 Template:PageSeeAlso
  8.67%    1.351      1 Template:PageNavigation
  8.58%    1.337      1 Template:PageExamples
  8.26%    1.288      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:142-0!canonical and timestamp 20240714192716 and revision id 8332.
 -->
</div>
</div>
</div>
</div>
</body>
</html>