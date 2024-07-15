<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDBAL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDBAL rootpage-SNDBAL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDBAL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDBAL</a> statement attempts to set the balance or 3D position of a sound.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDBAL</a> <i>handle&amp;</i>[, <i>x!</i>][, <i>y!</i>][, <i>z!</i>][, <i>channel&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>handle&amp;</i> is a valid sound handle created by the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function.</li>
<li><i>x!</i> distance values go from left (negative) to right (positive).</li>
<li><i>y!</i> distance values go from below (negative) to above (positive).</li>
<li><i>z!</i> distance values go from behind (negative) to in front (positive).</li>
<li><i>channel&amp;</i> value 1 denotes left (mono) and 2 denotes right (stereo) channel (beginning with <b>build 20170811/60</b>)
<ul><li>The ability to set the balance per channel is gone in version <b>3.1.0</b> and higher.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Attempts to position a sound in 3D space, or as close to it as the underlying software libraries allow. In some cases, this will be true 3D positioning, in others, a mere volume adjustment based on distance alone.</li>
<li>Omitted x!, y! or z! <a href="SINGLE" title="SINGLE">SINGLE</a> values are set to 0 or not changed in <b>build 20170811/60 onward</b>.</li>
<li>By setting the x! value to -1 or 1 it plays the sound at full volume from the appropriate speaker.</li>
<li>Sounds at a distance of 1 or -1 are played at full volume. Sounds further than a distance of 1000 cannot be heard.</li>
<li>The volume decreases linearly (at a constant gradient) over distance. Half volume = 500.</li>
<li>An "<b>Illegal Function Call</b>" error can occur if another sound is using the primary or same channel position.</li>
<li>Opened sound files must have the <a href="SNDOPEN" title="SNDOPEN">"VOL"</a> capability to use this statement in versions <b>before build 20170811/60.</b></li>
<li>Version <b>3.1.0</b> enables this for <b>"raw"</b> sounds.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> This example loads, plays, and then bounces the sound between the left and right channels.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' This examples load, plays and then bounces the sound between the left and right channels
Laff&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("KONGlaff.ogg", "stream") 'load sound file and get LONG handle value
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Laff&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> Laff&amp; 'play sound
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Failed to load sound file."
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press ESC to stop."
dir = 0.01
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> laffx! &lt;= -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = 0.01
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> laffx! &gt;= 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = -0.01
    laffx! = laffx! + dir
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , 1: <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> "Balance = ##.##"; laffx!;
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDBAL</span></a> Laff&amp;, laffx! 'balance sound to left or right speaker
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(Laff&amp;) <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> &lt;&gt; 27
</pre>
</td></tr></tbody></table>
<p>
<i>Example:</i> Loading a sound after <b>build 20170811/60</b> - no need to specify "sound capabilities" in <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">s&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("song.ogg")
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "<a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a>Y"; s&amp;
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> s&amp;
<a href="SNDLOOP" title="SNDLOOP"><span style="color:#4593D8;">_SNDLOOP</span></a> s&amp;
xleft = -1
xright = 1
DO
    k$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> k$
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "f"
            xleft = xleft - 0.1
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDBAL</span></a> s&amp;, xleft, , , 1
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "g"
            xleft = xleft + 0.1
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDBAL</span></a> s&amp;, xleft, , , 1
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "h"
            xright = xright - 0.1
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDBAL</span></a> s&amp;, xright, , , 2
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "j"
            xright = xright + 0.1
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDBAL</span></a> s&amp;, xright, , , 2
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "n"
            volume = volume - 0.1
            <a href="SNDVOL" title="SNDVOL"><span style="color:#4593D8;">_SNDVOL</span></a> s&amp;, volume
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "m"
            volume = volume + 0.1
            <a href="SNDVOL" title="SNDVOL"><span style="color:#4593D8;">_SNDVOL</span></a> s&amp;, volume
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "p"
            <a href="SNDPAUSE" title="SNDPAUSE"><span style="color:#4593D8;">_SNDPAUSE</span></a> s&amp;
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> " "
            <a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> s&amp;
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "i"
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(s&amp;)
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SNDPAUSED" title="SNDPAUSED"><span style="color:#4593D8;">_SNDPAUSED</span></a>(s&amp;)
            <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "b"
            <a href="SNDSETPOS" title="SNDSETPOS"><span style="color:#4593D8;">_SNDSETPOS</span></a> s&amp;, 110
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "l"
            <a href="SNDLIMIT" title="SNDLIMIT"><span style="color:#4593D8;">_SNDLIMIT</span></a> s&amp;, 10
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "LIM"
            <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "k"
            <a href="SNDSTOP" title="SNDSTOP"><span style="color:#4593D8;">_SNDSTOP</span></a> s&amp;
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "c"
            <a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> s&amp;
            <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
            s2&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("song.ogg")
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> "d"
            s2&amp; = <a href="SNDCOPY" title="SNDCOPY"><span style="color:#4593D8;">_SNDCOPY</span></a>(s&amp;)
            <a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> s2&amp;
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> xleft, xright, volume, <a href="SNDGETPOS" title="SNDGETPOS"><span style="color:#4593D8;">_SNDGETPOS</span></a>(s&amp;); "   "
LOOP
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDOPENRAW" title="SNDOPENRAW">_SNDOPENRAW</a></li>
<li><a href="SNDVOL" title="SNDVOL">_SNDVOL</a>, <a href="SNDLIMIT" title="SNDLIMIT">_SNDLIMIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192856
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.049 seconds
Preprocessor visited node count: 573/1000000
Post‐expand include size: 4766/2097152 bytes
Template argument size: 900/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.484      1 -total
 14.62%    4.166     72 Template:Cl
  9.78%    2.786      1 Template:PageSyntax
  7.55%    2.151      1 Template:Small
  7.51%    2.140      9 Template:Parameter
  6.99%    1.992      1 Template:PageParameters
  6.62%    1.887      1 Template:PageDescription
  6.59%    1.878      2 Template:CodeEnd
  6.35%    1.808      1 Template:PageSeeAlso
  6.27%    1.785      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:329-0!canonical and timestamp 20240714192856 and revision id 8590.
 -->
</div>
</div>
</div>
</div>
</body>
</html>