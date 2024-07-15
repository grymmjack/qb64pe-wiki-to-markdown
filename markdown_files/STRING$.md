<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STRING$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STRING rootpage-STRING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STRING$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">STRING$</a> function returns a <a href="STRING" title="STRING">STRING</a> consisting of a single character repeated a number of times.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>result$ = STRING$(<i>count&amp;</i>, {<i>character$</i> | <i>ASCIIcode%</i>} )</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>count&amp;</i> is the number of times the character specified by <i>character</i> is repeated.</li>
<li>Character is a literal string character, a string variable or an <a href="ASCII" title="ASCII">ASCII</a> code number.</li>
<li>If <i>count&amp;</i> is negative, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur. The count can be zero.</li>
<li>If <i>character</i> is a <a href="STRING" title="STRING">STRING</a> value and its length is zero, an <a href="ERROR_Codes" title="ERROR Codes">illegal function call</a> error will occur.</li>
<li>If more than one string character value is used, the first character will be repeated.</li>
<li>A <a href="STRING" title="STRING">STRING</a> statement can be added to a string value with the + <a href="Concatenation" title="Concatenation">concatenation</a> operator.</li>
<li>The function result can also be used to <a href="GET" title="GET">GET</a> and <a href="PUT" title="PUT">PUT</a> a number of bytes as zero characters: bytes$ = STRING(numbytes, 0)</li></ul>
<p>
<i>Differences between QB64 and QB 4.5:</i>
</p>
<ul><li><b>QB64</b> can use <a href="LONG" title="LONG">LONG</a> values for a count up to 2,147,483,647 while <b>QB 4.5</b> could only use <a href="INTEGER" title="INTEGER">INTEGER</a> values up to 32,767.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd>Printing 40 asterisks across the screen using an ASCII character code instead of <a href="CHR$" title="CHR$">CHR$</a>(42).</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">STRING$</span></a>(40, 42)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">****************************************
</pre>
</td></tr></tbody></table>
<dl><dd>Using a <a href="STRING" title="STRING">STRING</a> to specify the repeated character.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">text$ = "B" + <a class="mw-selflink selflink"><span style="color:#4593D8;">STRING$</span></a>(40, "A") + "D"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD
</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li>
<li><a href="SaveIcon32" title="SaveIcon32">SaveIcon32</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SPACE$" title="SPACE$">SPACE$</a></li>
<li><a href="ASC" title="ASC">ASC</a>, <a href="CHR$" title="CHR$">CHR$</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034227
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.037 seconds
Real time usage: 0.064 seconds
Preprocessor visited node count: 128/1000000
Post‐expand include size: 1118/2097152 bytes
Template argument size: 78/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   45.988      1 -total
 13.16%    6.052      2 Template:OutputEnd
 11.20%    5.152      2 Template:OutputStart
 11.04%    5.077      2 Template:CodeEnd
 10.93%    5.027      4 Template:Cl
  8.88%    4.084      1 Template:PageDescription
  8.35%    3.842      1 Template:PageSeeAlso
  7.53%    3.464      1 Template:PageSyntax
  6.56%    3.015      2 Template:CodeStart
  6.26%    2.881      4 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:570-0!canonical and timestamp 20240715034227 and revision id 8676.
 -->
</div>
</div>
</div>
</div>
</body>
</html>