<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>$EMBED - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-_EMBED rootpage-_EMBED skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">$EMBED</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>$EMBED</b> metacommand can embed any designated file (e.g. images, sounds, fonts and all other file types) into the compiled EXE file. You can roughly compare this to converting and placing a file's contents into <a href="DATA" title="DATA">DATA</a> lines, but <b>$EMBED</b> obviously is much more convenient.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">$EMBED</a><b>:</b>'<i>filename</i>'<b>,</b>'<i>handle</i>'</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<dl><dt>IMPORTANT</dt>
<dd>
<ul><li>Both parameters must be enclosed in single quotes and given as <span style="color:red;">literal strings</span>, variables cannot be used here.</li>
<li>Your inputs are checked while typing to ensure its validity, warnings (if any) will be displayed immediately in the IDE status area.</li></ul></dd></dl>
<ul><li>The <i>filename</i> is the name of the file to embed, if required inclusive a full or relative path.</li>
<li>The <i>handle</i> is a unique case sensitive identifier beginning with a letter and only containing lower/upper case letters and/or numbers, it's used later in the <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a> call to recall the embedded data.
<ul><li>You can compare this identifier to the line label in front of a <a href="DATA" title="DATA">DATA</a> block, which is later used in a <a href="RESTORE" title="RESTORE">RESTORE</a> call to set the <a href="READ" title="READ">READ</a> pointer to exactly that <a href="DATA" title="DATA">DATA</a> block.</li></ul></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>All files will be embedded in a compressed form, if a 20% least ratio is reached.
<ul><li>This low ratio was chosen, cause it will be reached by most files, except those which are already highly compressed such as PNG, JPG, MP3/4, ZIP, 7z etc. and are not worth the additional effort for just a few bytes less.</li></ul></li>
<li>To recall the embedded file data use the <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a> call with the very same <i>handle</i> identifier which was used in the respective file's <b>$EMBED</b> line. That call also does the decompression, if required.</li>
<li>Embedding files can be useful to deliver a program inclusive all required assets in just one EXE file.</li>
<li>No more worries whether a user installs your program correctly and retains the required folder structure.</li>
<li>If required, you can easily write the files back to disk using the <a href="WRITEFILE" title="WRITEFILE">_WRITEFILE</a> command, i.e. you could create your own simple installer or package manager.</li>
<li>Embedded images, sounds or fonts can be passed directly to <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="LOADFONT" title="LOADFONT">_LOADFONT</a> respectively when using the <i>memory load</i> capabilities of these functions.</li>
<li>The <b>$EMBED</b> metacommand can be used everywhere in a program. You may even place it inside pre-compiler <a href="$IF" title="$IF">$IF</a>..<a class="mw-redirect" href="$ELSE" title="$ELSE">$ELSE</a>...<a class="mw-redirect" href="$END_IF" title="$END IF">$END IF</a> blocks and only the files designated in the true block are embedded then.</li>
<li>How many or how big files you can embed depends on your system achitecture (x86/x64) as well as your installed memory. However, it should work just fine for all the normally expected working cases like embedding a font, a spritesheet and some level graphics as well a couple sound effects.</li>
<li>To avoid useless bloat of the compiled EXE file, the embedding process is smart enough to only embed those files, which are recalled by the <a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a> call at least once. I.e. you may <b>$EMBED</b> a dozen files, but if you recall only one of it in your program, then only that one file will be really embedded, while the other files are simply ignored.</li></ul>
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
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#55FF55;">$EMBED</span></a>:<span style="color:#919191;">'source\peLogo.png','bigImg'</span>
<a class="mw-selflink selflink"><span style="color:#55FF55;">$EMBED</span></a>:<span style="color:#919191;">'source\qb64pe.png','smallImg'</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">640</span>, <span style="color:#F580B1;">480</span>, <span style="color:#F580B1;">32</span>)
bi&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<a href="EMBEDDED$" title="EMBEDDED$"><span style="color:#4593D8;">_EMBEDDED$</span></a>(<span style="color:#FFB100;">"bigImg"</span>), <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>)
si&amp; = <a href="LOADIMAGE" title="LOADIMAGE"><span style="color:#4593D8;">_LOADIMAGE</span></a>(<a href="EMBEDDED$" title="EMBEDDED$"><span style="color:#4593D8;">_EMBEDDED$</span></a>(<span style="color:#FFB100;">"smallImg"</span>), <span style="color:#F580B1;">32</span>, <span style="color:#FFB100;">"memory"</span>)
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
<li><a href="EMBEDDED$" title="EMBEDDED$">_EMBEDDED$</a></li>
<li><a href="DATA" title="DATA">DATA</a>, <a href="RESTORE" title="RESTORE">RESTORE</a>, <a href="READ" title="READ">READ</a></li>
<li><a href="LOADFONT" title="LOADFONT">_LOADFONT</a>, <a href="LOADIMAGE" title="LOADIMAGE">_LOADIMAGE</a>, <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714214351
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.081 seconds
Real time usage: 0.110 seconds
Preprocessor visited node count: 280/1000000
Post‐expand include size: 2488/2097152 bytes
Template argument size: 620/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2463/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   83.898      1 -total
  6.17%    5.178     16 Template:Text
  4.13%    3.462      2 Template:Cm
  3.93%    3.297      1 Template:PageSyntax
  3.52%    2.950      1 Template:PageExamples
  3.30%    2.765     11 Template:Cl
  2.74%    2.303      5 Template:Parameter
  2.73%    2.294      1 Template:CodeStart
  2.71%    2.273      1 Template:CodeEnd
  2.57%    2.157      1 Template:Small
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:1221-0!canonical and timestamp 20240714214351 and revision id 9018.
 -->
</div>
</div>
</div>
</div>
</body>
</html>