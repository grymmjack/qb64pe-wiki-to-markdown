<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BIN$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BIN rootpage-BIN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BIN$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>This function returns the binary (base 2) representation of any numeric value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>binvalue$</i> = <a class="mw-selflink selflink">_BIN$</a>(<i>number</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>number</i> can be any <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a> or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> value, positive or negative.</li>
<li><i>number</i> can also be any <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> value, but only the integer part of the value is converted in that case. That is, from the value <i>-123.45</i> the function would convert the <i>-123</i> only.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns the base 2 (binary) representation of the given <i>number</i> as <a href="STRING" title="STRING">STRING</a>.</li>
<li>Different from <a href="STR$" title="STR$">STR$</a>, this function does not return a leading sign placeholder space, so no <a href="LTRIM$" title="LTRIM$">LTRIM$</a> to strip that space from positive numbers is necessary.</li>
<li><a href="VAL" title="VAL">VAL</a> can convert the returned bin string value back to a decimal value by prefixing the string with "<a href="%26B" title="&amp;B">&amp;B</a>".
<ul><li>Eg. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">decimal = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;B"</span> + binvalue$)</span>.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v2.1 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Comparing decimal, hexadecimal, octal and binary string values from 0 to 15.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">tabletop$ = <span style="color:#FFB100;">" Decimal | Hexadecimal | Octal | Binary "</span>
tablesep$ = <span style="color:#FFB100;">"---------+-------------+-------+--------"</span>
tableout$ = <span style="color:#FFB100;">"  \ \    |      \\     |   \\  |  \  \  "</span> <span style="color:#919191;">'the PRINT USING template</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">10</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tabletop$
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">10</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tablesep$
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> n% = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">4</span> + n%, <span style="color:#F580B1;">10</span>: <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> tableout$; <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(n%); <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(n%); <a href="OCT$" title="OCT$"><span style="color:#4593D8;">OCT$</span></a>(n%); <a class="mw-selflink selflink"><span style="color:#4593D8;">_BIN$</span></a>(n%)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> n%
</pre>
</td></tr></tbody></table>
<dl><dt>Note</dt>
<dd>Although the decimal numbers 0-15 have a maximum width of 2 digits only, an extra space in the <i>tableout$</i> template is needed when using the (fixed width string) slash output format, as <a href="STR$" title="STR$">STR$</a> values contain a leading sign placeholder space.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">          Decimal | Hexadecimal | Octal | Binary
         ---------+-------------+-------+--------
            0     |      0      |   0   |  0
            1     |      1      |   1   |  1
            2     |      2      |   2   |  10
            3     |      3      |   3   |  11
            4     |      4      |   4   |  100
            5     |      5      |   5   |  101
            6     |      6      |   6   |  110
            7     |      7      |   7   |  111
            8     |      8      |   10  |  1000
            9     |      9      |   11  |  1001
            10    |      A      |   12  |  1010
            11    |      B      |   13  |  1011
            12    |      C      |   14  |  1100
            13    |      D      |   15  |  1101
            14    |      E      |   16  |  1110
            15    |      F      |   17  |  1111
</pre>
</td></tr></tbody></table>
<p>
</p>
<dl><dt>Example 2</dt>
<dd>Converting a binary value to decimal.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">binvalue$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_BIN$</span></a>(<span style="color:#F580B1;">255</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Bin: "</span>; binvalue$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Converting Bin value to Decimal:"</span>; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<span style="color:#FFB100;">"&amp;B"</span> + binvalue$)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Bin: 11111111
Converting Bin value to Decimal: 255
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="HEX$" title="HEX$">HEX$</a>, <a href="OCT$" title="OCT$">OCT$</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="%26B" title="&amp;B">&amp;B</a> (binary), <a href="%26H" title="&amp;H">&amp;H</a> (hexadecimal), <a href="%26O" title="&amp;O">&amp;O</a> (octal), <a href="VAL" title="VAL">VAL</a></li>
<li><a href="Base_Comparisons" title="Base Comparisons">Base Comparisons</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192629
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.053 seconds
Real time usage: 0.102 seconds
Preprocessor visited node count: 332/1000000
Post‐expand include size: 3005/2097152 bytes
Template argument size: 611/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 200/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   75.875      1 -total
 16.02%   12.155      1 Template:PageParameters
  9.25%    7.022      1 Template:PageExamples
  9.11%    6.909      1 Template:InlineCodeEnd
  7.48%    5.678      2 Template:CodeStart
  7.33%    5.561      1 Template:PageNavigation
  6.48%    4.917     17 Template:Text
  5.92%    4.495      2 Template:OutputStart
  4.61%    3.501     18 Template:Cl
  4.09%    3.105      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:681-0!canonical and timestamp 20240714192629 and revision id 8268.
 -->
</div>
</div>
</div>
</div>
</body>
</html>