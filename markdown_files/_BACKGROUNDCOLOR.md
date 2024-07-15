<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BACKGROUNDCOLOR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BACKGROUNDCOLOR rootpage-BACKGROUNDCOLOR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BACKGROUNDCOLOR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_BACKGROUNDCOLOR</b> function returns the current background color for an image handle or page.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>col~&amp;</i> = <a class="mw-selflink selflink">_BACKGROUNDCOLOR</a> [(<i>imageHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>If <i>imageHandle&amp;</i> is omitted, it is assumed to be the current write page or image designated by <a href="DEST" title="DEST">_DEST</a>.</li>
<li>If <i>imageHandle&amp;</i> is an invalid handle, an <a href="ERROR_Codes" title="ERROR Codes">Invalid handle</a> error occurs. Check handle values first. Zero designates the current screen.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use it to get the current background color to restore it later in a program.</li>
<li>In legacy <a href="SCREEN" title="SCREEN">SCREEN</a> modes and in <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 256 colors mode the color attribute/palette index is returned.</li>
<li>In <a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a> 32-bit mode the <a href="RGBA32" title="RGBA32">_RGBA32</a> value (<b>&amp;H00<span style="color:red;">00</span><span style="color:green;">00</span><span style="color:blue;">00</span></b> to <b>&amp;HFF<span style="color:red;">FF</span><span style="color:green;">FF</span><span style="color:blue;">FF</span></b>) is returend, make sure to store it in an <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> variable (as seen in the syntax above with the <b>~&amp;</b> suffix), otherwise the blue component may be lost.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Storing the background color for later use.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">0</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">3</span> <span style="color:#919191;">'set color 1 as foreground, color 3 as background</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
col~&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_BACKGROUNDCOLOR</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> col~&amp;
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt3"><span style="color:#0000aa;">3</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEFAULTCOLOR" title="DEFAULTCOLOR">_DEFAULTCOLOR</a></li>
<li><a href="COLOR" title="COLOR">COLOR</a>, <a href="DEST" title="DEST">_DEST</a></li>
<li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="SCREEN_(function)" title="SCREEN (function)">SCREEN (function)</a></li>
<li><a href="Windows_Libraries#Color_Dialog_Box" title="Windows Libraries">Color Dialog Box</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062246
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.073 seconds
Preprocessor visited node count: 160/1000000
Post‐expand include size: 1520/2097152 bytes
Template argument size: 220/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 49/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   48.901      1 -total
 17.48%    8.548      1 Template:OutputEnd
 10.35%    5.062      5 Template:Cl
  8.68%    4.247      1 Template:OutputStartBG3
  6.30%    3.080      1 Template:PageSyntax
  6.07%    2.966      1 Template:PageSeeAlso
  6.01%    2.940     11 Template:Text
  5.82%    2.844      1 Template:PageNavigation
  5.37%    2.625      1 Template:PageParameters
  5.34%    2.611      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:52-0!canonical and timestamp 20240715062246 and revision id 8264.
 -->
</div>
</div>
</div>
</div>
</body>
</html>