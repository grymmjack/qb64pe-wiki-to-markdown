<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDCOPY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDCOPY rootpage-SNDCOPY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDCOPY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDCOPY</a> function copies a sound to a new handle so that two or more of the same sound can be played at once. The passed handle parameter is from the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>copyHandle&amp;</i> = <a class="mw-selflink selflink">_SNDCOPY</a>(<i>handle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns a new handle to the a copy in memory of the sound data referred to by the source handle.</li>
<li>No changes to the source handle (such as a volume change) are inherited.</li>
<li>The sound data referred to by the handle and its copies are not freed until all of them are closed.</li>
<li>In versions <b>prior to build 20170811/60</b>, the sound identified by <i>handle&amp;</i> must have been opened using the <a href="SNDOPEN" title="SNDOPEN">"SYNC" capability</a> to use this function.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDPLAYCOPY" title="SNDPLAYCOPY">_SNDPLAYCOPY</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062452
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.018 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 25/1000000
Post‐expand include size: 582/2097152 bytes
Template argument size: 25/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.463      1 -total
 34.61%    6.044      1 Template:PageSyntax
 17.32%    3.025      1 Template:PageDescription
 16.62%    2.902      1 Template:PageNavigation
 14.58%    2.546      3 Template:Parameter
 12.60%    2.200      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:331-0!canonical and timestamp 20240715062452 and revision id 381.
 -->
</div>
</div>
</div>
</div>
</body>
</html>