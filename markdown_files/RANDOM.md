<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RANDOM - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RANDOM rootpage-RANDOM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RANDOM</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>RANDOM</b> is used in an <a href="OPEN" title="OPEN">OPEN</a> statement to read(<a href="GET" title="GET">GET</a>) from or write(<a href="PUT" title="PUT">PUT</a>) to a file.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>OPEN Filename$ FOR RANDOM AS #1 [LEN = <i>recordlength%</i>]</dd></dl></dd></dl>
<p>
</p>
<ul><li>RANDOM is the Default mode if no mode is given in the <a href="OPEN" title="OPEN">OPEN</a> statement.</li>
<li>It creates the file if the legal file name given does NOT exist.</li>
<li>As a RANDOM file, it can read or write any record using <a href="GET" title="GET">GET</a> and/or <a href="PUT" title="PUT">PUT</a> statements.</li>
<li><i>Recordlength%</i> is determined by getting the LEN of a <a href="TYPE" title="TYPE">TYPE</a> variable or a <a href="FIELD" title="FIELD">FIELD</a> statement.</li></ul>
<dl><dd><dl><dd><a href="STRING" title="STRING">STRING</a> = 1 byte/character, <a href="INTEGER" title="INTEGER">INTEGER</a> = 2 bytes, <a href="LONG" title="LONG">LONG</a> = 4 bytes, <a href="SINGLE" title="SINGLE">SINGLE</a> = 4 bytes <a href="DOUBLE" title="DOUBLE">DOUBLE</a> = 8 bytes</dd>
<dd><a href="BYTE" title="BYTE">_BYTE</a> = 1 byte, <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> = 8 bytes, <a href="FLOAT" title="FLOAT">_FLOAT</a> = 10 bytes (so far)</dd></dl></dd></dl>
<ul><li>If no record length is used in the <a href="OPEN" title="OPEN">OPEN</a> statement, the default record size is 128 bytes except for the last record.</li>
<li>A record length cannot exceed 32767 or an <a href="ERROR_Codes" title="ERROR Codes">error</a> will occur!</li>
<li>To determine the number of records in a file the records% = <a href="LOF" title="LOF">LOF</a> \ recordlength%.</li>
<li>When <b>variable length strings</b> are PUT into RANDOM files the record length must exceed the maximum string entry by:</li></ul>
<dl><dd><dl><dd>2 bytes are reserved for recording variable string lengths up to 32767 bytes (LEN = longest + 2)</dd>
<dd>8 bytes are reserved for recording variable string lengths exceeding 32767 bytes (LEN = longest + 8)</dd></dl></dd></dl>
<ul><li>A serial communication port can also be opened for RANDOM in an <a href="OPEN_COM" title="OPEN COM">OPEN COM</a> statement.</li></ul>
<p>
<i>Example 1:</i> Function that finds a RANDOM file's record number for a string value such as a phone number.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> customer
  age <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
  phone <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 10
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> cust <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> customer, recLEN
recLEN = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(cust)            'get the length of the record type
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Rec<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>:"; recLEN
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "randfile.rec" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = recLEN
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4
  <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> cust.age, cust.phone
  <a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, , cust
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
RP = RecordPos("randfile.rec", "2223456789")  'returns 0 if record not found!
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> RP
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> RP <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "randfile.rec" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = recLEN
  <a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #2, RP, cust
  <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #2
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> cust.age, cust.phone
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 59,2223456789,62,4122776477,32,3335551212,49,1234567890
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> RecordPos (file$, search$)
f = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #f
FL = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(f)
dat$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(FL, f)
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> f
recpos = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(dat$, search$)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> recpos <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> RecordPos = recpos \ recLEN + 1 <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> RecordPos = 0
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Random files can store records holding various variable types using a <a href="TYPE" title="TYPE">TYPE</a> definition or a <a href="FIELD" title="FIELD">FIELD</a> statement.</dd></dl>
<p>
<i>Example 2:</i> When not using a <a href="TYPE" title="TYPE">TYPE</a> or fixed length strings, QB4.5 allows RANDOM files to hold variable length strings up to 2 bytes less than the LEN = record length statement:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONTROLCHR" title="CONTROLCHR"><span style="color:#4593D8;">_CONTROLCHR</span></a> OFF
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "myfile.txt" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1: <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1: ' clears former file of all entries.
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "myfile.txt" <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = 13 'strings can be up to 11 bytes with 2 byte padder
a$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(1) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(0) + "ABCDEFGHI"
b$ = "ABCDEFGHI"
c$ = "1234"
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, 1, a$
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, 2, b$
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, 3, c$
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 3
  <a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #1, i, a$
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(a$)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">☺ ABCDEFGHI       11
ABCDEFGHI         9
1234              4
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The 2 byte file padders before each string PUT will show the length of a string for GET as <a href="ASCII" title="ASCII">ASCII</a> characters. Padders will always be 2 bytes and strings up to the last one will be 13 bytes each no matter the length up to 11, so the file size can be determined as (2 + 11) + (2 + 9 + 2) + (2 + 4) or 13 + 13 + 2 + 4 = 32 bytes.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a>, <a href="FIELD" title="FIELD">FIELD</a></li>
<li><a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="SEEK" title="SEEK">SEEK</a>, <a href="SEEK_(function)" title="SEEK (function)">SEEK (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211203
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.064 seconds
Real time usage: 0.110 seconds
Preprocessor visited node count: 547/1000000
Post‐expand include size: 4484/2097152 bytes
Template argument size: 697/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   66.757      1 -total
 17.42%   11.630      1 Template:PageSeeAlso
 16.67%   11.126      1 Template:OutputEnd
 13.33%    8.900     75 Template:Cl
 11.10%    7.407      1 Template:PageSyntax
  9.01%    6.015      1 Template:PageNavigation
  7.61%    5.077      1 Template:OutputStart
  5.97%    3.984      2 Template:CodeStart
  5.19%    3.462      2 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:238-0!canonical and timestamp 20240714211203 and revision id 8099.
 -->
</div>
</div>
</div>
</div>
</body>
</html>