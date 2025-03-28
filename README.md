# igcc_profiles
 Hotkeys for Intel Graphics Command Centre

 Intel has deprived users of hotkeys and APIs for its graphics control panel (IGCC) to switch user profiles, so Mr JS is rectifying the situation.

 ![Hotkeys for Intel Graphics Command Centre](/images/igcc_profiles-0.png) 

 ![Hotkeys for Intel Graphics Command Centre](/images/igcc_profiles-1.png)

 ## Features

 - Multi-language localization support
 - Custom profile names & hotkeys support

 ## Install

 1. Unpack all files to:
 ```
 C:\Program Files\igcc_profiles
 ```
 2. Run Intel Graphics Command Centre (IGCC) and create profiles. For example:
 ```
 Custom 1
 Custom 2
 Custom 3
 ```
 3. Open [config](/config.py): select your localization and setup profiles (names, hotkeys)
 4. OPTIONAL: you can set automatic hidden startup, in which case you don't need to run anything -- see the last tip at the end of the readme


 ## Usage

 1. OPTIONAL: run ``igcc_profiles`` manually (if you skipped step 4 in the installation process)
 2. Use pre-set hotkeys anywhere in the system to switch profiles


 ## Remarks
 
 > [!TIP]
 > If you experience problems (e.g., the program doesn't always trigger), try changing ``timeout`` in the [config](/config.py).

 > [!TIP]
 > If Intel Graphics Command Centre (IGCC) is not running at the time of launching the utility, the utility will find the program in the list of installed programs and launch it on its own (it will take some time). Option ``keep_alive`` in the [config](/config.py) allows you to keep the graphics control center minimized in the background, which makes it much faster to re-select a new profile.

 > [!TIP]
 > You can configure autorun and hidden execution of the utility in the background (without windows and console) for convenience, for this purpose use a combination of features of standard windows tools: [wscript.exe](/igcc_profiles.vbs) and [taskschd.msc](/igcc_profiles.xml). The screen adjustment tools in laptops work in a similar way.