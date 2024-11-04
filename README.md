# igcc_profiles
 Hotkeys for Intel Graphics Command Centre

 Intel has deprived users of hotkeys and APIs for its graphics control panel (IGCC) to switch user profiles, so Mr JS is rectifying the situation.

 ![Hotkeys for Intel Graphics Command Centre](/images/igcc_profiles-0.png) 

 ![Hotkeys for Intel Graphics Command Centre](/images/igcc_profiles-1.png)

 ## Install

 1. Run Intel Graphics Command Centre (IGCC) and create profiles "Пользовательский 1", "Пользовательский 2", "Пользовательский 3" (it only has to be done once)

 ## Usage

 1. Run igcc_profiles
 2. Use Ctrl + Alt + [1, 2, 3, 0] anywhere in the system

 ## Remarks

 > [!TIP]
 > If Intel Graphics Command Centre (IGCC) is not running at the time of launching the utility, the utility will find the program in the list of installed programs and launch it on its own (it will take some time).

 > [!WARNING]
 > Right now it's only for russian localization (RU) installed from Window Store: Центр управления графикой Intel® (1.100.5635.0).
 
 > [!IMPORTANT]
 > If you experience problems (e.g., the program doesn't always trigger), try changing time.sleep and timeout in the source code.

