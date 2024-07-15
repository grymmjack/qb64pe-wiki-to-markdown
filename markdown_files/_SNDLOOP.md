<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDLOOP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDLOOP rootpage-SNDLOOP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDLOOP</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDLOOP</a> statement is like <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a> but the sound is looped. Uses a handle from the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDLOOP</a> <i>handle&amp;</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Plays the sound identified by <i>handle&amp;</i> in a loop.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Loading a sound or music file and playing it in a loop until a key is pressed.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">bg = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("back.ogg") '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; change to your sound file name
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDLOOP</span></a> bg
DO
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 10   'keep CPU resources used low
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" 'key press program exit
<a href="SNDSTOP" title="SNDSTOP"><span style="color:#4593D8;">_SNDSTOP</span></a> bg
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> bg
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDSTOP" title="SNDSTOP">_SNDSTOP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062456
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 85/1000000
Post‐expand include size: 1108/2097152 bytes
Template argument size: 122/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.316      1 -total
 26.58%    8.591      1 Template:PageDescription
 12.07%    3.901      1 Template:PageExamples
  9.83%    3.178      2 Template:Parameter
  9.71%    3.139      1 Template:PageSyntax
  8.84%    2.857      8 Template:Cl
  7.92%    2.560      1 Template:CodeStart
  6.66%    2.151      1 Template:CodeEnd
  6.50%    2.100      1 Template:PageNavigation
  6.31%    2.038      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:335-0!canonical and timestamp 20240715062455 and revision id 6247.
 -->
</div>
</div>
</div>
</div>
</body>
</html>