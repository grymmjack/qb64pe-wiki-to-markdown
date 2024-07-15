<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDRATE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDRATE rootpage-SNDRATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDRATE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDRATE</a> function returns the sample rate frequency per second of the current computer's sound card.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>sampleRate&amp;</i> = <a class="mw-selflink selflink">_SNDRATE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The sample rate frequency per second value returned can be any <a href="LONG" title="LONG">LONG</a> value. Common values are 22050 or 44100.</li>
<li><b>The sound card sample rate is determined by the sound card and it cannot be changed.</b></li>
<li><b>Do not assume this to be a certain value. Always write code that can adapt to whatever is returned.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See the example in <a href="SNDRAW" title="SNDRAW">_SNDRAW</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li>
<li><a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062503
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.022 seconds
Preprocessor visited node count: 20/1000000
Post‐expand include size: 597/2097152 bytes
Template argument size: 11/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   11.566      1 -total
 18.69%    2.162      1 Template:PageSyntax
 16.00%    1.851      1 Template:PageNavigation
 15.79%    1.826      1 Template:Parameter
 15.14%    1.751      1 Template:PageSeeAlso
 14.93%    1.727      1 Template:PageExamples
 14.66%    1.696      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:344-0!canonical and timestamp 20240715062503 and revision id 4844.
 -->
</div>
</div>
</div>
</div>
</body>
</html>