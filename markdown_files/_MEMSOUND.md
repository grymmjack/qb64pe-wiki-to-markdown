<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_MEMSOUND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-MEMSOUND rootpage-MEMSOUND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_MEMSOUND</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_MEMSOUND</b> function returns a <a href="MEM" title="MEM">_MEM</a> value referring to a sound's raw data in memory using a designated sound handle created by the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> or <a href="SNDNEW" title="SNDNEW">_SNDNEW</a> function.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><i>soundBlock</i> = <a class="mw-selflink selflink">_MEMSOUND</a>(<i>soundHandle&amp;</i>[, <i>channel&amp;</i>])</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>soundBlock</i> <a href="MEM" title="MEM">_MEM</a> type variable holds the read-only elements .OFFSET, .SIZE, .ELEMENTSIZE, .TYPE and .SOUND.
<ul><li><b>.OFFSET</b> is the starting memory address of the sound sample data.</li>
<li><b>.SIZE</b> is the size of the sample data in <b>bytes</b></li>
<li><b>.ELEMENTSIZE</b> will contain the number of <b>bytes-per-sample</b> the audio contains.
<ul><li>Can return 1 (8-bit mono), 2 (8-bit stereo), 2 (16-bit mono), 4 (16-bit stereo), 4 (32-bit mono) or 8 (32-bit stereo).</li>
<li>Use <b>.TYPE</b> to determine the data type of the sample data.</li></ul></li>
<li><b>.TYPE</b> will contain the data type of the sample data. See <a href="MEM" title="MEM">_MEM</a> for details.</li>
<li><b>.SOUND</b> will contain the same handle value as returned by the <a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a> function.</li></ul></li>
<li>The second parameter <i>channel&amp;</i> is optional and deprecated. This was used to specify the sound channel. In <b>QB64-PE v3.1.0</b> and above stereo data is always interleaved. You must use <b>.ELEMENTSIZE</b> and <b>.TYPE</b> to determine the type of audio data you are dealing with.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Use this function to obtain a pointer to the raw sound data in memory for direct access.</li>
<li>Even if the memory pointer obtained by this fuction was already freed again using <a href="MEMFREE" title="MEMFREE">_MEMFREE</a>, the respective Sound handle itself must still be freed using <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a> when no longer required.</li>
<li>If .SIZE returns 0, that means the data could not be accessed. It may happen if you try to access the right channel in a mono file or the format simply does not support accessing raw PCM samples.</li>
<li><i>channel&amp;</i> - 1 (left channel/mono) or 2 (right channel; for stereo files) was supported on the old OpenAL backend. For the new miniaudio backend, this must be 0.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Availability">Availability</span></h2>
<ul><li><b>QB64 v1.5 and up</b></li>
<li><b>QB64-PE all versions</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Checking that a sound file is stereo.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION_EXPLICIT" title="OPTION EXPLICIT"><span style="color:#4593D8;">OPTION _EXPLICIT</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Loading...";
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Song <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
Song = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>("onward_ride1.flac") ' Replace file name with your sound file
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Song &lt; 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Failed to load sound!"
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Done!"
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Channels <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>
Channels = SndChannels(Song)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Channels = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This file is STEREO"
<a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> Channels = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "This file is MONO"
<a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "An error occurred."
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> Song 'closing the sound releases the mem blocks
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
' This function returns the number of sound channels for a valid sound "handle"
' 2 = stereo, 1 = mono, 0 = error
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> SndChannels~%% (handle <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> SampleData <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
    SndChannels = 0 ' Assume failure
    ' Check if the sound is valid
    SampleData = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMSOUND</span></a>(handle, 0)
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.SIZE = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="EXIT_FUNCTION" title="EXIT FUNCTION"><span style="color:#4593D8;">EXIT FUNCTION</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    ' Check the data type and then decide if the sound is stereo or mono
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.TYPE = 260 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' 32-bit floating point
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.ELEMENTSIZE = 4 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 1
        <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.ELEMENTSIZE = 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 2
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = 132 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' 32-bit integer
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.ELEMENTSIZE = 4 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 1
        <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.ELEMENTSIZE = 8 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 2
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = 130 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' 16-bit integer
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.ELEMENTSIZE = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 1
        <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.ELEMENTSIZE = 4 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 2
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = 1153 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' 8-bit unsigned integer
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.ELEMENTSIZE = 1 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 1
        <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.ELEMENTSIZE = 2 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 2
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> ' This means this is an OpenAL sound handle
        <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> RightChannel <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>
        RightChannel = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMSOUND</span></a>(handle, 2)
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> RightChannel.SIZE &gt; 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            SndChannels = 2
        <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
            SndChannels = 1
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Plotting a sound's waves.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="DECLARE_LIBRARY" title="DECLARE LIBRARY"><span style="color:#4593D8;">DECLARE LIBRARY</span></a>
    <a href="$IF" title="$IF"><span style="color:#55FF55;">$IF</span></a> <span style="color:#F580B1;">32BIT</span> <a href="THEN" title="THEN"><span style="color:#55FF55;">THEN</span></a>
        <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">ConvertOffset~&amp;</span> <a href="ALIAS" title="ALIAS"><span style="color:#4593D8;">ALIAS</span></a> <span style="color:#FFB100;">"uintptr_t"</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> o <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>)
    <a class="mw-redirect" href="$ELSE" title="$ELSE"><span style="color:#55FF55;">$ELSE</span></a>
        <a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> <span style="color:#55FF55;">ConvertOffset~&amp;&amp;</span> <a href="ALIAS" title="ALIAS"><span style="color:#4593D8;">ALIAS</span></a> <span style="color:#FFB100;">"uintptr_t"</span> (<a class="mw-redirect" href="BYVAL" title="BYVAL"><span style="color:#4593D8;">BYVAL</span></a> o <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="OFFSET_(function)" title="OFFSET (function)"><span style="color:#4593D8;">_OFFSET</span></a>)
    <a class="mw-redirect" href="$END_IF" title="$END IF"><span style="color:#55FF55;">$END IF</span></a> 
<a class="mw-redirect" href="END_DECLARE" title="END DECLARE"><span style="color:#4593D8;">END DECLARE</span></a>
<a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <a href="NEWIMAGE" title="NEWIMAGE"><span style="color:#4593D8;">_NEWIMAGE</span></a>(<span style="color:#F580B1;">800</span>, <span style="color:#F580B1;">327</span>, <span style="color:#F580B1;">32</span>)
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Loading..."</span>;
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Song <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>: Song = <a href="SNDOPEN" title="SNDOPEN"><span style="color:#4593D8;">_SNDOPEN</span></a>(<span style="color:#FFB100;">"OPL3 Groove.rad"</span>) <span style="color:#919191;">' replace this with your (WAV, AIFF, AIFC, FLAC, OGG, MP3, MID, IT, XM, S3M, MOD, RAD, AHX, HVL, QOA) sound file</span>
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> Song &lt; <span style="color:#F580B1;">1</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Failed to load song!"</span>
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Done!"</span>
<a href="SNDPLAY" title="SNDPLAY"><span style="color:#4593D8;">_SNDPLAY</span></a> Song
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> SampleData <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="MEM" title="MEM"><span style="color:#4593D8;">_MEM</span></a>: SampleData = <a class="mw-selflink selflink"><span style="color:#4593D8;">_MEMSOUND</span></a>(Song, <span style="color:#F580B1;">0</span>)
<a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.SIZE = <span style="color:#F580B1;">0</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Failed to access sound sample data."</span>
    <a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> sz <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER64" title="INTEGER64"><span style="color:#4593D8;">_INTEGER64</span></a>: sz = <span style="color:#55FF55;">ConvertOffset</span>(SampleData.ELEMENTSIZE) <span style="color:#919191;">' sz is the total size of the sound in bytes</span>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> x <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, i <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="INTEGER64" title="INTEGER64"><span style="color:#4593D8;">_INTEGER64</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO UNTIL</span></a> <a href="KEYHIT" title="KEYHIT"><span style="color:#4593D8;">_KEYHIT</span></a> = <span style="color:#F580B1;">27</span> <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> <a href="NOT" title="NOT"><span style="color:#4593D8;">NOT</span></a> <a href="SNDPLAYING" title="SNDPLAYING"><span style="color:#4593D8;">_SNDPLAYING</span></a>(Song) <a href="OR_(boolean)" title="OR (boolean)"><span style="color:#4593D8;">OR</span></a> i + (<a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> * sz) &gt; SampleData.SIZE
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">1</span>, <span style="color:#F580B1;">1</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> i; <span style="color:#FFB100;">"/"</span>; SampleData.SIZE, <span style="color:#FFB100;">"Frame Size ="</span>; sz, <span style="color:#FFB100;">"Data Type ="</span>; SampleData.TYPE
    <a href="$CHECKING" title="$CHECKING"><span style="color:#55FF55;">$CHECKING</span></a>:<a href="OFF" title="OFF"><span style="color:#4593D8;">OFF</span></a>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> SampleData.TYPE = <span style="color:#F580B1;">130</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' 128 OR 2: integer stereo or mono</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> - <span style="color:#F580B1;">1</span>
            <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> si <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>: si = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(SampleData, SampleData.OFFSET + i + x * sz, <a href="INTEGER" title="INTEGER"><span style="color:#4593D8;">INTEGER</span></a>) <span style="color:#919191;">' get sound data</span>
            <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / <span style="color:#F580B1;">2</span>)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">300</span> * si / <span style="color:#F580B1;">32768</span>), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">111</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">'plot wave</span>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = <span style="color:#F580B1;">260</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' 256 OR 4: floating point stereo or mono</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> - <span style="color:#F580B1;">1</span>
            <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> sf <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: sf = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(SampleData, SampleData.OFFSET + i + x * sz, <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>) <span style="color:#919191;">' get sound data</span>
            <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / <span style="color:#F580B1;">2</span>)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(<span style="color:#F580B1;">0</span>, sf * <span style="color:#F580B1;">300</span>), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">111</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">'plot wave</span>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="ELSEIF" title="ELSEIF"><span style="color:#4593D8;">ELSEIF</span></a> SampleData.TYPE = <span style="color:#F580B1;">1153</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <span style="color:#919191;">' 128 OR 1 OR 1024: unsigned byte stereo or mono</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> x = <span style="color:#F580B1;">0</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <a href="WIDTH_(function)" title="WIDTH (function)"><span style="color:#4593D8;">_WIDTH</span></a> - <span style="color:#F580B1;">1</span>
            <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> sb <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>: sb = <a href="MEMGET_(function)" title="MEMGET (function)"><span style="color:#4593D8;">_MEMGET</span></a>(SampleData, SampleData.OFFSET + i + x * sz, <a href="UNSIGNED" title="UNSIGNED"><span style="color:#4593D8;">_UNSIGNED</span></a> <a href="BYTE" title="BYTE"><span style="color:#4593D8;">_BYTE</span></a>) <a class="mw-redirect" href="XOR" title="XOR"><span style="color:#4593D8;">XOR</span></a> <span style="color:#F580B1;">&amp;H80</span> <span style="color:#919191;">' get sound data and convert to signed</span>
            <a href="LINE" title="LINE"><span style="color:#4593D8;">LINE</span></a> (x, <a href="HEIGHT" title="HEIGHT"><span style="color:#4593D8;">_HEIGHT</span></a> / <span style="color:#F580B1;">2</span>)-<a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">300</span> * sb / <span style="color:#F580B1;">128</span>), <a href="RGB32" title="RGB32"><span style="color:#4593D8;">_RGB32</span></a>(<span style="color:#F580B1;">0</span>, <span style="color:#F580B1;">111</span>, <span style="color:#F580B1;">0</span>) <span style="color:#919191;">' plot wave</span>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="$CHECKING" title="$CHECKING"><span style="color:#55FF55;">$CHECKING</span></a>:<a href="ON" title="ON"><span style="color:#4593D8;">ON</span></a>
    <a href="DISPLAY" title="DISPLAY"><span style="color:#4593D8;">_DISPLAY</span></a>
    <a href="LIMIT" title="LIMIT"><span style="color:#4593D8;">_LIMIT</span></a> <span style="color:#F580B1;">60</span>
    i = <a href="FIX" title="FIX"><span style="color:#4593D8;">FIX</span></a>(<a href="SNDGETPOS" title="SNDGETPOS"><span style="color:#4593D8;">_SNDGETPOS</span></a>(Song) * <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>) * sz <span style="color:#919191;">' calculate the new sample frame position</span>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="SNDCLOSE" title="SNDCLOSE"><span style="color:#4593D8;">_SNDCLOSE</span></a> Song <span style="color:#919191;">' closing the sound releases the mem blocks</span>
<a href="AUTODISPLAY" title="AUTODISPLAY"><span style="color:#4593D8;">_AUTODISPLAY</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="MEM" title="MEM">_MEM</a>, <a href="MEMFREE" title="MEMFREE">_MEMFREE</a></li>
<li><a href="MEMPUT" title="MEMPUT">_MEMPUT</a>, <a href="MEMGET" title="MEMGET">_MEMGET</a>, <a href="MEMGET_(function)" title="MEMGET (function)">_MEMGET (function)</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a>, <a href="SNDNEW" title="SNDNEW">_SNDNEW</a>, <a href="SNDCLOSE" title="SNDCLOSE">_SNDCLOSE</a>, <a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li>
<li><a href="SNDRATE" title="SNDRATE">_SNDRATE</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715062404
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.133 seconds
Real time usage: 0.171 seconds
Preprocessor visited node count: 2006/1000000
Post‐expand include size: 14668/2097152 bytes
Template argument size: 3621/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 611/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   90.747      1 -total
 18.64%   16.915    196 Template:Cl
 10.21%    9.262     67 Template:Text
  5.35%    4.856      1 Template:PageParameters
  4.82%    4.377      6 Template:Parameter
  4.60%    4.174      1 Template:PageSyntax
  4.54%    4.117      1 Template:PageNavigation
  4.41%    3.998      6 Template:Cm
  3.75%    3.404      1 Template:PageSeeAlso
  3.74%    3.390      1 Template:PageDescription
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:830-0!canonical and timestamp 20240715062404 and revision id 8569.
 -->
</div>
</div>
</div>
</div>
</body>
</html>