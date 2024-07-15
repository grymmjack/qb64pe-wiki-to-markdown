<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$LET - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_LET rootpage-_LET skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$LET</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">$LET</a> is a precompiler command, which helps to include and/or exclude sections of code in a program based on OS/bit-size or other predefined conditions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$LET</a> variable = expression</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Unlike <a href="LET" title="LET">LET</a>, <a class="mw-selflink selflink">$LET</a> is not optional.</li>
<li>$LET a = 12 sets a precompiler variable "a" to the value of 12.   This variable is only valid for the precompiler itself and does nothing to affect the values of any variable/constant which might also be called "a" in the program.</li>
<li>Variable names must follow QB64's variable naming conventions.</li>
<li>You can check a precompiler variable against special values <b>DEFINED</b> and <b>UNDEFINED</b>, in order to assess whether the variable has already been assigned a value. Useful for code in libraries which may be repeated.</li>
<li>The precompiler comes with some preset values which can be used to help determine which code blocks to include/exclude.  These are:
<ul><li><b>WIN</b> or <b>WINDOWS</b> if the user is running QB64 in a Windows environment.</li>
<li><b>LINUX</b> if the user is running QB64 in a Linux environment.</li>
<li><b>MAC</b> or <b>MACOSX</b> if the user is running QB64 in a macOS environment.</li>
<li><b>32BIT</b> if the user is running a 32-bit version of QB64.</li>
<li><b>64BIT</b> if the user is running a 64-bit version of QB64.</li>
<li><b>VERSION</b>, which is set to the version of the QB64 compiler.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<ul><li>See example 1 in <a href="$IF" title="$IF">$IF</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$IF" title="$IF">$IF</a></li>
<li><a class="mw-redirect" href="$ELSE" title="$ELSE">$ELSE</a></li>
<li><a class="mw-redirect" href="$ELSEIF" title="$ELSEIF">$ELSEIF</a></li>
<li><a class="mw-redirect" href="$END_IF" title="$END IF">$END IF</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192331
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.017 seconds
Real time usage: 0.023 seconds
Preprocessor visited node count: 15/1000000
Post‐expand include size: 582/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   10.703      1 -total
 25.36%    2.714      1 Template:PageSyntax
 18.68%    2.000      1 Template:PageDescription
 17.68%    1.892      1 Template:PageExamples
 17.46%    1.869      1 Template:PageNavigation
 16.63%    1.780      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:164-0!canonical and timestamp 20240714192331 and revision id 4906.
 -->
</div>
</div>
</div>
</div>
</body>
</html>