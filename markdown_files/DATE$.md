<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>DATE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DATE rootpage-DATE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">DATE$</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">DATE$</a> function returns the current computer date as a string in the format "mm-dd-yyyy".
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>today$</i> = <a class="mw-selflink selflink">DATE$</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns the current computer date in the format "mm-dd-yyyy" (e.g., "12-25-2009").</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Displaying the weekday and current date.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">DATE$</span></a>
month$ = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">DATE$</span></a>, 2): M = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(month$)
day$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">DATE$</span></a>, 4, 2): D = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(day$)
day$ = <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(D)                  ' eliminate any leading zeros
year$ = <a href="RIGHT$" title="RIGHT$"><span style="color:#4593D8;">RIGHT$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">DATE$</span></a>, 4): Y = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(year$)
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> M
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1: Moon$ = "January"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2: Moon$ = "February"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 3: Moon$ = "March"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 4: Moon$ = "April"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 5: Moon$ = "May"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 6: Moon$ = "June"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 7: Moon$ = "July"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 8: Moon$ = "August"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 9: Moon$ = "September"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 10: Moon$ = "October"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 11: Moon$ = "November"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 12: Moon$ = "December"
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Today is " + WeekDay$(M, D, Y) + ", " + Moon$ + day$ + ", " + year$ + <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(10)
<a href="DEFINT" title="DEFINT"><span style="color:#4593D8;">DEFINT</span></a> A-Z
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> WeekDay$ (M, D, Y)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> M &lt; 3 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> M = M + 12: Y = Y - 1  'add 12 to Jan - Feb month, -1 year
C = Y \ 100: Y = Y <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 100           'split century and year number
S1 = (C \ 4) - (2 * C) - 1           'century leap
S2 = (5 * Y) \ 4                     '4 year leap
S3 = 26 * (M + 1) \ 10               'days in months
WkDay = (S1 + S2 + S3 + D) <a href="MOD" title="MOD"><span style="color:#4593D8;">MOD</span></a> 7     'weekday total remainder
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> WkDay &lt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> WkDay = WkDay + 7  'Adjust negative results to 0 to 6
<a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> WkDay
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 0: day$ = "Sunday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 1: day$ = "Monday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 2: day$ = "Tuesday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 3: day$ = "Wednesday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 4: day$ = "Thursday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 5: day$ = "Friday"
   <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> 6: day$ = "Saturday"
<a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
WeekDay$ = day$
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">06-02-2010
Today is Wednesday, June 2, 2010
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="TIME$" title="TIME$">TIME$</a>, <a href="IF...THEN" title="IF...THEN">IF...THEN</a></li>
<li><a href="VAL" title="VAL">VAL</a>, <a href="STR$" title="STR$">STR$</a>, <a href="MID$_(function)" title="MID$ (function)">MID$ (function)</a>, <a href="LEFT$" title="LEFT$">LEFT$</a>, <a href="RIGHT$" title="RIGHT$">RIGHT$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061251
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.063 seconds
Preprocessor visited node count: 356/1000000
Post‐expand include size: 3224/2097152 bytes
Template argument size: 492/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   34.103      1 -total
 14.49%    4.942     46 Template:Cl
  9.12%    3.110      1 Template:PageSyntax
  7.54%    2.570      1 Template:CodeEnd
  6.52%    2.225      1 Template:Small
  6.34%    2.162      1 Template:CodeStart
  6.31%    2.153      1 Template:Parameter
  6.23%    2.125      1 Template:PageSeeAlso
  6.20%    2.116      1 Template:OutputEnd
  6.18%    2.107      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:451-0!canonical and timestamp 20240715061251 and revision id 8122.
 -->
</div>
</div>
</div>
</div>
</body>
</html>