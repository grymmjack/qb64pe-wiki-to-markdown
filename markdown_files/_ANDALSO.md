<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_ANDALSO - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-ANDALSO rootpage-ANDALSO skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_ANDALSO</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_ANDALSO</a> is a <a href="Boolean" title="Boolean">boolean</a> logical operator that performs short-circuiting logical conjunction on two expressions.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result</i> = <i>firstvalue</i> <a class="mw-selflink selflink">_ANDALSO</a> <i>secondvalue</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>A logical operation is said to be short-circuiting if the compiled code can bypass the evaluation of one expression depending on the result of another expression.</li>
<li>If the result of the first expression evaluated determines the final result of the operation, there is no need to evaluate the second expression, because it cannot change the final result.</li>
<li>Short-circuiting can improve performance if the bypassed expression is complex, or if it involves procedure calls.</li>
<li>If both expressions evaluate to true, result is true.</li></ul>
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
<p><i>Example:</i> AND versus _ANDALSO
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> index, values(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">10</span>), v
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> index = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">10</span>
    values(index) = <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">255</span>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> index
<span style="color:#919191;">' value of index is now &gt; 10</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Trying _ANDALSO"</span>
<span style="color:#919191;">' _ANDALSO performs short-circuiting logical conjunction and hence the GetArrayValue check is completely bypassed</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> index &gt;= <span style="color:#F580B1;">1</span> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ANDALSO</span></a> index &lt;= <span style="color:#F580B1;">10</span> <a class="mw-selflink selflink"><span style="color:#4593D8;">_ANDALSO</span></a> <span style="color:#55FF55;">GetArrayValue</span>(values(), index, v) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_ANDALSO: Value ="</span>; v
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"_ANDALSO: Outside range."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Trying AND"</span>
<span style="color:#919191;">' AND does not performs short-circuiting logical conjunction and hence QB64-PE will throw a runtime error: Subscript out of range</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> index &gt;= <span style="color:#F580B1;">1</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> index &lt;= <span style="color:#F580B1;">10</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <span style="color:#55FF55;">GetArrayValue</span>(values(), index, v) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"AND: Value ="</span>; v
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"AND: Outside range."</span>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">GetArrayValue%%</span> (arr() <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, idx <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, value <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    value = arr(idx)
    <span style="color:#55FF55;">GetArrayValue</span> = <span style="color:#F580B1;">-1</span> <span style="color:#919191;">' return true</span>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2658" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="BIT" title="BIT">_BIT</a>, <a href="%26B" title="&amp;B">&amp;B</a>, <a href="BYTE" title="BYTE">_BYTE</a></li>
<li><a href="AND" title="AND">AND</a>, <a class="mw-redirect" href="XOR" title="XOR">XOR</a>, <a href="OR" title="OR">OR</a></li>
<li><a href="AND_(boolean)" title="AND (boolean)">AND (boolean)</a>, <a href="XOR_(boolean)" title="XOR (boolean)">XOR (boolean)</a>, <a href="OR_(boolean)" title="OR (boolean)">OR (boolean)</a></li>
<li><a href="ORELSE" title="ORELSE">_ORELSE</a>, <a href="NEGATE" title="NEGATE">_NEGATE</a></li>
<li><a href="Binary" title="Binary">Binary</a>, <a href="Boolean" title="Boolean">Boolean</a></li>
<li><a href="Mathematical_Operations" title="Mathematical Operations">Mathematical Operations</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062620
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.050 seconds
Real time usage: 0.060 seconds
Preprocessor visited node count: 494/1000000
Post‐expand include size: 3807/2097152 bytes
Template argument size: 932/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2766/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   39.817      1 -total
  8.12%    3.234     36 Template:Cl
  7.42%    2.956     24 Template:Text
  6.34%    2.524      1 Template:CodeEnd
  5.27%    2.099      1 Template:PageNavigation
  5.13%    2.043      1 Template:PageSeeAlso
  4.90%    1.952      1 Template:PageExamples
  4.68%    1.865      3 Template:Parameter
  4.58%    1.822      1 Template:PageSyntax
  3.88%    1.547      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1236-0!canonical and timestamp 20240715062620 and revision id 8939.
 -->
</div>
</div>
</div>
</div>
</body>
</html>