<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_FULLPATH$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FULLPATH rootpage-FULLPATH skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_FULLPATH$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_FULLPATH$</b> function returns an absolute or full path name for the specified relative path name.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>p$</i> = <a class="mw-selflink selflink">_FULLPATH$</a>(<i>pathName$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>pathname$</i> is the file or directory for which to obtain absolute path information.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The path returned ends with a backslash on Windows and a forward-slash on Linux and macOS if <i>pathname$</i> is a directory.</li>
<li>A nonexistent file or directory generates the error message, "Path Not Found.".</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.11.0"><img alt="v3.11.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.11.0</b>
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
<dd>Display the absolute path name of the parent directory.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Parent directory full path: "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_FULLPATH$</span></a>(<span style="color:#FFB100;">"../"</span>)
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2734" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="CWD$" title="CWD$">_CWD$</a>, <a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a></li>
<li><a href="FILES" title="FILES">FILES</a>, <a href="FILES$" title="FILES$">_FILES$</a></li>
<li><a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a>, <a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715002328
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.053 seconds
Real time usage: 0.075 seconds
Preprocessor visited node count: 77/1000000
Post‐expand include size: 1001/2097152 bytes
Template argument size: 123/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2406/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   61.499      1 -total
  8.67%    5.334      1 Template:PageAvailability
  8.08%    4.970      1 Template:PageExamples
  4.88%    3.004      1 Template:PageParameters
  4.41%    2.715      1 Template:PageSyntax
  3.50%    2.151      1 Template:PageDescription
  3.48%    2.139      2 Template:Parameter
  2.66%    1.635      1 Template:CodeStart
  2.51%    1.541      2 Template:Cl
  2.44%    1.501      2 Template:Text
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1224-0!canonical and timestamp 20240715002328 and revision id 8949.
 -->
</div>
</div>
</div>
</div>
</body>
</html>