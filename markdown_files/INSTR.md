<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INSTR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INSTR rootpage-INSTR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INSTR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INSTR</a> function searches for the first occurence of a search <a href="STRING" title="STRING">STRING</a> within a base string and returns the position it was found.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>position%</i> = <a class="mw-selflink selflink">INSTR</a>([<i>start%</i>,] <i>baseString$</i>, <i>searchString$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The optional literal or variable <a href="INTEGER" title="INTEGER">INTEGER</a> <i>start%</i> indicates where in the <i>baseString$</i> the search must start.</li>
<li>The <i>baseString$</i> is a literal or variable <a href="STRING" title="STRING">STRING</a> value to be searched for an exact match including <a href="UCASE$" title="UCASE$">letter cases</a>.</li>
<li>The <i>searchString$</i> is a literal or variable <a href="STRING" title="STRING">STRING</a> value being searched.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns the <i>position%</i> in the <i>baseString$</i> where the <i>searchString$</i> was found.</li>
<li><i>position%</i> will be 0 if the search found no matches in the base string.</li>
<li><a class="mw-selflink selflink">INSTR</a> returns 0 if an empty <i>baseString$</i> is passed, and returns 1 with an empty <i>searchString$</i>.</li>
<li>The <i>start%</i> position is useful when making multiple searches in the same string. See the example below.</li>
<li>The <i>searchString$</i> should be smaller or equal in <a href="LEN" title="LEN">length</a> to the <i>baseString$</i>, or 0 is returned.</li>
<li>Non-zero <i>position%</i> return values can be used as a new start position by adding 1 to re-search the base string. See the example below.</li>
<li>In a loop, INSTR can search an entire file for occurences of certain words. See the <a href="MID$" title="MID$">MID$</a> statement example.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>The <i>start%</i> position had to be at least 1 or greater when used or there will be an <a href="ERROR_Codes" title="ERROR Codes">Illegal function call</a> error. In <b>QB64</b>, a <i>start%</i> value of 0 or negative is interpreted as 1 and doesn't generate an error.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Reading more than one instance of a word in a string using the INSTR return value as the start value plus 1.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">text$ = "The cats and dogs where playing, even though dogs don't like cats."
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  findcats% = <a class="mw-selflink selflink"><span style="color:#4593D8;">INSTR</span></a>(findcats% + 1, text$, "cats") ' find another occurance after
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> findcats% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "There is 'cats' in the string at position:"; findcats%
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> findcats% = 0
findmonkey% = <a class="mw-selflink selflink"><span style="color:#4593D8;">INSTR</span></a>(text$, "monkeys")  ' find any occurance?
PRINT findmonkey%; "'monkeys' were found so it returned:"; findmonkey%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">There is 'cats' in the string at position: 5
There is 'cats' in the string at position: 62
 0 'monkeys' were found so INSTR returned: 0
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> When the INSTR return value is 0 there are no more instances of a string in a string so the search loop is exited.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="INSTRREV" title="INSTRREV">_INSTRREV</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a></li>
<li><a href="LCASE$" title="LCASE$">LCASE$</a>, <a href="UCASE$" title="UCASE$">UCASE$</a></li>
<li><a href="STRING" title="STRING">STRING</a>, <a href="INTEGER" title="INTEGER">INTEGER</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192449
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.054 seconds
Real time usage: 0.086 seconds
Preprocessor visited node count: 218/1000000
Post‐expand include size: 1443/2097152 bytes
Template argument size: 275/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   55.515      1 -total
 17.00%    9.435      1 Template:PageParameters
 12.54%    6.964      1 Template:PageExamples
  9.17%    5.091     20 Template:Parameter
  7.52%    4.173      8 Template:Cl
  7.26%    4.030      1 Template:PageDescription
  7.02%    3.896      1 Template:PageSyntax
  5.70%    3.164      1 Template:OutputStart
  5.49%    3.048      1 Template:CodeEnd
  5.45%    3.027      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:375-0!canonical and timestamp 20240714192449 and revision id 8386.
 -->
</div>
</div>
</div>
</div>
</body>
</html>