<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_TRIM$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-TRIM rootpage-TRIM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_TRIM$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_TRIM$</a> function removes both leading and trailing space characters from a <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>return$</i> = <a class="mw-selflink selflink">_TRIM$</a>(<i>text$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Shorthand to using <a href="LTRIM$" title="LTRIM$">LTRIM$</a>(<a href="RTRIM$" title="RTRIM$">RTRIM$</a>("text"))</li>
<li><i>text$</i> is the <a href="STRING" title="STRING">STRING</a> value to trim.</li>
<li>If <i>text$</i> contains no leading or trailing space characters, it is returned unchanged.</li>
<li>Convert fixed length <a href="STRING" title="STRING">STRING</a> values by using a different <i>return$</i> variable.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example: Demonstrating how _TRIM$(text$) can replace LTRIM$(RTRIM$(text$)):</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">text$ = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10) + "some text" + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + text$ + "]"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a href="RTRIM$" title="RTRIM$"><span style="color:#4593D8;">RTRIM$</span></a>(text$) + "]"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(text$) + "]"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="RTRIM$" title="RTRIM$"><span style="color:#4593D8;">RTRIM$</span></a>(text$)) + "]"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + <a class="mw-selflink selflink"><span style="color:#4593D8;">_TRIM$</span></a>(text$) + "]"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">[          some text          ]
[          some text]
[some text          ]
[some text]
[some text]
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1246" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="RTRIM$" title="RTRIM$">RTRIM$</a>, <a href="LTRIM$" title="LTRIM$">LTRIM$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714141914
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.032 seconds
Real time usage: 0.044 seconds
Preprocessor visited node count: 130/1000000
Post‐expand include size: 1396/2097152 bytes
Template argument size: 163/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.654      1 -total
 12.03%    3.206     12 Template:Cl
 10.45%    2.786      5 Template:Parameter
  9.68%    2.581      1 Template:PageSyntax
  8.93%    2.379      1 Template:CodeStart
  8.92%    2.378      1 Template:PageExamples
  8.66%    2.309      1 Template:CodeEnd
  8.63%    2.301      1 Template:OutputStart
  7.23%    1.926      1 Template:OutputEnd
  7.05%    1.880      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:360-0!canonical and timestamp 20240714141914 and revision id 8912.
 -->
</div>
</div>
</div>
</div>
</body>
</html>