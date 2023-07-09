# Introduction

The RS mainspring winder is a fully functional 3D printable watch mainspring winder, with accurately calculated design files provided for every possible size imaginable. Everything provided here is free and open source.

This is the modern solution to hobbyist mainspring winding woes and it comes with **absolutely zero warranty**. You are advised to thouroughly go through this README, the [wiki pages](https://github.com/vishnu350/rs-mainspring-winder/wiki), [video](https://youtu.be/EZvd_MKBOUQ) resources found here.

Watch mainspring winding for hobbyists has always been a problem, as most of us cannot afford the $1500 Bergeon set to wind vintage unbranded mainsprings/barrels. Or sometimes the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding, which may kink or damage the mainspring.

The RS mainspring winder was designed using FreeCAD+Python, and is easy to 3D print. It costs ~$10 to print a single set by most 3D print service providers. Alternatively, you may choose to just purchase a prebuilt kit from **eBay seller AndyShap2 [here](https://www.ebay.com/itm/125428348675) (single set)** or **[here](https://www.ebay.com/itm/125578735361) (complete set).**

<p align="center">
<img src="https://user-images.githubusercontent.com/5123344/179362355-92640bc8-f01c-4858-81e5-610a5d544c9d.jpg" alt="drawing" width="40%"/>
<img src="https://user-images.githubusercontent.com/5123344/179362734-67d5340e-5dd6-44f6-97d1-f3182b52eb8a.jpg" alt="drawing" width="31%"/>
</p>

The RS mainspring winder works very well when properly constructed. **List of features:**
- Guaranteed to work on all released sizes, since the generation process is scripted.
- Cheap and easy to print with no post-processing/finishing or support material required.
- Winds cleanly and safely, no more getting bits of skin stuck due to handwinding.
- Can wind in both directions, clockwise and counter-clockwise.
- Has knurling patterns on body for a good grip during use, along with clear size labelling.
- PLA/PLA+ material is tough/elastic enough to withstand the winding stress.
- Both PLA/PLA+ and staple pins are softer than steel, and thus it will not kink or damage the mainspring.
- Never need to worry about wearing out the arbour hooks, as [staple pins are easy to replace](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base).
- Pick any size from the generated [set of winders](https://github.com/vishnu350/rs-mainspring-winder/releases/latest/download/rs-winder.zip) (7mm-18.5mm) or [customize](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder) it yourself.

**Watch this YouTube video [here](https://youtu.be/EZvd_MKBOUQ) or [here](https://youtu.be/OAfQTk89P3s) (older) to better understand the RS winder parts and how it works.**<br/>
**Discussion/Feedback: WRT forum thread [here](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/), or GitHub discussion section [here](https://github.com/vishnu350/rs-mainspring-winder/discussions).**<br/>

# RS Winder Parts Description
There are several parts to the RS mainspring winder:
- **The housing barrel**. This part is the barrel that houses the mainspring and plunger, with a rising sun knurling pattern on the top for no reason.
- **The winder base**. This part is responsible for winding the mainspring with the help of the arbour hook.
- **The plunger**. This part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
- **The arbour hook**. Fashion this part out of a staple pin using the staple jig part (see [instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base)) and insert into one of the holes on the winder base part (see [guide](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbour-Hook-to-the-Mainspring)). Also called **anchor**.
- **The setter bowl**. This part helps the ejection of the mainspring by a very small amount so that the actual mainspring barrel can be easily fitted in by hand (see 2nd picture above).
- **The arbour rod**. Get a dowel pin (or equivalent) with 1.5mm-3.0mm diameter and place it at the center of the winder base.
- **The staple jig**. Use this part to easily cut the staple pins to form the arbour hook, watch instructional video [here](https://youtu.be/na0XtIDea9I).

**NOTE:** *The arbour hook and rod are too small to be 3D printed, hence metal parts are **required**.*

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
3. Fashion a staple pin into an arbour hook with using the staple jig (see [instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbour-Hook-for-the-Winder-Base) or watch [video](https://youtu.be/na0XtIDea9I)), use a metal file to reduce thickness if needed. Insert it into one of the holes on the winder base part (see [guide](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbour-Hook-to-the-Mainspring)).
4. Install the appropriate dowel pin for your winder base part:
   - Recommended online purchase links: [AliExpress](https://www.aliexpress.com/item/1005002177332247.html), [Amazon](https://www.amazon.com/dp/B09W5PBHGR).
   - For normal size winder base: 1.5mm/2.0mm (M1.5/M2) diameter dowel pins, 18mm in length.
   - For large size winder base: 2.0mm/2.5mm (M2.0/M2.5) diameter dowel pins, 18mm in length.
   - Using glue/epoxy for the dowel pins are optional, apply only a teeny tiny amount as needed.

# Using the RS winder
Please go to the wiki for instructions: [Using the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Using-the-RS-winder), or watch a [YouTube video](https://youtu.be/EZvd_MKBOUQ).

Make sure to study the [correct arbour hook latching method](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbour-Hook-to-the-Mainspring).

# Customizing/Generating the RS winder
Please go to the wiki for instructions: [Customizing & Generating the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder).

To generate the STL/3MF files for the various different sizes of all the RS winder parts, just clone this repo and execute the Python FreeCAD script using the following command:<br/>`freecadcmd generate_stl.py`

# Warnings and Advice
Please read every single sentence below carefully:
- As stated before, everything provided here comes with **ABSOLUTELY ZERO WARRANTY**.
- While this winder works great for many users, it still requires you to be resourceful and **competent in basic watchmaking skills**.
- You must be competent enough to **assess the health of the mainspring** (see [here for guidance](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring)). Tired/old mainsprings **WILL BREAK** regardless of how expensive your tools are.
- It is recommended to **practice first with spare mainsprings/barrels** to get a feel of using the RS winder. Incorrect use can break or damage your mainspring, this is the case even with professional winders.
- Refer to the wiki for help with [**winder size selection**](https://github.com/vishnu350/rs-mainspring-winder/wiki/Selecting-the-correct-winder-size-for-your-mainspring), choosing the wrong size will damage your mainspring.
- When initially placing the housing barrel on the winder base with the latched mainspring, **do not forcefully ram the mainspring into position**. Watch the [video](https://youtu.be/OAfQTk89P3s?t=204) (min 3:24) for an elegant way to do this.
- Always **hook the staple pin from the outside** of the mainspring with the **correct "*g*" gap** from the dowel pins to avoid deforming/breaking it when winding. Study the [correct arbour hook latching method](https://github.com/vishnu350/rs-mainspring-winder/wiki/Attaching-the-Arbour-Hook-to-the-Mainspring) diagrams to undertand this better.
- If the staple pin is not fashioned correctly, it will easily get unhooked while winding or cause other issues.
- If the printed parts are stringy, it means your printer isnt properly calibrated. Make sure to properly clean the parts before use to avoid contamination.
- Be very careful when unwinding, do it slowly.

# Thanks & How To Contribute
If you like this work, please consider to:
- Please ⭐️ this repository if this project helped you.
- Fix bugs/issues, contribute to the design, or experiment with 3D printouts using untested parameters.
- Tip me via a one time [sponsor](https://github.com/sponsors/vishnu350?frequency=one-time) :)

Credits and thanks to the following folk:
- AndyShap for sharing his setter bowl and staple jig ideas. Also for providing the design files and wiki guides.
- Fratink for coming up with the original design [here](https://www.thingiverse.com/thing:3540660) in Thingiverse. The same free Creative Commons licensing scheme is reused.
