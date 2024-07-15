<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_glDeleteLists - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GlDeleteLists rootpage-GlDeleteLists skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_glDeleteLists</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_glDeleteLists</b> statement deletes a contiguous group of display lists.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_glDeleteLists</a> GLuint <i>list</i>, GLsizei <i>range</i></dd></dl>
<p>
</p>
<h2><span class="mw-headline" id="Parameters">Parameters</span></h2>
<ul><li>OpenGL is using its own set of variable types to describe its command parameters.</li>
<li>Use the following table to find the respective QB64 <a href="Variable_Types" title="Variable Types">Variable Types</a>.</li></ul>
<table cellpadding="5px" width="100%">
<tbody><tr>
<td><pre class="outputfixed">   Table 2: Relations between the OpenGL variable types vs. C/C++ and QB64.
 ┌──────────────┬────────────────┬──────────────────────────────────────────┐
 │    <b>OpenGL</b>    │     <b>C/C++</b>      │     <b>QB64</b>                                 │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLenum       │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLboolean    │ unsigned char  │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a>                          │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLbitfield   │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLbyte       │ signed char    │ <a href="BYTE" title="BYTE">_BYTE</a>                                    │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLshort      │ short          │ <a href="INTEGER" title="INTEGER">INTEGER</a>                                  │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLint        │ int            │ <a href="LONG" title="LONG">LONG</a>                                     │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLsizei      │ int            │ <a href="LONG" title="LONG">LONG</a>                                     │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLubyte      │ unsigned char  │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="BYTE" title="BYTE">_BYTE</a>                          │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLushort     │ unsigned short │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="INTEGER" title="INTEGER">INTEGER</a>                        │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLuint       │ unsigned int   │ <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a>                           │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLfloat      │ float          │ <a href="SINGLE" title="SINGLE">SINGLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLclampf     │ float          │ <a href="SINGLE" title="SINGLE">SINGLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLdouble     │ double         │ <a href="DOUBLE" title="DOUBLE">DOUBLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLclampd     │ double         │ <a href="DOUBLE" title="DOUBLE">DOUBLE</a>                                   │
 ├──────────────┼────────────────┼──────────────────────────────────────────┤
 │ GLvoid   <b>(1)</b> │ void           │ <a href="OFFSET" title="OFFSET">_OFFSET</a>(any fixed lenght string or <a href="BYTE" title="BYTE">_BYTE</a> │
 │              │                │         array element)                   │
 └──────────────┴────────────────┴──────────────────────────────────────────┘
 <b>Note:</b> If a parameter has an asterisk (*) in front, then it's a pointer to
       the designated OpenGL variable type, rather than a value of that type.
       Those must be passed using the <a href="OFFSET" title="OFFSET">_OFFSET</a>(...) notation.
 <b>E.g.</b>  GLuint *anyParam is actually the offset of a <a href="UNSIGNED" title="UNSIGNED">_UNSIGNED</a> <a href="LONG" title="LONG">LONG</a> (~&amp;)
       variable or array, which must be passed as <a href="OFFSET" title="OFFSET">_OFFSET</a>(anyVar~&amp;) or
       <a href="OFFSET" title="OFFSET">_OFFSET</a>(anyArr~&amp;()) respectively.
  <b>(1)</b>  This type is regularly only used for pointers (with asterisk (*)) to
       any byte sized memory data, hence <a href="BYTE" title="BYTE">_BYTE</a> or fixed length strings.
</pre>
</td></tr></tbody></table>
<p>
</p>
<h2><span class="mw-headline" id="Description">Description</span></h2>
<ul><li>OpenGL's documentation is available in several places, so we won't reproduce it here for another time.</li>
<li>The full description for this command can be found at <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gldeletelists" rel="nofollow">Microsoft Docs</a> and is also valid for QB64 usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GL" title="GL">SUB _GL</a></li>
<li><a href="GlBegin" title="GlBegin">_glBegin</a>, <a href="GlCallList" title="GlCallList">_glCallList</a>, <a href="GlCallLists" title="GlCallLists">_glCallLists</a>, <a href="GlEnd" title="GlEnd">_glEnd</a></li>
<li><a href="GlGenLists" title="GlGenLists">_glGenLists</a>, <a href="GlIsList" title="GlIsList">_glIsList</a>, <a href="GlNewList" title="GlNewList">_glNewList</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240715032809
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.025 seconds
Real time usage: 0.033 seconds
Preprocessor visited node count: 31/1000000
Post‐expand include size: 6896/2097152 bytes
Template argument size: 9/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   18.849      1 -total
 29.40%    5.542      1 Template:OpenGLTypesPlugin
 12.42%    2.341      1 Template:PageSyntax
 11.43%    2.154      1 Template:PageSeeAlso
 11.38%    2.146      2 Template:Parameter
 11.02%    2.077      1 Template:PageParameters
 10.59%    1.997      1 Template:PageNavigation
 10.01%    1.887      1 Template:PageDescription
  9.90%    1.866      1 Template:FixedStart
  8.30%    1.565      1 Template:FixedEnd
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:864-0!canonical and timestamp 20240715032809 and revision id 6835.
 -->
</div>
</div>
</div>
</div>
</body>
</html>