<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CHAIN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CHAIN rootpage-CHAIN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CHAIN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">CHAIN</a> is used to change seamlessly from one module to another one in a program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CHAIN</a> <i>moduleName$</i></dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li>The multi-modular technique goes back to when <b>QBasic</b> and <b>QuickBASIC</b> had module size constraints. In <b>QB64</b> the <a class="mw-selflink selflink">CHAIN</a> statement has been implemented so that that older code can still be compiled, though it is advisable to use single modules for a single project (not counting <a href="$INCLUDE" title="$INCLUDE">$INCLUDE</a> libraries), for ease of sharing and also because the module size constraints no longer exist.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>moduleName$</i> is a variable or a literal <a href="STRING" title="STRING">STRING</a> value in quotation marks with the optional EXE or BAS file name extension.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>CHAIN requires that both the invoking and called modules are of either .BAS or .EXE file types.</li>
<li>In Windows, <b>QB64</b> will automatically compile a CHAIN referenced BAS file if there is no EXE file found.</li>
<li>CHAIN looks for a file extension that is the same as the invoking module's extension.</li>
<li>The module's filename extension is not required. To save editing at compile time just omit the extensions in the calls.</li>
<li>To pass data from one module to the other use <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a>. The COMMON list should match <a href="Variable_Types" title="Variable Types">types</a> and names.</li>
<li><b>QB64 does not retain the <a href="SCREEN" title="SCREEN">SCREEN</a> mode like QBasic did.</b></li>
<li>Variable data can be passed in files instead of using <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a> values. <b>QB64</b> uses files to pass <a href="COMMON" title="COMMON">COMMON</a> lists.</li>
<li><b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b></li></ul>
<p>
<i>QBasic/QuickBASIC:</i>
</p>
<ul><li>Compiled EXE files had to include BRUN45.EXE in QuickBASIC 4.5 when CHAIN was used with <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> CHAIN looks for same file type extension as program module (BAS or EXE).
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"> <a class="mw-selflink selflink"><span style="color:#4593D8;">CHAIN</span></a> "Level1"
</pre>
</td></tr></tbody></table>
<p><i>Explanation:</i> The file referred to is "Level1.BAS" if the program module using the call is a BAS file. If the program was compiled, it would look for "Level1.EXE".
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="RUN" title="RUN">RUN</a></li>
<li><a href="COMMON" title="COMMON">COMMON</a>, <a href="COMMON_SHARED" title="COMMON SHARED">COMMON SHARED</a></li>
<li><a href="SHARED" title="SHARED">SHARED</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192352
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.039 seconds
Preprocessor visited node count: 45/1000000
Post‐expand include size: 770/2097152 bytes
Template argument size: 32/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.794      1 -total
 13.34%    3.175      1 Template:PageSyntax
 11.49%    2.735      1 Template:Cl
 10.52%    2.504      1 Template:CodeStart
  9.76%    2.322      1 Template:PageParameters
  9.25%    2.201      1 Template:CodeEnd
  9.11%    2.168      2 Template:Parameter
  8.01%    1.905      1 Template:PageDescription
  7.91%    1.881      1 Template:PageSeeAlso
  7.89%    1.877      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:408-0!canonical and timestamp 20240714192352 and revision id 8701.
 -->
</div>
</div>
</div>
</div>
</body>
</html>