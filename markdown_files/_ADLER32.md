<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ADLER32 - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ADLER32 rootpage-ADLER32 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ADLER32</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_ADLER32</b> function returns the <a class="extiw" href="https://en.wikipedia.org/wiki/Adler-32" title="wikipedia:Adler-32">Adler-32</a> checksum of any arbitrary string.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>chksum~&amp;</i> = <a class="mw-selflink selflink">_ADLER32</a>(<i>dataString$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>chksum~&amp;</i> is the <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> checksum returned (one (1), if the given <i>dataString$</i> was empty).</li>
<li><i>dataString$</i> is any literal or variable <a href="STRING" title="STRING">STRING</a> to build the checksum from.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <b>Adler-32</b> checksum uses a relative simple but very fast algorithm, it has the following known properties:
<ul><li>All single bit flips will be detected.</li>
<li>All double bit flips will be detected.</li>
<li>Burst errors up to seven bits are always detected.</li></ul></li>
<li>For more informations have a closer look at <a class="external text" href="https://www.intel.com/content/www/us/en/content-details/709921/intel-quickassist-technology-intel-qat-using-adler-32-checksum-and-crc32-hash-to-ensure-data-compression-integrity.html" rel="nofollow">Chapters 5-7 here</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.12.0"><img alt="v3.12.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.12.0</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Showing how the Adler-32 checksum can detect differences in two strings.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'this is the correct text</span>
t$ = <span style="color:#FFB100;">"QB64 Phoenix Edition"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Correct Text: "</span>; t$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Adler-32 Sum: "</span>; <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<span style="color:#FFB100;">"00000000"</span> + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_ADLER32</span></a>(t$)), <span style="color:#F580B1;">8</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<span style="color:#919191;">'this text differs in just 1 bit from the above, by changing 4 to 5</span>
<span style="color:#919191;">'ASC("4") = 52 = &amp;B00110100</span>
<span style="color:#919191;">'ASC("5") = 53 = &amp;B00110101</span>
t$ = <span style="color:#FFB100;">"QB65 Phoenix Edition"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Mangled Text: "</span>; t$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Adler-32 Sum: "</span>; <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<span style="color:#FFB100;">"00000000"</span> + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_ADLER32</span></a>(t$)), <span style="color:#F580B1;">8</span>)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Correct Text: QB64 Phoenix Edition
Adler-32 Sum: 41F806E5
Mangled Text: QB65 Phoenix Edition
Adler-32 Sum: 420906E6
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2681" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a>, <a href="INFLATE$" title="INFLATE$">_INFLATE$</a></li>
<li><a href="CRC32" title="CRC32">_CRC32</a>, <a href="MD5$" title="MD5$">_MD5$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062549
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.072 seconds
Real time usage: 0.108 seconds
Preprocessor visited node count: 283/1000000
Post‐expand include size: 2544/2097152 bytes
Template argument size: 704/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2645/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   85.410      1 -total
 13.94%   11.909      1 Template:PageNavigation
  6.66%    5.686      1 Template:PageSeeAlso
  4.71%    4.024     12 Template:Cl
  4.49%    3.831     14 Template:Text
  4.46%    3.809      1 Template:PageSyntax
  4.02%    3.436      1 Template:OutputEnd
  3.68%    3.141      1 Template:CodeEnd
  3.52%    3.010      1 Template:OutputStart
  3.24%    2.769      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1226-0!canonical and timestamp 20240715062549 and revision id 8942.
 -->
</div>
</div>
</div>
</div>
</body>
</html>