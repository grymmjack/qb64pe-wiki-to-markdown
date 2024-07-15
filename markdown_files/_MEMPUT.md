<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMPUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMPUT rootpage-MEMPUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMPUT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMPUT</a> statement writes data to a portion of a designated memory block at an <a href="OFFSET" title="OFFSET">OFFSET</a> position.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MEMPUT</a> <i>memoryBlock</i>, <i>bytePosition</i>, <i>sourceVariable</i> [AS <i>type</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>memoryBlock</i> is a <a href="MEM" title="MEM">_MEM</a> variable type memory block name created by <a href="MEMNEW" title="MEMNEW">_MEMNEW</a> or the <a href="MEM_(function)" title="MEM (function)">_MEM</a> function.</li>
<li><i>bytePosition</i> is the <i>memoryBlock</i>.<a href="OFFSET" title="OFFSET">OFFSET</a> start position plus any bytes needed to read specific values.</li>
<li>The <i>sourceVariable</i> type designates the size and <i>bytePosition</i> it should be written to. It can be a variable, <a href="Arrays" title="Arrays">array</a> or user defined type.</li>
<li><i>bytePosition</i> can be converted <a href="AS" title="AS">AS</a> a specific variable <i><a href="TYPE" title="TYPE">type</a></i> before being written to the <i>memoryBlock</i> as bytes.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The _MEMPUT statement is similar to the <a href="PUT" title="PUT">PUT</a> file statement, but <i>bytePosition</i> is required.</li>
<li>The <i>memoryBlock</i>.<a href="OFFSET" title="OFFSET">OFFSET</a> returns the starting byte position of the block. Add bytes to move into the block.</li>
<li>The variable type held in the memory block can determine the next <i>byte position</i> to write a value.</li>
<li><a href="LEN" title="LEN">LEN</a> can be used to determine the byte size of numerical or user defined <a href="Variable_Types" title="Variable Types">Variable Types</a> regardless of the value held.</li>
<li><a href="STRING" title="STRING">STRING</a> values should be of a defined length. Variable length strings can actually move around in memory and not be found.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description_2">Description</span></h2>
<p><i>Example:</i> _MEMPUT can be used just like <a href="POKE" title="POKE">POKE</a> without <a href="DEF_SEG" title="DEF SEG">DEF SEG</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> o <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
o = <a href="MEM_(function)" title="MEM (function)"><span style="color:#4593D8;">_MEM</span></a>(d&amp;)
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMPUT</span></a> o, o.OFFSET + 1, 3 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>  'POKE
v = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(o, o.OFFSET + 1, <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>) 'PEEK
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> v 'prints 3
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> d&amp; 'print 768 because the 2nd byte of d&amp; has been set to 3 or 3 * 256
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li>
<li><a href="MEM" title="MEM">_MEM</a>, <a href="MEM_(function)" title="MEM (function)">_MEM (function)</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMFREE" title="MEMFREE">_MEMFREE</a>, <a href="MEMCOPY" title="MEMCOPY">_MEMCOPY</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062406
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.068 seconds
Preprocessor visited node count: 165/1000000
Post‐expand include size: 1580/2097152 bytes
Template argument size: 303/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   44.450      1 -total
 21.70%    9.646      1 Template:CodeStart
 20.20%    8.978     13 Template:Cl
 10.16%    4.517      1 Template:PageSyntax
  7.43%    3.304     13 Template:Parameter
  6.98%    3.101      1 Template:CodeEnd
  6.80%    3.024      1 Template:PageNavigation
  6.56%    2.917      1 Template:PageSeeAlso
  6.49%    2.883      1 Template:PageParameters
  6.14%    2.730      2 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:185-0!canonical and timestamp 20240715062406 and revision id 8716.
 -->
</div>
</div>
</div>
</div>
</body>
</html>