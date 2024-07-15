<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OCT$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OCT rootpage-OCT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">OCT$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>This function returns the octal (base 8) representation of any numeric value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>octvalue$</i> = <a class="mw-selflink selflink">OCT$</a>(<i>number</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>number</i> can be any <a href="INTEGER" title="INTEGER">INTEGER</a>, <a href="LONG" title="LONG">LONG</a> or <a href="INTEGER64" title="INTEGER64">_INTEGER64</a> value, positive or negative.</li>
<li><i>number</i> can also be any <a href="SINGLE" title="SINGLE">SINGLE</a>, <a href="DOUBLE" title="DOUBLE">DOUBLE</a> or <a href="FLOAT" title="FLOAT">_FLOAT</a> value, but only the integer part of the value is converted in that case. That is, from the value <i>-123.45</i> the function would convert the <i>-123</i> only.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns the base 8 (octal) representation of the given <i>number</i> as <a href="STRING" title="STRING">STRING</a>.</li>
<li>Different from <a href="STR$" title="STR$">STR$</a>, this function does not return a leading sign placeholder space, so no <a href="LTRIM$" title="LTRIM$">LTRIM$</a> to strip that space from positive numbers is necessary.</li>
<li><a href="VAL" title="VAL">VAL</a> can convert the returned oct string value back to a decimal value by prefixing the string with "<a href="%26O" title="&amp;O">&amp;O</a>".
<ul><li>Eg. <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">decimal = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>("&amp;O" + octvalue$)</span>.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Comparing decimal, hexadecimal, octal and binary string values from 0 to 15.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">tabletop$ = " Decimal | Hexadecimal | Octal | Binary "
tablesep$ = "---------+-------------+-------+--------"
tableout$ = "  \ \    |      \\     |   \\  |  \  \  " 'the PRINT USING template
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 2, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tabletop$
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 3, 10: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> tablesep$
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> n% = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 15
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 4 + n%, 10: <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> tableout$; <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(n%); <a href="HEX$" title="HEX$"><span style="color:#4593D8;">HEX$</span></a>(n%); <a class="mw-selflink selflink"><span style="color:#4593D8;">OCT$</span></a>(n%); <a href="BIN$" title="BIN$"><span style="color:#4593D8;">_BIN$</span></a>(n%)
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
<dd>Converting a octal value to decimal.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">octvalue$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">OCT$</span></a>(255)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Oct: "; octvalue$
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Converting Oct value to Decimal:"; <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>("&amp;O" + octvalue$)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Oct: 377
Converting Oct value to Decimal: 255
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BIN$" title="BIN$">_BIN$</a>, <a href="HEX$" title="HEX$">HEX$</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="%26B" title="&amp;B">&amp;B</a>, <a href="%26H" title="&amp;H">&amp;H</a>, <a href="%26O" title="&amp;O">&amp;O</a>, <a href="VAL" title="VAL">VAL</a></li>
<li><a href="Base_Comparisons" title="Base Comparisons">Base Comparisons</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061347
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.041 seconds
Real time usage: 0.075 seconds
Preprocessor visited node count: 185/1000000
Post‐expand include size: 2070/2097152 bytes
Template argument size: 210/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   59.503      1 -total
 17.57%   10.455      1 Template:PageSeeAlso
 15.74%    9.365     18 Template:Cl
  8.04%    4.783      1 Template:PageParameters
  5.79%    3.446      2 Template:OutputEnd
  5.18%    3.081      1 Template:PageSyntax
  5.12%    3.045      1 Template:PageDescription
  5.05%    3.004      1 Template:PageExamples
  5.00%    2.975      1 Template:PageNavigation
  4.86%    2.890      5 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:530-0!canonical and timestamp 20240715061347 and revision id 7628.
 -->
</div>
</div>
</div>
</div>
</body>
</html>