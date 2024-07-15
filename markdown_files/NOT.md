<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>NOT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-NOT rootpage-NOT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">NOT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">NOT</a> is a <a href="Boolean" title="Boolean">boolean</a> logical operator that will change a false statement to a true one and vice-versa.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>True</i> = -1: <i>False</i> = <a class="mw-selflink selflink">NOT</a> True</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>In QBasic, True = -1 and False = 0 in boolean logic and evaluation statements.</li>
<li><a class="mw-selflink selflink">NOT</a> evaluates a value and returns the bitwise opposite, meaning that <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">NOT 0 = -1</span>.</li>
<li>Often called a negative logic operator, it returns the opposite of a value as true or false.</li>
<li>Values are changed by their bit values so that each bit is changed to the opposite of on or off. See example 3 below.</li></ul>
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
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a class="mw-selflink selflink">NOT</a> <b>B</b> │ <b>A</b> <a href="AND" title="AND">AND</a> <b>B</b> │ <b>A</b> <a href="OR" title="OR">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a href="EQV" title="EQV">EQV</a> <b>B</b> │ <b>A</b> <a href="IMP" title="IMP">IMP</a> <b>B</b> │
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
<p><i>Example 1:</i> Alternating between two conditions in a program loop.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
switch = <a class="mw-selflink selflink"><span style="color:#4593D8;">NOT</span></a> switch       '<a class="mw-selflink selflink"><span style="color:#4593D8;">NOT</span></a> changes value from -1 to 0 and vice-versa
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 38
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> switch <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "True!" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "False"
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a>
k$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> k$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27) ' escape key quit
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Reading a file until it reaches the End Of File.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">DO WHILE NOT EOF(1)
  INPUT #1, data1, data2, data3
LOOP
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a href="EOF" title="EOF">EOF</a> will return 0 until a file ends. NOT converts 0 to -1 so that the loop continues to run. When EOF becomes -1, NOT converts it to 0 to end the loop.</dd></dl>
<p>
<i>Example 3:</i> So why does <b>NOT 5 = -6</b>? Because NOT changes every bit of a value into the opposite:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">NOT</span></a> 5
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
ReadBits 5
ReadBits -6
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> ReadBits (n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>) 'change type value and i bit reads for other whole type values
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 15 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -1 'see the 16 bit values
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 2 ^ i <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "1"; <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "0";
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">-6
0000000000000101
1111111111111010
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The bit values of an <a href="INTEGER" title="INTEGER">INTEGER</a> are 2 <a href="BYTE" title="BYTE">_BYTEs</a> and each bit is an exponent of 2 from 15 to 0 (16 bits). Thus comparing the numerical value with those exponents using <a href="AND" title="AND">AND</a> reveals the bit values as "1" for bits on or "0" for bits off as text.</dd></dl>
<dl><dd>QB64 can use <a href="%26B" title="&amp;B">&amp;B</a> to convert the above <a href="BIT" title="BIT">_BIT</a> values back to <a href="INTEGER" title="INTEGER">INTEGER</a> or <a href="BYTE" title="BYTE">_BYTE</a> values as shown below:</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">'16 bit INTEGER values from -32768 to 32767
a% = <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>0000000000000101
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a%
b% = <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>1111111111111010
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> b%
'8 bit BYTE values from -128 to 127
a%% = <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>00000101
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a%%
b%% = <a href="%26B" title="&amp;B"><span style="color:#4593D8;">&amp;B</span></a>11111010
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> b%%
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BIT" title="BIT">_BIT</a>, <a href="%26B" title="&amp;B">&amp;B</a>, <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><a href="AND" title="AND">AND</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a>, <a href="OR" title="OR">OR</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715014052
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.074 seconds
Real time usage: 0.099 seconds
Preprocessor visited node count: 333/1000000
Post‐expand include size: 11111/2097152 bytes
Template argument size: 342/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   58.784      1 -total
 21.39%   12.575      1 Template:RelationalOperationsPlugin
 11.84%    6.961      1 Template:LogicalTruthPlugin
  8.76%    5.152      2 Template:FixedStart
  8.31%    4.884     40 Template:Cl
  6.67%    3.923      2 Template:FixedEnd
  5.86%    3.442      4 Template:CodeStart
  5.70%    3.351      1 Template:OutputStart
  5.31%    3.124      1 Template:PageExamples
  5.04%    2.962      1 Template:OutputEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:505-0!canonical and timestamp 20240715014052 and revision id 6124.
 -->
</div>
</div>
</div>
</div>
</body>
</html>