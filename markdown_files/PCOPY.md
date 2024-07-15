<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PCOPY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PCOPY rootpage-PCOPY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PCOPY</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">PCOPY</a> statement copies one source screen page to a destination page in memory.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">PCOPY</a> <i>sourcePage%</i>, <i>destinationPage%</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>sourcePage%</i> is an image page in video memory.</li>
<li><i>destinationPage%</i> is the video memory location to copy the source image to.</li>
<li>The working page is set as 0. All drawing occurs there.</li>
<li>The visible page is set as any page number that the SCREEN mode allows.</li>
<li>The <a href="DISPLAY_(function)" title="DISPLAY (function)">_DISPLAY (function)</a> return can be used a page number reference in <b>QB64</b> (See Example 1).</li>
<li>The <b>QB64</b> <a href="DISPLAY" title="DISPLAY">_DISPLAY</a> statement can also be used to stop screen flicker without page flipping or <a href="CLS" title="CLS">CLS</a> and <b>is the recommended practice</b>.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li><i>sourcePage%</i> and <i>destinationPage%</i> numbers are limited by the SCREEN mode used. In <b>QB64</b>, the same limits don't apply.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Creating a mouse cursor using a page number that <b>you create</b> in memory without setting up page flipping.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32) 'any graphics mode should work without setting up pages
<a href="MOUSEHIDE" title="MOUSEHIDE"><span style="color:#4593D8;">_MOUSEHIDE</span></a>
SetupCursor
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello World!"
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> 'main loop must contain _MOUSEINPUT
'       other program code
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> SetupCursor
<a href="ON_TIMER(n)" title="ON TIMER(n)"><span style="color:#4593D8;">ON TIMER</span></a>(0.02) UpdateCursor
<a href="TIMER" title="TIMER"><span style="color:#4593D8;">TIMER</span></a> <a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> UpdateCursor
<a class="mw-selflink selflink"><span style="color:#4593D8;">PCOPY</span></a> <a href="DISPLAY_(function)" title="DISPLAY (function)"><span style="color:#4593D8;">_DISPLAY</span></a>, 100  'any page number as desination with the _DISPLAY function as source
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (<a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a>, <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 255, 0)
<a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "ND10F10L3F5L4H5L3"
<a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>                  'statement shows image
<a class="mw-selflink selflink"><span style="color:#4593D8;">PCOPY</span></a> 100, <a href="DISPLAY_(function)" title="DISPLAY (function)"><span style="color:#4593D8;">_DISPLAY</span></a> 'function return as destination page
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Works with <a href="DISPLAY_(function)" title="DISPLAY (function)">_DISPLAY (function)</a> as the other page. If mouse reads are not crucial, put the _MOUSEINPUT loop inside of the UpdateCursor Sub.</dd></dl>
<p>
<i>Example 2:</i> Bouncing balls
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 7, 0, 1, 0
 <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x(10), y(10), dx(10), dy(10)
 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
   x(a) = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 320) + 1
   y(a) = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 200) + 1
   dx(a) = (<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 2) - 1
   dy(a) = (<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 2) - 1
 <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
 <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
 <a class="mw-selflink selflink"><span style="color:#4593D8;">PCOPY</span></a> 1, 0                           'place image on the visible page 0
 <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
 <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 100                           'regulates speed of balls in QB64
 <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> a = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10
   <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a>(x(a), y(a)), 5, 15          'all erasing and drawing is done on page 1
    x(a) = x(a) + dx(a)
    y(a) = y(a) + dy(a)
   <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x(a) &gt; 320 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dx(a) = -dx(a): x(a) = x(a) - 1
   <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x(a) &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dx(a) = -dx(a): x(a) = x(a) + 1
   <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y(a) &gt; 200 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dy(a) = -dy(a): y(a) = y(a) - 1
   <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> y(a) &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dy(a) = -dy(a): y(a) = y(a) + 1
 <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
 <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) ' escape exit
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> PCOPY reduces the flickering produced by clearing the screen. x(a) = x(a) - 1, etc. is just to be safe that the balls stay within the boundaries. dx(a) = -dx(a), etc. is to keep the actual speed while inverting it (so that the ball "bounces"). The rest should be self-explanatory, but if you are unsure about arrays you might want to look at QB64 Tutorials -&gt; <a href="Arrays" title="Arrays">Arrays</a>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DISPLAY" title="DISPLAY">_DISPLAY</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192523
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 479/1000000
Post‐expand include size: 3859/2097152 bytes
Template argument size: 698/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.358      1 -total
 15.49%    3.463     59 Template:Cl
 10.46%    2.338      1 Template:PageSyntax
 10.08%    2.253      1 Template:PageSeeAlso
  9.44%    2.110      6 Template:Parameter
  9.08%    2.030      1 Template:PageDescription
  8.69%    1.943      1 Template:PageNavigation
  7.51%    1.678      2 Template:CodeEnd
  6.97%    1.558      1 Template:PageExamples
  6.85%    1.531      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:429-0!canonical and timestamp 20240714192523 and revision id 8055.
 -->
</div>
</div>
</div>
</div>
</body>
</html>