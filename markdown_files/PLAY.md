<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>PLAY - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-PLAY rootpage-PLAY skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">PLAY</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>PLAY</b> is a statement that plays notes of sound through the sound card in QB64 using a command <a href="STRING" title="STRING">STRING</a>.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">PLAY</a> <i>commandstring$</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>commandstring$</i> can be any literal or variable <a href="STRING" title="STRING">STRING</a> consisting of the following commands:
<ul><li>Command string values are not case sensitive and spacing is ignored. Use upper or lower case as desired.</li></ul></li></ul>
<dl><dd><ul><li><b>O</b>n - Sets the current octave (from 0 to 6). Example: <b><span style="color:green;">PLAY "O3"</span></b></li>
<li><b>&lt;</b> - Down one octave (cannot be below zero). Example: <b><span style="color:green;">PLAY "&lt;&lt;"</span></b> 'goes down two octaves.</li>
<li><b>&gt;</b> - Up one octave (cannot be above 6). Example: <b><span style="color:green;">PLAY "&gt;&gt;"</span></b> ' goes up two octaves.</li>
<li><b>A</b>, <b>B</b>, <b>C</b>, <b>D</b>, <b>E</b>, <b>F</b> or <b>G</b> are the notes in the current octave. Can use the following suffixes:</li></ul>
<dl><dd><ul><li><b>+</b> or <b>#</b> for a sharp note. Example: <b><span style="color:green;">PLAY "C#"</span></b></li>
<li><b>-</b> for a flat note. Example: <b><span style="color:green;">PLAY "C-"</span></b></li></ul></dd></dl>
<ul><li><b>N</b>n - Plays a note n by number(n can be between 0 to 84 in the 7 octaves, where 0 is a rest). Example: <b><span style="color:green;">PLAY "N42"</span></b></li>
<li><b>L</b>n - Sets length of a note (n can be 1 to 64 where 1 is a whole note and 4 is a quarter of a note etc.). Example: <b><span style="color:green;">PLAY "L4"</span></b></li></ul>
<dl><dd><ul><li><b>MS</b> - Each note plays 3/4 of length set by L (staccato)</li>
<li><b>MN</b> - Each note plays 7/8 of length set by L (normal)</li>
<li><b>ML</b> - Each note plays full length set by L (legato)</li>
<li><b>P</b>n - Specifies a pause (1 - 64). P1 is a whole-note pause, P2 is a half-note pause, etc.  (The pause is 1/n notes in length.) Example: <b><span style="color:green;">PLAY "P32"</span></b></li>
<li><b>T</b>n - Tempo sets number of L4 quarter notes per minute (n can be 32 to 255 where 120 is the default). Example: <b><span style="color:green;">PLAY "T180"</span></b></li></ul>
<dl><dd><ul><li><b> .  </b>  - period after a note plays 1½ times the note length determined by L * T.</li>
<li><b>.. </b>  - two periods plays 1-3/4 times the note length determined by L * T.</li></ul></dd></dl></dd></dl>
<ul><li><b>,  </b>  - <b>commas in QB64</b> stop play advancement to allow more than one note to be played simultaneously. Example: <b><span style="color:green;">PLAY "C,E,G,"</span></b></li>
<li><b>V</b>n - Volume in <b>QB64 only</b> can be any volume from 0 (none) to 100 (full).  The default level is 50 when <b>n</b> is not specified.</li>
<li><b>MF</b> - Play music in the foreground (each note must be completed before another can start).</li>
<li><b>MB</b> - Play music in the background while program code execution continues (QB64 has no note buffer limits).</li>
<li><b>X</b> <b>+</b> <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(string-expression) - executes a command string variable. <b>MUST be used with variables!</b>.</li>
<li><b>@</b>n - Select waveform in <b>QB64-PE only</b> can be (<b>1</b> for square waveform, <b>2</b> for sawtooth waveform, <b>3</b> for triangle waveform (default), <b>4</b> for sine waveform or <b>5</b> for white noise)</li>
<li><b>Q</b>n - Volume ramp in <b>QB64-PE only</b> can be any duration (ms) from 0 to 100.</li>
<li>Numeric values "n" listed above can also be fetched from numeric variables using <b>"="</b> + <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(numeric_variable).</li></ul></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul class="gallery mw-gallery-nolines">
<li class="gallerybox" style="width: 53px"><div style="width: 53px">
<div class="thumb" style="width: 48px;"><div style="margin:0px auto;"><a class="image" href="File:Qb64.png" title="v0.610"><img alt="v0.610" decoding="async" height="48" src="/qb64wiki/images/9/91/Qb64.png" width="48"/></a></div></div>
<div class="gallerytext">
<p><b>v0.610</b>
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
<ul><li>Complete <b>X</b> <b>+</b> <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(string-expression) support was added in <b>QB64-PE v3.8.0</b>. Earlier versions of QB64-PE and QB64 only had <b>=</b> + <a href="VARPTR$" title="VARPTR$">VARPTR$</a>(numeric_variable) support.</li>
<li>Support for <b>@</b>n and <b>Q</b>n was added in <b>QB64-PE v3.8.0</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Plays a sound with the volume and note varying from 0 to 50. Maximum note can only be 84.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"q0mll64"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">50</span>
        a$ = a$ + <span style="color:#FFB100;">"v"</span> + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(x)) + <span style="color:#FFB100;">"n"</span> + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(x))
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">50</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">1</span> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">-1</span>
        a$ = a$ + <span style="color:#FFB100;">"v"</span> + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(x)) + <span style="color:#FFB100;">"n"</span> + <a href="LTRIM$" title="LTRIM$"><span style="color:#4593D8;">LTRIM$</span></a>(<a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(x))
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> a$
    a$ = <span style="color:#FFB100;">""</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &lt;&gt; <span style="color:#FFB100;">""</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"v10l1c,l4egl2o5c,o4l4eg"</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Plays "Frosty the snowman". The lyric printing is not delayed by PLAY in QB64.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Frosty the Snow Man"</span>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> X = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">2</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Fros-ty the Snow man was a jolly happy soul,"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Fros-ty the Snow man knew the sun was hot that day"</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"t140o2p4g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g2."</span> <span style="color:#919191;">'MB removed to print song one line at a time</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"with a corn cob pipe and a button nose and two eyes made out of coal."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"so he said Let's run and we'll have some fun now before I melt away."</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4f4g2."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Fros-ty the Snow Man is a fair-y tale, they say,"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Down to the vil-lage, with a broom-stick in his hand,"</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g2."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"He was made of snow but the chil-dren knew how he come to life one day."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"run-ning here and there all a-round the square, say-in' catch me if you can."</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4d4c2."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"There must have been some magic in that old silk hat they found."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"He led them down the streets of town right to the traffic cop."</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"c4a4a4o3c4c4o2b4a4g4e4f4a4g4f4e2."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"For when they placed it on his head he be-gan to dance a round."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"And he on-ly paused a moment when he heard him hol-ler Stop!"</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"e8e8d4d4g4g4b4b4o3d4d8o2b8o3d4c4o2b4a4g4p4"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Oh, Fros-ty the Snow Man was a-live as he could be,"</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"For, Fros-ty the Snow Man had to hur-ry on his way"</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"g2g2e4.f8g4o3c2o2b8o3c8d4c4o2b4a8g8g2."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"and the chil-dren say he could laugh and play just the same as you and me."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> X = <span style="color:#F580B1;">2</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"but he waved good-bye say-in' Don't you cry, I'll be back a-gain some day."</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"o2b8o3c8d4c4o2b4a8a8g8o3c4o2e8e4g8a8g4f4e4d4c2.p4"</span>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> X
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Thump-et-y thump thump, thump-et-y thump thump, look at Fros-ty go."</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"t180g8g8g4g4g4a8g8g4g4g4a4g4e4g4d1"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Thump-et-y thump thump, thump-et-y thump thump, ov-er the hills of snow."</span>
<a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"t180g8g8g4g4g4a8g8g4g4g4g8g8g4a4b4o3c2c4p1"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Clicking on the grid enables various notes to be played simultaneously.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> grid(<span style="color:#F580B1;">16</span>, <span style="color:#F580B1;">16</span>), grid2(<span style="color:#F580B1;">16</span>, <span style="color:#F580B1;">16</span>), cur
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> maxx = <span style="color:#F580B1;">512</span>
<a href="CONST" title="CONST"><span style="color:#4593D8;">CONST</span></a> maxy = <span style="color:#F580B1;">512</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(maxx, maxy, <span style="color:#F580B1;">32</span>)
<a href="TITLE" title="TITLE"><span style="color:#4593D8;">_TITLE</span></a> <span style="color:#FFB100;">"MusicGrid"</span>
<span style="color:#55FF55;">cleargrid</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a> - t# &gt; <span style="color:#F580B1;">1</span> / <span style="color:#F580B1;">8</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> cur = (cur + <span style="color:#F580B1;">1</span>) <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <span style="color:#F580B1;">15</span>: t# = <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> cur &lt;&gt; oldcur <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <span style="color:#55FF55;">figuregrid</span>
        <span style="color:#55FF55;">drawgrid</span>
        <span style="color:#55FF55;">playgrid</span>
        oldcur = cur
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <span style="color:#55FF55;">domousestuff</span>
    in$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> in$ = <span style="color:#FFB100;">"C"</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> in$ = <span style="color:#FFB100;">"c"</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#55FF55;">cleargrid</span>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> in$ = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>)
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">drawgrid</span>
    scale! = maxx / <span style="color:#F580B1;">16</span>
    scale2 = maxx \ <span style="color:#F580B1;">16</span> - <span style="color:#F580B1;">2</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
        y1 = y * scale!
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
            x1 = x * scale!
            c&amp; = <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(grid2(x, y) * <span style="color:#F580B1;">64</span> + <span style="color:#F580B1;">64</span>, <span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">0</span>)
            <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x1, y1)-(x1 + scale2, y1 + scale2), c&amp;, BF
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">figuregrid</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
            grid2(x, y) = grid(x, y)
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">14</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">14</span>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(x, y) = <span style="color:#F580B1;">1</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> cur = x <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                grid2(x, y) = <span style="color:#F580B1;">2</span>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(x - <span style="color:#F580B1;">1</span>, y) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> grid2(x - <span style="color:#F580B1;">1</span>, y) = <span style="color:#F580B1;">1</span>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(x + <span style="color:#F580B1;">1</span>, y) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> grid2(x + <span style="color:#F580B1;">1</span>, y) = <span style="color:#F580B1;">1</span>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(x, y - <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> grid2(x, y - <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">1</span>
                <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(x, y + <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> grid2(x, y + <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">1</span>
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">domousestuff</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="MOUSEINPUT" title="MOUSEINPUT"><span style="color:#4593D8;">_MOUSEINPUT</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="MOUSEBUTTON" title="MOUSEBUTTON"><span style="color:#4593D8;">_MOUSEBUTTON</span></a>(<span style="color:#F580B1;">1</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            x = <a href="MOUSEX" title="MOUSEX"><span style="color:#4593D8;">_MOUSEX</span></a> \ (maxx \ <span style="color:#F580B1;">16</span>)
            y = <a href="MOUSEY" title="MOUSEY"><span style="color:#4593D8;">_MOUSEY</span></a> \ (maxy \ <span style="color:#F580B1;">16</span>)
            grid(x, y) = <span style="color:#F580B1;">1</span> - grid(x, y)
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">playgrid</span>
    n$ = <span style="color:#FFB100;">"L16 "</span>
    <span style="color:#919191;">'scale$ = "O1CO1DO1EO1FO1GO1AO1BO2CO2DO2EO2FO2GO2AO2BO3CO3D"</span>
    scale$ = <span style="color:#FFB100;">"o1fo1go1ao2co2do2fo2go2ao3co3do3fo3go3ao4co4do4fo"</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">15</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">0</span> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">-1</span>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> grid(cur, y) = <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            note$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(scale$, <span style="color:#F580B1;">1</span> + (<span style="color:#F580B1;">15</span> - y) * <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">3</span>)
            n$ = n$ + note$ + <span style="color:#FFB100;">","</span> <span style="color:#919191;">'comma plays 2 or more column notes simultaneously</span>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
    n$ = <a href="LEFT$" title="LEFT$"><span style="color:#4593D8;">LEFT$</span></a>(n$, <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(n$) - <span style="color:#F580B1;">1</span>)
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> n$
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">cleargrid</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> y = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">15</span>
            grid(x, y) = <span style="color:#F580B1;">0</span>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> x
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> y
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 4</dt>
<dd>Play strings starting with MB allow program code to run while music plays in background.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">' 2012, 2013 mennonite</span>
<span style="color:#919191;">' license: creative commons cc0 1.0 universal</span>
<span style="color:#919191;">' (public domain) http://creativecommons.org/publicdomain/zero/1.0/</span>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">12</span> <span style="color:#919191;">' the following works in other screen modes, too</span>
<a href="RANDOMIZE" title="RANDOMIZE"><span style="color:#4593D8;">RANDOMIZE</span></a> <a href="TIMER_(function)" title="TIMER (function)"><span style="color:#4593D8;">TIMER</span></a>
<a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"mb l4cf.l8el4fag.l8fl4gl8agl4f.l8fl4a&gt;cl2dl4dl4c.&lt;l8al4afg.l8fl4gl8agl4f.l8dl4dcl2f&gt;l4dc.&lt;l8al4afg.l8fl4g&gt;dc.&lt;l8al4a&gt;cl2dl4dc.&lt;l8al4afg.l8fl4gl8agl4f.l8dl4dcl1f"</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> ccs(<span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">9</span>, <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">2</span>)
ccs(<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">415</span>: ccs(<span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">289</span>
ccs(<span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">185</span>: ccs(<span style="color:#F580B1;">2</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">128</span>
ccs(<span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">108</span>: ccs(<span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">75</span>
ccs(<span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">70</span>: ccs(<span style="color:#F580B1;">4</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">48</span>
ccs(<span style="color:#F580B1;">5</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">48</span>: ccs(<span style="color:#F580B1;">5</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">32</span>
ccs(<span style="color:#F580B1;">6</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">32</span>: ccs(<span style="color:#F580B1;">6</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">20</span>
ccs(<span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">20</span>: ccs(<span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">12</span>
ccs(<span style="color:#F580B1;">8</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">10</span>: ccs(<span style="color:#F580B1;">8</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">6</span>
ccs(<span style="color:#F580B1;">9</span>, <span style="color:#F580B1;">1</span>) = <span style="color:#F580B1;">2</span>: ccs(<span style="color:#F580B1;">9</span>, <span style="color:#F580B1;">2</span>) = <span style="color:#F580B1;">2</span>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> extra = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">23</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> p = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">9</span>
        <span style="color:#55FF55;">gcolor</span> <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(<a href="RND" title="RND"><span style="color:#4593D8;">RND</span></a> * <span style="color:#F580B1;">9</span> + <span style="color:#F580B1;">14</span> - <span style="color:#F580B1;">9</span>)
        <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">.04</span>
        <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
        <span style="color:#55FF55;">gscale</span> p
        row = ccs(p, <span style="color:#F580B1;">1</span>)
        cl = ccs(p, <span style="color:#F580B1;">2</span>)
        <span style="color:#55FF55;">glocate</span> row, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"000000000000000000000000000000000000000000000000000000000000000000000"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">1</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"0x00x0xxxx0xxxx0xxxx0x0x000x00x0xxxx0x000x000x0x0xxxx0xxxx0xxxx000x00"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">2</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"0x00x0x00x0x00x0x00x0x0x000xx0x0x0000x000x000x0x0x0000x00x0x00x000x00"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">3</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"0xxxx0xxxx0xxxx0xxxx0x0x000x0xx0xxx00x0x0x000x0x0xxx00xxxx0xxxx000x00"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">4</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"0x00x0x00x0x0000x00000x0000x00x0x0000x0x0x0000x00x0000x00x0x0x0000000"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">5</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"0x00x0x00x0x0000x00000x0000x00x0xxxx0xx0xx0000x00xxxx0x00x0x00x000x00"</span>
        <span style="color:#55FF55;">glocate</span> row + <span style="color:#F580B1;">6</span>, cl
        <span style="color:#55FF55;">gprint</span> <span style="color:#FFB100;">"000000000000000000000000000000000000000000000000000000000000000000000"</span>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> p
    <a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">1</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">27</span>) <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_FOR" title="EXIT FOR"><span style="color:#4593D8;">EXIT FOR</span></a>
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> extra
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">gscale</span> (s):
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gscalep
    gscalep = <a href="INT" title="INT"><span style="color:#4593D8;">INT</span></a>(s)
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">gcolor</span> (c):
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gcolorp
    gcolorp = c
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">gbackcolor</span> (c):
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gbackcolorp
    gbackcolorp = c
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">glocate</span> (row, column):
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gposxp
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gposyp
    gposyp = row
    gposxp = column
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">gprint</span> (p$):
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gscalep
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gposxp, gposyp
    <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> gcolorp, gbackcolorp
    <span style="color:#919191;">' # means "use the foreground color here."</span>
    <span style="color:#919191;">' . means "use the background color here."</span>
    <span style="color:#919191;">' _ means "transparent - don't draw this block at all" (you can layer!)</span>
    <span style="color:#919191;">' 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f means "do color attribute 0 to 15."</span>
    <span style="color:#919191;">' any letter after f: "use the foreground color here."</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> gscalep &lt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> gscalep = <span style="color:#F580B1;">1</span>
    pcolorp = gcolorp
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> p = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(p$):
        <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> <a href="LCASE$" title="LCASE$"><span style="color:#4593D8;">LCASE$</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(p$, p, <span style="color:#F580B1;">1</span>))
            <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"#"</span>, <span style="color:#FFB100;">"g"</span>, <span style="color:#FFB100;">"h"</span>, <span style="color:#FFB100;">"i"</span>, <span style="color:#FFB100;">"j"</span>, <span style="color:#FFB100;">"k"</span>, <span style="color:#FFB100;">"l"</span>, <span style="color:#FFB100;">"m"</span>, <span style="color:#FFB100;">"n"</span>, <span style="color:#FFB100;">"o"</span>, <span style="color:#FFB100;">"p"</span>, <span style="color:#FFB100;">"q"</span>, <span style="color:#FFB100;">"r"</span>, <span style="color:#FFB100;">"s"</span>, <span style="color:#FFB100;">"t"</span>, <span style="color:#FFB100;">"u"</span>, <span style="color:#FFB100;">"v"</span>, <span style="color:#FFB100;">"w"</span>, <span style="color:#FFB100;">"x"</span>, <span style="color:#FFB100;">"y"</span>, <span style="color:#FFB100;">"z"</span>
                pcolorp = gcolorp
            <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"."</span>
                pcolorp = gbackcolorp
            <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"_"</span>
                pcolorp = <span style="color:#F580B1;">-1</span>
            <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#FFB100;">"0"</span>, <span style="color:#FFB100;">"1"</span>, <span style="color:#FFB100;">"2"</span>, <span style="color:#FFB100;">"3"</span>, <span style="color:#FFB100;">"4"</span>, <span style="color:#FFB100;">"5"</span>, <span style="color:#FFB100;">"6"</span>, <span style="color:#FFB100;">"7"</span>, <span style="color:#FFB100;">"8"</span>, <span style="color:#FFB100;">"9"</span>, <span style="color:#FFB100;">"a"</span>, <span style="color:#FFB100;">"b"</span>, <span style="color:#FFB100;">"c"</span>, <span style="color:#FFB100;">"d"</span>, <span style="color:#FFB100;">"e"</span>, <span style="color:#FFB100;">"f"</span>
                pcolorp = <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(<span style="color:#FFB100;">"0123456789abcdef"</span>, <a href="LCASE$" title="LCASE$"><span style="color:#4593D8;">LCASE$</span></a>(<a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(p$, p, <span style="color:#F580B1;">1</span>))) - <span style="color:#F580B1;">1</span>
        <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> pcolorp = <span style="color:#F580B1;">-1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> gscalep &gt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
                <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> ((gposxp - <span style="color:#F580B1;">1</span>) * gscalep, (gposyp - <span style="color:#F580B1;">1</span>) * gscalep)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(gscalep - <span style="color:#F580B1;">1</span>, gscalep - <span style="color:#F580B1;">1</span>), pcolorp, BF
            <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>:
                <a href="PSET" title="PSET"><span style="color:#4593D8;">PSET</span></a> (gposxp, gposyp), pcolorp
            <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
        <span style="color:#55FF55;">glocate</span> gposyp, gposxp + <span style="color:#F580B1;">1</span>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> p
    gposxp = <span style="color:#F580B1;">1</span>
    <span style="color:#55FF55;">glocate</span> gposyp + <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span> <span style="color:#919191;">'gposyp = gposyp + 1</span>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 5</dt>
<dd>This example uses <a href="PRINT" title="PRINT">PRINT</a> to good effect as string spacing is ignored by <b>PLAY</b>.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="WIDTH" title="WIDTH"><span style="color:#4593D8;">WIDTH</span></a> <span style="color:#F580B1;">59</span>, <span style="color:#F580B1;">28</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
x$ = x$ + <span style="color:#FFB100;">"   o3    l4         t         0120c    ml&lt;f1   ,a      1,  "</span>
x$ = x$ + <span style="color:#FFB100;">"   &gt;c    1,        mnf        .e  8f   am  l&lt;   e1    ,g   "</span>
x$ = x$ + <span style="color:#FFB100;">"   1,    &gt;c       1, mn       g.   f8  ga   8g   8m  l&lt;    "</span>
x$ = x$ + <span style="color:#FFB100;">"   f2.,a2.,      &gt;c   2.      ,m  nf   .f  8a     ml&lt;f     "</span>
x$ = x$ + <span style="color:#FFB100;">"   ,a,&gt;c,mn     &gt;cd2.,&lt;f2     .,d2     .,&lt;b        -2      "</span>
x$ = x$ + <span style="color:#FFB100;">"   .m    lb    -,&gt;d,f,mn&gt;d    ml       &lt;c          1,      "</span>
x$ = x$ + <span style="color:#FFB100;">"   &lt;a    1,   f1         ,m   n&gt;       &gt;c          .&lt;      "</span>
x$ = x$ + <span style="color:#FFB100;">"   a8    af  ml           c1  ,&lt;       e1          ,g      "</span>
x$ = x$ + <span style="color:#FFB100;">"                                                           "</span>
x$ = x$ + <span style="color:#FFB100;">"      1,m      n&gt;  g.f8ga8g8m  l&lt;                   f1     "</span>
x$ = x$ + <span style="color:#FFB100;">"      ,d1,     &lt;b  -1           ,m                 n&gt;      "</span>
x$ = x$ + <span style="color:#FFB100;">"      &gt;f .d    8d  c&lt;            f2               .,       "</span>
x$ = x$ + <span style="color:#FFB100;">"      a2  .,   c2  .,&gt;f2.         ml      &lt;      b-        "</span>
x$ = x$ + <span style="color:#FFB100;">"      ,&gt;   d,  f,  mn&gt;dml          &lt;c    1,&lt;    a1         "</span>
x$ = x$ + <span style="color:#FFB100;">"      ,f    1, mn  &gt;&gt;               c.  &lt;a 8a  fm          "</span>
x$ = x$ + <span style="color:#FFB100;">"      lc     2.,&lt;  e2                .,g2   .,mn           "</span>
x$ = x$ + <span style="color:#FFB100;">"      &gt;g      .f8  gml&lt;b-,&gt;d,         f,     mn            "</span>
x$ = x$ + <span style="color:#FFB100;">"                                                           "</span>
x$ = x$ + <span style="color:#FFB100;">"&gt;d      ml  &lt;&lt;f2.,a2.,         &gt;         c2.,m       n&gt;  c."</span>
x$ = x$ + <span style="color:#FFB100;">" &lt;a    8a   ml                &lt;e,        g,  &gt;c      ,m  n&gt;"</span>
x$ = x$ + <span style="color:#FFB100;">"  cm  l&lt;    &lt;b               -2 .,       &gt;d   2.     ,f  2."</span>
x$ = x$ + <span style="color:#FFB100;">"   ,mn&gt;     d2.ml&lt;          &lt;b   -,      &gt;d  ,f      ,m  n&gt;"</span>
x$ = x$ + <span style="color:#FFB100;">"    dm      l&lt;&lt;f1,         a1,&gt;c1,mn     &gt;c.&lt;a       8a  fm"</span>
x$ = x$ + <span style="color:#FFB100;">"    lc      1,            &lt;e1,g1,mn&gt;g    .f  8g      a8  g8"</span>
x$ = x$ + <span style="color:#FFB100;">"    ml      &lt;&lt;           b-         1,   &gt;d   1,           "</span>
x$ = x$ + <span style="color:#FFB100;">"    f1      ,mn&gt;f.d8dc  l1           ml  f,    c,    &lt;a  ,f"</span>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> x$;
<a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> x$
</pre>
</td></tr></tbody></table>
<dl><dt>Example 6</dt>
<dd>Demonstrates usage of <a href="VARPTR$" title="VARPTR$">VARPTR$</a> with <b>PLAY</b>.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><span style="color:#919191;">'Play scale in 7 different octaves</span>
scale$ = <span style="color:#FFB100;">"CDEFGAB"</span>
play$ = <span style="color:#FFB100;">"L16O="</span> + <a href="VARPTR$" title="VARPTR$"><span style="color:#4593D8;">VARPTR$</span></a>(i%) + <span style="color:#FFB100;">"X"</span> + <a href="VARPTR$" title="VARPTR$"><span style="color:#4593D8;">VARPTR$</span></a>(scale$)
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">6</span>
    <a class="mw-selflink selflink"><span style="color:#4593D8;">PLAY</span></a> play$
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PLAY_(function)" title="PLAY (function)">PLAY (function)</a></li>
<li><a href="SOUND" title="SOUND">SOUND</a>, <a href="DRAW" title="DRAW">DRAW</a></li>
<li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061356
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.173 seconds
Real time usage: 0.200 seconds
Preprocessor visited node count: 4863/1000000
Post‐expand include size: 32980/2097152 bytes
Template argument size: 10063/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 7385/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  108.983      1 -total
 16.70%   18.196    366 Template:Text
 10.22%   11.136    260 Template:Cl
  6.67%    7.267      1 Template:PageAvailability
  4.65%    5.068      1 Template:PageParameters
  4.23%    4.613      2 Template:Parameter
  3.71%    4.045      1 Template:PageSyntax
  2.00%    2.185      6 Template:CodeEnd
  1.96%    2.135      1 Template:PageExamples
  1.96%    2.133      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:511-0!canonical and timestamp 20240715061356 and revision id 8783.
 -->
</div>
</div>
</div>
</div>
</body>
</html>