<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ALIAS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ALIAS rootpage-ALIAS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ALIAS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>ALIAS</b> clause in a <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a> statement block tells the program the name of the procedure used in the external library.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a>
<dl><dd>SUB <i>pseudoname</i> <a class="mw-selflink selflink">ALIAS</a> <i>actualname</i> [(<i>parameters</i>)]</dd></dl></dd>
<dd><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">END DECLARE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>pseudoname</i> is the name of the <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> the QB64 program will use.</li>
<li>The <i>actualname</i> is the same procedure name as it is inside of the library code, it may optionally have a prepended namespace specification (e.g. <b>ALIAS</b> std::malloc).</li>
<li>QB64 must use all parameters of imported procedures including optional ones.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <b>ALIAS</b> name clause is optional as the original library procedure name can be used.</li>
<li>The procedure name does not have to be inside of quotes when using <a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a>.</li>
<li>QB64 does not support optional parameters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Instead of creating a wrapper <a href="SUB" title="SUB">SUB</a> with the Library statement inside of it, just rename it in the declaration.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>
    <a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">MouseMove</span> <a class="mw-selflink selflink"><span style="color:#4593D8;">ALIAS</span></a> glutWarpPointer (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> xoffset&amp;, <a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> yoffset&amp;)
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> <a href="SCREENEXISTS" title="SCREENEXISTS"><span style="color:#4593D8;">_SCREENEXISTS</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hit a key to move the pointer to top left corner..."</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
<span style="color:#55FF55;">MouseMove</span> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputplain"><b>Explanation</b>
 When a Library procedure is used to represent another procedure name
 use <b>ALIAS</b> instead of creating a wrapper <a href="SUB" title="SUB">SUB</a>. Just place your name for
 the procedure first with the actual Library name after <b>ALIAS</b>.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li>
<li><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a>, <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034019
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.044 seconds
Real time usage: 0.062 seconds
Preprocessor visited node count: 159/1000000
Post‐expand include size: 1661/2097152 bytes
Template argument size: 288/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 53/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.694      1 -total
 11.55%    4.584      1 Template:CodeStart
  9.30%    3.692      1 Template:PreEnd
  8.73%    3.466     11 Template:Cl
  8.17%    3.245      1 Template:PageSyntax
  7.44%    2.955      1 Template:PreStart
  7.10%    2.818      1 Template:PageExamples
  6.55%    2.599      5 Template:Text
  6.24%    2.476      1 Template:PageDescription
  5.79%    2.298      4 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:392-0!canonical and timestamp 20240715034019 and revision id 8792.
 -->
</div>
</div>
</div>
</div>
</body>
</html>