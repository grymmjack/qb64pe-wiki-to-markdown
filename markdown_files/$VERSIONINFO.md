<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$VERSIONINFO - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_VERSIONINFO rootpage-_VERSIONINFO skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$VERSIONINFO</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">$VERSIONINFO</a> <a href="Metacommand" title="Metacommand">metacommand</a> adds text metadata to the resulting executable for identification purposes across the OS. Windows-only.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$VERSIONINFO</a>:<i>key</i>=<i>value</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Text <i>keys</i> can be: <b>Comments, CompanyName, FileDescription, FileVersion, InternalName, LegalCopyright, LegalTrademarks, OriginalFilename, ProductName, ProductVersion, Web</b></li>
<li>Numeric <i>keys</i> can be:<b>FILEVERSION#</b> and <b>PRODUCTVERSION#</b>
<ul><li>When provided, the numerical keys <b>FILEVERSION#</b> and <b>PRODUCTVERSION#</b> will also provide values to the text keys <b>FileVersion</b> and <b>ProductVersion,</b> if the text versions are not provided separately. (QB64-PE v0.6.0 and up)</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Text and numerical values are string literals without quotes entered by programmer. <b>No variables are accepted.</b> (variable names would be interpreted as literals).</li>
<li>Numeric key=<i>value</i> must be 4 comma-separated numerical text values entered by programmer which usually stand for major, minor, revision and build numbers).</li>
<li>A manifest file is automatically embedded into the resulting .exe file so that Common Controls v6.0 gets linked at runtime, if required.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="no"><img alt="no" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>no</b>
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
<p><i>Example:</i> Adding metadata to a Windows exe compiled with QB64:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">$VERSIONINFO</span></a>:CompanyName=Your company name goes here
<a class="mw-selflink selflink"><span style="color:#4593D8;">$VERSIONINFO</span></a>:FILEVERSION#=1,0,0,0
<a class="mw-selflink selflink"><span style="color:#4593D8;">$VERSIONINFO</span></a>:PRODUCTVERSION#=1,0,0,0
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$EXEICON" title="$EXEICON">$EXEICON</a></li>
<li><a href="ICON" title="ICON">_ICON</a></li>
<li><a class="external text" href="https://msdn.microsoft.com/library/windows/desktop/aa381058(v=vs.85).aspx" rel="nofollow">VERSIONINFO resource (MSDN)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192335
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.057 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 67/1000000
Post‐expand include size: 949/2097152 bytes
Template argument size: 84/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2353/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   63.747      1 -total
  6.09%    3.883      1 Template:PageAvailability
  5.16%    3.287      1 Template:PageParameters
  4.63%    2.952      3 Template:Parameter
  4.36%    2.778      1 Template:PageSyntax
  3.61%    2.304      1 Template:PageExamples
  2.88%    1.834      3 Template:Cl
  2.67%    1.704      1 Template:PageDescription
  2.65%    1.687      1 Template:CodeStart
  2.47%    1.572      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:361-0!canonical and timestamp 20240714192335 and revision id 7744.
 -->
</div>
</div>
</div>
</div>
</body>
</html>