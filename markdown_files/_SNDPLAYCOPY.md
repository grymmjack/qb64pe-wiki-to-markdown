<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDPLAYCOPY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDPLAYCOPY rootpage-SNDPLAYCOPY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDPLAYCOPY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDPLAYCOPY</a> statement copies a sound, plays it, and automatically closes the copy using a handle parameter passed from <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDPLAYCOPY</a> <i>handle&amp;</i>[, [<i>volume!</i>][, <i>x!</i>][, <i>y!</i>][, <i>z!</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <a href="LONG" title="LONG">LONG</a> <i>handle&amp;</i> value is returned by <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> using a specific sound file.</li>
<li>The <i>volume!</i> parameter can be any <a href="SINGLE" title="SINGLE">SINGLE</a> value from 0 (no volume) to 1 (full volume).</li>
<li><i>x!</i> distance values go from left (negative) to right (positive) (beginning with <b>v3.3.x</b>).</li>
<li><i>y!</i> distance values go from below (negative) to above (positive) (beginning with <b>v3.3.x</b>).</li>
<li><i>z!</i> distance values go from behind (negative) to in front (positive) (beginning with <b>v3.3.x</b>).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Makes coding easier by doing all of the following automatically:</li></ul>
<dl><dd><ol><li>Copies/duplicates the source handle (see <a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a>).</li>
<li>Changes the volume of the copy if volume is passed.</li>
<li>Applies stereo panning or a 3D position if x, y, z is passed.</li>
<li>Plays the copy.</li>
<li>Closes the copy.</li></ol></dd></dl>
<ul><li>This statement is a better choice than <a href="SNDPLAYFILE" title="SNDPLAYFILE">_SNDPLAYFILE</a> if the sound will be played often, reducing the burden on the computer.</li>
<li>By setting the x! value to -1 or 1 it plays the sound at full volume from the appropriate speaker.</li>
<li>Omitted x!, y! or z! values are set to 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Playing a previously opened sound from left and right speakers.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> h, i
h = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("explosion.wav")
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> h &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 1
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> i <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 2 = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Playing from right"
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAYCOPY</span></a> h, , 1
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Playing from left"
            <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAYCOPY</span></a> h, , -1
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Playing a sound at random volumes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">chomp&amp; = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("chomp.wav")
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> chomp&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDPLAYCOPY</span></a> chomp&amp;, 0.5 + <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 0.49
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li>
<li><a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a></li>
<li><a href="SNDPLAYFILE" title="SNDPLAYFILE">_SNDPLAYFILE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062501
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.076 seconds
Preprocessor visited node count: 242/1000000
Post‐expand include size: 2114/2097152 bytes
Template argument size: 292/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.852      1 -total
 19.90%   10.519     10 Template:Parameter
 12.84%    6.788      1 Template:PageSyntax
 12.58%    6.650      1 Template:PageParameters
 11.37%    6.008      2 Template:CodeEnd
  9.96%    5.265     25 Template:Cl
  5.85%    3.090      1 Template:PageSeeAlso
  5.17%    2.733      2 Template:CodeStart
  5.16%    2.728      1 Template:PageDescription
  4.68%    2.471      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:341-0!canonical and timestamp 20240715062501 and revision id 7416.
 -->
</div>
</div>
</div>
</div>
</body>
</html>