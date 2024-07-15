<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDOPENRAW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDOPENRAW rootpage-SNDOPENRAW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDOPENRAW</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDOPENRAW</a> function opens a new channel to fill with _SNDRAW content to manage multiple dynamically generated sounds.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>pipeHandle&amp;</i> = <a class="mw-selflink selflink">_SNDOPENRAW</a></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>You can manage multiple dynamically generated sounds at once without having to worry about mixing.</li>
<li>Use <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a> to remove the pipe sound handles from memory.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Combining 2 sounds without worrying about mixing:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">a = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDOPENRAW</span></a>
b = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDOPENRAW</span></a>
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> x = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 100000
    <a href="SNDRAW" title="SNDRAW"><span style="color:#4593D8;">_SNDRAW</span></a> <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(x / 10), , a 'fill with a tone
    <a href="SNDRAW" title="SNDRAW"><span style="color:#4593D8;">_SNDRAW</span></a> <a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * 1 - 0.5, , b 'fill with static
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> a
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> b
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDRAWDONE" title="SNDRAWDONE">_SNDRAWDONE</a></li>
<li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li>
<li><a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062457
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.031 seconds
Real time usage: 0.053 seconds
Preprocessor visited node count: 107/1000000
Post‐expand include size: 1397/2097152 bytes
Template argument size: 171/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   30.094      1 -total
 14.29%    4.301      1 Template:CodeEnd
 13.51%    4.066      1 Template:Small
 10.90%    3.279      1 Template:PageSyntax
  9.12%    2.743     11 Template:Cl
  8.41%    2.530      1 Template:Parameter
  8.10%    2.437      1 Template:PageExamples
  7.85%    2.362      1 Template:PageDescription
  7.67%    2.308      1 Template:CodeStart
  7.29%    2.195      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:337-0!canonical and timestamp 20240715062457 and revision id 7960.
 -->
</div>
</div>
</div>
</div>
</body>
</html>