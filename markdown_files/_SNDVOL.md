<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDVOL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDVOL rootpage-SNDVOL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDVOL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDVOL</a> statement sets the volume of a sound loaded in memory using a handle from the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDVOL</a> <i>handle&amp;</i>, <i>volume!</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>volume!</i> is a value from 0 (silence) to 1 (full volume).</li>
<li>In versions <b>prior to build 20170811/60</b>, the sound identified by <i>handle&amp;</i> must have been opened using the <a href="SNDOPEN" title="SNDOPEN">"VOL" capability</a> to use this function.</li>
<li>Version <b>3.1.0</b> enables this for <b>"raw"</b> sounds.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">h&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("bell.wav")
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDVOL</span></a> h&amp;, 0.5
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> h&amp;
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDOPENRAW" title="SNDOPENRAW">_SNDOPENRAW</a></li>
<li><a href="SNDBAL" title="SNDBAL">_SNDBAL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062508
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 58/1000000
Post‐expand include size: 863/2097152 bytes
Template argument size: 74/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.168      1 -total
 24.04%    6.531      4 Template:Parameter
 12.29%    3.339      1 Template:PageSyntax
  9.85%    2.676      1 Template:PageDescription
  8.70%    2.365      1 Template:PageExamples
  8.69%    2.360      1 Template:CodeStart
  8.61%    2.338      3 Template:Cl
  8.14%    2.212      1 Template:CodeEnd
  8.10%    2.200      1 Template:PageSeeAlso
  6.85%    1.861      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:350-0!canonical and timestamp 20240715062508 and revision id 8589.
 -->
</div>
</div>
</div>
</div>
</body>
</html>