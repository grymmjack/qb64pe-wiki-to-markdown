<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$ERROR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_ERROR rootpage-_ERROR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$ERROR</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>$ERROR</b> <a href="Metacommand" title="Metacommand">metacommand</a> triggers a compilation error.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>$ERROR</b> <i>message</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>This metacommand does not require a comment <i><a href="Apostrophe" title="Apostrophe">'</a></i> or <a href="REM" title="REM">REM</a> before it.</li>
<li><i>message</i> is any text. Quotation marks are not required.</li>
<li>When QB64 tries to compile an <b>$ERROR</b> metacommand a compilation error is triggered and <i>message</i> is shown to the user. This is useful in <a href="$IF" title="$IF">$IF</a> blocks.</li>
<li>If there is a particular situation where you know your program will not work properly, you can prevent the user compiling and give them a helpful error message instead by checking for the condition with <a href="$IF" title="$IF">$IF</a>.</li>
<li>An <b>$ERROR</b> directive not inside an conditional <a href="$IF" title="$IF">$IF</a> (or <a class="mw-redirect" href="$ELSEIF" title="$ELSEIF">$ELSEIF</a>) block is useless because the program will <b>never</b> compile in that case.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$IF" title="$IF"><span style="color:#55FF55;">$IF</span></a> <span style="color:#55FF55;">VERSION</span> &lt; <span style="color:#F580B1;">2.1</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#55FF55;">OR</span></a> <span style="color:#55FF55;">WINDOWS</span> = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
    <a class="mw-selflink selflink"><span style="color:#55FF55;">$ERROR</span></a> Requires Windows QB64 version 2.1 or above
<a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
</pre>
</td></tr></tbody></table>
<dl><dt>Output (IDE Status Area)</dt>
<dd>Compilation check failed: REQUIRES WINDOWS QB64 VERSION 2.1 OR ABOVE on line 2 (assuming your version of QB64 doesn't meet those requirements).</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Metacommand" title="Metacommand">Metacommand</a></li>
<li><a href="$IF" title="$IF">$IF</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061209
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.038 seconds
Real time usage: 0.072 seconds
Preprocessor visited node count: 95/1000000
Post‐expand include size: 1104/2097152 bytes
Template argument size: 121/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.891      1 -total
 26.24%   13.878      4 Template:Text
 14.97%    7.920      5 Template:Cm
 14.56%    7.703      1 Template:PageSeeAlso
  7.91%    4.184      1 Template:PageSyntax
  6.00%    3.173      1 Template:CodeEnd
  5.70%    3.014      1 Template:PageExamples
  5.45%    2.885      1 Template:PageNavigation
  5.24%    2.772      3 Template:Parameter
  5.18%    2.741      1 Template:CodeStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:744-0!canonical and timestamp 20240715061209 and revision id 8327.
 -->
</div>
</div>
</div>
</div>
</body>
</html>