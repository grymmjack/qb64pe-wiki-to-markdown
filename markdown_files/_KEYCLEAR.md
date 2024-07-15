<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_KEYCLEAR - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-KEYCLEAR rootpage-KEYCLEAR skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_KEYCLEAR</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p><a class="mw-selflink selflink">_KEYCLEAR</a> clears all keyboard input buffers.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_KEYCLEAR</a> [<i>buffer&amp;</i>]</dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li><i>buffer&amp;</i> indicates the buffer to be cleared:
<ul><li>1 - Clear the regular keyboard buffer, as used by all input command except the following:  _KEYHIT, _KEYDOWN, INP(&amp;H60.  This is the same as the the emulated BIOS keyboard buffer, so legacy code reading from it via PEEK/POKE/CALL ABSOLUTE will also be affected.</li>
<li>2 - Clear the buffer used by _KEYHIT.</li>
<li>3 - Clear INP(&amp;H60) buffer. (see <b>Warning</b> in the the description below)</li></ul></li>
<li>If no parameter is passed, all three buffers are cleared.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>The <b>_KEYCLEAR</b> command clears the specified keyboard input buffer. In effect, it is as if a loop has been used to read from the buffer until it is empty. All keys cleared are lost.</li>
<li><b>Warning:</b> The buffer read by INP(&amp;H60) does not behave as the other buffers do. Whilst reading from the others will eventually empty after reading all data, this buffer will continue to return the last value. For this reason, <a class="mw-selflink selflink">_KEYCLEAR</a> is of little effect, but is included for completeness (an internal flag indicating new data on the port is cleared). However, using <a href="INP" title="INP">INP</a> for anything is strongly discouraged, and is for backwards compatibility only.</li>
<li>This command is best used just before getting input, in order to clear stray key presses from commands such as SLEEP, or just random keyboard bashing by the user. The programmer also ought to be aware of key release events in the _KEYHIT buffer; consider the following code:</li></ul>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">INPUT "Name: ", name$
_KEYCLEAR
_DELAY 2 'Simulate doing some processing that takes some time.
PRINT _KEYHIT
</pre>
</td></tr></tbody></table>
<ul><li>The INPUT statement finishes as soon as the Enter key is struck; the program then proceeds to clear all input buffers. Because this is executed so quickly, it is likely that the user will release the Enter key after the _KEYCLEAR command is executed, leaving a -13 (Enter key release) event in the _KEYHIT buffer.</li>
<li>As mentioned above, it is best to place the _KEYCLEAR after the processing, immediately before the PRINT _KEYHIT command:</li></ul>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">INPUT "Name: ", name$
_DELAY 2 'Simulate doing some processing that takes some time.
_KEYCLEAR
PRINT _KEYHIT
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Examples">Examples</span></h2>
<p>Example:
</p>
<table cellpadding="15px" width="100%">
<tbody><tr>
<td><pre class="codeide">PRINT "Press a key"
SLEEP 'Wait for keypress
'Three alternative _KEYCLEAR calls. Try uncommenting different ones to see the effect.
'_KEYCLEAR
'_KEYCLEAR 1
'_KEYCLEAR 2
PRINT "In regular buffer, there is "; INKEY$ 'read regular buffer
PRINT "In _KEYHIT buffer, there is "; _KEYHIT 'read the _KEYHIT buffer
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a class="external text" href="https://qb64phoenix.com/forum/showthread.php?tid=1105" rel="nofollow">Featured in our "Keyword of the Day" series</a></li>
<li><a href="SLEEP" title="SLEEP">SLEEP</a></li>
<li><a href="INKEY$" title="INKEY$">INKEY$</a>, <a href="KEYHIT" title="KEYHIT">_KEYHIT</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714144222
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.022 seconds
Real time usage: 0.040 seconds
Preprocessor visited node count: 38/1000000
Post‐expand include size: 847/2097152 bytes
Template argument size: 14/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   28.576      1 -total
 52.73%   15.068      1 Template:PageSyntax
  7.35%    2.099      2 Template:Parameter
  5.61%    1.603      1 Template:PageParameters
  5.40%    1.544      3 Template:CodeStart
  5.29%    1.513      1 Template:PageExamples
  5.21%    1.489      1 Template:PageDescription
  5.10%    1.456      1 Template:PageSeeAlso
  5.01%    1.432      1 Template:PageNavigation
  4.83%    1.381      3 Template:CodeEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:161-0!canonical and timestamp 20240714144222 and revision id 8886.
 -->
</div>
</div>
</div>
</div>
</body>
</html>