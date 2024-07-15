<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LCASE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LCASE rootpage-LCASE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LCASE$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LCASE$</a> function outputs an all-lowercase version of a <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">LCASE$</a>(<i>text$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Normally used to guarantee that user input is not capitalized.</li>
<li>Does not affect non-alphabetical characters.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> The following code guarantees that all user letter entries will be lower case:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Do you want to continue? (y/n)"
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a>
    K$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">LCASE$</span></a>(<a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>)
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP</span></a> <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">UNTIL</span></a> K$ = "y" <a href="OR" title="OR"><span style="color:#4593D8;">OR</span></a> K$ = "n"
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1232" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="UCASE$" title="UCASE$">UCASE$</a> <span style="color:#777777;">(upper case)</span></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a></li>
<li><a href="INPUT$" title="INPUT$">INPUT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061328
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.029 seconds
Real time usage: 0.046 seconds
Preprocessor visited node count: 83/1000000
Post‐expand include size: 1081/2097152 bytes
Template argument size: 100/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.806      1 -total
 28.30%    8.719      1 Template:PageSyntax
  8.53%    2.627      2 Template:Parameter
  8.17%    2.518      7 Template:Cl
  8.03%    2.473      1 Template:PageExamples
  7.44%    2.291      1 Template:PageNavigation
  7.36%    2.266      1 Template:Text
  7.01%    2.159      1 Template:CodeStart
  6.88%    2.118      1 Template:CodeEnd
  6.68%    2.059      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:377-0!canonical and timestamp 20240715061328 and revision id 8906.
 -->
</div>
</div>
</div>
</div>
</body>
</html>