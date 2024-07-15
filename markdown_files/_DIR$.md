<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_DIR$ - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-DIR rootpage-DIR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_DIR$</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_DIR$</b> function returns common paths such as Documents, Pictures, Music, Desktop, etc.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>d$</i> = <a class="mw-selflink selflink">_DIR$</a>("<i>folderspecification</i>")</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>folderspecification</i> may be "desktop", "downloads", "documents", "music", "video", "pictures", "appdata", "common program data", "local data", "program files", "program files (x86)", "temp", "home", "fonts", "user fonts".</li>
<li>Some variation is accepted for the folder specification:</li></ul>
<dl><dd><dl><dd>MY DOCUMENTS, TEXT, DOCUMENT, DOCUMENTS, DOWNLOAD, DOWNLOADS</dd>
<dd>MY MUSIC, MUSIC, AUDIO, SOUND, SOUNDS</dd>
<dd>MY PICTURES, PICTURE, PICTURES, IMAGE, IMAGES, PHOTO, PHOTOS, DCIM, CAMERA, CAMERA ROLL</dd>
<dd>MY VIDEOS, VIDEO, VIDEOS, MOVIE, MOVIES,</dd>
<dd>DATA, APPDATA, APPLICATION DATA, PROGRAM DATA, LOCAL DATA, LOCALAPPDATA, LOCAL APPLICATION DATA, LOCAL PROGRAM DATA</dd>
<dd>PROGRAMFILES, PROGRAMFILESX86, PROGRAMFILES X86, PROGRAM FILES X86, PROGRAM FILES 86, PROGRAMFILES (X86), PROGRAM FILES(X86), PROGRAMFILES(X86)</dd>
<dd>FONT, USERFONT, USERFONTS, USER FONT</dd>
<dd>USER, PROFILE, USERPROFILE, USER PROFILE</dd></dl></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The path returned ends with a backslash on Windows and a forward-slash on Linux and macOS.</li>
<li>A nonexistent folder specification usually defaults to the Desktop folder path.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v1.1"><img alt="v1.1" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v1.1</b>
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
<ul><li>In <b>QB64-PE v3.11.0</b> support for "font" &amp; "user font" and full Linux and macOS support was added.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example</dt>
<dd>Displaying default paths in Windows.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"DESKTOP="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"desktop"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"DOWNLOADS="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"download"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"DOCUMENTS="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"my documents"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"PICTURES="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"pictures"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"MUSIC="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"music"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"VIDEO="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"video"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"APPLICATION DATA="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"data"</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"LOCAL APPLICATION DATA="</span> + <a class="mw-selflink selflink"><span style="color:#4593D8;">_DIR$</span></a>(<span style="color:#FFB100;">"local application data"</span>)
</pre>
</td></tr></tbody></table>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="outputcrt0">DESKTOP=C:\Documents and Settings\Administrator\Desktop\
DOWNLOADS=C:\Documents and Settings\Administrator\Downloads\
DOCUMENTS=C:\Documents and Settings\Administrator\My Documents\
PICTURES=C:\Documents and Settings\Administrator\My Documents\My Pictures\
MUSIC=C:\Documents and Settings\Administrator\My Documents\My Music\
VIDEO=C:\Documents and Settings\Administrator\My Documents\My Videos\
APPLICATION DATA=C:\Documents and Settings\Administrator\Application Data\
LOCAL APPLICATION DATA=C:\Documents and Settings\Administrator\Local Settings\Application Data\
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="CWD$" title="CWD$">_CWD$</a></li>
<li><a href="STARTDIR$" title="STARTDIR$">_STARTDIR$</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192707
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.061 seconds
Real time usage: 0.088 seconds
Preprocessor visited node count: 320/1000000
Post‐expand include size: 2766/2097152 bytes
Template argument size: 837/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2551/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   69.104      1 -total
  7.64%    5.282      1 Template:PageSeeAlso
  4.58%    3.163      1 Template:PageExamples
  4.04%    2.793     16 Template:Text
  3.84%    2.657     16 Template:Cl
  3.73%    2.580      1 Template:CodeEnd
  3.40%    2.352      1 Template:OutputStart
  3.22%    2.222      1 Template:PageSyntax
  3.20%    2.208      1 Template:PageNavigation
  3.11%    2.148      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:121-0!canonical and timestamp 20240714192707 and revision id 8624.
 -->
</div>
</div>
</div>
</div>
</body>
</html>