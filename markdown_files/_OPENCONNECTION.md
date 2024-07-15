<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OPENCONNECTION - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPENCONNECTION rootpage-OPENCONNECTION skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OPENCONNECTION</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_OPENCONNECTION</a> function opens a connection from a client that the host has detected and returns a status handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>connectHandle</i> = <a class="mw-selflink selflink">_OPENCONNECTION</a>(<i>hostHandle</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Valid <i>connectHandle</i> values returned are negative numbers.</li>
<li>If the syntax is correct but they fail to begin/connect, a <i>connectHandle</i> of 0 is returned.</li>
<li>Always check if the handle returned is 0 (failed) before continuing.</li>
<li><a href="CLOSE" title="CLOSE">CLOSE</a> #<i>connectHandle</i> closes the connection. Failed connections(<i>connectHandle</i> = 0) do not need to be closed.</li>
<li>As a <b>Host</b> you can check for new clients (users). Each will have a unique connection handle.</li>
<li>Creates an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call</a> error if called with a string argument of the wrong syntax.</li>
<li>Handle values can be used as the open number by <a href="GET_(TCP/IP_statement)" title="GET (TCP/IP statement)">GET #</a> read statement and <a href="PUT_(TCP/IP_statement)" title="PUT (TCP/IP statement)">PUT #</a> write statement.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li>
<li><a href="CONNECTED" title="CONNECTED">_CONNECTED</a>, <a href="CONNECTIONADDRESS" title="CONNECTIONADDRESS">_CONNECTIONADDRESS</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715044633
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.054 seconds
Preprocessor visited node count: 37/1000000
Post‐expand include size: 644/2097152 bytes
Template argument size: 75/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   36.492      1 -total
 38.08%   13.897      1 Template:PageSyntax
 23.93%    8.732      6 Template:Parameter
 14.39%    5.252      1 Template:PageDescription
 12.45%    4.544      1 Template:PageSeeAlso
  8.35%    3.048      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:206-0!canonical and timestamp 20240715044633 and revision id 6141.
 -->
</div>
</div>
</div>
</div>
</body>
</html>