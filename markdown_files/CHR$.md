<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CHR$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CHR rootpage-CHR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CHR$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CHR$</a> function returns the character associated with a certain <a href="ASCII" title="ASCII">character code</a> as a <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">CHR$</a>(<i>code%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Valid ASCII <i>code%</i> numbers range from 0 to 255.</li>
<li>The character code of a character can be found using the <a href="ASC_(function)" title="ASC (function)">ASC (function)</a>.</li>
<li>Some control codes below 32 will not <a href="PRINT" title="PRINT">PRINT</a> or will move the screen cursor, unless <a href="CONTROLCHR" title="CONTROLCHR">_CONTROLCHR OFF</a> is used.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Outputs the characters of several character codes:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(65); <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(65 + 32)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(66); <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(66 + 32)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Aa
Bb
</pre>
</td></tr></tbody></table>
<dl><dd>Explanation: 65 is the ASCII code for "A" and 65 + 32 is the ASCII code for "a". 66 is the ASCII code for "B" and 66 + 32 is the ASCII code for "b"</dd></dl>
<p>
<i>Example 2:</i> To cut down on typing CHR$(???) all day, define often used characters as variables such as Q$ = CHR$(34) as shown.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Q AS <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 1   'define as one byte string(get rid of $ type suffix too)
Q = <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(34)          'Q will now represent the elusive quotation mark in a string
PRINT "This text uses "; Q; "quotation marks"; Q; " that could have caused a syntax error!"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This text uses "quotation marks" that could have caused a syntax error!
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Using <a href="ASC_(function)" title="ASC (function)">ASC</a> and <a class="mw-selflink selflink">CHR$</a> to <i>encrypt</i> a text file size up to 32K bytes
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> FileName$ <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 ' FileName to be encrypted
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1) &lt;= 32000 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> Text$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1), 1) ' get Text as one string
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
Send$ = "" ' clear value
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Text$)
    Letter$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(Text$, i, 1) ' get each character in the text
    Code = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(Letter$)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (Code &gt; 64 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Code &lt; 91) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> (Code &gt; 96 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Code &lt; 123) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        Letter$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(Code + 130) ' change letter's ASCII character by 130
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    Send$ = Send$ + Letter$ ' reassemble string with just letters encrypted
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> FileName$ <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 ' erase FileName to be encrypted
<a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, Send$   ' Text as one string
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Warning: The routine above will change an original text file to be unreadable. Use a second file name to preserve the original file.</i></dd></dl>
<p>
<i>Example 4:</i> <b>Decrypting</b> the above encrypted text file (32K byte file size limit).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> FileName$ <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1       ' FileName to be decrypted
    Text$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<a href="LOF" title="LOF"><span style="color:#4593D8;">LOF</span></a>(1), 1)         ' open Text as one string
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
Send$ = ""
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Text$)
    Letter$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(Text$, i, 1)
    Code = <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(Letter$)
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (Code &gt; 194 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Code &lt; 221) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> (Code &gt; 226 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> Code &lt; 253) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        Letter$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">CHR$</span></a>(Code - 130)  ' change back to a Letter character
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    Send$ = Send$ + Letter$ ' reassemble string as normal letters
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i
<a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> FileName$ <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="OUTPUT" title="OUTPUT"><span style="color:#4593D8;">OUTPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #1 ' Erase file for decrypted text
    <a href="PRINT_(file_statement)" title="PRINT (file statement)"><span style="color:#4593D8;">PRINT</span></a> #1, Send$ ' place Text as one string
<a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Examples 3 and 4 encrypt and decrypt a file up to 32 thousand bytes. <a href="INPUT$" title="INPUT$">INPUT$</a> can only get strings less than 32767 characters. The upper and lower case letter characters are the only ones altered, but the encryption and decryption rely on the fact that most text files do not use the code characters above 193. You could alter any character from ASCII 32 to 125 without problems using the 130 adder. No <a href="ASCII" title="ASCII">ASCII</a> code above 255 is allowed. Don't alter the codes below code 32 as they are control characters. Specifically, characters 13 and 10 (CrLf) may be used for line returns in text files.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ASC" title="ASC">ASC</a>, <a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="ASCII" title="ASCII">ASCII character codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034033
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.053 seconds
Real time usage: 0.068 seconds
Preprocessor visited node count: 502/1000000
Post‐expand include size: 4470/2097152 bytes
Template argument size: 717/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   40.864      1 -total
 13.64%    5.574      2 Template:OutputEnd
 12.88%    5.264     64 Template:Cl
  8.36%    3.418      2 Template:OutputStart
  6.99%    2.858      1 Template:PageSyntax
  6.90%    2.819      1 Template:Small
  5.71%    2.333      4 Template:CodeEnd
  5.45%    2.227      3 Template:Parameter
  5.39%    2.201      4 Template:CodeStart
  5.33%    2.178      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:379-0!canonical and timestamp 20240715034033 and revision id 8113.
 -->
</div>
</div>
</div>
</div>
</body>
</html>