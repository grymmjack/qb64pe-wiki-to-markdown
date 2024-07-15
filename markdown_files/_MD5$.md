<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MD5$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MD5 rootpage-MD5 skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MD5$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_MD5$</b> function returns the <a class="extiw" href="https://en.wikipedia.org/wiki/MD5" title="wikipedia:MD5">MD5</a> hash value of any arbitrary string.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>md5hash$</i> = <a class="mw-selflink selflink">_MD5$</a>(<i>dataString$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>md5hash$</i> is the hash value returned as hexadecimal <a href="STRING" title="STRING">STRING</a>, if the given <i>dataString$</i> was empty the unusual but absolutely correct hash value is:
<ul><li>D41D8CD98F00B204E9800998ECF8427E</li></ul></li>
<li><i>dataString$</i> is any literal or variable <a href="STRING" title="STRING">STRING</a> to build the hash value from.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>MD5 can be used as a checksum to verify data integrity against unintentional corruption.</li>
<li>Historically it was widely used as a cryptographic hash function, however it has been found to suffer from extensive vulnerabilities.</li>
<li>It remains suitable for other non-cryptographic purposes and may be preferred due to lower computational requirements than more recent Secure Hash Algorithms.</li></ul>
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
<dd>Showing how the MD5 hash value can detect differences in two strings.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'this is the correct text</span>
t$ = <span style="color:#FFB100;">"QB64 Phoenix Edition"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Correct Text: "</span>; t$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    MD5 hash: "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_MD5$</span></a>(t$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<span style="color:#919191;">'this text differs in just 1 bit from the above, by changing 4 to 5</span>
<span style="color:#919191;">'ASC("4") = 52 = &amp;B00110100</span>
<span style="color:#919191;">'ASC("5") = 53 = &amp;B00110101</span>
t$ = <span style="color:#FFB100;">"QB65 Phoenix Edition"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Mangled Text: "</span>; t$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"    MD5 hash: "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_MD5$</span></a>(t$)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Correct Text: QB64 Phoenix Edition
    MD5 hash: E512ECA19E9487D7C2F564E848314238
Mangled Text: QB65 Phoenix Edition
    MD5 hash: 3EF03E7B0DB46F7D1FA6B9626563C10B
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2681" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a>, <a href="INFLATE$" title="INFLATE$">_INFLATE$</a></li>
<li><a href="ADLER32" title="ADLER32">_ADLER32</a>, <a href="CRC32" title="CRC32">_CRC32</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062551
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.082 seconds
Real time usage: 0.123 seconds
Preprocessor visited node count: 221/1000000
Post‐expand include size: 2114/2097152 bytes
Template argument size: 554/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2625/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   88.457      1 -total
  8.64%    7.639      1 Template:PageExamples
  8.00%    7.073      1 Template:PageParameters
  4.57%    4.047     10 Template:Text
  4.21%    3.723      8 Template:Cl
  3.78%    3.347      1 Template:PageSyntax
  3.60%    3.185      1 Template:PageDescription
  3.52%    3.115      1 Template:PageNavigation
  3.49%    3.087      1 Template:PageAvailability
  3.45%    3.051      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1228-0!canonical and timestamp 20240715062551 and revision id 8944.
 -->
</div>
</div>
</div>
</div>
</body>
</html>