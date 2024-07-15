<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENEXISTS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENEXISTS rootpage-SCREENEXISTS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENEXISTS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENEXISTS</a> function returns true (-1) once a screen has been created.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>screenReady%%</i> = <a class="mw-selflink selflink">_SCREENEXISTS</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Function returns true (-1) once a program screen is available to use or change.</li>
<li>Can be used to avoid program errors because a screen was not ready for input or alterations.
<ul><li>Use before <a href="TITLE" title="TITLE">_TITLE</a>, <a href="SCREENMOVE" title="SCREENMOVE">_SCREENMOVE</a> and other functions that require the output window to have been created.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Waiting in a loop until the screen exists to add the title. The <a href="LIMIT" title="LIMIT">_LIMIT</a> prevents the loop from using all CPU time while waiting.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENEXISTS</span></a>
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> "My Title"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FULLSCREEN" title="FULLSCREEN">_FULLSCREEN</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a></li>
<li><a href="$CONSOLE" title="$CONSOLE">$CONSOLE</a></li>
<li><a href="$RESIZE" title="$RESIZE">$RESIZE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062440
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 74/1000000
Post‐expand include size: 1038/2097152 bytes
Template argument size: 97/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.200      1 -total
 12.56%    2.034      1 Template:PageSyntax
 11.74%    1.902      7 Template:Cl
 10.33%    1.673      1 Template:Parameter
 10.26%    1.662      1 Template:CodeStart
 10.04%    1.626      1 Template:PageSeeAlso
  9.91%    1.605      1 Template:PageDescription
  9.73%    1.577      1 Template:PageNavigation
  9.70%    1.571      1 Template:CodeEnd
  9.64%    1.562      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:264-0!canonical and timestamp 20240715062440 and revision id 4818.
 -->
</div>
</div>
</div>
</div>
</body>
</html>