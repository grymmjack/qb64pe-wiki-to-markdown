<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PUT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PUT rootpage-PUT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PUT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>PUT #</b> file or port statement writes data to a specific byte or record location.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>PUT #<i>filenumber&amp;</i>,</b> [<i>position</i>][, {<i>holdingvariable</i>|<i>holdingarray()</i>}]</dd></dl></dd></dl>
<p>
</p>
<ul><li>File/port number is the number used in the <a href="OPEN" title="OPEN">OPEN</a> statement.</li>
<li>The <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="LONG" title="LONG">LONG</a> file byte <i>position</i> in a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file or the record <i>position</i> in a <a href="RANDOM" title="RANDOM">RANDOM</a> file <b>must be greater than zero</b>.</li>
<li>The file byte or record <i>position</i> can be omitted if the <a class="mw-selflink selflink">PUT</a> or <a href="GET" title="GET">GET</a> is consecutive or when creating new file data sequentially.</li>
<li>The <i>holding variable</i> <a href="TYPE" title="TYPE">type</a> determines byte size and the next byte position in the file when the <i>position</i> is ommitted.</li>
<li>The first byte or record position is 1. This may require adding one to an offset value when documentation uses that position as 0.</li>
<li>Both the file <i>position</i> and <i>holding variable</i>(and comma) can be omitted when using a <a href="FIELD" title="FIELD">FIELD</a> definition.</li>
<li>If a <a href="LEN" title="LEN">LEN</a> = record length statement is omitted in an <a href="OPEN" title="OPEN">OPEN</a> FOR <a href="RANDOM" title="RANDOM">RANDOM</a>  statement the record size defaults to 128 bytes!</li>
<li><b>Warning: Not designating a PUT position can overwrite previous file data based on the current file <i>position</i>!</b></li>
<li>When using a numeric <i>holding variable</i>, values do NOT require conversion using <a href="MKI$" title="MKI$">MKI$</a>, <a href="MKL$" title="MKL$">MKL$</a>, <a href="MKS$" title="MKS$">MKS$</a> or <a href="MKD$" title="MKD$">MKD$</a>.</li>
<li><b>QB64</b> can load <a href="Arrays" title="Arrays">array</a> data directly(brackets required) to a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file using <b>one</b> PUT to a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> file: <b><span style="color:green;">PUT #1, , array()</span></b></li></ul>
<p>
<i>Example 1:</i> Using a <a href="TYPE" title="TYPE">TYPE</a> record variable(Contact) to enter a new <a href="RANDOM" title="RANDOM">RANDOM</a> record to a file.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> ContactType
  first <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 10
  last <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 20
  age <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Contact <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> ContactType
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a first name: ", Contact.first
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a last name: ", Contact.last
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter an age: ", Contact.age
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "Record.lst" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Contact)
NumRecords% = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1) \ <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Contact)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> NumRecords%; "previous records"
<a class="mw-selflink selflink"><span style="color:#4593D8;">PUT</span></a> #1, NumRecords% + 1, Contact ' add a new record <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> record value
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The DOT record variable values were created or changed before the PUT. The record length is 32 bytes.</dd></dl>
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
<a class="mw-selflink selflink"><span style="color:#4593D8;">PUT</span></a> #1, , array()
<a href="ERASE" title="ERASE"><span style="color:#4593D8;">ERASE</span></a> array 'clear element values from array and display empty
showme
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "BINFILE.BIN" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="BINARY" title="BINARY"><span style="color:#4593D8;">BINARY</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #2, , array()
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
<dl><dd><i>Note:</i> Use empty brackets in QB64 when using <a href="GET" title="GET">GET</a> to create an array or <a class="mw-selflink selflink">PUT</a> to create a <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> data file.</dd></dl>
<h3><span class="mw-headline" id="More_Examples">More Examples</span></h3>
<ul><li><a href="Program_ScreenShots" title="Program ScreenShots">Program ScreenShots</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GET" title="GET">GET #</a></li>
<li><a href="SEEK" title="SEEK">SEEK</a>, <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a></li>
<li><a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT  #</a></li>
<li><a href="FIELD" title="FIELD">FIELD</a></li>
<li><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="PUT_(TCP/IP_statement)" title="PUT (TCP/IP statement)">PUT (TCP/IP statement)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031656
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.038 seconds
Real time usage: 0.048 seconds
Preprocessor visited node count: 549/1000000
Post‐expand include size: 3361/2097152 bytes
Template argument size: 477/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.771      1 -total
 23.15%    5.734     54 Template:Cl
 16.56%    4.101      1 Template:Text
  9.43%    2.336      2 Template:CodeEnd
  9.37%    2.320      2 Template:CodeStart
  8.99%    2.228      1 Template:PageSyntax
  8.28%    2.050      1 Template:PageSeeAlso
  7.51%    1.860      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:273-0!canonical and timestamp 20240715031656 and revision id 8098.
 -->
</div>
</div>
</div>
</div>
</body>
</html>