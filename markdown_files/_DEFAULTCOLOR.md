<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEFAULTCOLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEFAULTCOLOR rootpage-DEFAULTCOLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEFAULTCOLOR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_DEFAULTCOLOR</b> function returns the current default (text/drawing) color for an image handle or page.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>col~&amp;</i> = <a class="mw-selflink selflink">_DEFAULTCOLOR</a> [(<i>imageHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current write page or image designated by <a href="DEST" title="DEST">_DEST</a>.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">Invalid handle</a> error occurs. Check handle values first. Zero designates the current screen.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use it to get the current default (foreground) color to restore it later in a program.</li>
<li>In legacy <a href="SCREEN" title="SCREEN">SCREEN</a> modes and in <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 256 colors mode the color attribute/palette index is returned.</li>
<li>In <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 32-bit mode the <a href="RGBA32" title="RGBA32">_RGBA32</a> value (<b>&amp;H00<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b>) is returend, make sure to store it in an <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> variable (as seen in the syntax above with the <b>~&amp;</b> suffix), otherwise the blue component may be lost.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Storing the default color for later use. The default color is the color set as foreground.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">0</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">7</span> <span style="color:#919191;">'set color 4 as foreground, color 7 as background</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
col~&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEFAULTCOLOR</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> col~&amp;
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt7"><span style="color:#aa0000;">4</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BACKGROUNDCOLOR" title="BACKGROUNDCOLOR">_BACKGROUNDCOLOR</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="DEST" title="DEST">_DEST</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="Windows_Libraries#Color_Dialog_Box" title="Windows Libraries">Color Dialog Box</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062314
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 160/1000000
Post‐expand include size: 1514/2097152 bytes
Template argument size: 214/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 49/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.874      1 -total
  9.72%    3.000     11 Template:Text
  9.48%    2.928      1 Template:PageSyntax
  8.89%    2.746      4 Template:Parameter
  8.01%    2.474      1 Template:PageDescription
  7.79%    2.404      1 Template:PageParameters
  7.09%    2.190      1 Template:OutputStartBG7
  6.28%    1.939      1 Template:PageExamples
  6.26%    1.933      5 Template:Cl
  5.94%    1.835      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:109-0!canonical and timestamp 20240715062314 and revision id 8302.
 -->
</div>
</div>
</div>
</div>
</body>
</html>