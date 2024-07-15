<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMIMAGE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMIMAGE rootpage-MEMIMAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMIMAGE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_MEMIMAGE</a> function returns a <a href="MEM" title="MEM">_MEM</a> value referring to an image's memory using a designated image handle.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>imageBlock</i> = <a class="mw-selflink selflink">_MEMIMAGE</a>[(<i>imageHandle&amp;</i>)]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>imageBlock</i> <a href="MEM" title="MEM">_MEM</a> type variable holds the read-only elements .OFFSET, .SIZE, .TYPE and .ELEMENTSIZE.</li>
<li>If the optional <i>imageHandle&amp;</i> isn't passed, it is assumed to be the current <a href="DEST" title="DEST">_DESTination</a> program screen image.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use the function to place images into memory access blocks for faster data access.</li>
<li>All values created by this function must be freed using <a href="MEMFREE" title="MEMFREE">_MEMFREE</a> with a valid <a href="MEM" title="MEM">_MEM</a> variable.</li>
<li>Image handle values and the memory used must still be freed using <a href="FREEIMAGE" title="FREEIMAGE">_FREEIMAGE</a> when no longer required.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Darkening an image using memory with <a href="$CHECKING" title="$CHECKING">$CHECKING</a>:OFF for greater speed. Use any 24 bit image file name on the second code line.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(1024, 768, 32)
i&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("turtle.jpg") '&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt; use any 24 bit image file
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> n! = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 0.01 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> -0.01
    i2&amp; = <a href="COPYIMAGE" title="COPYIMAGE"><span style="color:#4593D8;">_COPYIMAGE</span></a>(i&amp;)
    DarkenImage i2&amp;, n!
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (0, 0), i2&amp;
    <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> i2&amp;
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> DarkenImage (Image <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Value_From_0_To_1 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>)
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> Value_From_0_To_1 &lt;= 0 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> Value_From_0_To_1 &gt;= 1 <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <a href="PIXELSIZE" title="PIXELSIZE"><span style="color:#4593D8;">_PIXELSIZE</span></a>(Image) &lt;&gt; 4 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_SUB" title="EXIT SUB"><span style="color:#4593D8;">EXIT SUB</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Buffer <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>: Buffer = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMIMAGE</span></a>(Image) 'Get a memory reference to our image
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Frac_Value <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: Frac_Value = Value_From_0_To_1 * 65536 'Used to avoid slow floating point calculations
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> O <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="OFFSET" title="OFFSET"><span style="color:#4593D8;">_OFFSET</span></a>, O_Last <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="OFFSET" title="OFFSET"><span style="color:#4593D8;">_OFFSET</span></a>
O = Buffer.OFFSET 'We start at this offset
O_Last = Buffer.OFFSET + <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a>(Image) * <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a>(Image) * 4 'We stop when we get to this offset
'use on error free code ONLY!
<a href="$CHECKING" title="$CHECKING"><span style="color:#4593D8;">$CHECKING</span></a>:OFF
DO
    <a href="MEMPUT" title="MEMPUT"><span style="color:#4593D8;">_MEMPUT</span></a> Buffer, O, <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(Buffer, O, <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>) * Frac_Value \ 65536 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
    <a href="MEMPUT" title="MEMPUT"><span style="color:#4593D8;">_MEMPUT</span></a> Buffer, O + 1, <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(Buffer, O + 1, <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>) * Frac_Value \ 65536 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
    <a href="MEMPUT" title="MEMPUT"><span style="color:#4593D8;">_MEMPUT</span></a> Buffer, O + 2, <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(Buffer, O + 2, <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>) * Frac_Value \ 65536 <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
    O = O + 4
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> O = O_Last
'turn checking back on when done!
<a href="$CHECKING" title="$CHECKING"><span style="color:#4593D8;">$CHECKING</span></a>:ON
<a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> Buffer
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The second value passed to DarkenImage is a value from 0.0 to 1.0 where 0.0 is full darkness and 1 is none.</dd></dl>
<p>
<i>Example 2:</i> Reading information stored in an image with <a class="mw-selflink selflink">_MEMIMAGE</a> to print <a href="ASC_(function)" title="ASC (function)">ASC</a> text characters to the screen.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> 13
<a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a>
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (0, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("H")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (1, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("E")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (2, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("L")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (3, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("L")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (4, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("O")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (5, 0), 32
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (6, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("W")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (7, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("O")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (8, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("R")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (9, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("L")
<a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (10, 0), <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>("D")
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> m <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
m = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMIMAGE</span></a>
x1$ = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(m, m.OFFSET, <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a> * 11) 'convert numbers to ASCII text characters
<a href="MEMFREE" title="MEMFREE"><span style="color:#4593D8;">_MEMFREE</span></a> m 'free memory when done
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> 10, 1: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(x1$) 'prints 11 as byte length
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x1$ 'prints HELLO WORLD
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Notes:</i> The colors in the upper left corner are the text data used. An image could hold a hidden text message this way.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a></li>
<li><a href="MEMNEW" title="MEMNEW">_MEMNEW</a></li>
<li><a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMPUT" title="MEMPUT">_MEMPUT</a></li>
<li><a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li>
<li><a href="$CHECKING" title="$CHECKING">$CHECKING</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062403
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.072 seconds
Real time usage: 0.154 seconds
Preprocessor visited node count: 734/1000000
Post‐expand include size: 6184/2097152 bytes
Template argument size: 1272/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  101.959      1 -total
 12.52%   12.762      4 Template:Parameter
 10.16%   10.358      1 Template:PageExamples
 10.10%   10.298      1 Template:Small
  9.76%    9.954      1 Template:PageParameters
  8.94%    9.118     98 Template:Cl
  8.52%    8.687      1 Template:PageSyntax
  8.08%    8.237      2 Template:CodeEnd
  7.99%    8.144      1 Template:PageDescription
  5.80%    5.910      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:183-0!canonical and timestamp 20240715062403 and revision id 8714.
 -->
</div>
</div>
</div>
</div>
</body>
</html>