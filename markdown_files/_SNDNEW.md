<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDNEW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDNEW rootpage-SNDNEW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDNEW</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_SNDNEW</b> function creates a raw empty sound in memory and returns a <a href="LONG" title="LONG">LONG</a> handle value for later access.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>soundHandle&amp;</i> = <a class="mw-selflink selflink">_SNDNEW</a>(<i>frames&amp;</i>, <i>channels&amp;</i>, <i>bits&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>frames&amp;</i> is the number of sample frames needed. The number needed for one second of sound is determined by your sound hardware's sample rate, hence you may use the following formula:
<ul><li><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">frames&amp; = <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a> * neededSeconds!</span> where you may also specify fractional seconds.</li></ul></li>
<li><i>channels&amp;</i> is the number of channels needed (1 = mono, 2 = stereo).</li>
<li><i>bits&amp;</i> is the number of bits per channel (8 = 8-bit unsigned integer, 16 = 16-bit signed integer, 32 = 32-bit floating point).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use this function to create a raw sound in memory.</li>
<li>Once the sound is created, it can be accessed and manipulated using the <a href="MEM" title="MEM">_MEM</a> interface statements and functions, mainly <a href="MEMSOUND" title="MEMSOUND">_MEMSOUND</a>, <a href="MEMGET" title="MEMGET">_MEMGET</a> &amp; <a href="MEMPUT" title="MEMPUT">_MEMPUT</a>.</li>
<li>Using this function can generate sounds once programmatically and then play it multiple times.</li>
<li>The sound memory can also be filled with sample data from other sources like files, <a href="DATA" title="DATA">DATA</a> statements and more.</li>
<li>Sound memory pointers obtained with <a href="MEMSOUND" title="MEMSOUND">_MEMSOUND</a> must be freed using <a href="MEMFREE" title="MEMFREE">_MEMFREE</a> and the Sound handle value itself must be freed using <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a> when no longer required.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.5.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Creating a sound at runtime and playing it.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT"><span style="color:#4593D8;">OPTION _EXPLICIT</span></a>
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> SOUND_DURATION = 5 ' duration is seconds
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> SAMPLE_CHANNELS = 1 ' number of channes. For stereo we need to add another _MEMPUT below and +offset by SAMPLE_BYTES
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> SAMPLE_BYTES = 4 ' number of bytes / sample (not frame!)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> h <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: h = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDNEW</span></a>(SOUND_DURATION * <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>, SAMPLE_CHANNELS, SAMPLE_BYTES * 8)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> (h &lt; 1) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Failed to create sound!"
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> sndblk <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>: sndblk = <a href="MEMSOUND" title="MEMSOUND"><span style="color:#4593D8;">_MEMSOUND</span></a>(h, 0)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> sndblk.SIZE = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> h
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Failed to access sound data!"
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> t <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER64" title="INTEGER64"><span style="color:#4593D8;">_INTEGER64</span></a>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> t = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> (SOUND_DURATION * <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>) - 1
    <a href="MEMPUT" title="MEMPUT"><span style="color:#4593D8;">_MEMPUT</span></a> sndblk, sndblk.OFFSET + (t * SAMPLE_BYTES * SAMPLE_CHANNELS), <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(2 * <a href="PI" title="PI"><span style="color:#4593D8;">_PI</span></a> * 440 * t / <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>) + <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> - <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> ' mixes noise and a sine wave
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> h
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> SOUND_DURATION
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> h
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a>, <a href="MEMSOUND" title="MEMSOUND">_MEMSOUND</a>, <a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li>
<li><a href="MEMPUT" title="MEMPUT">_MEMPUT</a>, <a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a>, <a href="SNDRAW" title="SNDRAW">_SNDRAW</a>, <a href="SNDRATE" title="SNDRATE">_SNDRATE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062622
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.063 seconds
Preprocessor visited node count: 382/1000000
Post‐expand include size: 3384/2097152 bytes
Template argument size: 537/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.322      1 -total
 13.36%    5.387     46 Template:Cl
  8.76%    3.532      7 Template:Parameter
  8.17%    3.294      1 Template:PageSyntax
  6.90%    2.782      1 Template:InlineCode
  6.61%    2.667      1 Template:PageDescription
  6.39%    2.575      1 Template:PageAvailability
  6.05%    2.439      1 Template:CodeStart
  5.86%    2.364      1 Template:PageParameters
  5.41%    2.183      1 Template:InlineCodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1180-0!canonical and timestamp 20240715062622 and revision id 8063.
 -->
</div>
</div>
</div>
</div>
</body>
</html>