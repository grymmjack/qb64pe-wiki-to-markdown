<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>MID$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MID rootpage-MID skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">MID$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>MID$</b> statement substitutes one or more new characters for existing characters of a previously defined <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">MID$</a>(<i>baseString$</i>, <i>startPosition%</i>[, <i>bytes%</i>]) = <i>replacementString$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>baseString$</i> variable must exist and be large enough to contain the <i>replacementString$</i>.</li>
<li><i>startPosition%</i> specifies the string character position to start the overwrite.</li>
<li><i>bytes%</i> or number of characters is optional. Excess byte lenghts are ignored.</li>
<li>The <i>replacementString$</i> should be as long as the byte length reserved.</li>
<li>The length of the original string is not changed in any case. If <i>replacementString$</i> is longer, it gets clipped.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Using <a href="INSTR" title="INSTR">INSTR</a> to locate the string positions and a <b>MID$</b> statement to change the words.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> text$ = "The cats and dogs were playing, even though dogs don't like cats."
 PRINT text$
 start% = 1          ' start cannot be 0 when used in the INSTR function!
 <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
   position% = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(start%, text$, "dog")
   IF position% THEN            ' when position is a value greater than 0
     <a class="mw-selflink selflink"><span style="color:#4593D8;">MID$</span></a>(text$, position%, 3) = "rat"   ' changes "dog" to "rat" when found
     start% = position% + 1     ' advance one position to search rest of string
   END IF
 LOOP UNTIL position% = 0       ' no other matches found
 PRINT text$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">The cats and dogs were playing, even though dogs don't like cats.
The cats and rats were playing, even though rats don't like cats.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="ASC" title="ASC">ASC</a>, <a href="ASC_(function)" title="ASC (function)">ASC (function)</a></li>
<li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a></li>
<li><a href="INSTR" title="INSTR">INSTR</a>, <a href="ASCII" title="ASCII">ASCII</a>,  <a href="STR$" title="STR$">STR$</a>, <a href="HEX$" title="HEX$">HEX$</a>, <a href="Bitmaps" title="Bitmaps">Bitmaps</a></li>
<li><a href="MKI$" title="MKI$">MKI$</a>, <a href="MKL$" title="MKL$">MKL$</a>, <a href="MKS$" title="MKS$">MKS$</a>, <a href="MKD$" title="MKD$">MKD$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061340
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.040 seconds
Preprocessor visited node count: 86/1000000
Post‐expand include size: 1046/2097152 bytes
Template argument size: 163/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   27.082      1 -total
 10.58%    2.864      1 Template:PageSyntax
 10.54%    2.854      1 Template:PageParameters
 10.10%    2.735     10 Template:Parameter
  8.67%    2.349      1 Template:PageExamples
  8.12%    2.198      1 Template:OutputEnd
  8.11%    2.196      1 Template:CodeStart
  7.56%    2.048      1 Template:OutputStart
  7.56%    2.047      3 Template:Cl
  7.38%    2.000      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:578-0!canonical and timestamp 20240715061340 and revision id 8152.
 -->
</div>
</div>
</div>
</div>
</body>
</html>