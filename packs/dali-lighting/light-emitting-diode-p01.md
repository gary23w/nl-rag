---
title: "Light-emitting diode (part 1/2)"
source: https://en.wikipedia.org/wiki/Light-emitting_diode
domain: dali-lighting
license: CC-BY-SA-4.0
tags: dali lighting protocol, digital addressable lighting interface, lighting control bus, led dimming control
fetched: 2026-07-02
part: 1/2
---

# Light-emitting diode

A **light-emitting diode** (**LED**) is an electronic component that uses a semiconductor to emit light when current flows through it. Electrons in the semiconductor recombine with electron holes, thereby releasing energy in the form of photons. The color of the light (corresponding to the energy of the photons) is determined by the energy required for electrons to cross the band gap of the semiconductor. White light is obtained by using multiple semiconductors or a layer of light-emitting phosphor on the semiconductor device.

Appearing as practical electronic components in 1962, the earliest LEDs emitted low-intensity infrared (IR) light. Infrared LEDs are used in remote-control circuits, such as those used with a wide variety of consumer electronics. The first visible-light LEDs were of low intensity and limited to red.

Early LEDs were often used as indicator lamps, replacing small incandescent bulbs, and in seven-segment displays. Later developments produced LEDs available in visible, ultraviolet (UV), and infrared wavelengths with high, low, or intermediate light output; for instance, white LEDs suitable for room and outdoor lighting. LEDs have also given rise to new types of displays and sensors, while their high switching rates have uses in advanced communications technology. LEDs have been used in diverse applications such as aviation lighting, fairy lights, strip lights, automotive headlamps, advertising, stage lighting, general lighting, traffic signals, camera flashes, lighted wallpaper, horticultural grow lights, and medical devices.

LEDs have many advantages over incandescent light sources, including lower power consumption, reduced waste heat, a longer lifetime, improved physical robustness, smaller sizes, and faster switching. In exchange for these generally favorable attributes, disadvantages of LEDs include electrical limitations to low voltage and generally to DC (not AC) power, the inability to provide steady illumination from a pulsing DC or an AC electrical supply source, and a lesser maximum operating temperature and storage temperature.

LEDs are transducers of electricity into light.


## History

Electroluminescence from a solid state diode was discovered in 1906 by Henry Joseph Round of Marconi Labs, and was published in February 1907 in Electrical World. Round observed that various carborundum (silicon carbide) crystals would emit yellow, light green, orange, or blue light when a voltage was passed between the poles.

A silicon carbide LED was created by Soviet inventor Oleg Losev in 1927.

Commercially viable LEDs only became available after Texas Instruments engineers patented efficient near-infrared emission from a diode based on GaAs in 1962. Commercial LEDs were extremely costly and saw no practical use until Monsanto and Hewlett-Packard developed them to the point where a unit cost less than five cents in the 1970s.

In the early 1990s, Shuji Nakamura, Hiroshi Amano and Isamu Akasaki developed blue light-emitting diodes, bringing white lighting and full-color LED displays into practical use. For this work, they won the 2014 Nobel Prize in Physics.


## Physics of light production and emission

In a light-emitting diode, the recombination of electrons and electron holes in a semiconductor produces light (infrared, visible or UV), a process called electroluminescence. The wavelength of the light depends on the energy band gap of the semiconductors used. Since these materials have a high index of refraction, design features of the devices, such as special optical coatings and die shape, are required to efficiently emit light.

Unlike a laser, the light emitted from an LED is neither spectrally nor spatially coherent nor even highly monochromatic. Its spectrum is sufficiently narrow that it appears to the human eye as a pure (saturated) color. Also, it cannot approach the very high intensity characteristic of lasers.


## Single-color LEDs

By selection of different semiconductor materials, single-color LEDs can be made that emit light in a narrow band of wavelengths, from the near-infrared through the visible spectrum and into the ultraviolet range. The required operating voltages of LEDs increase as the emitted wavelengths become shorter (higher energy, red to blue), because of their increasing semiconductor band gap.

Blue LEDs have an active region consisting of one or more InGaN quantum wells sandwiched between thicker layers of GaN, called cladding layers. By varying the relative In/Ga fraction in the InGaN quantum wells, the light emission can in theory be varied from violet to amber.

Aluminium gallium nitride (AlGaN) of varying Al/Ga fraction can be used to manufacture the cladding and quantum well layers for ultraviolet LEDs, but these devices have not yet reached the level of efficiency and technological maturity of InGaN/GaN blue/green devices. If unalloyed GaN is used in this case to form the active quantum well layers, the device emits near-ultraviolet light with a peak wavelength centered around 365 nm. Green LEDs manufactured from the InGaN/GaN system are far more efficient and brighter than green LEDs produced with non-nitride material systems, but practical devices still exhibit efficiency too low for high-brightness applications.

With AlGaN and AlGaInN, even shorter wavelengths are achievable. Near-UV emitters at wavelengths around 360–395 nm are already cheap and often encountered, for example, as black light lamp replacements for inspection of anti-counterfeiting UV watermarks in documents and bank notes, and for UV curing. Substantially more expensive, shorter-wavelength diodes are commercially available for wavelengths down to 240 nm. As the photosensitivity of microorganisms approximately matches the absorption spectrum of DNA, with a peak at about 260 nm, UV LED emitting at 250–270 nm are expected in prospective disinfection and sterilization devices. Recent research has shown that commercially available UVA LEDs (365 nm) are already effective disinfection and sterilization devices. UV-C wavelengths were obtained in laboratories using aluminium nitride (210 nm), boron nitride (215 nm) and diamond (235 nm).


## White LEDs

There are two primary ways of producing white light-emitting diodes (**WLED**). One is to use individual LEDs that emit three primary colors—red, green and blue—and then mix all the colors to form white light. The other, more common method is to use a phosphor material to convert monochromatic light from a blue or UV LED to broad-spectrum white light, similar to a fluorescent lamp. The yellow phosphor is made of cerium-doped YAG crystals suspended in the package or coated on the LED. This YAG phosphor causes white LEDs to appear yellow when off, and the spaces between the crystals allow some blue light to pass through in LEDs with partial phosphor conversion. Alternatively, white LEDs may use other phosphors like manganese(IV)-doped potassium fluorosilicate (PFS) or other engineered phosphors. PFS assists in red light generation, and is used in conjunction with a conventional Ce:YAG phosphor.

In LEDs with PFS phosphor, some blue light passes through the phosphors, the Ce:YAG phosphor converts blue light to green and red (yellow) light, and the PFS phosphor converts blue light to red light. The color emission spectrum or color temperature of white phosphor-converted and other phosphor-converted LEDs can be controlled by changing the concentration of several phosphors that form a phosphor blend used in an LED package.

The 'whiteness' of the light produced is engineered to suit the human eye. Because of metamerism, it is possible to have quite different spectra that appear white. The appearance of objects illuminated by that light may vary as the spectrum varies. This is the issue of color rendition, quite separate from color temperature. An orange or cyan object could appear with the wrong color and much darker as the LED or phosphor does not emit the wavelength it reflects. The best color rendition LEDs use a mix of phosphors, resulting in less efficiency and better color rendering.

The first white light-emitting diodes (LEDs) were offered for sale in the autumn of 1996. Nichia made some of the first white LEDs which were based on blue LEDs with Ce:YAG phosphor. Ce:YAG is often grown using the Czochralski method.

### RGB systems

Mixing red, green, and blue sources to produce white light needs electronic circuits to control the blending of the colors. Since LEDs have slightly different emission patterns, the color balance may change depending on the angle of view, even if the RGB sources are in a single package, so RGB diodes are seldom used to produce white lighting. Nonetheless, this method has many applications because of the flexibility of mixing different colors, and in principle, this mechanism also has higher quantum efficiency in producing white light.

There are several types of multicolor white LEDs: di-, tri-, and tetrachromatic white LEDs. Several key factors that play among these different methods include color stability, color rendering capability, and luminous efficacy. Often, higher efficiency means lower color rendering, presenting a trade-off between the luminous efficacy and color rendering. For example, the dichromatic white LEDs have the best luminous efficacy (120 lm/W), but the lowest color rendering capability. Although tetrachromatic white LEDs have excellent color rendering capability, they often have poor luminous efficacy. Trichromatic white LEDs are in between, having both good luminous efficacy (>70 lm/W) and fair color rendering capability.

One of the challenges is the development of more efficient green LEDs. The theoretical maximum for green LEDs is 683 lumens per watt, but as of 2010 few green LEDs exceed even 100 lumens per watt. The blue and red LEDs approach their theoretical limits.

Multicolor LEDs offer a means to form light of different colors. Most perceivable colors can be formed by mixing different amounts of three primary colors. This allows precise dynamic color control. Their emission power decays exponentially with rising temperature, resulting in a substantial change in color stability. Such problems hinder industrial use. Multicolor LEDs without phosphors cannot provide good color rendering because each LED is a narrowband source. LEDs without phosphors, while a poorer solution for general lighting, are the best solution for displays, whether they are LCD-backlit or direct LED-based pixels.

Dimming a multicolor LED source to match the characteristics of incandescent lamps is difficult because manufacturing variations, age, and temperature change the actual color value output. To emulate the appearance of dimming in incandescent lamps, LEDs may require a feedback system with color sensor to actively monitor and control the color.

### Phosphor-based LEDs

This method involves coating LEDs of one color (mostly blue LEDs made of InGaN) with phosphors of different colors to form white light; the resultant LEDs are called phosphor-based or phosphor-converted white LEDs (pcLEDs). A fraction of the blue light undergoes the Stokes shift, which transforms it from shorter wavelengths to longer. Depending on the original LED's color, various color phosphors are used. Using several phosphor layers of distinct colors broadens the emitted spectrum, effectively raising the color rendering index (CRI).

Phosphor-based LEDs have efficiency losses due to heat loss from the Stokes shift and other phosphor-related issues. Their luminous efficacies compared to normal LEDs depend on the spectral distribution of the resultant light output and the original wavelength of the LED itself. For example, the luminous efficacy of a typical YAG yellow phosphor based white LED ranges from 3 to 5 times the luminous efficacy of the original blue LED because of the human eye's greater sensitivity to yellow than to blue (as modeled in the luminosity function).

Due to the simplicity of manufacturing, the phosphor method is still the most popular method for making high-intensity white LEDs. The design and production of a light source or light fixture using a monochrome emitter with phosphor conversion is simpler and cheaper than a complex RGB system, and the majority of high-intensity white LEDs presently on the market are manufactured using phosphor light conversion.

Among the challenges being faced to improve the efficiency of LED-based white light sources is the development of more efficient phosphors. As of 2010, the most efficient yellow phosphor is still the YAG phosphor, with less than 10% Stokes shift loss. Losses attributable to internal optical losses due to re-absorption in the LED chip and in the LED packaging itself typically account for another 10% to 30% loss. Currently, in the area of phosphor LED development, much effort is being spent on optimizing these devices to higher light output and higher operation temperatures. For instance, the efficiency can be raised by adapting better package design or by using a more suitable type of phosphor. Conformal coating process is frequently used to address the issue of varying phosphor thickness.

Some phosphor-based white LEDs encapsulate InGaN blue LEDs inside phosphor-coated epoxy. Alternatively, the LED might be paired with a remote phosphor, a preformed polycarbonate piece coated with the phosphor material. Remote phosphors provide more diffuse light, which is desirable for many applications. Remote phosphor designs are also more tolerant of variations in the LED emissions spectrum. A common yellow phosphor material is cerium-doped yttrium aluminium garnet (Ce3+:YAG).

White LEDs can also be made by coating near-ultraviolet (NUV) LEDs with a mixture of high-efficiency europium-based phosphors that emit red and blue, plus copper and aluminium-doped zinc sulfide (ZnS:Cu, Al) that emits green. This is a method analogous to the way fluorescent lamps work. This method is less efficient than blue LEDs with YAG:Ce phosphor, as the Stokes shift is larger, but it yields light with better spectral characteristics, which render color better. Due to the higher radiative output of the ultraviolet LEDs than of the blue ones, both methods offer comparable brightness. A concern is that UV light may leak from a malfunctioning light source and cause harm to human eyes or skin.

A new style of wafers composed of gallium-nitride-on-silicon (GaN-on-Si) is being used to produce white LEDs using 200-mm silicon wafers. This avoids the typical costly sapphire substrate for relatively small 100- or 150-mm wafer sizes. The sapphire apparatus must be coupled with a mirror-like collector to reflect light that would otherwise be wasted. It was predicted that in 2020, 40% of all GaN LEDs are made with GaN-on-Si.

### Mixed white LEDs

There are RGBW LEDs that combine RGB units with a phosphor white LED on the market. Doing so retains the extremely tunable color of RGB LEDs, but allows color rendering and efficiency to be optimized when a color close to white is selected.

Some phosphor white LED units are "tunable white", blending two extremes of color temperatures (commonly 2700K and 6500K) to produce intermediate values. This feature allows users to change the lighting to suit the current use of a multifunction room. As illustrated by a straight line on the chromaticity diagram, simple two-white blends will have a pink bias, becoming most severe in the middle. A small amount of green light, provided by another LED, could correct the problem. Some products are RGBWW, i.e. RGBW with tunable white.

A final class of white LED with mixed light is dim-to-warm. These are ordinary 2700K white LED bulbs with a small red LED that turns on when the bulb is dimmed. Doing so makes the color warmer, emulating an incandescent light bulb.

### Zinc selenide white LEDs

Experimental white LEDs have been developed using homoepitaxially grown zinc selenide (ZnSe) on ZnSe substrates. These LEDs lack the yellow phosphors found in conventional white LEDs. In ZnSe LEDs, the active region emits blue light, while the conductive ZnSe substrate emits yellow light, resulting in white light output. Researchers suggest these LEDs offer lower operating voltages and a wider range of color temperatures than conventional white LEDs.


## Organic light-emitting diodes (OLEDs)

In an organic light-emitting diode (OLED), the electroluminescent material composing the emissive layer of the diode is an organic compound. The organic material is electrically conductive due to the delocalization of pi electrons caused by conjugation over all or part of the molecule, and the material therefore functions as an organic semiconductor. The organic materials can be small organic molecules in a crystalline phase, or polymers.

The potential advantages of OLEDs include thin, low-cost displays with a low driving voltage, wide viewing angle, and high contrast and color gamut. Polymer LEDs have the added benefit of printable and flexible displays. OLEDs have been used to make visual displays for portable electronic devices such as cellphones, digital cameras, lighting and televisions.


## Types

LEDs are made in different packages for different applications. A single or a few LED junctions may be packed in one miniature device for use as an indicator or pilot lamp. An LED array may include controlling circuits within the same package, which may range from a simple resistor, blinking or color changing control, or an addressable controller for RGB devices. Higher-powered white-emitting devices will be mounted on heat sinks and will be used for illumination. Alphanumeric displays in dot matrix or bar formats are widely available. Special packages permit connection of LEDs to optical fibers for high-speed data communication links.

### Miniature

These are mostly single-die LEDs used as indicators, and they come in various sizes from 1.8 mm to 10 mm, through-hole and surface mount packages. Typical current ratings range from around 1 mA to above 20 mA. LED's can be soldered to a flexible PCB strip to form LED tape popularly used for decoration.

Common package shapes include round, with a domed or flat top, rectangular with a flat top (as used in bar-graph displays), and triangular or square with a flat top. The encapsulation may also be clear or tinted to improve contrast and viewing angle. Infrared devices may have a black tint to block visible light while passing infrared radiation, such as the Osram SFH 4546.

5 V and 12 V LEDs are ordinary miniature LEDs that have a series resistor for direct connection to a 5 V or 12 V supply.

### High-power

High-power LEDs (HP-LEDs) or high-output LEDs (HO-LEDs) can be driven at currents from hundreds of mA to more than an ampere, compared with the tens of mA for other LEDs. Some can emit over a thousand lumens. LED power densities up to 300 W/cm2 have been achieved. Since overheating is destructive, the HP-LEDs must be mounted on a heat sink to allow for heat dissipation. If the heat from an HP-LED is not removed, the device fails in seconds. One HP-LED can often replace an incandescent bulb in a flashlight, or be set in an array to form a powerful LED lamp.

Some HP-LEDs in this category are the Nichia 19 series, Lumileds Rebel Led, Osram Opto Semiconductors Golden Dragon, and Cree X-lamp. As of September 2009, some HP-LEDs manufactured by Cree exceed 105 lm/W.

Examples for Haitz's law—which predicts an exponential rise in light output and efficacy of LEDs over time—are the CREE XP-G series LED, which achieved 105 lm/W in 2009 and the Nichia 19 series with a typical efficacy of 140 lm/W, released in 2010.

### AC-driven

LEDs developed by Seoul Semiconductor can operate on AC power without a DC converter. For each half-cycle, part of the LED emits light and part is dark, and this is reversed during the next half-cycle. The efficiency of this type of HP-LED is typically 40 lm/W. A large number of LED elements in series may be able to operate directly from line voltage. In 2009, Seoul Semiconductor released a high DC voltage LED, named 'Acrich MJT', capable of being driven from AC power with a simple controlling circuit. The low-power dissipation of these LEDs affords them more flexibility than the original AC LED design.

### Strip

An LED strip light is a flexible circuit board populated by surface-mount LEDs and other components that usually comes with an adhesive backing. LED lamps have been widely adopted in personal, professional, and hobbyist environments for their aesthetic, functionality, and flexibility. Traditionally, strip lights had been used solely in accent lighting, backlighting, task lighting, and decorative lighting applications, such as cove lighting.

LED strip lights were first produced in the early 2000s. Since then, increased luminous efficacy and higher-power SMDs have allowed them to be used in applications such as high brightness task lighting, fluorescent and halogen lighting fixture replacements, indirect lighting applications, ultraviolet inspection during manufacturing processes, set and costume design, and growing plants.

There are many types of LED Strips each with different codenames and LED types. Each one can vary in input power, led spacing, color capability and more.

### Application-specific

**Flashing**

Flashing LEDs are used as attention seeking indicators without requiring external electronics. Flashing LEDs resemble standard LEDs but they contain an integrated

voltage regulator

and a

multivibrator

circuit that causes the LED to flash with a typical period of one second. In diffused lens LEDs, this circuit is visible as a small black dot. Most flashing LEDs emit light of one color, but more sophisticated devices can flash between multiple colors and even fade through a color sequence using RGB color mixing. Flashing SMD LEDs in the 0805 and other size formats have been available since early 2019.

**Flickering**

Simple electronic circuits integrated into the LED package have been around since at least 2011 which produce a random LED intensity pattern reminiscent of a flickering

candle

.

Reverse engineering

in 2024 has suggested that some flickering LEDs with automatic sleep and wake modes might be using an integrated

8-bit

microcontroller

for such functionally.

Sometimes a flickering effect might happen due to an electric malfunction.

**Bi-color**

Bi-color LEDs contain two different LED emitters in one case. There are two types of these. One type consists of two dies connected to the same two leads

antiparallel

to each other. Current flow in one direction emits one color, and current in the opposite direction emits the other color. The other type consists of two dies with separate leads for both dies and another lead for common anode or cathode so that they can be controlled independently. The most common bi-color combination is

red/traditional green

. Others include amber/traditional green, red/pure green, red/blue, and blue/pure green.

**RGB tri-color**

Tri-color LEDs contain three different LED emitters in one case. Each emitter is connected to a separate lead so they can be controlled independently. A four-lead arrangement is typical with one common lead (anode or cathode) and an additional lead for each color. Others have only two leads (positive and negative) and have a built-in electronic controller.

RGB

LEDs consist of one red, one green, and one blue LED.

By independently

adjusting

each of the three, RGB LEDs are capable of producing a wide color gamut. Unlike dedicated-color LEDs, these do not produce pure wavelengths. Modules may not be optimized for smooth color mixing.

**Decorative-multicolor**

Decorative-multicolor LEDs incorporate several emitters of different colors supplied by only two lead-out wires. Colors are switched internally by varying the supply voltage.

**Alphanumeric**

Alphanumeric LEDs are available in

seven-segment

,

starburst

, and

dot-matrix

format. Seven-segment displays handle all numbers and a limited set of letters. Starburst displays can display all letters. Dot-matrix displays typically use 5×7 pixels per character. Seven-segment LED displays were in widespread use in the 1970s and 1980s, but rising use of

liquid-crystal displays

, with their lower power needs and greater display flexibility, has reduced the popularity of numeric and alphanumeric LED displays.

**Digital RGB**

Digital RGB addressable LEDs contain their own "smart" control electronics. In addition to power and ground, these provide connections for data-in, data-out, clock and sometimes a strobe signal. These are connected in a

daisy chain

, which allows individual LEDs in a long

LED strip light

to be easily controlled by a microcontroller. Data sent to the first LED of the chain can control the brightness and color of each LED independently of the others. They are used where a combination of maximum control and minimum visible electronics are needed such as strings for Christmas and LED matrices. Some even have refresh rates in the kHz range, allowing for basic video applications. These devices are known by their part number (

WS2812

being common) or a brand name such as

NeoPixel

.

**Filament**

An

LED filament

consists of multiple LED chips connected in series on a common longitudinal substrate that forms a thin rod reminiscent of a traditional incandescent filament.

These are being used as a low-cost decorative alternative for traditional light bulbs that are being phased out in many countries. The filaments use a rather high voltage, allowing them to work efficiently with mains voltages. Often a simple rectifier and capacitive current limiting are employed to create a low-cost replacement for a traditional light bulb without the complexity of the low voltage, high current converter that single die LEDs need.

Usually, they are packaged in bulb similar to the lamps they were designed to replace, and filled with inert gas at slightly lower than ambient pressure to remove heat efficiently and prevent corrosion.

**Chip-on-board arrays**

Surface-mounted LEDs are frequently produced in

chip on board

(COB) arrays, allowing better heat dissipation than with a single LED of comparable luminous output.

The LEDs can be arranged around a cylinder, and are called "corn cob lights" because of the rows of yellow LEDs.


## Considerations for use

- Efficiency: LEDs emit more lumens per watt than incandescent light bulbs. The efficiency of LED lighting fixtures is not affected by shape and size, unlike fluorescent light bulbs or tubes.
- Size: LEDs can be very small (smaller than 2 mm2) and are easily attached to printed circuit boards.

### Power sources

The current in an LED or other diodes rises exponentially with the applied voltage (see Shockley diode equation), so a small change in voltage can cause a large change in current. Current through the LED must be regulated by an external circuit such as a constant current source to prevent damage.

LEDs are sensitive to voltage. They must be supplied with a voltage above their threshold voltage and a current below their rating. Current and lifetime change greatly with a small change in applied voltage. They thus require a current-regulated supply (usually just a series resistor for indicator LEDs).

Efficiency droop: The efficiency of LEDs decreases as the electric current increases. Heating also increases with higher currents, which compromises LED lifetime. These effects put practical limits on the current through an LED in high power applications.

### Electrical polarity

Unlike a traditional incandescent lamp, an LED will light only when voltage is applied in the forward direction of the diode. No current flows and no light is emitted if voltage is applied in the reverse direction. If the reverse voltage exceeds the breakdown voltage, which is typically about five volts, a large current flows and the LED will be damaged. If the reverse current is sufficiently limited to avoid damage, the reverse-conducting LED is a useful noise diode.

By definition, the energy band gap of any diode is higher when reverse-biased than when forward-biased. Because the band gap energy determines the wavelength of the light emitted, the color cannot be the same when reverse-biased. The reverse breakdown voltage is sufficiently high that the emitted wavelength cannot be similar enough to still be visible. Though dual-LED packages exist that contain a different color LED in each direction, it is not expected that any single LED element can emit visible light when reverse-biased.

It is not known if any zener diode could exist that emits light only in reverse-bias mode. Uniquely, this type of LED would conduct when connected backwards.

### Appearance

- Color: LEDs can emit light of an intended color without using any color filters as traditional lighting methods need. This is more efficient and can lower initial costs.
- Cool light: In contrast to most light sources, LEDs radiate very little heat in the form of IR that can cause damage to sensitive objects or fabrics. Wasted energy is dispersed as heat through the base of the LED.
- Color rendition: Most cool-white LEDs have spectra that differ significantly from a black body radiator like the sun or an incandescent light. The spike at 460 nm and dip at 500 nm can make the color of objects appear differently under cool-white LED illumination than sunlight or incandescent sources, due to metamerism, red surfaces being rendered particularly poorly by typical phosphor-based cool-white LEDs. The same is true with green surfaces. The quality of color rendition of an LED is measured by the Color Rendering Index (CRI).
- Dimming: LEDs can be dimmed either by pulse-width modulation or lowering the forward current. This pulse-width modulation is why LED lights, particularly headlights on cars, when viewed on camera or by some people, seem to flash or flicker. This is a type of stroboscopic effect.

### Light properties

- Switch on time: LEDs light up extremely quickly. A typical red indicator LED achieves full brightness in under a microsecond. LEDs used in communications devices can have even faster response times.
- Focus: The solid package of the LED can be designed to focus its light. Incandescent and fluorescent sources often require an external reflector to collect light and direct it in a usable manner. For larger LED packages total internal reflection (TIR) lenses are often used to the same effect. When large quantities of light are needed, many light sources such as LED chips are usually deployed, which are difficult to focus or collimate on the same target.
- Area light source: Single LEDs do not approximate a point source of light giving a spherical light distribution, but rather a lambertian distribution. So, LEDs are difficult to apply to uses needing a spherical light field. Different fields of light can be manipulated by the application of different optics or "lenses". LEDs cannot provide divergence below a few degrees.

### Reliability

- Shock resistance: LEDs, being solid-state components, are difficult to damage with external shock, unlike fluorescent and incandescent bulbs, which are fragile.
- Thermal runaway: Parallel strings of LEDs will not share current evenly due to the manufacturing tolerances in their forward voltage. Running two or more strings from a single current source may result in LED failure as the devices warm up. If forward voltage binning is not possible, a circuit is required to ensure even distribution of current between parallel strands.
- Slow failure: LEDs mainly fail by dimming over time, rather than the abrupt failure of incandescent bulbs.
- Lifetime: LEDs can have a relatively long useful life. One report estimates 35,000 to 50,000 hours of useful life for white LEDs, though time to complete failure may be shorter or longer. Fluorescent tubes typically are rated at about 10,000 to 25,000 hours, depending partly on the conditions of use, and incandescent light bulbs at 1,000 to 2,000 hours. Several DOE demonstrations have shown that reduced maintenance costs from this extended lifetime, rather than energy savings, is the primary factor in determining the payback period for an LED product.
- Cycling: LEDs are ideal for uses subject to frequent on-off cycling, unlike incandescent and fluorescent lamps that fail faster when cycled often, or high-intensity discharge lamps (HID lamps) that require a long time to warm up to full output and to cool down before they can be lighted again if they are being restarted.
- Temperature dependence: LED performance largely depends on the ambient temperature of the operating environment – or thermal management properties. Overdriving an LED in high ambient temperatures may result in overheating the LED package, eventually leading to device failure. An adequate heat sink is needed to maintain long life. This is especially important in automotive, medical, and military uses where devices must operate over a wide range of temperatures, and require low failure rates.


## Manufacturing

LED manufacturing involves multiple steps, including epitaxy, chip processing, chip separation, and packaging.

In a typical LED manufacturing process, encapsulation is performed after probing, dicing, die transfer from wafer to package, and wire bonding or flip chip mounting, perhaps using indium tin oxide, a transparent electrical conductor. In this case, the bond wire(s) are attached to the ITO film that has been deposited in the LEDs.

Flip chip circuit on board (COB) is a technique that can be used to manufacture LEDs.


## Colors and materials

Conventional LEDs are made from a variety of inorganic semiconductor materials. The following table shows the available colors with wavelength range, voltage drop and material:

|   | Color | Wavelength (nm) | Voltage (V) | Semiconductor material |
|---|---|---|---|---|
|   | Infrared | *λ* > 760 | Δ*V* < 1.9 | Gallium arsenide (GaAs) Aluminium gallium arsenide (AlGaAs) |
|   | Red | 610 < *λ* < 760 | 1.63 < Δ*V* < 2.03 | Aluminium gallium arsenide (AlGaAs) Gallium arsenide phosphide (GaAsP) Aluminium gallium indium phosphide (AlGaInP) Gallium(III) phosphide (GaP) |
|   | Orange | 590 < *λ* < 610 | 2.03 < Δ*V* < 2.10 | Gallium arsenide phosphide (GaAsP) Aluminium gallium indium phosphide (AlGaInP) Gallium(III) phosphide (GaP) |
|   | Yellow | 570 < *λ* < 590 | 2.10 < Δ*V* < 2.18 | Gallium arsenide phosphide (GaAsP) Aluminium gallium indium phosphide (AlGaInP) Gallium(III) phosphide (GaP) |
|   | Green | 500 < *λ* < 570 | 1.9 < Δ*V* < 4.0 | Indium gallium nitride (InGaN) / Gallium(III) nitride (GaN) Gallium(III) phosphide (GaP) Aluminium gallium indium phosphide (AlGaInP) Aluminium gallium phosphide (AlGaP) |
|   | Blue | 450 < *λ* < 500 | 2.48 < Δ*V* < 3.7 | Zinc selenide (ZnSe) Indium gallium nitride (InGaN) Silicon carbide (SiC) as substrate Silicon (Si) as substrate — (under development) |
|   | Violet | 400 < *λ* < 450 | 2.76 < Δ*V* < 4.0 | Indium gallium nitride (InGaN) |
|   | Purple | multiple types | 2.48 < Δ*V* < 3.7 | Dual blue/red LEDs, blue with red phosphor, or white with purple plastic |
|   | Ultraviolet | *λ* < 400 | 3.1 < Δ*V* < 4.4 | Diamond (235 nm) Boron nitride (215 nm) Aluminium nitride (AlN) (210 nm) Aluminium gallium nitride (AlGaN) Aluminium gallium indium nitride (AlGaInN) — (down to 210 nm) |
|   | White | Broad spectrum | 2.7 < Δ*V* < 3.5 | Blue diode with yellow phosphor or violet/UV diode with multi-color phosphor |
