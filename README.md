# Introduction
This is the 3D printable "Rising Sun" watch mainspring winder for watchmaking hobbyists. The RS nickname is derived from the fingergrip knurling pattern on the top of the winder. This is the 2021 solution to hobbiyst mainspring winding woes and it proudly comes with **absolutely zero warranty**. Use it at your own risk.

Watch mainspring winding for hobbyists has always been a problem, as most of us cannot afford the $1000 Bergeon set to wind their vintage unbranded mainsprings/barrels. In the worst case scenario, the appropriate size just isn't available. This forces most casual hobbyists to resort to handwinding, which will definately kink or damage the mainspring. Worry not, as I have come to your rescue.

This FreeCAD based mainspring winder is designed to be 3D printed, and will approximately cost $5/set by most 3D print service providers (use eBay to find someone near you). The design is parameterized, allowing you to dynamically change the size/dimensions of the winder and the entire design will be recalculated accordingly.

The RS mainspring winder is a pleasure to use when constructed correctly, and can wind in both clockwise and counter-clockwise directions. It will not kink or damage the mainspring due to the PLA material being softer than steel, but still tough enough to withstand the winding stress. Due to this, it may even be viable for professional watchmakers.

##### TODO: Add link to video here.

# RS Winder Parts Description

There are four parts to the RS mainspring winder:
- **The housing barrel**. This 3D printed part has a barrel that houses the mainspring and plunger, and the knurling pattern on the top is akin to a rising sun.
- **The winder base**. This 3D printed part holds the anchor which latches to the mainspring hole and winds it up. When reversed, it holds the actual mainspring barrel in place for plunging the mainspring back in.
- **The plunger**. This 3D printed part pushes the mainspring out of the housing barrel into the actual mainspring barrel.
- **The anchor**. Fashion this part out of a stapler clip and insert into the hole on the winder beside the arbour.

**NOTE:** *The anchor is too small to be 3D printed with enough strength/accuracy, hence a metal part is **required** for the RS winder to work. A stapler clip is an everyday item accesible to everyone, and is perfect for this task.*

# Building the RS winder

Recommended 3D printing options:
- **Material: PLA** (needed for the accuracy over PETG, PLA+, Nylon, etc). Avoid cheap or low quality PLA.
- **Filling: 100%** (lower values are not recommended, parts may crumble under stress).
- **Layer thickness: 200 µm** or better.
- **Printer: Prusa I3 MK3** or better.
- **Colour: White** for all (optionally orange for plunger if desired). Or whatever.

Steps to customize and building your own RS winder:
1. Download and install FreeCAD. Why FreeCAD? It is lightweight, free, open-source, works on any machine, doesnt spy on you, and doesnt constantly nag you to pay for features you will never need.
2. Download the RS mainspring winder FreeCAD project file and open it.
3. Open up the parameter spreadsheet on the right pane by double clicking on it.
4. Go through the parameter descriptions, and then tune the values to match your needs. You will need a caliper to measure your mainspring/barrel dimensions.
5. Click on each part and then export as STL files (winder, housing, plunger).
6. 3D print these three parts with the recommended print settings, or look for someone on eBay to help you.
7. Fashion a stapler pin as an anchor and insert it into the hole beside the arbour on the winder. Use a file if you need to trim it down.
8. Clean/wash all parts and then (optionally) lubricate all contact points appropriately.

**NOTE:** *Only customize the RS winder if the pre-generated STL files do not fit your needs.*

##### TODO: Add link to FreeCAD installer, mention 0.19 works.
##### TODO: Add link to FreeCAD project file.
##### TODO: Add link to STL files and proper description so some users can avoid using FreeCAD.
##### TODO: Add more description on anchor part with pics and how to hold the RS winder.

# Using the RS winder

Steps to using the RS winder:
1. Place the plunger into the housing barrel.
2. Place the mainspring into the arbour on the winder part. Be careful not to break it.
3. Use a tweezer to latch the anchor onto the mainspring hole (see video).
4. Carefully put the housing barrel and winder parts together , careful not to wind in reverse as this will unlatch the anchor.
5. Wind the mainspring until end tail of the mainspring sticks out. Use a tweezer to ram it in **until it cannot be seen**. If it refuses to go in, wind a little bit more to make it easier to do so (but not too much).
6. Once done, **unwind** by going in the **reverse direction until there is no more force from the mainspring**. The anchor will naturally unlatch, allowing you to just pull off the winder part. If the mainspring is still latched, then gently unwind a little bit more. Do not overdo it as the hook may scratch the mainspring.
7. Next, reverse the winder and place the actual mainspring barrel inside the recess. Plug it back into the housing barrel, apply some force to hold it together, and press the plunger. All done!
8. Enjoy the rest of your day knowing that it just cost you $5 and a measly stapler clip to wind up a fancy Swiss mainspring.

# Future Updates
- Store common parameters for known movements in a library file.
- Add python based generator to use this file and generate/release commonly used winder parameter/sizes for known movements.
- Tweak design further for better quality and ease of use.

# Thanks
Thanks to Fratink for coming up with the original design: https://www.thingiverse.com/thing:3540660, the same free Creative Commons licensing scheme is reused for this work. However the design was lacking in polish, so I rebuilt it from scratch.

If you like my work, consider contributing to the design or experimenting with 3D printouts using untested parameters. Or just buy me a drink by sponsoring me, that will also work :)
