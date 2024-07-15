<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SUB - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SUB rootpage-SUB skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SUB</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>A <b>SUB</b> procedure is a procedure within a program that can calculate and return multiple parameter values just like a full program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SUB</a> ProcedureName [(<i>1stParam</i>[, <i>2ndParam</i> ... [, <i>lastParam</i>)]</dd>
<dd>...</dd>
<dd>... 'procedure variable definitions and statements</dd>
<dd>...</dd>
<dd><a href="END_SUB" title="END SUB">END SUB</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Parameters passed after the procedure call must match the variable types in the SUB parameters in order.</li>
<li>If there are no <i>parameter</i>s passed or they are <a href="SHARED" title="SHARED">SHARED</a> the parameters and parenthesis are not required in the procedure.</li>
<li>Parameter <a href="Variable" title="Variable">Variable</a> names in the procedure do not have to match the names used in the <a href="CALL" title="CALL">CALL</a>, just the value types.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All <a href="$DYNAMIC" title="$DYNAMIC">dynamic</a> <a href="Variable" title="Variable">variable</a> values return to 0 or null strings when the procedure is exited except for <a href="STATIC" title="STATIC">STATIC</a> variable values.</li>
<li>SUB procedures can return multiple values through the parameters unlike functions.</li>
<li>SUB procedures return to the next code statement after the call in the main or other procedures.</li>
<li><a href="EXIT" title="EXIT">EXIT</a> SUB can be used to exit early or to exit before <a href="GOSUB" title="GOSUB">GOSUB</a> procedures using <a href="RETURN" title="RETURN">RETURN</a>.</li>
<li><a href="TYPE" title="TYPE">TYPE</a> and <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a> declarations can be made inside of SUB procedures in QB64 only.</li>
<li>SUB procedures can save program memory as all memory used in a SUB is released on procedure exit except for <a href="STATIC" title="STATIC">STATIC</a> values.</li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a> can be used to define all new or old QB64 variable <a href="TYPE" title="TYPE">TYPE</a> definitions instead of DEF***.</li>
<li><a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> text library files with needed SUB and <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures can be included in programs after all sub-procedures.</li>
<li><b>QB64 ignores all procedural DECLARE statements.</b> Define all <i>parameter</i> <a href="TYPE" title="TYPE">TYPEs</a> in the SUB procedure.</li>
<li><b>Images are not deallocated when the <a class="mw-selflink selflink">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li></ul>
<p>
<i>Example 1:</i> Text <a href="PRINT" title="PRINT">PRINT</a> screen centering using <a href="PEEK" title="PEEK">PEEK</a> to find the SCREEN mode width. Call and SUB procedure code:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
Center 10, 15, "This text is centered." ' example module sub call
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z ' only code allowed before SUB line is a DEF statement or a comment
<a class="mw-selflink selflink"><span style="color:#4593D8;">SUB</span></a> Center (Tclr, Trow, Text$)
Columns = <a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">_WIDTH</span></a> / <a href="FONTWIDTH" title="FONTWIDTH"><span style="color:#4593D8;">_FONTWIDTH</span></a> 'Convert _WIDTH (in pixels) to width in characters
Middle = (Columns \ 2) + 1 ' reads any screen mode width
Tcol = Middle - (<a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(Text$) \ 2)
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> Tclr: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> Trow, Tcol: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Text$; ' end semicolon prevents screen roll
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The procedure centers text printed to the screen. The parameters are the text color, row and the text itself as a string or string variable. The maximum width of the screen mode in characters is found and divided in half to find the center point. The text string's length is also divided in half and subtracted from the screen's center position. The procedure will also work when the <a href="WIDTH" title="WIDTH">WIDTH</a> statement has been used. When adding variables to Text$ use the + concatenation operator. Not semicolons!</dd></dl>
<p>
<i>Example 2:</i> SUB and <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures always return to the place they were called in the main or other sub-procedures:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = 10
Add1 a
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a  'Add1 returns final 'a' value here
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">SUB</span></a> Add1 (n)
n = n + 1
Add2 n
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "exit 1"
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">SUB</span></a> Add2 (m)
m = m + 2
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "exit 2"
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">exit 2
exit 1
 13
</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> Parameter <b>a</b> is used to call the sub-procedures even though parameters <b>n</b> and <b>m</b> are used internally.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="FUNCTION" title="FUNCTION">FUNCTION</a>, <a href="CALL" title="CALL">CALL</a></li>
<li><a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="EXIT" title="EXIT">EXIT</a>, <a href="END" title="END">END</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192557
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 180/1000000
Post‐expand include size: 1856/2097152 bytes
Template argument size: 233/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.118      1 -total
 12.10%    3.040      3 Template:Parameter
 10.27%    2.579     20 Template:Cl
  9.51%    2.389      1 Template:PageSyntax
  8.78%    2.206      2 Template:CodeEnd
  7.51%    1.886      1 Template:OutputStart
  7.51%    1.886      1 Template:OutputEnd
  7.50%    1.885      1 Template:PageNavigation
  7.49%    1.882      2 Template:CodeStart
  7.39%    1.855      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:289-0!canonical and timestamp 20240714192557 and revision id 7432.
 -->
</div>
</div>
</div>
</div>
</body>
</html>