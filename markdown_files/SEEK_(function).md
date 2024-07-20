## SEEK (function)
---

### The SEEK function returns the byte or record position in a file, which is read or written next.

#### SYNTAX

`byte = SEEK ( filenumber& )`

#### PARAMETERS
* filenumber& is the number of an [OPEN](./OPEN.md) file in any mode.
* In [RANDOM](./RANDOM.md) files [SEEK](./SEEK.md) returns the record position to read or write.
* In [BINARY](./BINARY.md) or sequencial files [SEEK](./SEEK.md) returns the byte position to read or write (first byte = 1).
* Since the first file position is 1 it may require adding one to an offset value when documentation uses that position as 0.
* Devices that do not support [SEEK](./SEEK.md) (SCRN, CONS, KBRD, COMn and LPTn) return 0.


#### EXAMPLES
```vb
OPEN "readme.md" FOR BINARY AS #1

PRINT LOC(1) 'LOC returns 0, as we didn't read something yet
PRINT SEEK(1) 'SEEK otherwise returns 1, as it's the first byte to read

GET #1, , a& 'now let's read a LONG (4 bytes)

PRINT LOC(1) 'now LOC returns 4, the last read byte
PRINT SEEK(1) 'and SEEK returns 5 now, the next byte to read

CLOSE #1
END
```
  
```vb
0
1
4
5
```
  


#### SEE ALSO
* [SEEK](./SEEK.md) , [LOC](./LOC.md)
* [GET](./GET.md) , [PUT](./PUT.md)
