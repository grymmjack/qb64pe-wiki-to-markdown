<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMFILL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMFILL rootpage-MEMFILL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMFILL</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMFILL</a> statement converts a value to a specified type, then fills memory with that type including any non-whole remainder.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MEMFILL</a> <i>memoryBlock</i>, <i>memoryBlock.OFFSET</i>, <i>fillBytes</i>, <i>value</i> [AS <i>variableType</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>memoryBlock</i> <a href="MEM" title="MEM">_MEM</a> memory block is the block referenced to be filled.</li>
<li><i>memoryBlock.OFFSET</i> is the starting offset of the above referenced memory block.</li>
<li>The <i>fillBytes</i> is the number of bytes to fill the memory block.</li>
<li>The <i>value</i> is the value to place in the memory block at the designated OFFSET position.</li>
<li>A literal or variable <i>value</i> can be optionally set <a href="AS" title="AS">AS</a> a variable <a href="Variable_Types" title="Variable Types">type</a> appropriate for the memory block.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>To clear previous data from a <a href="MEMNEW" title="MEMNEW">_MEMNEW</a> memory block, use _MEMFILL with a <i>value</i> of 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Filling array values quickly using FOR loops or a simple memory fill.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a(100, 100) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> b(100, 100) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
'filling array a with value 13
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i1 = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i2 = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100
        a(i1, i2) = 13
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
'filling array b with value 13
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> mema <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
mema = <a href="MEM_(function)" title="MEM (function)"><span style="color:#4593D8;">_MEM</span></a>(b())
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMFILL</span></a> mema, mema.OFFSET, mema.SIZE, 13 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
<a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> mema
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a>, <a href="MEM_(function)" title="MEM (function)">_MEM (function)</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062400
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 208/1000000
Post‐expand include size: 1828/2097152 bytes
Template argument size: 275/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.175      1 -total
 12.33%    3.350     20 Template:Cl
 10.33%    2.806      1 Template:PageSyntax
  9.47%    2.574     11 Template:Parameter
  8.74%    2.375      1 Template:CodeStart
  8.31%    2.257      1 Template:PageParameters
  8.18%    2.222      1 Template:PageDescription
  8.10%    2.202      1 Template:PageNavigation
  8.02%    2.180      1 Template:PageSeeAlso
  7.53%    2.047      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:179-0!canonical and timestamp 20240715062400 and revision id 8711.
 -->
</div>
</div>
</div>
</div>
</body>
</html>