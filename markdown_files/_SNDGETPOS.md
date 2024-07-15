<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDGETPOS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDGETPOS rootpage-SNDGETPOS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDGETPOS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDGETPOS</a> function returns the current playing position in seconds using a handle from <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>position</i> = <a class="mw-selflink selflink">_SNDGETPOS</a>(<i>handle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the current playing position in seconds from an open sound file.</li>
<li>If a sound isn't playing, it returns 0.</li>
<li>If a sound is paused, it returns the paused position.</li>
<li>For a looping sound, the value returned continues to increment and does not reset to 0 when the sound loops.</li>
<li>In versions <b>prior to build 20170811/60</b>, the sound identified by <i>handle&amp;</i> must have been opened using the <a href="SNDOPEN" title="SNDOPEN">"SETPOS" capability</a> to use this function.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> To check the current playing position in an MP3 file, use <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a> with <a class="mw-selflink selflink">_SNDGETPOS</a> printed in a loop:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">SoundFile&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("YourSoundFile.mp3") '&lt;&lt;&lt; your MP3 sound file here!
<a href="SNDSETPOS" title="SNDSETPOS"><span style="color:#4593D8;">_SNDSETPOS</span></a> SoundFile&amp;, 5.5   'set to play sound 5 1/2 seconds into music
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> SoundFile&amp;  'play sound
Do: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
   LOCATE 5, 2: PRINT "Current play position&gt; "; <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDGETPOS</span></a>(SoundFile&amp;)
LOOP UNTIL <a href="KEYDOWN" title="KEYDOWN"><span style="color:#4593D8;">_KEYDOWN</span></a>(27) OR <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(SoundFile&amp;) 'ESC or end of sound exit
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDSETPOS" title="SNDSETPOS">_SNDSETPOS</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062453
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 89/1000000
Post‐expand include size: 1140/2097152 bytes
Template argument size: 150/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.498      1 -total
 13.69%    3.490      1 Template:PageSyntax
 11.42%    2.913      8 Template:Cl
 10.80%    2.755      1 Template:PageNavigation
 10.74%    2.738      1 Template:CodeEnd
 10.51%    2.681      3 Template:Parameter
  9.46%    2.413      1 Template:CodeStart
  9.39%    2.394      1 Template:PageSeeAlso
  8.63%    2.201      1 Template:PageExamples
  8.61%    2.195      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:332-0!canonical and timestamp 20240715062453 and revision id 6245.
 -->
</div>
</div>
</div>
</div>
</body>
</html>