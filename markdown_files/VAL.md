<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>VAL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-VAL rootpage-VAL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">VAL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>VAL</b> Function returns the decimal numerical equivalent value of a <a href="STRING" title="STRING">STRING</a> numerical value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>value</i> = <b>VAL</b>(<i>string_value$</i>)</dd></dl>
<p>
</p>
<ul><li>VAL converts string numbers to numerical values including decimal point values and prefixed "<a href="%26B" title="&amp;B">&amp;B</a>" binary, "<a href="%26H" title="&amp;H">&amp;H</a>" hexadecimal, "<a href="%26O" title="&amp;O">&amp;O</a>" octal.</li>
<li>VAL conversion stops at non-numeric characters except for letter "D" or "E" exponential notation values.</li></ul>
<dl><dd>String values with "D" and "E" letters between numbers may be converted also! EX: <b><span style="color:green;">VAL("9D4") = 90000</span></b></dd></dl>
<ul><li>If the first string character is not a number VAL returns 0. VAL may return erratic values with "%" or "&amp;" starting characters.</li>
<li>Binary <a href="BIN$" title="BIN$">_BIN$</a> string values with the "<a href="%26B" title="&amp;B">&amp;B</a>" prefix can be converted to a decimal value with digits from 0 to 1 only.</li>
<li>Hexadecimal <a href="HEX$" title="HEX$">HEX$</a> string values with the "<a href="%26H" title="&amp;H">&amp;H</a>" prefix can be converted to a decimal value with digits 0 to 9 and letters A to F, like; dec = VAL("&amp;H"+hexvar$).</li>
<li>Octal <a href="OCT$" title="OCT$">OCT$</a> string values with the "<a href="%26O" title="&amp;O">&amp;O</a>" prefix can be converted to a decimal value with digits from 0 to 7 only.</li>
<li>For character values of <a href="ASCII" title="ASCII">ASCII</a> data use the <a href="ASC_(function)" title="ASC (function)">ASC (function)</a> to get the value.</li>
<li>In QB64 use an <a href="INTEGER" title="INTEGER">INTEGER</a> return variable to hold integer values  returned by VAL <a href="HEX$" title="HEX$">Hex</a> strings: <b><span style="color:green;">value% = VAL("&amp;HFFFF") = -1</span></b></li></ul>
<p>
<i>Example 1:</i> Differences in values returned with QBasic and QB64:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">VAL</span></a>("<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>") '203 in QB, 0 in QB64
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">VAL</span></a>("<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FFFF") ' -1 QB, 65535 in QB64
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">VAL</span></a>("<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FFFF&amp;") '65535 in both
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> A quirk in QBasic returned VAL values of 203 for "&amp;" and "&amp;H" that was never fixed until PDS(7.1).</dd></dl>
<p>
<i>Example 2:</i> Converting a string with some number characters
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> text$ = "1.23Hello"
 number! = VAL(text$)
 PRINT number!
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">1.23
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Converting literal and variable <a href="STRING" title="STRING">string</a> values to numerical values.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> a$ = "33"
 PRINT VAL("10") + VAL(a$) + 1
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">44
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> 10 + 33 + 1 = 44, the strings were converted to values.</dd></dl>
<dl><dd>You have to convert the string to values in order to use them in a mathematical expression also since mixing strings with numbers isn't allowed. VAL will stop at a text letter so VAL("123G56) would return 123.</dd></dl>
<dl><dd>If VAL wasn't used the program would break with an error, as you can't add the value 1 to a string, if the 1 was a string ("1") then the program would return "10331", but now since we used VAL, the numbers were added as they should.</dd></dl>
<p>
<i>Example 4:</i> Converting a hexadecimal value to decimal value using HEX$ with VAL.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> decnumber% = 96
 hexnumber$ = "&amp;H" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(decnumber%)  'convert decimal value to hex and add hex prefix
 PRINT hexnumber$
 decimal% = <a class="mw-selflink selflink"><span style="color:#4593D8;">VAL</span></a>(hexnumber$)
 PRINT decimal%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">&amp;H60
 96
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="HEX$" title="HEX$">HEX$</a> converts a decimal number to hexadecimal, but <a class="mw-selflink selflink">VAL</a> will only recognize it as a valid value with the "&amp;H" prefix. Especially since hexadecimal numbers can use "A" through "F" in them. Create a converter function from this code!</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ASC_(function)" title="ASC (function)">ASC (function)</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="BIN$" title="BIN$">_BIN$</a>, <a href="HEX$" title="HEX$">HEX$</a>, <a href="OCT$" title="OCT$">OCT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062227
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 139/1000000
Post‐expand include size: 1704/2097152 bytes
Template argument size: 197/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 18/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.194      1 -total
 11.73%    2.721      1 Template:PageSyntax
 10.34%    2.399      2 Template:Text
 10.12%    2.347      4 Template:CodeStart
  9.43%    2.186     11 Template:Cl
  9.40%    2.180      3 Template:OutputStart
  8.86%    2.055      2 Template:Parameter
  8.57%    1.987      1 Template:PageSeeAlso
  8.02%    1.860      3 Template:OutputEnd
  7.85%    1.821      4 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:495-0!canonical and timestamp 20240715062227 and revision id 8180.
 -->
</div>
</div>
</div>
</div>
</body>
</html>