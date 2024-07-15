<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMELEMENT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMELEMENT rootpage-MEMELEMENT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMELEMENT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMELEMENT</a> function returns a <a href="MEM" title="MEM">_MEM</a> block referring to a variable's memory, but not past it.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>memoryBlock</i> = <a class="mw-selflink selflink">_MEMELEMENT</a>(<i>referenceVariable</i>)</dd></dl>
<p>
</p>
<ul><li>The <i>referenceVariable</i> parameter designates the existing variable name using the memory block.</li>
<li>_MEMELEMENT is the same as <a href="MEM" title="MEM">_MEM</a> but in an array it returns the specifications of an element, not the entire array.</li>
<li>All values created by memory functions MUST be freed using <a href="MEMFREE" title="MEMFREE">_MEMFREE</a> with a valid <a href="MEM" title="MEM">_MEM</a> variable type.</li>
<li>The _MEMELEMENT type contains the following <b>read-only</b> elements where <i>name</i> is the variable name:</li></ul>
<dl><dd><dl><dd><i>name</i><b>.OFFSET</b> is the beginning offset of the memory block AS <a href="OFFSET" title="OFFSET">_OFFSET</a></dd>
<dd><i>name</i><b>.SIZE</b> returns the largest available region of memory of the ELEMENT in bytes AS <a href="OFFSET" title="OFFSET">_OFFSET</a></dd>
<dd><i>name</i><b>.ELEMENTSIZE</b> is the <a href="BYTE" title="BYTE">_BYTE</a> size of the elements within the block AS <a href="OFFSET" title="OFFSET">_OFFSET</a></dd></dl></dd></dl>
<dl><dd><dl><dd><dl><dd><ul><li>2 = <a href="INTEGER" title="INTEGER">INTEGER</a> values have an element size of 2 bytes</li>
<li>4 = <a href="LONG" title="LONG">LONG</a> integer and <a href="SINGLE" title="SINGLE">SINGLE</a> float values have an element size of 4 bytes</li>
<li>8 = <a href="DOUBLE" title="DOUBLE">DOUBLE</a> float and <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> values have an element size of 8 bytes</li>
<li>32 = <a href="FLOAT" title="FLOAT">_FLOAT</a> values have an element size of 32 bytes</li>
<li><a href="LEN" title="LEN">LEN</a> = <a href="STRING" title="STRING">STRING</a> or <a href="OFFSET" title="OFFSET">_OFFSET</a> byte sizes vary so use <a href="LEN" title="LEN">LEN</a>(variable) for the number of bytes.</li></ul></dd></dl></dd>
<dd><i>name</i><b>.TYPE</b> is the type (represented as bits combined to form a value) AS <a href="LONG" title="LONG">LONG</a> (see below).</dd></dl></dd></dl>
<p>
</p>
<h2><span id=".TYPE_values_.28version_1.000_and_up.29"></span><span class="mw-headline" id=".TYPE_values_(version_1.000_and_up)">.TYPE values (version 1.000 and up)</span></h2>
<dl><dd><dl><dd><dl><dd><ul><li>0 = UDT (<a href="TYPE" title="TYPE">user defined type</a>) or memory created by <a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li>1 = 1 bit   ELEMENT.SIZE=1   *Only used along with specific types (currently integers or floats)</li>
<li>2 = 2 bit. ELEMENT.SIZE=2   *</li>
<li>4 = 4 bit. ELEMENT.SIZE=4   *</li>
<li>8 = 8 bit. ELEMENT.SIZE=8   *</li>
<li>16 = 16 bit. ELEMENT.SIZE=16  *</li>
<li>32 = 32 bit. ELEMENT.SIZE=32  *</li>
<li>64 = 64 bit. ELEMENT.SIZE=64  *</li>
<li>128 = 128 bit. ELEMENT.SIZE=128 *</li>
<li>256 = 256 bit. ELEMENT.SIZE=256 *</li>
<li>512(+ bit*) = integer types only(ie. whole numbers)</li>
<li>1024(+ bit*) = floating point types only(ie. numbers that can have a decimal point)</li>
<li>2048 = <a href="STRING" title="STRING">STRING</a> type only</li>
<li>4096(+ 512 + bit*) = <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> integer type only</li>
<li>8192 = <a href="MEM" title="MEM">_MEM</a> type only</li>
<li>16384(+ 512 + bit*)= <a href="OFFSET" title="OFFSET">_OFFSET</a> type only</li></ul></dd></dl></dd></dl></dd></dl>
<p><i>Note: If a future integer, float or other type doesn't have a size that is 1,2,4,8,16,32,64,128 or 256 it won't have a size-bit set.</i>
</p>
<h3><span class="mw-headline" id="Versions_prior_to_1.000">Versions prior to 1.000</span></h3>
<dl><dd><dl><dd><dl><dd><ul><li>1 = Integer types such as <a href="BYTE" title="BYTE">_BYTE</a>, <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a>, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> or <a href="OFFSET" title="OFFSET">_OFFSET</a></li>
<li>2 = <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> variable types. Value must be added to the variable type value.(2 cannot be used by itself)</li>
<li>3 = ALL <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a> type values.(add 1 + 2)</li>
<li>4 = Floating point types such as <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a></li>
<li>8 = <a href="STRING" title="STRING">STRING</a></li>
<li>0 = unknown(eg. created with <a href="MEMNEW" title="MEMNEW">_MEMNEW</a>) or <a href="TYPE" title="TYPE">user-defined-types</a></li></ul></dd></dl></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Comparing the specifications returned by <a href="MEM" title="MEM">_MEM</a> and _MEMELEMENT from an array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m1 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m2 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
m1 = <a href="MEM_(function)" title="MEM (function)"><span style="color:#4593D8;">_MEM</span></a>(a(50)) 'function returns information about array up to specific element
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> m1.OFFSET, m1.SIZE, m1.TYPE, m1.ELEMENTSIZE
m2 = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMELEMENT</span></a>(a(50)) 'function returns information about the specific element
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> m2.OFFSET, m2.SIZE, m2.TYPE, m2.ELEMENTSIZE
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd>Output using VERSION .954 ONLY .TYPE values: 1 (integer) + 2 (unsigned)</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">28377205        51        3        1
28377205        1         3        1 </pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="MEM" title="MEM">_MEM</a> returns the info about the array to that element while _MEMELEMENT returns info about that element only.
<dl><dd><ul><li><a href="MEM" title="MEM">_MEM</a> value returns the available array .SIZE as 51 bytes from the designated array element.</li>
<li><a class="mw-selflink selflink">_MEMELEMENT</a> value returns the available element .SIZE as one byte.</li></ul></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a></li>
<li><a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062359
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.043 seconds
Real time usage: 0.051 seconds
Preprocessor visited node count: 188/1000000
Post‐expand include size: 1539/2097152 bytes
Template argument size: 190/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.067      1 -total
 13.24%    2.922     16 Template:Cl
  9.91%    2.187      1 Template:CodeEnd
  9.27%    2.046      1 Template:CodeStart
  9.02%    1.990      1 Template:PageNavigation
  8.95%    1.975      1 Template:OutputStart
  8.84%    1.950      1 Template:PageSyntax
  8.17%    1.803      1 Template:PageExamples
  8.10%    1.788      1 Template:OutputEnd
  7.84%    1.730      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:177-0!canonical and timestamp 20240715062359 and revision id 7511.
 -->
</div>
</div>
</div>
</div>
</body>
</html>