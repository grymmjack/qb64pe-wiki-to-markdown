<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>XOR (boolean) - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-XOR_boolean rootpage-XOR_boolean skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">XOR (boolean)</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">XOR</a> evaluates two conditions and if either of them is True then it returns True, if both of them are True then it returns False, if both of them are False then it returns False.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>condition</i> <a class="mw-selflink selflink">XOR</a> <i>condition2</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Either <i>condition</i> or <i>condition2</i> must be True for the evaluation to return True.</li>
<li>It is called <b>"exclusive OR"</b> because the conditions cannot both be True for it to return True like the <a href="OR_(boolean)" title="OR (boolean)">OR</a> evaluation.</li>
<li><i>condition</i> and <i>condition2</i> can themselves contain XOR evaluations.</li></ul>
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
<p><i>Example:</i> Dilemma...
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
True = <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> False
AndersWon = True
PeterWon = True
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> AndersWon = True <a class="mw-selflink selflink"><span style="color:#4593D8;">XOR</span></a> PeterWon = True <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Thank you for your honesty!"
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "You can't both have won (or lost)!"
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">You can't both have won (or lost)!
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a>, <a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a></li>
<li><a href="IF...THEN" title="IF...THEN">IF...THEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192616
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.049 seconds
Preprocessor visited node count: 112/1000000
Post‐expand include size: 5739/2097152 bytes
Template argument size: 138/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   32.883      1 -total
 23.87%    7.850      1 Template:RelationalOperationsPlugin
  7.83%    2.575      1 Template:PageSyntax
  7.38%    2.425      6 Template:Parameter
  7.28%    2.394      8 Template:Cl
  6.36%    2.090      1 Template:FixedStart
  6.23%    2.050      1 Template:PageDescription
  5.92%    1.947      1 Template:CodeEnd
  5.84%    1.920      1 Template:FixedEnd
  5.79%    1.903      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:605-0!canonical and timestamp 20240714192616 and revision id 6634.
 -->
</div>
</div>
</div>
</div>
</body>
</html>