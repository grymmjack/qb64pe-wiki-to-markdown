<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>ELSEIF - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ELSEIF rootpage-ELSEIF skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">ELSEIF</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">ELSEIF</a> is used in an <a href="IF...THEN" title="IF...THEN">IF...THEN</a> block statement to offer an alternative condition.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>condition</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-selflink selflink">ELSEIF</a> <i>condition2</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a href="ELSE" title="ELSE">ELSE</a>
<dl><dd><i>{alternative-code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-redirect" href="END_IF" title="END IF">END IF</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>ELSEIF statements require a <b>separate</b> code block line with <a href="THEN" title="THEN">THEN</a> for each alternative condition.</li>
<li>There can be more than one <a href="ELSE" title="ELSE">ELSE</a> IF statement in a single-line IF statement.</li>
<li>If there is only one possible alternative condition (such as 0 or <a href="NOT" title="NOT">NOT</a> 0), use <a href="ELSE" title="ELSE">ELSE</a> instead.</li>
<li>If the comparisons are based on multiple conditions being true, it may require many ELSEIF comparisons. ELSE could help cover some of those conditions.</li>
<li>You can use <a href="SELECT_CASE" title="SELECT CASE">SELECT CASE</a> when IF blocks have a long list of alterative ELSEIF conditions.</li></ul>
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
<p><i>Example 1:</i> IF statement using ELSE IF in one statement line.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
IF x = 100 THEN COLOR 10: PRINT x ELSE IF x &gt; 100 THEN COLOR 12: PRINT x ELSE PRINT "&lt; 100"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> IF statement block
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
IF x = 100 THEN ' must place ANY code on next line!
  COLOR 10: PRINT x
ELSEIF x &gt; 100 THEN COLOR 12: PRINT x
ELSE : PRINT "&lt; 100"
END IF
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1313" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="ELSE" title="ELSE">ELSE</a>, <a class="mw-redirect" href="END_IF" title="END IF">END IF</a></li>
<li><a href="IF...THEN" title="IF...THEN">IF...THEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061300
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 38/1000000
Post‐expand include size: 5273/2097152 bytes
Template argument size: 19/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   31.041      1 -total
 28.49%    8.845      2 Template:Parameter
 20.08%    6.233      1 Template:RelationalOperationsPlugin
  9.21%    2.859      1 Template:PageSyntax
  7.92%    2.459      1 Template:PageDescription
  6.27%    1.947      2 Template:CodeStart
  6.09%    1.889      2 Template:CodeEnd
  6.03%    1.873      1 Template:PageNavigation
  6.00%    1.862      1 Template:PageExamples
  5.92%    1.838      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:381-0!canonical and timestamp 20240715061300 and revision id 8933.
 -->
</div>
</div>
</div>
</div>
</body>
</html>