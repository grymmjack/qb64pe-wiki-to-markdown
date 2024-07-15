<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CLOSE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLOSE rootpage-CLOSE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CLOSE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>CLOSE</b> closes an open file or port using the number(s) assigned in an <a href="OPEN" title="OPEN">OPEN</a> statement.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CLOSE</a> [<i>fileNumber</i>[, ...</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fileNumber</i> indicates the file or list of file numbers to close. When not specified, all open files are closed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>A file must be closed when changing to another file mode.</li>
<li><a class="mw-selflink selflink">CLOSE</a> files when they are no longer needed, in order to save memory.</li>
<li>Files cannot be opened in the same <a href="OPEN" title="OPEN">OPEN</a> mode using another number until the first one is closed.</li>
<li>Use holding variables for each file number returned by <a href="FREEFILE" title="FREEFILE">FREEFILE</a> so that the file reference is known.</li>
<li>Will not return an error if a filenumber is already closed or was never opened. It does not verify that a file was closed.</li>
<li><a href="CLEAR" title="CLEAR">CLEAR</a> can be used to close all open files.</li>
<li><a class="mw-selflink selflink">CLOSE</a> can also be used to close an open TCP/IP or HTTP connection using a handle returned by <b>QB64</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPEN" title="OPEN">OPEN</a>, <a href="OPEN_COM" title="OPEN COM">OPEN COM</a></li>
<li><a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a>, <a href="OPENHOST" title="OPENHOST">_OPENHOST</a></li>
<li><a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a></li>
<li><a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192358
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.024 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 23/1000000
Post‐expand include size: 612/2097152 bytes
Template argument size: 20/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.740      1 -total
 20.49%    3.225      1 Template:PageDescription
 17.81%    2.804      1 Template:PageSeeAlso
 15.65%    2.463      1 Template:PageNavigation
 15.51%    2.441      1 Template:PageParameters
 14.12%    2.222      1 Template:PageSyntax
 11.91%    1.874      2 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:306-0!canonical and timestamp 20240714192358 and revision id 6572.
 -->
</div>
</div>
</div>
</div>
</body>
</html>