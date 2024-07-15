<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_TOTALDROPPEDFILES - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TOTALDROPPEDFILES rootpage-TOTALDROPPEDFILES skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_TOTALDROPPEDFILES</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_TOTALDROPPEDFILES</a> function returns the number of items (files or folders) dropped in a program's window after <a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a> is enabled.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>totalFilesReceived&amp;</i> = <a class="mw-selflink selflink">_TOTALDROPPEDFILES</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>After <a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a> is enabled, <a class="mw-selflink selflink">_TOTALDROPPEDFILES</a> will return 0 until the user drops files or folders into the program's window.</li>
<li>When using <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> to read the list sequentially, <a class="mw-selflink selflink">_TOTALDROPPEDFILES</a> will be reset to 0 after the last item is retrieved (after <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> returns an empty string "").</li>
<li>If using <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> with an index, you must call <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a> after you finish working with the list.</li>
<li>When using <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a> to read the list with an index, <a class="mw-selflink selflink">_TOTALDROPPEDFILES</a> will <b>not</b> be reset (and the list of items won't be cleared) until <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a> is called.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.3 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See example for <a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ACCEPTFILEDROP" title="ACCEPTFILEDROP">_ACCEPTFILEDROP</a>, <a href="DROPPEDFILE" title="DROPPEDFILE">_DROPPEDFILE</a>, <a href="FINISHDROP" title="FINISHDROP">_FINISHDROP</a></li>
<li><a href="FILEEXISTS" title="FILEEXISTS">_FILEEXISTS</a>, <a href="DIREXISTS" title="DIREXISTS">_DIREXISTS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062544
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 23/1000000
Post‐expand include size: 646/2097152 bytes
Template argument size: 19/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.556      1 -total
 36.22%   12.154      1 Template:PageDescription
 12.33%    4.136      1 Template:PageSyntax
 10.95%    3.674      1 Template:PageAvailability
 10.24%    3.436      1 Template:PageNavigation
  9.90%    3.322      1 Template:PageSeeAlso
  9.56%    3.209      1 Template:Parameter
  7.64%    2.562      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:359-0!canonical and timestamp 20240715062544 and revision id 7452.
 -->
</div>
</div>
</div>
</div>
</body>
</html>