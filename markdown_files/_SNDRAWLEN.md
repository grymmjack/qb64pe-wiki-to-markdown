<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDRAWLEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDRAWLEN rootpage-SNDRAWLEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDRAWLEN</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDRAWLEN</a> function returns the length, in seconds, of a <a href="SNDRAW" title="SNDRAW">_SNDRAW</a> sound currently queued.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>length#</i> = <a class="mw-selflink selflink">_SNDRAWLEN</a> [<i>pipeHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The optional <i>pipeHandle&amp;</i> parameter refers to the sound pipe opened using <a href="SNDOPENRAW" title="SNDOPENRAW">_SNDOPENRAW</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use <a class="mw-selflink selflink">_SNDRAWLEN</a> to determine the length of a sound queue during creation and when to stop playing the sound.</li>
<li>Ensure that <a class="mw-selflink selflink">_SNDRAWLEN</a> is comfortably above 0 (until you've actually finished playing sound).</li>
<li>If you are getting occasional random clicks, this generally means that <a class="mw-selflink selflink">_SNDRAWLEN</a> has dropped to 0.</li>
<li>The <a href="SNDRATE" title="SNDRATE">_SNDRATE</a> determines how many samples are played per second. However, the timing is achieved by the sound card and <a class="mw-selflink selflink">_SNDRAWLEN</a>, not your program.</li>
<li><b>Do not attempt to use <a href="TIMER" title="TIMER">_TIMER</a> or <a href="DELAY" title="DELAY">_DELAY</a> or <a href="LIMIT" title="LIMIT">_LIMIT</a> to control the timing of <a href="SNDRAW" title="SNDRAW">_SNDRAW</a> sounds. You may use them as usual for delays or to limit your program's CPU usage, but the decision of how much sound to queue should only be based on the remaining _SNDRAWLEN</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See the example in <a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li>
<li><a href="SNDRATE" title="SNDRATE">_SNDRATE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062506
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.037 seconds
Preprocessor visited node count: 31/1000000
Post‐expand include size: 662/2097152 bytes
Template argument size: 29/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.701      1 -total
 15.67%    2.931      1 Template:PageSeeAlso
 14.31%    2.676      1 Template:PageSyntax
 13.96%    2.611      1 Template:PageNavigation
 13.63%    2.549      1 Template:PageExamples
 13.47%    2.519      1 Template:PageDescription
 13.02%    2.434      3 Template:Parameter
 10.94%    2.046      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:347-0!canonical and timestamp 20240715062506 and revision id 6258.
 -->
</div>
</div>
</div>
</div>
</body>
</html>