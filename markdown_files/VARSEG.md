<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>VARSEG - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-VARSEG rootpage-VARSEG skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">VARSEG</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>VARSEG</b> function returns an <a href="INTEGER" title="INTEGER">INTEGER</a> value that is the segment part of a variable or array memory address.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><a href="DEF_SEG" title="DEF SEG">DEF SEG</a> = VARSEG(variable_name[(start_index)])</dd></dl></dd></dl>
<p>
</p>
<ul><li>If variablename is not defined before <a href="VARPTR" title="VARPTR">VARPTR</a> or VARSEG is called, the variable is created and its address is returned.</li>
<li>The start index is the lowest index of an array variable when used.</li>
<li>When a string variable, VARSEG returns the segment location address of the first byte of the string.</li>
<li>Because many QBasic statements change the locations of variables in memory, use the values returned by VARPTR and VARSEG immediately after the functions are used!</li>
<li>Integer array sizes are limited to 32767 elements when using <a class="mw-selflink selflink">VARSEG</a> in QB and <b>QB64</b>!. Create a larger array using <a href="BYTE" title="BYTE">_BYTE</a>. Example: <a href="DIM" title="DIM">DIM</a> <a href="SHARED" title="SHARED">SHARED</a> Memory (65535) AS <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><b>Warning: DEF SEG, VARSEG , VARPTR, PEEK or POKE access QB64's emulated 16 bit conventional memory block!</b></li></ul>
<dl><dd><b>It is highly recommended that QB64's <a href="MEM" title="MEM">_MEM</a> memory system be used to avoid running out of memory.</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BSAVE" title="BSAVE">BSAVE</a>, <a href="BLOAD" title="BLOAD">BLOAD</a></li>
<li><a href="SADD" title="SADD">SADD</a>, <a href="DEF_SEG" title="DEF SEG">DEF SEG</a></li>
<li><a href="VARPTR" title="VARPTR">VARPTR</a>, <a href="VARPTR$" title="VARPTR$">VARPTR$</a></li>
<li><a href="POKE" title="POKE">POKE</a>, <a href="PEEK" title="PEEK">PEEK</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062229
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.013 seconds
Real time usage: 0.028 seconds
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
100.00%   12.978      1 -total
 46.93%    6.090      1 Template:PageNavigation
 29.02%    3.766      1 Template:PageSeeAlso
 18.60%    2.414      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:499-0!canonical and timestamp 20240715062229 and revision id 7465.
 -->
</div>
</div>
</div>
</div>
</body>
</html>