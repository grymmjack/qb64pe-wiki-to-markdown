<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>POS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-POS rootpage-POS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">POS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>POS</b> function returns the current print cursor text column position.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><dl><dd>column% = POS(0)</dd></dl></dd></dl>
<p>
</p>
<ul><li>The value in parenthesis is normally  0, but any numerical value or variable could be used for compatibility with Basic.</li>
<li>When a semicolon ends the previous PRINT statement the cursor column position will be after the last character printed.</li>
<li>If <a href="TAB" title="TAB">TAB</a> or a comma is used the column position will be immediately after the tabbed position normally 9 spaces after text</li>
<li>If a <a href="PRINT" title="PRINT">PRINT</a> statement does not use a semicolon or comma at the end, the return value will be 1 on the next row.</li>
<li>Column position returned can be saved to return to a previous print position later using <a href="LOCATE" title="LOCATE">LOCATE</a>.</li></ul>
<p>
<i>Example:</i> Column positions after prints.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POS</span></a>(0) 'column position always starts on 1 at top of new or after <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "hello"; 'column position is 6 on same row immediately after text
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POS</span></a>(0)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> 'start new row
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "hello", 'column position is 15 on same row (normally tabs 9 spaces)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POS</span></a>(0)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> 'start new row
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">POS</span></a>(0) ' column position is 1 on next row
</pre>
</td></tr></tbody></table>
<p><i>Note:</i> Column tab prints may not always move 9 spaces past the center of the screen. Some may move text to next row.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CSRLIN" title="CSRLIN">CSRLIN</a>, <a href="LOCATE" title="LOCATE">LOCATE</a>, <a href="PRINT" title="PRINT">PRINT</a></li>
<li><a href="PRINTSTRING" title="PRINTSTRING">_PRINTSTRING</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715035520
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.018 seconds
Real time usage: 0.023 seconds
Preprocessor visited node count: 112/1000000
Post‐expand include size: 1267/2097152 bytes
Template argument size: 120/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   11.995      1 -total
 19.20%    2.303      1 Template:PageSyntax
 18.84%    2.259     14 Template:Cl
 14.06%    1.687      1 Template:CodeStart
 13.61%    1.632      1 Template:PageNavigation
 13.25%    1.589      1 Template:PageSeeAlso
 12.82%    1.538      1 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:432-0!canonical and timestamp 20240715035520 and revision id 7649.
 -->
</div>
</div>
</div>
</div>
</body>
</html>