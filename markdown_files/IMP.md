<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>IMP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-IMP rootpage-IMP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">IMP</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">IMP</a> logical operator converts the result of two comparative values and returns a bit result.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <i>firstValue</i> <a class="mw-selflink selflink">IMP</a> <i>secondValue</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns a different result from <a href="AND" title="AND">AND</a>, <a href="OR" title="OR">OR</a> or <a class="mw-redirect" href="XOR" title="XOR">XOR</a> - see truth table below.</li>
<li>Evaluates if <i>firstValue</i> <i><b>imp</b>lies</i> <i>secondValue</i>.
<ul><li>If <i>firstValue</i> is true then <i>secondValue</i> must also be true.</li>
<li>So if <i>firstValue</i> is true, and <i>secondValue</i> false, then the condition is false, otherwise it is true (see table below).</li></ul></li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a href="NOT" title="NOT">NOT</a> <b>B</b> │ <b>A</b> <a href="AND" title="AND">AND</a> <b>B</b> │ <b>A</b> <a href="OR" title="OR">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a href="EQV" title="EQV">EQV</a> <b>B</b> │ <b>A</b> <a class="mw-selflink selflink">IMP</a> <b>B</b> │
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
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Binary" title="Binary">Binary</a></li>
<li><a href="Boolean" title="Boolean">Boolean</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061319
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 55/1000000
Post‐expand include size: 4144/2097152 bytes
Template argument size: 90/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   16.873      1 -total
 35.00%    5.906      1 Template:LogicalTruthPlugin
 14.14%    2.386      1 Template:PageSyntax
 12.34%    2.082      9 Template:Parameter
 11.42%    1.927      1 Template:PageNavigation
 11.34%    1.913      1 Template:FixedStart
 11.27%    1.901      1 Template:PageSeeAlso
 11.13%    1.878      1 Template:FixedEnd
 10.69%    1.803      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:473-0!canonical and timestamp 20240715061319 and revision id 6033.
 -->
</div>
</div>
</div>
</div>
</body>
</html>