# Introduction
This project helps watchmaking hobbyists build 3D printable "Rising Sun" mainspring winders for every possible size imaginable. Everything provided here is free and open source. This is the modern solution to hobbyist mainspring winding woes and it proudly comes with **absolutely zero warranty**. Use it at your own risk.

Watch mainspring winding for hobbyists has always been a problem, as most of us cannot afford the $1500 Bergeon set to wind vintage unbranded mainsprings/barrels. Or sometimes, the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding or other similar stunts, which will definitely kink or damage the mainspring. Worry not, as we have come to your rescue.

This mainspring winder is designed using FreeCAD to be easily 3D printed with no post-processing/finishing required. It will approximately cost $5/set by most 3D print service providers. The design is parameterized, allowing you to dynamically change the size/dimensions of the winder and the entire design will be recalculated accordingly.

The RS mainspring winder works very well when constructed correctly, and can wind in both clockwise and counter-clockwise directions. It will not kink or damage the mainspring due to the PLA material being softer than steel, yet tough enough to withstand the winding stress.

**Watch this YouTube video [here](https://youtu.be/OAfQTk89P3s) to better understand the RS winder parts and how it works.**<br/>
**Discussion/Feedback: WRT forum thread [here](https://www.watchrepairtalk.com/topic/19340-3d-printed-rs-mainspring-winder-project-for-hobbyists/), or GitHub discussion section [here](https://github.com/vishnu350/rs-mainspring-winder/discussions).**

<p align="center">
<img src="https://user-images.githubusercontent.com/5123344/179362355-92640bc8-f01c-4858-81e5-610a5d544c9d.jpg" alt="drawing" width="40%"/>
<img src="https://user-images.githubusercontent.com/5123344/179362734-67d5340e-5dd6-44f6-97d1-f3182b52eb8a.jpg" alt="drawing" width="31%"/>
</p>

# RS Winder Parts Description

There are several parts to the RS mainspring winder:
- **The housing barrel**. This part is the barrel that houses the mainspring and plunger, with a rising sun knurling pattern on the top for no reason.
- **The winder base**. This part is responsible for winding the mainspring by latching onto it with the anchor.
- **The plunger**. This part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
- **The anchor**. Fashion this part out of a stapler pin and insert into the hole on the winder beside the arbour ([instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbor-Hook)).
- **The setter bowl**. This part helps the ejection of the mainspring by a very small amount so that the actual mainspring barrel can be easily fitted in by hand (see 2nd picture above).
- **The barrel bowl (optional)**. This part holds the actual mainspring barrel in place for safely plunging the mainspring back in. It is optional, the plunging step can still be performed without it.
- **The arbour (optional)**. Get a dowel pin (or equivalent) with 2mm/2.5 diameter and place it at the center of the winder base. Only needed for the winder base hole version.

**NOTE:** *The anchor is too small to be 3D printed with enough strength/accuracy, hence a metal part is **required** for the RS winder to work. A stapler pin is an everyday item accessible to everyone, and is perfect for this task.*

# Building the RS winder

Recommended 3D printing options:
- **Material: PLA** (best for high accuracy prints). Avoid overly cheap or low quality materials.
- **Filling: 100%** (parts may crumble under stress if lower).
- **Layer thickness: 200 µm** or better.
- **Printer: Any decent 3D printer**, as long as you understand your printer settings well enough.
- **Color: Any**, best if all parts are the same color for equal tolerances between prints.

Steps to build your RS mainspring winder:
1. Use a caliper to measure your mainspring barrel inner and outer diameters. The outer diameter includes the main wheel (gear).
2. Download the latest rs-winder-vXXX.zip from the [release section](https://github.com/vishnu350/rs-mainspring-winder/releases).
   - Select your winder base part STL file (either arbour or hole version).
   - Select your housing barrel and plunger part STL files. Size is based on mainspring barrel inner diameter, make sure to select matching sizes.
   - Select your setter bowl part STL files. Optionally, select a matching barrel bowl part (size based on outer diameter).
3. 3D print the STL files with the recommended 3D print settings, or just get someone help you with that.
4. Fashion a stapler pin into an anchor with a pair of pliers ([instructions](https://github.com/vishnu350/rs-mainspring-winder/wiki/Creating-the-Arbor-Hook)), use a metal file to reduce thickness if needed. Insert it into any of the holes on the winder base part that fits best.
5. If you printed the winder base hole version (no arbour rod), then install the appropriate dowel pins:
   - For normal size winder base: 2.0mm diameter (M2) dowel pins, 16mm in length.
   - For large size winder base: 2.5mm diameter (M2.5) dowel pins, 16mm in length.
   - Purchase links: [AliExpress](https://www.aliexpress.com/item/1005002177332247.html), [Amazon](https://www.amazon.com/dp/B09W5PBHGR).

# Using the RS winder

Read the wiki instructions [here](https://github.com/vishnu350/rs-mainspring-winder/wiki/Using-the-RS-winder) or watch a [video](https://youtu.be/OAfQTk89P3s).

# Customizing/Generating the RS winder

Please head to the wiki for step by step instructions: [Customizing & Generating the RS winder](https://github.com/vishnu350/rs-mainspring-winder/wiki/Customizing-&-Generating-the-RS-winder)

To generate the STL files for the various different sizes of all the RS winder parts, just clone this repo and execute the Python FreeCAD script using the following command:<br />
`freecadcmd generate_stl.py`

# Warnings and Tips
- As stated before, everything provided here comes with **ABSOLUTELY ZERO WARRANTY**. Only use this on your beloved grandfather's vintage Rolex if you are confident in doing so.
- Take your time to properly **fashion the stapler pin to the right size**. If it is not correct, it will easily get unhooked while winding or may even cause the winding base arbour to break.
- When initially placing the housing barrel on the winder base with the latched mainspring, **do not forcefully ram the mainspring into position**. Watch the [YouTube video](https://youtu.be/OAfQTk89P3s) for an elegant way to do this.
- Be very careful with the winder base part! Although it may appear sturdy, **dropping it will most likely break the arbour**. Consider using the winder base hole version with dowel pins instead.
- Double check if the plunger base is **level, round and flat**. If it is not, then work it down with a metal file or sandpaper.
- Make sure to **apply downward force** while plunging the mainspring back in, otherwise it may fail to pop back into the barrel.
- It is good to **lubricate** the housing barrel walls and mainspring before winding it in. This reduces winding stress and also makes it easier to plunge later on.
- When unwinding, be gentle so as to not scratch the mainspring with the anchor.
- It is recommended to practice first with spare mainsprings/barrels to get a feel of using the RS winder.
- The barrel bowl part can also be used to snap the barrel lid back on, as well as holding it during assembly/disassembly service.
 
# Future Updates
- Further tweak design for better quality and ease of use.
- Store common parameters/dimensions for known movements in a library file, include sizes of all popular movements.
- Further improve the staple cutting mechanism, or replace it with something better.
- Explore soldering the staple pin to the dowel pins to create an even better winder base arbour.

# Thanks & How To Contribute
If you like my work, please consider:
- Fixing bugs/issues, contributing to the design, or experimenting with 3D printouts using untested parameters.
- Share your success/failure story on your using the RS winder for unknown mainsprings/barrels.
- Offering to print or ship experimental 3D printed designs for me.

Credits and thanks to the following folk:
- Fratink for coming up with the original design [here](https://www.thingiverse.com/thing:3540660) in Thingiverse. The same free Creative Commons licensing scheme is reused for this work.
- AndyShap for sharing his setter bowl idea, providing the design files and wiki guides.
