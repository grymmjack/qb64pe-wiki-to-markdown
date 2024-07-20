## Images
---

### Images are areas of graphics stored in memory, the most common image is the program screen itself, where graphics are displayed. This image is designated as image handle 0 or _DEST 0. QB64 refers to the image memory by using negative LONG handle values. Those values can then be referred to using other functions such as _WIDTH and _HEIGHT to find the image properties. Statements like SCREEN or _PUTIMAGE can use the image handle to display the image when necessary. QBasic functions like POINT can read the colors, even 32 bit _ALPHA colors.
