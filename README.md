# Introduction
This is the 3D printable "Rising Sun" watch mainspring winder for watchmaking hobbyists. This is the 2021 solution to hobbyist mainspring winding woes and it proudly comes with **absolutely zero warranty**. Use it at your own risk.

Watch mainspring winding for hobbyist has always been a problem, as most of us cannot afford the $1000 Bergeon set to wind their vintage unbranded mainsprings/barrels. In the worst case scenario, the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding, which will definitely kink or damage the mainspring. Worry not, as I have come to your rescue.

This mainspring winder is designed using FreeCAD to be 3D printed, and will approximately cost $5/set by most 3D print service providers (use eBay to find someone near you). The design is parameterized, allowing you to dynamically change the size/dimensions of the winder and the entire design will be recalculated accordingly.

The RS mainspring winder is a pleasure to use when constructed correctly, and can wind in both clockwise and counter-clockwise directions. It will not kink or damage the mainspring due to the PLA material being softer than steel, but still tough enough to withstand the winding stress. Due to this, it may even be viable for professional watchmakers.

# RS Winder Parts Description

There are five parts to the RS mainspring winder:
- **The housing barrel**. This 3D printed part has a barrel that houses the mainspring and plunger, and the knurling pattern on the top is akin to a rising sun.
- **The winder base**. This 3D printed part holds the anchor which latches to the mainspring hole and winds it up.
- **The barrel bowl**. This 3D printed part holds the actual mainspring barrel in place for safely plunging the mainspring back in.
- **The plunger**. This 3D printed part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
- **The anchor**. Fashion this part out of a stapler clip and insert into the hole on the winder beside the arbour.

**NOTE:** *The anchor is too small to be 3D printed with enough strength/accuracy, hence a metal part is **required** for the RS winder to work. A stapler clip is an everyday item accessible to everyone, and is perfect for this task.*

# Building the RS winder

Recommended 3D printing options:
- **Material: PLA** (needed for the accuracy over PETG, PLA+, Nylon, etc). Avoid cheap or low quality PLA.
- **Filling: 100%** (lower values are not recommended, parts may crumble under stress).
- **Layer thickness: 200 µm** or better.
- **Printer: Prusa I3 MK3** or better.
- **Color: White** for all (optionally orange for plunger if desired). Or whatever.

Steps to build your RS mainspring winder:
1. Use a caliper to measure your mainspring barrel inner and outer diameters. The outer diameter includes the main wheel (gear).
2. Download the latest rs-winder-vXXX.zip from the [release section](https://github.com/vishnu350/rs-mainspring-winder/releases).
   - Select your winder base part STL file (standard size).
   - Select your housing barrel and plunger part STL files. Size is based on mainspring barrel inner diameter, make sure to select matching sizes for both parts.
   - Select your bowl part STL files. Size is based on the mainspring barrel outer diameter.
   - Alternatively, you may customize and generate these files yourself (see 'customizing' steps below).
3. 3D print the four STL files with the recommended 3D print settings, or just send it to someone on eBay to help you with that.
4. Fashion a stapler pin as an anchor and insert it into the hole beside the arbour on the winder. Use a file if you need to trim it down.
5. Clean all parts and then lubricate all contact points appropriately.

##### TODO: Add more description on anchor part with pics and how to hold the RS winder.

# Customizing/Generating the RS winder

Steps to customizing your RS winder:
1. Download and install [FreeCAD](https://freecadweb.org/downloads.php). It is an amazing piece of free and open-source software.
2. Download the RS mainspring winder [FreeCAD project file](https://github.com/vishnu350/rs-mainspring-winder/blob/main/rs-winder.FCStd) and open it.
3. Open up the parameter spreadsheet on the left pane by double clicking on it.
4. Go through the parameter descriptions, and then tune the values to match your needs. You will need a caliper to measure your mainspring/barrel/etc dimensions.
5. Make sure a proper font file is selected for *Version_Text* on the housing part. *FreeSansBold.ttf* is included in the repo.
6. Recompute the entire design by pressing CTRL+R, and check if the parts look alright.
7. Click on each part and then export as STL files (winder, housing, bowl, plunger).

To automatically generate the STL files for the various different sizes of all the RS winder parts, clone the repo and execute the Python FreeCAD script using the following command:<br />
`freecadcmd generate_stl.py`

**NOTE:** *Only customize the RS winder if the pre-generated STL files do not fit your needs.*

# Using the RS winder

Steps to using the RS winder:
1. Place the plunger into the housing barrel.
2. Place the mainspring into the arbour on the winder part.
3. Use a tweezer to latch the anchor onto the mainspring hole.
4. Carefully put the housing barrel and winder parts together. Take care **not to wind in reverse** as this will unlatch the anchor.
5. Wind the mainspring until end tail of the mainspring sticks out. Ram it in with any tool of your choosing,  **until it can no longer be seen**. If it refuses to go in, wind a little bit more to make space for it to do so (but not too much).
6. Once done, **unwind** by going in the **reverse direction until there is no more force from the mainspring**. Once unwound, the anchor will naturally unlatch, allowing you to easily take off the winder base part. If the mainspring is still latched, then gently unwind a little bit more.
7. Next, place the actual mainspring barrel inside the barrel bowl recess and plug it into the housing barrel.
8. Place the housing+bowl parts on a level surface, apply some downward force to hold it together, and then press the plunger. All done!
9. Enjoy the rest of your day knowing that it just cost you $5 and a measly stapler clip to wind up a fancy Swiss mainspring.

# Warnings and Tips
- As stated before, everything provided here comes with **ABSOLUTELY ZERO WARRANTY**. Only use this on your beloved grandfather's vintage Rolex if you are confident in doing so.
- Be very careful with the winder base part! Although it appears sturdy, **dropping it will most likely break the arbour**.
- When pushing the final bit of the mainspring into the housing barrel, take care **not to accidentally push upwards and get it stuck** in between the plunger and the housing barrel walls. You may need to reset and try again if this happens.
- Double check if the plunger base is **level, round and flat**. If it isnt, there is a higher chance for the mainspring to get caught. So work it down with a metal file or sandpaper.
- Make sure to **apply downward force** while plunging the mainspring back in, otherwise it may fail to pop back into the barrel.
- It is good to **lubricate** the housing barrel walls and mainspring before winding it in. This reduces winding stress and also makes it easier to plunge later on.
- When unwinding, be gentle so as to not scratch the mainspring with the anchor, even though this is unlikely.
- It is recommend to practice first with spare mainsprings/barrels to get a feel of using the RS winder.
- The barrel bowl part can also be used to snap the barrel lid back on, as well as holding it during assembly/disassembly service.
 
# Future Updates
- Store common parameters/dimensions for known movements in a library file.
- Add python based generator to use this file and generate/release commonly used winder parameter/sizes for known movements.
- Further tweak design for better quality and ease of use.

# Thanks & How To Contribute
I lack the knowledge on the complete spectrum of barrel sizes, mainspring sizes, etc, so I can never build something that is perfect without your help. I also do not have a 3D printer, so I have been paying for each experimental print with the help of a local 3D print company.

So if you like my work, please consider:
- Contributing to the design or experimenting with 3D printouts using untested parameters.
- Share the dimensions of known existing mainspring barrel and parts.
- Offering to print and ship experimental 3D printed designs for me.
- [Sponsoring me](https://github.com/sponsors/vishnu350), whichs helps me out with paying for experimental prints.
- Or just [buy me](https://github.com/sponsors/vishnu350) a drink, that will also work :)

Thanks to Fratink for coming up with the original design [here](https://www.thingiverse.com/thing:3540660) in Thingiverse. The same free Creative Commons licensing scheme is reused for this work.
