## _SNDOPEN-v0.954
---

### 

#### SYNTAX

`sound_handle& = _SNDOPEN ( filename$ [, "[VOL][,][SYNC][,][LEN][,][PAUSE][,][SETPOS]"])`

#### DESCRIPTION
* Sound file support for: WAV, OGG, AIFF, RIFF, VOC, MP3, [MOD](./MOD.md), MIDI
* Capabilities of VOL, [LEN](./LEN.md), SYNC, SETPOS and PAUSE is a string of parameters separated by commas. It is [NOT](./NOT.md) case sensitive.
* The value returned by [_SNDOPEN](./_SNDOPEN.md) is a handle to the sound or 0. A zero return means the sound could [NOT](./NOT.md) be loaded. ALWAYS check the handle value returned before attempting to play them!
* The handle can be used by most of the SND sound playing Functions and Subs in QB64 except [_SNDPLAYFILE](./_SNDPLAYFILE.md) which plays a sound file name directly and does not use a handle value.
* Handles can be closed with [_SNDCLOSE](./_SNDCLOSE.md) when the sound is no longer necessary.
* An ILLEGAL [FUNCTION](./FUNCTION.md) [CALL](./CALL.md) error message means the capabilities$ string was invalid or two NON-SYNC sounds are using the same channel!


#### SEE ALSO
* [_SNDCLOSE](./_SNDCLOSE.md) , [_SNDPLAY](./_SNDPLAY.md) , [_SNDSTOP](./_SNDSTOP.md)
* [_SNDPAUSE](./_SNDPAUSE.md) , [_SNDLOOP](./_SNDLOOP.md) , [_SNDLIMIT](./_SNDLIMIT.md)
* [_SNDSETPOS](./_SNDSETPOS.md) , [_SNDGETPOS](./_SNDGETPOS.md)
* [_SNDPLAYING](./_SNDPLAYING.md) , [_SNDPAUSED](./_SNDPAUSED.md)
* [_SNDCOPY](./_SNDCOPY.md) , [_SNDPLAYCOPY](./_SNDPLAYCOPY.md)
* [_SNDBAL](./_SNDBAL.md) , [_SNDLEN](./_SNDLEN.md) , [_SNDVOL](./_SNDVOL.md)
* [_SNDPLAYFILE](./_SNDPLAYFILE.md)
* [_SNDRAW](./_SNDRAW.md) , [_SNDRATE](./_SNDRATE.md) , [_SNDRAWLEN](./_SNDRAWLEN.md)
