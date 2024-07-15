<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SELECT CASE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SELECT_CASE rootpage-SELECT_CASE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SELECT CASE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">SELECT CASE</a> is used to determine the program flow by comparing the value of a variable to specific CASE values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>SELECT</b> [EVERY]<b>CASE</b> <i>testExpression</i>
<dl><dd><b>CASE</b> <i>expressionList1</i>
<dl><dd>[statement-block1]</dd></dl></dd>
<dd>[<b>CASE</b> <i>expressionList2</i>
<dl><dd>[statement-block2...</dd></dl></dd>
<dd>[<b>CASE ELSE</b>
<dl><dd>[statementblock-n</dd></dl></dd></dl></dd>
<dd><b>END SELECT</b></dd></dl>
<p>
</p>
<ul><li><b>SELECT CASE</b> evaluates <i>testExpression</i> and executes the first matching <a class="mw-redirect" href="CASE" title="CASE">CASE</a> or <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE">CASE ELSE</a> block and exits.</li>
<li><b>SELECT EVERYCASE</b> allows the execution of all matching <a class="mw-redirect" href="CASE" title="CASE">CASE</a> blocks from top to bottom or the <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE">CASE ELSE</a> block.</li>
<li>The literal, variable or expression <i>testExpression</i> comparison can result in any string or numerical type.</li>
<li><b>Note:</b> A <i>testExpression</i> variable value can be changed inside of true CASE evaluations in SELECT EVERYCASE.</li>
<li>A <i>testExpression</i> derived from an expression or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> will only be determined once at the start of the block execution.</li>
<li>Supports individual CASE values and ranges or lists of literal values as below:
<ul><li><b>CASE</b> casevalue: code <span style="color:#777777;">'<b>case compares one numerical or text value</b></span></li>
<li><b>CASE</b> casevalue1 <a href="TO" title="TO">TO</a> casevalue2: code <span style="color:#777777;">'<b>case compares a range of values </b></span></li>
<li><b>CASE</b> casevalue1, casevalue2, casevalue3: code <span style="color:#777777;">'<b>case compares a list of values separated by commas</b></span></li>
<li><b>CASE IS</b> &gt; casevalue: code <span style="color:#777777;">'<b>case compares a value as  =, &lt;&gt;, &lt; or &gt; </b></span></li>
<li><b>CASE ELSE</b>: code <span style="color:#777777;">'<b>bottom case statement executes only when no other CASE is executed.</b></span></li></ul></li>
<li>The CASE values should cover the normal ranges of the comparison <i>testExpression</i> values.</li>
<li>Use <b>CASE ELSE</b> before <b>END SELECT</b> if an alternative is necessary when no other case matches.</li>
<li>CASEs should be listed in an ascending or descending values for best and fastest results.</li>
<li><a href="STRING" title="STRING">STRING</a> comparisons will be based on their respective <a href="ASCII" title="ASCII">ASCII</a> code values where capital letters are valued less than lower case.</li>
<li>Use <b>SELECT CASE</b> when <a href="IF...THEN" title="IF...THEN">IF...THEN</a> statements get too long or complicated.</li>
<li><b>SELECT CASE</b> and <b>EVERYCASE</b> statement blocks must <b>always</b> be ended with <a href="END_SELECT" title="END SELECT">END SELECT</a>.</li>
<li>Use <b><a href="Colon" title="Colon">colons</a></b> to execute multiple statements in one line.</li>
<li>An <b><a href="Underscore" title="Underscore">underscore</a></b> can be used anywhere after the code on one line to continue it to the next line in <b>QB64</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> SELECT CASE can use literal or variable <a href="STRING" title="STRING">STRING</a> or numerical values in CASE comparisons:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a whole number value from 1 to 40: ", value
value1 = 10
value2 = 20
value3 = 30
<a class="mw-selflink selflink"><span style="color:#4593D8;">SELECT CASE</span></a> value
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Ten only"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> value2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "11 to 20 only" '10 is already evaluated
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1, value2, value3: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "30 only" '10 and 20 are already evaluated
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &gt; value2: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "greater than 20 but not 30" '30 is already evaluated
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Other value" 'values less than 10
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The first true CASE is executed and SELECT CASE is exited. "Other value" is printed for values less than 10.</dd></dl>
<p>
<i>Example 2:</i> SELECT CASE will execute the first CASE statement that is true and ignore all CASE evaluations after that:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = 100
<a class="mw-selflink selflink"><span style="color:#4593D8;">SELECT CASE</span></a> a          'designate the value to compare
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1, 3, 5, 7, 9
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 10
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 50
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 100
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will be displayed when a equals 100"
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "(and no other case will be checked)"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &lt; 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown as a previous case was true"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 50 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown as a previous case was true"
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>
   <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will only print if it gets this far!"
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This will be displayed when a equals 100
(and no other case will be checked)
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The first case where a value is true is shown, the remainder are skipped. Try changing the value of <i>a</i>.</dd></dl>
<p>
<i>Example 3:</i> Same as Example 2 but, SELECT EVERYCASE will execute every CASE statement that is true.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = 100
<a class="mw-selflink selflink"><span style="color:#4593D8;">SELECT EVERYCASE</span></a> a          'designate the value to compare
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1, 3, 5, 7, 9
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 10
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 50
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 100
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will be displayed when a equals 100"
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "(and other cases will be checked)"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will not be shown."
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &lt; 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will be shown as 100 is less than 150"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 50 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 150
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will be shown as 100 is between 50 and 150"
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>
   <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This will only print if no other CASE is true!"
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">This will be displayed when a equals 100
(and other cases will be checked)
This will be shown as 100 is less than 150
This will be shown as 100 is between 50 and 150
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE">CASE ELSE</a> will only execute if no other CASE was true. See Example 5 for more usages.</dd></dl>
<p>
<i>Example 4:</i> SELECT CASE evaluates string values by the <a href="ASC_(function)" title="ASC (function)">ASC</a> code value according to <a href="ASCII" title="ASCII">ASCII</a>.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter a letter, number or punctuation mark from the keyboard: ";
value$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> value$
value1$ = "A"
value2$ = "m"
value3$ = "z"
<a class="mw-selflink selflink"><span style="color:#4593D8;">SELECT CASE</span></a> value$
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "A only"
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$ <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> value2$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "B to m" 'A is already evaluated
  <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> value1$, value2$, value3$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "z only" 'A and m are already evaluated
  <a class="mw-redirect" href="CASE_IS" title="CASE IS"><span style="color:#4593D8;">CASE IS</span></a> &gt; value2$: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "greater than m but not z" 'z is already evaluated
  <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "other value" 'key entry below A including all numbers
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> <a href="STRING" title="STRING">STRING</a> values using multiple characters will be compared by the <a href="ASCII" title="ASCII">ASCII</a> code values sequentially from left to right. Once the equivalent code value of one string is larger than the other the evaluation stops. This allows string values to be compared and sorted alphabetically using <a href="Greater_Than" title="Greater Than">&gt;</a> or <a href="Less_Than" title="Less Than">&lt;</a> and to <a href="SWAP" title="SWAP">SWAP</a> values in <a href="Arrays" title="Arrays">arrays</a> regardless of the string lengths.</dd></dl>
<p>
<i>Example 5:</i> EVERYCASE is used to draw sections of digital numbers in a simulated LED readout using numbers from 0 to 9:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 12
DO
  <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 1, 1: <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a number 0 to 9: ", num
  <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
  <a class="mw-selflink selflink"><span style="color:#4593D8;">SELECT EVERYCASE</span></a> num
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 3, 5 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 20), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12,12" 'top horiz
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 4 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6, 8, 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 20), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'left top vert
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 6, 8: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 54), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12, 12" 'left bot vert
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 6, 8, 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 54), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12, 12" 'middle horiz
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 4, 7 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (54, 20), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'top right vert
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 1, 3 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 9: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (54, 54), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "F2D30G2H2U30E2BD5P12,12" 'bottom right vert
    <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0, 2, 3, 5, 6, 8: <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (20, 88), 12
      <a href="DRAW" title="DRAW"><span style="color:#4593D8;">DRAW</span></a> "E2R30F2G2L30H2BR5P12,12" 'bottom horiz
    <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE"><span style="color:#4593D8;">CASE ELSE</span></a>
      <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 20, 20: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Goodbye!"; num
  <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> num &gt; 9
</pre>
</td></tr></tbody></table>
<dl><dd><b>Note:</b> <a class="mw-redirect" href="CASE_ELSE" title="CASE ELSE">CASE ELSE</a> will only execute if no other CASE is true! Changing the comparison value in a CASE may affect later CASE evaluations. <b>Beware of duplicate variables inside of cases affecting the comparison values and remaining cases.</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="IF...THEN" title="IF...THEN">IF...THEN</a>, <a href="Boolean" title="Boolean">Boolean</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031527
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.056 seconds
Real time usage: 0.067 seconds
Preprocessor visited node count: 858/1000000
Post‐expand include size: 7179/2097152 bytes
Template argument size: 1515/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 27/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   37.252      1 -total
 17.01%    6.336    108 Template:Cl
  7.33%    2.730      5 Template:Text
  7.27%    2.709      2 Template:OutputEnd
  6.69%    2.491      2 Template:OutputStart
  6.68%    2.489      8 Template:Parameter
  6.43%    2.394      1 Template:PageSyntax
  5.90%    2.198      5 Template:CodeEnd
  5.83%    2.170      1 Template:PageSeeAlso
  5.71%    2.126      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:383-0!canonical and timestamp 20240715031527 and revision id 8591.
 -->
</div>
</div>
</div>
</div>
</body>
</html>