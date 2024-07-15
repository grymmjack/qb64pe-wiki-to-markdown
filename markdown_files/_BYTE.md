<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BYTE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BYTE rootpage-BYTE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BYTE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>A <a class="mw-selflink selflink">_BYTE</a> variable can hold signed variable values from -128 to 127 (one byte or 8 <a href="BIT" title="BIT">_BITs</a>). <a href="UNSIGNED" title="UNSIGNED">Unsigned</a> from 0 to 255.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>byte</i> <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <a class="mw-selflink selflink">_BYTE</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Signed _BYTE values can range from -128 to 127.</li>
<li><a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> _BYTEs can hold values from 0 to 255. <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> expands the range of positive values.</li>
<li>Can be defined in a <b>QB64</b> <a href="DEFINE" title="DEFINE">_DEFINE</a> statement using a starting letter range of variable names.</li>
<li>Also can be used in a subroutine parameter <a href="AS" title="AS">AS</a> _BYTE variable definitions.</li>
<li>Define a byte using the suffix %% after the variable name: <i>variable%%</i> = -54</li>
<li>Define an unsigned byte by adding the suffix ~%% after the variable name: variable~%% = 54</li>
<li><b>When a variable has not been assigned or has no type suffix, the value defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li></ul>
<p>
</p>
<ul><li>The <b>MSB</b> is the most significant(largest) bit value and <b>LSB</b> is the least significant bit of a binary or register memory address value. The order in which the bits are read determines the binary or decimal byte value. There are two common ways to read a byte:</li></ul>
<dl><dd><ul><li><b>"Big-endian"</b>: MSB is the first bit encountered, decreasing to the LSB as the last bit by position, memory address or time.</li>
<li><b>"Little-endian"</b>: LSB is the first bit encountered, increasing to the MSB as the last bit by position, memory address or time.</li></ul></dd></dl>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">         <b>Offset or Position:    0    1   2   3   4   5   6   7      Example: 11110000</b>
                              ----------------------------------             --------
    <b>Big-Endian Bit On Value:</b>   128  64  32  16   8   4   2   1                 240
 <b>Little-Endian Bit On Value:</b>    1    2   4   8  16  32  64  128                 15
</pre>
</td></tr></tbody></table>
<dl><dd><dl><dd>The big-endian method compares exponents of 2 ^ 7 down to 2 ^ 0 while the little-endian method does the opposite.</dd></dl></dd></dl>
<p>
</p>
<ul><li><a href="INTEGER" title="INTEGER">INTEGER</a> values consist of 2 bytes called the <b>HI</b> and <b>LO</b> bytes. Anytime that the number of binary digits is a multiple of 16 (2bytes, 4 bytes, etc.) and the HI byte's MSB is on(1), the value returned will be negative. Even with <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> values!</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                                 <b>16 BIT INTEGER OR REGISTER</b>
              <b>AH (High Byte Bits)                         AL (Low Byte Bits)</b>
   BIT:    15    14   13   12   11   10   9   8  |   7   6    5   4    3    2   1    0
          ---------------------------------------|--------------------------------------
   HEX:   8000  4000 2000 1000  800 400  200 100 |  80   40  20   10   8    4   2    1
</pre></td>
<td>
   DEC: -32768 16384 8192 4096 2048 1024 512 256 | 128   64  32   16   8    4   2    1
</td></tr></tbody></table>
<dl><dd><dl><dd>The HI byte's <b>MSB</b> is often called the <b>sign</b> bit! When all 16 of the integer binary bits are on, the decimal return is -1.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dd>How negative assignments affect the _UNSIGNED value returned by a byte (8 bits).</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> unsig <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_BYTE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> sig <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">_BYTE</span></a>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
unsig = <span style="color:#F580B1;">1</span>
sig = <span style="color:#F580B1;">1</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"&amp;B00000001 = unsigned &amp; signed are both"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(unsig <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> sig)
unsig = <span style="color:#F580B1;">127</span>
sig = <span style="color:#F580B1;">127</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"&amp;B01111111 = unsigned &amp; signed are both"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(unsig <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> sig)
unsig = <span style="color:#F580B1;">255</span>
sig = <span style="color:#F580B1;">255</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"&amp;B11111111 = unsigned is"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(unsig) + <span style="color:#FFB100;">" but signed is "</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(sig)
unsig = <span style="color:#F580B1;">254</span>
sig = <span style="color:#F580B1;">254</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"&amp;B11111110 = unsigned is"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(unsig) + <span style="color:#FFB100;">" but signed is "</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(sig)
unsig = <span style="color:#F580B1;">253</span>
sig = <span style="color:#F580B1;">253</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"&amp;B11111101 = unsigned is"</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(unsig) + <span style="color:#FFB100;">" but signed is "</span> + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(sig)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The signed value needs the MSB bit for the sign."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The most significant bit is furthest to the left."</span>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">&amp;B00000001 = unsigned &amp; signed are both 1
&amp;B01111111 = unsigned &amp; signed are both 127
&amp;B11111111 = unsigned is 255 but signed is -1
&amp;B11111110 = unsigned is 254 but signed is -2
&amp;B11111101 = unsigned is 253 but signed is -3
The signed value needs the MSB bit for the sign.
The most significant bit is furthest to the left.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="BIT" title="BIT">_BIT</a>, <a href="%26B" title="&amp;B">&amp;B</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="DIM" title="DIM">DIM</a></li>
<li><a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li>
<li><a href="Screen_Memory" title="Screen Memory">Screen Memory</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li>
<li><a href="Converting_Bytes_to_Bits" title="Converting Bytes to Bits">Converting Bytes to Bits</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715034303
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.046 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 394/1000000
Post‐expand include size: 3257/2097152 bytes
Template argument size: 740/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 312/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   35.478      1 -total
 10.69%    3.793     26 Template:Cl
  9.99%    3.546     20 Template:Text
  6.78%    2.407      1 Template:PageSyntax
  6.38%    2.265      1 Template:CodeStart
  6.34%    2.249      1 Template:PageExamples
  5.98%    2.122      1 Template:CodeEnd
  5.92%    2.099      1 Template:PageNavigation
  5.61%    1.990      2 Template:FixedEnd
  5.43%    1.927      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:62-0!canonical and timestamp 20240715034303 and revision id 8275.
 -->
</div>
</div>
</div>
</div>
</body>
</html>