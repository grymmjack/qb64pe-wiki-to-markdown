<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOF - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOF rootpage-LOF skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOF</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>LOF</b> function is used to find the length of an <a href="OPEN" title="OPEN">OPEN</a> file in bytes, or content length of an HTTP response.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>totalBytes&amp;</i> = <a class="mw-selflink selflink">LOF</a>([#]<i>fileNumber</i>)</dd>
<dd><i>totalBytes&amp;</i> = <a class="mw-selflink selflink">LOF</a>([#]<i>httpHandle</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>For regular <a href="OPEN" title="OPEN">OPENed</a> files:
<ul><li>LOF returns the number of bytes in an <a href="OPEN" title="OPEN">OPENed</a> designated <i>fileNumber</i>. File is empty if it returns 0.</li>
<li><i>fileNumber</i> is the number of the opened file. <b>#</b> is not required.</li>
<li>Often used to determine the number of records in a <a href="RANDOM" title="RANDOM">RANDOM</a> access file.</li>
<li>Can also be used to avoid reading an empty file, which would create an error.</li>
<li>LOF in <b>QB64</b> can return up to 9 GB (9,223,372,036 bytes) file sizes.</li></ul></li></ul>
<ul><li>For HTTP handles opened using <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a>:
<ul><li><a class="mw-selflink selflink">LOF</a> returns the length listed in the Content-Length header of the HTTP response.</li>
<li>If no Content-Length header was provided on the HTTP response, then <a class="mw-selflink selflink">LOF</a> return -1</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Finding the number of records in a RANDOM file using a <a href="TYPE" title="TYPE">TYPE</a> variable.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">  <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Type_variable)
  NumRecords% = <a class="mw-selflink selflink"><span style="color:#4593D8;">LOF</span></a>(1) \ RecordLEN%
</pre>
</td></tr></tbody></table>
<dl><dt>Example</dt>
<dd>Reading the Content length of an HTTP response</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#4593D8;">$UNSTABLE</span></a>:HTTP
h&amp; = <a href="OPENCLIENT" title="OPENCLIENT"><span style="color:#4593D8;">_OPENCLIENT</span></a>("HTTP:https://qb64phoenix.com")
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">LOF</span></a>(h&amp;)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LEN" title="LEN">LEN</a>, <a href="EOF" title="EOF">EOF</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a>, <a href="RANDOM" title="RANDOM">RANDOM</a>, <a href="TYPE" title="TYPE">TYPE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192503
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 119/1000000
Post‐expand include size: 1329/2097152 bytes
Template argument size: 144/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 23/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.520      1 -total
 12.91%    2.133      1 Template:PageSyntax
 11.97%    1.977     11 Template:Cl
 10.58%    1.748      4 Template:Parameter
  9.69%    1.601      1 Template:PageNavigation
  9.30%    1.536      1 Template:PageSeeAlso
  9.29%    1.535      1 Template:PageDescription
  9.27%    1.532      1 Template:PageExamples
  9.24%    1.526      2 Template:CodeStart
  9.12%    1.507      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:279-0!canonical and timestamp 20240714192503 and revision id 7593.
 -->
</div>
</div>
</div>
</div>
</body>
</html>