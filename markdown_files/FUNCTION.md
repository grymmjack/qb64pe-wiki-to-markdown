<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>FUNCTION - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-FUNCTION rootpage-FUNCTION skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">FUNCTION</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>A <a class="mw-selflink selflink">FUNCTION</a> block statement is used to create a function procedure to return a calculated value to a program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>FUNCTION procedureName</b>[type-suffix] [(<i>parameters</i>)]
<dl><dd><i>{code}</i></dd>
<dd>'variable definitions and procedure statements</dd>
<dd>⋮</dd>
<dd>procedureName = returnValue</dd></dl></dd>
<dd><b>END FUNCTION</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function type can be any variable type that it will return to the program and is represented by the type suffix.</li>
<li>Functions hold one return value in the function's name which is a variable type. Other values can be passed through <i>parameters</i>.</li>
<li>Functions are often referred to in program calculations, not called like SUB procedures. <a href="CALL" title="CALL">CALL</a> cannot be used with functions.</li>
<li>If there are no parameters passed or they are <a href="SHARED" title="SHARED">SHARED</a> the <i>parameters</i> and parenthesis are not required.</li>
<li>Variable names within the procedure do not have to match the names used in the reference parameters, just the value types.</li>
<li>To pass parameter variables <a class="mw-redirect" href="BYVAL" title="BYVAL">by value</a> to protect the value in a call, parenthesis can be placed around each variable name also.</li>
<li>To pass <a href="Arrays" title="Arrays">arrays</a> to a sub-procedure use empty brackets after the name or indicate the index in the call.</li>
<li>All <a href="$DYNAMIC" title="$DYNAMIC">dynamic</a> variable values return to 0 or null strings when the procedure is exited except when a variable or the entire function is <a href="STATIC" title="STATIC">STATIC</a>. This can save program memory as all <a href="$DYNAMIC" title="$DYNAMIC">dynamic</a> memory used in a FUNCTION is released on procedure exit.</li>
<li>FUNCTION procedure code can use <a href="GOSUB" title="GOSUB">GOSUB</a> and <a href="GOTO" title="GOTO">GOTO</a> line numbers or labels inside of the procedure when necessary.</li>
<li>For early function exits use <a href="EXIT" title="EXIT">EXIT</a> <a class="mw-selflink selflink">FUNCTION</a> before <a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION">END FUNCTION</a> and <a href="GOSUB" title="GOSUB">GOSUB</a> procedures using <a href="RETURN" title="RETURN">RETURN</a>.</li>
<li><b>QB64 ignores all procedural DECLARE statements.</b> Define all <i>parameter</i> <a href="Data_types" title="Data types">types</a> in the FUNCTION procedure.</li>
<li><b>Images are not deallocated when the <a href="SUB" title="SUB">SUB</a> or <a class="mw-selflink selflink">FUNCTION</a> they are created in ends. Free them with <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a>.</b></li>
<li>The IDE can create the FUNCTION and END FUNCTION lines for you. Use the <i>New FUNCTION...</i> option in the Edit Menu. A box will come up for you to enter a name for the FUNCTION. Enter all code between the FUNCTION and <a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION">END FUNCTION</a> lines.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Once a FUNCTION was created and used, the QBasic IDE would DECLARE it when the file was saved. <b>QB64 doesn't need these declarations.</b></li>
<li>QBasic's IDE could place a <a href="DEFINT" title="DEFINT">DEFINT</a>, <a href="DEFSNG" title="DEFSNG">DEFSNG</a>, <a href="DEFLNG" title="DEFLNG">DEFLNG</a>, <a href="DEFDBL" title="DEFDBL">DEFDBL</a> or <a href="DEFSTR" title="DEFSTR">DEFSTR</a> statement before the FUNCTION line if it is used in the main module. It may even be the wrong variable type needed.</li>
<li>QBasic allowed programmers to add DATA fields anywhere because the IDE separated the main code from other procedures.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> A simple function that returns the current path. Place <a class="mw-selflink selflink">FUNCTION</a> or <a href="SUB" title="SUB">SUB</a> procedures after the program <a href="END" title="END">END</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Current path = "; PATH$
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">FUNCTION</span></a> PATH$
    f% = <a href="FREEFILE" title="FREEFILE"><span style="color:#4593D8;">FREEFILE</span></a>
    file$ = "D0Spath.inf" 'file name uses a zero to prevent an overwrite of existing file name
    <a href="SHELL" title="SHELL"><span style="color:#4593D8;">SHELL</span></a> <a href="HIDE" title="HIDE"><span style="color:#4593D8;">_HIDE</span></a> "CD &gt; " + file$ 'send screen information to a created text file
    <a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> file$ <a class="mw-redirect" href="FOR_(file_statement)" title="FOR (file statement)"><span style="color:#4593D8;">FOR</span></a> <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> #f% 'file should exist with one line of text
    <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT</span></a> #f%, PATH$ 'read file path text to function name
    <a href="CLOSE" title="CLOSE"><span style="color:#4593D8;">CLOSE</span></a> #f%
    <a href="KILL" title="KILL"><span style="color:#4593D8;">KILL</span></a> file$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Returns a <a href="LONG" title="LONG">LONG</a> array byte size required for a certain sized graphics screen pixel area <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a screen mode: ", mode%
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter image width: ", wide&amp;
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter image depth: ", deep&amp;
IntegerArray&amp; = ImageBufferSize&amp;(wide&amp;, deep&amp;, mode%) \ 2 ' returns size of an <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a> array.
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> IntegerArray&amp;
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a class="mw-selflink selflink"><span style="color:#4593D8;">FUNCTION</span></a> ImageBufferSize&amp; (Wide&amp;, Deep&amp;, ScreenMode%)
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> ScreenMode%
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1: BPPlane = 2: Planes = 1
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2, 3, 4, 11: BPPlane = 1: Planes = 1
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 7, 8, 9, 12: BPPlane = 1: Planes = 4
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 10: BPPlane = 1: Planes = 2
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 13: BPPlane = 8: Planes = 1
        <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: BPPlane = 0
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    ImageBufferSize&amp; = 4 + <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>((Wide&amp; * BPPlane + 7) / 8) * (Deep&amp; * Planes) 'return the value to function name.
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Function calculates the array byte size required when you <a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> an area of a graphics <a href="SCREEN" title="SCREEN">SCREEN</a>. Each mode may require a different sized array. Since graphics uses <a href="INTEGER" title="INTEGER">INTEGER</a> arrays, 2 byte elements, the size returned is divided by 2 in the IntegerArray&amp; calculation function reference. Function returns only 4 for <a href="SCREEN" title="SCREEN">SCREEN</a> 0 which is a text only mode.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SUB" title="SUB">SUB</a>, <a href="SCREEN" title="SCREEN">SCREEN</a></li>
<li><a href="EXIT" title="EXIT">EXIT</a> (statement), <a href="END" title="END">END</a></li>
<li><a href="EXIT_(function)" title="EXIT (function)">_EXIT (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192438
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.051 seconds
Real time usage: 0.067 seconds
Preprocessor visited node count: 273/1000000
Post‐expand include size: 2452/2097152 bytes
Template argument size: 422/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.129      1 -total
 15.81%    4.606     32 Template:Cl
 12.14%    3.535      1 Template:PageExamples
 11.28%    3.285      2 Template:CodeEnd
 10.96%    3.192      1 Template:PageSyntax
 10.21%    2.973      1 Template:PageSeeAlso
  9.60%    2.796      2 Template:CodeStart
  9.00%    2.622      1 Template:PageNavigation
  8.90%    2.591      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:290-0!canonical and timestamp 20240714192438 and revision id 6773.
 -->
</div>
</div>
</div>
</div>
</body>
</html>