<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RANDOMIZE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RANDOMIZE rootpage-RANDOMIZE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RANDOMIZE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>RANDOMIZE</b> is used with a seed value to generate different random number sequences using the <a href="RND" title="RND">RND</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd><b>RANDOMIZE</b> [USING] <b>{<i>seednumber</i>|TIMER}</b></dd></dl></dd></dl>
<p>
</p>
<ul><li>The <i>seed number</i> can be ANY positive or negative numerical type value. The <a href="TIMER_(function)" title="TIMER (function)">TIMER</a> value is often used to change <a href="RND" title="RND">RND</a> output each run.</li>
<li>If the <i>seed number</i> is omitted, the program will display: <b>Random-number seed (-32768 to 32767)?</b> request on screen.</li>
<li><b>USING</b> resets a <i>seed number</i> sequence to the start of the sequence as if the program just started using that seed in <b>QB64 only</b>.</li>
<li><b>Note:</b> The RANDOMIZE USING <i>seed number</i> MUST be designated or a <span style="color:blue;">Name already in use</span> status error will occur!</li>
<li>If the same initial seed number is used, the sequence of random numbers returned will be identical every program run.</li>
<li>The fact that random numbers would always be the same has been used for simple data encryption and decryption.</li>
<li>Using a <a href="TIMER_(function)" title="TIMER (function)">TIMER</a> starting value ensures that the initial return sequence values are different almost every time the program is run!</li>
<li><a href="RUN" title="RUN">RUN</a> should reset the <a class="mw-selflink selflink">RANDOMIZE</a> sequence to the starting <a href="RND" title="RND">RND</a> function value.(Not yet in QB64)</li></ul>
<p>
<i>Example 1:</i> Using RANDOMIZE <b>TIMER</b> to set a different starting sequence of <a href="RND" title="RND">random</a> numbers every run.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
randnum% = INT(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 11) + 2  'add one to multiplier as INT rounds down and never equals 10
PRINT randnum%
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(K$) = "Q"  'q = quit
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Procedure generates random integer values from 2 to 12 like a pair of dice.</dd></dl>
<p>
<i>Example 2:</i> Repeating a random number sequence with RANDOMIZE <b>USING</b> and a specific seed value in <b>QB64</b> only.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">seed = 10
<a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOMIZE</span></a> seed
Print7
<a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOMIZE</span></a> seed
Print7
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press a key to start sequence over!"
K$ = <a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)
<a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOMIZE</span></a> <b>USING</b> seed
Print7
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> Print7
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> r = 1 TO 7
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The second RANDOMIZE statement just continues the sequence where USING in the third restarts the sequence.</dd></dl>
<p>
<i>Example 3:</i> Random fireworks explosions:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a> ftype
    vx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
    vy <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a href="TYPE" title="TYPE"><span style="color:#4593D8;">TYPE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> frag(500) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> ftype 'fragments
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> pi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
pi = 3.141593
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, y <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> t <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, g <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>, p <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
t = 0
g = 0.4 'gravity
p = 15 'explosion power
sw = 800
sh = 600
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(sw, sh, 32)
DO
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(frag)
        frag(i).vx = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="COS" title="COS"><span style="color:#4593D8;">COS</span></a>(2 * pi * <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>)
        frag(i).vy = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(2 * pi * <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>)
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    x = sw * <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>
    y = sh * <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a>
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> t = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 25 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> 0.1
        <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (0, 0)-(sw, sh), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(0, 0, 0), BF
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="UBOUND" title="UBOUND"><span style="color:#4593D8;">UBOUND</span></a>(frag)
            <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (x + t * p * frag(i).vx, y + t * p * frag(i).vy + g * t * t), <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255, 255, 0)
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
        <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 150
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> = -27 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RND" title="RND">RND</a>, <a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a></li>
<li><a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031658
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.052 seconds
Preprocessor visited node count: 613/1000000
Post‐expand include size: 5094/2097152 bytes
Template argument size: 832/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   20.448      1 -total
 20.64%    4.221     83 Template:Cl
 10.30%    2.106      1 Template:PageSyntax
 10.11%    2.068      1 Template:Text
  9.02%    1.845      3 Template:CodeStart
  9.01%    1.843      1 Template:Small
  7.69%    1.573      1 Template:PageSeeAlso
  7.53%    1.540      1 Template:PageNavigation
  6.61%    1.352      3 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:239-0!canonical and timestamp 20240715031658 and revision id 8060.
 -->
</div>
</div>
</div>
</div>
</body>
</html>