<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ORELSE - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ORELSE rootpage-ORELSE skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ORELSE</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_ORELSE</a> is a <a href="Boolean" title="Boolean">boolean</a> logical operator that performs short-circuiting inclusive logical disjunction on two expressions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <i>firstvalue</i> <a class="mw-selflink selflink">_ORELSE</a> <i>secondvalue</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>A logical operation is said to be short-circuiting if the compiled code can bypass the evaluation of one expression depending on the result of another expression.</li>
<li>If the result of the first expression evaluated determines the final result of the operation, there is no need to evaluate the second expression, because it cannot change the final result.</li>
<li>Short-circuiting can improve performance if the bypassed expression is complex, or if it involves procedure calls.</li>
<li>If either or both expressions evaluate to true, result is true.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="none"><img alt="none" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>none</b>
</p>
</div>
</div></li>
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.13.0"><img alt="v3.13.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.13.0</b>
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
<p><i>Example:</i> OR versus _ORELSE
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Trying _ORELSE"</span>
<span style="color:#919191;">' _ORELSE performs short-circuiting logical conjunction and hence for "strawberry", only isFruit() is called</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <span style="color:#55FF55;">isFruit</span>(<span style="color:#FFB100;">"strawberry"</span>) <a class="mw-selflink selflink"><span style="color:#4593D8;">_ORELSE</span></a> <span style="color:#55FF55;">isRed</span>(<span style="color:#FFB100;">"strawberry"</span>) <a class="mw-selflink selflink"><span style="color:#4593D8;">_ORELSE</span></a> <span style="color:#55FF55;">isSeasonal</span>(<span style="color:#FFB100;">"strawberry"</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Probably a strawberry."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Certainly not a strawberry."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Trying OR"</span>
<span style="color:#919191;">' OR does not performs short-circuiting logical conjunction and hence all is***() functions are called</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <span style="color:#55FF55;">isFruit</span>(<span style="color:#FFB100;">"strawberry"</span>) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <span style="color:#55FF55;">isRed</span>(<span style="color:#FFB100;">"strawberry"</span>) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <span style="color:#55FF55;">isSeasonal</span>(<span style="color:#FFB100;">"strawberry"</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Probably a strawberry."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Certainly not a strawberry."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">isFruit%%</span> (fruit <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"isFruit() called!"</span>
    <span style="color:#55FF55;">isFruit</span> = (fruit = <span style="color:#FFB100;">"strawberry"</span>)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">isRed%%</span> (fruit <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"isRed() called!"</span>
    <span style="color:#55FF55;">isRed</span> = (fruit = <span style="color:#FFB100;">"strawberry"</span>)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">isSeasonal%%</span> (fruit <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>)
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"isSeasonal() called!"</span>
    <span style="color:#55FF55;">isSeasonal</span> = (fruit = <span style="color:#FFB100;">"strawberry"</span>)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">Trying _ORELSE
isFruit() called!
Probably a strawberry.
Trying OR
isFruit() called!
isRed() called!
isSeasonal() called!
Probably a strawberry.
</pre>
</td></tr></tbody></table>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2661" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="BIT" title="BIT">_BIT</a>, <a href="%26B" title="&amp;B">&amp;B</a>, <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><a href="AND" title="AND">AND</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a>, <a href="OR" title="OR">OR</a></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a>, <a href="XOR_(boolean)" title="XOR (boolean)">XOR (boolean)</a>, <a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a></li>
<li><a href="ANDALSO" title="ANDALSO">_ANDALSO</a>, <a href="NEGATE" title="NEGATE">_NEGATE</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062621
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.047 seconds
Real time usage: 0.057 seconds
Preprocessor visited node count: 578/1000000
Post‐expand include size: 4556/2097152 bytes
Template argument size: 1419/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2880/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.191      1 -total
  6.88%    2.698     35 Template:Cl
  6.61%    2.590     32 Template:Text
  4.53%    1.775      1 Template:PageSyntax
  4.46%    1.748      3 Template:Parameter
  4.34%    1.701      1 Template:PageExamples
  4.14%    1.622      1 Template:CodeEnd
  4.08%    1.599      1 Template:PageAvailability
  3.88%    1.522      1 Template:OutputEnd
  3.80%    1.489      1 Template:PageNavigation
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1237-0!canonical and timestamp 20240715062621 and revision id 8940.
 -->
</div>
</div>
</div>
</div>
</body>
</html>