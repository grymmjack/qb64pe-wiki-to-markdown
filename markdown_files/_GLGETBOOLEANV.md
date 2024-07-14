


\_glGetBooleanv - QB64 Phoenix Edition Wiki








# \_glGetBooleanv



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_glGetBooleanv** statement returns the value or values of a selected parameter.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


\_glGetBooleanv GLenum *pname*, GLboolean *\*params*
  




## Parameters


* OpenGL is using its own set of variable types to describe its command parameters.
* Use the following table to find the respective QB64 [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types").




| ```    Table 2: Relations between the OpenGL variable types vs. C/C++ and QB64.  ┌──────────────┬────────────────┬──────────────────────────────────────────┐  │    **OpenGL**    │     **C/C++**      │     **QB64**                                 │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLenum       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLboolean    │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbitfield   │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbyte       │ signed char    │ [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                                    │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLshort      │ short          │ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                                  │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLint        │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLsizei      │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLubyte      │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLushort     │ unsigned short │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                        │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLuint       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLfloat      │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampf     │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLdouble     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampd     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLvoid   **(1)** │ void           │ [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(any fixed lenght string or [_BYTE](/qb64wiki/index.php/BYTE "BYTE") │  │              │                │         array element)                   │  └──────────────┴────────────────┴──────────────────────────────────────────┘  **Note:** If a parameter has an asterisk (*) in front, then it's a pointer to        the designated OpenGL variable type, rather than a value of that type.        Those must be passed using the [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(...) notation.   **E.g.**  GLuint *anyParam is actually the offset of a [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") (~&)        variable or array, which must be passed as [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyVar~&) or        [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyArr~&()) respectively.    **(1)**  This type is regularly only used for pointers (with asterisk (*)) to        any byte sized memory data, hence [_BYTE](/qb64wiki/index.php/BYTE "BYTE") or fixed length strings.  ``` |
| --- |


  




## Description


* OpenGL's documentation is available in several places, so we won't reproduce it here for another time.
* The full description for this command can be found at [Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetbooleanv) and is also valid for QB64 usage.


  




## See also


* [SUB \_GL](/qb64wiki/index.php/GL "GL")
* [\_glAccum](/qb64wiki/index.php/GlAccum "GlAccum"), [\_glAlphaFunc](/qb64wiki/index.php/GlAlphaFunc "GlAlphaFunc"), [\_glBegin](/qb64wiki/index.php/GlBegin "GlBegin"), [\_glBlendFunc](/qb64wiki/index.php/GlBlendFunc "GlBlendFunc")
* [\_glCallList](/qb64wiki/index.php/GlCallList "GlCallList"), [\_glClearAccum](/qb64wiki/index.php/GlClearAccum "GlClearAccum"), [\_glClearColor](/qb64wiki/index.php/GlClearColor "GlClearColor"), [\_glClearDepth](/qb64wiki/index.php/GlClearDepth "GlClearDepth")
* [\_glClearIndex](/qb64wiki/index.php/GlClearIndex "GlClearIndex"), [\_glClearStencil](/qb64wiki/index.php/GlClearStencil "GlClearStencil"), [\_glClipPlane](/qb64wiki/index.php/GlClipPlane "GlClipPlane"), [\_glColor](https://learn.microsoft.com/en-us/windows/win32/opengl/glcolor-functions)
* [\_glColorMask](/qb64wiki/index.php/GlColorMask "GlColorMask"), [\_glColorMaterial](/qb64wiki/index.php/GlColorMaterial "GlColorMaterial"), [\_glCullFace](/qb64wiki/index.php/GlCullFace "GlCullFace"), [\_glDepthFunc](/qb64wiki/index.php/GlDepthFunc "GlDepthFunc")
* [\_glDepthMask](/qb64wiki/index.php/GlDepthMask "GlDepthMask"), [\_glDepthRange](/qb64wiki/index.php/GlDepthRange "GlDepthRange"), [\_glDrawBuffer](/qb64wiki/index.php/GlDrawBuffer "GlDrawBuffer"), [\_glEdgeFlag](https://learn.microsoft.com/en-us/windows/win32/opengl/gledgeflag-functions)
* [\_glEnd](/qb64wiki/index.php/GlEnd "GlEnd"), [\_glFog](https://learn.microsoft.com/en-us/windows/win32/opengl/glfog), [\_glFrontFace](/qb64wiki/index.php/GlFrontFace "GlFrontFace"), [\_glGetClipPlane](/qb64wiki/index.php/GlGetClipPlane "GlGetClipPlane")
* [\_glGetError](/qb64wiki/index.php/GlGetError "GlGetError"), [\_glGetLight](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetlight), [\_glGetMap](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetmap), [\_glGetMaterial](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetmaterial)
* [\_glGetPixelMap](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetpixelmap), [\_glGetPolygonStipple](/qb64wiki/index.php/GlGetPolygonStipple "GlGetPolygonStipple"), [\_glGetString](/qb64wiki/index.php/GlGetString "GlGetString"), [\_glGetTexEnv](https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexenv)
* [\_glGetTexGen](https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexgen), [\_glGetTexImage](/qb64wiki/index.php/GlGetTexImage "GlGetTexImage"), [\_glGetTexLevelParameter](https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexlevelparameter), [\_glGetTexParameter](https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexparameter)
* [\_glHint](/qb64wiki/index.php/GlHint "GlHint"), [\_glIndex](https://learn.microsoft.com/en-us/windows/win32/opengl/glindex-functions), [\_glIndexMask](/qb64wiki/index.php/GlIndexMask "GlIndexMask"), [\_glIsEnabled](/qb64wiki/index.php/GlIsEnabled "GlIsEnabled")
* [\_glLight](https://learn.microsoft.com/en-us/windows/win32/opengl/gllight-functions), [\_glLightModel](https://learn.microsoft.com/en-us/windows/win32/opengl/gllightmodel-functions), [\_glLineStipple](/qb64wiki/index.php/GlLineStipple "GlLineStipple"), [\_glLineWidth](/qb64wiki/index.php/GlLineWidth "GlLineWidth")
* [\_glListBase](/qb64wiki/index.php/GlListBase "GlListBase"), [\_glLogicOp](/qb64wiki/index.php/GlLogicOp "GlLogicOp"), [\_glMap1](https://learn.microsoft.com/en-us/windows/win32/opengl/glmap1), [\_glMap2](https://learn.microsoft.com/en-us/windows/win32/opengl/glmap2)
* [\_glMapGrid](https://learn.microsoft.com/en-us/windows/win32/opengl/glmapgrid-functions), [\_glMatrixMode](/qb64wiki/index.php/GlMatrixMode "GlMatrixMode"), [\_glNewList](/qb64wiki/index.php/GlNewList "GlNewList"), [\_glNormal](https://learn.microsoft.com/en-us/windows/win32/opengl/glnormal-functions)
* [\_glPixelMap](https://learn.microsoft.com/en-us/windows/win32/opengl/glpixelmap), [\_glPixelStore](https://learn.microsoft.com/en-us/windows/win32/opengl/glpixelstore-functions), [\_glPixelTransfer](https://learn.microsoft.com/en-us/windows/win32/opengl/glpixeltransfer), [\_glPixelZoom](/qb64wiki/index.php/GlPixelZoom "GlPixelZoom")
* [\_glPointSize](/qb64wiki/index.php/GlPointSize "GlPointSize"), [\_glPolygonMode](/qb64wiki/index.php/GlPolygonMode "GlPolygonMode"), [\_glPolygonStipple](/qb64wiki/index.php/GlPolygonStipple "GlPolygonStipple"), [\_glPushAttrib](/qb64wiki/index.php/GlPushAttrib "GlPushAttrib")
* [\_glPushMatrix](/qb64wiki/index.php/GlPushMatrix "GlPushMatrix"), [\_glPushName](/qb64wiki/index.php/GlPushName "GlPushName"), [\_glRasterPos](https://learn.microsoft.com/en-us/windows/win32/opengl/glrasterpos-functions), [\_glReadPixels](/qb64wiki/index.php/GlReadPixels "GlReadPixels")
* [\_glScissor](/qb64wiki/index.php/GlScissor "GlScissor"), [\_glShadeModel](/qb64wiki/index.php/GlShadeModel "GlShadeModel"), [\_glStencilFunc](/qb64wiki/index.php/GlStencilFunc "GlStencilFunc"), [\_glStencilMask](/qb64wiki/index.php/GlStencilMask "GlStencilMask")
* [\_glStencilOp](/qb64wiki/index.php/GlStencilOp "GlStencilOp"), [\_glTexCoord](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexcoord-functions), [\_glTexEnv](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexenv-functions), [\_glTexGen](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexgen-functions)
* [\_glTexImage1D](/qb64wiki/index.php/GlTexImage1D "GlTexImage1D"), [\_glTexImage2D](/qb64wiki/index.php/GlTexImage2D "GlTexImage2D"), [\_glViewport](/qb64wiki/index.php/GlViewport "GlViewport")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GlGetBooleanv&oldid=6876>"




## Navigation menu








### Search





















