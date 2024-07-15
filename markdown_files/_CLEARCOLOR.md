<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CLEARCOLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLEARCOLOR rootpage-CLEARCOLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CLEARCOLOR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CLEARCOLOR</a> statement sets a specific color to be treated as transparent when an image is later put (via <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>) onto another image.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_CLEARCOLOR</a> {<i>color&amp;</i>|_NONE}[, <i>Dest_Handle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>In color modes using a palette, <i>color&amp;</i> is the palette index of the new transparent color value or _NONE designates no clear colors.</li>
<li>If <i>color&amp;</i> is not a valid palette index, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li>In 32-bit color modes, <i>color&amp;</i> is the <a href="LONG" title="LONG">_LONG</a> color value of the new transparent color.</li>
<li>If <i>Dest_Handle&amp;</i> is omitted, the destination is assumed to be the current write page. Zero can designate the current program screen.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>Dest_Handle&amp;</i> is an invalid handle, then an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error is returned. Check for bad handle values of -1 first.</li>
<li>In 32-bit color modes, it simply sets the Alpha to 0 for all pixels matching the specified color.</li>
<li>In the second syntax, transparency is disabled for color modes using a palette.</li>
<li><b>Note:</b> <a href="SETALPHA" title="SETALPHA">_SETALPHA</a> can affect any _CLEARCOLOR alpha setting within the color range set.</li>
<li><b>NOTE: 32 bit <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> screen page backgrounds are transparent black or <a href="ALPHA" title="ALPHA">_ALPHA</a> 0. Use <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> or <a href="CLS" title="CLS">CLS</a> for opaque.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Using _CLEARCOLOR to "mask" the background color of an image.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
img&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<span style="color:#FFB100;">"qb64_trans.png"</span>)
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , img&amp;, <span style="color:#F580B1;">0</span> <span style="color:#919191;">'place actual image with background</span>
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>)
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">'clear screen with red background</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>), img&amp;
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , img&amp;, <span style="color:#F580B1;">0</span> <span style="color:#919191;">'place image without white background</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CLEARCOLOR_(function)" title="CLEARCOLOR (function)"><span style="color:#4593D8;">_CLEARCOLOR</span></a>(img&amp;) <span style="color:#919191;">'displays closest clear color attribute</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Using a _CLEARCOLOR transparency with images created on a <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> page. Does not require an image file.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">512</span>, <span style="color:#F580B1;">384</span>, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">' screen uses handle value</span>
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (<span style="color:#F580B1;">50</span>, <span style="color:#F580B1;">50</span>), <span style="color:#F580B1;">50</span>, <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">' create a red ball image</span>
<a href="PAINT" title="PAINT"><span style="color:#4593D8;">PAINT</span></a> (<span style="color:#F580B1;">50</span>, <span style="color:#F580B1;">50</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">128</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)
redball = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">101</span>, <span style="color:#F580B1;">101</span>, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">' create a new image page</span>
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , <span style="color:#F580B1;">0</span>, redball, (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">101</span>, <span style="color:#F580B1;">101</span>) <span style="color:#919191;">' put screen page 0 image onto redball page</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_CLEARCOLOR</span></a> <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>), redball <span style="color:#919191;">' makes black become see-through</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>) <span style="color:#919191;">' erase original ball and create a blue background</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">512</span>, <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">384</span>), redball
    <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">1</span> <span style="color:#919191;">' one second delay</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
</pre>
</td></tr></tbody></table>
<p><i>Example 3:</i> Fading an image with a _CLEARCOLOR background using a new page image to prevent <a href="SETALPHA" title="SETALPHA">_SETALPHA</a> changes.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">mainscreen = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>) <span style="color:#919191;">' Main Screen (viewable)</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> mainscreen
<a href="SCREENMOVE" title="SCREENMOVE"><span style="color:#4593D8;">_SCREENMOVE</span></a> <a class="mw-redirect" href="MIDDLE" title="MIDDLE"><span style="color:#4593D8;">_MIDDLE</span></a>
Image1&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<span style="color:#FFB100;">"qb64_trans.png"</span>) <span style="color:#919191;">'&lt;&lt;&lt;&lt;&lt;&lt; any image with one background color to clear</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Image1&amp; &lt; <span style="color:#F580B1;">-1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">'check loaded image handle value before using!</span>
    <a href="SOURCE" title="SOURCE"><span style="color:#4593D8;">_SOURCE</span></a> Image1&amp;
    clr~&amp; = <a href="POINT" title="POINT"><span style="color:#4593D8;">POINT</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">'get background color from image source</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_CLEARCOLOR</span></a> clr~&amp;, Image1&amp; <span style="color:#919191;">'clear background color of loaded image</span>
    NewImage1&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(Image1&amp;), <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(Image1&amp;), <span style="color:#F580B1;">32</span>) <span style="color:#919191;">'new image page</span>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Image1&amp;, NewImage1&amp; <span style="color:#919191;">'put image without background color on new page</span>
    <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> Image1&amp; <span style="color:#919191;">'free loaded image from memory</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> mainscreen:
a&amp; = <span style="color:#F580B1;">0</span>: d = <span style="color:#F580B1;">1</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">10</span> <span style="color:#919191;">'regulate speed of fades</span>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    a&amp; = a&amp; + d
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> a&amp; = <span style="color:#F580B1;">255</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> d = -d <span style="color:#919191;">'reverse fade</span>
    <a href="SETALPHA" title="SETALPHA"><span style="color:#4593D8;">_SETALPHA</span></a> a&amp;, , NewImage1&amp; <span style="color:#919191;">'sets alpha level of all colors to fade image page in/out</span>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">342</span>), NewImage1&amp;
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Alpha: "</span>; a&amp;
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> a&amp; = <span style="color:#F580B1;">0</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> If the _CLEARCOLOR image background was not put onto a separate page, <a href="SETALPHA" title="SETALPHA">_SETALPHA</a> would display it also.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CLEARCOLOR_(function)" title="CLEARCOLOR (function)">_CLEARCOLOR (function)</a></li>
<li><a href="SETALPHA" title="SETALPHA">_SETALPHA</a> <span style="color:#777777;">(sets transparency level)</span></li>
<li><a href="ALPHA" title="ALPHA">_ALPHA</a>, <a href="ALPHA32" title="ALPHA32">_ALPHA32</a> <span style="color:#777777;">(read functions)</span></li>
<li><a href="Images" title="Images">Images</a>, <a href="Creating_Sprite_Masks" title="Creating Sprite Masks">Creating Sprite Masks</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192638
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.058 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 1177/1000000
Post‐expand include size: 8415/2097152 bytes
Template argument size: 2495/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 810/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   44.946      1 -total
 21.94%    9.860      1 Template:PageParameters
 10.10%    4.538     88 Template:Text
  9.12%    4.099     61 Template:Cl
  6.81%    3.061      1 Template:PageSyntax
  5.92%    2.659      7 Template:Parameter
  4.90%    2.201      3 Template:CodeEnd
  4.71%    2.116      1 Template:PageSeeAlso
  4.59%    2.061      1 Template:PageDescription
  4.16%    1.870      3 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:86-0!canonical and timestamp 20240714192638 and revision id 8279.
 -->
</div>
</div>
</div>
</div>
</body>
</html>