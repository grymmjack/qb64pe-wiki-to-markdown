<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>UCASE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-UCASE rootpage-UCASE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">UCASE$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">UCASE$</a> function outputs an all-uppercase version of a <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">UCASE$</a>(<i>text$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used to guarantee that all alphabetical characters in a <a href="STRING" title="STRING">STRING</a> are capitalized.</li>
<li>Does not affect non-alphabetical characters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> The following code guarantees that all letter key entries are capitalized:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Do you want to continue? (y/n)"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
    K$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">UNTIL</span></a> K$ = "Y" <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> K$ = "N"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1232" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="LCASE$" title="LCASE$">LCASE$</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="INPUT$" title="INPUT$">INPUT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714081828
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.032 seconds
Preprocessor visited node count: 77/1000000
Post‐expand include size: 1033/2097152 bytes
Template argument size: 88/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.855      1 -total
 15.22%    3.021      1 Template:PageSyntax
 13.24%    2.630      2 Template:Parameter
 12.04%    2.391      1 Template:PageExamples
 11.58%    2.299      1 Template:PageDescription
  9.37%    1.860      1 Template:CodeStart
  8.85%    1.756      7 Template:Cl
  7.74%    1.537      1 Template:CodeEnd
  7.73%    1.535      1 Template:PageNavigation
  7.57%    1.503      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:376-0!canonical and timestamp 20240714081828 and revision id 8907.
 -->
</div>
</div>
</div>
</div>
</body>
</html>