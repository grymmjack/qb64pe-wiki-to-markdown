<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_INSTRREV - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INSTRREV rootpage-INSTRREV skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_INSTRREV</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_INSTRREV</a> function searches for a substring inside another string, but unlike <a href="INSTR" title="INSTR">INSTR</a> it searches from right to left.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>position%</i> = <a class="mw-selflink selflink">_INSTRREV</a>([<i>start%</i>,] <i>baseString$</i>, <i>subString$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The optional literal or variable <a href="INTEGER" title="INTEGER">INTEGER</a> <i>start%</i> indicates where in the <i>baseString$</i> the search must start, counted from the left.</li>
<li>The <i>baseString$</i> is a literal or variable <a href="STRING" title="STRING">STRING</a> value to be searched for an exact match including <a href="UCASE$" title="UCASE$">letter cases</a>.</li>
<li>The <i>subString$</i> is a literal or variable <a href="STRING" title="STRING">STRING</a> value being searched.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The function returns the <i>position%</i> in the <i>baseString$</i> where the <i>subString$</i> was found, from right to left.</li>
<li><i>position%</i> will be 0 if the search found no matches in the base string.</li>
<li><a class="mw-selflink selflink">_INSTRREV</a> returns 0 if an empty <i>baseString$</i> is passed, and returns <a href="LEN" title="LEN">LEN</a>(<i>baseString$</i>) with an empty <i>subString$</i>.</li>
<li>The <i>start%</i> position is useful when making multiple searches in the same string. See the example below.</li>
<li>The <i>subString$</i> should be smaller or equal in <a href="LEN" title="LEN">length</a> to the <i>baseString$</i>, or 0 is returned.</li>
<li>A <i>start%</i> value of 0 or less starts search from the end of the <i>baseString$</i> (same as not passing a <i>start%</i> parameter).</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Separating a file name from a full path.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">fullPath$ = "C:\Documents and Settings\Administrator\Desktop\qb64\internal\c\libqb\os\win\libqb_1_2_000000000000.o"
file$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(fullPath$, <a class="mw-selflink selflink"><span style="color:#4593D8;">_INSTRREV</span></a>(fullPath$, "\") + 1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> file$
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">libqb_1_2_000000000000.o
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Searching for multiple instances of a substring inside a base string, going from the end to the start.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">sentence$ = " This is a string full of spaces, including at start and end... "
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> sentence$
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    findPrevSpace% = <a class="mw-selflink selflink"><span style="color:#4593D8;">_INSTRREV</span></a>(findPrevSpace% - 1, sentence$, <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(1))
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> findPrevSpace% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 4, 1
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "No more spaces"
        <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 2, findPrevSpace%
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "^"
    totalSpaces = totalSpaces + 1
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> findPrevSpace% = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 4, 1
        <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Last space found at position 1"
        <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Total spaces found: "; totalSpaces
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> This is a string full of spaces, including at start and end...
^    ^  ^ ^      ^    ^  ^       ^         ^  ^     ^   ^      ^
Last space found at position 1
Total spaces found: 13
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1269" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a>, <a href="INSTR" title="INSTR">INSTR</a></li>
<li><a href="SPACE$" title="SPACE$">SPACE$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062540
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.056 seconds
Real time usage: 0.082 seconds
Preprocessor visited node count: 294/1000000
Post‐expand include size: 2450/2097152 bytes
Template argument size: 442/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   54.142      1 -total
 13.32%    7.210      1 Template:PageSyntax
 11.25%    6.092     25 Template:Cl
  8.50%    4.602     21 Template:Parameter
  7.66%    4.146      2 Template:CodeEnd
  6.77%    3.663      1 Template:PageDescription
  6.00%    3.248      1 Template:PageParameters
  5.95%    3.220      2 Template:OutputEnd
  5.85%    3.165      2 Template:OutputStart
  5.81%    3.148      2 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:159-0!canonical and timestamp 20240715062540 and revision id 8920.
 -->
</div>
</div>
</div>
</div>
</body>
</html>