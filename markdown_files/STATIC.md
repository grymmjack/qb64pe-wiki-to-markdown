<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>STATIC - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-STATIC rootpage-STATIC skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">STATIC</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">STATIC</a> keyword is used in declaration statements to control where variables are stored.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dt>Variables</dt>
<dd><a class="mw-selflink selflink">STATIC</a> <i>variableName</i>[()] [[[AS <i>dataType</i>][, ...]</dd>
<dt>Subs &amp; Functions</dt>
<dd>{<a href="SUB" title="SUB">SUB</a>|<a href="FUNCTION" title="FUNCTION">FUNCTION</a>} <i>procedureName</i> [(<i>parameterList</i>)] <b>STATIC</b></dd>
<dt>Library function block</dt>
<dd><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE STATIC LIBRARY</a></dd></dl>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>A STATIC list can be used in <a href="SUB" title="SUB">SUB</a> and <a href="FUNCTION" title="FUNCTION">FUNCTION</a> procedures to designate one or more variables to retain their values.</li>
<li>Variables and arrays with static storage will retain their values in between procedure calls. The values may also be used recursively.</li></ul>
<dl><dd><ul><li><i>variableName</i> may include a type suffix or use <a href="AS" title="AS">AS</a> to specify a type other than the default <a href="SINGLE" title="SINGLE">SINGLE</a> type.</li>
<li>Arrays with static storage are declared by specifying empty parenthesis following the array name. See <a href="Arrays" title="Arrays">Arrays</a></li></ul></dd></dl>
<ul><li>STATIC can be used after the name of a <a href="SUB" title="SUB">SUB</a> or <a href="FUNCTION" title="FUNCTION">FUNCTION</a> in the procedure to force all variables to retain their values.</li>
<li><b>Recursive procedures may be required to be STATIC to avoid a Stack Overflow! QB64 programs may just close!</b></li>
<li><a href="$STATIC" title="$STATIC">$STATIC</a> defined program <a href="Arrays" title="Arrays">arrays</a> cannot be <a href="REDIM" title="REDIM">re-sized</a> or use <a href="PRESERVE" title="PRESERVE">_PRESERVE</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1: Finding the binary bit settings from a 32 bit <a href="LONG" title="LONG">LONG</a> register return using recursion.</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> "Enter a numerical value to see binary value: ", num&amp;
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> BinStr$(num&amp;)
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> BinStr$ (n&amp;) <a class="mw-selflink selflink"><span style="color:#4593D8;">STATIC</span></a> 'comment out STATIC to see what happens!
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> p%, s$
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> 2 ^ p% &gt; n&amp; <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
  p% = 0
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n&amp; <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> 2 ^ p% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> s$ = "1" + s$ <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> s$ = "0" + s$
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n&amp; &gt; 2 ^ p% <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    p% = p% + 1
    s$ = BinStr$(n&amp;) 'recursive call to itself
  <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>: p% = 0
  <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> s$ = "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> BinStr$ = "0" <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a> BinStr$ = s$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The <a href="FUNCTION" title="FUNCTION">FUNCTION</a> above returns a <a href="STRING" title="STRING">STRING</a> value representing the bits ON in an <a href="INTEGER" title="INTEGER">INTEGER</a> value. The string can be printed to the screen to see what is happening in a port register. <b>STATIC</b> keeps the function from overloading the memory "Stack" and is normally REQUIRED when recursive calls are used in QBasic! <b>QB64 procedures will close without warning or error!</b></dd></dl>
<p>
<i>Example 2:</i> Using a static array to cache factorials, speeding up repeated calculations:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Factorial(0)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Factorial(5)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> Factorial(50
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> Factorial# ( n <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a> )
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> maxNToCache = 50
    <a class="mw-selflink selflink"><span style="color:#4593D8;">STATIC</span></a> resultCache() <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">STATIC</span></a> firstCall <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
    ' The lookup table is initially empty, so re-size it..
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> firstCall = 0 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">THEN</span></a>
        firstCall = -1
        <a href="REDIM" title="REDIM"><span style="color:#4593D8;">REDIM</span></a> resultCache(maxNToCache) <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="DOUBLE" title="DOUBLE"><span style="color:#4593D8;">DOUBLE</span></a>
        ' ..and pre-calculate some factorials.
        resultCache(0) = 1
        resultCache(1) = 1
        resultCache(2) = 2
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">END IF</span></a>
    ' See if we have the result cached. If so, we're done.
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> n &lt;= maxNToCache <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> resultCache(n) &lt;&gt; 0 <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">THEN</span></a>
            Factorial = resultCache(n)
            <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
        <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">END IF</span></a>
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">END IF</span></a>
    ' If not, we use recursion to calculate the result, then cache it for later use:
    resultCache(n) = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(n) * Factorial(<a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(n) - 1)
    Factorial = resultCache(n)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0"> 1
 120
 3.041409320171338D+64
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a>, <a href="COMMON" title="COMMON">COMMON</a></li>
<li><a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li>
<li><a href="DECLARE_LIBRARY" title="DECLARE LIBRARY">DECLARE LIBRARY</a></li>
<li><a href="TYPE" title="TYPE">TYPE</a>, <a href="Arrays" title="Arrays">Arrays</a></li>
<li><a href="$STATIC" title="$STATIC">$STATIC</a>, <a href="$DYNAMIC" title="$DYNAMIC">$DYNAMIC</a></li>
<li><a href="Data_types" title="Data types">Data types</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192551
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.045 seconds
Real time usage: 0.075 seconds
Preprocessor visited node count: 405/1000000
Post‐expand include size: 3525/2097152 bytes
Template argument size: 625/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.009      1 -total
 24.92%   12.963      2 Template:CodeStart
 12.97%    6.746     51 Template:Cl
  7.68%    3.993      1 Template:OutputStart
  6.46%    3.360      2 Template:CodeEnd
  6.15%    3.198      1 Template:PageNavigation
  5.84%    3.038      1 Template:PageSeeAlso
  5.30%    2.756      1 Template:PageSyntax
  5.23%    2.719      1 Template:OutputEnd
  4.65%    2.417      5 Template:Parameter
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:299-0!canonical and timestamp 20240714192551 and revision id 8367.
 -->
</div>
</div>
</div>
</div>
</body>
</html>