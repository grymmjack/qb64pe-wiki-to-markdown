<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDPLAYFILE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDPLAYFILE rootpage-SNDPLAYFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDPLAYFILE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDPLAYFILE</a> statement is used to play a sound file without generating a handle, automatically closing it after playback finishes.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDPLAYFILE</a> <i>filename$</i>[, <i>ignored%</i>][, <i>volume!</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Supported file formats are <b>WAV, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD or RAD (v2 only)</b>. See <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.</li>
<li><i>ignored%</i> is an optional parameter , accepted for historical reasons.
<ul><li>In versions prior to <b>build 20170811/60</b>, <i>ignored%</i> identified if a sound was to be loaded with <a href="SNDOPEN" title="SNDOPEN">"SYNC" capabilities</a>, (-1 for true, 0 for false). This is true for all sound files in the latest versions, making this parameter safe to be ignored.</li></ul></li>
<li><i>volume!</i> is a <a href="SINGLE" title="SINGLE">SINGLE</a> value from 0 (silence) to 1 (full volume). If not used or outside this range, the sound will be played at full volume.</li>
<li><a class="mw-selflink selflink">_SNDPLAYFILE</a> never creates an error. If the sound cannot be played it takes no further action.</li>
<li>The sound is closed automatically after it finishes playing.</li>
<li>When a sound will be used often, open the file with <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> and use <a href="SNDPLAYCOPY" title="SNDPLAYCOPY">_SNDPLAYCOPY</a> to play the handle instead to reduce the burden on the computer.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Playing a sound file at half volume.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAYFILE</span></a> "dog.wav", , .5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a></li>
<li><a href="SNDPLAYCOPY" title="SNDPLAYCOPY">_SNDPLAYCOPY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062502
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.061 seconds
Preprocessor visited node count: 52/1000000
Post‐expand include size: 786/2097152 bytes
Template argument size: 71/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   34.484      1 -total
 24.90%    8.588      1 Template:CodeEnd
 18.93%    6.528      1 Template:PageSeeAlso
  8.04%    2.771      1 Template:PageSyntax
  7.61%    2.623      6 Template:Parameter
  7.55%    2.602      1 Template:PageExamples
  7.36%    2.537      1 Template:PageNavigation
  7.25%    2.500      1 Template:CodeStart
  7.17%    2.473      1 Template:Cl
  6.91%    2.382      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:342-0!canonical and timestamp 20240715062502 and revision id 6254.
 -->
</div>
</div>
</div>
</div>
</body>
</html>