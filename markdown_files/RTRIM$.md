<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RTRIM$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RTRIM rootpage-RTRIM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RTRIM$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">RTRIM$</a> function removes trailing space characters from a <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>return$</i> = <a class="mw-selflink selflink">RTRIM$</a>(<i>value$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>value$</i> is the <a href="STRING" title="STRING">STRING</a> value to trim.</li>
<li>If <i>value$</i> contains no trailing space characters, <i>value$</i> is returned unchanged.</li>
<li>Convert fixed length <a href="STRING" title="STRING">STRING</a> values by using a different <i>return$</i> variable.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p>Trimming a fixed length string value for use by another string variable:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">name$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">RTRIM$</span></a>(contact.name) ' trims spaces from end of fixed length <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> value.
</pre>
</td></tr></tbody></table>
<p>Trimming text string ends:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RTRIM$</span></a>("some text") + "."
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RTRIM$</span></a>("some text   ") + "."
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RTRIM$</span></a>("Tommy    ")
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">some text.
some text.
Tommy
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1246" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="TRIM$" title="TRIM$">_TRIM$</a>, <a href="LTRIM$" title="LTRIM$">LTRIM$</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="LSET" title="LSET">LSET</a>, <a href="RSET" title="RSET">RSET</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061412
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 108/1000000
Post‐expand include size: 1265/2097152 bytes
Template argument size: 124/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.668      1 -total
 15.57%    4.930      6 Template:Parameter
 15.33%    4.856      1 Template:PageDescription
  8.84%    2.800      1 Template:PageSyntax
  8.81%    2.790      8 Template:Cl
  7.04%    2.230      1 Template:PageExamples
  6.99%    2.214      1 Template:OutputStart
  6.93%    2.195      2 Template:CodeEnd
  6.87%    2.175      2 Template:CodeStart
  5.88%    1.863      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:263-0!canonical and timestamp 20240715061412 and revision id 8911.
 -->
</div>
</div>
</div>
</div>
</body>
</html>