<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_OS$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-OS rootpage-OS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_OS$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_OS$</a> function returns the operating system and QB64 compiler bit version <b>used to compile</b> a QB64 program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>compilerVersion$</i> = <a class="mw-selflink selflink">_OS$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns a <a href="STRING" title="STRING">STRING</a> listing the OS as [WINDOWS], [LINUX] or [MACOSX] and the compiler bit format of [32BIT] or [64BIT]. Example: <span style="color:#777777;">[WINDOWS][32BIT]</span></li>
<li>Allows a BAS program to be compiled with QB64 in Windows, Linux or macOS using different OS or language specifications.</li>
<li>Use the return <i>compilerVersion$</i> to specify the current OS code to use when a BAS program is compiled using another version of the QB64 compiler.</li>
<li>Windows can use either a 32 (default) or 64 bit compiler. Linux and macOS use 64 bit by default.</li></ul>
<dl><dt>Important Note</dt>
<dd><ul><li>Even if you're on a 64-bit Windows system, the <a class="mw-selflink selflink">_OS$</a> function may return [32BIT].</li>
<li>That is, if your program was compiled with the 32-bit version of QB64, hence it's a 32-bit executable running on 64-bit Windows.</li>
<li>This is by design and not a bug, as your program gets the information it needs to run (e.g. to use 32-bit or 64-bit DLL using DECLARE DYNAMIC LIBRARY) and not what you as user would expect to see according to your system.</li>
<li>That's why the "<b>used to compile</b>" phrase was printed bold in the first line above.</li></ul></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ENVIRON$" title="ENVIRON$">ENVIRON$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062421
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.020 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 27/1000000
Post‐expand include size: 637/2097152 bytes
Template argument size: 48/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   15.954      1 -total
 24.70%    3.941      1 Template:PageNavigation
 15.19%    2.424      1 Template:PageSyntax
 14.86%    2.371      2 Template:Parameter
 14.74%    2.352      1 Template:PageDescription
 14.11%    2.251      1 Template:PageSeeAlso
 12.71%    2.028      1 Template:Text
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:211-0!canonical and timestamp 20240715062421 and revision id 7920.
 -->
</div>
</div>
</div>
</div>
</body>
</html>