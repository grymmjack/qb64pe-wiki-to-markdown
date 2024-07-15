<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OPTION _EXPLICIT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPTION_EXPLICIT rootpage-OPTION_EXPLICIT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">OPTION _EXPLICIT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">OPTION _EXPLICIT</a> instructs the compiler to require variable declaration with <a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a> or an equivalent statement.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">OPTION _EXPLICIT</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>With <a class="mw-selflink selflink">OPTION _EXPLICIT</a> you can avoid typos by having QB64 immediately warn in the <b>Status area</b> of new variables used without previous declaration.</li>
<li>The use of <a class="mw-selflink selflink">OPTION _EXPLICIT</a> does also enforce the requirement to <a href="DIM" title="DIM">DIM</a> or <a href="REDIM" title="REDIM">REDIM</a> any arrays before first use, no extra <a href="OPTION_EXPLICITARRAY" title="OPTION EXPLICITARRAY">OPTION _EXPLICITARRAY</a> is needed.</li>
<li>Enable <a class="mw-selflink selflink">OPTION _EXPLICIT</a> temporarily even if a program source file doesn't contain the directive by specifying the <b>-e</b> switch when compiling via command line (<i>qb64 -c file.bas -e</i>).</li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>If used, <a class="mw-selflink selflink">OPTION _EXPLICIT</a> must be the very first statement in your program. No other statements can precede it (except for <a href="$NOPREFIX" title="$NOPREFIX">$NOPREFIX</a> or comment lines started with an <a href="Apostrophe" title="Apostrophe">apostrophe</a> or <a href="REM" title="REM">REM</a>).</li>
<li>Do not use <a class="mw-selflink selflink">OPTION _EXPLICIT</a> in <a href="$INCLUDE" title="$INCLUDE">$INCLUDEd</a> modules.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Avoiding simple typos with <a class="mw-selflink selflink">OPTION _EXPLICIT</a> results shown in the QB64 IDE Status area.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OPTION _EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> myVariable <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>
myVariable = 5
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> myVariabe
</pre>
</td></tr></tbody></table>
<p><i>QB64 IDE Status will show:</i>
<b>Variable 'myVariabe' (SINGLE) not defined on line 4</b>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1727" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="OPTION_EXPLICITARRAY" title="OPTION EXPLICITARRAY">OPTION _EXPLICITARRAY</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="STATIC" title="STATIC">STATIC</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714132535
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.030 seconds
Preprocessor visited node count: 73/1000000
Post‐expand include size: 921/2097152 bytes
Template argument size: 66/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.460      1 -total
 16.84%    2.941      1 Template:PageSyntax
 12.98%    2.267      1 Template:PageDescription
 11.82%    2.064      1 Template:CodeStart
 11.36%    1.983      5 Template:Cl
 10.67%    1.863      1 Template:PageExamples
 10.61%    1.853      1 Template:CodeEnd
 10.42%    1.820      1 Template:PageNavigation
 10.39%    1.814      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:209-0!canonical and timestamp 20240714132535 and revision id 8936.
 -->
</div>
</div>
</div>
</div>
</body>
</html>