<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>RND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RND rootpage-RND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">RND</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>RND</b> function returns a random number with a value between 0 (inclusive) and 1 (exclusive).
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>result! = <a class="mw-selflink selflink">RND</a> [(<i>n</i>)]</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>n</i> is a <a href="SINGLE" title="SINGLE">SINGLE</a> numeric value that defines the behavior of the RND function but is <b>NOT normally required</b>:</li></ul>
<dl><dd><dl><dd>n parameter omitted: Returns next random number in the sequence.</dd>
<dd>n = 0: Return the last value returned.</dd>
<dd>n &lt; 0: Always returns the same value for any given n</dd>
<dd>n &gt; 0: the sequence of numbers generated will not change unless <a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a> is initiated.</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The random numbers generated range from 0 minimum to .9999999 maximum  <a href="SINGLE" title="SINGLE">SINGLE</a> values that never equal 1.</li>
<li>To get values in a range larger than 1, multiply RND with a number to get returns up to but not including that numerical value.</li>
<li>To get values starting at a certain number, add that number to the RND result as RND minimums can be 0.</li>
<li>If you need an integer range of numbers, like a dice roll, round it down to an <a href="INT" title="INT">INT</a>. Add 1 to the maximum number with <a href="INT" title="INT">INT</a>.</li>
<li>The random sequence is 2 ^ 24 or 16,777,216 entries long, which can allow repeated patterns in some procedures.</li>
<li>Formulas for the <a href="INT" title="INT">Integer</a> or <a href="CINT" title="CINT">Closest Integer</a> of ANY number range from <i>min%</i>(lowest value) to <i>max%</i>(greatest value):</li></ul>
<dl><dd><dl><dd><ul><li>Using <a href="INT" title="INT">INT</a>: randNum% = INT(RND * (max% - min% + 1)) + min%</li>
<li>Using <a href="CINT" title="CINT">CINT</a>: randNum% = CINT(RND * (max% - min%)) + min%</li></ul></dd></dl></dd></dl>
<ul><li>Use <a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a> <a href="TIMER_(function)" title="TIMER (function)">TIMER</a> for different random number results each time a program is run.</li>
<li><a href="RUN" title="RUN">RUN</a> should reset the <a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a> sequence to the starting <a class="mw-selflink selflink">RND</a> function value.(Not yet in QB64)</li></ul>
<p>
<i>Example 1:</i> Generating a random integer value between 1 and 6 (inclusive) using INT.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">dice% = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * 6) + 1 'add one as INT value never reaches 6
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Using uniform random numbers to create random numbers with a gaussian distribution (<a class="extiw" href="https://en.wikipedia.org/wiki/Marsaglia_polar_method" title="wikipedia:Marsaglia polar method">Marsaglia's polar method</a>).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
  u! = <a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * 2 - 1
  v! = <a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * 2 - 1
  s! = u! * u! + v! * v!
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> s! &gt;= 1 <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> s! = 0
s! = SQR(-2 * <a href="LOG" title="LOG"><span style="color:#4593D8;">LOG</span></a>(s!) / s!) * 0.5
u! = u! * s!
v! = v! * s!
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Values <i>u!</i> and <i>v!</i> are now two independent random numbers with gaussian distribution, centered at 0.</dd></dl>
<p>
<i>Example 3:</i> Random flashes from an explosion
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(640, 480, 32)
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
BC = 120 ' BALL COUNT
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> ballx(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> bally(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> velx(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> vely(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> bsize(1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC)
Y = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (400 - 100 + 1)) + 100
X0 = 325
Y0 = 300
Tmax = 150
DO
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> p = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC
        T = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (Tmax - 50 + 1)) + 50
        X = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (1000 + 500 + 1)) - 500
        velx(p) = (X - X0) / T '                       calculate velocity based on flight time
        vely(p) = -1 * (Y - .05 * (T ^ 2 + 20 * Y0)) / (T) ' verticle velocity
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> p
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> w = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC
        bsize(w) = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (10 - 0 + 1)) + 0 'size
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> w
    <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> J = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> Tmax
        <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
        '<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 255 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .5
        '<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (X0, Y0), i, <a href="RGB" title="RGB"><span style="color:#4593D8;">_RGB</span></a>(255 - i, 0, 0), 0, 3.147
        ' <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i
        R = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (25 - 20 + 1)) + 20 'random glimmer
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> z = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC
            ballx(z) = X0 + velx(z) * J
            bally(z) = Y0 - vely(z) * J + .5 * .1 * J ^ 2
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> z
        <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> d = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> BC
            RCOL = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">RND</span></a> * (255 - 0 + 1)) 'color
            <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> i = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> bsize(d) + 1 <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> .4 'draw balls
                <a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (ballx(d), bally(d)), i, <a href="RGBA" title="RGBA"><span style="color:#4593D8;">_RGBA</span></a>(255, RCOL - (R * i), RCOL - R * i, 255)
            <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> d
        <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> J
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="UNTIL" title="UNTIL"><span style="color:#4593D8;">UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; ""
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RANDOMIZE" title="RANDOMIZE">RANDOMIZE</a>, <a href="TIMER_(function)" title="TIMER (function)">TIMER (function)</a></li>
<li><a href="INT" title="INT">INT</a>, <a href="CINT" title="CINT">CINT</a>, <a href="FIX" title="FIX">FIX</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061410
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.043 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 507/1000000
Post‐expand include size: 4255/2097152 bytes
Template argument size: 558/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.702      1 -total
 16.80%    4.149     68 Template:Cl
 11.26%    2.782      1 Template:PageSyntax
  9.59%    2.369      1 Template:Small
  8.92%    2.204      1 Template:PageDescription
  8.51%    2.102      3 Template:CodeEnd
  7.59%    1.874      3 Template:CodeStart
  7.57%    1.871      1 Template:PageParameters
  7.51%    1.854      1 Template:PageSeeAlso
  7.16%    1.768      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:261-0!canonical and timestamp 20240715061410 and revision id 8993.
 -->
</div>
</div>
</div>
</div>
</body>
</html>