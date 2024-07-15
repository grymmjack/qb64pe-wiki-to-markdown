<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_SNDRAW - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-SNDRAW rootpage-SNDRAW skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_SNDRAW</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <a class="mw-selflink selflink">_SNDRAW</a> statement plays sound wave sample frequencies created by a program.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_SNDRAW</a> <i>leftSample</i>[, <i>rightSample</i>][, <i>pipeHandle&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>The <i>leftSample</i> and <i>rightSample</i> value(s) can be any <a href="SINGLE" title="SINGLE">SINGLE</a> or <a href="DOUBLE" title="DOUBLE">DOUBLE</a> literal or variable frequency value from -1.0 to 1.0.</li>
<li>The <i>pipeHandle&amp;</i> parameter refers to the sound pipe opened using <a href="SNDOPENRAW" title="SNDOPENRAW">_SNDOPENRAW</a>.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>Specifying <i>pipeHandle&amp;</i> allows sound to be played through two or more channels at the same time (<b>version 1.000 and up</b>).</li>
<li>If only <i>leftSample</i> value is used, the sound will come out of both speakers.</li>
<li>Using _SNDRAW will pause any currently playing music.</li>
<li>_SNDRAW is designed for continuous play. It will not produce any sound until a significant number of samples have been queued. No sound is played if only a few samples are queued.</li>
<li>Ensure that <a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a> is comfortably above 0 (until you've actually finished playing sound). If you are getting occasional unintended random clicks, this generally means that <a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a> has dropped to 0.</li>
<li>_SNDRAW is not intended to queue up many minutes worth of sound. It will probably work but will chew up a lot of memory (and if it gets swapped to disk, your sound could be interrupted abruptly).</li>
<li><a href="SNDRATE" title="SNDRATE">_SNDRATE</a> determines how many samples are played per second, but timing is done by the sound card, not your program.</li>
<li><b>Do not attempt to use <a href="TIMER" title="TIMER">_TIMER</a> or <a href="DELAY" title="DELAY">_DELAY</a> or <a href="LIMIT" title="LIMIT">_LIMIT</a> to control the timing of _SNDRAW. You may use them for delays or to limit your program's CPU usage, but how much to queue should only be based on the <a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a>.</b></li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p><i>Example 1:</i> Sound using a sine wave with _SNDRAW Amplitude * SIN(8 * ATN(1) * Duration * (Frequency / _SNDRATE))
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">FREQ = 400                             'any frequency desired from 36 to 10,000
Pi2 = 8 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1)                       '2 * pi
Amplitude = .3                         'amplitude of the signal from -1.0 to 1.0
SampleRate = <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>                  'sets the sample rate
FRate = FREQ / SampleRate'
<a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> Duration = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 5 * SampleRate     'play 5 seconds
        <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDRAW</span></a> Amplitude * <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(Pi2 * Duration * FRate)            'sine wave
       '<a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDRAW</span></a> Amplitude * <a href="SGN" title="SGN"><span style="color:#4593D8;">SGN</span></a>(<a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(Pi2 * Duration * FRate))       'square wave
<a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="SNDRAWDONE" title="SNDRAWDONE"><span style="color:#4593D8;">_SNDRAWDONE</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: LOOP <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="SNDRAWLEN" title="SNDRAWLEN"><span style="color:#4593D8;">_SNDRAWLEN</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<dl><dd><i>Explanation:</i> The loop Duration is determined by the number of seconds times the <a href="SNDRATE" title="SNDRATE">_SNDRATE</a> number of samples per second. Square waves can use the same formula with Amplitude * <a href="SGN" title="SGN">SGN</a>(SIN(8 * ATN(1) * Duration * (Frequency/_SNDRATE))).</dd></dl>
<p>
<i>Example 2:</i> A simple ringing bell tone that tapers off.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">t = 0
tmp$ = "Sample = ##.#####   Time = ##.#####"
LOCATE 1, 60: PRINT "Rate:"; <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>
DO
  'queue some sound
  DO WHILE <a href="SNDRAWLEN" title="SNDRAWLEN"><span style="color:#4593D8;">_SNDRAWLEN</span></a> &lt; 0.2             'you may wish to adjust this
    sample = <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>(t * 440 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1) * 8)  '440Hz sine wave (t * 440 * 2π)
    sample = sample * <a href="EXP" title="EXP"><span style="color:#4593D8;">EXP</span></a>(-t * 3)       'fade out eliminates clicks after sound
    <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDRAW</span></a> sample
    t = t + 1 / <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>                'sound card sample frequency determines time
  LOOP
  'do other stuff, but it may interrupt sound
  LOCATE 1, 1: PRINT USING tmp$; sample; t
LOOP WHILE t &lt; 3.0                      'play for 3 seconds
<a href="SNDRAWDONE" title="SNDRAWDONE"><span style="color:#4593D8;">_SNDRAWDONE</span></a>
DO WHILE <a href="SNDRAWLEN" title="SNDRAWLEN"><span style="color:#4593D8;">_SNDRAWLEN</span></a> &gt; 0                 'Finish any left over queued sound!
LOOP
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
</pre>
</td></tr></tbody></table>
<p>
<i>Example 3:</i> Routine uses _SNDRAW to display and play 12 notes from octaves 1 through 9.
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide"><a href="DIM" title="DIM"><span style="color:#4593D8;">DIM</span></a> <a href="SHARED" title="SHARED"><span style="color:#4593D8;">SHARED</span></a> rate&amp;
rate&amp; = <a href="SNDRATE" title="SNDRATE"><span style="color:#4593D8;">_SNDRATE</span></a>
DO
  <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> "Enter the octave 1 to 8 (0 quits!):";
  oct% = <a href="VAL" title="VAL"><span style="color:#4593D8;">VAL</span></a>(<a href="INPUT$" title="INPUT$"><span style="color:#4593D8;">INPUT$</span></a>(1)): <a href="PRINT" title="PRINT"><span style="color:#4593D8;">PRINT</span></a> oct%
  <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> oct% = 0 <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  octave = oct% - 4 '440 is in the 4th octave, 9th note
  <a href="COLOR" title="COLOR"><span style="color:#4593D8;">COLOR</span></a> oct% + 1
  <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> "Octave: ##"; oct%
  <a href="FOR...NEXT" title="FOR...NEXT"><span style="color:#4593D8;">FOR</span></a> Note = 0 <a href="TO" title="TO"><span style="color:#4593D8;">TO</span></a> 11  'notes C to B
    fq = FreQ(octave, Note, note$)
    <a href="PRINT_USING" title="PRINT USING"><span style="color:#4593D8;">PRINT USING</span></a> "#####.## \\"; fq, note$
    PlaySound fq
    <a href="IF...THEN" title="IF...THEN"><span style="color:#4593D8;">IF</span></a> <a href="INKEY$" title="INKEY$"><span style="color:#4593D8;">INKEY$</span></a> &gt; "" <a href="THEN" title="THEN"><span style="color:#4593D8;">THEN</span></a> <a href="EXIT_DO" title="EXIT DO"><span style="color:#4593D8;">EXIT DO</span></a>
  <a href="NEXT" title="NEXT"><span style="color:#4593D8;">NEXT</span></a>
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="END" title="END"><span style="color:#4593D8;">END</span></a>
<a href="FUNCTION" title="FUNCTION"><span style="color:#4593D8;">FUNCTION</span></a> FreQ (octave, note, note$)
FreQ = 440 * 2 ^ (octave + (note + 3) / 12 - 1) '* 12 note octave starts at C (3 notes up)
note$ = <a href="MID$_(function)" title="MID$ (function)"><span style="color:#4593D8;">MID$</span></a>("C C#D D#E F F#G G#A A#B ", note * 2 + 1, 2)
<a class="mw-redirect" href="END_FUNCTION" title="END FUNCTION"><span style="color:#4593D8;">END FUNCTION</span></a>
<a href="SUB" title="SUB"><span style="color:#4593D8;">SUB</span></a> PlaySound (frq!)    ' plays sine wave fading in and out
SndLoop! = 0
<a href="DO...LOOP" title="DO...LOOP"><span style="color:#4593D8;">DO</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> SndLoop! &lt; rate&amp;
  <a class="mw-selflink selflink"><span style="color:#4593D8;">_SNDRAW</span></a> <a href="SIN" title="SIN"><span style="color:#4593D8;">SIN</span></a>((2 * 4 * <a href="ATN" title="ATN"><span style="color:#4593D8;">ATN</span></a>(1) * SndLoop! / rate&amp;) * frq!) * <a href="EXP" title="EXP"><span style="color:#4593D8;">EXP</span></a>(-(SndLoop! / rate&amp;) * 3)
  SndLoop! = SndLoop! + 1
<a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a>
<a href="SNDRAWDONE" title="SNDRAWDONE"><span style="color:#4593D8;">_SNDRAWDONE</span></a>
<a class="mw-redirect" href="DO" title="DO"><span style="color:#4593D8;">DO</span></a>: <a href="LOOP" title="LOOP"><span style="color:#4593D8;">LOOP</span></a> <a class="mw-redirect" href="WHILE" title="WHILE"><span style="color:#4593D8;">WHILE</span></a> <a href="SNDRAWLEN" title="SNDRAWLEN"><span style="color:#4593D8;">_SNDRAWLEN</span></a>   'flush the sound playing buffer
<a href="END_SUB" title="END SUB"><span style="color:#4593D8;">END SUB</span></a>
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="SNDRATE" title="SNDRATE">_SNDRATE</a>, <a href="SNDRAWLEN" title="SNDRAWLEN">_SNDRAWLEN</a></li>
<li><a href="SNDOPENRAW" title="SNDOPENRAW">_SNDOPENRAW</a>, <a href="SNDRAWDONE" title="SNDRAWDONE">_SNDRAWDONE</a></li>
<li><a href="SNDOPEN" title="SNDOPEN">_SNDOPEN</a></li>
<li><a href="PLAY" title="PLAY">PLAY</a>, <a href="BEEP" title="BEEP">BEEP</a></li>
<li><a href="DTMF_Phone_Demo" title="DTMF Phone Demo">DTMF Phone Demo</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714192909
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.039 seconds
Real time usage: 0.050 seconds
Preprocessor visited node count: 525/1000000
Post‐expand include size: 4710/2097152 bytes
Template argument size: 866/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.867      1 -total
 14.31%    4.130     64 Template:Cl
 11.11%    3.207      1 Template:PageSyntax
  7.76%    2.240      1 Template:PageSeeAlso
  7.17%    2.071      8 Template:Parameter
  6.99%    2.017      1 Template:PageNavigation
  6.80%    1.963      3 Template:Small
  6.73%    1.943      1 Template:PageParameters
  6.36%    1.837      3 Template:CodeStart
  6.10%    1.760      3 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:345-0!canonical and timestamp 20240714192909 and revision id 8786.
 -->
</div>
</div>
</div>
</div>
</body>
</html>