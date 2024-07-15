<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_READFILE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-READFILE rootpage-READFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_READFILE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_READFILE$</b> function returns the complete contents of a file in a single string, but without the usual overhead. It does <a href="OPEN" title="OPEN">OPEN</a>, <a href="GET" title="GET">GET</a> and <a href="CLOSE" title="CLOSE">CLOSE</a> the file in one run.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>contents$</i> = <a class="mw-selflink selflink">_READFILE$</a>(<i>fileSpec$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>contents$</i> is the entire file contents returned as <a href="STRING" title="STRING">STRING</a>. May return an empty string, if the specified file was empty, or if the program was continued from a file related <a href="ERROR_Codes" title="ERROR Codes">ERROR</a>.</li>
<li><i>fileSpec$</i> is the name of the file to read as literal or variable <a href="STRING" title="STRING">STRING</a>, if required inclusive a full or relative path.
<ul><li>To avoid errors you should use <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a> before calling this function to make sure the file exists.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Sometimes it's required or at least useful to have the whole contents of a file in a single string for further processing, e.g. to pass it to hashing or compression functions which expect strings.</li>
<li>In earlier versions of QB64(PE) you had to implement that loading process manually all the time or create a reusable custom <a href="FUNCTION" title="FUNCTION">FUNCTION</a> for it.</li>
<li>Now <b>_READFILE$</b> will simplify this, it's mainly a convenience function to wrap the following code sequence into one handy function:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">fh = <a href="FREEFILE" title="FREEFILE"><span style="color:blue;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:blue;">OPEN</span></a> fileSpec$ <a href="FOR" title="FOR"><span style="color:blue;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:blue;">BINARY</span></a> <a href="AS" title="AS"><span style="color:blue;">AS</span></a> #fh
contents$ = <a href="SPACE$" title="SPACE$"><span style="color:blue;">SPACE$</span></a>(<a href="LOF" title="LOF"><span style="color:blue;">LOF</span></a>(fh))
<a href="GET" title="GET"><span style="color:blue;">GET</span></a> #fh, , contents$
<a href="CLOSE" title="CLOSE"><span style="color:blue;">CLOSE</span></a> #fh
</pre>
</td></tr></tbody></table>
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
<dl><dt>Example 1</dt>
<dd>Showing that this function's result is equal to the code sequence shown above.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$COLOR" title="$COLOR"><span style="color:#55FF55;">$COLOR</span></a>:<span style="color:#F580B1;">0</span>
fileSpec$ = <span style="color:#FFB100;">"source\global\settings.bas"</span>
fh = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> fileSpec$ <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">BINARY</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #fh
content$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(fh))
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #fh, , content$
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #fh
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> LightGreen
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Using old manual load method..."</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> White
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> content$
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> LightGreen
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Using new direct load method..."</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> White
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_READFILE$</span></a>(fileSpec$)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Passing a whole file's contents to hashing functions.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$COLOR" title="$COLOR"><span style="color:#55FF55;">$COLOR</span></a>:<span style="color:#F580B1;">0</span>
fileSpec$ = <span style="color:#FFB100;">"source\global\settings.bas"</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> LightGreen
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"CRC32 of the file..."</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> White
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<span style="color:#FFB100;">"00000000"</span> + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(<a href="CRC32" title="CRC32"><span style="color:#4593D8;">_CRC32</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_READFILE$</span></a>(fileSpec$))), <span style="color:#F580B1;">8</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> LightGreen
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"MD5 of the file..."</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> White
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="MD5$" title="MD5$"><span style="color:#4593D8;">_MD5$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_READFILE$</span></a>(fileSpec$))
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2699" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="WRITEFILE" title="WRITEFILE">_WRITEFILE</a>, <a href="BLOAD" title="BLOAD">BLOAD</a>, <a href="BSAVE" title="BSAVE">BSAVE</a></li>
<li><a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a>, <a href="INFLATE$" title="INFLATE$">_INFLATE$</a></li>
<li><a href="ADLER32" title="ADLER32">_ADLER32</a>, <a href="CRC32" title="CRC32">_CRC32</a>, <a href="MD5$" title="MD5$">_MD5$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714145151
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.079 seconds
Real time usage: 0.109 seconds
Preprocessor visited node count: 482/1000000
Post‐expand include size: 4165/2097152 bytes
Template argument size: 890/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2545/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   84.193      1 -total
  6.40%    5.388      1 Template:PageAvailability
  6.40%    5.387      1 Template:PageExamples
  3.16%    2.661     35 Template:Cl
  2.90%    2.442      1 Template:PageSyntax
  2.74%    2.305      9 Template:Cb
  2.51%    2.114      4 Template:Parameter
  2.44%    2.053      1 Template:PageSeeAlso
  2.33%    1.961      1 Template:TextStart
  2.22%    1.869     10 Template:Text
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1231-0!canonical and timestamp 20240714145151 and revision id 8945.
 -->
</div>
</div>
</div>
</div>
</body>
</html>