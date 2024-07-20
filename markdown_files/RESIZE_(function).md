## _RESIZE (function)
---

### The _RESIZE function returns true (-1) when a user has attempted to resize the program window and $RESIZE :ON has allowed it.

#### SYNTAX

`IF _RESIZE THEN rx& = _RESIZEWIDTH : ry& = _RESIZEHEIGHT`

#### DESCRIPTION
* The function returns -1 if a program screen resize was attempted by the user.
* After the function returns -1, [_RESIZEWIDTH](./_RESIZEWIDTH.md) and [_RESIZEHEIGHT](./_RESIZEHEIGHT.md) can return the new requested dimensions in pixels.
* The $RESIZE :[ON](./ON.md) metacommand must be used so the program is created with a user resizable window.


#### EXAMPLES
##### Example: Resize the current screen image according to user's request.
```vb
$RESIZE:ON

s& = _NEWIMAGE(300, 300, 32)
SCREEN s&

bee& = _LOADIMAGE("qb64_trans.png") 'any image

DO
   IF _RESIZE THEN
       oldimage& = s&
       s& = _NEWIMAGE(_RESIZEWIDTH, _RESIZEHEIGHT, 32)
       SCREEN s&
       _FREEIMAGE oldimage&
   END IF

   CLS

   'Center the QB64 bee image:
   x = _WIDTH / 2 - _WIDTH(bee&) / 2
   y = _HEIGHT / 2 - _HEIGHT(bee&) / 2
   _PUTIMAGE (x, y), bee&
   _DISPLAY
   _LIMIT 30
LOOP
```
  


#### SEE ALSO
* $RESIZE
* [_RESIZE](./_RESIZE.md)
* [_RESIZEWIDTH](./_RESIZEWIDTH.md) , [_RESIZEHEIGHT](./_RESIZEHEIGHT.md)
