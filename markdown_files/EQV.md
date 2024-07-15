<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>EQV - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-EQV rootpage-EQV skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">EQV</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">EQV</a> operator returns a value based on the <i>equivalence</i> of two conditions or values.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <i>firstValue</i> <a class="mw-selflink selflink">EQV</a> <i>secondValue</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns true (-1) when both values are the same (<i>equivalent</i>).</li>
<li>Turns a bit on if both bits are the same, turns a bit off if both bits are different.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a href="NOT" title="NOT">NOT</a> <b>B</b> │ <b>A</b> <a href="AND" title="AND">AND</a> <b>B</b> │ <b>A</b> <a href="OR" title="OR">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a class="mw-selflink selflink">EQV</a> <b>B</b> │ <b>A</b> <a href="IMP" title="IMP">IMP</a> <b>B</b> │
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
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1187" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="Binary" title="Binary">Binary</a></li>
<li><a href="Boolean" title="Boolean">Boolean</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061304
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 31/1000000
Post‐expand include size: 4057/2097152 bytes
Template argument size: 27/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   25.163      1 -total
 30.75%    7.737      1 Template:LogicalTruthPlugin
 19.78%    4.978      1 Template:PageDescription
 12.96%    3.262      3 Template:Parameter
 12.76%    3.212      1 Template:PageSeeAlso
 11.22%    2.823      1 Template:PageSyntax
  9.88%    2.485      1 Template:FixedStart
  9.15%    2.303      1 Template:PageNavigation
  8.66%    2.179      1 Template:FixedEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:465-0!canonical and timestamp 20240715061303 and revision id 8919.
 -->
</div>
</div>
</div>
</div>
</body>
</html>