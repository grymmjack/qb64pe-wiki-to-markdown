<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_INFLATE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INFLATE rootpage-INFLATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_INFLATE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_INFLATE$</a> function decompresses a <a href="STRING" title="STRING">string</a> compressed by the <a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_INFLATE$</a>(<i>stringToDecompress$[, originalSize&amp;]</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>result$</i> will contain the original version of <i>stringToDecompress$</i>.</li>
<li>Optional parameter <i>originalSize&amp;</i> can be used if the original size of the uncompressed data is known beforehand, which makes the decompression routine run more efficiently.
<ul><li>If unspecified, decompression still works as expected, but may use more steps and need to allocate more memory internally.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.4 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Compressing a long string of text.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a$ = "The quick brown fox jumps over the lazy dog. "
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Original string (a$): "; a$
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15
    a$ = a$ + a$
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "After concatenating it into itself several times, LEN(a$) ="; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$)
b$ = <a href="DEFLATE$" title="DEFLATE$"><span style="color:#4593D8;">_DEFLATE$</span></a>(a$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "After using _DEFLATE$ to compress it, LEN ="; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(b$)
<a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> "(compressed size is #.###% of the original)"; ((<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(b$) * 100) / <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$))
c$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_INFLATE$</span></a>(b$)
PRINT "After using _INFLATE$ to decompress it, LEN ="; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(c$)
 </pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Original string (a$): The quick brown fox jumps over the lazy dog
After concatenating it into itself several times, LEN(a$) = 1474560
After using _DEFLATE$ to compress it, LEN = 4335
(compressed size is 0.295% of the original)
After using _INFLATE$ to decompress it, LEN = 1474560
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062553
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.090 seconds
Preprocessor visited node count: 147/1000000
Post‐expand include size: 1574/2097152 bytes
Template argument size: 218/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   68.240      1 -total
 26.90%   18.358      1 Template:OutputEnd
 18.10%   12.354      1 Template:CodeStart
  7.40%    5.051     14 Template:Cl
  6.84%    4.665      1 Template:CodeEnd
  6.20%    4.230      1 Template:PageSeeAlso
  4.54%    3.099      5 Template:Parameter
  4.53%    3.092      1 Template:PageSyntax
  4.47%    3.048      1 Template:PageDescription
  4.05%    2.764      1 Template:PageAvailability
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:158-0!canonical and timestamp 20240715062553 and revision id 7312.
 -->
</div>
</div>
</div>
</div>
</body>
</html>