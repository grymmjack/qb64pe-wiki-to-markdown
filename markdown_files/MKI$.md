<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MKI$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MKI rootpage-MKI skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MKI$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">MKI$</a> function encodes an <a href="INTEGER" title="INTEGER">INTEGER</a> numerical value into a 2-byte <a href="ASCII" title="ASCII">ASCII</a> <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">MKI$</a>(<i>integerVariableOrLiteral%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>integerVariableOrLiteral%</i> is converted to two ASCII characters.</li>
<li><a href="INTEGER" title="INTEGER">INTEGER</a> values can range from -32768 to 32767.</li>
<li>MKI$ string values can be converted back to numerical INTEGER values using <a href="CVI" title="CVI">CVI</a>.</li>
<li>The function takes up less byte space in a file than using the text numerical value when the value is over 2 digits.</li>
<li>When a variable value is used with <a href="PUT" title="PUT">PUT</a> a numerical value is converted automatically in <a href="RANDOM" title="RANDOM">RANDOM</a> and <a class="mw-redirect" href="BINARY" title="BINARY">BINARY</a> files.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> How MKI$ creates a two byte string integer value to save file space.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12    '_PRINTSTRING requires a graphic screen mode
DO
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 14: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 13, 20: <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter an Integer from 1 to 32767(0 quits): ", number%
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> number% &lt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  A$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(number% <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 256)   'first digit(0 to 255)
  B$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(number% \ 256)     'second digit(0 to 127)
  MKIvalue$ = A$ + B$
  Q$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(34)
  strng$ = "<a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(" + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(number% <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 256)) + ") + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(" + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(number% \ 256)) + ")"
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> 11
  <a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (222, 252), <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(number%) + " = " + strng$
  <a href="PRINTSTRING" title="PRINTSTRING"><span style="color:#4593D8;">_PRINTSTRING</span></a> (252, 300), "<a class="mw-selflink selflink"><span style="color:#4593D8;">MKI$</span></a> value = " + Q$ + MKIvalue$ + Q$ 'print ASCII characters
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> INPUT in QB64 limits integer entries to 32767 maximum. MOD 256 finds the part of a value from 0 to 255 while the second value is the number of times that 256 can go into the value. <a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> can print all of the <a href="ASCII" title="ASCII">ASCII</a> characters.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MKD$" title="MKD$">MKD$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKL$" title="MKL$">MKL$</a></li>
<li><a href="CVD" title="CVD">CVD</a>, <a href="CVI" title="CVI">CVI</a>, <a href="CVS" title="CVS">CVS</a>, <a href="CVL" title="CVL">CVL</a></li>
<li><a href="MK$" title="MK$">_MK$</a>, <a href="CV" title="CV">_CV</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192510
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 219/1000000
Post‐expand include size: 2192/2097152 bytes
Template argument size: 343/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.845      1 -total
 12.10%    3.731     26 Template:Cl
 11.96%    3.690      1 Template:PageSyntax
  9.89%    3.049      3 Template:Parameter
  8.77%    2.705      1 Template:PageDescription
  8.57%    2.644      1 Template:PageExamples
  8.54%    2.635      1 Template:CodeEnd
  8.08%    2.492      1 Template:CodeStart
  7.69%    2.371      1 Template:Small
  7.23%    2.231      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:536-0!canonical and timestamp 20240714192510 and revision id 7911.
 -->
</div>
</div>
</div>
</div>
</body>
</html>