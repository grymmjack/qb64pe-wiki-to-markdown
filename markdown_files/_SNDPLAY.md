<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDPLAY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDPLAY rootpage-SNDPLAY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDPLAY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDPLAY</a> statement plays a sound designated by a file handle created by <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDPLAY</a> <i>handle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Make sure that the <i>handle&amp;</i> value is not 0 before attempting to play it.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Checking a handle value before playing
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> h&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAY</span></a> h&amp;
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDPAUSE" title="SNDPAUSE">_SNDPAUSE</a>, <a href="SNDPLAYING" title="SNDPLAYING">_SNDPLAYING</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062500
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 50/1000000
Post‐expand include size: 830/2097152 bytes
Template argument size: 49/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.937      1 -total
 11.78%    2.466      3 Template:Cl
 11.21%    2.348      1 Template:PageSyntax
 11.21%    2.347      1 Template:CodeStart
 10.72%    2.244      1 Template:PageExamples
 10.36%    2.169      2 Template:Parameter
 10.10%    2.114      1 Template:PageNavigation
 10.03%    2.099      1 Template:PageSeeAlso
  9.80%    2.051      1 Template:CodeEnd
  8.89%    1.862      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:340-0!canonical and timestamp 20240715062500 and revision id 6252.
 -->
</div>
</div>
</div>
</div>
</body>
</html>