<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>SOUND - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SOUND rootpage-SOUND skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">SOUND</span></h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><b>SOUND</b> sets frequency and duration of sounds from the internal PC speaker if the computer has one or the sound card in QB64.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">SOUND</a> <i>frequency#</i>, <i>duration#</i>[, <i>volume#</i>][, <i>panning#</i>][, <i>waveform&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li><i>frequency#</i> is any literal or variable value from 37 to 32767, but 0 is allowed for delays.
<ul><li>Just like QuickBASIC 4.5 frequencies on or above 20000 produces silence.</li></ul></li>
<li><i>duration#</i> is any literal or variable number of <a href="TIMER_(function)" title="TIMER (function)">TIMER</a> ticks with a duration of 1/18th second. 18 = one second.</li>
<li>Optional parameter <i>volume#</i> should be between 0.0 (muted) to 1.0 (full volume).</li>
<li>Optional parameter <i>panning#</i> should be between -1.0 (hard left) to 1.0 (hard right). 0.0 being center.</li>
<li>Optional parameter <i>waveform&amp;</i> can be one of the following:
<ul><li><b>1</b> for square waveform</li>
<li><b>2</b> for sawtooth waveform</li>
<li><b>3</b> for triangle waveform (default)</li>
<li><b>4</b> for sine waveform</li>
<li><b>5</b> for white noise</li></ul></li>
<li>More waveform types may be introduced in the future.</li>
<li><a href="PLAY" title="PLAY">PLAY</a> can be used for musical sounds.</li></ul>
<dl><dt>Note</dt>
<dd>The last volume, panning and waveform settings will apply to subsequent calls to <b>SOUND</b> (when used without the optional parameters) and <a href="PLAY" title="PLAY">PLAY</a>.</dd></dl>
<h3><span class="mw-headline" id="Errors">Errors</span></h3>
<ul><li>Low <i>frequency#</i> values between 0 and 37 will create an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function call error</a>.</li>
<li>Out of range values for <i>volume#</i>, <i>panning#</i> and <i>waveform&amp;</i> will create an <a href="ERROR_Codes" title="ERROR Codes">Illegal Function call error</a>.</li>
<li>All audio related statements and functions work even if the program is not in focus. However, depending on the operating system and environment, this may not always be the case.</li>
<li><b>SOUND</b> may have clicks or pauses between the sounds generated.</li></ul>
<dl><dt>Note</dt>
<dd><b>SOUND</b> 0, 0 will not stop previous <b>QB64</b> sounds like it did in QBasic!</dd></dl>
<p>
</p>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">        <b>                     The Seven Music Octaves </b>
        <b> Note     Frequency      Note     Frequency      Note      Frequency</b>
       <b>1</b>* D#1 ...... 39           G3 ....... 196          A#5 ...... 932
          E1 ....... 41           G#3 ...... 208          B5 ....... 988
          F1 ....... 44           A3 ....... 220       <b>6</b>* C6 ....... 1047
          F#1 ...... 46           A#3 ...... 233          C#6 ...... 1109
          G1 ....... 49           B3 ....... 247          D6 ....... 1175
          G#1 ...... 51        <b>4</b>* C4 ....... 262          D#6 ...... 1245
          A1 ....... 55           C#4 ...... 277          E6 ....... 1318
          A#1 ...... 58           D4 ....... 294          F6 ....... 1397
          B1 ....... 62           D#4 ...... 311          F#6 ...... 1480
       <b>2</b>* C2 ....... 65           E4 ....... 330          G6 ....... 1568
          C#2 ...... 69           F4 ....... 349          G# ....... 1661
          D2 ....... 73           F#4 ...... 370          A6 ....... 1760
          D#2 ...... 78           G4 ....... 392          A#6 ...... 1865
          E2 ....... 82           G#4 ...... 415          B6 ....... 1976
          F2 ....... 87           A4 ....... 440       <b>7</b>* C7 ....... 2093
          F#2 ...... 92           A# ....... 466          C#7 ...... 2217
          G2 ....... 98           B4 ....... 494          D7 ....... 2349
          G#2 ...... 104       <b>5</b>* C5 ....... 523          D#7 ...... 2489
          A2 ....... 110          C#5 ...... 554          E7 ....... 2637
          A#2 ...... 117          D5 ....... 587          F7 ....... 2794
          B2 ....... 123          D#5 ...... 622          F#7 ...... 2960
       <b>3</b>* C3 ....... 131          E5 ....... 659          G7 ....... 3136
          C#3 ...... 139          F5 ....... 698          G#7 ...... 3322
          D3 ....... 147          F#5 ...... 740          A7 ....... 3520
          D#3 ...... 156          G5 ....... 784          A#7 ...... 3729
          E3 ....... 165          G#5 ...... 831          B7 ....... 3951
          F3 ....... 175          A5 ....... 880       <b>8</b>* C8 ....... 4186
          F#3 ...... 185
                                 <b># denotes sharp</b>
</pre>
</td></tr></tbody></table>
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
<ul><li>Support for <i>volume#</i>, <i>panning#</i>, <i>waveform&amp;</i> was added in <b>QB64-PE v3.8.0</b>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<dl><dt>Example 1</dt>
<dd>Playing the seven octaves based on the base note DATA * 2 ^ (octave - 1).</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">notes$ = <span style="color:#FFB100;">"C C#D D#E F F#G G#A A#B "</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">9</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">5</span>, <span style="color:#F580B1;">20</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Select an octave (1 - 7) to play (8 quits):"</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: octa$ = <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a>
        <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> octa$ &lt;&gt; <span style="color:#FFB100;">""</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(octa$) &gt; <span style="color:#F580B1;">48</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> <a href="ASC_(function)" title="ASC (function)"><span style="color:#4593D8;">ASC</span></a>(octa$) &lt; <span style="color:#F580B1;">58</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> octave% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(octa$): <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
        <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> octave% &gt; <span style="color:#F580B1;">7</span>
    <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> octave% &gt; <span style="color:#F580B1;">0</span> <a href="AND_(boolean)" title="AND (boolean)"><span style="color:#4593D8;">AND</span></a> octave% &lt; <span style="color:#F580B1;">8</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a>
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">15</span>, <span style="color:#F580B1;">6</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">70</span>)
        <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">16</span>, <span style="color:#F580B1;">6</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="SPACE$" title="SPACE$"><span style="color:#4593D8;">SPACE$</span></a>(<span style="color:#F580B1;">70</span>)
        <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">15</span>, <span style="color:#F580B1;">6</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Octave"</span>; octave%; <span style="color:#FFB100;">":"</span>;
        <a href="RESTORE" title="RESTORE"><span style="color:#4593D8;">RESTORE</span></a> Octaves
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">12</span>
            <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> note!
            snd% = <a href="CINT" title="CINT"><span style="color:#4593D8;">CINT</span></a>(note! * (<span style="color:#F580B1;">2</span> ^ (octave% - <span style="color:#F580B1;">1</span>))) <span style="color:#919191;">'calculate note frequency</span>
            <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="STR$" title="STR$"><span style="color:#4593D8;">STR$</span></a>(snd%);
            c0l = <a href="POS" title="POS"><span style="color:#4593D8;">POS</span></a>(<span style="color:#F580B1;">0</span>)
            <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">11</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">16</span>, c0l - <span style="color:#F580B1;">2</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>(notes$, <span style="color:#F580B1;">1</span> + (<span style="color:#F580B1;">2</span> * (i - <span style="color:#F580B1;">1</span>)), <span style="color:#F580B1;">2</span>)
            <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">15</span>, c0l
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> snd% &gt; <span style="color:#F580B1;">36</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> snd%, <span style="color:#F580B1;">12</span> <span style="color:#919191;">'error if sound value is &lt; 36</span>
            <a href="DELAY" title="DELAY"><span style="color:#4593D8;">_DELAY</span></a> <span style="color:#F580B1;">.8</span>
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a class="mw-redirect" href="END_IF" title="END IF"><span style="color:#4593D8;">END IF</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> octave% &gt; <span style="color:#F580B1;">7</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
Octaves:
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">32.7</span>,<span style="color:#F580B1;">34.65</span>,<span style="color:#F580B1;">36.71</span>,<span style="color:#F580B1;">38.9</span>,<span style="color:#F580B1;">41.2</span>,<span style="color:#F580B1;">43.65</span>,<span style="color:#F580B1;">46.25</span>,<span style="color:#F580B1;">49</span>,<span style="color:#F580B1;">51.91</span>,<span style="color:#F580B1;">55</span>,<span style="color:#F580B1;">58.27</span>,<span style="color:#F580B1;">61.74</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 2</dt>
<dd>Playing a song called "Bonnie" with <b>SOUND</b> frequencies.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="SCREEN" title="SCREEN"><span style="color:#4593D8;">SCREEN</span></a> <span style="color:#F580B1;">13</span>
<a href="FULLSCREEN" title="FULLSCREEN"><span style="color:#4593D8;">_FULLSCREEN</span></a>
<a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <span style="color:#F580B1;">&amp;H3C8</span>, <span style="color:#F580B1;">0</span>: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <span style="color:#F580B1;">&amp;H3C9</span>, <span style="color:#F580B1;">0</span>: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <span style="color:#F580B1;">&amp;H3C9</span>, <span style="color:#F580B1;">0</span>: <a href="OUT" title="OUT"><span style="color:#4593D8;">OUT</span></a> <span style="color:#F580B1;">&amp;H3C9</span>, <span style="color:#F580B1;">20</span>
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">1</span>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">21</span>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span> + i%, <span style="color:#F580B1;">2</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">178</span>)
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span> + i%, <span style="color:#F580B1;">39</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">178</span>)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">2</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">39</span>
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">2</span>, i%: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">223</span>)
    <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">23</span>, i%: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">220</span>)
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">9</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">3</span>, <span style="color:#F580B1;">16</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">34</span>); <span style="color:#FFB100;">"MY BONNIE"</span>; <a href="CHR$" title="CHR$"><span style="color:#4593D8;">CHR$</span></a>(<span style="color:#F580B1;">34</span>)
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">3</span>
<a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> i% = <span style="color:#F580B1;">1</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">34</span>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> i%
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">1</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">5</span>, <span style="color:#F580B1;">5</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">10</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">10</span>, <span style="color:#F580B1;">5</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">18</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">15</span>, <span style="color:#F580B1;">5</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <span style="color:#F580B1;">27</span>: <a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">20</span>, <span style="color:#F580B1;">5</span>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
    <a href="READ" title="READ"><span style="color:#4593D8;">READ</span></a> note%, duration%, word$
    <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> note%, duration%: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> word$;
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a> i%
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">2</span>
<a href="LOCATE" title="LOCATE"><span style="color:#4593D8;">LOCATE</span></a> <span style="color:#F580B1;">23</span>, <span style="color:#F580B1;">16</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Thank You!"</span>
<a href="SLEEP" title="SLEEP"><span style="color:#4593D8;">SLEEP</span></a> <span style="color:#F580B1;">4</span>
<a href="SYSTEM" title="SYSTEM"><span style="color:#4593D8;">SYSTEM</span></a>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"My "</span>,<span style="color:#F580B1;">659</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Bon-"</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"nie "</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"lies "</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"O-"</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Ver "</span>,<span style="color:#F580B1;">440</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"the "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"O-"</span>,<span style="color:#F580B1;">330</span>,<span style="color:#F580B1;">32</span>,<span style="color:#FFB100;">"cean "</span>,<span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"My "</span>,<span style="color:#F580B1;">659</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Bon-"</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"nie "</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"lies "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"O-"</span>,<span style="color:#F580B1;">494</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"ver "</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"the "</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">40</span>,<span style="color:#FFB100;">"sea "</span>,<span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"My "</span>,<span style="color:#F580B1;">659</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Bon-"</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"nie"</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">" lies "</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"O-"</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"ver "</span>,<span style="color:#F580B1;">440</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"the "</span>,<span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"O-"</span>,<span style="color:#F580B1;">330</span>,<span style="color:#F580B1;">32</span>,<span style="color:#FFB100;">"cean "</span>,<span style="color:#F580B1;">392</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Oh "</span>
<a href="DATA" title="DATA"><span style="color:#4593D8;">DATA</span></a> <span style="color:#F580B1;">440</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"bring "</span>,<span style="color:#F580B1;">587</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"back "</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"my "</span>,<span style="color:#F580B1;">494</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"Bon-"</span>,<span style="color:#F580B1;">440</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"nie "</span>,<span style="color:#F580B1;">494</span>,<span style="color:#F580B1;">8</span>,<span style="color:#FFB100;">"to "</span>,<span style="color:#F580B1;">523</span>,<span style="color:#F580B1;">32</span>,<span style="color:#FFB100;">"me..!"</span>
</pre>
</td></tr></tbody></table>
<dl><dt>Example 3</dt>
<dd>Playing sound effects using the new QB64-PE <b>SOUND</b> extensions.</dd></dl>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="OPTION" title="OPTION"><span style="color:#4593D8;">OPTION</span></a> <a class="mw-redirect" href="EXPLICIT" title="EXPLICIT"><span style="color:#4593D8;">_EXPLICIT</span></a>
<a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> Q <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="STRING" title="STRING"><span style="color:#4593D8;">STRING</span></a>
<span style="color:#919191;">' Sound effects menu</span>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Sound effects"</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"  B"</span>;: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"ouncing"</span>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"  F"</span>;: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"alling"</span>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"  K"</span>;: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"laxon"</span>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"  S"</span>;: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"iren"</span>
    <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">14</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"  Q"</span>;: <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> <span style="color:#F580B1;">7</span>, <span style="color:#F580B1;">0</span>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"uit"</span>
    <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a>: <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Select: "</span>;
    <span style="color:#919191;">' Get valid key</span>
    <a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>
        Q = <a href="UCASE$" title="UCASE$"><span style="color:#4593D8;">UCASE$</span></a>(<a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(<span style="color:#F580B1;">1</span>))
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP WHILE</span></a> <a href="INSTR" title="INSTR"><span style="color:#4593D8;">INSTR</span></a>(<span style="color:#FFB100;">"BFKSQ"</span>, Q) = <span style="color:#F580B1;">0</span>
    <span style="color:#919191;">' Take action based on key</span>
    <a href="CLS" title="CLS"><span style="color:#4593D8;">CLS</span></a>
    <a href="SELECT_CASE" title="SELECT CASE"><span style="color:#4593D8;">SELECT CASE</span></a> Q
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> = <span style="color:#FFB100;">"B"</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Bouncing . . . "</span>
            <span style="color:#55FF55;">Bounce</span> <span style="color:#F580B1;">32767</span>, <span style="color:#F580B1;">246</span> <span style="color:#919191;">' the 32767 will make the PSG generate silence (exactly like QB45 does)</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> = <span style="color:#FFB100;">"F"</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Falling . . . "</span>
            <span style="color:#55FF55;">Fall</span> <span style="color:#F580B1;">2000</span>, <span style="color:#F580B1;">550</span>, <span style="color:#F580B1;">500</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> = <span style="color:#FFB100;">"S"</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Wailing . . ."</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">" . . . press any key to end."</span>
            <span style="color:#55FF55;">Siren</span> <span style="color:#F580B1;">780</span>, <span style="color:#F580B1;">650</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a class="mw-redirect" href="IS" title="IS"><span style="color:#4593D8;">IS</span></a> = <span style="color:#FFB100;">"K"</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">"Oscillating . . ."</span>
            <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> <span style="color:#FFB100;">" . . . press any key to end."</span>
            <span style="color:#55FF55;">Klaxon</span> <span style="color:#F580B1;">987</span>, <span style="color:#F580B1;">329</span>
        <a class="mw-redirect" href="CASE" title="CASE"><span style="color:#4593D8;">CASE</span></a> <a href="ELSE" title="ELSE"><span style="color:#4593D8;">ELSE</span></a>
    <a href="END_SELECT" title="END SELECT"><span style="color:#4593D8;">END SELECT</span></a>
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">LOOP UNTIL</span></a> Q = <span style="color:#FFB100;">"Q"</span>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<span style="color:#919191;">' Loop two sounds down at decreasing time intervals</span>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">Bounce</span> (Hi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Low <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> count <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    <a href="PLAY" title="PLAY"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"Q0"</span> <span style="color:#919191;">' turn off volume ramping</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> count = <span style="color:#F580B1;">60</span> <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> <span style="color:#F580B1;">1</span> <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">-2</span>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> Low - count / <span style="color:#F580B1;">2</span>, count / <span style="color:#F580B1;">20</span>, <span style="color:#F580B1;">1.0!</span>, <span style="color:#F580B1;">0.0!</span>, <span style="color:#F580B1;">1</span>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> Hi, count / <span style="color:#F580B1;">15</span>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<span style="color:#919191;">' Loop down from a high sound to a low sound</span>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">Fall</span> (Hi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Low <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Del <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> vol <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> count <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>
    <a href="PLAY" title="PLAY"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"Q3"</span> <span style="color:#919191;">' enable 3ms volume ramping</span>
    <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> count = Hi <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> Low <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">-10</span>
        vol = <span style="color:#F580B1;">1.0!</span> - vol
        <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> count, Del / count, vol, <span style="color:#F580B1;">0.0!</span>, <span style="color:#F580B1;">3</span> <span style="color:#919191;">' triangle wave</span>
    <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<span style="color:#919191;">' Alternate two sounds until a key is pressed</span>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">Klaxon</span> (Hi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Low <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="PLAY" title="PLAY"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"Q5"</span> <span style="color:#919191;">' enable 5ms volume ramping</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <span style="color:#FFB100;">""</span>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> Hi, <span style="color:#F580B1;">5!</span>, <span style="color:#F580B1;">1.0!</span>, <span style="color:#F580B1;">-1.0!</span>, <span style="color:#F580B1;">4</span>
        <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> Low, <span style="color:#F580B1;">5!</span>, <span style="color:#F580B1;">1.0!</span>, <span style="color:#F580B1;">1.0!</span>, <span style="color:#F580B1;">4</span>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
<span style="color:#919191;">' Loop a sound from low to high to low</span>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> <span style="color:#55FF55;">Siren</span> (Hi <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, Range <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>)
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> count <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="LONG" title="LONG"><span style="color:#4593D8;">LONG</span></a>, pan <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>
    <a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> dir <a href="AS" title="AS"><span style="color:#4593D8;">AS</span></a> <a href="SINGLE" title="SINGLE"><span style="color:#4593D8;">SINGLE</span></a>: dir = <span style="color:#F580B1;">0.01!</span>
    <a href="PLAY" title="PLAY"><span style="color:#4593D8;">PLAY</span></a> <span style="color:#FFB100;">"Q0"</span> <span style="color:#919191;">' disable volume ramping</span>
    <a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO WHILE</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> = <span style="color:#FFB100;">""</span>
        <a href="FOR" title="FOR"><span style="color:#4593D8;">FOR</span></a> count = Range <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> -Range <a href="STEP" title="STEP"><span style="color:#4593D8;">STEP</span></a> <span style="color:#F580B1;">-4</span>
            pan = pan + dir
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> pan &lt;= <span style="color:#F580B1;">-1.0!</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = <span style="color:#F580B1;">0.01!</span>: pan = <span style="color:#F580B1;">-1.0!</span>
            <a class="mw-redirect" href="IF" title="IF"><span style="color:#4593D8;">IF</span></a> pan &gt;= <span style="color:#F580B1;">1.0!</span> <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> dir = <span style="color:#F580B1;">-0.01!</span>: pan = <span style="color:#F580B1;">1.0!</span>
            <a class="mw-selflink selflink"><span style="color:#4593D8;">SOUND</span></a> Hi - <a href="ABS" title="ABS"><span style="color:#4593D8;">ABS</span></a>(count), <span style="color:#F580B1;">0.3!</span>, <span style="color:#F580B1;">1.0!</span>, pan, <span style="color:#F580B1;">4</span> <span style="color:#919191;">' sine wave</span>
            count = count - <span style="color:#F580B1;">2</span> / Range
        <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
    <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="PLAY" title="PLAY">PLAY</a>, <a href="BEEP" title="BEEP">BEEP</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li>
<li><a href="SNDRAW" title="SNDRAW">_SNDRAW</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715061420
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.162 seconds
Real time usage: 0.217 seconds
Preprocessor visited node count: 4364/1000000
Post‐expand include size: 28773/2097152 bytes
Template argument size: 8184/2097152 bytes
Highest expansion depth: 4/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 3419/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  130.664      1 -total
 15.13%   19.773    322 Template:Text
 12.55%   16.401     17 Template:Parameter
  8.83%   11.537    242 Template:Cl
  5.85%    7.648      1 Template:PageExamples
  5.63%    7.356      1 Template:FixedStart
  5.49%    7.168      1 Template:PageDescription
  2.85%    3.724      1 Template:PageSyntax
  2.19%    2.862      3 Template:CodeStart
  2.17%    2.832      1 Template:PageSeeAlso
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:564-0!canonical and timestamp 20240715061420 and revision id 8787.
 -->
</div>
</div>
</div>
</div>
</body>
</html>