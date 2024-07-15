<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DONTBLEND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DONTBLEND rootpage-DONTBLEND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DONTBLEND</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DONTBLEND</a> statement turns off 32 bit alpha blending for the current image or screen mode where <a href="BLEND" title="BLEND">_BLEND</a> is default.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_DONTBLEND</a> [<i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current <a href="DEST" title="DEST">_DESTination</a> write page.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is not valid, an <a href="ERROR_Codes" title="ERROR Codes">Invalid handle</a> error will occur.</li>
<li><a class="mw-selflink selflink">_DONTBLEND</a> is faster than the default <a href="BLEND" title="BLEND">_BLEND</a>. <b>You may want to disable it</b>, unless you really need to use it in 32 bit.</li>
<li><b>32 bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> so that they are transparent when placed over other surfaces.</b></li>
<li>Use <a href="CLS" title="CLS">CLS</a> to make a new surface background <a href="ALPHA" title="ALPHA">_ALPHA</a> 255 or opaque.</li>
<li>Both <a href="SOURCE" title="SOURCE">_SOURCE</a> and <a href="DEST" title="DEST">_DEST</a> must have <a href="BLEND" title="BLEND">_BLEND</a> enabled, or else colors will NOT blend.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Use _DONTBLEND when you want the 32 bit screen surface to be opaque so that it covers up other backgrounds. <a href="CLS" title="CLS">CLS</a> works too.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">1280</span>, <span style="color:#F580B1;">720</span>, <span style="color:#F580B1;">32</span>)
<span style="color:#919191;">'CLS</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">_DONTBLEND</span></a> <span style="color:#919191;">'&lt;&lt;&lt; comment out to see the difference</span>
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (<span style="color:#F580B1;">100</span>, <span style="color:#F580B1;">100</span>)-(<span style="color:#F580B1;">500</span>, <span style="color:#F580B1;">500</span>), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>), BF
b&amp; = <span style="color:#55FF55;">SaveBackground&amp;</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This is just test junk"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hit any key and the text should disappear, leaving us our pretty yellow box."</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<span style="color:#55FF55;">RestoreBackground</span> b&amp;
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">SaveBackground&amp;</span>
    <span style="color:#55FF55;">SaveBackground&amp;</span> = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(<span style="color:#F580B1;">0</span>)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">RestoreBackground</span> (Image <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , Image, <span style="color:#F580B1;">0</span>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Turning off blending to create transparency.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
alphaSprite&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">64</span>, <span style="color:#F580B1;">64</span>, <span style="color:#F580B1;">32</span>)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_DONTBLEND</span></a> alphaSprite&amp; <span style="color:#919191;">' turn off alpha-blending</span>
<span style="color:#919191;">'Create a simple sprite with transparency</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> alphaSprite&amp;
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">63</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">63</span>
        alpha = <a href="SQR" title="SQR"><span style="color:#4593D8;">SQR</span></a>((x - <span style="color:#F580B1;">32</span>) ^ <span style="color:#F580B1;">2</span> + (y - <span style="color:#F580B1;">32</span>) ^ <span style="color:#F580B1;">2</span>) / <span style="color:#F580B1;">32</span>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> alpha &lt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> alpha = <span style="color:#F580B1;">0</span>
        alpha = (<span style="color:#F580B1;">1</span> - alpha * alpha) <span style="color:#919191;">'parabolic curve</span>
        <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (x, y), <a href="RGBA32" title="RGBA32"><span style="color:#4593D8;">_RGBA32</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">255</span>, alpha * <span style="color:#F580B1;">255</span>)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<span style="color:#919191;">'Make a simple background texture</span>
<a href="DEST" title="DEST"><span style="color:#4593D8;">_DEST</span></a> <span style="color:#F580B1;">0</span>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">479</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">639</span>
        <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (x, y), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(x <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">255</span>, y <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">255</span>, (x <a class="mw-redirect" href="XOR" title="XOR"><span style="color:#4593D8;">XOR</span></a> y) <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">255</span>)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<span style="color:#919191;">'Store background so we can show moveable objects on it</span>
background&amp; = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(<span style="color:#F580B1;">0</span>)
<span style="color:#919191;">'Treat my alpha values as transparency</span>
<a href="BLEND" title="BLEND"><span style="color:#4593D8;">_BLEND</span></a> alphaSprite&amp;
ph = <span style="color:#F580B1;">0</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">60</span>
    x = <span style="color:#F580B1;">320</span> - <span style="color:#F580B1;">250</span> * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(ph) - (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(alphaSprite&amp;) \ <span style="color:#F580B1;">2</span>)
    y = <span style="color:#F580B1;">240</span> - <span style="color:#F580B1;">150</span> * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(ph * <span style="color:#F580B1;">1.3</span>) - (<a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(alphaSprite&amp;) \ <span style="color:#F580B1;">2</span>)
    ph = ph + <span style="color:#F580B1;">0.03</span>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> , background&amp;, <span style="color:#F580B1;">0</span>
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (x, y), alphaSprite&amp;, <span style="color:#F580B1;">0</span>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>)
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> To make the alpha image, turn alpha blending off. Otherwise PSET blends the pixel to instead of making the sprite transparent.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BLEND" title="BLEND">_BLEND</a></li>
<li><a href="BLEND_(function)" title="BLEND (function)">_BLEND (function)</a></li>
<li><a href="Images" title="Images">Images</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714130832
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.060 seconds
Real time usage: 0.070 seconds
Preprocessor visited node count: 991/1000000
Post‐expand include size: 7153/2097152 bytes
Template argument size: 1732/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 361/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.391      1 -total
 12.97%    4.071     61 Template:Cl
 12.32%    3.869     70 Template:Text
  6.93%    2.175      1 Template:PageSyntax
  6.80%    2.134      1 Template:Small
  5.52%    1.734      1 Template:PageSeeAlso
  5.49%    1.722      1 Template:PageNavigation
  5.25%    1.648      3 Template:Parameter
  4.91%    1.540      1 Template:PageParameters
  4.72%    1.483      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:126-0!canonical and timestamp 20240714130832 and revision id 8315.
 -->
</div>
</div>
</div>
</div>
</body>
</html>