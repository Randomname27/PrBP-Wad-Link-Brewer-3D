<img height="256" alt="prbpwadlinkbrewer3d" src="https://github.com/user-attachments/assets/7da66f15-ab89-4c84-9e3f-5c93cce1c3e0" />

this is a shitty python script to generate xml shortcuts to PrBoom+ Wads for homebrew launcher

# Requirements
3DS
- [CFW (Custom Firmware)](https://3ds.hacks.guide/)
- Homebrew Launcher 
- [PrBoom+](https://gbatemp.net/threads/release-prboom-3ds-port-gpu-accelerated.636076/) in 3dsx format in the 3ds folder _(also on Universal Updater)_

PC
- Python 3
- Tkinter (Python)

# How to use and stuff

**_IT CREATES THE XML FILE IN THE SAME DIRECTORY AS THE MAIN.PY FILE_**

**Ultimate Doom** - pick if the wad will use doom.wad

**Doom 2** - pick if the wad will use doom2.wad

**Wad Name** - this will be what the title of the homebrew shortcut will be
it also has the doom version at the start

_(EXAMPLE: DOOM 2 CRAZY WEAPONS WAD)_

**Wad Description** - this will be the description of the shortcut

**_(DONT MAKE TOO LONG OR IT WILL LOOK LIKE SHIT IN THE HOMEBREW LAUNCHER)_**

**Wad Author** - will be the author of the mod (leave blank if you dont care)

**Wad file** - this will be the wad file that you will use, the wad has to be in the 3ds directory (or a folder inside, if it is you will have to specify path **_OTHERWISE IT WILL LOOK IN ROOT OF /3ds_**

_EXAMPLE: mydoomwads/mod.wad_ <- *Will look in ***sdmc:/3ds/mydoomwads/mod.wad****

**IWad Path** - what folder the iwad *(doom.wad or doom2.wad)* is located

**_(leave blank if in root of /3ds)_**

*EXAMPLE: prboomiwads/*



**This is an example of what it should look like when you're done**

<img height="256" alt="prbpwadlinkbrewer3d" src="https://github.com/user-attachments/assets/ca2471bb-752f-4549-b94f-9db76f2ff49d" /> 
