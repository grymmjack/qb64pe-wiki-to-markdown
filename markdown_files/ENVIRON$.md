# ENVIRON$
> The ENVIRON$ function returns a STRING environmental value from Windows' environmental settings list.

## SYNTAX
`setting$ = ENVIRON$ ({ listIndex% | systemID$ })`

## DESCRIPTION
* The function can use an [INTEGER](INTEGER.md) listIndex% value or [STRING](STRING.md) systemID$ parameter.
* listIndex% refers to the number order of the environmental list. Returns are not in any particular numerical order.
* systemID$ is the specific [STRING](STRING.md) parameter requested. Returns only the specified environmental [STRING](STRING.md) setting: "BLASTER" = current Sound Blaster settings if installed. "COMPUTERNAME" or "USERDOMAIN" = OEM PC serial number or the computer name assigned by owner. "HOMEDRIVE" or "SystemDrive" = Windows root drive, normally C: on single partition drives. "HOMEPATH" = current user's Administrator or the single user's "OWNER" folder path. "OS" = Windows Operating System version. Often WindowsNT in modern computers. "PATH" = full path setting that Windows uses to look for file extensions in PATHEXT below. "PATHEXT = Windows extensions used:  [COM](COM.md), EXE, BAT, CMD, VBS, VBE, JS, JSE, WSF, WSH, MSC "PROCESSOR_ARCHITECTURE" = x86 for 32 or 64 bit. "PROGRAMFILES" = path to Program files folder, normally "C:\PROGRAM [FILES](FILES.md)" "PROMPT" = normally "$P$G" on Windows NT. "SYSTEMROOT" or "windir" = path to the Windows folder including the drive letter like "C:\WINDOWS" "TEMP" or "TMP" = path to TEMP folder. "C:\TEMP" or the user specific temp folder on later versions. "USERNAME" = current Administrator name or "OWNER".
	* "BLASTER" = current Sound Blaster settings if installed.
	* "COMPUTERNAME" or "USERDOMAIN" = OEM PC serial number or the computer name assigned by owner.
	* "HOMEDRIVE" or "SystemDrive" = Windows root drive, normally C: on single partition drives.
	* "HOMEPATH" = current user's Administrator or the single user's "OWNER" folder path.
	* "OS" = Windows Operating System version. Often WindowsNT in modern computers.
	* "PATH" = full path setting that Windows uses to look for file extensions in PATHEXT below.
	* "PATHEXT = Windows extensions used:  [COM](COM.md), EXE, BAT, CMD, VBS, VBE, JS, JSE, WSF, WSH, MSC
	* "PROCESSOR_ARCHITECTURE" = x86 for 32 or 64 bit.
	* "PROGRAMFILES" = path to Program files folder, normally "C:\PROGRAM [FILES](FILES.md)"
	* "PROMPT" = normally "$P$G" on Windows NT.
	* "SYSTEMROOT" or "windir" = path to the Windows folder including the drive letter like "C:\WINDOWS"
	* "TEMP" or "TMP" = path to TEMP folder. "C:\TEMP" or the user specific temp folder on later versions.
	* "USERNAME" = current Administrator name or "OWNER".
* "BLASTER" = current Sound Blaster settings if installed.
* "COMPUTERNAME" or "USERDOMAIN" = OEM PC serial number or the computer name assigned by owner.
* "HOMEDRIVE" or "SystemDrive" = Windows root drive, normally C: on single partition drives.
* "HOMEPATH" = current user's Administrator or the single user's "OWNER" folder path.
* "OS" = Windows Operating System version. Often WindowsNT in modern computers.
* "PATH" = full path setting that Windows uses to look for file extensions in PATHEXT below.
* "PATHEXT = Windows extensions used:  [COM](COM.md), EXE, BAT, CMD, VBS, VBE, JS, JSE, WSF, WSH, MSC
* "PROCESSOR_ARCHITECTURE" = x86 for 32 or 64 bit.
* "PROGRAMFILES" = path to Program files folder, normally "C:\PROGRAM [FILES](FILES.md)"
* "PROMPT" = normally "$P$G" on Windows NT.
* "SYSTEMROOT" or "windir" = path to the Windows folder including the drive letter like "C:\WINDOWS"
* "TEMP" or "TMP" = path to TEMP folder. "C:\TEMP" or the user specific temp folder on later versions.
* "USERNAME" = current Administrator name or "OWNER".


## EXAMPLES
> Example 1: Viewing the list of environmental parameter settings using a counter loop like SET does in DOS.

```vb
DO
 i = i + 1
 setting$ = ENVIRON$(i) ' get a setting from the list
 PRINT setting$
 IF i MOD 20 = 0 THEN PRINT "Press a key": SLEEP: CLS
LOOP UNTIL setting$ = ""
```

> Example 2: Creating a shortcut on a user's desktop for QB64.EXE using the program's icon. Must be run in program's folder to work!

```vb
DO
 i = i + 1
 setting$ = ENVIRON$(i) ' get a setting from the list
 PRINT setting$
 IF i MOD 20 = 0 THEN PRINT "Press a key": SLEEP: CLS
LOOP UNTIL setting$ = ""
```


```vb
DO
 i = i + 1
 setting$ = ENVIRON$(i) ' get a setting from the list
 PRINT setting$
 IF i MOD 20 = 0 THEN PRINT "Press a key": SLEEP: CLS
LOOP UNTIL setting$ = ""
```

* [ENVIRON](ENVIRON.md) (statement)
* [_DEVICES](_DEVICES.md) , _DEVICE$
* [_LASTBUTTON](_LASTBUTTON.md) , _OS$
* Windows Environment
* Windows User Paths Library

```vb
DO
 i = i + 1
 setting$ = ENVIRON$(i) ' get a setting from the list
 PRINT setting$
 IF i MOD 20 = 0 THEN PRINT "Press a key": SLEEP: CLS
LOOP UNTIL setting$ = ""
```



# SEE ALSO
* [ENVIRON](ENVIRON.md) (statement)
* [_DEVICES](_DEVICES.md) , _DEVICE$
* [_LASTBUTTON](_LASTBUTTON.md) , _OS$
* Windows Environment
* Windows User Paths Library

