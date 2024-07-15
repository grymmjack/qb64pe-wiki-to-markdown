<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FIELD - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FIELD rootpage-FIELD skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FIELD</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">FIELD</a> statement creates a <a href="STRING" title="STRING">STRING</a> type definition for a <a href="RANDOM" title="RANDOM">random</a>-access file buffer.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">FIELD</a> [#]<i>fileNumber&amp;</i>, <i>fieldWidth1%</i> AS <i>variable1$</i>[, <i>fieldWidthN%</i> AS <i>variableN$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>fileNumber%</i> is a file number used in the <a href="OPEN" title="OPEN">OPEN</a> statement or a value from the <a href="FREEFILE" title="FREEFILE">FREEFILE</a> function.</li>
<li>Combined size of the <i>fieldWidth%</i> parameters <b>must not exceed the <a href="LEN" title="LEN">LEN</a> = recordsize in the <a href="RANDOM" title="RANDOM">RANDOM</a> <a href="OPEN" title="OPEN">OPEN</a> statement</b> or a <a href="ERROR_Codes" title="ERROR Codes">"FIELD overflow" error</a> will occur.</li>
<li>Variables are limited to <a href="STRING" title="STRING">STRING</a> types. Use <a href="TYPE" title="TYPE">TYPE</a> instead of FIELD if you want to use numerical values.</li>
<li>Once a <a class="mw-selflink selflink">FIELD</a> is defined in a statement, <a href="GET" title="GET">GET</a> can read and <a href="PUT" title="PUT">PUT</a> can write data without placeholders or variables.</li>
<li><a href="LSET" title="LSET">LSET</a>, <a href="RSET" title="RSET">RSET</a>, <a href="PRINT_(file_statement)" title="PRINT (file statement)">PRINT #</a>, <a href="PRINT_USING_(file_statement)" title="PRINT USING (file statement)">PRINT # USING</a>, and <a href="WRITE_(file_statement)" title="WRITE (file statement)">WRITE #</a> can be used to place characters in the file buffer before a <a href="PUT" title="PUT">PUT</a>.</li>
<li>All field definitions for a file are removed when the file is <a href="CLOSE" title="CLOSE">closed</a> or <a href="RESET" title="RESET">RESET</a> and all strings are set to null ("").</li>
<li><b>Do not re-assign a field defined variable value or use it in an <a href="INPUT" title="INPUT">INPUT</a> statement if you want the variable to remain a field</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Comparing a <a href="TYPE" title="TYPE">TYPE</a> definition with a FIELD <a href="STRING" title="STRING">string</a> definition. Demo using a <a href="TYPE" title="TYPE">TYPE</a> definition to create a file:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> ClientType
   CName <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 30     '30 bytes
   Address <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 30   '30 bytes
   City   <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 15    '15 bytes
   State  <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 2     ' 2 bytes
   Zip    <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 5     ' 5 bytes
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>      ' total size = 82 bytes
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Client <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> ClientType
RecordLEN = <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Client)       'find the size of each TYPE record
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "ADDRESS.DAT" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = RecordLEN
<a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> ClientData         'restore to start of DATA
record = 0
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
   <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> CName$, Address$, City$, State$, Zip$       'read DATA
   <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> CName$ = "END" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
   record = record + 1               'increment record number
   Client.CName = CName$
   Client.Address = Address$
   Client.City = City$
   Client.State = State$
   Client.Zip = Zip$
   <a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, record, Client     'PUT by record number
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
ClientData:
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "Bob White","104 Birdland Rd.","Bellview","PA","15236"
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "Ward Cleaver","123 W. Beaver St.","Beaver","PA","15255"
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "Elmer Fudd","45 Wabbit St.","Bethel Park","PA","15022"
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "Wyley Coyote","33 Roadrunner Ave.","Clairton","PA","15122"
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "Jim Morrison","19 Doorway Dr.","Belleview","PA","15236"
   <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> "END",0,0,0,0
</pre>
</td></tr></tbody></table>
<p>Demo using the FIELD statement to read the file:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> NM = 30, AD = 30, CT = 15, ST = 2, ZC = 5  ' Define field and record lengths with constants.
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> RLEN = NM + AD + CY + ST + ZC
'
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "ADDRESS.DAT" <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a> = RLEN
<a class="mw-selflink selflink"><span style="color:#4593D8;">FIELD</span></a> #1, NM <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> CName$, AD <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> Address$, CY <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> City$, ST <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> State$, ZC <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> Zip$
<a class="mw-selflink selflink"><span style="color:#4593D8;">FIELD</span></a> #1, RLEN <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> Clist$         'define entire record
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #1, 1                  'GET does not need a variable to read FIELD records!
                                  'Read file for zip codes from 15230 to 15239 .
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(1)
   ZipCheck$ = Zip$                            'read zip codes
   <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> (ZipCheck$ &gt;= "15230" <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> ZipCheck$ &lt;= "15239") <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
      Info$ = Clist$
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(Info$, 30)     'read name string
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(Info$, 31, 30)  'read address string
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(Info$, 17)    'read city, state and zip code
      <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
   <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
   <a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #1                               'simply GET reads each FIELD record after first
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPEN" title="OPEN">OPEN</a>, <a href="TYPE" title="TYPE">TYPE</a></li>
<li><a href="GET" title="GET">GET</a>, <a href="PUT" title="PUT">PUT</a></li>
<li><a href="LSET" title="LSET">LSET</a>, <a href="RSET" title="RSET">RSET</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211105
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.090 seconds
Preprocessor visited node count: 555/1000000
Post‐expand include size: 4376/2097152 bytes
Template argument size: 678/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   56.090      1 -total
 17.43%    9.775     72 Template:Cl
 10.53%    5.906      1 Template:PageSyntax
 10.03%    5.626      1 Template:PageSeeAlso
  8.51%    4.772      1 Template:PageDescription
  7.85%    4.401      7 Template:Parameter
  7.70%    4.317      2 Template:CodeEnd
  7.19%    4.034      1 Template:PageNavigation
  6.83%    3.829      1 Template:PageExamples
  6.50%    3.646      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:275-0!canonical and timestamp 20240714211105 and revision id 8126.
 -->
</div>
</div>
</div>
</div>
</body>
</html>