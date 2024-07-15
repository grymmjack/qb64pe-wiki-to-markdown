<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDPAUSED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDPAUSED rootpage-SNDPAUSED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDPAUSED</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDPAUSED</a> function checks if a sound is paused. Uses a handle parameter passed from <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>isPaused%%</i> = <a class="mw-selflink selflink">_SNDPAUSED</a>(<i>handle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns true (-1) if the sound is paused. False (0) if not paused.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPAUSED</span></a>(h&amp;)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDPAUSE" title="SNDPAUSE">_SNDPAUSE</a>, <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a></li>
<li><a href="SNDSTOP" title="SNDSTOP">_SNDSTOP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034508
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 43/1000000
Post‐expand include size: 787/2097152 bytes
Template argument size: 47/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.143      1 -total
 20.51%    5.157      2 Template:Cl
 17.81%    4.477      1 Template:CodeEnd
 10.45%    2.628      1 Template:CodeStart
  9.16%    2.304      1 Template:PageSyntax
  8.69%    2.184      1 Template:PageSeeAlso
  8.13%    2.044      1 Template:PageNavigation
  7.49%    1.884      1 Template:PageExamples
  7.26%    1.825      2 Template:Parameter
  6.84%    1.719      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:339-0!canonical and timestamp 20240715034508 and revision id 7678.
 -->
</div>
</div>
</div>
</div>
</body>
</html>