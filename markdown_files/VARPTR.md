<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>VARPTR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-VARPTR rootpage-VARPTR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">VARPTR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>VARPTR</b> function returns an <a href="INTEGER" title="INTEGER">INTEGER</a> value that is the offset part of the variable or array memory address within it's segment.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>offset% = VARPTR(variable_name[(reference_index%)])</dd></dl></dd></dl>
<p>
</p>
<ul><li>If variablename is not defined before VARPTR or <a href="VARSEG" title="VARSEG">VARSEG</a> is called, the variable is created and it's address is returned.</li>
<li>Reference index is used to set the offset address of an array index, not necessarily the lowest index.</li>
<li>When a string variable, VARPTR returns the offset address location of the first byte of the string.</li>
<li>Because many QBasic statements change the locations of variables in memory, use the values returned by VARPTR and VARSEG immediately after the functions are used!</li>
<li>Integer array sizes are limited to 32767 elements when using <a class="mw-selflink selflink">VARPTR</a> in QB and <b>QB64</b>!. Create a larger array using <a href="BYTE" title="BYTE">_BYTE</a>. Example: <a href="DIM" title="DIM">DIM</a> <a href="SHARED" title="SHARED">SHARED</a> Memory (65535) AS <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><b>Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!</b></li></ul>
<dl><dd><b>It is highly recommended that QB64's <a href="MEM" title="MEM">_MEM</a> memory system be used to avoid running out of memory.</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BSAVE" title="BSAVE">BSAVE</a>, <a href="BLOAD" title="BLOAD">BLOAD</a></li>
<li><a href="SADD" title="SADD">SADD</a>,  <a href="DEF_SEG" title="DEF SEG">DEF SEG</a></li>
<li><a href="VARPTR$" title="VARPTR$">VARPTR$</a>, <a href="VARSEG" title="VARSEG">VARSEG</a></li>
<li><a href="POKE" title="POKE">POKE</a>, <a href="PEEK" title="PEEK">PEEK</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062227
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.012 seconds
Real time usage: 0.016 seconds
Preprocessor visited node count: 9/1000000
Post‐expand include size: 505/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    6.247      1 -total
 35.35%    2.208      1 Template:PageSyntax
 30.03%    1.876      1 Template:PageSeeAlso
 29.50%    1.843      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:496-0!canonical and timestamp 20240715062227 and revision id 7705.
 -->
</div>
</div>
</div>
</div>
</body>
</html>