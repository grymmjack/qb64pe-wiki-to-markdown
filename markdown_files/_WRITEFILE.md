<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_WRITEFILE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WRITEFILE rootpage-WRITEFILE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_WRITEFILE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_WRITEFILE</b> statement writes a string into a new file, overwriting an existing file of the same name. It does <a href="OPEN" title="OPEN">OPEN</a>, <a href="PUT" title="PUT">PUT</a> and <a href="CLOSE" title="CLOSE">CLOSE</a> the file in one run. It's the counterpart to the <a href="READFILE$" title="READFILE$">_READFILE$</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_WRITEFILE</a> <i>fileSpec$</i>, <i>contents$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fileSpec$</i> is the name of the file to write as literal or variable <a href="STRING" title="STRING">STRING</a>, if required inclusive a full or relative path.
<ul><li>To avoid errors you should use <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a> before using this statement to make sure a desired path exists.</li></ul></li>
<li><i>contents$</i> is the literal or variable <a href="STRING" title="STRING">STRING</a> which its contents shall be written into the file.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Sometimes you may be in need to quickly dump a huge amount of data into a file without much fuss, e.g. the results of the pack/unpack functions <a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a> and <a href="INFLATE$" title="INFLATE$">_INFLATE$</a> or when copying a file in conjunction with the <a href="READFILE$" title="READFILE$">_READFILE$</a> function.</li>
<li>In earlier versions of QB64(PE) you had to implement that saving process manually all the time or create a reusable custom <a href="FUNCTION" title="FUNCTION">FUNCTION</a> for it.</li>
<li>Now <b>_WRITEFILE</b> will simplify this, it's mainly for convenience to wrap the following code sequence into one handy statement:</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">fh = <a href="FREEFILE" title="FREEFILE"><span style="color:blue;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:blue;">OPEN</span></a> fileSpec$ <a href="FOR" title="FOR"><span style="color:blue;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:blue;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:blue;">AS</span></a> #fh: <a href="CLOSE" title="CLOSE"><span style="color:blue;">CLOSE</span></a> #fh
<a href="OPEN" title="OPEN"><span style="color:blue;">OPEN</span></a> fileSpec$ <a href="FOR" title="FOR"><span style="color:blue;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:blue;">BINARY</span></a> <a href="AS" title="AS"><span style="color:blue;">AS</span></a> #fh
<a href="PUT" title="PUT"><span style="color:blue;">PUT</span></a> #fh, , contents$
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
<dl><dt>Example</dt>
<dd>Implementing a simple file copy routine using <b>_READFILE$</b> and <b>_WRITEFILE</b>.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">s$ = <span style="color:#FFB100;">"Makefile"</span>
d$ = <span style="color:#FFB100;">"Makefile - Copy"</span>
r$ = <span style="color:#55FF55;">CopyFile$</span>(s$, d$)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> r$ = <span style="color:#FFB100;">""</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Sucessfully copied '"</span>; s$; <span style="color:#FFB100;">"' to '"</span>; d$; <span style="color:#FFB100;">"'."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> r$
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">CopyFile$</span> (src$, dst$)
    <span style="color:#55FF55;">CopyFile$</span> = <span style="color:#FFB100;">""</span> <span style="color:#919191;">'empty = success, otherwise error message</span>
    buffer$ = <a href="READFILE$" title="READFILE$"><span style="color:#4593D8;">_READFILE$</span></a>(src$)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> buffer$ = <span style="color:#FFB100;">""</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="FILEEXISTS" title="FILEEXISTS"><span style="color:#4593D8;">_FILEEXISTS</span></a>(src$) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <span style="color:#55FF55;">CopyFile$</span> = <span style="color:#FFB100;">"ERROR: Source file not found."</span>
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        slp% = <a href="INSTRREV" title="INSTRREV"><span style="color:#4593D8;">_INSTRREV</span></a>(dst$, <span style="color:#FFB100;">"\"</span>)
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> slp% = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> slp% = <a href="INSTRREV" title="INSTRREV"><span style="color:#4593D8;">_INSTRREV</span></a>(dst$, <span style="color:#FFB100;">"/"</span>)
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> slp% &gt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="DIREXISTS" title="DIREXISTS"><span style="color:#4593D8;">_DIREXISTS</span></a>(<a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(dst$, slp% - <span style="color:#F580B1;">1</span>)) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                <span style="color:#55FF55;">CopyFile$</span> = <span style="color:#FFB100;">"ERROR: Destination path not found."</span>
                <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_WRITEFILE</span></a> dst$, buffer$
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2713" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="READFILE$" title="READFILE$">_READFILE$</a>, <a href="BLOAD" title="BLOAD">BLOAD</a>, <a href="BSAVE" title="BSAVE">BSAVE</a></li>
<li><a href="DEFLATE$" title="DEFLATE$">_DEFLATE$</a>, <a href="INFLATE$" title="INFLATE$">_INFLATE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714150401
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.074 seconds
Real time usage: 0.103 seconds
Preprocessor visited node count: 555/1000000
Post‐expand include size: 4470/2097152 bytes
Template argument size: 1168/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2552/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   57.686      1 -total
  6.82%    3.933     31 Template:Cl
  5.80%    3.343     22 Template:Text
  4.07%    2.345      1 Template:CodeEnd
  4.00%    2.308      1 Template:PageExamples
  3.87%    2.230      1 Template:PageSyntax
  3.80%    2.195     12 Template:Cb
  3.67%    2.118      1 Template:Small
  3.46%    1.996      1 Template:PageNavigation
  3.44%    1.986      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1232-0!canonical and timestamp 20240714150401 and revision id 8946.
 -->
</div>
</div>
</div>
</div>
</body>
</html>