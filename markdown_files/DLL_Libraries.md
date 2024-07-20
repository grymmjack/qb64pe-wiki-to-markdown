## DLL Libraries
---

### QB64 supports some DLL Library statements and functions. Currently the specified DLL file MUST either be in the Windows System folder (System32) or in the QB64 folder! NOTE: Use them at your own risk! QB64 CANNOT provide specific DLL Library information or support! When using unsupported DLL files use DECLARE DYNAMIC LIBRARY and the name of an inactive library without the .DLL extension. The following statement and function routine examples have been provided by members AS IS:

#### EXAMPLES
##### Example 1: This example plays Midi files using the playmidi32.dll documented here: Liberty Basic University . Download the following DLL file to your main QB64 folder: PlayMidi32.dll
```vb
DECLARE DYNAMIC LIBRARY "playmidi32"
   FUNCTION PlayMIDI& (filename AS STRING)
END DECLARE
result = PlayMIDI(".\samples\qb64\original\ps2battl.mid" + CHR$(0))
PRINT result
```
  


#### SEE ALSO
* [DECLARE](./DECLARE.md) [LIBRARY](./LIBRARY.md) , [BYVAL](./BYVAL.md)
* [_OFFSET](./_OFFSET.md) , [_OFFSET](./_OFFSET.md) (function) (lp, ptr and p names)
* C Libraries , Windows Libraries
* C++ Variable Types
* Port Access Libraries ([COM](./COM.md) or LPT)
