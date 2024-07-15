<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>WINDOW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WINDOW rootpage-WINDOW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">WINDOW</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>WINDOW</b> command scales the graphics coordinate system of the current <a href="DEST" title="DEST">_DEST</a> image, optionally inverting the direction of the vertical axis. Any coordinates used in drawing commands made to the image are scaled such that the image seems have have the dimensions requested.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>WINDOW</b> [ [ <b>SCREEN</b>] (<i>x1!</i>, <i>y1!</i>) - (<i>x2!</i>, <i>y2!</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<p>Where (<i>x1!</i>, <i>y1!</i>)-(<i>x2!</i>, <i>y2!</i>) specifies the new dimensions of the image to scale to. Non-integer values may be used.
Using <b>WINDOW</b> with no parameters reverts the effect of any previous calls to it.
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<p>When a command such as <a href="LINE" title="LINE">LINE</a>, <a href="CIRCLE" title="CIRCLE">CIRCLE</a> or <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a> needs a position in an image specified, it is given as a combination of x (horizontal) and y (vertical) coordinates. Usually these values are measured as pixels from the top-left origin. The <b>WINDOW</b> command changes the way these values are measured. This is best illustrated with an example:
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"><a href="SCREEN" title="SCREEN"><span style="color:blue;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:blue;">_NEWIMAGE</span></a>(600, 600, 32) '600 pixels in x and y directions and displayed on screen
<a class="mw-selflink selflink"><span style="color:blue;">WINDOW</span></a> <a href="SCREEN" title="SCREEN"><span style="color:blue;">SCREEN</span></a> (0, 0)-(6, 6)
</pre>
</td></tr></tbody></table>
<p>The coordinates of the image now run from 0 to 6 in both the x and y directions. The centre of the screen is now referred to as (3, 3) and the bottom-right corner of the screen is (6, 6). The image has not actually just changed size or the number of pixels, just the way the program refers to positions on the image. Despite this example, there is no requirement for the image or scaling coordinates to be square; each direction is scaled independently, and can result in commands such as LINE (0, 0)-(10, 10), , BF drawing a rectangle instead of a square.
If the <b>SCREEN</b> part is omitted, the y axis is inverted. Thus the origin is now at the bottom-left, and y coordinates increase as you move up the screen. Such a system may be more familiar to mathematically-oriented programmers.
<b>WINDOW</b> does not change any of the content already on the image; it only modifies coordinates used while it is in effect. The scaling is relative to the original image, so successive invocations do not compound upon each other.
Although <b>WINDOW</b> affects all coordinates, it does not affect all graphics operations entirely. <a href="PUTIMAGE" title="PUTIMAGE">_PUTIMAGE</a>, if only given one destination coordinate, will not scale or stretch the image being drawn. <a href="CIRCLE" title="CIRCLE">CIRCLE</a> will scale its radius such that it matches the horizontal axis. This means it always draws perfect circles even if the scaling of the two axes are not the same, but the radius measured against the vertical scale may not be correct.
The location of the graphics cursor (used to calculate relative positions for STEP) is not affected. It will remain in the same position on the image, but the relative coordinates that are specified with STEP will be scaled as described above.
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p>Demonstrate a circle's radius only matching the scaling in the horizontal direction by comparing against a box:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32) 'Not a square image
<a class="mw-selflink selflink"><span style="color:#4593D8;">WINDOW</span></a> <a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> (0, 0)-(10, 10) 'SCREEN keeps the axis direction the same
<a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (4, 4)-(6, 6), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(255, 0, 0), BF 'Red square centred on (5, 5); will be stretched into a rectangle
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (5, 5), 1, <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(0, 255, 0) 'Green circle at (5, 5) with radius 1
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PMAP" title="PMAP">PMAP</a></li>
<li><a href="VIEW" title="VIEW">VIEW</a></li>
<li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062232
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 112/1000000
Post‐expand include size: 1391/2097152 bytes
Template argument size: 152/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.242      1 -total
 11.62%    3.745      1 Template:PageExamples
 10.00%    3.223      4 Template:Cb
  8.36%    2.697      8 Template:Cl
  7.96%    2.567      1 Template:PageSyntax
  7.41%    2.388      1 Template:TextEnd
  7.03%    2.268      1 Template:CodeStart
  6.87%    2.216      1 Template:PageParameters
  6.79%    2.189      1 Template:CodeEnd
  6.79%    2.188      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:461-0!canonical and timestamp 20240715062232 and revision id 7470.
 -->
</div>
</div>
</div>
</div>
</body>
</html>