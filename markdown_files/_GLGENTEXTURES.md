


\_glGenTextures - QB64 Phoenix Edition Wiki








# \_glGenTextures



From QB64 Phoenix Edition Wiki



[Jump to navigation](#mw-head)
[Jump to search](#searchInput)
The **\_glGenTextures** statement generates texture names.


  






| Contents * [1 Syntax](#Syntax) * [2 Parameters](#Parameters) * [3 Description](#Description) * [4 See also](#See_also) |
| --- |


## Syntax


\_glGenTextures GLsizei *n*, GLuint *\*textures*
  




## Parameters


* OpenGL is using its own set of variable types to describe its command parameters.
* Use the following table to find the respective QB64 [Variable Types](/qb64wiki/index.php/Variable_Types "Variable Types").




| ```    Table 2: Relations between the OpenGL variable types vs. C/C++ and QB64.  ┌──────────────┬────────────────┬──────────────────────────────────────────┐  │    **OpenGL**    │     **C/C++**      │     **QB64**                                 │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLenum       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLboolean    │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbitfield   │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLbyte       │ signed char    │ [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                                    │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLshort      │ short          │ [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                                  │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLint        │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLsizei      │ int            │ [LONG](/qb64wiki/index.php/LONG "LONG")                                     │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLubyte      │ unsigned char  │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [_BYTE](/qb64wiki/index.php/BYTE "BYTE")                          │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLushort     │ unsigned short │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [INTEGER](/qb64wiki/index.php/INTEGER "INTEGER")                        │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLuint       │ unsigned int   │ [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG")                           │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLfloat      │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampf     │ float          │ [SINGLE](/qb64wiki/index.php/SINGLE "SINGLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLdouble     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLclampd     │ double         │ [DOUBLE](/qb64wiki/index.php/DOUBLE "DOUBLE")                                   │  ├──────────────┼────────────────┼──────────────────────────────────────────┤  │ GLvoid   **(1)** │ void           │ [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(any fixed lenght string or [_BYTE](/qb64wiki/index.php/BYTE "BYTE") │  │              │                │         array element)                   │  └──────────────┴────────────────┴──────────────────────────────────────────┘  **Note:** If a parameter has an asterisk (*) in front, then it's a pointer to        the designated OpenGL variable type, rather than a value of that type.        Those must be passed using the [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(...) notation.   **E.g.**  GLuint *anyParam is actually the offset of a [_UNSIGNED](/qb64wiki/index.php/UNSIGNED "UNSIGNED") [LONG](/qb64wiki/index.php/LONG "LONG") (~&)        variable or array, which must be passed as [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyVar~&) or        [_OFFSET](/qb64wiki/index.php/OFFSET "OFFSET")(anyArr~&()) respectively.    **(1)**  This type is regularly only used for pointers (with asterisk (*)) to        any byte sized memory data, hence [_BYTE](/qb64wiki/index.php/BYTE "BYTE") or fixed length strings.  ``` |
| --- |


  




## Description


* OpenGL's documentation is available in several places, so we won't reproduce it here for another time.
* The full description for this command can be found at [Microsoft Docs](https://learn.microsoft.com/en-us/windows/win32/opengl/glgentextures) and is also valid for QB64 usage.


  




## See also


* [SUB \_GL](/qb64wiki/index.php/GL "GL")
* [\_glBegin](/qb64wiki/index.php/GlBegin "GlBegin"), [\_glBindTexture](/qb64wiki/index.php/GlBindTexture "GlBindTexture"), [\_glDeleteTextures](/qb64wiki/index.php/GlDeleteTextures "GlDeleteTextures"), [\_glEnd](/qb64wiki/index.php/GlEnd "GlEnd")
* [\_glGet](https://learn.microsoft.com/en-us/windows/win32/opengl/glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv), [\_glGetTexParameter](https://learn.microsoft.com/en-us/windows/win32/opengl/glgettexparameter), [\_glIsTexture](/qb64wiki/index.php/GlIsTexture "GlIsTexture"), [\_glTexImage1D](/qb64wiki/index.php/GlTexImage1D "GlTexImage1D")
* [\_glTexImage2D](/qb64wiki/index.php/GlTexImage2D "GlTexImage2D"), [\_glTexParameter](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexparameter-functions)


  






---


**Navigation:**
[Main Page with Articles and Tutorials](/qb64wiki/index.php/Main_Page "Main Page")
[Keyword Reference - Alphabetical](/qb64wiki/index.php/Keyword_Reference_-_Alphabetical "Keyword Reference - Alphabetical")
[Keyword Reference - By usage](/qb64wiki/index.php/Keyword_Reference_-_By_usage "Keyword Reference - By usage")
**[Report a broken link](https://qb64phoenix.com/forum/showthread.php?tid=2800)**  





Retrieved from "<https://qb64phoenix.com/qb64wiki/index.php?title=GlGenTextures&oldid=6875>"




## Navigation menu








### Search





















