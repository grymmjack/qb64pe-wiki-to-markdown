<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_STATUSCODE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STATUSCODE rootpage-STATUSCODE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_STATUSCODE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>_STATUSCODE</b> gives the HTTP status code of an HTTP response that was opened using <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a>.
<span style="color:red;"><b>HTTP functionality is current unstable, and requires <a href="$UNSTABLE" title="$UNSTABLE">$UNSTABLE</a>:HTTP to be able to use.</b></span>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_STATUSCODE</a>(<i>Handle</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>Handle</i> is the handle returned from <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a> when making an HTTP request.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<p><b>_STATUSCODE</b> is used to get the HTTP status code returned on an HTTP response. A list of HTTP status codes can be read <a class="extiw" href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes" title="wikipedia:List of HTTP status codes">here</a>, generally speaking codes in the 200 range indicate success, 400 range indicates a client error, and 500 range indicate a server error.
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64-PE v3.5.0 and up</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$UNSTABLE" title="$UNSTABLE"><span style="color:#4593D8;">$UNSTABLE</span></a>:HTTP
' This URL simply returns a fake JSON response
h&amp; = <a href="OPENCLIENT" title="OPENCLIENT"><span style="color:#4593D8;">_OPENCLIENT</span></a>("HTTP:https://httpbin.org/json")
' Print the status code on the HTTP response
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_STATUSCODE</span></a>(h&amp;)
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> h&amp;
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">200
</pre>
</td></tr></tbody></table>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715003748
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.037 seconds
Real time usage: 0.056 seconds
Preprocessor visited node count: 87/1000000
Post‐expand include size: 1343/2097152 bytes
Template argument size: 216/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 24/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.873      1 -total
 14.89%    6.084      1 Template:OutputEnd
  8.54%    3.489      1 Template:OutputStartBG0
  7.26%    2.966      1 Template:Text
  6.90%    2.818      5 Template:Cl
  6.52%    2.667      1 Template:PageSyntax
  6.21%    2.537      2 Template:Parameter
  6.08%    2.486      1 Template:PageParameters
  5.98%    2.443      1 Template:Small
  5.96%    2.435      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1179-0!canonical and timestamp 20240715003748 and revision id 8995.
 -->
</div>
</div>
</div>
</div>
</body>
</html>