<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STRING - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STRING rootpage-STRING skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STRING</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>STRING</b> variables or literal values are one byte per character length text or <a href="ASCII" title="ASCII">ASCII</a> characters.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>DIM variable AS STRING [* byte_length]</dd></dl></dd></dl>
<p>
</p>
<ul><li><i>Byte length</i> is optional in <a href="DIM" title="DIM">DIM</a> statements, but is required in <a href="TYPE" title="TYPE">TYPE</a> definitions as a literal or <a href="CONST" title="CONST">constant</a> <a href="INTEGER" title="INTEGER">INTEGER</a> value.</li>
<li>Literal strings are defined by quotation marks on each end. The quotes will not <a href="PRINT" title="PRINT">PRINT</a> to the screen.</li>
<li>Quotation marks cannot be placed inside of literal string values! Use <a href="CHR$" title="CHR$">CHR$</a>(34) to display " quotes.</li>
<li>Semicolons and commas outside of the string can be used to combine strings in a <a href="PRINT" title="PRINT">PRINT</a> statement only.</li>
<li><a href="LEN" title="LEN">LEN</a> determines the number of bytes and number of string characters that are in a particular string.</li>
<li>Literal string ends are designated by quotation marks such as: "text". Use <a href="CHR$" title="CHR$">CHR$</a>(34) to add quotes to string values.</li>
<li>Variable suffix type definition is $ such as: text$.</li>
<li>STRING values are compared according to the <a href="ASCII" title="ASCII">ASCII</a> code values from left to right until one string code value exceeds the other.</li>
<li><b>NOTE: Many QBasic keyword variable names CAN be used with a <a class="mw-selflink selflink">STRING</a> suffix($) ONLY! You CANNOT use them without the suffix, use a numerical suffix or use <a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="DEFINE" title="DEFINE">_DEFINE</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> or <a href="TYPE" title="TYPE">TYPE</a> variable <a href="AS" title="AS">AS</a> statements!</b></li></ul>
<p>
</p>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><b>Creating a fixed length STRING variable in QBasic:</b></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
<dl><dd><ul><li>Variable$ = " " ' 1 space creates a one <a href="BYTE" title="BYTE">byte</a> string length in a procedure(not fixed)</li>
<li>Variable$ = SPACE$(n%) ' defined as a n% length string in a procedure(not fixed)</li>
<li><a href="DIM" title="DIM">DIM</a> variable AS STRING * n% ' fixed string length cannot be changed later</li>
<li>Variable AS STRING * n% ' fixed string length in a <a href="SUB" title="SUB">SUB</a> parameter or <a href="TYPE" title="TYPE">TYPE</a> definition.</li>
<li><a href="CONST" title="CONST">CONST</a> variables can also be used after the constant value is defined.</li></ul></dd></dl>
<p>
</p>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><b>QB64 fixed length string type suffixes</b></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
<ul><li>A number after the string variable name $ suffix denotes the fixed string length: <b>X$2</b> denotes a 2 byte string.</li></ul>
<p>
</p>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><b>String <a href="Concatenation" title="Concatenation">Concatenation</a> (addition)</b></dd></dl></dd></dl></dd>
<dd><i>Must be used when defining a string variable's literal value!</i></dd></dl></dd></dl></dd></dl></dd></dl>
<ul><li>Concatenation uses the + addition symbol to add literal or variable parts to a string variable value.</li>
<li>Quotation marks cannot be added. Use <a href="CHR$" title="CHR$">CHR$</a>(34) as quotes are used to define the ends of strings.</li>
<li>Numerical values added must be converted to strings in string variable definitions. See the <a href="STR$" title="STR$">STR$</a> function.</li>
<li>Concatenation can be used in PRINT statements along with semicolons and commas used by <a href="PRINT" title="PRINT">PRINT</a> ONLY.</li>
<li>Semicolons or commas outside of quotes cannot be used to make a string variable's literal string value!</li></ul>
<p>
<i>Example 1:</i> Using a string type suffix with a fixed length byte size in QB64 only. The number designates the fixed string length.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">var$5 = "1234567"
PRINT var$5
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">12345</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The suffix must keep the same byte length or it is considered a different string variable with a different value!</dd></dl>
<p>
<i>Example 2:</i> Creating a string variable value by adding variable and literal string values. This procedure is called string <a href="Concatenation" title="Concatenation">concatenation</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">age% = 10
a$ = "I am " + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34) + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(age%)) + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34) + " years old."
b$ = "How old are you?"
question$ = a$ + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1) + b$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> question$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">I am "10" years old. How old are you?
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Since quotation marks are used to denote the ends of literal strings, <a href="CHR$" title="CHR$">CHR$</a>(34) must be used to place quotes inside them.</dd></dl>
<p>
<i>Example 3:</i> How QB64 string type suffixes can fix the length by adding a number of bytes after it.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">strings$5 = "Hello world"
PRINT strings$5
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello</pre>
</td></tr></tbody></table>
<p>
<i>Example 4:</i> STRING values can be compared by the <a href="ASC_(function)" title="ASC (function)">ASC</a> code value according to <a href="ASCII" title="ASCII">ASCII</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter a letter, number or punctuation mark from the keyboard: ";
valu$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> value$
value1$ = "A"
value2$ = "m"
value3$ = "z"
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> value$
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "A only"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$ <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> value2$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "B to m" 'A is already evaluated
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$, value2$, value3$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "z only" 'A and m are already evaluated
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &gt; value2$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "greater than m but not z" 'z is already evaluated
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "other value" 'key entry below A including all numbers
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> <a class="mw-selflink selflink">STRING</a> values using multiple characters will be compared by the <a href="ASCII" title="ASCII">ASCII</a> code values sequentially from left to right. Once the equivalent code value of one string is larger than the other the evaluation stops. This allows string values to be compared and sorted alphabetically using <a href="Greater_Than" title="Greater Than">&gt;</a> or <a href="Less_Than" title="Less Than">&lt;</a> and to <a href="SWAP" title="SWAP">SWAP</a> values in <a href="Arrays" title="Arrays">arrays</a> irregardless of the string lengths.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="DEFSTR" title="DEFSTR">DEFSTR</a></li>
<li><a href="CHR$" title="CHR$">CHR$</a>, <a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="LTRIM$" title="LTRIM$">LTRIM$</a>, <a href="RTRIM$" title="RTRIM$">RTRIM$</a></li>
<li><a href="LCASE$" title="LCASE$">LCASE$</a>, <a href="UCASE$" title="UCASE$">UCASE$</a></li>
<li><a href="STR$" title="STR$">STR$</a></li>
<li><a href="HEX$" title="HEX$">HEX$</a></li>
<li><a href="MKI$" title="MKI$">MKI$</a>, <a href="MKL$" title="MKL$">MKL$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKD$" title="MKD$">MKD$</a>, <a href="MK$" title="MK$">_MK$</a></li>
<li><a href="CVI" title="CVI">CVI</a>, <a href="CVL" title="CVL">CVL</a>, <a href="CVS" title="CVS">CVS</a>, <a href="CVD" title="CVD">CVD</a>, <a href="CV" title="CV">_CV</a></li>
<li><a href="LEN" title="LEN">LEN</a>, <a href="VAL" title="VAL">VAL</a></li>
<li><a href="ASCII" title="ASCII">ASCII</a>, <a href="DRAW" title="DRAW">DRAW</a></li>
<li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_USING" title="PRINT USING">PRINT USING</a>, <a href="WRITE" title="WRITE">WRITE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031724
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 188/1000000
Post‐expand include size: 2135/2097152 bytes
Template argument size: 242/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.326      1 -total
 20.60%    5.011      1 Template:PageSyntax
 14.36%    3.494     22 Template:Cl
 10.92%    2.656      3 Template:OutputEnd
  9.28%    2.258      1 Template:PageNavigation
  9.00%    2.190      3 Template:OutputStart
  8.78%    2.135      1 Template:PageSeeAlso
  8.35%    2.032      4 Template:CodeStart
  7.73%    1.881      4 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:276-0!canonical and timestamp 20240715031724 and revision id 8170.
 -->
</div>
</div>
</div>
</div>
</body>
</html>