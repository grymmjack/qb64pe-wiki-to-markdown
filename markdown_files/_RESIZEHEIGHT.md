<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_RESIZEHEIGHT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-RESIZEHEIGHT rootpage-RESIZEHEIGHT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_RESIZEHEIGHT</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_RESIZEHEIGHT</a> function returns the user resized screen pixel height if <a href="$RESIZE" title="$RESIZE">$RESIZE</a>:ON allows it and <a href="RESIZE_(function)" title="RESIZE (function)">_RESIZE</a> returns -1
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>newHeight&amp;</i> = <a class="mw-selflink selflink">_RESIZEHEIGHT</a></dd></dl>
<p>
<i>Details:</i>
</p>
<ul><li><a href="RESIZE_(function)" title="RESIZE (function)">_RESIZE</a> function must return true (-1) before the requested screen dimensions can be returned by the function.</li>
<li>The program should decide if the request is allowable for proper program interaction.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>Version 1.000 and up</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Resize the current screen image according to user's request.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$RESIZE" title="$RESIZE"><span style="color:#4593D8;">$RESIZE</span></a>:ON
s&amp; = <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(300, 300, 32)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> s&amp;
bee&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>("qb64_trans.png") 'any image
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="RESIZE_(function)" title="RESIZE (function)"><span style="color:#4593D8;">_RESIZE</span></a> THEN
        oldimage&amp; = s&amp;
        s&amp; = _NEWIMAGE(_RESIZEWIDTH, _RESIZEHEIGHT, 32)
        SCREEN s&amp;
        <a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> oldimage&amp;
    END IF
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    'Center the QB64 bee image:
    x = <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> / 2 - _WIDTH(bee&amp;) / 2
    y = <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / 2 - _HEIGHT(bee&amp;) / 2
    <a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (x, y), bee&amp;
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 30
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$RESIZE" title="$RESIZE">$RESIZE</a></li>
<li><a href="RESIZE_(function)" title="RESIZE (function)">_RESIZE (function)</a></li>
<li><a href="RESIZEWIDTH" title="RESIZEWIDTH">_RESIZEWIDTH</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062433
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.030 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 134/1000000
Post‐expand include size: 1506/2097152 bytes
Template argument size: 232/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   22.942      1 -total
 13.19%    3.026     15 Template:Cl
 12.25%    2.810      1 Template:PageSyntax
 11.09%    2.545      2 Template:Parameter
 10.55%    2.421      1 Template:CodeStart
 10.48%    2.404      1 Template:PageAvailability
  9.96%    2.286      1 Template:PageExamples
  8.60%    1.973      1 Template:CodeEnd
  8.51%    1.953      1 Template:PageSeeAlso
  8.38%    1.922      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:224-0!canonical and timestamp 20240715062433 and revision id 7173.
 -->
</div>
</div>
</div>
</div>
</body>
</html>