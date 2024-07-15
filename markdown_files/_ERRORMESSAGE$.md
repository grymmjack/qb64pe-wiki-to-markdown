<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ERRORMESSAGE$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ERRORMESSAGE rootpage-ERRORMESSAGE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ERRORMESSAGE$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_ERRORMESSAGE$</a> function returns a human-readable description of the most recent runtime error, or the description of an arbitrary error code passed to it.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>e$</i> = <a class="mw-selflink selflink">_ERRORMESSAGE$</a></dd>
<dd><i>e$</i> = <a class="mw-selflink selflink">_ERRORMESSAGE$</a>(<i>errorCode%</i>)</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Used in program error troubleshooting.</li>
<li>The message returned is identical to the message shown in the dialog box that appears if your program has no error handler. See <a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a> for the full list of error codes and their messages.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Using an error handler that ignores any error.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="ON_ERROR" title="ON ERROR"><span style="color:#4593D8;">ON ERROR</span></a> <a href="GOTO" title="GOTO"><span style="color:#4593D8;">GOTO</span></a> Errhandler
<span style="color:#919191;">' Main module program error simulation code</span>
<a href="ERROR" title="ERROR"><span style="color:#4593D8;">ERROR</span></a> <span style="color:#F580B1;">7</span> <span style="color:#919191;">' simulate an Out of Memory Error</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Error handled...ending program"</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">4</span>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a> <span style="color:#919191;">' end of program code</span>
Errhandler: <span style="color:#919191;">' error handler sub program line label</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Error"</span>; <a href="ERR" title="ERR"><span style="color:#4593D8;">ERR</span></a>; <span style="color:#FFB100;">"on program file line"</span>; <a href="ERRORLINE" title="ERRORLINE"><span style="color:#4593D8;">_ERRORLINE</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Description: "</span>; <a class="mw-selflink selflink"><span style="color:#4593D8;">_ERRORMESSAGE$</span></a>; <span style="color:#FFB100;">"."</span>
<a href="BEEP" title="BEEP"><span style="color:#4593D8;">BEEP</span></a> <span style="color:#919191;">' warning beep</span>
<a href="RESUME" title="RESUME"><span style="color:#4593D8;">RESUME</span></a> <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> <span style="color:#919191;">' moves program to code following the error.</span>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="ON_ERROR" title="ON ERROR">ON ERROR</a></li>
<li><a href="ERRORLINE" title="ERRORLINE">_ERRORLINE</a></li>
<li><a href="INCLERRORLINE" title="INCLERRORLINE">_INCLERRORLINE</a>, <a href="INCLERRORFILE$" title="INCLERRORFILE$">_INCLERRORFILE$</a></li>
<li><a href="ERR" title="ERR">ERR</a>, <a href="ERL" title="ERL">ERL</a></li>
<li><a href="ERROR" title="ERROR">ERROR</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062328
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.043 seconds
Preprocessor visited node count: 255/1000000
Post‐expand include size: 2262/2097152 bytes
Template argument size: 649/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 272/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   26.161      1 -total
 11.63%    3.042      1 Template:PageSyntax
 10.59%    2.769     13 Template:Text
  9.99%    2.614     14 Template:Cl
  9.73%    2.545      3 Template:Parameter
  9.18%    2.401      1 Template:PageDescription
  8.65%    2.262      1 Template:PageExamples
  7.91%    2.070      1 Template:CodeEnd
  7.88%    2.061      1 Template:CodeStart
  7.07%    1.849      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:743-0!canonical and timestamp 20240715062328 and revision id 8329.
 -->
</div>
</div>
</div>
</div>
</body>
</html>