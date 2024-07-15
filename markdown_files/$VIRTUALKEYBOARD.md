<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$VIRTUALKEYBOARD - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_VIRTUALKEYBOARD rootpage-_VIRTUALKEYBOARD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$VIRTUALKEYBOARD</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The (<span style="color:red;">now deprecated</span>) <b>$VIRTUALKEYBOARD</b> <a href="Metacommand" title="Metacommand">metacommand</a> did turn the virtual keyboard ON or OFF.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>$VIRTUALKEYBOARD:ON</b></dd>
<dd><b>$VIRTUALKEYBOARD:OFF</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>This metacommand did not require a comment <i><a href="Apostrophe" title="Apostrophe">'</a></i> or <a href="REM" title="REM">REM</a> before it. There was no space between the metacommand name, the colon and the ON/OFF parameter.</li>
<li>It placed a virtual keyboard on screen, which could be used in touch-enabled devices like Windows tablets.</li>
<li><span style="color:red;">Deprecated</span>, in all current versions of QB64 it just generates a warning now, but has no other effect anymore.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">$VIRTUALKEYBOARD:ON</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211006
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 76/1000000
Post‐expand include size: 1061/2097152 bytes
Template argument size: 107/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.990      1 -total
 14.32%    3.005      2 Template:Text
 11.93%    2.505      1 Template:PageSyntax
 10.31%    2.164      1 Template:CodeEnd
  9.99%    2.096      1 Template:PageExamples
  9.83%    2.063      6 Template:Cl
  9.77%    2.051      1 Template:CodeStart
  9.66%    2.027      1 Template:PageSeeAlso
  9.39%    1.972      1 Template:PageDescription
  8.73%    1.833      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:362-0!canonical and timestamp 20240714211006 and revision id 5853.
 -->
</div>
</div>
</div>
</div>
</body>
</html>