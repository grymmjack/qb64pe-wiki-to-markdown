<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ASSERT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ASSERT rootpage-ASSERT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ASSERT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ASSERT</a> statement can be used to perform tests in code that's in development, for debugging purposes.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_ASSERT</a> <i>condition</i>[,  <i>errorMessage$</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>condition</i> is the condition that must be met in order to consider the _ASSERT valid.</li>
<li>Optional <i>errorMessage$</i> is the message to be displayed in the console window if <a href="$ASSERTS" title="$ASSERTS">$ASSERTS:CONSOLE</a> is used.</li>
<li>If the condition is not met (that is, if it evaluates to 0), an error occurs ("_ASSERT failed on line #") and program execution stops.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.4 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Adding test checks for parameter inputs in a function.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$ASSERTS" title="$ASSERTS"><span style="color:#55FF55;">$ASSERTS</span></a>:CONSOLE
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    a = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">10</span>)
    b$ = <span style="color:#55FF55;">myFunc$</span>(a)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a, , b$
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">3</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">myFunc$</span> (value <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_ASSERT</span></a> value &gt; <span style="color:#F580B1;">0</span>, <span style="color:#FFB100;">"Value cannot be zero"</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_ASSERT</span></a> value &lt;= <span style="color:#F580B1;">10</span>, <span style="color:#FFB100;">"Value cannot exceed 10"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> value &gt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> plural$ = <span style="color:#FFB100;">"s"</span>
    <span style="color:#55FF55;">myFunc$</span> = <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(value, <span style="color:#FFB100;">"*"</span>) + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(value) + <span style="color:#FFB100;">" star"</span> + plural$ + <span style="color:#FFB100;">" :-)"</span>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$ASSERTS" title="$ASSERTS">$ASSERTS</a></li>
<li><a href="$CHECKING" title="$CHECKING">$CHECKING</a></li>
<li><a href="Relational_Operations" title="Relational Operations">Relational Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193325
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.027 seconds
Real time usage: 0.042 seconds
Preprocessor visited node count: 289/1000000
Post‐expand include size: 2477/2097152 bytes
Template argument size: 585/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 65/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   29.819      1 -total
 19.35%    5.770      4 Template:Parameter
 10.42%    3.106      1 Template:PageDescription
 10.35%    3.086      1 Template:PageSyntax
  7.52%    2.243     18 Template:Cl
  6.83%    2.037     14 Template:Text
  5.87%    1.749      1 Template:PageAvailability
  5.52%    1.647      1 Template:PageExamples
  5.42%    1.616      1 Template:CodeEnd
  5.41%    1.614      1 Template:Cm
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:45-0!canonical and timestamp 20240714193325 and revision id 8261.
 -->
</div>
</div>
</div>
</div>
</body>
</html>