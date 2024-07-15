<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CONNECTIONADDRESS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CONNECTIONADDRESS rootpage-CONNECTIONADDRESS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CONNECTIONADDRESS</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_CONNECTIONADDRESS</b> function returns a connected user's <a href="STRING" title="STRING">STRING</a> IP address value. For HTTP connections it returns the effective URL of the connection.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_CONNECTIONADDRESS[$]</a>(<i>connectionHandle&amp;</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The handle can come from the <a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCLIENT" title="OPENCLIENT">OPENCLIENT</a> or <a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a>.</li>
<li>For <b><a href="OPENHOST" title="OPENHOST">HOSTs</a></b>: It may return "TCP/IP:8080:213.23.32.5" where 8080 is the port it is listening on and 213.23.32.5 is the global IP address which any computer connected to the internet could use to locate your computer. If a connection to the internet is unavailable or your firewall blocks it, it returns your 'local IP' address (127.0.0.1). You might like to store this address somewhere where other computers can find it and connect to your host. Dynamic IPs which can change will need to be updated.</li>
<li>For <b><a href="OPENCLIENT" title="OPENCLIENT">CLIENTs</a></b>:
<ul><li>For TCP/IP, it may return "TCP/IP:8080:213.23.32.5" where 8080 is the port it used to connect to the listening host and 213.23.32.5 is the IP address of the host name it resolved.</li>
<li>For HTTP, it will return a url, such as "<a class="external free" href="https://qb64phoenix.com" rel="nofollow">https://qb64phoenix.com</a>". It is possible for this URL to differ from the one originally passed to <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a> if a HTTP redirect occurs when connecting to the original URL. The formatting may also differ slightly from the original URL.</li></ul></li>
<li>For <b><a href="OPENCONNECTION" title="OPENCONNECTION">CONNECTIONs</a></b> (from clients): It may return "TCP/IP:8080:34.232.321.25" where 8080 was the host listening port it connected to and 34.232.321.25 is the IP address of the client that connected. This is very useful because the host can log the IP address of clients for future reference (or banning, for example).</li>
<li>The $ sygil is optional for compatibility with older versions.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>A Host logging new chat clients in a Chat program. See the <a href="OPENHOST" title="OPENHOST">_OPENHOST</a> example for the rest of the code used.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">f = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> <span style="color:#FFB100;">"ChatLog.dat"</span> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">FOR</span></a> <a href="OPEN#File_Access_Modes" title="OPEN"><span style="color:#4593D8;">APPEND</span></a> <a href="OPEN" title="OPEN"><span style="color:#4593D8;">AS</span></a> #f <span style="color:#919191;">' code at start of host section before DO loop.</span>
newclient = <a href="OPENCONNECTION" title="OPENCONNECTION"><span style="color:#4593D8;">_OPENCONNECTION</span></a>(host) <span style="color:#919191;">' receive any new client connection handles</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> newclient <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    numclients = numclients + <span style="color:#F580B1;">1</span> <span style="color:#919191;">' increment index</span>
    Users(numclients) = newclient <span style="color:#919191;">' place handle into array</span>
    IP$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_CONNECTIONADDRESS</span></a>(newclient)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> IP$ + <span style="color:#FFB100;">" has joined."</span> <span style="color:#919191;">' displayed to Host only</span>
    <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #f, IP$, numclients <span style="color:#919191;">' print info to a log file</span>
    <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #Users(numclients), <span style="color:#FFB100;">"Welcome!"</span> <span style="color:#919191;">' from Host to new clients only</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Explanation</b>
 The function returns the new client's IP address to the IP$ variable.
 Prints the IP and the original login position to a log file. The
 information can later be used by the host for reference  if necessary.
 The host could set up a ban list too.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPENCONNECTION" title="OPENCONNECTION">_OPENCONNECTION</a>, <a href="CONNECTED" title="CONNECTED">_CONNECTED</a></li>
<li><a href="OPENHOST" title="OPENHOST">_OPENHOST</a>, <a href="OPENCLIENT" title="OPENCLIENT">_OPENCLIENT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192644
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.038 seconds
Real time usage: 0.071 seconds
Preprocessor visited node count: 232/1000000
Post‐expand include size: 2261/2097152 bytes
Template argument size: 679/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 250/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.862      1 -total
 11.08%    3.529      1 Template:PreEnd
  9.35%    2.979     11 Template:Text
  8.92%    2.843      1 Template:PageSyntax
  8.65%    2.756     13 Template:Cl
  8.30%    2.643      1 Template:PreStart
  7.13%    2.273      1 Template:PageSeeAlso
  6.94%    2.212      2 Template:Parameter
  6.86%    2.184      1 Template:PageNavigation
  6.48%    2.066      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:422-0!canonical and timestamp 20240714192644 and revision id 8288.
 -->
</div>
</div>
</div>
</div>
</body>
</html>