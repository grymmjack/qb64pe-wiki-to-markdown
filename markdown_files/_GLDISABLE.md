


\_glDisable - QB64 Phoenix Edition Wiki








# \_glDisable



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_glEnable** and **\_glDisable** statements enable or disable OpenGL capabilities.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


\_glDisable GLenum *cap*
  




## Parameters


* OpenGL is using its own set of variable types to describe its command parameters.
* Use the following table to find the respective QB64 [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types").




| ```    Table 2: Relations between the OpenGL variable types vs. C/C++ and QB64.  ┌──────────────┬────────────────┬──────────────────────────────────────────┐  │    **OpenGL**    │     **C/C++**      │     **QB64**                                 │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLenum       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLboolean    │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbitfield   │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbyte       │ signed char    │ [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                                    │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLshort      │ short          │ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                                  │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLint        │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLsizei      │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLubyte      │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLushort     │ unsigned short │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                        │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLuint       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLfloat      │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampf     │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLdouble     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampd     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLvoid   **(1)** │ void           │ [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(any fixed lenght string or [_BYTE](/qb64wiki/index.php/BYTE "BYTE") │  │              │                │         array element)                   │  └──────────────┴────────────────┴──────────────────────────────────────────┘  **Note:** If a parameter has an asterisk (*) in front, then it's a pointer to        the designated OpenGL variable type, rather than a value of that type.        Those must be passed using the [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(...) notation.   **E.g.**  GLuint *anyParam is actually the offset of a [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") (~&)        variable or array, which must be passed as [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyVar~&) or        [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyArr~&()) respectively.    **(1)**  This type is regularly only used for pointers (with asterisk (*)) to        any byte sized memory data, hence [_BYTE](/qb64wiki/index.php/BYTE "BYTE") or fixed length strings.  ``` |
| --- |


  




## Description


* OpenGL's documentation is available in several places, so we won't reproduce it here for another time.
* The full description for this command can be found at [Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/opengl/gldisable) and is also valid for QB64 usage.


  




## See also


* [SUB \_GL](/qb64wiki/index.php/GL "GL")
* [\_glAlphaFunc](/qb64wiki/index.php/GlAlphaFunc "GlAlphaFunc"), [\_glArrayElement](/qb64wiki/index.php/GlArrayElement "GlArrayElement"), [\_glBegin](/qb64wiki/index.php/GlBegin "GlBegin"), [\_glBlendFunc](/qb64wiki/index.php/GlBlendFunc "GlBlendFunc")
* [\_glClipPlane](/qb64wiki/index.php/GlClipPlane "GlClipPlane"), [\_glColorMaterial](/qb64wiki/index.php/GlColorMaterial "GlColorMaterial"), [\_glColorPointer](/qb64wiki/index.php/GlColorPointer "GlColorPointer"), [\_glCullFace](/qb64wiki/index.php/GlCullFace "GlCullFace")
* [\_glDepthFunc](/qb64wiki/index.php/GlDepthFunc "GlDepthFunc"), [\_glDepthRange](/qb64wiki/index.php/GlDepthRange "GlDepthRange"), [\_glDrawArrays](/qb64wiki/index.php/GlDrawArrays "GlDrawArrays"), [\_glEdgeFlagPointer](/qb64wiki/index.php/GlEdgeFlagPointer "GlEdgeFlagPointer")
* [\_glEnable](/qb64wiki/index.php/GlEnable "GlEnable"), [\_glEnd](/qb64wiki/index.php/GlEnd "GlEnd"), [\_glEvalCoord](https://learn.microsoft.com/en-us/windows/win32/opengl/glevalcoord-functions), [\_glEvalMesh](https://learn.microsoft.com/en-us/windows/win32/opengl/glevalmesh-functions)
* [\_glEvalPoint](https://learn.microsoft.com/en-us/windows/win32/opengl/glevalpoint), [\_glFog](https://learn.microsoft.com/en-us/windows/win32/opengl/glfog), [\_glGet](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv), [\_glIndexPointer](/qb64wiki/index.php/GlIndexPointer "GlIndexPointer")
* [\_glIsEnabled](/qb64wiki/index.php/GlIsEnabled "GlIsEnabled"), [\_glLight](https://learn.microsoft.com/en-us/windows/win32/opengl/gllight-functions), [\_glLightModel](https://learn.microsoft.com/en-us/windows/win32/opengl/gllightmodel-functions), [\_glLineWidth](/qb64wiki/index.php/GlLineWidth "GlLineWidth")
* [\_glLineStipple](/qb64wiki/index.php/GlLineStipple "GlLineStipple"), [\_glLogicOp](/qb64wiki/index.php/GlLogicOp "GlLogicOp"), [\_glMap1](https://learn.microsoft.com/en-us/windows/win32/opengl/glmap1), [\_glMap2](https://learn.microsoft.com/en-us/windows/win32/opengl/glmap2)
* [\_glMaterial](https://learn.microsoft.com/en-us/windows/win32/opengl/glmaterial-functions), [\_glNormal](https://learn.microsoft.com/en-us/windows/win32/opengl/glnormal-functions), [\_glNormalPointer](/qb64wiki/index.php/GlNormalPointer "GlNormalPointer"), [\_glPointSize](/qb64wiki/index.php/GlPointSize "GlPointSize")
* [\_glPolygonMode](/qb64wiki/index.php/GlPolygonMode "GlPolygonMode"), [\_glPolygonStipple](/qb64wiki/index.php/GlPolygonStipple "GlPolygonStipple"), [\_glScissor](/qb64wiki/index.php/GlScissor "GlScissor"), [\_glStencilFunc](/qb64wiki/index.php/GlStencilFunc "GlStencilFunc")
* [\_glStencilOp](/qb64wiki/index.php/GlStencilOp "GlStencilOp"), [\_glTexCoordPointer](/qb64wiki/index.php/GlTexCoordPointer "GlTexCoordPointer"), [\_glTexGen](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexgen-functions), [\_glTexImage1D](/qb64wiki/index.php/GlTexImage1D "GlTexImage1D")
* [\_glTexImage2D](/qb64wiki/index.php/GlTexImage2D "GlTexImage2D")


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GlDisable&oldid=6840>"




## Navigation menu








### Search





















