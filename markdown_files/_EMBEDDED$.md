<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_EMBEDDED$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-EMBEDDED rootpage-EMBEDDED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_EMBEDDED$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_EMBEDDED$</b> function is used to recall the data of a file which was earlier embedded into the EXE file using the <a href="$EMBED" title="$EMBED">$EMBED</a> metacommand. You can roughly compare this to a <a href="RESTORE" title="RESTORE">RESTORE</a> to any <a href="DATA" title="DATA">DATA</a> block and then using <a href="READ" title="READ">READ</a> to retrieve the data.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>filedata$</i> = <a class="mw-selflink selflink">_EMBEDDED$</a>("<i>handle</i>")</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<dl><dt>IMPORTANT</dt>
<dd>
<ul><li>The parameter <i>handle</i> must be given as a <span style="color:red;">single literal string</span> enclosed in quotes, variables cannot be used here.</li>
<li>Your inputs are checked while typing to ensure its validity, warnings (if any) will be displayed immediately in the IDE status area.</li></ul></dd></dl>
<ul><li>The <i>filedata$</i> will receive the embedded file data as a single contiguous string, just as you would regularly <a href="OPEN" title="OPEN">OPEN</a> the file and read its entire contents into that string.</li>
<li>The <i>handle</i> is a unique case sensitive identifier beginning with a letter and only containing lower/upper case letters and/or numbers. It must exactly match the <i>handle</i> value used to <a href="$EMBED" title="$EMBED">$EMBED</a> the respective file.
<ul><li>You can compare this identifier to the line label in front of a <a href="DATA" title="DATA">DATA</a> block, which is later used in a <a href="RESTORE" title="RESTORE">RESTORE</a> call to set the <a href="READ" title="READ">READ</a> pointer to exactly that <a href="DATA" title="DATA">DATA</a> block.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All embedded files can be recalled individually by using its respective <i>handle</i> identifier.
<ul><li>If required, decompression is done internally, hence you always get back the original file contents.</li></ul></li>
<li>Recalling a file multiple times is possible, but in regard for the needed decompression time considered inefficient. Rather recall the file once and store the result in a <a href="STRING" title="STRING">STRING</a> variable, if you know you need it multiple times in your program.</li>
<li>To easily embed a file into your compiled EXE file use the <a href="$EMBED" title="$EMBED">$EMBED</a> metacommand.</li>
<li>Embedding files can be useful to deliver a program inclusive all required assets in just one EXE file.</li>
<li>No more worries whether a user installs your program correctly and retains the required folder structure.</li>
<li>If required, you can easily write the files back to disk using the <a href="WRITEFILE" title="WRITEFILE">_WRITEFILE</a> command, i.e. you could create your own simple installer or package manager.</li>
<li>Embedded images, sounds or fonts can be passed directly to <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="LOADFONT" title="LOADFONT">_LOADFONT</a> respectively when using the <i>memory load</i> capabilities of these functions.</li></ul>
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
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qbpe.png" title="v3.10.0"><img alt="v3.10.0" decoding="async" height="48" src="/qb64wiki/images/0/07/Qbpe.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v3.10.0</b>
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
<dd>Embeds two image files into the compiled EXE, then memory loads and displays it.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="$EMBED" title="$EMBED"><span style="color:#55FF55;">$EMBED</span></a>:<span style="color:#919191;">'source\peLogo.png','bigImg'</span>
<a href="$EMBED" title="$EMBED"><span style="color:#55FF55;">$EMBED</span></a>:<span style="color:#919191;">'source\qb64pe.png','smallImg'</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
bi&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_EMBEDDED$</span></a>(<span style="color:#FFB100;">"bigImg"</span>), <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>)
si&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<a class="mw-selflink selflink"><span style="color:#4593D8;">_EMBEDDED$</span></a>(<span style="color:#FFB100;">"smallImg"</span>), <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>)
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">140</span>, <span style="color:#F580B1;">180</span>), bi&amp;
<a href="PUTIMAGE" title="PUTIMAGE"><span style="color:#4593D8;">_PUTIMAGE</span></a> (<span style="color:#F580B1;">410</span>, <span style="color:#F580B1;">230</span>), si&amp;
<a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> si&amp;
<a href="FREEIMAGE" title="FREEIMAGE"><span style="color:#4593D8;">_FREEIMAGE</span></a> bi&amp;
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=2740" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="$EMBED" title="$EMBED">$EMBED</a></li>
<li><a href="DATA" title="DATA">DATA</a>, <a href="RESTORE" title="RESTORE">RESTORE</a>, <a href="READ" title="READ">READ</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062609
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.078 seconds
Preprocessor visited node count: 289/1000000
Post‐expand include size: 2516/2097152 bytes
Template argument size: 640/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2463/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   52.046      1 -total
 10.39%    5.409      1 Template:PageSyntax
  5.43%    2.827     16 Template:Text
  5.35%    2.784      7 Template:Parameter
  4.84%    2.521      1 Template:PageExamples
  4.56%    2.372     11 Template:Cl
  3.97%    2.068      2 Template:Cm
  3.93%    2.046      1 Template:CodeStart
  3.90%    2.030      1 Template:CodeEnd
  3.69%    1.920      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1222-0!canonical and timestamp 20240715062609 and revision id 9019.
 -->
</div>
</div>
</div>
</div>
</body>
</html>