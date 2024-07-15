<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMGET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMGET rootpage-MEMGET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMGET</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMGET</a> statement reads a portion of a memory block at an OFFSET position into a variable, array or user defined type.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MEMGET</a> <i>memoryBlock</i>, <i>bytePosition</i>, <i>destinationVariable</i></dd></dl>
<p>
</p>
<ul><li><i>memoryBlock</i> is a <a href="MEM" title="MEM">_MEM</a> variable type memory block name created by <a href="MEMNEW" title="MEMNEW">_MEMNEW</a> or the <a href="MEM_(function)" title="MEM (function)">_MEM</a> function.</li>
<li><i>bytePosition</i> is the <i>memoryBlock</i>.<a href="OFFSET" title="OFFSET">OFFSET</a> memory start position plus any bytes to move into the block.</li>
<li><i>destinationVariable</i> is the variable assigned to hold the data. The number of bytes read is determined by the variable <a href="Variable_Types" title="Variable Types">type</a> used.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <a class="mw-selflink selflink">_MEMGET</a> statement is similar to the <a href="GET" title="GET">GET</a> statement used in files, but the position is required.</li>
<li>The memory block name.<a href="OFFSET" title="OFFSET">OFFSET</a> returns the starting byte position of the block. Add bytes to move into the block.</li>
<li>The variable type held in the memory block can determine the next <i>bytePosition</i> to read.</li>
<li><a href="LEN" title="LEN">LEN</a> can be used to determine the byte size of numerical or user defined <a href="Variable_Types" title="Variable Types">Variable Types</a> regardless of the value held.</li>
<li><a href="STRING" title="STRING">STRING</a> values should be of a defined length. Variable length strings can actually move around in memory and not be found.</li></ul>
<p>
{{PageExamples
<i>Example:</i> Shows how to read the PSET color values from a program's <a href="SCREEN" title="SCREEN">SCREEN</a> memory to an array.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (0, 0), 123
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (1, 0), 222 'create screen image
'here is an array
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> screen_array(319, 199) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a> 'use screen dimensions from 0
'here's how we can copy the screen to our array
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
m = <a href="MEMIMAGE" title="MEMIMAGE"><span style="color:#4593D8;">_MEMIMAGE</span></a>  '0 or no handle necessary when accessing the current program screen
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMGET</span></a> m, m.OFFSET, screen_array()
'here's the proof
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> screen_array(0, 0) 'print 123
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> screen_array(1, 0) 'print 222
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li>
<li><a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="MEM" title="MEM">_MEM</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a></li>
<li><a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062402
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.038 seconds
Preprocessor visited node count: 155/1000000
Post‐expand include size: 1509/2097152 bytes
Template argument size: 249/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.935      1 -total
 14.57%    2.904     15 Template:Cl
 12.86%    2.564      8 Template:Parameter
 12.47%    2.486      1 Template:PageSyntax
 11.64%    2.321      1 Template:PageSeeAlso
 10.19%    2.032      1 Template:CodeStart
  9.93%    1.980      1 Template:CodeEnd
  9.43%    1.879      1 Template:PageDescription
  9.28%    1.850      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:181-0!canonical and timestamp 20240715062402 and revision id 8712.
 -->
</div>
</div>
</div>
</div>
</body>
</html>