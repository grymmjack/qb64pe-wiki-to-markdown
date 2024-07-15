<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CLEAR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLEAR rootpage-CLEAR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CLEAR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CLEAR</a> statement clears all variable and array element values in a program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CLEAR</a> [, <i>ignored&amp;</i> , <i>ignored&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All parameters are optional and ignored by <b>QB64</b>.</li>
<li>Normally used to clear all program variable and <a href="Arrays" title="Arrays">array</a> values where numerical values become zero and string values become empty ("").</li>
<li>It does not clear <a href="CONST" title="CONST">constant</a> values.</li>
<li>Closes all opened files.</li>
<li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> or <a href="REDIM" title="REDIM">REDIM</a> arrays will need to be <a href="REDIM" title="REDIM">redimensioned</a> or an <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur when referenced because they are removed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Using CLEAR to clear array elements from <a href="STATIC" title="STATIC">static</a> arrays or arrays created using <a href="DIM" title="DIM">DIM</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> array(10)   'create a <a href="$STATIC" title="$STATIC"><span style="color:#4593D8;">$STATIC</span></a> array
array(5) = 23
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(5)
<a class="mw-selflink selflink"><span style="color:#4593D8;">CLEAR</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(5)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> If you change DIM to REDIM a "Subscript out of range" error will occur because a <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> array is removed by CLEAR.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1223" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ERASE" title="ERASE">ERASE</a></li>
<li><a href="REDIM" title="REDIM">REDIM</a>, <a href="PRESERVE" title="PRESERVE">_PRESERVE</a></li>
<li><a href="Arrays" title="Arrays">Arrays</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034035
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.023 seconds
Real time usage: 0.029 seconds
Preprocessor visited node count: 70/1000000
Post‐expand include size: 976/2097152 bytes
Template argument size: 72/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.058      1 -total
 12.95%    2.079      1 Template:PageSyntax
 11.78%    1.892      1 Template:CodeStart
 11.47%    1.842      6 Template:Cl
  9.95%    1.598      1 Template:PageNavigation
  9.93%    1.595      1 Template:PageSeeAlso
  9.89%    1.588      2 Template:Parameter
  9.47%    1.520      1 Template:CodeEnd
  9.27%    1.489      1 Template:PageDescription
  9.10%    1.461      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:302-0!canonical and timestamp 20240715034035 and revision id 9011.
 -->
</div>
</div>
</div>
</div>
</body>
</html>