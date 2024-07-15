<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>BLOAD - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BLOAD rootpage-BLOAD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">BLOAD</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">BLOAD</a> loads a binary graphics file created by <a href="BSAVE" title="BSAVE">BSAVE</a> to an array.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">BLOAD</a> <i>fileName$</i>, <a href="VARPTR" title="VARPTR">VARPTR</a>(<i>imageArray%(</i>index<i>)</i>)</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li><b>QB64</b> can load larger arrays directly from binary files using <a href="PUT" title="PUT">PUT</a> # and <a href="GET" title="GET">GET</a> # without <b>BLOAD</b>. For that reason, <b>BLOAD</b> isn't recommended practice anymore and is supported to maintain compatibility with legacy code.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fileName$</i> is the name of the file that the image should be <a href="BSAVE" title="BSAVE">BSAVEd</a> to.</li>
<li><i>imageArray%(index)</i> is the <a href="INTEGER" title="INTEGER">INTEGER</a> <a href="Arrays" title="Arrays">array</a> start index to store the image loaded.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>There must be an <a href="INTEGER" title="INTEGER">INTEGER</a> array of adequate size (up to 26K) to hold the graphic data.</li>
<li>A <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> pointing to the array is required. <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> = <a href="VARSEG" title="VARSEG">VARSEG</a>(imageArray%(index))</li>
<li><i>index</i> is the starting image element of the Array. Can also include RGB color settings at the start index.</li>
<li>Fullscreen images in <a href="SCREEN" title="SCREEN">SCREEN</a> 12 require 3 file BLOADs. A 26K array can hold 1/3 of screen.</li>
<li>Custom RGB color settings can be embedded(indexed) at the start of the image array.</li>
<li>BLOAD can be used to load any array that was saved with <a href="BSAVE" title="BSAVE">BSAVE</a>, not just graphics.</li>
<li>Array sizes are limited to 32767 Integer elements due to use of <a href="VARPTR" title="VARPTR">VARPTR</a> in QBasic and <b>QB64'</b>s emulated conventional memory.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Loading data to an array from a BSAVED file.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="VARSEG" title="VARSEG"><span style="color:#4593D8;">VARSEG</span></a>(Array(0))
   <a class="mw-selflink selflink"><span style="color:#4593D8;">BLOAD</span></a> filename$, <a href="VARPTR" title="VARPTR"><span style="color:#4593D8;">VARPTR</span></a>(Array(<a href="LBOUND" title="LBOUND"><span style="color:#4593D8;">LBOUND</span></a>(Array))) ' changeable index
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Referance any type of array that matches the data saved. Can work with Integer, Single, Double, Long, fixed length Strings or <a href="TYPE" title="TYPE">TYPE</a> arrays. <a href="LBOUND" title="LBOUND">LBOUND</a> determines the starting offset of the array or another index could be used.</dd></dl>
<p>
<i>Example 2:</i> Using a QB default colored image.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a> = <a href="VARSEG" title="VARSEG"><span style="color:#4593D8;">VARSEG</span></a>(Image%(0)) ' pointer to first image element of an array
   <a class="mw-selflink selflink"><span style="color:#4593D8;">BLOAD</span></a> FileName$, <a href="VARPTR" title="VARPTR"><span style="color:#4593D8;">VARPTR</span></a>(Image%(0)) ' place data into array at index position 0
   <a href="PUT_(graphics_statement)" title="PUT (graphics statement)"><span style="color:#4593D8;">PUT</span></a>(Col, Row), Image%(0), PSET ' Put the image on the screen from index 0
 <a href="DEF_SEG" title="DEF SEG"><span style="color:#4593D8;">DEF SEG</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a href="PSET" title="PSET">PSET</a> is used as a <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> action that places the image over any background objects.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BSAVE" title="BSAVE">BSAVE</a>, <a href="OPEN" title="OPEN">OPEN</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="PUT" title="PUT">PUT</a>, <a href="GET" title="GET">GET</a> <span style="color:#777777;">(file statement)</span></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a>, <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="VARSEG" title="VARSEG">VARSEG</a>, <a href="VARPTR" title="VARPTR">VARPTR</a></li>
<li><a href="DEF_SEG" title="DEF SEG">DEF SEG</a></li>
<li><a href="Text_Using_Graphics" title="Text Using Graphics">Text Using Graphics</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192345
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 151/1000000
Post‐expand include size: 1556/2097152 bytes
Template argument size: 247/2097152 bytes
Highest expansion depth: 5/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.335      1 -total
 11.85%    3.238     12 Template:Cl
  9.49%    2.594      1 Template:PageSyntax
  9.45%    2.584      1 Template:Text
  9.43%    2.578      6 Template:Parameter
  8.72%    2.383      1 Template:PageDescription
  7.66%    2.093      2 Template:CodeStart
  7.43%    2.031      1 Template:PageParameters
  7.25%    1.982      1 Template:PageNavigation
  7.25%    1.981      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:400-0!canonical and timestamp 20240714192345 and revision id 7824.
 -->
</div>
</div>
</div>
</div>
</body>
</html>