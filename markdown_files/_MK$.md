<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MK$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MK rootpage-MK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MK$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MK$</a> function can convert any numerical type into an <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> value that can be converted back using <a href="CV" title="CV">_CV</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>string_value$</i> = <a class="mw-selflink selflink">_MK$</a>(<i>numericalType</i>, <i>numericalValue</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>numericalType</i> is any QB64 numerical type: <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a>, <a href="BYTE" title="BYTE">_BYTE</a> or <a href="BIT" title="BIT">_BIT</a>.</li>
<li>Whole integer values can be signed or <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a>.</li>
<li><i>numericalValue</i> must match the <i>numericalType</i> used.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Supports converting any QBasic or <b>QB64</b> numerical value into a string value.</li>
<li>Some resulting <a href="ASCII" title="ASCII">ASCII</a> string characters might not be able to be printed to the screen.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CV" title="CV">_CV</a></li>
<li><a href="MKI$" title="MKI$">MKI$</a>, <a href="CVI" title="CVI">CVI</a>, <a href="INTEGER" title="INTEGER">INTEGER</a></li>
<li><a href="MKL$" title="MKL$">MKL$</a>, <a href="CVL" title="CVL">CVL</a>, <a href="LONG" title="LONG">LONG</a></li>
<li><a href="MKS$" title="MKS$">MKS$</a>, <a href="CVS" title="CVS">CVS</a>, <a href="SINGLE" title="SINGLE">SINGLE</a></li>
<li><a href="MKD$" title="MKD$">MKD$</a>, <a href="CVD" title="CVD">CVD</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a></li>
<li><a href="MKSMBF$" title="MKSMBF$">MKSMBF$</a>, <a href="CVSMBF" title="CVSMBF">CVSMBF</a></li>
<li><a href="MKDMBF$" title="MKDMBF$">MKDMBF$</a>, <a href="CVDMBF" title="CVDMBF">CVDMBF</a></li>
<li><a href="PDS(7.1)_Procedures#CURRENCY" title="PDS(7.1) Procedures">CURRENCY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192814
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 40/1000000
Post‐expand include size: 688/2097152 bytes
Template argument size: 80/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.670      1 -total
 34.30%    6.403      1 Template:PageParameters
 15.64%    2.921      1 Template:PageSyntax
 14.94%    2.789      6 Template:Parameter
 11.09%    2.070      1 Template:PageDescription
  8.83%    1.648      1 Template:PageNavigation
  8.68%    1.620      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:187-0!canonical and timestamp 20240714192814 and revision id 7622.
 -->
</div>
</div>
</div>
</div>
</body>
</html>