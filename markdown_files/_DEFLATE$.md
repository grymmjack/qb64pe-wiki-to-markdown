<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DEFLATE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DEFLATE rootpage-DEFLATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DEFLATE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_DEFLATE$</a> function compresses a <a href="STRING" title="STRING">string</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_DEFLATE$</a>(<i>stringToCompress$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>result$</i> will contain the compressed version of <i>stringToCompress$</i>.</li>
<li>To decompress the resulting string, use <a href="INFLATE$" title="INFLATE$">_INFLATE$</a>.</li></ul>
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
<td><pre class="codeide">a$ = <span style="color:#FFB100;">"The quick brown fox jumps over the lazy dog. "</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Original string (a$): "</span>; a$
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
    a$ = a$ + a$
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"After concatenating it into itself several times, LEN(a$) ="</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$)
b$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_DEFLATE$</span></a>(a$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"After using _DEFLATE$ to compress it, LEN ="</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(b$)
<a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> <span style="color:#FFB100;">"(compressed size is #.###% of the original)"</span>; ((<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(b$) * <span style="color:#F580B1;">100</span>) / <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$))
c$ = <a href="INFLATE$" title="INFLATE$"><span style="color:#4593D8;">_INFLATE$</span></a>(b$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"After using _INFLATE$ to decompress it, LEN ="</span>; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(c$)
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
<ul><li><a href="INFLATE$" title="INFLATE$">_INFLATE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062552
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.042 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 231/1000000
Post‐expand include size: 2121/2097152 bytes
Template argument size: 467/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 269/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.241      1 -total
  7.87%    2.616      9 Template:Text
  7.59%    2.524      1 Template:PageSyntax
  7.53%    2.503     15 Template:Cl
  7.20%    2.395      4 Template:Parameter
  7.04%    2.339      1 Template:CodeStart
  6.96%    2.313      1 Template:PageExamples
  6.93%    2.303      1 Template:CodeEnd
  6.82%    2.266      1 Template:PageAvailability
  6.71%    2.231      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:111-0!canonical and timestamp 20240715062552 and revision id 8304.
 -->
</div>
</div>
</div>
</div>
</body>
</html>