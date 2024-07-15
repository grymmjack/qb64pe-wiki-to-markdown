# SHELL
> The SHELL statement allows a program to run external programs or command line statements in Windows, macOS and Linux.

## SYNTAX
`SHELL [ DOSCommand$ ]`

## DESCRIPTION
* If the DOSCommand$ [STRING](STRING.md) parameter isn't used, the "command console" is opened and execution is halted until the user closes it manually.
* If [_DONTWAIT](_DONTWAIT.md) is used, the QB64 program doesn't wait for the SHELLed program/command to end.
* When the [_HIDE](_HIDE.md) action is used, the console window is hidden and screen info can be "redirected" (using redirection characters like >) to a file (recommended).
* Commands are external commands, according to the user's operating system, passed as strings enclosed in quotes or string variables.
* Commands can be a mixture of strings and string variables added together using the + concatenation operator.
* Command text can be in upper or lower case. Use single spacing between items and options.
* QB64 automatically uses CMD /C when using [SHELL](SHELL.md) , but it is allowed in a command string. Note: CMD alone may lock up program. Note: Some commands may not work without adding CMD /C to the start of the command line.
	* Note: Some commands may not work without adding CMD /C to the start of the command line.
* Note: Some commands may not work without adding CMD /C to the start of the command line.
* QB64 program screens will not get distorted, minimized or freeze the program like QBasic fullscreen modes would.
* QB64 can use long path folder names and file names and [SHELL](SHELL.md) command lines can be longer than 124 characters.
* In Windows, use additional CHR$ (34) quotation marks around folder or file names that contain spaces.
* For other operating systems, both the quotation mark character and the apostrophe can be used to enclose a file name that contains spaces.
* NOTE: Use [CHDIR](CHDIR.md) instead of CD as [SHELL](SHELL.md) commands cannot affect the current program path.


## EXAMPLES
> Example 1: When working with file or folder names with spaces, add quotation marks around the path and/or file name with CHR$ (34).

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Example 2: Opening a Windows program (Notepad) to read or print a Basic created text file.

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```


```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Example 3: Function that returns the program's current working path.

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Example 4: Determining if a drive or path exists. Cannot use with a file name specification.

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Snippet 1: When looking for printers this command gives you a file list with the default printer marked as TRUE :

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Created file's text:

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

> Snippet 2: Here is the code to set the default printer to the "HP Officejet Pro 8600":

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

* FILELIST$ (function)
* FileExist Library Function

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```

* Featured in our "Keyword of the Day" series
* [SHELL](SHELL.md) (function) , [_SHELLHIDE](_SHELLHIDE.md)
* [FILES](FILES.md) , [CHDIR](CHDIR.md) , [MKDIR](MKDIR.md)
* _CWD$ , _STARTDIR$
* [_FILEEXISTS](_FILEEXISTS.md) , [_DIREXISTS](_DIREXISTS.md)
* [RMDIR](RMDIR.md) , [NAME](NAME.md) , [KILL](KILL.md) , [RUN](RUN.md)
* [_HIDE](_HIDE.md) , [_DONTWAIT](_DONTWAIT.md)
* [_CONSOLE](_CONSOLE.md) , $[CONSOLE](CONSOLE.md)
* $SCREENHIDE , $SCREENSHOW
* [_SCREENHIDE](_SCREENHIDE.md) , [_SCREENSHOW](_SCREENSHOW.md)
* FILELIST$ , DIR$
* Windows Open and Save Dialog Boxes
* C Console Library
* Windows Printer Settings

```vb
SHELL _HIDE "dir " + CHR$(34) + "free cell.ico" + CHR$(34) + " /b > temp.dir"
SHELL "start Notepad temp.dir" ' display temp file contents in Notepad window
```



## MORE EXAMPLES
* FILELIST$ (function)
* FileExist Library Function


# SEE ALSO
* Featured in our "Keyword of the Day" series
* [SHELL](SHELL.md) (function) , [_SHELLHIDE](_SHELLHIDE.md)
* [FILES](FILES.md) , [CHDIR](CHDIR.md) , [MKDIR](MKDIR.md)
* _CWD$ , _STARTDIR$
* [_FILEEXISTS](_FILEEXISTS.md) , [_DIREXISTS](_DIREXISTS.md)
* [RMDIR](RMDIR.md) , [NAME](NAME.md) , [KILL](KILL.md) , [RUN](RUN.md)
* [_HIDE](_HIDE.md) , [_DONTWAIT](_DONTWAIT.md)
* [_CONSOLE](_CONSOLE.md) , $[CONSOLE](CONSOLE.md)
* $SCREENHIDE , $SCREENSHOW
* [_SCREENHIDE](_SCREENHIDE.md) , [_SCREENSHOW](_SCREENSHOW.md)
* FILELIST$ , DIR$
* Windows Open and Save Dialog Boxes
* C Console Library
* Windows Printer Settings

