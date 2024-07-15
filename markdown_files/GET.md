<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>GET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GET rootpage-GET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">GET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">GET #</a> statement reads data from a file or port device by bytes or record positions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">GET #</a><i>fileNumber&amp;</i>, [<i>position</i>][, {<i>targetVariable</i>|<i>targetArray()</i>}]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileNumber&amp;</i> is the file or port number used in the <a href="OPEN" title="OPEN">OPEN</a> AS <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> or <a href="RANDOM" title="RANDOM">RANDOM</a> statement.</li>
<li>The <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> byte <i>position</i> in a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file or the record <i>position</i> in a <a href="RANDOM" title="RANDOM">RANDOM</a> file <b>must be greater than zero</b>.</li>
<li>The <i>position</i> can be omitted if the GET operations are consecutive based on the <i>targetVariable</i> <a href="TYPE" title="TYPE">TYPE</a> byte size.</li>
<li>The <i>targetVariable</i> <a href="Data_types" title="Data types">type</a> or <a href="FIELD" title="FIELD">FIELD</a> <i>variable</i> size determines the byte size and the next <i>position</i> in the file.</li>
<li>The first byte position in a file is 1.</li>
<li>GET does not require a byte or record <i>position</i> or <i>targetVariable</i> (or comma) when using a <a href="FIELD" title="FIELD">FIELD</a> statement.</li>
<li><b>QB64</b> can <a href="PUT" title="PUT">PUT</a> the entire contents of an array to a file and later GET those contents to a <i>targetArray()</i> (include brackets).</li>
<li><b>GET may ignore the end of a file and return bad data. If the <a href="EOF" title="EOF">EOF</a> function returns -1 after a GET operation, it indicates that the data has ended.</b></li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"> DO UNTIL <a href="EOF" title="EOF"><span style="color:blue;">EOF</span></a>(1)
   <a class="mw-selflink selflink"><span style="color:blue;">GET</span></a> #1, , value%
   IF <a href="NOT" title="NOT"><span style="color:blue;">NOT</span></a>(<a href="EOF" title="EOF"><span style="color:blue;">EOF</span></a>(1)) THEN <a href="PUT" title="PUT"><span style="color:blue;">PUT</span></a> #2, , value%
 LOOP
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> variabletype
  x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>'       '2 bytes
  y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 10'  '10 bytes
  z <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>'          '4 bytes
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>'            '16 bytes total
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> record <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> variabletype
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> newrec <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> variabletype
file$ = "testrand.inf" '&lt;&lt;&lt;&lt; filename may overwrite existing file
number% = 1 '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; record number to write cannot be zero
RecordLEN% = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(record)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> RecordLEN%; "bytes"
record.x = 255
record.y = "Hello world!"
record.z = 65535
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> record.x, record.y, record.z
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = RecordLEN%
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, number% , record 'change record position number to add records
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = RecordLEN%
NumRecords% = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(2) \ RecordLEN%
PRINT NumRecords%; "records"
<a class="mw-selflink selflink"><span style="color:#4593D8;">GET</span></a> #2, NumRecords% , newrec 'GET last record available
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #2
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> newrec.x, newrec.y, newrec.z
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 16 bytes
 255        Hello worl       65535
 1 records
 255        Hello worl       65535
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The byte size of the record <a href="TYPE" title="TYPE">TYPE</a> determines the <a href="LOF" title="LOF">LOF</a> byte size of the file and can determine the number of records.</dd>
<dd>To read the last record <a class="mw-selflink selflink">GET</a> the number of records. To add a record, use the number of records + 1 to <a href="PUT" title="PUT">PUT</a> new record data.</dd></dl>
<p>
<i>Example 2:</i> Placing the contents of a numerical array into a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file. You may want to put the array size at the beginning too.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> array(100) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100
  array(i) = i
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
showme  'display array contents
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "BINFILE.BIN" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, , array()
<a href="ERASE" title="ERASE"><span style="color:#4593D8;">ERASE</span></a> array 'clear element values from array and display empty
showme
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "BINFILE.BIN" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2
<a class="mw-selflink selflink"><span style="color:#4593D8;">GET</span></a> #2, , array()
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #2
showme  'display array after transfer from file
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> showme
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> array(i);
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "done"
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Use empty brackets in QB64 when using <a class="mw-selflink selflink">GET</a> to create an array or <a href="PUT" title="PUT">PUT</a> to create a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> data file.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PUT" title="PUT">PUT #</a>, <a href="SEEK" title="SEEK">SEEK</a>, <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a></li>
<li><a href="INPUT_(file_statement)" title="INPUT (file statement)">INPUT #</a>, <a href="GET_(TCP/IP_statement)" title="GET (TCP/IP statement)">GET (TCP/IP statement)</a></li>
<li><a href="FIELD" title="FIELD">FIELD</a>, <a href="RANDOM" title="RANDOM">RANDOM</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="LEN" title="LEN">LEN</a>, <a href="LOF" title="LOF">LOF</a>, <a href="EOF" title="EOF">EOF</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031609
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.057 seconds
Real time usage: 0.077 seconds
Preprocessor visited node count: 551/1000000
Post‐expand include size: 4290/2097152 bytes
Template argument size: 684/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   41.396      1 -total
 13.75%    5.693     61 Template:Cl
  7.36%    3.045      1 Template:TextEnd
  6.47%    2.678      5 Template:Cb
  5.98%    2.477     14 Template:Parameter
  5.94%    2.457      1 Template:PageSyntax
  5.67%    2.345      2 Template:CodeEnd
  5.51%    2.279      1 Template:TextStart
  5.46%    2.262      1 Template:PageSeeAlso
  4.83%    1.998      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:272-0!canonical and timestamp 20240715031609 and revision id 8093.
 -->
</div>
</div>
</div>
</div>
</body>
</html>