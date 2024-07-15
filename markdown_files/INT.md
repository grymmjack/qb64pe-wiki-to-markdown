<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INT rootpage-INT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INT</a> function rounds a numeric value down to the next whole number.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <a class="mw-selflink selflink">INT</a>(<i>expression</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>expression</i> is any <a href="Data_types" title="Data types">type</a> of literal or variable numerical value or mathematical calculation.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">INT</a> returns the first whole number <a href="INTEGER" title="INTEGER">INTEGER</a> that is less than the <i>expression</i> value.</li>
<li>This means that <a class="mw-selflink selflink">INT</a> rounds down for both positive and negative numbers.</li>
<li>Use <a href="FIX" title="FIX">FIX</a> to round negative values up. It is identical to <a class="mw-selflink selflink">INT</a> for positive values.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displaying the rounding behavior of <a class="mw-selflink selflink">INT</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PRINT INT(2.5)
PRINT INT(-2.5)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 2
-3
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CINT" title="CINT">CINT</a>, <a href="CLNG" title="CLNG">CLNG</a>, <a href="FIX" title="FIX">FIX</a></li>
<li><a href="CSNG" title="CSNG">CSNG</a>, <a href="CDBL" title="CDBL">CDBL</a></li>
<li><a href="ROUND" title="ROUND">_ROUND</a>, <a href="CEIL" title="CEIL">_CEIL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714154210
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.022 seconds
Real time usage: 0.028 seconds
Preprocessor visited node count: 44/1000000
Post‐expand include size: 812/2097152 bytes
Template argument size: 36/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.672      1 -total
 11.77%    1.963      1 Template:PageSyntax
  9.38%    1.563      4 Template:Parameter
  8.89%    1.483      1 Template:OutputStart
  8.31%    1.386      1 Template:CodeStart
  8.23%    1.373      1 Template:PageParameters
  8.09%    1.349      1 Template:PageSeeAlso
  8.06%    1.344      1 Template:PageNavigation
  8.01%    1.335      1 Template:OutputEnd
  7.98%    1.331      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:285-0!canonical and timestamp 20240714154210 and revision id 6428.
 -->
</div>
</div>
</div>
</div>
</body>
</html>