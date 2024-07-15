<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SCREENMOVE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SCREENMOVE rootpage-SCREENMOVE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SCREENMOVE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SCREENMOVE</a> statement positions the program window on the desktop using designated coordinates.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SCREENMOVE</a> {<i>column&amp;</i>, <i>row&amp;</i>|_MIDDLE}</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Positions the program window on the desktop using the <i>column&amp;</i> and <i>row&amp;</i> pixel coordinates for the upper left corner.</li>
<li><b>_MIDDLE</b> can be used instead to automatically center the program window on the desktop, in any screen resolution.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The program's <a href="SCREEN" title="SCREEN">SCREEN</a> dimensions may influence the desktop position that can be used to keep the entire window on the screen.</li>
<li>Use <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a> and <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a> to find the current desktop resolution to place the program's window.</li>
<li>On dual monitors a negative <i>column&amp;</i> position or a value greater than the main screen width can be used to position a window in another monitor.</li>
<li><b>A small delay may be necessary when a program first starts up to properly orient the screen on the desktop properly.</b> See <a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a>.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.926"><img alt="v0.926" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.926</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="no"><img alt="no" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>no</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Calculating the border and header offsets by comparing a coordinate move with _MIDDLE by using trial and error.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">userwidth&amp; = <a href="DESKTOPWIDTH" title="DESKTOPWIDTH"><span style="color:#4593D8;">_DESKTOPWIDTH</span></a>: userheight&amp; = <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT"><span style="color:#4593D8;">_DESKTOPHEIGHT</span></a> 'get current screen resolution
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(800, 600, 256)
scrnwidth&amp; = <a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">_WIDTH</span></a>: scrnheight&amp; = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>  'get the dimensions of the program screen
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENMOVE</span></a> (userwidth&amp; \ 2 - scrnwidth&amp; \ 2) - 3, (userheight&amp; \ 2 - scrnheight&amp; \ 2) - 29
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 4
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENMOVE</span></a> _MIDDLE  'check centering
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>When positioning the window, offset the position by -3 columns and - 29 rows to calculate the top left corner coordinate.</dd></dl>
<p>
<i>Example 2:</i> Moving a program window to a second monitor positioned to the right of the main desktop.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">wide&amp; = <a href="DESKTOPWIDTH" title="DESKTOPWIDTH"><span style="color:#4593D8;">_DESKTOPWIDTH</span></a>
high&amp; = <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT"><span style="color:#4593D8;">_DESKTOPHEIGHT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> wide&amp;; "X"; high&amp;
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 4
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENMOVE</span></a> wide&amp; + 200, 200 'positive value for right monitor 2
img2&amp; = <a href="SCREENIMAGE" title="SCREENIMAGE"><span style="color:#4593D8;">_SCREENIMAGE</span></a>
wide2&amp; = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(img2&amp;)
high2&amp; = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(img2&amp;)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> wide2&amp;; "X"; high2&amp;
<a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> 4
<a class="mw-selflink selflink"><span style="color:#4593D8;">_SCREENMOVE</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_MIDDLE</span></a> 'moves program back to main monitor 1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> Change the <a class="mw-selflink selflink">_SCREENMOVE</a> column to negative for a left monitor.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREENX" title="SCREENX">_SCREENX</a>, <a href="SCREENY" title="SCREENY">_SCREENY</a></li>
<li><a href="SCREENIMAGE" title="SCREENIMAGE">_SCREENIMAGE</a>, <a href="DESKTOPWIDTH" title="DESKTOPWIDTH">_DESKTOPWIDTH</a>, <a href="DESKTOPHEIGHT" title="DESKTOPHEIGHT">_DESKTOPHEIGHT</a></li>
<li><a href="SCREENPRINT" title="SCREENPRINT">_SCREENPRINT</a></li>
<li><a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192814
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 212/1000000
Post‐expand include size: 2142/2097152 bytes
Template argument size: 422/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2362/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   45.144      1 -total
  6.46%    2.916      1 Template:PageSyntax
  5.91%    2.670     22 Template:Cl
  5.64%    2.544      5 Template:Parameter
  5.39%    2.434      1 Template:PageParameters
  4.93%    2.225      1 Template:PageDescription
  4.66%    2.102      1 Template:PageExamples
  4.55%    2.054      1 Template:PageAvailability
  4.45%    2.008      2 Template:CodeStart
  3.97%    1.793      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:186-0!canonical and timestamp 20240714192813 and revision id 7748.
 -->
</div>
</div>
</div>
</div>
</body>
</html>