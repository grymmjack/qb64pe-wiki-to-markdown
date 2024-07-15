<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$UNSTABLE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_UNSTABLE rootpage-_UNSTABLE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$UNSTABLE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$UNSTABLE</a> metacommand is used to enable the use of features that have not yet been made a permanent part of the language. Features hidden behind this metacommand may have breaking changes or be removed between releases.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$UNSTABLE</a>: {MIDI, HTTP}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The current unstable features are as follows:
<ul><li><b>MIDI</b> allows usage of the <a href="$MIDISOUNDFONT" title="$MIDISOUNDFONT">$MIDISOUNDFONT</a> metacommand</li>
<li><b>HTTP</b> allows opening HTTP connections using <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">$UNSTABLE</a> exists as a way to allow usage of new language features before they are finalized as part of the language.</li>
<li>Any languages features hidden behind <a class="mw-selflink selflink">$UNSTABLE</a> may be changed in breaking ways in the next version of QB64-PE.</li>
<li>Language features that become a permanent part of the language will no longer require <a class="mw-selflink selflink">$UNSTABLE</a> to be used.</li>
<li>More than one <a class="mw-selflink selflink">$UNSTABLE</a> can be used in a program.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.2.0"><img alt="v3.2.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.2.0</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<ul><li>MIDI keyword added in <b>QB64-PE v3.2.0</b></li>
<li>HTTP keyword added in <b>QB64-PE v3.5.0</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">$UNSTABLE</span></a>:MIDI
' This line is only allowed when <a class="mw-selflink selflink"><span style="color:#4593D8;">$UNSTABLE</span></a>:MIDI is used
<a href="$MIDISOUNDFONT" title="$MIDISOUNDFONT"><span style="color:#4593D8;">$MIDISOUNDFONT</span></a>: Default
<a href="SNDPLAYFILE" title="SNDPLAYFILE"><span style="color:#4593D8;">_SNDPLAYFILE</span></a> "example.mid"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$MIDISOUNDFONT" title="$MIDISOUNDFONT">$MIDISOUNDFONT</a></li>
<li><a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193335
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 62/1000000
Post‐expand include size: 982/2097152 bytes
Template argument size: 88/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2368/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.667      1 -total
  7.38%    2.484      1 Template:PageSyntax
  6.42%    2.161      1 Template:PageParameters
  6.10%    2.052      1 Template:PageDescription
  5.58%    1.879      1 Template:PageAvailability
  5.52%    1.857      1 Template:PageExamples
  5.36%    1.804      4 Template:Cl
  5.31%    1.787      1 Template:PageNavigation
  4.55%    1.532      1 Template:CodeStart
  4.52%    1.522      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1030-0!canonical and timestamp 20240714193335 and revision id 7802.
 -->
</div>
</div>
</div>
</div>
</body>
</html>