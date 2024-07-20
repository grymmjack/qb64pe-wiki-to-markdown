## PALETTE USING
---

### The PALETTE USING statement sets all RGB screen color intensities using values from an array .

#### SYNTAX

`PALETTE USING array%( startIndex% )`

#### DESCRIPTION
* The array holds the RGB color value using the color value as red% + 256 * green% + 65536 * blue% .
	* Color intensities range from 0 to 63.
* startIndex% indicates the index in the array from which the statement should start reading. The statement will read all color attributes available in that [SCREEN](./SCREEN.md) mode. The number of values required in the array is listed below:


#### SEE ALSO
* [PALETTE](./PALETTE.md) , [COLOR](./COLOR.md)
* [_PALETTECOLOR](./_PALETTECOLOR.md)
* [SCREEN](./SCREEN.md)
