# Introduction

The rising sun (RS) mainspring winder is a fully functional 3D printable watch mainspring winder, with accurately calculated design files provided for every possible size imaginable. Everything provided here is free and open source. This is the modern solution to hobbyist mainspring winding woes and it comes with **absolutely zero warranty**. You are advised to thoroughly go through this README, the [wiki pages](https://github.com/vishnu350/rs-mainspring-winder/wiki), [video](https://youtu.be/EZvd_MKBOUQ) resources found here.

Watch mainspring winding for hobbyists has always been a problem, as most of us cannot afford the $1500 Bergeon set to wind vintage unbranded mainsprings/barrels. Or sometimes the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding, which may kink or damage the mainspring.

The RS mainspring winder was designed using FreeCAD+Python, and is easy to 3D print. It costs ~$10 to print a single set by most 3D print service providers. Alternatively, you may choose to just purchase a prebuilt kit from **eBay seller AndyShap2 [here](https://www.ebay.com/itm/125428348675) (single set)** or **[here](https://www.ebay.com/itm/125578735361) (complete set).**

The RS mainspring winder works very well when properly constructed. **List of features:**
- Guaranteed to work on all released sizes, since the generation process is scripted.
- Cheap and easy to print with no post-processing/finishing or support material required.
- Winds cleanly and safely, no more getting bits of skin stuck due to handwinding.
- Can wind in both directions, clockwise and counter-clockwise.
- Has knurling patterns on body for a good grip during use, along with clear size labeling.
- Mainspring will never get caught in between winder barrel and plunger due to unique design style.
- PLA/PLA+ material is tough enough to withstand the winding stress and has very low friction vs steel.
- Both PLA/PLA+ and staple pins are softer than steel, and thus it will not kink or damage the mainspring.
- Never need to worry about wearing out the arbor hooks, as [staple pins are easy to replace](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbor-Hook-for-the-Winder-Base).
- Pick any size from the generated [set of winders](https://github.com/vishnu350/rs-mainspring-winder/releases/latest/download/rs-winder.zip) (7mm-18.5mm) or [customize](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder) it yourself.

**Watch this YouTube video [here](https://youtu.be/EZvd_MKBOUQ) or [here](https://youtu.be/OAfQTk89P3s) (older) to better understand the RS winder parts and how it works.**<br/>
**Discussion/Feedback: WRT forum thread [here](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/), or GitHub discussion section [here](https://github.com/vishnu350/rs-mainspring-winder/discussions).**<br/>

<p align="center">
<img src="https://github.com/user-attachments/assets/2005ca8c-3879-42f4-be2a-23a659c61cc7" alt="drawing" width="38%"/>
<img src="https://user-images.githubusercontent.com/5123344/179362734-67d5340e-5dd6-44f6-97d1-f3182b52eb8a.jpg" alt="drawing" width="34.8%"/>
</p>

# RS Winder Parts Description
There are several parts to the RS mainspring winder:
1. **The housing barrel**. This part is the barrel that houses the mainspring and plunger, with a rising sun knurling pattern on the top for no reason.
2. **The plunger**. This part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
3. **The winder base**. This part is responsible for winding the mainspring with the help of the arbor hook.
4. **The setter bowl**. This part helps the ejection of the mainspring by a very small amount so that the actual mainspring barrel can be easily fitted in by hand (see 2nd picture above).
5. **The staple jig**. Use this part to easily cut the staple pins to form the arbor hook, watch instructional video [here](https://youtu.be/na0XtIDea9I).
6. **The arbor rod**. Get a dowel pin (or equivalent) with 1.5mm-3.0mm diameter and place it at the center of the winder base.
7. **The arbor hook**. Fashion this part out of a staple pin using the staple jig part (see [instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbor-Hook-for-the-Winder-Base)) and insert into one of the holes on the winder base part (see [guide](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbor-Hook-to-the-Mainspring)).

**NOTE:** *The arbor hook and rod are too small to be 3D printed, hence metal parts are **required**.*

# Building the RS winder
Recommended 3D printing options:
- **Material:**
   - **PLA or PLA+ is the optimal choice** for low friction parts with high accuracy printing.
   - Nylon or similar tough materials for FDM 3D printers may be used, but your mileage may vary.
   - **Avoid resin materials**, they are not recommended due to [higher surface friction](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/?do=findComment&comment=280627) vs steels.
- **Infill: 20% or more** (parts may crumble under stress if lower).
- **Layer thickness: 0.1 mm** or better.
- **Color: Any**, go with off-white if unsure. Best if all parts are of the same color for equal tolerances.
- **Printer: Any well calibrated FDM 3D printer**, best if the print job is done with high accuracy settings.
- **Placement: Widest flat surface should face downwards** on print bed for best results, applies for all parts.

Steps to build your RS mainspring winder:
1. Use a caliper to measure your mainspring barrel inner diameter and the mainspring arbor diameter.
2. Download the latest [rs-winder.zip](https://github.com/vishnu350/rs-mainspring-winder/releases/latest/download/rs-winder.zip) from the [release section](https://github.com/vishnu350/rs-mainspring-winder/releases).
   - Print your winder base part STL/3MF file. Choose from 1.5-3.0mm sizes, whichever matches your mainspring arbor the best.
   - Print your housing barrel and plunger part STL/3MF files. Size is based on mainspring barrel inner diameter, make sure to select matching sizes. In-depth winder size selection guide [here](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring).
   - Print your setter bowl part STL/3MF file, this part should universally work with all housing barrels.
   - Print your staple jig part STL file.
3. Fashion a staple pin into an arbor hook with using the staple jig (see [instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbor-Hook-for-the-Winder-Base) or watch [video](https://youtu.be/na0XtIDea9I)). Insert it into one of the holes on the winder base part (see [guide](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbor-Hook-to-the-Mainspring)).
4. Install the appropriate dowel pin for your winder base part:
   - Recommended online purchase links: [AliExpress](https://www.aliexpress.com/item/1005002177332247.html), [Amazon](https://www.amazon.com/dp/B09W5PBHGR).
   - For normal size winder base: 1.5mm/2.0mm (M1.5/M2) diameter dowel pins, 18mm in length.
   - For large size winder base: 2.5mm/3.0mm (M2.5/M3.0) diameter dowel pins, 18mm in length.
   - Using glue/epoxy for the dowel pins are optional, apply only a teeny tiny amount as needed.
5. Optionally, use a fish hook sharpener to reduce the staple pin thickness so that it will better match the mainspring hole.
   - Recomended online purchase links: [AliExpress](https://www.aliexpress.com/item/1005006607858844.html).
   - For best results, use eye magnification while working on sharpening the staple hook.
   - Remember to clean off the metal filings after sharpening the staple hook.

# Using the RS winder
Please go to the wiki for instructions: [Using the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Using-the-RS-winder), or watch a [YouTube video](https://youtu.be/EZvd_MKBOUQ).

Make sure to study the [correct staple pin latching method](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbor-Hook-to-the-Mainspring).

# Customizing/Generating the RS winder
Please go to the wiki for instructions: [Customizing & Generating the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder).

To generate the STL/3MF files for the various different sizes of all the RS winder parts, just clone this repo and execute the Python FreeCAD script using the following command:<br/>`freecadcmd generate_stl.py`

# Warnings and Advice (READ CAREFULLY!)
Please read every single sentence below carefully:
- As stated before, everything provided here comes with **ABSOLUTELY ZERO WARRANTY**.
- While this winder works great for many users, it still requires you to be resourceful and **competent in basic watchmaking skills**.
- It is recommended to **practice first with spare mainsprings/barrels** to get a feel of using the RS winder. Incorrect use can break or damage your mainspring, this is the case even with professional winders.
- Refer to the wiki for help with [**winder size selection**](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring), choosing the wrong size will damage your mainspring.
- If the printed parts are stringy, it probably means your printer is not properly calibrated. Make sure to properly clean the stringy bits before using the winder to avoid contamination.
- Be very careful when unwinding, do it slowly or risk getting the mainspring and staple pin entangled.

On winding the mainspring:
- You must be competent enough to **assess the health of the mainspring** (see [here for guidance](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring)). Tired or old mainsprings will break regardless of how expensive your tools are.
- When initially placing the housing barrel on the winder base with the latched mainspring, **do not forcefully ram the mainspring into position**. Watch the [video](https://youtu.be/OAfQTk89P3s?t=204) (min 3:24) for an simple way to do this.
- Always **manually push the mainspring's tail end** instead of forcibly winding it into the winder. This is to avoid unnecessary stress onto the arbor and mainspring eye.
- If a mainspring is **harder to wind as compared to your successfully wound practice mainsprings**, then something is wrong and you should stop immediately to asses the problem. If you are unable to determine this, then go back to practicing with spare mainsprings to get a feel.
- **Learn how to use the setter bowl part properly!** It is specifically designed for pushing out the mainspring a teeny bit **BEFORE** actually placing the mainspring barrel, and the viewhole allows you to see it pushed. Once it is slightly jutting out of the winder, placing the mainspring barrel on it is easy and it can be safely plunged.
<p align="center">
<img src="https://github.com/user-attachments/assets/dcaa3484-9426-4535-9b7f-20b19842a85c" width=25%>
<img src="https://github.com/user-attachments/assets/234f7cfe-e982-4e7a-9265-6dfcd0232555" alt="drawing" width="18.5%"/>
</p>

On using the staple pin:
- The **height of the staple pin is extremely important**, it must be trimmed correctly to fit. Make sure the staple pin height is adjusted such that the hook aligns with the hole of the mainspring, so that it will catch properly while winding.
- Always **hook the staple pin from the outside** of the mainspring to avoid issues when winding. Study the [correct staple pin latching method](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbor-Hook-to-the-Mainspring) diagrams to understand this better.
- If you are struggling to latch the staple pin to the mainspring hole, **use a [fish hook sharpener](https://www.aliexpress.com/item/1005006607858844.html) to sharpen the top half of the staple** so that it will match the size of the mainspring hole.
- If you still find the staple pin too **"fiddly"** even after sharpening it, then **learn how to steady your hands ([see article here](https://www.wikihow.com/Improve-Hand-Steadiness))**. Other movement parts such as hairsprings and jewel clips are far smaller/harder to work with compared to the staple pin, and will pose an immediate roadblock in your journey if you do not deal with it.

# Thanks & How To Contribute
If you like this work, please consider to:
- Please ⭐️ this repository if this project helped you.
- Notify me if the part links are no longer functional.
- Buy me a cup of [coffee](https://github.com/sponsors/vishnu350?frequency=one-time)

Help needed for future work:
- Support for magnet wires or steel braiding wires (staple hole all the way down) + updated jig. Possibly U shaped.
- 3D printed washer part for mainspring arbor to help reduce stress on the innermost coil while winding on the large winder sets.

Credits and thanks to the following folk:
- **AndyShap** for sharing his setter bowl and staple jig ideas, as well as refinements to the overall design. Also for providing the design files, wiki guides and video walkthroughs.
- **Yxoc** for sharing detailed step by step instructions with pictures [here](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/?do=findComment&comment=233556) to be used by the wiki guides.
- **Fred** and **aac58** for testing and contributing to the metal rod idea (now dowel pin) for the winder base during the early stages of the project.
- **Fratink** for coming up with the first 3D winder design [here](https://www.thingiverse.com/thing:3540660) in Thingiverse. While the RS winder is now very different from this version, it helped inspire the creation of this project. The same free Creative Commons licensing scheme is re-used.
- All those who tested the RS winder, gave constructive feedback, posted pictures and helped others along their watchmaking journey. Thank you.
