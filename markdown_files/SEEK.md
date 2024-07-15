<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SEEK - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SEEK rootpage-SEEK skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SEEK</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>SEEK</b> statement sets the byte or record position in a file for the next read or write.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SEEK</a> <i>filenumber&amp;</i>, <i>position</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>filenumber&amp;</i> must be the file number that is <a href="OPEN" title="OPEN">OPEN</a> and being read or written to.</li>
<li><i>position</i> is a byte in <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> or sequencial files created in <a class="mw-redirect" href="OUTPUT" title="OUTPUT">OUTPUT</a>, <a class="mw-redirect" href="APPEND" title="APPEND">APPEND</a> or <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)">INPUT</a> modes. The first byte = 1.</li>
<li><i>position</i> is the record in <a href="RANDOM" title="RANDOM">RANDOM</a> files to read or write. Records can hold more than one variable defined in a <a href="TYPE" title="TYPE">TYPE</a>.</li>
<li>Since the first <b>SEEK</b> file position is 1 it may require adding one to an offset value when documentation uses that position as 0.</li>
<li>After a <b>SEEK</b> statement, the next file operation starts at that <b>SEEK</b> byte position.</li>
<li>The <b>SEEK</b> statement can work with the <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a> to move around in a file.</li></ul>
<h3><span class="mw-headline" id="Notes">Notes</span></h3>
<ul><li>Don't confuse the <a href="LOC" title="LOC">LOC</a> position with the <a href="SEEK_(function)" title="SEEK (function)">SEEK</a> position !!
<ul><li><b>LOC</b> is the <span style="color:red;">last</span> read or written byte or record prosition.</li>
<li><b>SEEK</b> is the byte or record prosition to read or write <span style="color:red;">next</span>.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>A <b>SEEK</b> statement using the <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a> to move to the next random record in a file.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">SEEK</span></a> 1, <a href="SEEK_(function)" title="SEEK (function)"><span style="color:#4593D8;">SEEK</span></a>(1) + 1
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Demonstrate the difference between <b>LOC</b> and <b>SEEK</b> positions in a file.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">OPEN "readme.md" FOR BINARY AS #1
PRINT LOC(1) 'LOC returns 0, as we didn't read something yet
PRINT SEEK(1) 'SEEK otherwise returns 1, as it's the first byte to read
GET #1, , a&amp; 'now let's read a LONG (4 bytes)
PRINT LOC(1) 'now LOC returns 4, the last read byte
PRINT SEEK(1) 'and SEEK returns 5 now, the next byte to read
CLOSE #1
END
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">0
1
4
5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a>, <a href="LOC" title="LOC">LOC</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061414
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 101/1000000
Post‐expand include size: 1035/2097152 bytes
Template argument size: 87/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.946      1 -total
  9.81%    2.939      2 Template:Text
  9.38%    2.808      1 Template:PageSyntax
  9.03%    2.704      5 Template:Parameter
  8.13%    2.434      2 Template:Cl
  7.79%    2.332      2 Template:CodeStart
  7.69%    2.302      1 Template:PageExamples
  7.33%    2.196      1 Template:PageParameters
  6.87%    2.058      1 Template:OutputEnd
  6.83%    2.045      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:282-0!canonical and timestamp 20240715061414 and revision id 8105.
 -->
</div>
</div>
</div>
</div>
</body>
</html>