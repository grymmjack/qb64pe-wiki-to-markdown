<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DEF SEG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEF_SEG rootpage-DEF_SEG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DEF SEG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">DEF SEG</a> is used to define the area in memory to access QB64's emulated conventional memory.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">DEF SEG</a> [=][{segment|VARSEG(variable}]</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li><b>QB64 implements memory access using <a href="MEM" title="MEM">_MEM</a> and related functions. For that reason, <a class="mw-selflink selflink">DEF SEG</a> isn't recommended practice anymore and is supported to maintain compatibility with legacy code.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used to set the pointer to a memory area of a variable/array or register.</li>
<li><a href="PEEK" title="PEEK">PEEK</a> and <a href="POKE" title="POKE">POKE</a> require a segment memory address (often just 0) without using VARSEG.</li>
<li>Important segments using <a href="PEEK" title="PEEK">PEEK</a> and <a href="POKE" title="POKE">POKE</a> include &amp;HB800 (text segment) and &amp;HA000 (graphics segment).</li>
<li><a href="BSAVE" title="BSAVE">BSAVE</a> and <a href="BLOAD" title="BLOAD">BLOAD</a> require a VARSEG reference to the grahic array(0 index) used.</li>
<li>Always use DEF SEG when the procedure is completed, in order to reset the segment to QBasic's default value.</li>
<li><a class="mw-selflink selflink">DEF SEG</a>, <a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a>, <a href="PEEK" title="PEEK">PEEK</a> and <a href="POKE" title="POKE">POKE</a> access QB64's emulated 16 bit conventional memory block. <b>It is highly recommended to use QB64's <a href="MEM" title="MEM">_MEM</a> memory system to avoid running out of memory.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEF_SEG_%3D_0" title="DEF SEG = 0">DEF SEG = 0</a></li>
<li><a href="VARPTR" title="VARPTR">VARPTR</a>, <a href="VARSEG" title="VARSEG">VARSEG</a></li>
<li><a href="PEEK" title="PEEK">PEEK</a>, <a href="POKE" title="POKE">POKE</a></li>
<li><a href="BSAVE" title="BSAVE">BSAVE</a>, <a href="BLOAD" title="BLOAD">BLOAD</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061252
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.016 seconds
Real time usage: 0.020 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    8.457      1 -total
 27.06%    2.288      1 Template:PageSyntax
 25.09%    2.122      1 Template:PageDescription
 21.94%    1.856      1 Template:PageSeeAlso
 21.82%    1.845      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:452-0!canonical and timestamp 20240715061252 and revision id 7261.
 -->
</div>
</div>
</div>
</div>
</body>
</html>