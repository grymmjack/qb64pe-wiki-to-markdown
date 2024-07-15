<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$EXEICON - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_EXEICON rootpage-_EXEICON skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$EXEICON</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>$EXEICON</b> pre-compiler  metacommand embeds a designated icon file into the compiled EXE file to be viewed in Windows Explorer.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$EXEICON</a><b>:</b>'<i>iconfile.ico</i>'</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><b>iconfile.ico</b> is a valid <a class="extiw" href="https://en.wikipedia.org/wiki/ICO_(file_format)" title="wikipedia:ICO (file format)">ICO file</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Calling <a href="ICON" title="ICON">_ICON</a> without an <i>imageHandle&amp;</i> uses the embeded icon, if available.
<ul><li>Starting with <b>build 20170906/64</b>, the window will automatically use the icon embedded by <a class="mw-selflink selflink">$EXEICON</a>, without having to call _ICON.</li></ul></li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Embeds a designated icon file into the compiled EXE which can be viewed in Windows Explorer folders.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$EXEICON</span></a>:<span style="color:#919191;">'mush.ico'</span>
<a href="ICON" title="ICON"><span style="color:#4593D8;">_ICON</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ICON" title="ICON">_ICON</a></li>
<li><a href="TITLE" title="TITLE">_TITLE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061214
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 64/1000000
Post‐expand include size: 1059/2097152 bytes
Template argument size: 126/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 10/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.884      1 -total
 11.78%    3.992      1 Template:Small
  9.26%    3.139      1 Template:PageParameters
  8.59%    2.912      1 Template:PageNavigation
  8.33%    2.822      1 Template:PageSyntax
  7.20%    2.441      1 Template:PageSeeAlso
  6.86%    2.325      1 Template:Cm
  6.43%    2.178      1 Template:CodeStart
  6.39%    2.165      3 Template:Parameter
  6.35%    2.153      1 Template:Text
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:134-0!canonical and timestamp 20240715061214 and revision id 8976.
 -->
</div>
</div>
</div>
</div>
</body>
</html>