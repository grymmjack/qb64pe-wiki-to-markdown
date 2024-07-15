<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ROR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ROR rootpage-ROR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ROR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ROR</a> function is used to rotate the bits of a numerical value to the right. A rotation (or circular shift) is an operation similar to shift (<a href="SHL" title="SHL">_SHL</a> and <a href="SHR" title="SHR">_SHR</a>) except that the bits that fall off at one end are put back to the other end.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">_ROR</a>(<i>numericalVariable</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalVariable</i> is the variable to shift the bits of and can be of the following types: <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>.</li>
<li>Integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> is the number of places to rotate the bits.</li>
<li>While 0 is a valid value it will have no affect on the variable being rotated.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In right rotation, the bits that fall off at right end are put back at left end.</li>
<li>The type of variable used to store the results should match the type of the variable being shifted.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.1.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT"><span style="color:#4593D8;">OPTION _EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> c <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> d <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER64" title="INTEGER64"><span style="color:#4593D8;">_INTEGER64</span></a>
a = &amp;B11110000
b = &amp;B1111111100000000
c = &amp;B11111111111111110000000000000000
d = &amp;B1111111111111111111111111111111100000000000000000000000000000000
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    a = <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROR</span></a>(a, 1)
    b = <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROR</span></a>(b, 1)
    c = <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROR</span></a>(c, 1)
    d = <a class="mw-selflink selflink"><span style="color:#4593D8;">_ROR</span></a>(d, 1)
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(8, "0") + <a href="BIN$" title="BIN$"><span style="color:#4593D8;">_BIN$</span></a>(a), 8);
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 2, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(16, "0") + <a href="BIN$" title="BIN$"><span style="color:#4593D8;">_BIN$</span></a>(b), 16);
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 3, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(32, "0") + <a href="BIN$" title="BIN$"><span style="color:#4593D8;">_BIN$</span></a>(c), 32);
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 4, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(64, "0") + <a href="BIN$" title="BIN$"><span style="color:#4593D8;">_BIN$</span></a>(d), 64);
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 15
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> &lt;&gt; 27
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ROL" title="ROL">_ROL</a>, <a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a></li>
<li><a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a></li>
<li><a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062548
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 369/1000000
Post‐expand include size: 3212/2097152 bytes
Template argument size: 576/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.833      1 -total
 10.39%    3.205      1 Template:PageSeeAlso
 10.33%    3.184     46 Template:Cl
  9.36%    2.886      1 Template:PageExamples
  8.35%    2.575      1 Template:PageSyntax
  8.20%    2.529      1 Template:PageNavigation
  8.17%    2.519      5 Template:Parameter
  7.39%    2.280      1 Template:CodeStart
  7.38%    2.275      1 Template:PageParameters
  6.72%    2.072      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1028-0!canonical and timestamp 20240715062548 and revision id 6514.
 -->
</div>
</div>
</div>
</div>
</body>
</html>