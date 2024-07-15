<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONNECTED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONNECTED rootpage-CONNECTED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONNECTED</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CONNECTED</a> function returns the status of a TCP/IP or HTTP connection handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result&amp;</i> = <a class="mw-selflink selflink">_CONNECTED</a>(<i>connectionHandle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The handle can come from the <a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCLIENT" title="OPENCLIENT">OPENCLIENT</a> or <a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a>.</li>
<li>Returns -1 if still connected or 0 if connection has ended/failed.</li>
<li>Do not rely solely on this function to check for ending communication.</li>
<li>Use "time-out" checking as well and <a href="CLOSE" title="CLOSE">CLOSE</a> any suspect connections.</li>
<li>If this function indicates the handle is not connected, any unread messages can still be read using <a href="GET_(TCP/IP_statement)" title="GET (TCP/IP statement)">GET #</a>.</li>
<li>Even if this function indicates the handle is not connected, it is important to <a href="CLOSE" title="CLOSE">CLOSE</a> the connection anyway or important resources cannot be reallocated.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a>, <a class="mw-redirect" href="CONNECTIONADDRESS$" title="CONNECTIONADDRESS$">_CONNECTIONADDRESS$</a></li>
<li><a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li>
<li><a href="Downloading_Files" title="Downloading Files">Downloading Files</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062259
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.020 seconds
Real time usage: 0.058 seconds
Preprocessor visited node count: 21/1000000
Post‐expand include size: 577/2097152 bytes
Template argument size: 24/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.653      1 -total
 29.93%    9.173      1 Template:PageSeeAlso
 24.62%    7.546      1 Template:PageNavigation
 16.41%    5.029      2 Template:Parameter
 15.77%    4.833      1 Template:PageSyntax
 11.58%    3.551      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:93-0!canonical and timestamp 20240715062259 and revision id 5912.
 -->
</div>
</div>
</div>
</div>
</body>
</html>