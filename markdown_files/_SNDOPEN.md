<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDOPEN - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDOPEN rootpage-SNDOPEN skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDOPEN</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDOPEN</a> function loads a sound file into memory and returns a <a href="LONG" title="LONG">LONG</a> handle value above 0.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>soundHandle&amp;</i> = <a class="mw-selflink selflink">_SNDOPEN</a>(<i>fileName$</i>[, <i>capabilities$</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Returns a <a href="LONG" title="LONG">LONG</a> <i>soundHandle&amp;</i> value to the sound file in memory. <b>A value of zero means the sound could not be loaded.</b></li>
<li>The literal or variable <a href="STRING" title="STRING">STRING</a> sound <i>fileName$</i> can be <b>WAV, AIFF, AIFC, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD, RAD (v1 &amp; v2), AHX, HVL &amp; QOA</b> file types.
<ul><li><b>MID</b> support is enabled via the <a href="$MIDISOUNDFONT" title="$MIDISOUNDFONT">$MIDISOUNDFONT</a> metacommand.</li></ul></li>
<li>The literal or variable <a href="STRING" title="STRING">STRING</a> <i>capabilities$</i> is optional but can be one of the following. Anything else is ignored. Multiple capability strings can be specified separated by a comma.
<ul><li><b>STREAM</b>: This will "stream" the sound into memory rather than fully decoding it.</li>
<li><b>MEMORY</b>: This will treat <i>fileName$</i> as a memory buffer containing the sound file instead of a file name.</li></ul></li>
<li>Short sounds should not be loaded using <b>STREAM</b>. Use <b>STREAM</b> when you want to play long sounds as background music and want to avoid loading delays.</li>
<li><a href="MEMSOUND" title="MEMSOUND">_MEMSOUND</a> will not work for sounds loaded using <b>STREAM</b> or <b>MEMORY</b>.</li>
<li><b>Always check the handle value returned is greater than zero before attempting to play the sound.</b></li>
<li>The handle can be used by most of the _SND sound playing functions and statements in QB64 except <a href="SNDPLAYFILE" title="SNDPLAYFILE">_SNDPLAYFILE</a> which plays a sound file directly from the disk and does not use a handle value.</li>
<li>Handles can be closed with <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a> when the sound is no longer necessary.</li>
<li>If a WAV sound file won't play, try it using the Windows <a href="Windows_Libraries#Play_WAV_Sounds" title="Windows Libraries">Play WAV sounds library</a> to check it or convert the sound file to FLAC, OGG or MP3.</li></ul>
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
<ul><li>Available for <i>Linux</i> since <b>QB64 v0.800</b> and for <i>macOS</i> since <b>QB64 v0.900</b></li>
<li>Until <b>QB64 v0.954</b> various formats and capabilities are supported via the SDL audio backend.
<ul><li>See the historic page <a href="SNDOPEN-v0.954" title="SNDOPEN-v0.954">_SNDOPEN-v0.954</a> for reference.</li></ul></li>
<li>In <b>QB64 v0.960</b> the underlying SDL library was exchanged by OpenGL (graphics) and OpenAL (sound) and as a result only the WAV, OGG, and MP3 formats are supported until today's current versions without any special capabilities.
<ul><li>See historic page <a href="SNDOPEN-v0.960" title="SNDOPEN-v0.960">_SNDOPEN-v0.960</a> for reference.</li>
<li>This limitation also applies up to <b>QB64-PE v3.0.0</b> of the Phoenix Edition.</li></ul></li>
<li>Since <b>QB64-PE v3.1.0</b> the new formats FLAC, MOD, S3M, XM, IT and RAD were added to that very limited list, in the move away from OpenAL to the Miniaudio library in combination with separate and extensible player libraries.
<ul><li>In this version also the new capability to STREAM the sound was added.</li></ul></li>
<li>With <b>QB64-PE v3.2.0</b> the MID format was added, but needs explicitly to be enabled via the <a href="$MIDISOUNDFONT" title="$MIDISOUNDFONT">$MIDISOUNDFONT</a> metacommand.</li>
<li>In <b>QB64-PE v3.5.0</b> the Amiga AHX and HVL formats were added to the list.
<ul><li>In this version also the new capability to load sounds from MEMORY was added.</li></ul></li>
<li>In <b>QB64-PE v3.8.0</b> support for Apple's AIFF and AIFC formats was added.</li>
<li>In <b>QB64-PE v3.9.0</b> support for Quite OK Audio (QOA) format was added.</li>
<li>In <b>QB64-PE v3.9.0</b> the old OpenAL audio backend was finally removed.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Snippet 1:</i> Loading a sound file to use in the program later. Only load it once and use the handle any time you want.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">h&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDOPEN</span></a>("dog.wav")
IF h&amp; &lt;= 0 THEN BEEP ELSE <a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> h&amp;      'check for valid handle before using!
</pre>
</td></tr></tbody></table>
<p>
<i>Snippet 2:</i> Playing a sound from 2 different speakers based on program results.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">' This examples load, plays and then bounces the sound between the left and right channels
Laff&amp; = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDOPEN</span></a>("KONGlaff.ogg", "stream") 'load sound file and get LONG handle value
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Laff&amp; &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> Laff&amp; 'play sound
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Failed to load sound file."
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a> <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Press ESC to stop."
dir = 0.01
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> laffx! &lt;= -1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = 0.01
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> laffx! &gt;= 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = -0.01
    laffx! = laffx! + dir
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> , 1: <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> "Balance = ##.##"; laffx!;
    <a href="SNDBAL" title="SNDBAL"><span style="color:#4593D8;">_SNDBAL</span></a> Laff&amp;, laffx! 'balance sound to left or right speaker
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> 60
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(Laff&amp;) <a href="AND" title="AND"><span style="color:#4593D8;">AND</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> &lt;&gt; 27
</pre>
</td></tr></tbody></table>
<p>
<i>Snippet 3:</i> Loading a sound file from memory and then playing it.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT"><span style="color:#4593D8;">OPTION _EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> buffer <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>: buffer = LoadSlidingAwayData
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Size ="; <a href="LEN" title="LEN"><span style="color:#4593D8;">LEN</span></a>(buffer)
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> h <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: h = <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDOPEN</span></a>(buffer, "memory")
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Handle ="; h
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Length ="; <a href="SNDLEN" title="SNDLEN"><span style="color:#4593D8;">_SNDLEN</span></a>(h)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Looping audio..."
<a href="SNDLOOP" title="SNDLOOP"><span style="color:#4593D8;">_SNDLOOP</span></a> h
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
' This function reads the file directly from data and then returns the decompressed data
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> LoadSlidingAwayData$
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a> numL, numb, stroffs, i, dat
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> rawdata <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
    <a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Sliding_Away
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> numL, numb
    rawdata = <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>((numL * 4) + numb)
    stroffs = 1
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> numL
        <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> dat
        <a href="MID$" title="MID$"><span style="color:#4593D8;">MID$</span></a>(rawdata, stroffs, 4) = <a href="MKL$" title="MKL$"><span style="color:#4593D8;">MKL$</span></a>(dat)
        stroffs = stroffs + 4
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> numb &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = 1 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> numb
            <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> dat
            <a href="MID$" title="MID$"><span style="color:#4593D8;">MID$</span></a>(rawdata, stroffs, 1) = <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(dat)
            stroffs = stroffs + 1
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    LoadSlidingAwayData = <a href="INFLATE$" title="INFLATE$"><span style="color:#4593D8;">_INFLATE$</span></a>(rawdata)
    '--- DATAs representing the contents of file sliding_away.hvl
    '---------------------------------------------------------------------
    Sliding_Away:
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> 192,10
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H56A59C78,&amp;H51134F5B,&amp;H7766FE10,&amp;HE96D0B6B,&amp;HC5258202,&amp;H5BAED8BA,&amp;H840A956B,&amp;HFBB240F8
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H3E2483E0,&amp;H4B3E24A0,&amp;H018928C4,&amp;H6217892F,&amp;H9F813FA2,&amp;H47E14FC0,&amp;H3D1356F1,&amp;HED9D9EB7
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H9A78DA05,&amp;HFB3399CE,&amp;HCCE677CD,&amp;HB3CE6ECC,&amp;H7451CF57,&amp;HDF05877E,&amp;H02F0F2DF,&amp;H0F297204
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HA39E8435,&amp;HF47BD182,&amp;H9ED67297,&amp;H95727A62,&amp;HC2AD1C62,&amp;HF6E174BD,&amp;HFC52E2CC,&amp;HCDF31E7B
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H8C1BFE31,&amp;H0530CF3F,&amp;HFC639FC6,&amp;H767F8C33,&amp;H3E117F0C,&amp;H12FE196E,&amp;HFC3551E6,&amp;HC5602C65
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H88B0E660,&amp;H622FE19A,&amp;HBF86AB19,&amp;H6DB89B82,&amp;H42588BF8,&amp;HFF9CEADD,&amp;HFE69F88E,&amp;HFE8E0AA2
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HB4151E28,&amp;HB77813DB,&amp;HC0F00F98,&amp;HB1D0D7E2,&amp;H6878BBF8,&amp;HB23C0DF1,&amp;H2DD626F8,&amp;HE2D7443E
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HC5B1E1EF,&amp;HF8B0D847,&amp;H35213616,&amp;H7DC6DF37,&amp;HBF4CA16C,&amp;H51D38F90,&amp;H988C1126,&amp;H6396662B
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H92BEE941,&amp;H82D4AECA,&amp;HAE19975A,&amp;H84D3803F,&amp;H78C59C84,&amp;H2FDA3819,&amp;H91FEB274,&amp;HBD99B759
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H696D74A3,&amp;H9EC47B19,&amp;HD31127F3,&amp;H7BFBB907,&amp;H55F2AF36,&amp;H07F1906A,&amp;H48D709CE,&amp;H28535583
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H14E43B7B,&amp;H26A6E166,&amp;HC5B6BE73,&amp;H9987436B,&amp;H4B9F9E0D,&amp;H711ECA4F,&amp;H1F8A569A,&amp;H4C4C7F8E
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HD687B61D,&amp;H169A5E4D,&amp;H2C214CDF,&amp;H606A9A4F,&amp;H39E3E02F,&amp;H19D3C0E2,&amp;HBB2BA06B,&amp;H44260BBA
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H36837A77,&amp;HD7E5755B,&amp;H8B6D5EB2,&amp;HE2BD64E8,&amp;H5DAFD7B6,&amp;H511EC46B,&amp;H28D99976,&amp;HB2229E54
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H119E361B,&amp;H7F0D34A1,&amp;H3F556E80,&amp;H54E38DA8,&amp;HB2C43EA2,&amp;H4A6A18AA,&amp;H6D68D8AE,&amp;HDD4B1A0F
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HB08FCF44,&amp;H9F93723A,&amp;H9BF305C9,&amp;H0940B334,&amp;H77655317,&amp;HCFA7E047,&amp;H1FABC0EE,&amp;HB2C99E6B
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H6938C69D,&amp;HD2B70456,&amp;H3A4AA7FE,&amp;H9A5571BE,&amp;H72E75DE4,&amp;HC6436D54,&amp;H63C88D17,&amp;H3B1E4C6B
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H7D6DAFC6,&amp;H2D781D78,&amp;H551D6B43,&amp;H6D631693,&amp;H0CA258D9,&amp;HC2AD8353,&amp;HDBED2EA1,&amp;HE7D494D6
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HDB5D33AA,&amp;HD774C635,&amp;HB7B60E08,&amp;HEA3C14D4,&amp;HAE70F1F7,&amp;H15274254,&amp;H20DB7E57,&amp;HDF3624DB
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HD967DE36,&amp;H34FB694A,&amp;H5CF3EAD5,&amp;H3714A95D,&amp;HDFB4B55D,&amp;H8E1B15F5,&amp;HD4C09FBB,&amp;HB2E5593E
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HAE7965FB,&amp;H1C50DEAF,&amp;H4AADD413,&amp;HCCF2D114,&amp;H3C053CBE,&amp;H2131FA2A,&amp;HA86FB8EF,&amp;H8B5EE49A
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H8E4EC59B,&amp;H4A212712,&amp;HE24DEF20,&amp;H5CD1131F,&amp;H8F7D3BC9,&amp;HBACE8D52,&amp;H48140715,&amp;HF214BADF
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H2F5717E5,&amp;HF0A5E631,&amp;H5148A8A5,&amp;HF4DD4296,&amp;HDD4AEDD4,&amp;HA3C4BD17,&amp;HB991EF24,&amp;H2C4E0200
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HE1EE4B6F,&amp;H5A527069,&amp;H07B674FC,&amp;HDA9EC13F,&amp;H70AF9D0A,&amp;HA12937B6,&amp;H196D4427,&amp;H8BD50886
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;H3422259D,&amp;HE5FA7FC8,&amp;HD1E1D1C3,&amp;HE0E0BBF1,&amp;H7C0FC1DB,&amp;HE4F9FB7F,&amp;H760F5838,&amp;H63EEEE5F
    <a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> &amp;HA3,&amp;HDB,&amp;HDD,&amp;H16,&amp;HF8,&amp;H7F,&amp;HEE,&amp;H68,&amp;H18,&amp;HB9
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a>, <a href="SNDPLAY" title="SNDPLAY">_SNDPLAY</a>, <a href="SNDSTOP" title="SNDSTOP">_SNDSTOP</a></li>
<li><a href="SNDPAUSE" title="SNDPAUSE">_SNDPAUSE</a>, <a href="SNDLOOP" title="SNDLOOP">_SNDLOOP</a>, <a href="SNDLIMIT" title="SNDLIMIT">_SNDLIMIT</a></li>
<li><a href="SNDSETPOS" title="SNDSETPOS">_SNDSETPOS</a>, <a href="SNDGETPOS" title="SNDGETPOS">_SNDGETPOS</a></li>
<li><a href="SNDPLAYING" title="SNDPLAYING">_SNDPLAYING</a>, <a href="SNDPAUSED" title="SNDPAUSED">_SNDPAUSED</a></li>
<li><a href="SNDCOPY" title="SNDCOPY">_SNDCOPY</a>, <a href="SNDPLAYCOPY" title="SNDPLAYCOPY">_SNDPLAYCOPY</a></li>
<li><a href="SNDBAL" title="SNDBAL">_SNDBAL</a>, <a href="SNDLEN" title="SNDLEN">_SNDLEN</a>, <a href="SNDVOL" title="SNDVOL">_SNDVOL</a></li>
<li><a href="SNDPLAYFILE" title="SNDPLAYFILE">_SNDPLAYFILE</a></li>
<li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a>, <a href="SNDRATE" title="SNDRATE">_SNDRATE</a>, <a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192902
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.083 seconds
Real time usage: 0.126 seconds
Preprocessor visited node count: 731/1000000
Post‐expand include size: 5713/2097152 bytes
Template argument size: 963/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 2365/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   80.098      1 -total
  9.94%    7.959     95 Template:Cl
  5.41%    4.335      1 Template:PageExamples
  4.87%    3.898      1 Template:PageSeeAlso
  4.76%    3.815      3 Template:CodeStart
  4.46%    3.570      3 Template:CodeEnd
  3.95%    3.163      1 Template:PageAvailability
  3.91%    3.135      1 Template:PageNavigation
  3.74%    2.996      7 Template:Parameter
  3.59%    2.872      1 Template:PageSyntax
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:336-0!canonical and timestamp 20240714192902 and revision id 8900.
 -->
</div>
</div>
</div>
</div>
</body>
</html>