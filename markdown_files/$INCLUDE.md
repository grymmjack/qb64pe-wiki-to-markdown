<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$INCLUDE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_INCLUDE rootpage-_INCLUDE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$INCLUDE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">$INCLUDE</a> is a metacommand that is used to insert a source code file into your program which is then executed at the point of the insertion.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd>{<a href="REM" title="REM">REM</a> | <a href="Apostrophe" title="Apostrophe">'</a> } <a class="mw-selflink selflink">$INCLUDE</a><b>:</b> '<i>sourceFile</i>'</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>QBasic <a href="Metacommand" title="Metacommand">metacommands</a> must be commented with <a href="REM" title="REM">REM</a> or an apostrophe.</li>
<li>The <i>sourceFile</i> name must be enclosed in apostrophes and can include a path.</li>
<li>$INCLUDE is often used to add functions and subs from an external text QBasic code library.</li>
<li>The $INCLUDE metacommand should be the only statement on a line.</li></ul>
<h3><span id="How_to_.24INCLUDE_a_BAS_or_Text_file_with_a_QB64_Program"></span><span class="mw-headline" id="How_to_$INCLUDE_a_BAS_or_Text_file_with_a_QB64_Program">How to $INCLUDE a BAS or Text file with a QB64 Program</span></h3>
<ul><li>Assemble the code to be reused into a file.</li>
<li>Common extensions are <b>.BI</b> (for declarations, usually included in the beginning of a program) or <b>.BM</b> (with SUBs and FUNCTIONs, usually included at the end of a program).
<ul><li>Any extension can be used, as long as the file contains code in plain text (binary files are not accepted).</li></ul></li>
<li>$INCLUDE any <a href="DIM" title="DIM">DIM</a>, <a href="CONST" title="CONST">CONST</a>, <a href="SHARED" title="SHARED">SHARED</a> arrays or <a href="DATA" title="DATA">DATA</a> at the <b>beginning</b> of the main program code.</li>
<li>$INCLUDE <a href="SUB" title="SUB">SUBs</a> or <a href="FUNCTION" title="FUNCTION">FUNCTIONs</a> at the bottom of the main program code <b>after any SUB procedures.</b>
<ul><li><b>Note:</b> <a href="TYPE" title="TYPE">TYPE</a> definitions, <a href="DATA" title="DATA">DATA</a> and <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a> can be placed inside of sub-procedures.</li></ul></li>
<li><b>Compile</b> the program.</li>
<li><i>Note: Once the program is compiled, the included text files are no longer needed with the program EXE.</i></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><b> '$INCLUDE:</b> 'QB.BI'</pre>
</td></tr></tbody></table>
<h3><span class="mw-headline" id="More_examples">More examples</span></h3>
<ul><li><a href="SelectScreen" title="SelectScreen">SelectScreen</a></li>
<li><a href="FILELIST$" title="FILELIST$">FILELIST$</a></li>
<li><a href="SaveImage_SUB" title="SaveImage SUB">SaveImage SUB</a></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INTERRUPT" title="INTERRUPT">INTERRUPT</a>, <a href="INTERRUPTX" title="INTERRUPTX">INTERRUPTX</a></li>
<li><a href="TYPE" title="TYPE">TYPE</a>, <a href="DIM" title="DIM">DIM</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommand</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714180055
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 61/1000000
Post‐expand include size: 678/2097152 bytes
Template argument size: 20/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.651      1 -total
 15.65%    3.231      1 Template:PageSyntax
 12.73%    2.629      2 Template:Parameter
 11.60%    2.395      1 Template:CodeStart
 11.46%    2.366      1 Template:PageDescription
 11.08%    2.289      1 Template:PageNavigation
 10.72%    2.214      1 Template:PageSeeAlso
 10.57%    2.183      1 Template:CodeEnd
 10.57%    2.182      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:303-0!canonical and timestamp 20240714180054 and revision id 8655.
 -->
</div>
</div>
</div>
</div>
</body>
</html>