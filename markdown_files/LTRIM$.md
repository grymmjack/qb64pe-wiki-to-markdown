<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>LTRIM$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-LTRIM rootpage-LTRIM skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">LTRIM$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">LTRIM$</a> function removes leading space characters from a <a href="STRING" title="STRING">STRING</a> value.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>return$</i> = <a class="mw-selflink selflink">LTRIM$</a>(<i>text$</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>text$</i> is the <a href="STRING" title="STRING">STRING</a> value to trim.</li>
<li>If <i>text$</i> contains no leading space characters, it is returned unchanged.</li>
<li>Convert fixed length <a href="STRING" title="STRING">STRING</a> values by using a different <i>return$</i> variable.</li>
<li>Can be used to trim the leading space of a positive numerical value converted to a string value by <a href="STR$" title="STR$">STR$</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Trimming a positive string number.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">value = 12345
number$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(value)) 'converting number to string removes right PRINT space
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "[" + number$ + "]"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">[12345]
</pre>
</td></tr></tbody></table>
<p>
<i>Example 2:</i> Trimming leading spaces from text strings.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">LTRIM$</span></a>("some text")
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">LTRIM$</span></a>("   some text")
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">some text
some text
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> A TRIM$ function to trim spaces off of both ends of a string.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">text$ = "        Text String           "
trimmed$ = TRIM$(text$)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(26) + trimmed$ + <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(27)
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> TRIM$(text$)
TRIM$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="RTRIM$" title="RTRIM$"><span style="color:#4593D8;">RTRIM$</span></a>(text$))
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">→Text String←
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1246" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="TRIM$" title="TRIM$">_TRIM$</a>, <a href="RTRIM$" title="RTRIM$">RTRIM$</a>, <a href="STR$" title="STR$">STR$</a></li>
<li><a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a></li>
<li><a href="HEX$" title="HEX$">HEX$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061340
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.028 seconds
Real time usage: 0.045 seconds
Preprocessor visited node count: 155/1000000
Post‐expand include size: 1786/2097152 bytes
Template argument size: 193/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   24.549      1 -total
 23.79%    5.841     14 Template:Cl
  7.98%    1.959      1 Template:PageNavigation
  7.60%    1.865      1 Template:PageSeeAlso
  7.47%    1.834      1 Template:PageSyntax
  7.07%    1.735      3 Template:CodeEnd
  6.92%    1.699      3 Template:CodeStart
  6.55%    1.607      5 Template:Parameter
  6.13%    1.504      1 Template:PageExamples
  6.00%    1.473      3 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:518-0!canonical and timestamp 20240715061340 and revision id 8910.
 -->
</div>
</div>
</div>
</div>
</body>
</html>