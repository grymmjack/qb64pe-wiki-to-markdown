<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OR rootpage-OR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">OR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">OR</a> numerical operator returns a comparative bit value of 1 if either value's bit is on.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = firstValue <a class="mw-selflink selflink">OR</a> secondValue</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>If both bits are off, it returns 0.</li>
<li>If one or both bits are on then it returns 1.</li>
<li><a class="mw-selflink selflink">OR</a> never turns off a bit and can be used only to turn a bit on.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a href="NOT" title="NOT">NOT</a> <b>B</b> │ <b>A</b> <a href="AND" title="AND">AND</a> <b>B</b> │ <b>A</b> <a class="mw-selflink selflink">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a href="EQV" title="EQV">EQV</a> <b>B</b> │ <b>A</b> <a href="IMP" title="IMP">IMP</a> <b>B</b> │
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
<p><i>Example 1:</i> OR always turns bits on! Never off.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> a% = 5 ' 101 binary
 b% = 4 ' 100 binary
 results% = a% <a class="mw-selflink selflink"><span style="color:#4593D8;">OR</span></a> b%  ' still 101 binary using OR
 <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Results% ="; results%
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> Results% = 5
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Turning a data register bit on.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">   address% = 888    'parallel port data register
   bytevalue% = <a href="INP" title="INP"><span style="color:#4593D8;">INP</span></a>(address%)
   <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> address%, bytevalue% <a class="mw-selflink selflink"><span style="color:#4593D8;">OR</span></a> 4
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The third register bit is only turned on if it was off. This ensures that a bit is set. OR could set more bits on with a sum of bit values such as: OUT address%, 7 would turn the first, second and third bits on. 1 + 2 + 4 = 7</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="AND" title="AND">AND</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a>, <a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192519
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.040 seconds
Real time usage: 0.056 seconds
Preprocessor visited node count: 74/1000000
Post‐expand include size: 4507/2097152 bytes
Template argument size: 36/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   35.829      1 -total
 26.14%    9.365      1 Template:LogicalTruthPlugin
  9.24%    3.312      1 Template:FixedStart
  8.38%    3.003      1 Template:PageSyntax
  6.85%    2.454      1 Template:PageExamples
  6.76%    2.421      1 Template:Parameter
  6.53%    2.341      1 Template:PageNavigation
  6.51%    2.331      1 Template:PageDescription
  6.33%    2.269      2 Template:CodeStart
  6.20%    2.221      5 Template:Cl
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:506-0!canonical and timestamp 20240714192519 and revision id 7352.
 -->
</div>
</div>
</div>
</div>
</body>
</html>