<style>pre.codeide, pre.outputfixed, .outputcrt0 { background-color: #000 !important; color: #FFF !important; }</style><!DOCTYPE html>
<html class="client-nojs" dir="ltr" lang="en">
<head>
<title>_glEvalCoord2d - QB64 Phoenix Edition Wiki</title>
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-GlEvalCoord2d rootpage-GlEvalCoord2d skin-vector action-view skin-vector-legacy vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-disabled vector-feature-sticky-header-disabled vector-feature-sticky-header-edit-disabled vector-feature-table-of-contents-disabled vector-feature-visual-enhancement-next-disabled">
<div class="mw-body" id="content" role="main">
<a id="top"></a>
<h1 class="firstHeading mw-first-heading" id="firstHeading">_glEvalCoord2d</h1>
<div class="vector-body" id="bodyContent">
<div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><p>The <b>_glEvalCoord2d</b> statement evaluates enabled two-dimensional maps.
</p>
<h2><span class="mw-headline" id="Syntax">Syntax</span></h2>
<dl><dd><a class="mw-selflink selflink">_glEvalCoord2d</a> GLdouble <i>u</i>, GLdouble <i>v</i></dd></dl>
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
<li>The full description for this command can be found at <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glevalcoord2d" rel="nofollow">Microsoft Docs</a> and is also valid for QB64 usage.</li></ul>
<p>
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="GL" title="GL">SUB _GL</a></li>
<li><a href="GlBegin" title="GlBegin">_glBegin</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glcolor-functions" rel="nofollow">_glColor</a>, <a href="GlDisable" title="GlDisable">_glDisable</a>, <a href="GlEnable" title="GlEnable">_glEnable</a></li>
<li><a href="GlEnd" title="GlEnd">_glEnd</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glevalmesh-functions" rel="nofollow">_glEvalMesh</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glevalpoint" rel="nofollow">_glEvalPoint</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glgetmap" rel="nofollow">_glGetMap</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glindex-functions" rel="nofollow">_glIndex</a>, <a href="GlIsEnabled" title="GlIsEnabled">_glIsEnabled</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmap1" rel="nofollow">_glMap1</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmap2" rel="nofollow">_glMap2</a></li>
<li><a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glmapgrid-functions" rel="nofollow">_glMapGrid</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glnormal-functions" rel="nofollow">_glNormal</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/gltexcoord-functions" rel="nofollow">_glTexCoord</a>, <a class="external text" href="https://learn.microsoft.com/en-us/windows/win32/opengl/glvertex-functions" rel="nofollow">_glVertex</a></li></ul>
<p>
</p>
<!-- 
NewPP limit report
Cached time: 20240714213247
Cache expiry: 86400
Reduced expiry: false
Complications: [show‐toc]
CPU time usage: 0.026 seconds
Real time usage: 0.035 seconds
Preprocessor visited node count: 31/1000000
Post‐expand include size: 6889/2097152 bytes
Template argument size: 2/2097152 bytes
Highest expansion depth: 3/100
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%   17.254      1 -total
 32.73%    5.647      1 Template:OpenGLTypesPlugin
 12.78%    2.205      2 Template:Parameter
 11.43%    1.973      1 Template:PageSyntax
 11.13%    1.920      1 Template:FixedEnd
 10.22%    1.764      1 Template:PageSeeAlso
 10.01%    1.728      1 Template:PageNavigation
  9.72%    1.677      1 Template:PageParameters
  9.47%    1.634      1 Template:PageDescription
  9.34%    1.612      1 Template:FixedStart
-->
<!-- Saved in parser cache with key qb64pnix_mw19894-mwmb_:pcache:idhash:911-0!canonical and timestamp 20240714213247 and revision id 6857.
 -->
</div>
</div>
</div>
</div>
</body>
</html>