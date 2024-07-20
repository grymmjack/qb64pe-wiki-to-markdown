## VIEW PRINT
---

### The VIEW PRINT statement defines the boundaries of a text viewport PRINT area.

#### SYNTAX

`VIEW PRINT [ topRow% TO bottomRow% ]`

#### PARAMETERS
* topRow% and bottomRow% specify the upper and lower rows of the text viewport.
* If topRow% and bottomRow% are not specified when first used, the text viewport is defined to be the entire screen.


#### DESCRIPTION
* A second [VIEW](./VIEW.md) [PRINT](./PRINT.md) statement without parameters can also disable a viewport when no longer needed.
* [CLS](./CLS.md) or [CLS](./CLS.md) 2 statement will clear the active text viewport area only, and reset the cursor location to topRow% .
* A [SCREEN](./SCREEN.md) mode change or [RUN](./RUN.md) statement can also clear and disable viewports.
* After active viewport is disabled, normal screen printing and clearing can begin.
* Row coordinates may vary when a [WIDTH](./WIDTH.md) statement has been used.
* Note: QB64 [RUN](./RUN.md) statements will not close [VIEW](./VIEW.md) [PRINT](./PRINT.md) , [VIEW](./VIEW.md) or [WINDOW](./WINDOW.md) view ports presently!


#### SEE ALSO
* Featured in our "Keyword of the Day" series
* [CLS](./CLS.md)
* [WINDOW](./WINDOW.md)
* [VIEW](./VIEW.md)
* [LOCATE](./LOCATE.md) , [PRINT](./PRINT.md)
