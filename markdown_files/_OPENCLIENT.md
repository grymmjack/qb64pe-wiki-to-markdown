<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OPENCLIENT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPENCLIENT rootpage-OPENCLIENT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OPENCLIENT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_OPENCLIENT</b> function connects to a Host on the Internet as a Client and returns the Client status handle.
<span style="color:red;"><b>HTTP functionality is current unstable, and requires <a href="$UNSTABLE" title="$UNSTABLE">$UNSTABLE</a>:HTTP to be able to use.</b></span>
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>clientHandle&amp;</i> = <a class="mw-selflink selflink">_OPENCLIENT</a>(<b>"TCP/IP:8080:12:30:1:10"</b>)</dd>
<dd><i>clientHandle&amp;</i> = <a class="mw-selflink selflink">_OPENCLIENT</a>(<b>"HTTP:url"</b>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>An <a href="ERROR_Codes" title="ERROR Codes">Illegal Function Call</a> error will be triggered if the function is called with a string argument of the wrong syntax.</li>
<li>Connects to a host somewhere on the internet as a client.</li>
<li>Valid <i>clientHandle&amp;</i> values are negative. 0 means that the connection failed. Always check that the handle returned is not 0.</li>
<li><a href="CLOSE" title="CLOSE">CLOSE</a> <i>clientHandle&amp;</i> closes the client. A failed handle of value 0 does not need to be closed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Attempting to connect to a local host(your host) as a client. A zero return indicates failure.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">client = <a class="mw-selflink selflink"><span style="color:#4593D8;">_OPENCLIENT</span></a>("TCP/IP:7319:localhost")
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> client <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
   <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[Connected to " + <a href="CONNECTIONADDRESS" title="CONNECTIONADDRESS"><span style="color:#4593D8;">_CONNECTIONADDRESS</span></a>(client) + "]"
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[Connection Failed!]"
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Using HTTP to download from a URL.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' Content of the HTTP response is returned. The statusCode is also assigned.
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Download$(url <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>, statusCode <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    h&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_OPENCLIENT</span></a>("HTTP:" + url)
    statusCode = <a href="STATUSCODE" title="STATUSCODE"><span style="color:#4593D8;">_STATUSCODE</span></a>(h&amp;)
    <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(h&amp;)
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
        <a href="GET_(HTTP_statement)" title="GET (HTTP statement)"><span style="color:#4593D8;">GET</span></a> #h&amp;, , s$
        content$ = content$ + s$
    <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
    <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #h&amp;
    Download$ = content$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a></li>
<li><a href="CONNECTED" title="CONNECTED">_CONNECTED</a>, <a class="mw-redirect" href="CONNECTIONADDRESS$" title="CONNECTIONADDRESS$">_CONNECTIONADDRESS$</a></li>
<li><a href="Email_Demo" title="Email Demo">Email Demo</a>, <a href="Inter-Program_Data_Sharing_Demo" title="Inter-Program Data Sharing Demo">Inter-Program Data Sharing Demo</a></li>
<li><a href="Downloading_Files" title="Downloading Files">Downloading Files</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211450
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.069 seconds
Preprocessor visited node count: 208/1000000
Post‐expand include size: 2161/2097152 bytes
Template argument size: 455/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   48.325      1 -total
 25.38%   12.267      2 Template:CodeStart
 14.80%    7.154     23 Template:Cl
 10.91%    5.270      1 Template:Text
 10.39%    5.020      1 Template:PageSeeAlso
  6.61%    3.192      2 Template:CodeEnd
  5.79%    2.796      1 Template:PageNavigation
  5.58%    2.695      1 Template:PageExamples
  5.23%    2.528      1 Template:PageSyntax
  4.65%    2.248      4 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:205-0!canonical and timestamp 20240714211450 and revision id 8005.
 -->
</div>
</div>
</div>
</div>
</body>
</html>