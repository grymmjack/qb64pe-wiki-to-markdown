<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDSETPOS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDSETPOS rootpage-SNDSETPOS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDSETPOS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDSETPOS</a> statement changes the current/starting playing position in seconds of a sound.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDSETPOS</a> <i>handle&amp;</i>, <i>position!</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Changes the current/starting playing position in seconds (a <a href="SINGLE" title="SINGLE">SINGLE</a> value) of a sound in memory.</li>
<li>If <i>position!</i> is past the length of the sound, playback will be interrupted.</li>
<li>Function cannot be called while a looping sound is being played (see <a href="SNDLOOP" title="SNDLOOP">_SNDLOOP</a>).</li>
<li>In versions <b>prior to build 20170811/60</b>, the sound identified by <i>handle&amp;</i> must have been opened using the <a href="SNDOPEN" title="SNDOPEN">"SETPOS" capability</a> to use this statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> To check the current playing position in an MP3 file, use <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a> with <a href="SNDGETPOS" title="SNDGETPOS">_SNDGETPOS</a> printed in a loop
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">SoundFile&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("YourSoundFile.mp3") '&lt;&lt;&lt; your MP3 sound file here!
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDSETPOS</span></a> SoundFile&amp;, 5.5   'set to play sound 5 1/2 seconds into music
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> SoundFile&amp;  'play sound
Do: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
   LOCATE 5, 2: PRINT "Current play position&gt; "; <a href="SNDGETPOS" title="SNDGETPOS"><span style="color:#4593D8;">_SNDGETPOS</span></a>(SoundFile&amp;)
LOOP UNTIL <a href="KEYDOWN" title="KEYDOWN"><span style="color:#4593D8;">_KEYDOWN</span></a>(27) OR <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(SoundFile&amp;) 'ESC or end of sound exit
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDGETPOS" title="SNDGETPOS">_SNDGETPOS</a>, <a href="SNDLEN" title="SNDLEN">_SNDLEN</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDLIMIT" title="SNDLIMIT">_SNDLIMIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034514
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 93/1000000
Post‐expand include size: 1154/2097152 bytes
Template argument size: 160/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.603      1 -total
 13.09%    2.436      8 Template:Cl
 12.79%    2.379      1 Template:PageSyntax
 10.91%    2.029      4 Template:Parameter
 10.01%    1.862      1 Template:CodeStart
  9.68%    1.801      1 Template:PageDescription
  9.57%    1.781      1 Template:CodeEnd
  9.24%    1.718      1 Template:PageExamples
  8.83%    1.642      1 Template:PageSeeAlso
  8.73%    1.623      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:348-0!canonical and timestamp 20240715034514 and revision id 6259.
 -->
</div>
</div>
</div>
</div>
</body>
</html>