## OPEN COM
---

### The OPEN COM statement is used to access a computer's serial port COM.

#### SYNTAX

`OPEN "COMn: Speed , Parity , Bits , Stopbit , [ Options ]" [FOR { RANDOM | BINARY | OUTPUT | INPUT }] AS # P [LEN = byteSize ]`

#### PARAMETERS
* Speed (baud rate): 50, 150, 300, 600, 1200, 1800, 2400, 9600 (QBasic's maximum), 19200 or 115200 ( QB64' s maximum).
* Parity : N (none), E (even), O (odd), S (space) or M (mark). Note: If 8 bits, use parity N for numerical data.
* Bits = number of bits/byte: Valid numbers: 5, 6, 7 or 8
* Stopbit = number of stop bits: Valid numbers: 1 , 1.5 or 2
* Optional [COM](./COM.md) port Options (separated by commas):


#### DESCRIPTION
* If any optional CD, CS, DS or OP timeouts occur the [OPEN](./OPEN.md) will fail or port access will stop. Try 0 to ignore.
* QB64 can open any [COM](./COM.md) n port number from 1 to 9.
* See Windows System Device Manager for [COM](./COM.md) port numbers and port addresses &H3F8, &H2F8, &H3E8 and &H2E8.
* Four commas are required after the Speed, Parity, Bits, and Stopbit, even if none of the Options are used.
* Other [OPEN](./OPEN.md) options are optional and in any order separated by commas within the [OPEN](./OPEN.md) command string .(See list below)
* The optional [FOR](./FOR.md) access mode can be [OUTPUT](./OUTPUT.md) , [INPUT](./INPUT.md) or [RANDOM](./RANDOM.md) (default mode when no [FOR](./FOR.md) statement is used).
* Currently, QB64 only supports [OPEN](./OPEN.md) [FOR](./FOR.md) [RANDOM](./RANDOM.md) access using the [GET](./GET.md) / [PUT](./PUT.md) commands in BIN mode.
* Use the BIN option listed below for [BINARY](./BINARY.md) byte mode port access.
* The [LEN](./LEN.md) statement is also optional. The default record size is 512 bytes when not used.
* Use the [LOC](./LOC.md) (portnumber) function to determine that there is data in the receive buffer when the value is greater than 0.
* [OPEN](./OPEN.md) [AS](./AS.md) number can use a [FREEFILE](./FREEFILE.md) value. Numbers used by files already open cannot be used by [OPEN](./OPEN.md) [COM](./COM.md).
* Keyword not supported in Linux or macOS versions


#### EXAMPLES
##### Example 1: Checking to see if a COM port exists. If the port does not exist QBasic will cause a Windows access error.
```vb
ON ERROR GOTO Handler
FF = FREEFILE
comPort$ = "COM1:"                         'try a COM port number that does not exist
CONST comMode$ = "9600,N,8,1,CS0,DS0"      'Use 0 to avoid timeouts
OPEN comPort$ + comMode$ FOR RANDOM AS FF
IF errnum = 0 THEN PRINT "COM exists!

K$ = INPUT$(1)
END

Handler:
errnum = ERR
PRINT "Error:"; errnum
RESUME NEXT
```
  
##### Example 2: Opening a COM port with the BIN, CS0 and DS0 options in QB64 .
```vb
DIM bytestr AS STRING * 1  'one byte transfers
INPUT "COM port number #", port$  'any COM port number available

OPEN "COM" + port$ + ":9600,N,8,1,BIN,CS0,DS0" FOR RANDOM AS #1
DO 'main loop
   'receive data in buffer when LOC > 0
   IF LOC(1) THEN
      GET #1, , bytestr
      PRINT "[" + bytestr + "]";
   END IF
   'transmit (send)
   k$ = INKEY$
   IF LEN(k$) = 1 THEN
      k = ASC(k$)
      IF k >= 32 THEN     'ignore control key codes
          PRINT ">" + k$ + "<";
          bytestr = k$: PUT #1, , bytestr
      END IF
   END IF
LOOP UNTIL k$ = CHR$(27)
CLOSE #1: PRINT "Finished!"
```
  
##### Example 3: Sending string data from one COM port to another requires predefined length strings:
```vb
DIM SHARED ByteIn AS STRING * 1 'One byte transfers
DIM SHARED Byte4 AS STRING * 4 'Four byte transfers

Byte4 = CHR$(254) + CHR$(175) + CHR$(0) + CHR$(3) 'Command code to query all 4 banks of switch input board.

OPEN "COM1:115200,N,8,1,BIN,CS0,DS0" FOR RANDOM AS #1 'Open port used to send commands.
OPEN "COM2:115200,N,8,1,BIN,CS0,DS0" FOR RANDOM AS #2 'Open port used to receive commands.

PUT #1, , Byte4 'Send the 4 byte command.

Start# = TIMER
DO UNTIL LOC(2) <> 0 'Check if there is data received at com2
   IF TIMER - Start# > .5 THEN EXIT DO 'Exit loop if no data arrives within .5 seconds.
LOOP

IF LOC(2) = 0 THEN 'If no data was received.....
   PRINT "No data received from COM port."
   END
END IF

PRINT "Received from COM2:";

DO UNTIL LOC(2) = 0 'Read data from COM2 until there is no more data.
   GET #2, , ByteIn
   PRINT ASC(ByteIn);
LOOP
END
```
  


#### SEE ALSO
* [BINARY](./BINARY.md) , [RANDOM](./RANDOM.md)
* [INPUT](./INPUT.md)$ , [PRINT](./PRINT.md) #
* [LOC](./LOC.md) , INKEY$ , [OPEN](./OPEN.md)
* [GET](./GET.md) # , [PUT](./PUT.md) #
* Port Access Libraries
* Enumerating Windows Ports
