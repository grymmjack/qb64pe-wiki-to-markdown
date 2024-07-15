<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LEFT$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LEFT rootpage-LEFT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LEFT$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LEFT$</a> string function returns a number of characters from the left of a <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LEFT$</a>(<i>stringValue$</i>, <i>numberOfCharacters%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>stringValue$</i> can be any <a href="STRING" title="STRING">STRING</a> literal or variable.</li>
<li><i>numberOfCharacters%</i> <a href="INTEGER" title="INTEGER">INTEGER</a> determines the number of characters to return from left of string.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If the number of characters exceeds the string length the entire string is returned. Use <a href="LEN" title="LEN">LEN</a> to determine a string's length.</li>
<li><a class="mw-selflink selflink">LEFT$</a> returns always start at the first character of the string, even if it's a space. <a href="LTRIM$" title="LTRIM$">LTRIM$</a> can remove leading spaces.</li>
<li><b><i>numberOfCharacters%</i> cannot be a negative value.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Getting the left portion of a string value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">name$ = "Tom Williams"
First$ = LEFT$(name$, 3)
PRINT First$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Tom </pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> A replace function using LEFT$ and <a href="RIGHT$" title="RIGHT$">RIGHT$</a> with <a href="INSTR" title="INSTR">INSTR</a> to insert a different length word into an existing string.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">text$ = "This is my sentence to change my words."
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$
oldword$ = "my"
newword$ = "your"
x = Replace(text$, oldword$, newword$)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$; x
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Replace (text$, old$, new$) 'can also be used as a <a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> without the count assignment
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
  find = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(start + 1, text$, old$) 'find location of a word in text
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> find <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    count = count + 1
    first$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">LEFT$</span></a>(text$, find - 1) 'text before word including spaces
    last$ = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(text$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(text$) - (find + <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(old$) - 1)) 'text after word
    text$ = first$ + new$ + last$
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
  start = find
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> find
Replace = count 'function returns the number of replaced words. Comment out in SUB
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This is my sentence to change my words.
This is your sentence to change your words.</pre>
</td></tr></tbody></table>
<dl><dd><i>Note:</i> The <a href="MID$" title="MID$">MID$</a> statement can only substitute words or sections of the original string length. It cannot change the string length.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RIGHT$" title="RIGHT$">RIGHT$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li>
<li><a href="LTRIM$" title="LTRIM$">LTRIM$</a>, <a href="RTRIM$" title="RTRIM$">RTRIM$</a></li>
<li><a href="INSTR" title="INSTR">INSTR</a>, <a href="LEN" title="LEN">LEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034126
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.034 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 187/1000000
Post‐expand include size: 1974/2097152 bytes
Template argument size: 276/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.818      1 -total
 10.83%    2.905     19 Template:Cl
  8.66%    2.322      1 Template:PageSyntax
  7.97%    2.136      5 Template:Parameter
  7.73%    2.072      2 Template:OutputEnd
  7.48%    2.006      2 Template:CodeEnd
  7.26%    1.948      1 Template:PageParameters
  6.89%    1.848      1 Template:PageDescription
  6.81%    1.826      2 Template:CodeStart
  6.81%    1.825      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:541-0!canonical and timestamp 20240715034126 and revision id 8144.
 -->
</div>
</div>
</div>
</div>
</body>
</html>