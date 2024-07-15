<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OPENHOST - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPENHOST rootpage-OPENHOST skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OPENHOST</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_OPENHOST</a> function opens a Host which listens for new connections and returns a Host status handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>hostHandle</i> = <a class="mw-selflink selflink">_OPENHOST</a>(<b>"TCP/IP:8080"</b>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Creates an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call</a> error if called with a string argument of the wrong syntax.</li>
<li>The port used in the syntax example is 8080.</li>
<li>Valid <i>hostHandle</i> values are negative numbers.</li>
<li>If the syntax is correct but they fail to begin/connect a <i>hostHandle</i> of 0 is returned.</li>
<li>Always check if the handle returned is 0 (failed) before continuing.</li>
<li><a href="CLOSE" title="CLOSE">CLOSE</a> <i>hostHandle</i> closes the host. A failed handle value of 0 does not need to be closed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a>, <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li>
<li><a href="CONNECTED" title="CONNECTED">_CONNECTED</a>, <a href="CONNECTIONADDRESS" title="CONNECTIONADDRESS">_CONNECTIONADDRESS</a></li>
<li><a href="Email_Demo" title="Email Demo">Email Demo</a>, <a href="Inter-Program_Data_Sharing_Demo" title="Inter-Program Data Sharing Demo">Inter-Program Data Sharing Demo</a></li>
<li><a href="Downloading_Files" title="Downloading Files">Downloading Files</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211452
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.016 seconds
Real time usage: 0.021 seconds
Preprocessor visited node count: 29/1000000
Post‐expand include size: 601/2097152 bytes
Template argument size: 40/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.060      1 -total
 21.56%    2.169      1 Template:PageSyntax
 19.23%    1.935      4 Template:Parameter
 17.97%    1.808      1 Template:PageNavigation
 17.85%    1.796      1 Template:PageSeeAlso
 17.80%    1.791      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:207-0!canonical and timestamp 20240714211452 and revision id 7350.
 -->
</div>
</div>
</div>
</div>
</body>
</html>