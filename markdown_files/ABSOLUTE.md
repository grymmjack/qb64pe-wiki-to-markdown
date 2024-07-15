<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CALL ABSOLUTE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CALL_ABSOLUTE rootpage-CALL_ABSOLUTE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CALL ABSOLUTE</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">CALL ABSOLUTE</a> is used to access interrupts on the computer or execute assembly type procedures.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CALL ABSOLUTE</a>([<i>argumentList</i>,] <i>integerOffset</i>)</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li><a class="mw-selflink selflink">CALL ABSOLUTE</a> is implemented to support older code and is not recommended practice. To handle mouse input, use <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> and related functions.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><a href="CALL" title="CALL">CALL</a> and parameter brackets are required in the statement.</li>
<li><i>argumentList</i> contains the list of arguments passed to the procedure.</li>
<li><i>integerOffset</i> contains the offset from the current code segment, set by <a href="DEF_SEG" title="DEF SEG">DEF SEG</a> and <a href="SADD" title="SADD">SADD</a>, to the starting location of the called procedure.</li>
<li>QBasic and <b>QB64</b> have the ABSOLUTE statement built in and require no library, like QuickBASIC did.</li>
<li><b>NOTE: QB64 does not support INT 33h mouse functions above 3 or <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> in an ABSOLUTE statement. Registers are emulated.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SADD" title="SADD">SADD</a>, <a href="INTERRUPT" title="INTERRUPT">INTERRUPT</a></li>
<li><a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715031516
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.014 seconds
Real time usage: 0.019 seconds
Preprocessor visited node count: 37/1000000
Post‐expand include size: 611/2097152 bytes
Template argument size: 50/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    8.835      1 -total
 21.53%    1.902      1 Template:PageSyntax
 20.93%    1.849      1 Template:PageNavigation
 18.21%    1.609      1 Template:PageSeeAlso
 17.49%    1.545      4 Template:Parameter
 15.73%    1.390      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:391-0!canonical and timestamp 20240715031516 and revision id 6742.
 -->
</div>
</div>
</div>
</div>
</body>
</html>