<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$IF - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_IF rootpage-_IF skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$IF</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>$IF</b> is precompiler <a href="Metacommand" title="Metacommand">metacommand</a>, which determines which sections of code inside its blocks are included into the final code for compliing.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$IF</a> variable = expression THEN</dd>
<dd>.</dd>
<dd><a class="mw-redirect" href="$ELSEIF" title="$ELSEIF">$ELSEIF</a> variable = expression THEN</dd>
<dd>.</dd>
<dd><a class="mw-redirect" href="$ELSE" title="$ELSE">$ELSE</a></dd>
<dd>.</dd>
<dd><a class="mw-redirect" href="$END_IF" title="$END IF">$END IF</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>$IF is the start of a precompiler code block which includes or excludes sections of code from being compiled.</li>
<li>There is no single line $IF statement.  $IF must be in a valid $IF THEN...$END IF block to work properly.</li>
<li>Like all other metacommands, you can not use more than one metacommand per line. <b>Use of : to separate statements in a single line is not allowed.</b></li>
<li>Variable names can contain numbers, letters and periods, in any order.</li>
<li>Expressions can contain one set of leading and/or trailing quotes; and any number of numbers, letters and periods, in any order.</li>
<li>The precompiler comes with some preset values which can be used to help determine which code blocks to include/exclude.  These are:
<ul><li><b>WIN</b> or <b>WINDOWS</b> if the user is running QB64 in a Windows environment.</li>
<li><b>LINUX</b> if the user is running QB64 in a Linux environment.</li>
<li><b>MAC</b> or <b>MACOSX</b> if the user is running QB64 in a macOS environment.</li>
<li><b>32BIT</b> if the user is running a 32-bit version of QB64.</li>
<li><b>64BIT</b> if the user is running a 64-bit version of QB64.</li>
<li><b>VERSION</b>, which is set to the version of the QB64 compiler. This is a number and can be ordered, see example below.</li></ul></li>
<li>Special values <b>DEFINED</b> and <b>UNDEFINED</b> can be used to check whether a precompiler variable has already been assigned a value. Useful for code in libraries which may be repeated.</li>
<li><a class="mw-redirect" href="$END_IF" title="$END IF">$END IF</a> denotes the end of a valid precompiler $IF block.</li>
<li><a class="mw-redirect" href="$ELSEIF" title="$ELSEIF">$ELSEIF</a> must follow a valid $IF or $ELSEIF statement.</li>
<li>If <a class="mw-redirect" href="$ELSE" title="$ELSE">$ELSE</a> is used, it must be used as the last conditional check before $END IF.  $ELSEIF cannot come after $ELSE.
<ul><li>There can only be one $ELSE in an <b>$IF-$ELSEIF-$ELSE-$END IF</b> block, and it must be the last block selection before the $END IF.  $ELSEIF cannot follow $ELSE.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$LET" title="$LET"><span style="color:#55FF55;">$LET</span></a> SCREENMODE = <span style="color:#F580B1;">32</span>
<a class="mw-selflink selflink"><span style="color:#55FF55;">$IF</span></a> SCREENMODE = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Red = <span style="color:#F580B1;">4</span>
<a class="mw-redirect" href="$ELSEIF" title="$ELSEIF"><span style="color:#55FF55;">$ELSEIF</span></a> SCREENMODE = <span style="color:#F580B1;">32</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Red = <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">255</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)
<a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> Red
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Hello World"</span>
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The same CONST is defined twice inside the program.  Normally, defining a CONST more than once generates an error, but the $IF condition here is choosing which CONST will be inside the final program.
As long as Screenmode is 0, the program will exclude the code where CONST Red is defined as color 4.  If Screenmode is 32, CONST Red will be defined as _RGB32(255, 0, 0).
The <a href="$LET" title="$LET">$LET</a> and $IF statements let the programmer control the code that actually gets compiled, while excluding the other blocks completely.
</p>
<p><i>Example 2:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$IF</span></a> <span style="color:#55FF55;">WIN</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Slash = <span style="color:#FFB100;">"\"</span>
<a class="mw-redirect" href="$ELSE" title="$ELSE"><span style="color:#55FF55;">$ELSE</span></a>
    <a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> Slash = <span style="color:#FFB100;">"/"</span>
<a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"The proper slash for your operating system is "</span>; Slash
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> For the above, the CONST slash is defined by the automatic internal flags which returns what operating system is being used at compile time. On a Windows PC, the Slash will be the backslash; for any other OS it will be the forward slash.
</p>
<p><i>Example 3:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$IF</span></a> <span style="color:#55FF55;">VERSION</span> &lt; <span style="color:#F580B1;">1.5</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a href="$ERROR" title="$ERROR"><span style="color:#55FF55;">$ERROR</span></a> Requires QB64 version 1.5 or greater
<a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> VERSION is a predefined variable that holds the QB64 compiler version. If we know our program needs features only available above a certain version, we can check for that and give the user a helpful error message instead of a confusing error elsewhere in the program.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$LET" title="$LET">$LET</a></li>
<li><a href="$ERROR" title="$ERROR">$ERROR</a></li>
<li><a href="Metacommand" title="Metacommand">Metacommands</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714143711
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.044 seconds
Real time usage: 0.057 seconds
Preprocessor visited node count: 290/1000000
Post‐expand include size: 2570/2097152 bytes
Template argument size: 476/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 67/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.646      1 -total
 13.01%    4.379     14 Template:Cm
 11.52%    3.878     14 Template:Text
  9.43%    3.172      1 Template:PageSyntax
  8.68%    2.920      8 Template:Cl
  8.35%    2.810      1 Template:PageDescription
  7.85%    2.642      1 Template:PageSeeAlso
  7.62%    2.563      3 Template:CodeEnd
  7.44%    2.504      1 Template:PageExamples
  7.30%    2.458      3 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:154-0!canonical and timestamp 20240714143711 and revision id 8323.
 -->
</div>
</div>
</div>
</div>
</body>
</html>