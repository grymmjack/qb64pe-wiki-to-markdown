<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_WINDOWHASFOCUS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WINDOWHASFOCUS rootpage-WINDOWHASFOCUS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_WINDOWHASFOCUS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_WINDOWHASFOCUS</a> function returns true (-1) if the current program's window has focus. Not supported for macOS.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>hasFocus%%</i> = <a class="mw-selflink selflink">_WINDOWHASFOCUS</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns true (-1) if the current program is the topmost window on the user's desktop and has focus. If the current program is running behind another window, the function returns false (0).</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.2"><img alt="v1.2" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.2</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="no"><img alt="no" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>no</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Detecting if the current program has focus. Windows and Linux-only.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_WINDOWHASFOCUS</span></a> THEN
        <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 15, 6
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "*** Hi there! ***"
    <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
        <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 0, 7
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "(ain't nobody looking...)"
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The program will display <i>"*** Hi There! ***"</i> while the window is the topmost and is being manipulated by the user. If another window, the taskbar or the desktop are clicked, the program window loses focus and the message <i>"(ain't nobody looking...)"</i> is displayed.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1084" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="WINDOWHANDLE" title="WINDOWHANDLE">_WINDOWHANDLE</a></li>
<li><a href="SCREENEXISTS" title="SCREENEXISTS">_SCREENEXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192923
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 134/1000000
Post‐expand include size: 1425/2097152 bytes
Template argument size: 156/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2356/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   35.637      1 -total
  8.45%    3.010     14 Template:Cl
  6.62%    2.358      1 Template:PageExamples
  6.01%    2.141      1 Template:PageSyntax
  5.77%    2.055      1 Template:CodeEnd
  5.45%    1.941      1 Template:Parameter
  5.20%    1.855      1 Template:CodeStart
  5.00%    1.783      1 Template:PageDescription
  4.97%    1.772      1 Template:PageSeeAlso
  4.91%    1.748      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:366-0!canonical and timestamp 20240714192923 and revision id 8885.
 -->
</div>
</div>
</div>
</div>
</body>
</html>