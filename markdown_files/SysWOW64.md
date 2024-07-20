## SysWOW64
---

### This can be somewhat confusing, but the System32 folder is intended for 64-bit files and the SysWOW64 folder is intended for 32-bit files . This may seem a bit illogical if you look at the folder names, but there is an explanation to this. It has to do with compatibility. Many developers have hard coded the system folder path name in their applications source code and to preserve compatibility, if the application is converted to 64-bit code, the 64-bit system folder is still named System32.
