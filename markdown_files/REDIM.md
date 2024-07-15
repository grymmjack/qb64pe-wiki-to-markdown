<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>REDIM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-REDIM rootpage-REDIM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">REDIM</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>A <a class="mw-selflink selflink">REDIM</a> statement can re-dimension one <a href="$DYNAMIC" title="$DYNAMIC">dynamic</a>(flexible) <a href="Arrays" title="Arrays">array</a> or a <a href="Comma" title="Comma">comma</a> separated list of arrays.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">REDIM</a> low_element[[[TO <i>upper_element</i>, ...]}) [[[AS <a href="TYPE" title="TYPE">Type</a>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Can change the number of elements in an array (the present array data is lost unless <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> is used).</li>
<li>Dynamic array elements can also be sized or resized by a program user's entry.</li>
<li>The <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> option also allows the <i>element</i> range values to be moved upward or downward in <b>QB64 only!</b></li>
<li><i>Array</i> is the name of the array to be dimensioned or re-dimensioned.</li>
<li><i>elements</i> is the number of elements the array should hold. Use the optional <a href="TO" title="TO">TO</a> <i>elements2</i> to set a range.</li>
<li><b>Always use the same array <a href="TYPE" title="TYPE">TYPE</a> suffix (<a href="AS" title="AS">AS</a> type) or a new array type with the same name may be created.</b></li>
<li>REDIM cannot change <a href="$STATIC" title="$STATIC">$STATIC</a> arrays created with a <a href="DIM" title="DIM">DIM</a> statement unless the <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> <a href="Metacommand" title="Metacommand">Metacommand</a> is used!</li>
<li>To create a dynamic array use the <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> metacommand or use <a class="mw-selflink selflink">REDIM</a> rather than <a href="DIM" title="DIM">DIM</a> when first creating the array.</li>
<li>Use REDIM <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> to change the range or number of array elements without losing the remaining elements. Data may move up or down to accommodate those boundary changes.</li>
<li><b>REDIM <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> cannot change the number of array dimensions or type!</b></li>
<li><a href="$DYNAMIC" title="$DYNAMIC">Dynamic</a> arrays MUST be <a class="mw-selflink selflink">REDIMensioned</a> if <a href="ERASE" title="ERASE">ERASE</a> or <a href="CLEAR" title="CLEAR">CLEAR</a> are used to clear the arrays as they no longer exist.</li>
<li>When <a href="AS" title="AS">AS</a> is used to declare the type, use <a href="AS" title="AS">AS</a> to retain that type or it will change to <a href="SINGLE" title="SINGLE">SINGLE</a>!</li>
<li><b>NOTE: Many QBasic keyword variable names CAN be used with a <a href="STRING" title="STRING">STRING</a> suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use <a href="DIM" title="DIM">DIM</a>, <a class="mw-selflink selflink">REDIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> or <a href="TYPE" title="TYPE">TYPE</a> variable <a href="AS" title="AS">AS</a> statements!</b></li>
<li><b>Warning! Do not use negative array upper bound index values as OS access or "Out of Memory" <a href="ERROR_Codes" title="ERROR Codes">errors</a> will occur!</b></li></ul>
<p>
<i>Example 1:</i> The <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> Metacommand allows an array to be re-sized using <a href="DIM" title="DIM">DIM</a> and REDIM.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'<a href="$DYNAMIC" title="$DYNAMIC"><span style="color:#4593D8;">$DYNAMIC</span></a>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter array size: ", size
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Array(size)
<a class="mw-selflink selflink"><span style="color:#4593D8;">REDIM</span></a> Array(2 * size)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(Array)
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Shows the difference between REDIM and REDIM <a href="PRESERVE" title="PRESERVE">_PRESERVE</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">REDIM</span></a> array(20)
array(10) = 24
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(10)
<a class="mw-selflink selflink"><span style="color:#4593D8;">REDIM</span></a> <a href="PRESERVE" title="PRESERVE"><span style="color:#4593D8;">_PRESERVE</span></a> array(30)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(10)
<a class="mw-selflink selflink"><span style="color:#4593D8;">REDIM</span></a> array(15)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(10)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 24
 24
 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> REDIM without _PRESERVE erases the array data and cannot change the number of dimensions.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Arrays" title="Arrays">Arrays</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="PRESERVE" title="PRESERVE">_PRESERVE</a>, <a href="ERASE" title="ERASE">ERASE</a></li>
<li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a>, <a href="$STATIC" title="$STATIC">$STATIC</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031659
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 128/1000000
Post‐expand include size: 1461/2097152 bytes
Template argument size: 164/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.020      1 -total
 11.27%    2.143     13 Template:Cl
 10.72%    2.039      1 Template:PageSyntax
  9.00%    1.711      1 Template:PageNavigation
  8.97%    1.707      1 Template:PageSeeAlso
  8.95%    1.703      1 Template:OutputStart
  8.94%    1.700      2 Template:CodeStart
  8.91%    1.695      3 Template:Parameter
  8.77%    1.669      1 Template:PageDescription
  8.65%    1.646      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:241-0!canonical and timestamp 20240715031659 and revision id 6608.
 -->
</div>
</div>
</div>
</div>
</body>
</html>