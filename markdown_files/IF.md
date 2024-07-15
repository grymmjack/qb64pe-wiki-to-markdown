<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>IF...THEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-IF_THEN rootpage-IF_THEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">IF...THEN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">IF...THEN</a> statements make boolean (true or false) evaluations to automate program decision making.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<h3><span class="mw-headline" id="Single-line">Single-line</span></h3>
<dl><dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>conditionStatement</i> <a href="THEN" title="THEN">THEN</a> <i>{code}</i> <a href="ELSE" title="ELSE">ELSE</a> <i>{alternativeCode}</i></dd>
<dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>conditionStatement</i> <a href="GOTO" title="GOTO">GOTO</a> <i>lineLabel</i></dd></dl>
<h3><span class="mw-headline" id="Block">Block</span></h3>
<dl><dd><a class="mw-redirect" href="IF" title="IF">IF</a> <i>conditionStatement</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a href="ELSEIF" title="ELSEIF">ELSEIF</a> <i>conditionStatement2</i> <a href="THEN" title="THEN">THEN</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a href="ELSE" title="ELSE">ELSE</a>
<dl><dd><i>{code}</i></dd>
<dd>⋮</dd></dl></dd>
<dd><a class="mw-redirect" href="END_IF" title="END IF">END IF</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <i>conditionStatement</i> evaluation by <a class="mw-redirect" href="IF" title="IF">IF</a> must be true (-1) or a <b>non-zero numerical value</b> for the <a href="THEN" title="THEN">THEN</a> <i>{code}</i> to be executed.</li>
<li>Multiple conditional evaluations can be made using inclusive <a href="AND_(boolean)" title="AND (boolean)">AND</a> or alternative <a href="OR_(boolean)" title="OR (boolean)">OR</a> conditional expressions.</li>
<li><a href="THEN" title="THEN">THEN</a> is not required when <a href="GOTO" title="GOTO">GOTO</a> is used to send program flow to a line number or label.</li>
<li><a class="mw-redirect" href="IF" title="IF">IF</a> statements can also have alternative evaluations using <a href="ELSEIF" title="ELSEIF">ELSEIF</a> and <a href="ELSE" title="ELSE">ELSE</a> conditions.</li>
<li>When the <a class="mw-redirect" href="IF" title="IF">IF</a> statement and/or code to be run is more than code line, an <a class="mw-redirect" href="END_IF" title="END IF">END IF</a> statement must be used.</li>
<li>With multiple code lines to run, end the IF statement with THEN and place all of the code on lines below that line.</li>
<li>Multiple code line block statements require that the <a class="mw-selflink selflink">IF...THEN</a>, <a href="ELSEIF" title="ELSEIF">ELSEIF</a>, <a href="ELSE" title="ELSE">ELSE</a> and <a class="mw-redirect" href="END_IF" title="END IF">END IF</a> be on separate lines.</li>
<li><b>The IDE may return an error of <i><a href="NEXT" title="NEXT">NEXT</a> without <a href="FOR" title="FOR">FOR</a></i> or <i><a href="LOOP" title="LOOP">LOOP</a> without <a href="DO...LOOP" title="DO...LOOP">DO</a></i> when <a class="mw-redirect" href="END_IF" title="END IF">END IF</a> does not end a statement block.</b></li>
<li>The <b>QB64</b> IDE will indicate an error in the IF statement line until END IF closes the statement block.</li>
<li>Use <a href="Colon" title="Colon">colons</a> to execute multiple statements in a single-line IF statement.</li>
<li>An <b><a href="Underscore" title="Underscore">underscore</a></b> can be used anywhere after the code on a single-line to continue it to the next line in <b>QB64</b>.</li>
<li><b>NOTE:</b> <a href="STRING" title="STRING">STRING</a> values can only be evaluated in an IF statement if a value is compared to a literal or <a href="CHR$" title="CHR$">CHR$</a> string value. <b>QB64 may not compile literal IF string statements or indicate an IDE coding error.</b> Use <a href="LEN" title="LEN">LEN</a> or <a href="ASC_(function)" title="ASC (function)">ASC</a> to compare strings numerically.</li></ul>
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
<p>
</p>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><ul><li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a> can be used to add extra conditions to a boolean statement evaluation.</li>
<li><a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a> can be used to add alternate conditions to a boolean statement evaluation.</li>
<li>Parenthesis are allowed inside of boolean statements to clarify an evaluation.</li></ul></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
<p>
</p>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a href="NOT" title="NOT">NOT</a> <b>B</b> │ <b>A</b> <a href="AND" title="AND">AND</a> <b>B</b> │ <b>A</b> <a href="OR" title="OR">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a href="EQV" title="EQV">EQV</a> <b>B</b> │ <b>A</b> <a href="IMP" title="IMP">IMP</a> <b>B</b> │
  ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
  │ <b>true</b>  │ <b>true</b>  │ false │  true   │ true   │  false  │  true   │  true   │
  ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
  │ <b>true</b>  │ <b>false</b> │ true  │  false  │ true   │  true   │  false  │  false  │
  ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
  │ <b>false</b> │ <b>true</b>  │ false │  false  │ true   │  true   │  false  │  true   │
  ├───────┼───────┼───────┼─────────┼────────┼─────────┼─────────┼─────────┤
  │ <b>false</b> │ <b>false</b> │ true  │  false  │ false  │  false  │  true   │  true   │
  └───────┴───────┴───────┴─────────┴────────┴─────────┴─────────┴─────────┘
   <b>Note:</b> In most BASIC languages incl. QB64 these are <b>bitwise</b> operations,
         hence the logic is performed for each corresponding bit in both
         operators, where <b>true</b> or <b>false</b> indicates whether a bit is <b>set</b> or
         <b>not set</b>. The outcome of each bit is then placed into the respective
         position to build the bit pattern of the final result value.
   As all <a href="Relational_Operations" title="Relational Operations">Relational Operations</a> return negative one (-1, <b>all bits set</b>) for
    <b>true</b> and zero (0, <b>no bits set</b>) for <b>false</b>, this allows us to use these
    bitwise logical operations to invert or combine any relational checks,
    as the outcome is the same for each bit and so always results into a
            <b>true</b> (-1) or <b>false</b> (0) again for further evaluations.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> In a one line IF statement, only <a href="REM" title="REM">REM</a> can be used to comment out the action without an <a class="mw-redirect" href="END_IF" title="END IF">END IF</a> error:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number over or under 100: ", x
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x &gt; 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x &gt; 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="REM" title="REM"><span style="color:#4593D8;">REM</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x <i> '</i>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> IF statement blocks require that the IF THEN and END IF statements be separate from the code executed.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number over or under 100: ", x
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x &gt; 100 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  y = 200
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> y
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> True or False evaluation of a numerical value executes only when the value is not 0. <b>Cannot evaluate <a href="STRING" title="STRING">STRING</a> values.</b>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number or just hit Enter: ", x
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x
</pre>
</td></tr></tbody></table>
<dl><dd>Example will only print if a numerical value is True (positive or negative). (Equivalent to: IF x &gt; 0 OR x &lt; 0 THEN evaluation)</dd></dl>
<p>
<i>Example 4:</i> Multiple evaluations using parenthesis to determine the order.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number over or under 100 or 50: ", value
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> (value% &gt; 100 <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> value% &lt; 200) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> value% = 50 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "OK"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 5:</i> Using multiple IF options in a one line statement.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number over or under 200: ", x
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x &gt; 200 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "High" <span style="color:#4593D8;"><a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a></span> x &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Low" <span style="color:#4593D8;"><a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a></span> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "OK"
</pre>
</td></tr></tbody></table>
<p>
<i>Example 6:</i> <a href="STRING" title="STRING">STRING</a> values can be compared using greater than, less than, not equal to or equal to operators only.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PRINT "Press a letter key: ";
Key$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
PRINT Key$
IF Key$ &gt;= <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(65) AND Key$ &lt;= <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(90) THEN PRINT "A to Z"
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Long <a href="STRING" title="STRING">STRING</a> expression values are compared by their cumulative <a href="ASCII" title="ASCII">ASCII</a> code values.</dd></dl>
<p>
</p>
<ul><li>Floating decimal point numerical values may not be compared as exactly the same value. QB64 will compare them the same.</li></ul>
<dl><dd><i>Example:</i> QBasic would print <i>unequal</i> in the IF comparison code below even though it is exactly the same value printed.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">x# = 5 / 10
y# = 6 / 10
z# = x# + y#
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x#, y#, z#
<a class="mw-selflink selflink"><span style="color:#4593D8;">IF</span></a> x# + y# = z# <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "equal" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "unequal"
</pre>
</td></tr></tbody></table>
<dl><dd>Note: QB64 will make the calculation correctly and print <i>equal</i>. Change older program code that relies on the error accordingly.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ELSEIF" title="ELSEIF">ELSEIF</a>, <a href="ELSE" title="ELSE">ELSE</a></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a>, <a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a></li>
<li><a href="NOT" title="NOT">NOT</a>, <a href="GOTO" title="GOTO">GOTO</a></li>
<li><a href="SELECT_CASE" title="SELECT CASE">SELECT CASE</a></li>
<li><a href="Boolean" title="Boolean">Boolean</a> <span style="color:#777777;">(numerical comparisons return a true or false value)</span></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714180352
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.083 seconds
Real time usage: 0.101 seconds
Preprocessor visited node count: 404/1000000
Post‐expand include size: 11681/2097152 bytes
Template argument size: 762/2097152 bytes
Highest expansion depth: 5/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.122      1 -total
 18.59%    9.689      1 Template:RelationalOperationsPlugin
 10.46%    5.450     44 Template:Cl
  8.94%    4.661      1 Template:LogicalTruthPlugin
  8.08%    4.213      1 Template:PageDescription
  6.50%    3.388      1 Template:PageSyntax
  5.58%    2.908      5 Template:Parameter
  5.43%    2.830      7 Template:CodeStart
  5.42%    2.824      1 Template:PageSeeAlso
  5.26%    2.743      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:380-0!canonical and timestamp 20240714180352 and revision id 8134.
 -->
</div>
</div>
</div>
</div>
</body>
</html>