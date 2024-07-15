<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDPLAYING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDPLAYING rootpage-SNDPLAYING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDPLAYING</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDPLAYING</a> function returns whether a sound is being played. Uses a handle from the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a> functions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>isPlaying%</i> = <a class="mw-selflink selflink">_SNDPLAYING</a>(<i>handle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns false (0) if a sound is not playing or true (-1) if it is.</li>
<li>If a sound is paused, <a class="mw-selflink selflink">_SNDPLAYING</a> returns 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAYING</span></a>(h&amp;)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a>, <a href="SNDPAUSE" title="SNDPAUSE">_SNDPAUSE</a>, <a href="SNDSTOP" title="SNDSTOP">_SNDSTOP</a></li>
<li><a href="SNDPAUSED" title="SNDPAUSED">_SNDPAUSED</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062502
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 43/1000000
Post‐expand include size: 789/2097152 bytes
Template argument size: 49/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.004      1 -total
 13.91%    3.477      1 Template:PageSyntax
 13.47%    3.367      1 Template:PageExamples
 11.54%    2.886      2 Template:Cl
 10.27%    2.567      2 Template:Parameter
  9.41%    2.353      1 Template:CodeStart
  9.32%    2.331      1 Template:PageNavigation
  9.25%    2.314      1 Template:PageSeeAlso
  8.87%    2.219      1 Template:CodeEnd
  8.77%    2.194      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:343-0!canonical and timestamp 20240715062502 and revision id 6255.
 -->
</div>
</div>
</div>
</div>
</body>
</html>