<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>CALL - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CALL rootpage-CALL skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">CALL</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">CALL</a> sends code execution to a subroutine procedure in a program. In <b>QB64</b> the subroutine doesn't need to be declared.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">CALL</a> <i>ProcedureName</i> (<i>parameter1</i>, <i>parameter2</i>,...)]</dd></dl>
<h3><span class="mw-headline" id="Alternative_syntax">Alternative syntax</span></h3>
<dl><dd><i>ProcedureName</i> <i>parameter1</i>, <i>parameter2</i>,...]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>CALL requires <a href="SUB" title="SUB">SUB</a> program parameters to be enclosed in brackets (parenthesis).</li>
<li>CALL is not required to call a subprocedure. Use the SUB-procedure name and list any parameters without parenthesis.</li>
<li>Neither syntax can be used to call <a href="GOSUB" title="GOSUB">GOSUB</a> linelabel sub procedures.</li>
<li>To pass parameters by value, instead of by reference, enclose passed variables in parenthesis.</li></ul>
<h3><span id="QBasic.2FQuickBASIC"></span><span class="mw-headline" id="QBasic/QuickBASIC">QBasic/QuickBASIC</span></h3>
<ul><li>PDS or QuickBASIC 7 up could use <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> to pass variables by values instead of reference.</li>
<li>QuickBASIC 4.5 could use <a class="mw-redirect" href="BYVAL" title="BYVAL">BYVAL</a> only for procedures created in Assembly or another language.</li>
<li>QBasic required <a href="CALL_ABSOLUTE" title="CALL ABSOLUTE">CALL ABSOLUTE</a> only. It did not have to be DECLAREd.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> How parameters are passed in two <a href="SUB" title="SUB">SUB</a> calls, one with CALL using brackets and one without CALL or brackets:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> a <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a> 'value not shared with SUB
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> b <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a> 'value shared with any SUB
a = 1
b = 2
c = 3
<a class="mw-selflink selflink"><span style="color:#4593D8;">CALL</span></a> helloworld (a) 'a passed to c parameter with CALL
helloworld a        'a passed to c parameter w/o CALL
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> helloworld (c) 'SUB parameter variables are always inside of brackets in SUB code
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Hello World!"
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a,  b, c
a = a + 1 'a is a SUB value of 0 when printed which may increase inside SUB only
b = b + 1 'b is a shared value which can increase anywhere
c = c + 1 'c is a SUB parameter value from a in calls which may increase inside SUB only
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p><i>Returns:</i>
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Hello World!
 0            2            1
Hello World!
 0            3            1
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> Variable <i><b>a</b></i> that is outside of the subroutine isn't <a href="SHARED" title="SHARED">SHARED</a> so it will have no effect inside the subroutine, the variable <i>a</i> inside the subroutine is only valid inside the subroutine, and whatever value <i>a</i> has outside of it makes no difference within the subroutine.</dd></dl>
<dl><dd>The variable <i><b>b</b></i> on the other hand is <a href="SHARED" title="SHARED">SHARED</a> with the subroutines and thus can be changed in the subroutine. The variable <i>a</i> is initiated with 0 as default when created, thus it will return 0 since it wasn't changed within the subroutine.</dd></dl>
<dl><dd>The variable <i><b>c</b></i> is the <a href="SUB" title="SUB">SUB</a> parameter variable that passes values into the sub. Its value could be changed by the passed parameter value or inside of the subroutine. The un-shared <i><b>c</b></i> variable value outside of the sub is irrelevant within the subroutine.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SUB" title="SUB">SUB</a>, <a href="FUNCTION" title="FUNCTION">FUNCTION</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714121933
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.072 seconds
Real time usage: 0.108 seconds
Preprocessor visited node count: 192/1000000
Post‐expand include size: 1493/2097152 bytes
Template argument size: 187/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   45.958      1 -total
 18.95%    8.709     13 Template:Cl
 13.90%    6.389      1 Template:PageSyntax
  8.10%    3.724      1 Template:PageExamples
  8.06%    3.705      1 Template:CodeEnd
  6.88%    3.162     13 Template:Parameter
  6.72%    3.090      1 Template:OutputStart
  6.54%    3.006      1 Template:OutputEnd
  6.25%    2.870      1 Template:CodeStart
  6.25%    2.870      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:403-0!canonical and timestamp 20240714121933 and revision id 7719.
 -->
</div>
</div>
</div>
</div>
</body>
</html>