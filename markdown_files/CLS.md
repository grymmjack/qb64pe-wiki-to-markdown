<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CLS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLS rootpage-CLS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CLS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>CLS</b> statement clears the <a href="DEST" title="DEST">current write page</a> or the designated image.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CLS</a> [<i>method%</i>] [, <i>bgColor&amp;</i>] [, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>method%</i> specifies which parts of the page to clear, and can have one of the following values:
<ul><li><b>CLS</b>    - clears the active graphics or text viewport or the entire text screen and refreshes bottom function <a href="KEY_LIST" title="KEY LIST">KEY ON</a> line.</li>
<li><b>CLS</b> 0 - Clears the entire page of text and graphics. Print cursor is moved to row 1 at column 1.</li>
<li><b>CLS</b> 1 - Clears only the graphics view port. Has no effect for text mode.</li>
<li><b>CLS</b> 2 - Clears only the text view port. The print cursor is moved to the top row of the text view port at column 1.</li></ul></li>
<li>The <i>bgColor&amp;</i> specifies the color attribute or palette index to use when clearing the screen in <b>QB64</b>.</li>
<li><i>imageHandle&amp;</i> specifies an image handle to clear. If it is not specified, then <b>CLS</b> clears the <a href="DEST" title="DEST">current write page</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In legacy <a href="SCREEN" title="SCREEN">SCREEN</a> modes <i>bgColor&amp;</i> specifies the color attribute of the background.</li>
<li>For 32-bit graphics mode, <i>bgColor&amp;</i> specifies the <a href="RGB32" title="RGB32">_RGB32</a> or <a href="RGBA32" title="RGBA32">_RGBA32</a> color to use.</li>
<li><b>32-bit screen surface backgrounds (black) have zero <a href="ALPHA" title="ALPHA">_ALPHA</a> so that they are transparent when placed over other surfaces.</b>
<ul><li>Use <b>CLS</b> or <a href="DONTBLEND" title="DONTBLEND">_DONTBLEND</a> to make a new surface background <a href="ALPHA" title="ALPHA">_ALPHA</a> 255 or opaque.</li></ul></li>
<li>If not specified, <i>bgColor&amp;</i> is assumed to be the current background color. 32-bit backgrounds will change to opaque.</li>
<li>If <i>bgColor&amp;</i> is not a valid attribute, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li>Use <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a> to allow the background colors to be visible through the text or the text background.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.610"><img alt="v0.610" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.610</b>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
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
<ul><li>In <b>QB64-PE v3.10.0</b> support for clearing images was added.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Printing black text on a white background in QB64.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a class="mw-selflink selflink"><span style="color:#4593D8;">CLS</span></a> , 15
<a href="PRINTMODE" title="PRINTMODE"><span style="color:#4593D8;">_PRINTMODE </span></a> _KEEPBACKGROUND        'keeps the text background visible
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This is black text on a white background!"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="PRINTMODE" title="PRINTMODE">_PRINTMODE</a> can be used with <a href="PRINT" title="PRINT">PRINT</a> or <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> to make the text or the text background transparent.</dd></dl>
<p>
<i>Example 2:</i> You don't need to do anything special to use a .PNG image with alpha/transparency. Here's a simple example:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a class="mw-selflink selflink"><span style="color:#4593D8;">CLS</span></a> , <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 255, 0)
i = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<b>"qb64_trans.png"</b>) 'see note below examples to get the image
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0), i 'places image at upper left corner of window w/o stretching it
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When QB64 loads a .PNG file containing a transparent color, that color will be properly treated as transparent when _PUTIMAGE is used to put it onto another image. You can use a .PNG file containing transparency information in a 256-color screen mode in QB64. <a class="mw-selflink selflink">CLS</a> sets the <a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a> setting using <a href="RGB" title="RGB">_RGB</a>.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="RGB" title="RGB">_RGB</a>, <a href="RGBA" title="RGBA">_RGBA</a>, <a href="RGB32" title="RGB32">_RGB32</a>, <a href="RGBA32" title="RGBA32">_RGBA32</a></li>
<li><a href="VIEW_PRINT" title="VIEW PRINT">VIEW PRINT</a>, <a href="VIEW" title="VIEW">VIEW</a></li>
<li><a href="CLEARCOLOR" title="CLEARCOLOR">_CLEARCOLOR</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035405
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.071 seconds
Real time usage: 0.097 seconds
Preprocessor visited node count: 161/1000000
Post‐expand include size: 1570/2097152 bytes
Template argument size: 240/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2365/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   82.122      1 -total
  4.01%    3.292     10 Template:Parameter
  3.68%    3.019      1 Template:PageExamples
  3.54%    2.908     12 Template:Cl
  3.49%    2.863      1 Template:PageSyntax
  3.43%    2.818      1 Template:PageParameters
  2.88%    2.368      2 Template:CodeStart
  2.83%    2.328      1 Template:PageDescription
  2.83%    2.328      1 Template:PageAvailability
  2.64%    2.164      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:415-0!canonical and timestamp 20240715035405 and revision id 8603.
 -->
</div>
</div>
</div>
</div>
</body>
</html>