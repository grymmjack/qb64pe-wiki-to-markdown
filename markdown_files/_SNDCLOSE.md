<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDCLOSE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDCLOSE rootpage-SNDCLOSE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDCLOSE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDCLOSE</a> statement frees and unloads an open sound using a <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a> handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDCLOSE</a> <i>handle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the sound is still playing, it will be freed automatically after it finishes.
<ul><li>Closing a looping/paused/etc. sound means it is never freed until the QB64 program terminates.</li></ul></li>
<li>When your QB64 program terminates, all sounds are automatically freed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDSTOP" title="SNDSTOP">_SNDSTOP</a>, <a href="SNDPAUSE" title="SNDPAUSE">_SNDPAUSE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062451
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.022 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 556/2097152 bytes
Template argument size: 7/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.080      1 -total
 41.99%   10.950      1 Template:PageSyntax
 15.48%    4.038      1 Template:Parameter
 15.11%    3.941      1 Template:PageDescription
 14.48%    3.776      1 Template:PageSeeAlso
  9.75%    2.543      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:330-0!canonical and timestamp 20240715062451 and revision id 7674.
 -->
</div>
</div>
</div>
</div>
</body>
</html>