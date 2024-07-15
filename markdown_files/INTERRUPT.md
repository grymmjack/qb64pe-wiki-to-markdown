<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>INTERRUPT - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INTERRUPT rootpage-INTERRUPT skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">INTERRUPT</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">INTERRUPT</a> statement is an assembly routine for accessing computer information registers.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="CALL" title="CALL">CALL</a> <a class="mw-selflink selflink">INTERRUPT</a>(<i>intNum</i>, <i>inRegs</i>, <i>outRegs</i>)</dd></dl>
<h3><span class="mw-headline" id="Legacy_support">Legacy support</span></h3>
<ul><li>Registers are emulated in <b>QB64</b> to allow older programs to be compiled. To enable mouse input in your programs, the recommended practice is to use <a href="MOUSEINPUT" title="MOUSEINPUT">_MOUSEINPUT</a> and related functions.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>Registers are emulated in QB64 and there is no support for <i>intNum</i> 33h mouse functions above 3 or <i>intNum</i> requests other than 33.</li>
<li><i>inRegs</i> are the values placed into the call and <i>outRegs</i> are the register return values.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>Available in QuickBASIC versions 4 and up and required an external library to be loaded. <b>QB64</b> emulates the statement without an external library.</li>
<li><i>intNum</i> is the interrupt reference vector table address. For historic reference, see: <a class="external text" href="http://www.ctyme.com/intr/cat.htm" rel="nofollow">Ralf Brown's Interrupt List</a></li>
<li>The <a href="TYPE" title="TYPE">TYPE</a> definition below will work for both <a class="mw-selflink selflink">INTERRUPT</a> and INTERRUPTX statement calls</li>
<li>INTERRUPT can use all of the below TYPE elements when they are required.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputtext"><a href="TYPE" title="TYPE"><span style="color:blue;">TYPE</span></a> RegTypeX
   ax AS INTEGER
   bx AS INTEGER
   cx AS INTEGER
   dx AS INTEGER
   bp AS INTEGER
   si AS INTEGER
   di AS INTEGER
   flags AS INTEGER
   ds AS INTEGER
   es AS INTEGER
<a class="mw-redirect" href="END_TYPE" title="END TYPE"><span style="color:blue;">END TYPE</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> inregs <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> RegTypeX, outregs <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> RegTypeX
</pre>
</td></tr></tbody></table>
<dl><dd>QBasic's <i>RegType.BI</i> $INCLUDE file can be used by INTERRUPT or <a href="INTERRUPTX" title="INTERRUPTX">INTERRUPTX</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="$INCLUDE" title="$INCLUDE">$INCLUDE:</a></li>
<li><a href="QB.BI" title="QB.BI">QB.BI</a>, <a href="CALL_ABSOLUTE" title="CALL ABSOLUTE">CALL ABSOLUTE</a></li>
<li><a href="INTERRUPTX" title="INTERRUPTX">INTERRUPTX</a></li>
<li>Ethan Winer's free QBasic Book and Programs: <a class="external text" href="http://www.ethanwiner.com/fullmoon.html" rel="nofollow">WINER.ZIP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192451
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.085 seconds
Preprocessor visited node count: 123/1000000
Post‐expand include size: 1054/2097152 bytes
Template argument size: 100/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   61.771      1 -total
 16.28%   10.057      2 Template:Cb
 13.92%    8.598      1 Template:TextStart
 12.04%    7.440      1 Template:TextEnd
 11.23%    6.940      1 Template:PageParameters
 10.86%    6.706      8 Template:Parameter
  6.35%    3.920      1 Template:PageSeeAlso
  5.61%    3.465      1 Template:PageSyntax
  5.27%    3.258      1 Template:CodeEnd
  4.76%    2.940      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:478-0!canonical and timestamp 20240714192451 and revision id 7500.
 -->
</div>
</div>
</div>
</div>
</body>
</html>