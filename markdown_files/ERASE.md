<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ERASE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERASE rootpage-ERASE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ERASE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">ERASE</a> statement is used to clear all data from an array. <a href="$STATIC" title="$STATIC">$STATIC</a> <a href="Arrays" title="Arrays">array</a> dimensions are not affected.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>ERASE <i>arrayName</i> [, <i>arrayName2</i>...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All string array elements become null strings ("") and all numerical array elements become 0.</li>
<li>Multiple arrays can be erased using commas between the array names.</li>
<li><a href="$DYNAMIC" title="$DYNAMIC">Dynamic</a> arrays must be <a href="REDIM" title="REDIM">REDIMensioned</a> if they are referenced after erased.</li>
<li>Dimension subprocedure arrays as <a href="STATIC" title="STATIC">STATIC</a> to use <a class="mw-selflink selflink">ERASE</a> and not have to REDIM.</li>
<li>You do not have to include array brackets in an <a class="mw-selflink selflink">ERASE</a> call.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1243" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="CLEAR" title="CLEAR">CLEAR</a></li>
<li><a href="STATIC" title="STATIC">STATIC</a></li>
<li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a></li>
<li><a href="Arrays" title="Arrays">Arrays</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034101
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.019 seconds
Real time usage: 0.025 seconds
Preprocessor visited node count: 12/1000000
Post‐expand include size: 545/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    9.857      1 -total
 29.20%    2.878      1 Template:PageSyntax
 23.71%    2.337      1 Template:PageSeeAlso
 21.46%    2.115      1 Template:PageDescription
 21.29%    2.098      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:301-0!canonical and timestamp 20240715034101 and revision id 8937.
 -->
</div>
</div>
</div>
</div>
</body>
</html>