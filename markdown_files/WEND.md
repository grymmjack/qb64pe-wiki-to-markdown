<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>WHILE...WEND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-WHILE_WEND rootpage-WHILE_WEND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">WHILE...WEND</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">WHILE...WEND</a> statement is used to repeat a block of statements while the condition is met.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-redirect" href="WHILE" title="WHILE">WHILE</a> <i>condition</i></dd>
<dd>.</dd>
<dd>.</dd>
<dd>.</dd>
<dd><a class="mw-redirect" href="WEND" title="WEND">WEND</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>condition</i> is a numeric expression used to determine if the loop will execute.</li>
<li><i>statements</i> will execute repeatedly while <i>condition</i> is a non-zero value.</li>
<li><a href="EXIT" title="EXIT">EXIT</a> WHILE can be used for emergency exits from the loop in QB64 only.</li>
<li>A <a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a> can use the same DO WHILE condition to get the same results.</li>
<li>WHILE loops only run if the WHILE condition is True.</li></ul>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">         Table 3: The relational operations for condition checking.
 In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to compare. Both must represent
 the same general type, i.e. they must result into either numerical values
 or <a href="STRING" title="STRING">STRING</a> values. If a test succeeds, then <b>true</b> (-1) is returned, <b>false</b> (0)
     if it fails, which both can be used in further <a href="Boolean" title="Boolean">Boolean</a> evaluations.
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                          <b><a href="Relational_Operations" title="Relational Operations">Relational Operations</a></b>                          │
 ├────────────┬───────────────────────────────────────────┬────────────────┤
 │ <b>Operation</b>  │                <b>Description</b>                │ <b>Example usage</b>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Equal" title="Equal">=</a> B    │ Tests if A is <b>equal</b> to B.                 │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Equal" title="Equal">=</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Not_Equal" title="Not Equal">&lt;&gt;</a> B   │ Tests if A is <b>not equal</b> to B.             │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Not_Equal" title="Not Equal">&lt;&gt;</a> B <a href="THEN" title="THEN">THEN</a> │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Less_Than" title="Less Than">&lt;</a> B    │ Tests if A is <b>less than</b> B.                │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Less_Than" title="Less Than">&lt;</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Greater_Than" title="Greater Than">&gt;</a> B    │ Tests if A is <b>greater than</b> B.             │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Greater_Than" title="Greater Than">&gt;</a> B <a href="THEN" title="THEN">THEN</a>  │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Less_Than_Or_Equal" title="Less Than Or Equal">&lt;=</a> B   │ Tests if A is <b>less than or equal</b> to B.    │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Less_Than_Or_Equal" title="Less Than Or Equal">&lt;=</a> B <a href="THEN" title="THEN">THEN</a> │
 ├────────────┼───────────────────────────────────────────┼────────────────┤
 │   A <a href="Greater_Than_Or_Equal" title="Greater Than Or Equal">&gt;=</a> B   │ Tests if A is <b>greater than or equal</b> to B. │ <a class="mw-redirect" href="IF" title="IF">IF</a> A <a href="Greater_Than_Or_Equal" title="Greater Than Or Equal">&gt;=</a> B <a href="THEN" title="THEN">THEN</a> │
 └────────────┴───────────────────────────────────────────┴────────────────┘
   The operations should be very obvious for numerical values. For strings
   be aware that all checks are done <b>case sensitive</b> (i.e. "Foo" &lt;&gt; "foo").
   The <b>equal</b>/<b>not equal</b> check is pretty much straight forward, but for the
   <b>less</b>/<b>greater</b> checks the <a href="ASCII" title="ASCII">ASCII</a> value of the first different character is
                          used for decision making:
   <b>E.g.</b> "abc" is <b>less</b> than "abd", because in the first difference (the 3rd
        character) the "c" has a lower <a href="ASCII" title="ASCII">ASCII</a> value than the "d".
   This behavior may give you some subtle results, if you are not aware of
                   the <a href="ASCII" title="ASCII">ASCII</a> values and the written case:
   <b>E.g.</b> "abc" is <b>greater</b> than "abD", because the small letters have higher
        <a href="ASCII" title="ASCII">ASCII</a> values than the capital letters, hence "c" &gt; "D". You may use
        <a href="LCASE$" title="LCASE$">LCASE$</a> or <a href="UCASE$" title="UCASE$">UCASE$</a> to make sure both strings have the same case.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Reading an entire file. Example assumes the program has a <a href="OPEN" title="OPEN">file opened</a> as #1
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPEN" title="OPEN"><span style="color:#4593D8;">OPEN</span></a> "Readme.txt" FOR <a class="mw-redirect" href="INPUT_(file_mode)" title="INPUT (file mode)"><span style="color:#4593D8;">INPUT</span></a> AS #1
<a class="mw-selflink selflink"><span style="color:#4593D8;">WHILE</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="EOF" title="EOF"><span style="color:#4593D8;">EOF</span></a>(1)
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 1                                    'limit line prints to one per second
    <a href="LINE_INPUT_(file_statement)" title="LINE INPUT (file statement)"><span style="color:#4593D8;">LINE INPUT #</span></a>1, text$
    IF <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) THEN <a href="EXIT" title="EXIT"><span style="color:#4593D8;">EXIT</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a>        'ESC key exits
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> text$
<a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Example 2:</i> Clearing the keyboard buffer.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; "" : <a class="mw-redirect" href="WEND" title="WEND"><span style="color:#4593D8;">WEND</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DO...LOOP" title="DO...LOOP">DO...LOOP</a></li>
<li><a href="FOR...NEXT" title="FOR...NEXT">FOR...NEXT</a></li>
<li><a href="UNTIL" title="UNTIL">UNTIL</a></li>
<li><a href="CONTINUE" title="CONTINUE">_CONTINUE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714153958
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 158/1000000
Post‐expand include size: 6151/2097152 bytes
Template argument size: 233/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.753      1 -total
 28.37%    6.740      1 Template:RelationalOperationsPlugin
  9.20%    2.184     16 Template:Cl
  8.38%    1.991      1 Template:PageSyntax
  7.48%    1.778      4 Template:Parameter
  7.34%    1.743      1 Template:FixedStart
  7.30%    1.733      1 Template:FixedEnd
  6.82%    1.619      1 Template:PageExamples
  6.73%    1.598      1 Template:PageNavigation
  6.69%    1.590      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:551-0!canonical and timestamp 20240714153958 and revision id 7708.
 -->
</div>
</div>
</div>
</div>
</body>
</html>