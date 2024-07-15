<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_CLIP - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-CLIP rootpage-CLIP skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_CLIP</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_CLIP</a> option is used in a QB64 graphics <a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> to allow placement of an image partially off of the screen.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT</a> PSET|AND|OR|PRESET}][, <i>omitcolor</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>_CLIP should be placed immediately before the PUT action if used. XOR is default when not used.</li>
<li>The offscreen portions of the image will be the omit color.</li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET</a> can get portions of the images off screen in <b>QB64</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example:</i> Placing an image partially or fully offscreen.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> mypic(<span style="color:#F580B1;">500</span>)
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
<a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
<a href="CIRCLE" title="CIRCLE"><span style="color:#4593D8;">CIRCLE</span></a> (<span style="color:#F580B1;">10</span>, <span style="color:#F580B1;">10</span>), <span style="color:#F580B1;">10</span>
<a href="GET_(general)" title="GET (general)"><span style="color:#4593D8;">GET</span></a> (<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)-(<span style="color:#F580B1;">20</span>, <span style="color:#F580B1;">20</span>), mypic(<span style="color:#F580B1;">0</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"This program puts an image off screen."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Select which option you'd like to try."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"1 will produce an illegal function call."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"1 is putting without _CLIP."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"2 is putting with _CLIP PSET."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"3 is putting with _CLIP XOR."</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"4 is putting with _CLIP PSET, 4."</span>
<a href="INPUT" title="INPUT"><span style="color:#4593D8;">INPUT</span></a> sel
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> sel = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PUT_(general)" title="PUT (general)"><span style="color:#4593D8;">PUT</span></a> (<span style="color:#F580B1;">-10</span>, <span style="color:#F580B1;">10</span>), mypic(<span style="color:#F580B1;">0</span>), <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> <span style="color:#919191;">' this causes an illegal function call</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> sel = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PUT_(general)" title="PUT (general)"><span style="color:#4593D8;">PUT</span></a> (<span style="color:#F580B1;">-10</span>, <span style="color:#F580B1;">10</span>), mypic(<span style="color:#F580B1;">0</span>), <a class="mw-selflink selflink"><span style="color:#4593D8;">_CLIP</span></a> <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> <span style="color:#919191;">' allows graphic to be drawn off-screen</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> sel = <span style="color:#F580B1;">3</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PUT_(general)" title="PUT (general)"><span style="color:#4593D8;">PUT</span></a> (<span style="color:#F580B1;">-10</span>, <span style="color:#F580B1;">10</span>), mypic(<span style="color:#F580B1;">0</span>), <a class="mw-selflink selflink"><span style="color:#4593D8;">_CLIP</span></a> <span style="color:#919191;">' uses the default PUT XOR operation</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> sel = <span style="color:#F580B1;">4</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PUT_(general)" title="PUT (general)"><span style="color:#4593D8;">PUT</span></a> (<span style="color:#F580B1;">-10</span>, <span style="color:#F580B1;">10</span>), mypic(<span style="color:#F580B1;">0</span>), <a class="mw-selflink selflink"><span style="color:#4593D8;">_CLIP</span></a> <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a>, <span style="color:#F580B1;">4</span> <span style="color:#919191;">' doesn't draw red pixels</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PUT_(graphics_statement)" title="PUT (graphics statement)">PUT (graphics statement)</a></li>
<li><a href="GET_(graphics_statement)" title="GET (graphics statement)">GET (graphics statement)</a></li>
<li><a href="STEP" title="STEP">STEP</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192639
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.033 seconds
Real time usage: 0.041 seconds
Preprocessor visited node count: 556/1000000
Post‐expand include size: 4105/2097152 bytes
Template argument size: 1029/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 384/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   23.186      1 -total
 12.50%    2.899     38 Template:Text
 12.00%    2.782     32 Template:Cl
  8.62%    1.998      1 Template:PageSyntax
  8.60%    1.994      1 Template:CodeEnd
  7.60%    1.762      3 Template:Parameter
  7.27%    1.685      1 Template:PageDescription
  7.13%    1.653      1 Template:PageSeeAlso
  7.07%    1.640      1 Template:PageNavigation
  7.00%    1.622      1 Template:PageExamples
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:87-0!canonical and timestamp 20240714192639 and revision id 8280.
 -->
</div>
</div>
</div>
</div>
</body>
</html>