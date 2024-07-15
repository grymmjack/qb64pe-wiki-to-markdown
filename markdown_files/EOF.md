<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>EOF - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-EOF rootpage-EOF skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">EOF</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>EOF</b> function indicates that the end of a file or HTTP response has been reached.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>endReached%%</i> =  <a class="mw-selflink selflink">EOF</a>([#]<i>fileNumber&amp;</i>)</dd>
<dd><i>endReached%%</i> =  <a class="mw-selflink selflink">EOF</a>([#]<i>httpHandle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileNumber&amp;</i> or <i>httpHandle&amp;</i> is the number of the file or HTTP connected being read. <b>#</b> is not required.
<ul><li><i>fileNumber&amp;</i> is a file opened using <a href="OPEN" title="OPEN">OPEN</a>.</li>
<li><i>httpHandle&amp;</i> is a HTTP connection opened using <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a>.</li></ul></li>
<li>Returns 0 until the end of a file. This avoids a file read error.</li>
<li>Returns -1 (true) at the end of the file.</li></ul>
<h3><span class="mw-headline" id="Notes">Notes</span></h3>
<ul><li>In files opened with the <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)">INPUT (file mode)</a> the <b>EOF</b> function returns <b>true</b> after any used input function reads a <a href="CHR$" title="CHR$">CHR$</a>(26) (Ctrl-Z) from the file, which denotes the "logical" end of a file. This is not necessarily equal to the "physical" end.
<ul><li>Although this subtle behavior is not required nowadays, it is still here for the sake of compatibility. If you're interested in the historic cause of it see <a class="external text" href="https://devblogs.microsoft.com/oldnewthing/20040316-00/?p=40233" rel="nofollow">this Article</a>.</li>
<li>To be able to read those files completely use the <a class="mw-redirect" href="BINARY" title="BINARY">BINARY (file mode)</a> instead, which is also much faster when used in conjunction with the regular <a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT</a>, <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT</a> and <a href="INPUT$" title="INPUT$">INPUT$</a> functions.</li></ul></li>
<li><a href="GET" title="GET">GET</a> can return invalid data at the end of a file. Read <b>EOF</b> after a <a href="GET" title="GET">GET</a> operation to see if the end of the file has been reached and discard the last read if required.
<ul><li>This is not a problem when using <a href="GET" title="GET">GET</a> with HTTP connections with a variable length string, the string will always only contain valid data or be empty.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Showing the difference between INPUT and BINARY file modes when Ctrl-Z is involved.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'Write a simple test file with Ctrl-Z in the middle.
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "test.txt" <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> #1, "Hello"; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(26); "World!"
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
'Now read it back, but uhh, this gives us the "Hello"
'only because of the Ctrl-Z.
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "test.txt" <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">EOF</span></a>(1)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1, 1);
<a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
'However, it works in the BINARY file mode.
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "test.txt" <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">EOF</span></a>(1)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1, 1);
<a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello
Hello→World!
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPEN" title="OPEN">OPEN</a></li>
<li><a href="LOF" title="LOF">LOF</a>, <a href="LEN" title="LEN">LEN</a></li>
<li><a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT (file statement)</a></li>
<li><a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)">LINE INPUT (file statement)</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714155612
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.036 seconds
Preprocessor visited node count: 300/1000000
Post‐expand include size: 2374/2097152 bytes
Template argument size: 350/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.065      1 -total
 12.67%    2.416     31 Template:Cl
  9.89%    1.886      1 Template:PageSyntax
  8.89%    1.696      8 Template:Parameter
  7.26%    1.384      1 Template:PageDescription
  7.21%    1.374      1 Template:CodeStart
  7.20%    1.373      1 Template:CodeEnd
  7.18%    1.369      1 Template:PageNavigation
  7.08%    1.349      1 Template:PageExamples
  7.07%    1.348      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:464-0!canonical and timestamp 20240714155612 and revision id 7205.
 -->
</div>
</div>
</div>
</div>
</body>
</html>