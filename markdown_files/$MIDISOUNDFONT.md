<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$MIDISOUNDFONT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_MIDISOUNDFONT rootpage-_MIDISOUNDFONT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$MIDISOUNDFONT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$MIDISOUNDFONT</a> metacommand enables MIDI support for <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.
<span style="color:red;"><b>MIDI functionality is current unstable, and requires <a href="$UNSTABLE" title="$UNSTABLE">$UNSTABLE</a>:MIDI to be able to use.</b></span>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$MIDISOUNDFONT</a>: {DEFAULT|"<i>Filename</i>"}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>DEFAULT indicates that the soundfont provided by QB64-PE should be used to play MIDI files.
<ul><li>The provided soundfont is about 1MB in size.</li></ul></li>
<li><i>Filename</i> can be used to provide your own soundfont for playing MIDI files.
<ul><li>The specified soundfont file is compiled into your program and is not required at runtime.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The use of this metacommand allows <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> to open MIDI files.</li>
<li>The selected soundfont is what is used to play all MIDI files.</li></ul>
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
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#4593D8;">$UNSTABLE</span></a>:MIDI
' This line is only allowed when <a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#4593D8;">$UNSTABLE</span></a>:MIDI is used
<a class="mw-selflink selflink"><span style="color:#4593D8;">$MIDISOUNDFONT</span></a>: Default
<a href="SNDPLAYFILE" title="SNDPLAYFILE"><span style="color:#4593D8;">_SNDPLAYFILE</span></a> "example.mid"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#4593D8;">$UNSTABLE</span></a>:MIDI
' Using a custom soundfont rather than the default
<a class="mw-selflink selflink"><span style="color:#4593D8;">$MIDISOUNDFONT</span></a>: "soundfont.sf2"
<a href="SNDPLAYFILE" title="SNDPLAYFILE"><span style="color:#4593D8;">_SNDPLAYFILE</span></a> "example.mid"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$UNSTABLE" title="$UNSTABLE">$UNSTABLE</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062611
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.053 seconds
Real time usage: 0.070 seconds
Preprocessor visited node count: 101/1000000
Post‐expand include size: 1395/2097152 bytes
Template argument size: 273/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2368/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   53.982      1 -total
  5.00%    2.697      1 Template:PageExamples
  4.84%    2.615      1 Template:PageParameters
  4.62%    2.492      1 Template:PageSyntax
  4.49%    2.422      2 Template:Parameter
  4.38%    2.364      1 Template:Text
  4.01%    2.163      2 Template:CodeStart
  3.80%    2.050      1 Template:PageDescription
  3.71%    2.005      7 Template:Cl
  3.65%    1.969      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1031-0!canonical and timestamp 20240715062611 and revision id 7799.
 -->
</div>
</div>
</div>
</div>
</body>
</html>