<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>OPTION _EXPLICITARRAY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OPTION_EXPLICITARRAY rootpage-OPTION_EXPLICITARRAY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">OPTION _EXPLICITARRAY</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a> instructs the compiler to require arrays to be properly dimensioned with <a href="DIM" title="DIM">DIM</a> or <a href="REDIM" title="REDIM">REDIM</a> before first use. However, it doesn't require regular variables to be declared.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Normally statements like <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">x(2) = 3</span> will implicitly create an array x(). <a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a> requires proper dimensioning for the array, helping to catch mistyped array and function names.</li>
<li>Unlike <a href="OPTION_EXPLICIT" title="OPTION EXPLICIT">OPTION _EXPLICIT</a>, simple variables can still be used without a declaration. Example: <span style="border: 2px solid #87cefa; border-radius: 4px; padding: 4px; font-family: Courier New, monospace, Courier; font-size: 16px; white-space: nowrap; background: #082080; color: #e2e2e2;">i = 1</span></li></ul>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>If used, <a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a> must be the very first statement in your program. No other statements can precede it (except for <a href="$NOPREFIX" title="$NOPREFIX">$NOPREFIX</a> or comment lines started with an <a href="Apostrophe" title="Apostrophe">apostrophe</a> or <a href="REM" title="REM">REM</a>).</li>
<li>Do not use <a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a> in <a href="$INCLUDE" title="$INCLUDE">$INCLUDEd</a> modules.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Avoiding simple typos with <a class="mw-selflink selflink">OPTION _EXPLICITARRAY</a> results shown in the QB64 IDE Status area.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">OPTION _EXPLICITARRAY</span></a>
x = 1 'This is fine, it's not an array so not affected
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> z(5)
z(2) = 3 'All good here, we've explicitly DIMmed our array
y(2) = 3 'This now generates an error
</pre>
</td></tr></tbody></table>
<p><i>QB64 IDE Status will show:</i>
<b>Array 'y' (SINGLE) not defined on line 7</b>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT">OPTION _EXPLICIT</a></li>
<li><a href="DIM" title="DIM">DIM</a>, <a href="REDIM" title="REDIM">REDIM</a></li>
<li><a href="SHARED" title="SHARED">SHARED</a></li>
<li><a href="STATIC" title="STATIC">STATIC</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062330
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.049 seconds
Preprocessor visited node count: 64/1000000
Post‐expand include size: 1186/2097152 bytes
Template argument size: 48/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   33.205      1 -total
 26.21%    8.704      1 Template:PageNavigation
 10.87%    3.609      2 Template:Cl
  8.84%    2.935      1 Template:PageSyntax
  8.09%    2.686      1 Template:CodeEnd
  7.64%    2.536      1 Template:PageDescription
  7.34%    2.437      1 Template:CodeStart
  7.04%    2.337      2 Template:InlineCode
  6.71%    2.228      1 Template:PageSeeAlso
  6.69%    2.223      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:210-0!canonical and timestamp 20240715062330 and revision id 7351.
 -->
</div>
</div>
</div>
</div>
</body>
</html>