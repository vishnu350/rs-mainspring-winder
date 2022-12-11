# Introduction
This project helps watchmaking hobbyists build 3D printable "Rising Sun" mainspring winders for every possible size imaginable. Everything provided here is free and open source. This is the modern solution to hobbyist mainspring winding woes and it comes with **absolutely zero warranty**. You are advised to thouroughly go through this README, the [wiki pages](https://github.com/vishnu350/rs-mainspring-winder/wiki), and [video](https://youtu.be/EZvd_MKBOUQ) resources found here.

Watch mainspring winding for hobbyists has always been a problem, as most of us cannot afford the $1500 Bergeon set to wind vintage unbranded mainsprings/barrels. Or sometimes, the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding or other similar stunts, which will definitely kink or damage the mainspring.

The RS mainspring winder was designed using FreeCAD+Python, and is easy to 3D print. It will cost $10 to print a single set (approximately) by most 3D print service providers. Alternatively, you may choose to just purchase a prebuilt kit from **eBay seller AndyShap2 [here](https://www.ebay.com/itm/125428348675) (single set)** or **[here](https://www.ebay.com/itm/125578735361) (complete set).**

The RS mainspring winder works very well when properly constructed. **List of features:**
- Guaranteed to work on all released sizes, since the build process is automated.
- Cheap and easy to print with no post-processing/finishing or support material required.
- PLA/PLA+ materials are softer than steel, and thus will not kink or damage the mainspring.
- PLA/PLA+ materials are tough/elastic enough to withstand the winding stress.
- PLA/PLA+ materials will not shear into tiny bits during use[<sup>1<sup>](https://github.com/vishnu350/rs-mainspring-winder#warnings-and-advice), and thus will not contaminate the mainspring.
- Never need to worry about wearing out the arbour hooks, as [staple pins are easily replaced](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base).
- Nice knurling patterns for a good grip while winding, and winder sizes are properly labelled.
- Can wind in both directions (clockwise and counter-clockwise).
- Pick any size. The Python generator script accurately buils a [complete set of winders](https://github.com/vishnu350/rs-mainspring-winder/releases/latest/download/rs-winder.zip) (7mm-18.5mm) from a single design file.
- Or customize it for a specific movement. The winder dimensions are parameterized, and can be easily [tweaked in FreeCAD](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder).

**Watch this YouTube video [here](https://youtu.be/EZvd_MKBOUQ) or [here](https://youtu.be/OAfQTk89P3s) (older) to better understand the RS winder parts and how it works.**<br/>
**Discussion/Feedback: WRT forum thread [here](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/), or GitHub discussion section [here](https://github.com/vishnu350/rs-mainspring-winder/discussions).**<br/>

<p align="center">
<img src="https://user-images.githubusercontent.com/5123344/179362355-92640bc8-f01c-4858-81e5-610a5d544c9d.jpg" alt="drawing" width="40%"/>
<img src="https://user-images.githubusercontent.com/5123344/179362734-67d5340e-5dd6-44f6-97d1-f3182b52eb8a.jpg" alt="drawing" width="31%"/>
</p>

# RS Winder Parts Description
There are several parts to the RS mainspring winder:
- **The housing barrel**. This part is the barrel that houses the mainspring and plunger, with a rising sun knurling pattern on the top for no reason.
- **The winder base**. This part is responsible for winding the mainspring with the help of the arbour hook.
- **The plunger**. This part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
- **The arbour hook**. Fashion this part out of a stapler pin and insert into the hole on the winder beside the arbour ([instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base)), use the staple jig part for best results. Also called **anchor**.
- **The setter bowl**. This part helps the ejection of the mainspring by a very small amount so that the actual mainspring barrel can be easily fitted in by hand (see 2nd picture above).
- **The arbour rod**. Get a dowel pin (or equivalent) with 1.5mm-3.0mm diameter and place it at the center of the winder base.
- **The staple jig**. Use this part to easily cut the staple pins to form the arbour hook, watch instructional video [here](https://youtu.be/na0XtIDea9I).

**NOTE:** *The arbour hook and rod are too small to be 3D printed, hence metal parts are **required** for the RS winder to work.*

# Building the RS winder
Recommended 3D printing options:
- **Material: PLA or PLA+** (best for high accuracy prints).
- **Infill: 20% or more** (parts may crumble under stress if lower).
- **Layer thickness: 0.1 mm** or better.
- **Color: Any**, go with white if unsure. Best if all parts are of the same color for equal tolerances.
- **Printer: Any well calibrated 3D printer**, best if the print job is done with high accuracy settings.
- **Placement: Widest flat surface should face downwards** on print bed for best results, applies for all parts.

Steps to build your RS mainspring winder:
1. Use a caliper to measure your mainspring barrel inner diameter and the mainspring arbour diameter.
2. Download the latest [rs-winder.zip](https://github.com/vishnu350/rs-mainspring-winder/releases/latest/download/rs-winder.zip) from the [release section](https://github.com/vishnu350/rs-mainspring-winder/releases).
   - Print your winder base part STL/3MF file. Choose from 1.5-3.0mm sizes, whichever matches your mainspring arbour the best.
   - Print your housing barrel and plunger part STL/3MF files. Size is based on mainspring barrel inner diameter, make sure to select matching sizes. In-depth winder size selection guide [here](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring).
   - Print your setter bowl part STL/3MF file, this part should universally work with all housing barrels.
   - Print your staple jig part STL file.
3. Fashion a stapler pin into an arbour hook with using the staple jig (see [instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base) or watch video [here](https://youtu.be/na0XtIDea9I)), use a metal file to reduce thickness if needed. Insert it into any of the holes on the winder base part that fits best.
4. Install the appropriate dowel pin for your winder base part:
   - Recommended online purchase links: [AliExpress](https://www.aliexpress.com/item/1005002177332247.html), [Amazon](https://www.amazon.com/dp/B09W5PBHGR).
   - For normal size winder base: 1.5mm/2.0mm (M1.5/M2) diameter dowel pins, 18mm in length.
   - For large size winder base: 2.0mm/2.5mm (M2.0/M2.5) diameter dowel pins, 18mm in length.
   - Using glue/epoxy for the dowel pins are optional, apply only a teeny tiny amount as needed.

# Using the RS winder
Please go to the wiki for instructions: [Using the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Using-the-RS-winder).

Or watch a [YouTube video](https://youtu.be/EZvd_MKBOUQ).

# Customizing/Generating the RS winder
Please go to the wiki for instructions: [Customizing & Generating the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder).

To generate the STL/3MF files for the various different sizes of all the RS winder parts, just clone this repo and execute the Python FreeCAD script using the following command:<br/>`freecadcmd generate_stl.py`

# Warnings and Advice
- For known issues, see the [issues section](https://github.com/vishnu350/rs-mainspring-winder/issues).
- As stated before, everything provided here comes with **ABSOLUTELY ZERO WARRANTY**. See the [issues section](https://github.com/vishnu350/rs-mainspring-winder/issues) before deciding if this is for you, otherwise please consider getting a professional mainspring winder set.
- While this winder works great for many users, it still requires you to be resourceful and competent in basic watchmaking skills.
- Refer to the wiki for [help with winder size selection](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring), if you chose the wrong size **you WILL damage your mainspring**.
- When initially placing the housing barrel on the winder base with the latched mainspring, **do not forcefully ram the mainspring into position**. Watch the [YouTube video](https://youtu.be/OAfQTk89P3s?t=204) (min 3:24) for an elegant way to do this.
- If the staple pin is not fashioned correctly, it will easily get unhooked while winding or cause other issues.
- It is recommended to practice first with spare mainsprings/barrels to get a feel of using the RS winder.
- If the printed parts are stringy, it means your printer isnt properly calibrated. Make sure to properly clean the parts before use to avoid contamination.
- Be very careful when unwinding, do it slowly.

# Thanks & How To Contribute
If you like this work, please consider to:
- **Post a picture of your first fully wound mainspring and winder set** in the discussion section or WRT forums!
- Fix bugs/issues, contribute to the design, or experiment with 3D printouts using untested parameters.
- **Tip me through a [one time sponsor](https://github.com/sponsors/vishnu350?frequency=one-time) :)**

Credits and thanks to the following folk:
- AndyShap for sharing his setter bowl and staple jig ideas. Also for providing the design files and wiki guides.
- Fratink for coming up with the original design [here](https://www.thingiverse.com/thing:3540660) in Thingiverse. The same free Creative Commons licensing scheme is reused.
