<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_PRESERVE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PRESERVE rootpage-PRESERVE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_PRESERVE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_PRESERVE</a> <a href="REDIM" title="REDIM">REDIM</a> action preserves the current contents of <a href="$DYNAMIC" title="$DYNAMIC">dynamic</a> <a href="Arrays" title="Arrays">arrays</a>, when resizing or changing indices.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="REDIM" title="REDIM">REDIM</a> <a class="mw-selflink selflink">_PRESERVE</a> array(<i>newLowerIndex&amp;</i> [TO <i>newUpperIndex&amp;</i>]) [AS variabletype]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="REDIM" title="REDIM">REDIM</a> or the <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> metacommand must be used when the array is first created to be able to resize and preserve.</li>
<li>If <a class="mw-selflink selflink">_PRESERVE</a> is not used, the current contents of the array are cleared by <a href="REDIM" title="REDIM">REDIM</a>.
<ul><li>All element values of an array are preserved if the array size is increased.</li>
<li>The remaining elements of the array are preserved if the array size is decreased.</li>
<li>If the new index range is different from the original, all values will be moved to the new corresponding indices.</li></ul></li>
<li><b>REDIM <a class="mw-selflink selflink">_PRESERVE</a> cannot change the number of array dimensions, but can change the number of elements.</b></li>
<li><b>Always use the same array <a href="TYPE" title="TYPE">TYPE</a> suffix (<a href="AS" title="AS">AS</a> type) or a new array type with the same name may be created.</b></li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li><a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> arrays created using <a href="REDIM" title="REDIM">REDIM</a> require that they be recreated to be used after arrays are <a href="ERASE" title="ERASE">ERASEd</a>.</li>
<li><b>Warning:</b> Do not use negative upper array index values as an "Out of Memory" <a href="ERROR_Codes" title="ERROR Codes">error</a> (or global Operating System errors) will occur.<b></b></li>
<li>Use <a class="mw-selflink selflink">_PRESERVE</a> before <a href="SHARED" title="SHARED">SHARED</a> or an "invalid variable name" error will occur.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Changing the upper and lower array bounds
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> a(5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 10) ' create array as dynamic using REDIM
a(5) = 123
<a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRESERVE</span></a> a(20 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 40)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a(20)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> a(20) is now the 123 value a(5) was. The upper or lower bounds of arrays can be changed, but the type cannot. New array indices like a(40) are null(0) or empty strings. If the array element count is not reduced, all of the data will be preserved.</dd></dl>
<p>
<i>Example 2:</i> Sizing an array while storing file data.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> Array$(1)                'create a dynamic string array
filename$ = "Readme.txt"       'QB64 information text file
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> filename$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(1)
  count = count + 1
  <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> count &gt; <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(Array$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_PRESERVE</span></a> Array$(count * 3 / 2)'increase array's size by 50% without losing data
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #1, textline$
  Array$(count) = textline$
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> c = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> count
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Array$(c)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> c <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 20 = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> k$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1111" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a></li>
<li><a href="Arrays" title="Arrays">Arrays</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034433
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 280/1000000
Post‐expand include size: 2406/2097152 bytes
Template argument size: 368/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.094      1 -total
 14.96%    2.707     32 Template:Cl
 10.45%    1.890      1 Template:PageSeeAlso
 10.42%    1.886      1 Template:PageNavigation
  9.87%    1.786      1 Template:PageSyntax
  9.67%    1.750      2 Template:Parameter
  8.74%    1.581      1 Template:PageDescription
  8.00%    1.447      1 Template:PageExamples
  7.91%    1.431      2 Template:CodeStart
  7.47%    1.351      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:247-0!canonical and timestamp 20240715034433 and revision id 8887.
 -->
</div>
</div>
</div>
</div>
</body>
</html>