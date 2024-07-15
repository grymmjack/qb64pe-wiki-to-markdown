<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LOC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LOC rootpage-LOC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LOC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>LOC</b> function returns the status of a serial (COM) port received buffer or the last read/written byte or record position in an open file.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>bytes%</i> = <a class="mw-selflink selflink">LOC</a>(<i>fileOrPortNumber%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>fileOrPortNumber%</i> is the number used in the port or file <a href="OPEN" title="OPEN">OPEN</a> AS statement.</li>
<li>Returns 0 if the buffer is empty. Any value above 0 indicates the COM port has received data.</li>
<li>Use it in conjunction with <a href="INPUT$" title="INPUT$">INPUT$</a> to get the data bytes received.</li>
<li>Can also be used to get the last read/written byte or record position in a file. See also <a href="SEEK_(function)" title="SEEK (function)">SEEK</a>.</li></ul>
<h3><span class="mw-headline" id="Notes">Notes</span></h3>
<ul><li>Don't confuse the <a class="mw-selflink selflink">LOC</a> position with the <a href="SEEK_(function)" title="SEEK (function)">SEEK</a> position !!
<ul><li><b>LOC</b> is the <span style="color:red;">last</span> read or written byte or record prosition.</li>
<li><b>SEEK</b> is the byte or record prosition to read or write <span style="color:red;">next</span>.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Reading and writing from a COM port opened in Basic.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "<a href="OPEN_COM" title="OPEN COM"><span style="color:#4593D8;">COM</span></a>1: 9600,N,8,1,OP0" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = 2048 ' random mode = input and output
  <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: t$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> ' get any transmit keypresses from user
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(t$) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, t$ ' send keyboard byte to transmit buffer
    bytes% = <a class="mw-selflink selflink"><span style="color:#4593D8;">LOC</span></a>(1) ' bytes in buffer
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> bytes% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' check receive buffer for data"
      r$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(bytes%, 1)          ' get bytes in the receive buffer
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> r$; ' print byte strings consecutively to screen"
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> t$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) 'escape key exit
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Demonstrate the difference between <b>LOC</b> and <b>SEEK</b> positions in a file.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">OPEN "readme.md" FOR BINARY AS #1
PRINT LOC(1) 'LOC returns 0, as we didn't read something yet
PRINT SEEK(1) 'SEEK otherwise returns 1, as it's the first byte to read
GET #1, , a&amp; 'now let's read a LONG (4 bytes)
PRINT LOC(1) 'now LOC returns 4, the last read byte
PRINT SEEK(1) 'and SEEK returns 5 now, the next byte to read
CLOSE #1
END
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">0
1
4
5
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PRINT" title="PRINT">PRINT</a>, <a href="OPEN_COM" title="OPEN COM">OPEN COM</a>, <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT (file statement)</a></li>
<li><a href="SEEK" title="SEEK">SEEK</a>, <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061334
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.047 seconds
Preprocessor visited node count: 224/1000000
Post‐expand include size: 2027/2097152 bytes
Template argument size: 267/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.777      1 -total
  9.69%    2.789     22 Template:Cl
  9.34%    2.688      2 Template:CodeStart
  9.20%    2.648      1 Template:PageSyntax
  8.57%    2.465      2 Template:Text
  8.14%    2.342      3 Template:Parameter
  7.25%    2.085      2 Template:CodeEnd
  7.00%    2.013      1 Template:PageExamples
  6.93%    1.994      1 Template:OutputStart
  6.76%    1.944      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:553-0!canonical and timestamp 20240715061334 and revision id 8106.
 -->
</div>
</div>
</div>
</div>
</body>
</html>