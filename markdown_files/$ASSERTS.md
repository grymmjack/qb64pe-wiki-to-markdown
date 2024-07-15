<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$ASSERTS - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_ASSERTS rootpage-_ASSERTS skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$ASSERTS</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>$ASSERTS</b> <a href="Metacommand" title="Metacommand">metacommand</a> enables debug tests with the <a href="ASSERT" title="ASSERT">_ASSERT</a> macro.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><b>$ASSERTS</b></dd>
<dd><b>$ASSERTS:CONSOLE</b></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>This metacommand does not require a comment <i><a href="Apostrophe" title="Apostrophe">'</a></i> or <a href="REM" title="REM">REM</a> before it. There is no space between the metacommand name, the colon and the CONSOLE parameter.</li>
<li>If this metacommand is used in a program and any of the set <a href="ASSERT" title="ASSERT">_ASSERT</a> checkpoints will fail, then the program will stop with an <b><span style="color:red;">_ASSERT failed</span></b> error.</li>
<li>Detailed error messages passed to the <a href="ASSERT" title="ASSERT">_ASSERT</a> statement will be displayed in the console window, but only if <b>$ASSERTS:CONSOLE</b> is used.</li></ul>
<dl><dt>Note</dt>
<dd>This metacommand is the main switch to enable debug tests during development. Later just remove this metacommand to compile the program without debugging code, all the <a href="ASSERT" title="ASSERT">_ASSERT</a> statements may remain in the code for later debugging sessions, they are simply ignored without this metacommand.</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.4"><img alt="v1.4" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.4</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="all"><img alt="all" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>all</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Apix.png"><img alt="Apix.png" decoding="async" height="48" src="/qb64wiki/images/5/5f/Apix.png" width="48"/></a></div></div>
<div class="gallerytext">
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Win.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/29/Win.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Lnx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/7/7a/Lnx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Osx.png" title="yes"><img alt="yes" decoding="async" height="48" src="/qb64wiki/images/2/22/Osx.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>yes</b>
</p>
</div>
</div></li>
</ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Adding test checks for parameter inputs in a function.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$ASSERTS</span></a>:CONSOLE
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    a = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">10</span>)
    b$ = <span style="color:#55FF55;">myFunc$</span>(a)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> a, , b$
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">3</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">myFunc$</span> (value <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>)
    <a href="ASSERT" title="ASSERT"><span style="color:#4593D8;">_ASSERT</span></a> value &gt; <span style="color:#F580B1;">0</span>, <span style="color:#FFB100;">"Value cannot be zero"</span>
    <a href="ASSERT" title="ASSERT"><span style="color:#4593D8;">_ASSERT</span></a> value &lt;= <span style="color:#F580B1;">10</span>, <span style="color:#FFB100;">"Value cannot exceed 10"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> value &gt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> plural$ = <span style="color:#FFB100;">"s"</span>
    <span style="color:#55FF55;">myFunc$</span> = <a href="STRING$" title="STRING$"><span style="color:#4593D8;">STRING$</span></a>(value, <span style="color:#FFB100;">"*"</span>) + <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(value) + <span style="color:#FFB100;">" star"</span> + plural$ + <span style="color:#FFB100;">" :-)"</span>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="Metacommand" title="Metacommand">Metacommand</a></li>
<li><a href="ASSERT" title="ASSERT">_ASSERT</a></li>
<li><a href="$CHECKING" title="$CHECKING">$CHECKING</a></li>
<li><a href="Relational_Operations" title="Relational Operations">Relational Operations</a></li>
<li><a href="ERROR_Codes" title="ERROR Codes">ERROR Codes</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714193323
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.056 seconds
Real time usage: 0.084 seconds
Preprocessor visited node count: 287/1000000
Post‐expand include size: 2463/2097152 bytes
Template argument size: 558/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2424/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   61.683      1 -total
  7.70%    4.748     18 Template:Cl
  7.39%    4.556      1 Template:CodeEnd
  7.15%    4.410     15 Template:Text
  6.76%    4.168      1 Template:PageAvailability
  5.03%    3.103      1 Template:PageSeeAlso
  4.95%    3.056      1 Template:PageSyntax
  4.62%    2.852      1 Template:PageExamples
  4.24%    2.617      1 Template:PageNavigation
  4.23%    2.611      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:46-0!canonical and timestamp 20240714193323 and revision id 8262.
 -->
</div>
</div>
</div>
</div>
</body>
</html>