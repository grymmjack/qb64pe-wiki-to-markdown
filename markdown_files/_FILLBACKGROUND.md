<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PRINTMODE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRINTMODE rootpage-PRINTMODE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PRINTMODE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PRINTMODE</a> statement sets the text or <a href="FONT" title="FONT">_FONT</a> printing mode on an image when using <a href="PRINT" title="PRINT">PRINT</a> or <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_PRINTMODE</a> {<i>_KEEPBACKGROUND</i>|<i>_ONLYBACKGROUND</i>|<i>_FILLBACKGROUND</i>}[, <i>imageHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>One of 3 mode keywords is mandatory when using this statement to deal with the text background.
<ul><li><i>_KEEPBACKGROUND</i> (mode 1): Text background transparent. Only the text is displayed over anything behind it.</li>
<li><i>_ONLYBACKGROUND</i> (mode 2): Text background only is displayed. Text is transparent to anything behind it.</li>
<li><i>_FILLBACKGROUND</i> (mode 3): Text and background block anything behind them like a normal <a href="PRINT" title="PRINT">PRINT</a>. <b>Default setting.</b></li></ul></li>
<li>If the optional <i>imageHandle&amp;</i> is omitted or is 0 then the setting will be applied to the current <a href="DEST" title="DEST">destination</a> image.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use the <a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a> to find the current <a class="mw-selflink selflink">_PRINTMODE</a> setting mode number for an image.</li>
<li><b>The _PRINTMODE statement and function can only be used on graphic images, not text-based ones such as SCREEN 0</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Using _PRINTMODE with <a href="PRINT" title="PRINT">PRINT</a> in a graphic screen mode. The background used is CHR$(219) = █
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 8: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(3, 219) 'background
<a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTMODE</span></a> _KEEPBACKGROUND
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRINTMODE</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINTMODE_(function)" title="PRINTMODE (function)">_PRINTMODE (function)</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a></li>
<li><a href="NEWIMAGE" title="NEWIMAGE">_NEWIMAGE</a></li>
<li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_USING" title="PRINT USING">_PRINT USING</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035801
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 109/1000000
Post‐expand include size: 1308/2097152 bytes
Template argument size: 160/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.316      1 -total
 12.78%    2.341      1 Template:PageSyntax
 10.76%    1.971      2 Template:Parameter
 10.57%    1.936     11 Template:Cl
  8.85%    1.621      1 Template:CodeStart
  8.60%    1.575      1 Template:PageParameters
  8.51%    1.559      1 Template:PageDescription
  8.42%    1.543      1 Template:PageNavigation
  8.37%    1.533      1 Template:CodeEnd
  8.05%    1.474      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:251-0!canonical and timestamp 20240715035801 and revision id 6688.
 -->
</div>
</div>
</div>
</div>
</body>
</html>