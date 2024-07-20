## QB.BI
---

### The QB.BI file can be used for INTERRUPT or INTERRUPTX routines by $INCLUDEing the file in a program. It is useful for the TYPE and SUB declarations.

#### SYNTAX

`The QB.BI file contents:`

#### DESCRIPTION
* Create your own BI files to $INCLUDE to hold your own [TYPE](./TYPE.md) definitions. Use notepad and save as All Files as filename.BI
* In QBasic the BI library or support file MUST be included in a program package or download!
* QB64 programs do not require any INCLUDED files once the BAS file is compiled!


#### EXAMPLES
```vb
'**************************************************************************
' QB.BI - Assembly Support Include File
'
' Copyright (C) 1987 Microsoft Corporation
'
' Purpose:
'      This include file defines the types and gives the DECLARE
'       statements for the assembly language routines CALL ABSOLUTE,
'       INTERRUPT, INTERRUPTX, INT86OLD, and INT86XOLD.
'
'***************************************************************************
'
' Define the TYPE needed for INTERRUPT
'
TYPE RegType
  ax    AS INTEGER
  bx    AS INTEGER
  cx    AS INTEGER
  dx    AS INTEGER
  bp    AS INTEGER
  si    AS INTEGER
  di    AS INTEGER
  flags AS INTEGER
END TYPE
'
' Define the TYPE needed for INTERRUPTX
'
TYPE RegTypeX
  ax    AS INTEGER
  bx    AS INTEGER
  cx    AS INTEGER
  dx    AS INTEGER
  bp    AS INTEGER
  si    AS INTEGER
  di    AS INTEGER
  flags AS INTEGER
  ds    AS INTEGER
  es    AS INTEGER
END TYPE
'
' DECLARE statements for the 5 supported routines
' -----------------------------------------
'
' Generate a software interrupt, loading all but the segment registers
'
DECLARE SUB INTERRUPT (intnum AS INTEGER, inreg AS RegType, outreg AS RegType)
'
' Generate a software interrupt, loading all registers
'
DECLARE SUB INTERRUPTX (intnum AS INTEGER, inreg AS RegTypeX, outreg AS RegTypeX)
'
' Call a routine at an absolute address.
' NOTE: If the routine called takes parameters, then they will have to
'       be added to this declare statement before the parameter given.
'
DECLARE SUB ABSOLUTE (address AS INTEGER)
'
' Generate a software interrupt, loading all but the segment registers
'       (old version)
'
DECLARE SUB INT86OLD (intnum AS INTEGER, inarray(1) AS INTEGER, outarray(1) AS INTEGER)
'
' Gemerate a software interrupt, loading all the registers
'       (old version)
'
DECLARE SUB INT86XOLD (intnum AS INTEGER, inarray(1) AS INTEGER, outarray(1) AS INTEGER)
```
  
```vb
TYPE RegType
  ax AS INTEGER
  bx AS INTEGER
  cx AS INTEGER
  dx AS INTEGER
  bp AS INTEGER
  si AS INTEGER
  di AS INTEGER
  flags AS INTEGER
  ds AS INTEGER
  es AS INTEGER
END TYPE
```
  


#### SEE ALSO
* $INCLUDE , [INTERRUPT](./INTERRUPT.md) , [INTERRUPTX](./INTERRUPTX.md)
