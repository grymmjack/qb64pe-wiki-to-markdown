<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DIM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DIM rootpage-DIM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DIM</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">DIM</a> statement is used to declare a variable or a list of variables as a specified data type or to dimension <a href="$STATIC" title="$STATIC">$STATIC</a> or <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> <a href="Arrays" title="Arrays">arrays</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><i>To declare variables:</i>
<dl><dd><a class="mw-selflink selflink">DIM</a>  <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>type</i>}] [, <i>variable2</i>...</dd></dl></dd></dl></dd></dl>
<dl><dd><dl><dd><i>To declare arrays:</i>
<dl><dd><a class="mw-selflink selflink">DIM</a>  <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>type</i>}] [, <i>variable2</i>...]</dd></dl></dd></dl></dd></dl>
<dl><dd><dl><dd><i> <b>QB64</b> Alternative Syntax:</i>
<dl><dd><a class="mw-selflink selflink">DIM</a> [[[SHARED] <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>type</i> <i>variable</i>  [, <i>variable2</i>...]</dd>
<dd><a class="mw-selflink selflink">DIM</a> [[[SHARED] <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <i>type</i> <i>array([lowest% <a href="TO" title="TO">TO</a>] highest%])</i> [, <i>array2(elements)</i>...]</dd></dl></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Sets the <a href="INTEGER" title="INTEGER">INTEGER</a> range of elements (indices) of a <a href="STATIC" title="STATIC">STATIC</a> array. If only one number is used, the <a href="LBOUND" title="LBOUND">lowest boundary</a> is 0 by default.</li>
<li>When used before an array is dimensioned, <b><a href="OPTION_BASE" title="OPTION BASE">OPTION BASE</a> 1</b> can set the default <a href="LBOUND" title="LBOUND">lower boundary</a> of arrays to 1.</li>
<li>DIM <a href="SHARED" title="SHARED">SHARED</a> shares variable values with sub-procedures without passing the value in a parameter.</li>
<li>Use the <a href="AS" title="AS">AS</a> keyword to define a variable or array <i>type</i> <a href="AS" title="AS">AS</a>...
<ul><li><a href="INTEGER" title="INTEGER">INTEGER</a> (or use variable suffix <b>%</b>)</li>
<li><a href="LONG" title="LONG">LONG</a> (or use variable suffix <b>&amp;</b>)</li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a> (or use variable suffix <b>!</b> or no suffix by default)</li>
<li><a href="DOUBLE" title="DOUBLE">DOUBLE</a> (or use variable suffix <b>#</b>)</li>
<li><a href="STRING" title="STRING">STRING</a> (or use variable suffix <b>$</b>). An AS multiplier can set the string <a href="LEN" title="LEN">length</a>. Ex: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">DIM <i>variable</i> AS STRING * 8</span></li></ul></li>
<li><b>QB64</b> variable types:
<ul><li><a href="BIT" title="BIT">_BIT</a> (or use variable suffix <b>`</b>). An AS multiplier can be used for multiple bits. Ex: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">DIM <i>variable</i> AS _BIT * 8</span></li>
<li><a href="BYTE" title="BYTE">_BYTE</a> (or use variable suffix <b>%%</b>)</li>
<li><a href="INTEGER64" title="INTEGER64">_INTEGER64</a> (or use variable suffix <b>&amp;&amp;</b>)</li>
<li><a href="FLOAT" title="FLOAT">_FLOAT</a> (or use variable suffix <b>##</b>)</li>
<li><a href="OFFSET" title="OFFSET">_OFFSET</a> (or use variable suffix <b>%&amp;</b>)</li>
<li>DIM AS <a href="MEM" title="MEM">_MEM</a> (the _MEM type has no type suffix).</li></ul></li>
<li><b>Note: When a variable has not been defined or has no type suffix, the type defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li>
<li>When using the <b>AS type variable-list</b> syntax, type symbols cannot be used.</li>
<li>When the <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> metacommand or <a href="REDIM" title="REDIM">REDIM</a> is used, array element sizes are changeable (not <a href="$STATIC" title="$STATIC">$STATIC</a>).</li>
<li>Use <a href="REDIM" title="REDIM">REDIM</a> instead of DIM to dimension arrays as dynamic without the <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a> metacommand.</li>
<li>Use <a href="REDIM" title="REDIM">REDIM</a> <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> in <b>QB64</b> to retain previous array values when changing the size of an array.</li>
<li><a href="REDIM" title="REDIM">REDIM</a> <a href="PRESERVE" title="PRESERVE">_PRESERVE</a> cannot change the number of array dimensions. An <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur.</li>
<li><a href="$DYNAMIC" title="$DYNAMIC">Dynamic</a> arrays MUST be <a href="REDIM" title="REDIM">REDIMensioned</a> if <a href="ERASE" title="ERASE">ERASE</a> or <a href="CLEAR" title="CLEAR">CLEAR</a> are used, as the arrays are completely removed.</li>
<li>All numerical variable types <b>except</b> <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> and <a href="FLOAT" title="FLOAT">_FLOAT</a> can be dimensioned as <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> (suffix ~) or positive only.</li>
<li><b>NOTE:</b> Many QBasic keyword variable names can be used with a <a href="STRING" title="STRING">STRING</a> suffix ($). You cannot use them without the suffix, use a numerical suffix or use <i>DIM, <a href="REDIM" title="REDIM">REDIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> or <a href="TYPE" title="TYPE">TYPE</a> variable <a href="AS" title="AS">AS</a></i> statements. <b>Although possible, it's recommended to avoid using reserved names.</b></li>
<li><b>Warning: Do not use negative array upper bound index values, or OS access or "Out of Memory" <a href="ERROR_Codes" title="ERROR Codes">errors</a> will occur.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Defines Qt variable as a one byte fixed length string.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> Qt <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Dimensions and types an array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> Image(2000) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 3:</i> Dimensions array with an <a href="INTEGER" title="INTEGER">INTEGER</a> type suffix.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> Image%(2000)
</pre>
</td></tr></tbody></table>
<p><i>Example 4:</i> Dimensions a range of <a href="Arrays" title="Arrays">array</a> elements as <a href="SHARED" title="SHARED">SHARED</a> integers.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> Image(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 1000) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 5:</i> Dimensions variable as an <a href="Arrays" title="Arrays">array</a> of 8 elements of the type <a href="UNSIGNED" title="UNSIGNED">UNSIGNED</a> BIT.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> bit(8) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BIT" title="BIT"><span style="color:#4593D8;">_BIT</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 6:</i> QB64 is more flexible than QBasic when it comes to "Duplicate Definition" errors. The following code does not error:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">x = 1 'x is a <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> variable
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
<a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="SINGLE" title="SINGLE">SINGLE</a> variable can be differentiated from the <a href="LONG" title="LONG">LONG</a> x variable by using suffixes like x! or x&amp; in later code.</dd></dl>
<p>
<i>Example 7:</i> The following code will create a "Name already in use" <b>status error</b> in QB64 when the variable types are the same.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">x = 1 'x is a <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> variable
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
<a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> QB64 gives an error because the creation of the new variable would make referring to the existing one impossible.</dd></dl>
<p>
<i>Example 8:</i> Using QB64's alternative syntax to declare multiple variables/arrays of the same type.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> w, h, id, weight, index 'all of these variables are created as type LONG
<a class="mw-selflink selflink"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a> x, y, z               'all of these variables are created as type SINGLE
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="PRESERVE" title="PRESERVE">_PRESERVE</a></li>
<li><a href="REDIM" title="REDIM">REDIM</a>, <a href="TYPE" title="TYPE">TYPE</a></li>
<li><a href="ERASE" title="ERASE">ERASE</a>, <a href="CLEAR" title="CLEAR">CLEAR</a></li>
<li><a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a>, <a href="DEFSTR" title="DEFSTR">DEFSTR</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a>, <a href="Arrays" title="Arrays">Arrays</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li>
<li><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT">OPTION _EXPLICIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192418
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 287/1000000
Post‐expand include size: 3198/2097152 bytes
Template argument size: 272/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.205      1 -total
 13.15%    2.920     34 Template:Cl
 10.54%    2.341      1 Template:PageSyntax
  9.27%    2.059      1 Template:PageDescription
  8.47%    1.880      2 Template:InlineCode
  8.24%    1.829      8 Template:CodeStart
  8.08%    1.793      2 Template:InlineCodeEnd
  8.02%    1.780      1 Template:PageExamples
  7.41%    1.646      1 Template:PageSeeAlso
  6.80%    1.510      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:300-0!canonical and timestamp 20240714192418 and revision id 6589.
 -->
</div>
</div>
</div>
</div>
</body>
</html>