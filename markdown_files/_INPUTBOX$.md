<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_INPUTBOX$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-INPUTBOX rootpage-INPUTBOX skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_INPUTBOX$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_INPUTBOX$</b> function displays a prompt in a dialog box, waits for the user to input text or click a button, and returns a string containing the contents of the text box.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>result$</i> = <a class="mw-selflink selflink">_INPUTBOX$</a>([<i>title$</i>][, <i>message$</i>][, <i>defaultInput$</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>title$</i> is an optional dialog box title.</li>
<li><i>message$</i> is an optional message or prompt that will be displayed in the dialog box.</li>
<li><i>defaultInput$</i> is an optional string that is displayed in the text box as the default response if no other input is provided.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use <i>message$</i> to specify instructions to the user.</li>
<li>All parameters are optional, hence omitting <i>defaultInput$</i> will display a empty text box.
<ul><li>However, if <i>defaultInput$</i> is provided, but is an empty string (<b>""</b>), then a password box is shown, and the text input will be masked.</li></ul></li>
<li>The <i>result$</i> may be an empty string (<b>""</b>), if the user simply cancelled the dialog.</li>
<li>The dialog box automatically becomes a modal window, if the application window is visible.</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.4.0"><img alt="v3.4.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.4.0</b>
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
<dl><dt>Example 1</dt>
<dd>Hello world, with common dialogs.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">username$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_INPUTBOX$</span></a>(<span style="color:#FFB100;">"Hello App"</span>, <span style="color:#FFB100;">"Enter your name:"</span>, <span style="color:#FFB100;">"anonymous"</span>)
<a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> <span style="color:#FFB100;">"Hello App"</span>, <span style="color:#FFB100;">"Hello "</span> + username$, <span style="color:#FFB100;">"info"</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Checking whether the user cancelled the input dialog.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">age$ = <a href="TRIM$" title="TRIM$"><span style="color:#4593D8;">_TRIM$</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_INPUTBOX$</span></a>(, <span style="color:#FFB100;">"Enter your age:"</span>))
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(age$) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> , <span style="color:#FFB100;">"Cancelled."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> , <span style="color:#FFB100;">"Age = "</span> + age$
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Getting passwords.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">password$ = <a class="mw-selflink selflink"><span style="color:#4593D8;">_INPUTBOX$</span></a>(<span style="color:#FFB100;">"Login"</span>, <span style="color:#FFB100;">"Enter password:"</span>, <span style="color:#FFB100;">""</span>)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(password$) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> , <span style="color:#FFB100;">"Cancelled."</span>
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="MESSAGEBOX" title="MESSAGEBOX"><span style="color:#4593D8;">_MESSAGEBOX</span></a> , <span style="color:#FFB100;">"You entered = "</span> + password$
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MESSAGEBOX" title="MESSAGEBOX">_MESSAGEBOX</a>, <a href="MESSAGEBOX_(function)" title="MESSAGEBOX (function)">_MESSAGEBOX (function)</a></li>
<li><a href="NOTIFYPOPUP" title="NOTIFYPOPUP">_NOTIFYPOPUP</a>, <a href="COLORCHOOSERDIALOG" title="COLORCHOOSERDIALOG">_COLORCHOOSERDIALOG</a></li>
<li><a href="SELECTFOLDERDIALOG$" title="SELECTFOLDERDIALOG$">_SELECTFOLDERDIALOG$</a>, <a href="OPENFILEDIALOG$" title="OPENFILEDIALOG$">_OPENFILEDIALOG$</a>, <a href="SAVEFILEDIALOG$" title="SAVEFILEDIALOG$">_SAVEFILEDIALOG$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062613
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.052 seconds
Real time usage: 0.067 seconds
Preprocessor visited node count: 372/1000000
Post‐expand include size: 3103/2097152 bytes
Template argument size: 950/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2524/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   49.015      1 -total
  6.03%    2.954      1 Template:PageExamples
  5.26%    2.577     19 Template:Cl
  5.21%    2.552     16 Template:Text
  5.08%    2.488      1 Template:PageSyntax
  4.89%    2.394     11 Template:Parameter
  4.18%    2.048      1 Template:PageAvailability
  4.08%    2.000      1 Template:PageSeeAlso
  4.07%    1.997      1 Template:PageDescription
  4.02%    1.970      1 Template:PageParameters
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1165-0!canonical and timestamp 20240715062613 and revision id 8602.
 -->
</div>
</div>
</div>
</div>
</body>
</html>