<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_BIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-BIT rootpage-BIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_BIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_BIT</a> datatype can return only values of 0 (bit off) and -1 (bit on).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="DIM" title="DIM">DIM</a> <i>variable</i> <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <a class="mw-selflink selflink">_BIT</a> [* <i>numberofbits</i>]</dd></dl>
<dl><dd><a href="DEFINE" title="DEFINE">_DEFINE</a> <i>Letter</i>[<i>-Range</i>|,...] <a href="AS" title="AS">AS</a> [[[_UNSIGNED] <a class="mw-selflink selflink">_BIT</a> [* <i>numberofbits</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>An <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> _BIT can hold 0 or 1 instead of 0 and -1, if you set the numberofbits you can hold larger values depending on the number of bits you have set (_BIT * 8 can hold the same values as <a href="BYTE" title="BYTE">_BYTE</a> for example) and the information below is compromised if setting any number of bits other than 1.</li>
<li>If you set the variable to any other number then the least significant bit of that number will be set as the variables number, if the bit is 1 (on) then the variable will be -1 and if the bit is 0 (off) then the variable will be 0.</li>
<li>The least significant bit is the last bit on a string of bits (11111) since that bit will only add 1 to the value if set. The most significant bit is the first bit on a string of bits and changes the value more dramatically (significantly) if set on or off.</li>
<li>The _BIT datatype can be succesfully used as a <a href="Boolean" title="Boolean">Boolean</a> (TRUE or FALSE) and it requires minimal amount of memory (the lowest amount possible actually, one byte can hold 8 bits, if you want to use bits in order to decrease memory usage, use them as arrays as a _BIT variable by itself allocates 4 bytes - DIM bitarray(800) AS _BIT uses 100 bytes).</li>
<li><b>When a variable has not been assigned or has no type suffix, the value defaults to <a href="SINGLE" title="SINGLE">SINGLE</a>.</b></li>
<li><b><a href="Keywords_currently_not_supported_by_QB64" title="Keywords currently not supported by QB64">_BIT is not supported in User Defined TYPES.</a></b> Use a <a href="BYTE" title="BYTE">_BYTE</a> and assign up to 8 bit values as shown below.</li></ul>
<p>
</p>
<ul><li><b>Suffix Symbols</b> The <a class="mw-selflink selflink">_BIT</a> type suffix used is below the grave accent (`), usually located under the tilde (~) key (not an apostrophe). Foreign keyboards may not have the ` key. Try Alt+96 in the IDE.</li></ul>
<dl><dd>You can define a bit on-the-fly by adding a ` after the variable, like this: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">variable` = <span style="color:#F580B1;">-1</span></span></dd></dl>
<dl><dd>If you want an unsigned bit you can define it on-the-fly by adding ~` instead, like this: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">variable~` = <span style="color:#F580B1;">1</span></span></dd></dl>
<dl><dd>You can set the number of bits on the fly by just adding that number - this defines it as being two bits: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">variable`2 = <span style="color:#F580B1;">-1</span></span></dd></dl>
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
<ul><li><a href="INTEGER" title="INTEGER">INTEGER</a> values consist of 2 bytes called the <b>HI</b> and <b>LO</b> bytes. Anytime that the number of binary digits is a multiple of 16 (2bytes, 4 bytes, etc.) and the HI byte's MSB is on(1), the value returned will be negative. Even with <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> values!</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">                                 <b>16 BIT INTEGER OR REGISTER</b>
              <b>AH (High Byte Bits)                         AL (Low Byte Bits)</b>
   BIT:    15    14   13   12   11   10   9   8  |   7   6    5   4    3    2   1    0
          ---------------------------------------|--------------------------------------
   HEX:   8000  4000 2000 1000  800 400  200 100 |  80   40  20   10   8    4   2    1
                                                 |
   DEC: -32768 16384 8192 4096 2048 1024 512 256 | 128   64  32   16   8    4   2    1
</pre>
</td></tr></tbody></table>
<dl><dd><dl><dd>The HI byte's <b>MSB</b> is often called the <b>sign</b> bit! When all 16 of the integer binary bits are on, the decimal return is -1.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Shifting bits in a value in QB64 versions prior to 1.3 (you can use <a href="SHL" title="SHL">_SHL</a> and <a href="SHR" title="SHR">_SHR</a> starting with version 1.3).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">n = <span style="color:#F580B1;">24</span>
Shift = <span style="color:#F580B1;">3</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#55FF55;">LShift</span>(n, Shift)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#55FF55;">RShift</span>(n, Shift)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">LShift&amp;</span> (n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, LS <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> LS &lt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
    <span style="color:#55FF55;">LShift</span> = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(n * (<span style="color:#F580B1;">2</span> ^ LS))
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">RShift&amp;</span> (n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, RS <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> RS &lt; <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
    <span style="color:#55FF55;">RShift</span> = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(n / (<span style="color:#F580B1;">2</span> ^ RS))
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 192
 3
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="%26B" title="&amp;B">&amp;B</a> (binary), <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><a href="SHL" title="SHL">_SHL</a>, <a href="SHR" title="SHR">_SHR</a></li>
<li><a href="DEFINE" title="DEFINE">_DEFINE</a>, <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a></li>
<li><a href="DIM" title="DIM">DIM</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li>
<li><a href="Variable_Types" title="Variable Types">Variable Types</a></li>
<li><a href="Converting_Bytes_to_Bits" title="Converting Bytes to Bits">Converting Bytes to Bits</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714211302
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.065 seconds
Real time usage: 0.138 seconds
Preprocessor visited node count: 339/1000000
Post‐expand include size: 3460/2097152 bytes
Template argument size: 469/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 1/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   81.988      1 -total
 18.40%   15.084     15 Template:Text
  8.21%    6.728      1 Template:CodeEnd
  7.18%    5.889      1 Template:PageSyntax
  7.04%    5.769      5 Template:Parameter
  5.92%    4.856      3 Template:InlineCode
  5.75%    4.715      2 Template:FixedEnd
  5.55%    4.550      3 Template:InlineCodeEnd
  4.53%    3.711     23 Template:Cl
  4.36%    3.573      2 Template:FixedStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:53-0!canonical and timestamp 20240714211302 and revision id 8266.
 -->
</div>
</div>
</div>
</div>
</body>
</html>