<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LPRINT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LPRINT rootpage-LPRINT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LPRINT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LPRINT</a> statement sends string text or numerical values to a parallel port (LPT1) printer in QBasic or a USB printer in <b>QB64</b>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">LPRINT</a> [<i>expression</i>] [{;|,}]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>expression</i> is one or more text or numerical expressions separated by a semi-colon (;) or comma (,).</li>
<li>Syntax is the same as <a href="PRINT" title="PRINT">PRINT</a>, but cannot use a port number.</li>
<li>Program does not have to <a href="OPEN" title="OPEN">OPEN</a> the LPT1: parallel port.</li>
<li>Assumes a 80 character wide page. <b><a href="Keywords_currently_not_supported_by_QB64" title="Keywords currently not supported by QB64">WIDTH LPRINT is not supported in QB64.</a></b></li>
<li><a href="LPRINT_USING" title="LPRINT USING">LPRINT USING</a> can print formatted text data to a page identically to how <a href="PRINT_USING" title="PRINT USING">PRINT USING</a> formats a program screen.</li>
<li><a href="COLOR" title="COLOR">COLORed</a> text and images can be printed using <a href="PRINTIMAGE" title="PRINTIMAGE">_PRINTIMAGE</a> which stretches them to fit the default printer's paper size.</li>
<li>LPRINT will only print to the default USB or LPT printer set up in Windows. <b><a href="Keywords_currently_not_supported_by_QB64#Keywords_not_supported_in_Linux_or_macOS_versions" title="Keywords currently not supported by QB64">Keyword not supported in Linux or macOS versions</a></b>.</li>
<li>Note: Printer <i>escape codes</i> starting with <a href="CHR$" title="CHR$">CHR$</a>(27) will not work with LPRINT and may produce text printing errors.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="LPRINT_USING" title="LPRINT USING">LPRINT USING</a></li>
<li><a href="PRINTIMAGE" title="PRINTIMAGE">_PRINTIMAGE</a> <span style="color:#777777;">(prints color images to page size)</span></li>
<li><a href="PRINT" title="PRINT">PRINT</a>, <a href="PRINT_USING" title="PRINT USING">PRINT USING</a></li>
<li><a href="Windows_Printer_Settings" title="Windows Printer Settings">Windows Printer Settings</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061339
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.018 seconds
Real time usage: 0.059 seconds
Preprocessor visited node count: 26/1000000
Post‐expand include size: 643/2097152 bytes
Template argument size: 54/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   45.869      1 -total
 26.17%   12.002      1 Template:Text
 24.50%   11.240      2 Template:Parameter
 19.18%    8.797      1 Template:PageNavigation
 15.41%    7.070      1 Template:PageSeeAlso
  7.55%    3.465      1 Template:PageSyntax
  5.68%    2.607      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:507-0!canonical and timestamp 20240715061338 and revision id 7904.
 -->
</div>
</div>
</div>
</div>
</body>
</html>