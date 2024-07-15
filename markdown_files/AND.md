<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>AND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-AND rootpage-AND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">AND</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The logical <a class="mw-selflink selflink">AND</a> numerical operator compares two values in respect of their bits. If both bits at a certain position in both values are set, then that bit position is set in the result.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <i>firstvalue</i> AND <i>secondvalue</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a class="mw-selflink selflink">AND</a> compares the bits of the <i>firstvalue</i> against the bits of the <i>secondvalue</i>, the result is stored in the <i>result</i> variable.</li>
<li>If both bits are on (1) then the result is on (1).</li>
<li>All other conditions return 0 (bit is off).</li>
<li>AND is often used to see if a bit is on by comparing a value to an exponent of 2.</li>
<li>Can turn off a bit by subtracting the bit on value from 255 and using that value to AND a byte value.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">               Table 4: The logical operations and its results.
       In this table, <b>A</b> and <b>B</b> are the <a href="Expression" title="Expression">Expressions</a> to invert or combine.
              Both may be results of former <a href="Boolean" title="Boolean">Boolean</a> evaluations.
  ┌────────────────────────────────────────────────────────────────────────┐
  │                           <b>Logical Operations</b>                           │
  ├───────┬───────┬───────┬─────────┬────────┬─────────┬─────────┬─────────┤
  │   <b>A</b>   │   <b>B</b>   │ <a href="NOT" title="NOT">NOT</a> <b>B</b> │ <b>A</b> <a class="mw-selflink selflink">AND</a> <b>B</b> │ <b>A</b> <a href="OR" title="OR">OR</a> <b>B</b> │ <b>A</b> <a class="mw-redirect" href="XOR" title="XOR">XOR</a> <b>B</b> │ <b>A</b> <a href="EQV" title="EQV">EQV</a> <b>B</b> │ <b>A</b> <a href="IMP" title="IMP">IMP</a> <b>B</b> │
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
<p><i>Example 1:</i>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">         101
         AND
         011
        -----
         001
</pre>
</td></tr></tbody></table>
<dl><dd>The 101 bit pattern equals 5 and the 011 bit pattern equals 3, it returns the bit pattern 001 which equals 1. Only the Least Significant Bits (LSB) match. So decimal values 5 AND 3 = 1.</dd></dl>
<p>
<i>Example 2:</i>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext">      11111011
        AND
      11101111
     ----------
      11101011
</pre>
</td></tr></tbody></table>
<dl><dd>Both bits have to be set for the resulting bit to be set. You can use the <a class="mw-selflink selflink">AND</a> operator to get one byte of a two byte integer this way:</dd></dl>
<dl><dd><dl><dd>firstbyte = twobyteint AND 255</dd></dl></dd></dl>
<dl><dd>Since 255 is 11111111 in binary, it will represent the first byte completely when compared with AND.</dd></dl>
<dl><dd>To find the second (HI) byte's decimal value of two byte <a href="INTEGER" title="INTEGER">INTEGERs</a> use: secondbyte = twobyteint \ 256</dd></dl>
<p>
<i>Example 3:</i> Finding the binary bits on in an <a href="INTEGER" title="INTEGER">INTEGER</a> value.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
 DO
  <a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter Integer value from -32768 to 32767 (Enter quits): ", INTvalue&amp;
  IF INTvalue&amp; &lt; -32768 OR INTvalue&amp; &gt; 32767 OR INTval&amp; = 0 THEN <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> exponent = 15 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -1
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> (INTvalue&amp; <a class="mw-selflink selflink"><span style="color:#4593D8;">AND</span></a> 2 ^ exponent) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "1"; <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "0";
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
  PRINT " "
 LOOP UNTIL INTvalue&amp; = 0 'zero entry quits
</pre>
</td></tr></tbody></table>
<dl><dd>Example output for 6055.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">0001011110100111
</pre>
</td></tr></tbody></table>
<dl><dd><dl><dd><i>Note:</i> The value of 32767 sets 15 bits. -1 sets all 16 bits. Negative values will all have the highest bit set. Use <a href="LONG" title="LONG">LONG</a> variables for input values to prevent overflow errors.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OR" title="OR">OR</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a>, <a href="NOT" title="NOT">NOT</a> <span style="color:#777777;">(logical operators)</span></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061223
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.102 seconds
Preprocessor visited node count: 154/1000000
Post‐expand include size: 5069/2097152 bytes
Template argument size: 183/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   76.327      1 -total
 22.09%   16.864      1 Template:LogicalTruthPlugin
 11.61%    8.858      1 Template:CodeStart
  7.08%    5.407     12 Template:Cl
  6.36%    4.856      2 Template:TextStart
  6.22%    4.745      1 Template:FixedEnd
  6.03%    4.600      2 Template:TextEnd
  5.92%    4.521      6 Template:Parameter
  5.36%    4.094      1 Template:PageDescription
  5.20%    3.969      1 Template:FixedStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:393-0!canonical and timestamp 20240715061223 and revision id 7808.
 -->
</div>
</div>
</div>
</div>
</body>
</html>