<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$STATIC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_STATIC rootpage-_STATIC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$STATIC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$STATIC</a> <a href="Metacommand" title="Metacommand">metacommand</a> allows the creation of static (unresizable) arrays.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>{<a href="REM" title="REM">REM</a> | <a href="Apostrophe" title="Apostrophe">'</a> } <a class="mw-selflink selflink">$STATIC</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>QBasic <a href="Metacommand" title="Metacommand">Metacommands</a> require a REM or apostrophy (') before them and are normally placed at the start of the main module.</li>
<li>Static arrays cannot be resized. If a variable is used to size any array, it becomes <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a>.</li>
<li>A <a href="REDIM" title="REDIM">REDIM</a> statement has no effect on <a class="mw-selflink selflink">$STATIC</a> arrays except perhaps a <a href="ERROR_Codes" title="ERROR Codes">duplicate definition error</a> at the <a href="REDIM" title="REDIM">REDIM</a> statement.</li>
<li>The array's type cannot be changed once <a href="DIM" title="DIM">DIM</a> and a literal value sets the dimensions and element size.</li>
<li><a class="mw-selflink selflink">$STATIC</a> defined program <a href="Arrays" title="Arrays">arrays</a> cannot be <a href="REDIM" title="REDIM">re-sized</a> or use <a href="PRESERVE" title="PRESERVE">_PRESERVE</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> When a variable is used, the array can be resized despite $STATIC. The array becomes <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'<a class="mw-selflink selflink"><span style="color:#4593D8;">$STATIC</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter array size: ", size
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(size)   'using an actual number instead of the variable will create an error!
<a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> array(2 * size)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(array)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a href="DIM" title="DIM">DIM</a> using a literal numerical size will create a Duplicate definition error.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a>, <a href="STATIC" title="STATIC">STATIC</a></li>
<li><a href="Arrays" title="Arrays">Arrays</a>, <a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034015
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 62/1000000
Post‐expand include size: 958/2097152 bytes
Template argument size: 62/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.831      1 -total
 22.65%    5.624      1 Template:PageDescription
 22.56%    5.601      6 Template:Cl
  9.91%    2.461      1 Template:CodeStart
  9.43%    2.342      1 Template:PageSyntax
  7.84%    1.946      1 Template:PageExamples
  7.84%    1.946      1 Template:CodeEnd
  7.71%    1.914      1 Template:PageNavigation
  7.21%    1.789      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:298-0!canonical and timestamp 20240715034015 and revision id 5851.
 -->
</div>
</div>
</div>
</div>
</body>
</html>