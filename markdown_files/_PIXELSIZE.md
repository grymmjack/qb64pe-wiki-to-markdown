<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PIXELSIZE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PIXELSIZE rootpage-PIXELSIZE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PIXELSIZE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PIXELSIZE</a> function returns the color depth (Bits Per Pixel) of an image as 0 for text, 1 for 1 to 8 BPP or 4 for 32 bit.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pixelSize%</i> = <a class="mw-selflink selflink">_PIXELSIZE</a>[(<i>imageHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current write page.</li>
<li>Returns:
<ul><li>0 if the image or screen page specified by <i>imageHandle&amp;</i> is in text mode.</li>
<li>1 if the image specified by <i>imageHandle&amp;</i> is in 1 (B &amp; W), 4 (16 colors) or 8 (256 colors) BPP mode.</li>
<li>4 if the image specified is a 24/32-bit compatible mode. Pixels use three bytes, one per red, green and blue color intensity.</li></ul></li>
<li>The <a href="SCREEN" title="SCREEN">SCREEN</a> or <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> or <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a> color mode (256 or 32) can influence the pixel sizes that can be returned.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, then an <a href="ERROR_Codes" title="ERROR Codes">invalid handle</a> error occurs.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Snippet:</i> Saving Images for later program use. Handle values could be saved to an array.
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">
handle1&amp; = _Getimage(sx1, sy1, sx2, sy2, sourcehandle&amp;) ' function call
<a href="FUNCTION" title="FUNCTION"><span style="color:blue;">FUNCTION</span></a> GetImage&amp; (sx1, sy1, sx2, sy2, sourcehandle&amp;)
bytespp = <a class="mw-selflink selflink"><span style="color:blue;">_PIXELSIZE</span></a>(sourcehandle&amp;)
<a href="IF...THEN" title="IF...THEN"><span style="color:blue;">IF</span></a> bytespp = 4 <a href="THEN" title="THEN"><span style="color:blue;">THEN</span></a> Pal = 32 <a href="ELSE" title="ELSE"><span style="color:blue;">ELSE</span></a> <a href="IF...THEN" title="IF...THEN"><span style="color:blue;">IF</span></a> bytespp = 1 <a href="THEN" title="THEN"><span style="color:blue;">THEN</span></a> Pal = 256 <a href="ELSE" title="ELSE"><span style="color:blue;">ELSE</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:blue;">EXIT FUNCTION</span></a>
h&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:blue;">_NEWIMAGE</span></a>(<a href="ABS" title="ABS"><span style="color:blue;">ABS</span></a>(sx2 - sx1) + 1, <a href="ABS" title="ABS"><span style="color:blue;">ABS</span></a>(sy2 - sy1) + 1, Pal)
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:blue;">_PUTIMAGE</span></a> (0, 0), sourcehandle&amp;, h&amp;, (sx1, sy1)-(sx2, sy2) 'image is not displayed
GetImage&amp; = h&amp;
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:blue;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li>
<li><a href="ThirtyTwoBit_SUB" title="ThirtyTwoBit SUB">ThirtyTwoBit SUB</a></li>
<li><a href="Bitmaps" title="Bitmaps">Bitmaps</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1362" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SAVEIMAGE" title="SAVEIMAGE">_SAVEIMAGE</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a></li>
<li><a href="COPYPALETTE" title="COPYPALETTE">_COPYPALETTE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062423
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 209/1000000
Post‐expand include size: 1615/2097152 bytes
Template argument size: 286/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.150      1 -total
 21.85%    4.402      1 Template:PageSyntax
 11.67%    2.351      6 Template:Parameter
  9.33%    1.881     14 Template:Cb
  7.61%    1.533      1 Template:TextStart
  7.46%    1.503      1 Template:PageDescription
  7.12%    1.435      1 Template:TextEnd
  6.91%    1.393      1 Template:PageExamples
  6.88%    1.386      1 Template:PageNavigation
  6.80%    1.370      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:246-0!canonical and timestamp 20240715062423 and revision id 8935.
 -->
</div>
</div>
</div>
</div>
</body>
</html>