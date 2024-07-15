<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LEN rootpage-LEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LEN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>LEN</b> function returns the number of bytes used by a variable value or the number of characters in a <a href="STRING" title="STRING">STRING</a>. In QB64 it can also return the size of an array or <a href="TYPE" title="TYPE">TYPE</a> variable.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>length%</i> = <a class="mw-selflink selflink">LEN</a>(<i>literalTextOrVariable</i>)</dd></dl>
<p>
</p>
<ul><li>Literal or variable <a href="STRING" title="STRING">STRING</a> values return the number of string bytes which is the same as the number of string characters.</li>
<li>A numerical <i>variable</i> will return the number of bytes used by a numerical variable type.
<ul><li><a href="BYTE" title="BYTE">_BYTE</a> variable types return 1 byte.</li>
<li><a href="INTEGER" title="INTEGER">INTEGER</a> variable types return 2 bytes.</li>
<li><a href="SINGLE" title="SINGLE">SINGLE</a> and <a href="LONG" title="LONG">LONG</a> integer variable types return 4 bytes.</li>
<li><a href="DOUBLE" title="DOUBLE">DOUBLE</a> and <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> variable types return 8 bytes.</li>
<li><a href="FLOAT" title="FLOAT">_FLOAT</a> variable types return 32 bytes.</li>
<li><a href="OFFSET" title="OFFSET">_OFFSET</a> and <a href="MEM" title="MEM">_MEM</a> variable types return varying byte sizes.</li>
<li><i>Note:</i> <a href="BIT" title="BIT">_BIT</a> variable types and bit multiples <b>cannot be measured in bytes</b>.</li></ul></li>
<li><b>LEN cannot return lengths of literal numerical values and will create a "variable required" status error in the IDE.</b></li>
<li><b>LEN =</b> can be used with a user defined <a href="TYPE" title="TYPE">TYPE</a> variable to determine the number of bytes used in <a href="RANDOM" title="RANDOM">RANDOM</a> file records:</li></ul>
<dl><dd><dl><dd><dl><dd><dl><dd><span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;"><a href="OPEN" title="OPEN">OPEN</a> file$ FOR <a href="RANDOM" title="RANDOM">RANDOM</a> AS #n LEN = LEN(recordTypeVariable)</span><b></b></dd></dl></dd></dl></dd></dl>
<ul><li>If a LEN = statement is not used, <a href="RANDOM" title="RANDOM">RANDOM</a> default record length is 128 or sequencial is 512 up to a maximum of 32767 bytes.</li>
<li><a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> OPEN statements will ignore LEN = statements. The byte size of a <a href="GET" title="GET">read</a> or <a href="PUT" title="PUT">write</a> is determined by the <a href="Variable_Types" title="Variable Types">variable type</a>.</li></ul></dd></dl>
<ul><li>In QB64 the <b>LEN</b> function can also return the size of entire arrays (except variable length string arrays), see example 5 below.</li></ul>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> With a string variable the byte size is the same as the number of characters.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">LastName$ = "Williams"
PRINT <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(LastName$); "bytes"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 8 bytes
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Testing <a href="INPUT" title="INPUT">INPUT</a> for numerical <a href="STRING" title="STRING">STRING</a> entries from a user.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "number: ", num$
value$ = <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(<a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(num$)))
L = <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(value$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(num$), L
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> <a href="%26H" title="&amp;H">&amp;H</a>, <a href="%26O" title="&amp;O">&amp;O</a>, D and E will also be accepted as numerical type data in a <a href="VAL" title="VAL">VAL</a> conversion, but will add to the entry length.</dd></dl>
<p>
<i>Example 3:</i> With numerical value types you MUST use a variable to find the inherent byte length when using LEN.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DIM I AS INTEGER
PRINT "INTEGER ="; LEN(I); "bytes"
DIM L AS LONG
PRINT "LONG ="; LEN(L); "bytes"
DIM I64 AS _INTEGER64
PRINT "_INTEGER64 ="; LEN(I64); "bytes"
DIM S AS SINGLE
PRINT "SINGLE ="; LEN(S); "bytes"
DIM D AS DOUBLE
PRINT "DOUBLE ="; LEN(D); "bytes"
DIM F AS _FLOAT
PRINT "_FLOAT ="; LEN(F); "bytes"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">INTEGER = 2 bytes
LONG = 4 bytes
_INTEGER64 = 8 bytes
SINGLE = 4 bytes
DOUBLE = 8 bytes
_FLOAT = 32 bytes
</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> Opening a RANDOM file using LEN to calculate and LEN = to designate the file record size.
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
RecordLEN% = <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(record)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> RecordLEN%; "bytes"
record.x = 255
record.y = "Hello world!"
record.z = 65535
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> record.x, record.y, record.z
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a> = RecordLEN%
<a href="PUT" title="PUT"><span style="color:#4593D8;">PUT</span></a> #1, number% , record 'change record position number to add records
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> <a href="RANDOM" title="RANDOM"><span style="color:#4593D8;">RANDOM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #2 <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a> = RecordLEN%
NumRecords% = <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(2) \ RecordLEN%
PRINT NumRecords%; "records"
<a href="GET" title="GET"><span style="color:#4593D8;">GET</span></a> #2, NumRecords% , newrec 'GET last record available
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
<dd>To read the last record <a href="GET" title="GET">GET</a> the number of records. To add a record, use the number of records + 1 to <a href="PUT" title="PUT">PUT</a> new record data.</dd></dl>
<p>
<i>Example 5:</i> Find the size of arrays and array elements.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a!(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>) <span style="color:#919191;">'a SINGLE has 4 bytes</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Element size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(a!(<span style="color:#F580B1;">1</span>)), <span style="color:#FFB100;">"Overall size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(a!()) <span style="color:#919191;">'5 elements * 4 bytes = 20 bytes</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> b%(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>) <span style="color:#919191;">'an INTEGER has 4 bytes</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Element size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(b%(<span style="color:#F580B1;">1</span>)), <span style="color:#FFB100;">"Overall size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(b%()) <span style="color:#919191;">'5 elements * 2 bytes = 10 bytes</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> c$(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>)
<span style="color:#919191;">'PRINT LEN(c$()) 'Error: cannot use for array of variable length strings</span>
<span style="color:#919191;">'but for fixed length strings it works</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> d$3(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>) <span style="color:#919191;">'fixed length (3 chars)</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Element size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(d$3(<span style="color:#F580B1;">1</span>)), <span style="color:#FFB100;">"Overall size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(d$3()) <span style="color:#919191;">'5 elements * 3 bytes = 15 bytes</span>
<span style="color:#919191;">'and it also works for TYPE arrays</span>
<a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> t
    a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> <span style="color:#919191;">'4 bytes</span>
    b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a> <span style="color:#919191;">'2 bytes</span>
<a class="mw-redirect" href="END_TYPE" title="END TYPE"><span style="color:#4593D8;">END TYPE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> e(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">5</span>) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> t <span style="color:#919191;">'type is 6 bytes long</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Element size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(e(<span style="color:#F580B1;">1</span>)), <span style="color:#FFB100;">"Overall size ="</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">LEN</span></a>(e()) <span style="color:#919191;">'5 elements * 6 bytes = 30 bytes</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LOF" title="LOF">LOF</a>, <a href="EOF" title="EOF">EOF</a></li>
<li><a href="AS" title="AS">AS</a>, <a href="TYPE" title="TYPE">TYPE</a></li>
<li><a href="RANDOM" title="RANDOM">RANDOM</a>, <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192457
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.071 seconds
Real time usage: 0.090 seconds
Preprocessor visited node count: 854/1000000
Post‐expand include size: 6706/2097152 bytes
Template argument size: 1515/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 505/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   50.527      1 -total
 11.26%    5.687     70 Template:Cl
  9.41%    4.757     35 Template:Text
  8.61%    4.349      1 Template:PageSeeAlso
  7.30%    3.689      5 Template:CodeStart
  6.88%    3.474      1 Template:PageSyntax
  5.99%    3.029      2 Template:Parameter
  5.49%    2.774      1 Template:InlineCodeEnd
  5.28%    2.670      1 Template:InlineCode
  5.12%    2.585      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:542-0!canonical and timestamp 20240714192457 and revision id 8870.
 -->
</div>
</div>
</div>
</div>
</body>
</html>