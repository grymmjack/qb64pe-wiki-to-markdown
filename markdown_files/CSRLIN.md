<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CSRLIN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CSRLIN rootpage-CSRLIN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CSRLIN</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">CSRLIN</a> function returns the current text row position of the <a href="PRINT" title="PRINT">PRINT</a> cursor.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>row%</i> = <a class="mw-selflink selflink">CSRLIN</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The value returned is within the range of 1 to the current number of rows in the <a href="SCREEN" title="SCREEN">SCREEN</a> mode used.
<ul><li>In <a href="SCREEN" title="SCREEN">SCREEN</a> 0 (text mode), the <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> function returns the number of text rows.</li>
<li>In graphic modes, the number of available text rows can be calculated by dividing <a href="HEIGHT" title="HEIGHT">_HEIGHT</a> (measured in pixels in graphic modes) by <a href="FONTHEIGHT" title="FONTHEIGHT">_FONTHEIGHT</a>: <b><i>totalRows%</i> = _HEIGHT / _FONTHEIGHT</b></li></ul></li>
<li>In screen modes that support page flipping, the <a class="mw-selflink selflink">CSRLIN</a> function returns the vertical coordinate of the cursor on the active page.</li>
<li>x = <a href="POS" title="POS">POS</a>(0) returns the column location of the cursor.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> A semicolon stops the print cursor immediately after the print.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">  LOCATE 5, 5: PRINT "HELLO ";
  Y = <a class="mw-selflink selflink"><span style="color:#4593D8;">CSRLIN</span></a> 'save the row
  X = <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(0) 'save the column
  LOCATE 10, 10: PRINT "WORLD"
  LOCATE Y, X 'restore saved position
  PRINT "GOODBYE"
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">
         HELLO GOODBYE
         WORLD
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> "HELLO " is printed and the semicolon stops the cursor immediately after the text. The <a class="mw-selflink selflink">CSRLIN</a> variable records the current print cursor's text row in Y. The <a href="POS" title="POS">POS</a> function records the current print cursor's text column in X. The second <a href="PRINT" title="PRINT">PRINT</a> statement displays the comment "WORLD" on the 10th line of the screen. The last <a href="LOCATE" title="LOCATE">LOCATE</a> statement restores the position of the cursor to the original line and column immediately after the first print.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SCREEN" title="SCREEN">SCREEN</a>, <a href="LOCATE" title="LOCATE">LOCATE</a>, <a href="POS" title="POS">POS</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a> (graphic print)</li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035410
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.021 seconds
Real time usage: 0.031 seconds
Preprocessor visited node count: 43/1000000
Post‐expand include size: 829/2097152 bytes
Template argument size: 22/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   19.616      1 -total
 17.83%    3.497      1 Template:PageSeeAlso
 10.48%    2.056      1 Template:PageNavigation
  8.76%    1.718      1 Template:PageSyntax
  7.64%    1.499      1 Template:CodeEnd
  7.57%    1.485      1 Template:Parameter
  7.43%    1.458      1 Template:CodeStart
  7.27%    1.426      2 Template:Cl
  7.19%    1.410      1 Template:PageDescription
  7.17%    1.406      1 Template:OutputStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:431-0!canonical and timestamp 20240715035410 and revision id 7247.
 -->
</div>
</div>
</div>
</div>
</body>
</html>