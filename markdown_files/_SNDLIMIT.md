<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDLIMIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDLIMIT rootpage-SNDLIMIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDLIMIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDLIMIT</a> statement stops playing a sound after it has been playing for a set number of seconds.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDLIMIT</a> <i>handle&amp;</i>, <i>numberOfSeconds!</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>handle&amp;</i> variable name is created using the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function from a loaded sound file.</li>
<li><i>numberOfSeconds!</i> is a <a href="SINGLE" title="SINGLE">SINGLE</a> value of seconds that the sound will play.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Sets how long a sound will be played in seconds. If the limit is set after the sound is started, the timer starts counting down from when the limit is applied, not from the start of playing.</li>
<li>Set <i>numberOfSeconds!</i> to 0 seconds to remove the limit.</li>
<li>Pausing or stopping the sound will also remove the limit.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDLIMIT</span></a> h&amp;, 5.5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDLEN" title="SNDLEN">_SNDLEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062455
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 51/1000000
Post‐expand include size: 830/2097152 bytes
Template argument size: 80/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.147      1 -total
 19.24%    5.993      1 Template:PageSyntax
  9.80%    3.052      1 Template:Cl
  9.54%    2.971      1 Template:PageSeeAlso
  9.53%    2.967      5 Template:Parameter
  9.08%    2.827      1 Template:PageExamples
  8.84%    2.753      1 Template:CodeEnd
  8.67%    2.699      1 Template:CodeStart
  7.24%    2.254      1 Template:PageParameters
  7.02%    2.186      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:334-0!canonical and timestamp 20240715062455 and revision id 6540.
 -->
</div>
</div>
</div>
</div>
</body>
</html>