<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RIGHT$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RIGHT rootpage-RIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RIGHT$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>RIGHT$</b> function returns a set number of characters in a <a href="STRING" title="STRING">STRING</a> variable starting from the end and counting backwards.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>RIGHT$(</b><i>stringvalue$, numberofcharacters%</i><b>)</b></dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>stringvalue$</i> can be any string of <a href="ASCII" title="ASCII">ASCII</a> characters as a <a href="STRING" title="STRING">STRING</a> variable.</li>
<li>The <i>numberofcharacters</i> <a href="INTEGER" title="INTEGER">INTEGER</a> value determines the number of characters to return from the right end of the string.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the number of characters exceeds the string length(<a href="LEN" title="LEN">LEN</a>) the entire string is returned.</li>
<li>RIGHT$ returns always start at the last character of the string, even if a space. <a href="RTRIM$" title="RTRIM$">RTRIM$</a> can remove ending spaces.</li>
<li><b>Number of characters cannot be a negative value.</b></li></ul>
<p>
<i>Example 1:</i> Getting the right portion of a string value such as a person's last name.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">name$ = "Tom Williams"
Last$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">RIGHT$</span></a>(name$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(name$) - <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(name$, " ")) 'subtract space position from string length
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Last$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Williams </pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Adding the leading zero in single digit <a href="HEX$" title="HEX$">HEX$</a> values using RIGHT to take the right two hexadecimal string digits.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32) '32 bit screen modes ONLY!
red = 255
green = 0
blue = 128
Color32 red, green, blue
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Colored text"
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> Color32 (R, G, B)
R = R <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FF: G = G <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FF: B = B <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FF '    limit values to 0 to 255
hexadecimal$ = "<a href="%26H" title="&amp;H"><span style="color:#4593D8;">&amp;H</span></a>FF" + <a class="mw-selflink selflink"><span style="color:#4593D8;">RIGHT$</span></a>("0" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(R), 2) + <a class="mw-selflink selflink"><span style="color:#4593D8;">RIGHT$</span></a>("0" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(G), 2) + <a class="mw-selflink selflink"><span style="color:#4593D8;">RIGHT$</span></a>("0" + <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(B), 2)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> hexadecimal$
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(hexadecimal$)
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"><b><span style="color:white;">&amp;HFFFF0080</span></b>
<b><span style="color:#FF0080;">Colored text</span></b></pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> When a single hexadecimal digit is returned the resulting value will need the leading zero added. Otherwise the hexa- decimal value created will have a byte missing from the value. EX: Color &amp;HFF000000 is valid while &amp;HFF000 is not.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="LTRIM$" title="LTRIM$">LTRIM$</a>, <a href="RTRIM$" title="RTRIM$">RTRIM$</a></li>
<li><a href="INSTR" title="INSTR">INSTR</a>, <a href="HEX$" title="HEX$">HEX$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192536
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.035 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 220/1000000
Post‐expand include size: 2227/2097152 bytes
Template argument size: 282/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.088      1 -total
 11.63%    2.568     25 Template:Cl
  9.19%    2.029      1 Template:PageSyntax
  8.98%    1.983      2 Template:Text
  8.09%    1.786      1 Template:PageParameters
  7.85%    1.733      2 Template:CodeStart
  7.83%    1.729      1 Template:PageNavigation
  7.64%    1.687      1 Template:PageDescription
  7.43%    1.642      1 Template:PageSeeAlso
  7.42%    1.639      2 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:258-0!canonical and timestamp 20240714192536 and revision id 8163.
 -->
</div>
</div>
</div>
</div>
</body>
</html>