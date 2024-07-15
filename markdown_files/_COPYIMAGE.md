<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_COPYIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-COPYIMAGE rootpage-COPYIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_COPYIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>This function creates an identical designated image in memory with a different negative <a href="LONG" title="LONG">LONG</a> handle value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>newhandle&amp; = <a class="mw-selflink selflink">_COPYIMAGE</a>(<i>imageHandle&amp;</i>[, <i>mode%</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <a href="LONG" title="LONG">LONG</a> <i>newhandle&amp;</i> value returned will be different than the source handle value supplied.</li>
<li>If <i>imageHandle&amp;</i> is designated being zero, the current software <a href="DEST" title="DEST">destination</a> screen or image is copied.</li>
<li>If 1 is designated instead of an <i>imageHandle&amp;</i>, it designates the last OpenGL hardware surface to copy.</li>
<li><i>Mode</i> 32 can be used to convert 256 color images to 32 bit colors.</li>
<li><i>Mode</i> 33 images are hardware accelerated in <b>version 1.000 and up</b>, and are created using <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> or <a class="mw-selflink selflink">_COPYIMAGE</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function copies any image or screen handle to a new and unique negative <a href="LONG" title="LONG">LONG</a> handle value.</li>
<li>Valid copy handles are less than -1. Invalid handles return -1 or 0 if it was never created.</li>
<li>Every attribute of the passed image or program screen is copied to a new handle value in memory.</li>
<li><b>32 bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> so that they are transparent when placed over other surfaces.</b></li></ul>
<dl><dd>Use <a href="CLS" title="CLS">CLS</a> or <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> to make a new surface background <a href="ALPHA" title="ALPHA">_ALPHA</a> 255 or opaque.</dd></dl>
<ul><li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li>
<li><b>It is important to free discarded images with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> to prevent PC memory allocation errors!</b></li>
<li><b>Do not try to free image handles currently being used as the active <a href="SCREEN" title="SCREEN">SCREEN</a>. Change screen modes first.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Restoring a Legacy SCREEN using the _COPYIMAGE return value.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (<span style="color:#F580B1;">160</span>, <span style="color:#F580B1;">100</span>), <span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">40</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<span style="color:#919191;">'backup screen before changing SCREEN mode</span>
oldmode&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_COPYIMAGE</span></a>(<span style="color:#F580B1;">0</span>) <span style="color:#919191;">'the 0 value designates the current destination SCREEN</span>
s&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">600</span>, <span style="color:#F580B1;">32</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> s&amp;
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>)-(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">500</span>), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>), BF
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> oldmode&amp; <span style="color:#919191;">'restore original screen</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> s&amp; &lt; <span style="color:#F580B1;">-1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> s&amp;
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Note</dt>
<dd>Only free valid handle values with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> AFTER a new <a href="SCREEN" title="SCREEN">SCREEN</a> mode is being used by the program.</dd></dl>
<dl><dt>Example 2</dt>
<dd>Program that copies desktop to a hardware image to form a 3D triangle (<b>version 1.000 and up</b>):</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
my_hardware_handle = <a class="mw-selflink selflink"><span style="color:#4593D8;">_COPYIMAGE</span></a>(<a href="SCREENIMAGE" title="SCREENIMAGE"><span style="color:#4593D8;">_SCREENIMAGE</span></a>, <span style="color:#F580B1;">33</span>) <span style="color:#919191;">'take a screenshot and use it as our texture</span>
<a href="MAPTRIANGLE" title="MAPTRIANGLE"><span style="color:#4593D8;">_MAPTRIANGLE</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">250</span>, <span style="color:#F580B1;">500</span>), my_hardware_handle <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> _
(<span style="color:#F580B1;">-1</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">-1</span>)-(<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">-1</span>)-(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">5</span>, <span style="color:#F580B1;">-10</span>), , <a href="SMOOTH_(function)" title="SMOOTH (function)"><span style="color:#4593D8;">_SMOOTH</span></a>
<a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">30</span>: <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>, <a href="MAPTRIANGLE" title="MAPTRIANGLE">_MAPTRIANGLE</a></li>
<li><a href="SOURCE" title="SOURCE">_SOURCE</a>, <a href="DEST" title="DEST">_DEST</a></li>
<li><a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a></li>
<li><a href="FILELIST$_(function)" title="FILELIST$ (function)">_FILELIST$ (function)</a> <span style="color:#777777;">(Demo of _COPYIMAGE)</span></li>
<li><a href="DISPLAYORDER" title="DISPLAYORDER">_DISPLAYORDER</a></li>
<li><a href="Hardware_images" title="Hardware images">Hardware images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192649
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 604/1000000
Post‐expand include size: 4763/2097152 bytes
Template argument size: 1132/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 170/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.551      1 -total
 11.23%    3.094     45 Template:Text
 10.04%    2.766     32 Template:Cl
  8.33%    2.296      1 Template:PageSyntax
  6.88%    1.895      2 Template:Parameter
  6.23%    1.717      2 Template:CodeEnd
  6.11%    1.683      1 Template:PageParameters
  6.04%    1.663      2 Template:Small
  6.03%    1.660      1 Template:PageDescription
  6.01%    1.656      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:103-0!canonical and timestamp 20240714192649 and revision id 8683.
 -->
</div>
</div>
</div>
</div>
</body>
</html>