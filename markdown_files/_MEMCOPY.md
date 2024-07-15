<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMCOPY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMCOPY rootpage-MEMCOPY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMCOPY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMCOPY</a> statement copies a block of bytes from one memory offset to another offset in memory.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_MEMCOPY</a> <i>sourceBlock</i>, <i>sourceBlock.OFFSET</i>, <i>sourceBlock.SIZE</i> <a href="TO" title="TO">TO</a> <i>destBlock</i>, <i>destBlock.OFFSET</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>sourceBlock</i> is the source memory block name created AS <a href="MEM" title="MEM">_MEM</a>.</li>
<li><i>sourceBlock.OFFSET</i> is the dot <a href="OFFSET" title="OFFSET">_OFFSET</a> within the source memory block to read from.</li>
<li><i>sourceBlock.SIZE</i> is the total number of bytes to transfer based on actual size.</li>
<li><i>destBlock</i> is the destination <a href="MEM" title="MEM">_MEM</a> memory block name to transfer data to.</li>
<li><i>destBlock.OFFSET</i> is the dot <a href="OFFSET" title="OFFSET">_OFFSET</a> within the dest <a href="MEM" title="MEM">_MEM</a> memory block to write to.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The dot OFFSET is the memory block's start location in memory. Add bytes to place data further into the block.</li>
<li>The dot SIZE is the total byte size of the memory block to transfer. You can transfer all or a portion of the data bytes.</li>
<li>The memory block regions may overlap.</li>
<li><b>Always free memory blocks after values have been transferred to variables and are no longer required.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Swapping data from one <a href="STRING" title="STRING">STRING</a> variable to another. Fixed length strings are recommended for speed.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
m = <a href="MEMNEW" title="MEMNEW"><span style="color:#4593D8;">_MEMNEW</span></a>(10)
n = <a href="MEMNEW" title="MEMNEW"><span style="color:#4593D8;">_MEMNEW</span></a>(100)
<a href="MEMPUT" title="MEMPUT"><span style="color:#4593D8;">_MEMPUT</span></a> m, m.OFFSET, "1234567890"
s$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10) 'to load into a variable length string set its length first
<a href="MEMGET" title="MEMGET"><span style="color:#4593D8;">_MEMGET</span></a> m, m.OFFSET, s$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "in:[" + s$ + "]"
<a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMCOPY</span></a> m, m.OFFSET, m.SIZE <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> n, n.OFFSET 'put m into n
b$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10)
<a href="MEMGET" title="MEMGET"><span style="color:#4593D8;">_MEMGET</span></a> n, n.OFFSET, b$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "out:[" + b$ + "]"
<a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> m: <a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> n 'always clear the memory when done
</pre>
</td></tr></tbody></table>
<p>
<i>Snippet:</i> Instead of copying each array element, one at a time in nested <a href="FOR...NEXT" title="FOR...NEXT">FOR</a> loops, _MEMCOPY does it in one statement instantly.
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">'copy array a to array b one index at a time:
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:blue;">FOR</span></a> i1 = 0 <a href="TO" title="TO"><span style="color:blue;">TO</span></a> 100
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:blue;">FOR</span></a> i2 = 0 <a href="TO" title="TO"><span style="color:blue;">TO</span></a> 100
        b(i1, i2) = a(i1, i2)
    <a href="NEXT" title="NEXT"><span style="color:blue;">NEXT</span></a>
<a href="NEXT" title="NEXT"><span style="color:blue;">NEXT</span></a>
'copy array a to array b in memory instantly:
<a href="DIM" title="DIM"><span style="color:blue;">DIM</span></a> ma <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:blue;">_MEM</span></a>: ma = <a href="MEM_(function)" title="MEM (function)"><span style="color:blue;">_MEM</span></a>(a()) 'place array data into blocks
<a href="DIM" title="DIM"><span style="color:blue;">DIM</span></a> mb <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:blue;">_MEM</span></a>: mb = <a href="MEM_(function)" title="MEM (function)"><span style="color:blue;">_MEM</span></a>(b())
<a class="mw-selflink selflink"><span style="color:blue;">_MEMCOPY</span></a> ma, ma.OFFSET, ma.SIZE <a href="TO" title="TO"><span style="color:blue;">TO</span></a> mb, mb.OFFSET
<a href="MEMFREE" title="MEMFREE"><span style="color:blue;">_MEMFREE</span></a> ma: <a href="MEMFREE" title="MEMFREE"><span style="color:blue;">_MEMFREE</span></a> mb 'clear the memory when done
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a>, <a href="MEM_(function)" title="MEM (function)">_MEM (function)</a></li>
<li><a href="MEMNEW" title="MEMNEW">_MEMNEW</a>, <a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li>
<li><a href="MEMIMAGE" title="MEMIMAGE">_MEMIMAGE</a>, <a href="MEMELEMENT" title="MEMELEMENT">_MEMELEMENT</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="MEMFILL" title="MEMFILL">_MEMFILL</a>, <a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192745
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 328/1000000
Post‐expand include size: 2786/2097152 bytes
Template argument size: 518/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.202      1 -total
  9.01%    2.541      1 Template:PageSyntax
  8.54%    2.409     10 Template:Parameter
  8.27%    2.332     16 Template:Cb
  8.15%    2.298     21 Template:Cl
  7.56%    2.132      1 Template:PageNavigation
  7.28%    2.053      1 Template:PageSeeAlso
  7.09%    2.000      1 Template:TextEnd
  5.94%    1.675      1 Template:PageParameters
  5.60%    1.579      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:176-0!canonical and timestamp 20240714192745 and revision id 6461.
 -->
</div>
</div>
</div>
</div>
</body>
</html>