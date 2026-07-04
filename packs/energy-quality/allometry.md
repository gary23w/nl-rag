---
title: "Allometry"
source: https://en.wikipedia.org/wiki/Allometry
domain: energy-quality
license: CC-BY-SA-4.0
tags: energy quality
fetched: 2026-07-04
---

# Allometry

Skeleton of an

elephant

Skeleton of a

tiger quoll

(Dasyurus maculatus)

.

The proportionately thicker bones in the elephant are an example of allometric scaling

**Allometry** (Ancient Greek ἄλλος *állos* "other", μέτρον *métron* "measurement") is the study of the relationship of body size to shape, anatomy, physiology and behaviour, first outlined by Otto Snell in 1892, by D'Arcy Thompson in 1917 in *On Growth and Form* and by Julian Huxley in 1932.

## Overview

Allometry is a well-known study, particularly in statistical shape analysis for its theoretical developments, as well as in biology for practical applications to the differential growth rates of the parts of a living organism's body. One application is in the study of various insect species (e.g., Hercules beetles), where a small change in overall body size can lead to an enormous and disproportionate increase in the dimensions of appendages such as legs, antennae, or horns. The relationship between the two measured quantities is often expressed as a power law equation (allometric equation) which expresses a remarkable scale symmetry:

$y=kx^{a},$

or in a logarithmic form,

$\log y=a\log x+\log k,$

or similarly,

$\ln y=a\ln x+\ln k,$

where a is the scaling exponent of the law. Methods for estimating this exponent from data can use type-2 regressions, such as major axis regression or reduced major axis regression, as these account for the variation in both variables, contrary to least-squares regression, which does not account for error variance in the independent variable (e.g., log body mass). Other methods include measurement-error models and a particular kind of principal component analysis.

The allometric equation can also be acquired as a solution of the differential equation

${\frac {dy}{y}}=a{\frac {dx}{x}}.$

Allometry often studies shape differences in terms of ratios of the objects' dimensions. Two objects of different size, but common shape, have their dimensions in the same ratio. Take, for example, a biological object that grows as it matures. Its size changes with age, but the shapes are similar. Studies of ontogenetic allometry often use lizards or snakes as model organisms both because they lack parental care after birth or hatching and because they exhibit a large range of body sizes between the juvenile and adult stage. Lizards often exhibit allometric changes during their ontogeny.

In addition to studies that focus on growth, allometry also examines shape variation among individuals of a given age (and sex), which is referred to as static allometry. Comparisons of species are used to examine interspecific or evolutionary allometry (see also Phylogenetic comparative methods).

## Isometric scaling and geometric similarity

| Group | Factor | Length range |
|---|---|---|
| Insects | 1000 | 10−4 to 10−1 m |
| Fish | 1000 | 10−2 to 10+1 m |
| Mammals | 1000 | 10−1 to 10+2 m |
| Vascular plants | 10,000 | 10−2 to 10+2 m |
| Algae | 100,000 | 10−5 to 100 m |

Isometric scaling happens when proportional relationships are preserved as size changes during growth or over evolutionary time. An example is found in frogs—aside from a brief period during the few weeks after metamorphosis, frogs grow isometrically. Therefore, a frog whose legs are as long as its body will retain that relationship throughout its life, even if the frog itself increases in size tremendously.

Isometric scaling is governed by the square–cube law. An organism which doubles in length isometrically will find that the surface area available to it will increase fourfold, while its volume and mass will increase by a factor of eight. This can present problems for organisms. In the case of above, the animal now has eight times the biologically active tissue to support, but the surface area of its respiratory organs has only increased fourfold, creating a mismatch between scaling and physical demands. Similarly, the organism in the above example now has eight times the mass to support on its legs, but the strength of its bones and muscles is dependent upon their cross-sectional area, which has only increased fourfold. Therefore, this hypothetical organism would experience twice the bone and muscle loads of its smaller version. This mismatch can be avoided either by being "overbuilt" when small or by changing proportions during growth, called allometry.

Isometric scaling is often used as a null hypothesis in scaling studies, with 'deviations from isometry' considered evidence of physiological factors forcing allometric growth.

## Allometric scaling

Allometric scaling is any change that deviates from isometry. A classic example discussed by Galileo in his *Dialogues Concerning Two New Sciences* is the skeleton of mammals. The skeletal structure becomes much stronger and more robust relative to the size of the body as the body size increases. Allometry is often expressed in terms of a scaling exponent based on body mass, or body length (snout–vent length, total length, etc.). A perfectly allometrically scaling organism would see all volume-based properties change proportionally to the body mass, all surface area-based properties change with mass to the power of 2/3, and all length-based properties change with mass to the power of 1/3. If, after statistical analyses, for example, a volume-based property was found to scale to mass to the 0.9th power, then this would be called "negative allometry", as the values are smaller than predicted by isometry. Conversely, if a surface area-based property scales to mass to the 0.8th power, the values are higher than predicted by isometry and the organism is said to show "positive allometry". One example of positive allometry occurs among species of monitor lizards (family Varanidae), in which the limbs are relatively longer in larger-bodied species. The same is true for some fish, e.g. the muskellunge, the weight of which grows with about the power of 3.325 of its length. A 30-inch (76 cm) muskellunge will weigh about 8 pounds (3.6 kg), while a 40-inch (100 cm) muskellunge will weigh about 18 pounds (8.2 kg), so 33% longer length will more than double the weight.

## Determining if a system is scaling with allometry

To determine whether isometry or allometry is present, an expected relationship between variables needs to be determined to compare data to. This is important in determining if the scaling relationship in a dataset deviates from an expected relationship (such as those that follow isometry). Using tools such as dimensional analysis is very helpful in determining expected slope. This 'expected' slope, as it is known, is essential for detecting allometry because scaling variables are comparisons to other things. Saying that mass scales with a slope of 5 in relation to length doesn't have much meaning unless knowing the isometric slope is 3, meaning in this case, the mass is increasing extremely fast. For example, different sized frogs should be able to jump the same distance according to the geometric similarity model proposed by Hill 1950 and interpreted by Wilson 2000, but in actuality larger frogs do jump longer distances.

Data gathered in science do not fall neatly in a straight line, so data transformations are useful. It is also important to remember what is being compared in the data. Comparing a characteristic such as head length to head width might yield different results from comparing head length to body length. That is, different characteristics may scale differently. A common way to analyze data such as those collected in scaling is to use log-transformation.

There are two reasons why logarithmic transformation should be used to study allometry —a biological reason and a statistical reason. Log-log transformation places numbers into a geometric domain so that proportional deviations are represented consistently, independent of the scale and units of measurement. In biology, this is appropriate because many biological phenomena (e.g., growth, reproduction, metabolism, sensation) are fundamentally multiplicative. Statistically, it is beneficial to transform both axes using logarithms and then perform a linear regression. This will normalize the data set and make it easier to analyze trends using the slope of the line. Before analyzing data, it is important to have a predicted slope of the line to compare the analysis to.

After data are log-transformed and linearly regressed, comparisons can then use least squares regression with 95% confidence intervals or reduced major axis analysis. Sometimes, the two analyses can yield different results, but often they do not. If the expected slope is outside the confidence intervals, allometry is present. If the mass in this imaginary animal scaled with a slope of 5, which was a statistically significant value, then mass would scale very fast in this animal versus the expected value. It would scale with positive allometry. If the expected slope were 3 and in reality, in a certain organism mass scaled with 1 (assuming this slope is statistically significant), it would be negatively allometric.

### Examples

To find the expected slope for the relationship between mass and the characteristic length of an animal (see figure), the units of mass (M) from the y-axis are divided by the units of the x-axis, Length (L). The expected slope on a double-logarithmic plot of L3 / L is 3 ( ${\frac {\log _{10}\mathrm {L} ^{3}}{\log _{10}\mathrm {L} }}=3$ ). This is the slope of a straight line.

Another example: Force is dependent on the cross-sectional area of muscle (CSA), which is L2. If comparing force to a length, then the expected slope is 2. Alternatively, this analysis may be accomplished with a power regression. Plot the relationship between the data onto a graph. Fit this to a power curve (depending on the stats program, this can be done multiple ways), and it will give an equation with the form: *y*=*Zx**n*, where *n* is the number. That "number" is the relationship between the data points. The downside, to this form of analysis, is that it makes it a little more difficult to do statistical analyses.

## Physiological scaling

Many physiological and biochemical processes (such as heart rate, respiration rate or the maximum reproduction rate) show scaling, mostly associated with the ratio between surface area and mass (or volume) of the animal. The metabolic rate of an individual animal is also subject to scaling.

### Metabolic rate and body mass

In plotting an animal's basal metabolic rate (BMR) against the animal's own body mass, a logarithmic straight line is obtained, indicating a power-law dependence. Overall metabolic rate in animals is generally accepted to show negative allometry, scaling to mass to a power of ≈ 0.75, known as Kleiber's law, 1932. This means that larger-bodied species (e.g., elephants) have lower mass-specific metabolic rates and lower heart rates, as compared with smaller-bodied species (e.g., mice). The straight line generated from a double logarithmic scale of metabolic rate in relation to body mass is known as the "mouse-to-elephant curve". These relationships of metabolic rates, times, and internal structure have been explained as, "an elephant is approximately a blown-up gorilla, which is itself a blown-up mouse."

Max Kleiber contributed the following allometric equation for relating the BMR to the body mass of an animal. Statistical analysis of the intercept did not vary from 70 and the slope was not varied from 0.75, thus:

${\text{Metabolic rate}}=70M^{0.75}$

(although the universality of this relation has been disputed both empirically and theoretically

)

where M is body mass, and metabolic rate is measured in kcal per day.

Consequently, the body mass itself can explain the majority of the variation in the BMR. After the body mass effect, the taxonomy of the animal plays the next most significant role in the scaling of the BMR. The further speculation that environmental conditions play a role in BMR can only be properly investigated once the role of taxonomy is established. The challenge with this lies in the fact that a shared environment also indicates a common evolutionary history and thus a close taxonomic relationship. There are strides currently in research to overcome these hurdles; for example, an analysis in muroid rodents, the mouse, hamster, and vole type, took into account taxonomy. Results revealed the hamster (warm dry habitat) had lowest BMR and the mouse (warm wet dense habitat) had the highest BMR. Larger organs could explain the high BMR groups, along with their higher daily energy needs. Analyses such as these demonstrate the physiological adaptations to environmental changes that animals undergo.

Energy metabolism is subjected to the scaling of an animal and can be overcome by an individual's body design. The metabolic scope for an animal is the ratio of resting and maximum rate of metabolism for that particular species as determined by oxygen consumption. Oxygen consumption VO2 and maximum oxygen consumption VO2 max. Oxygen consumption in species that differ in body size and organ system dimensions show a similarity in their charted VO2 distributions indicating that, despite the complexity of their systems, there is a power law dependence of similarity; therefore, universal patterns are observed in diverse animal taxonomy.

Across a broad range of species, allometric relations are not necessarily linear on a log-log scale. For example, the maximal running speeds of mammals show a complicated relationship with body mass, and the fastest sprinters are of intermediate body size.

### Allometric muscle characteristics

The muscle characteristics of animals are similar in a wide range of animal sizes, though muscle sizes and shapes can and often do vary depending on environmental constraints placed on them. The muscle tissue itself maintains its contractile characteristics and does not vary depending on the size of the animal. Physiological scaling in muscles affects the number of muscle fibers and their intrinsic speed to determine the maximum power and efficiency of movement in a given animal. The speed of muscle recruitment varies roughly in inverse proportion to the cube root of the animal's weight (compare the intrinsic frequency of the sparrow's flight muscle to that of a stork).

$\mathrm {frequency} ={\frac {1}{\mathrm {mass} ^{1/3}}}$

For inter-species allometric relations related to such ecological variables as maximal reproduction rate, attempts have been made to explain scaling within the context of dynamic energy budget theory and the metabolic theory of ecology. However, such ideas have been less successful.

### Allometry of legged locomotion

#### Methods of study

Allometry has been used to study patterns in locomotive principles across a broad range of species. Such research has been done in pursuit of a better understanding of animal locomotion, including the factors that different gaits seek to optimize. Allometric trends observed in extant animals have even been combined with evolutionary algorithms to form realistic hypotheses concerning the locomotive patterns of extinct species. These studies have been made possible by the remarkable similarities among disparate species' locomotive kinematics and dynamics, "despite differences in morphology and size".

Allometric study of locomotion involves the analysis of the relative sizes, masses, and limb structures of similarly shaped animals and how these features affect their movements at different speeds. Patterns are identified based on dimensionless Froude numbers, which incorporate measures of animals' leg lengths, speed or stride frequency, and weight.

Alexander incorporates Froude-number analysis into his "dynamic similarity hypothesis" of gait patterns. Dynamically similar gaits are those between which there are constant coefficients that can relate linear dimensions, time intervals, and forces. In other words, given a mathematical description of gait A and these three coefficients, one could produce gait B, and vice versa. The hypothesis itself is as follows: "animals of different sizes tend to move in dynamically similar fashion whenever the ratio of their speed allows it." While the dynamic similarity hypothesis may not be a truly unifying principle of animal gait patterns, it is a remarkably accurate heuristic.

It has also been shown that living organisms of all shapes and sizes utilize spring mechanisms in their locomotive systems, probably in order to minimize the energy cost of locomotion. The allometric study of these systems has fostered a better understanding of why spring mechanisms are so common, how limb compliance varies with body size and speed, and how these mechanisms affect general limb kinematics and dynamics.

#### Principles of legged locomotion identified through allometry

- Alexander found that animals of different sizes and masses traveling with the same Froude number consistently exhibit similar gait patterns.
- Duty factors—percentages of a stride during which a foot maintains contact with the ground—remain relatively constant for different animals moving with the same Froude number.
- The dynamic similarity hypothesis states that "animals of different sizes tend to move in dynamically similar fashion whenever the ratio of their speed allows it".
- Body mass has even more of an effect than speed on limb dynamics.
- Leg stiffness, $k_{\text{leg}}={\frac {\text{peak force}}{\text{peak displacement}}}$ , is proportional to $M^{0.67}$ , where M is body mass.
- Peak force experienced throughout a stride is proportional to $M^{0.97}$ .
- The amount by which a leg shortens during a stride (i.e. its peak displacement) is proportional to $M^{0.30}$ .
- The angle swept by a leg during a stride is proportional to $M^{-0.034}$ .
- The mass-specific work rate of a limb is proportional to $M^{0.11}$ .

### Drug dose scaling

The physiological effect of drugs and other substances in many cases scales allometrically. For example, plasma concentration of carotenoids scales to the three-quarter power of mass in nine predatory and scavenger raptor species.

West, Brown, and Enquist in 1997 derived a hydrodynamic theory to explain the universal fact that metabolic rate scales as the 3⁄4 power with body weight. They also showed why lifespan scales as the +1⁄4 power and heart rate as the -1⁄4 power. Blood flow (+3⁄4) and resistance (-3⁄4) scale in the same way, leading to blood pressure being constant across species.

Hu and Hayton in 2001 discussed whether the basal metabolic rate scale is a 2⁄3 or 3⁄4 power of body mass. The exponent of 3⁄4 might be used for substances that are eliminated mainly by metabolism, or by metabolism and excretion combined, while 2⁄3 might apply for drugs that are eliminated mainly by renal excretion.

An online allometric scaler of drug doses based on the above work is available.

The US Food and Drug Administration (FDA) published guidance in 2005 giving a flow chart that presents the decisions and calculations used to generate the maximum recommended starting dose in drug clinical trials from animal data.

## Allometric scaling in fluid locomotion

The mass and density of an organism have a large effect on the organism's locomotion through a fluid. For example, a tiny organism uses flagella and can effectively move through a fluid it is suspended in, while on the other end of the scale, a blue whale is much more massive and dense relative to the viscosity of the fluid compared to a bacterium in the same medium. The way in which the fluid interacts with the external boundaries of the organism is important with locomotion through the fluid. For streamlined swimmers, the resistance or drag determines the performance of the organism. This drag or resistance can be seen in two distinct flow patterns: laminar flow, where the fluid is relatively uninterrupted after the organism moves through it, and turbulent flow, where the fluid moves roughly around an organism, creating vortices that absorb energy from the propulsion or momentum of the organism. Scaling also affects locomotion through a fluid because of the energy needed to propel an organism and keep up velocity through momentum. The rate of oxygen consumption per gram body size decreases consistently with increasing body size.

In general, smaller, more streamlined organisms create laminar flow (*R* < 0.5x106), whereas larger, less streamlined organisms produce turbulent flow (*R* > 2.0×106). Also, increase in velocity (V) increases turbulence, which can be proved using the Reynolds equation. In nature however, organisms such as a 6-foot-6-inch (1.98 m) dolphin moving at 15 knots does not have the appropriate Reynolds numbers for laminar flow (*R* = 107), but exhibit it in nature. G. A. Steven observed and documented dolphins moving at 15 knots alongside his ship leaving a single trail of light when phosphorescent activity in the sea was high. The factors that contribute are:

- the surface area of the organism and its effect on the fluid in which the organism lives.
- the velocity of an organism through fluid, which changes the dynamic of the flow around that organism – the shape of the organism becomes more important for laminar flow as velocity increases.
- the density and viscosity of the fluid.
- the length of the organism, as the surface area of just the front 2/3 of the organism has an effect on the drag.

The resistance to the motion of an approximately stream-lined solid through a fluid can be expressed by the formula: *C**fρ*(total surface)*V*2/2,where:

V = velocity

ρ

= density of fluid

C

f

= 1.33

R

− 1 (laminar flow)

R

=

Reynolds number

The Reynolds number *R* is given by *R* = *VL*/*ν*, where:

V

= velocity

L

= axial length of organism

ν

=

kinematic viscosity

(viscosity/density)

Notable Reynolds numbers:

R

< 0.5 million = laminar flow threshold

R

> 2.0 million = turbulent flow threshold

Scaling also has an effect on the performance of organisms in fluid. This is extremely important for marine mammals and other marine organisms that rely on atmospheric oxygen for respiration and survival. This can affect how fast an organism can propel itself efficiently or how long and deep it can dive. Heart mass and lung volume are important in determining how scaling can affect metabolic function and efficiency.

Aquatic mammals, like other mammals, have the same size heart proportional to their bodies. In general, mammals have hearts about 0.6% of their total body mass: ${\text{Heart weight}}=0.006{M}^{1.0}$ , where *M* is the body mass of the individual. Lung volume is also directly related to body mass in mammals (slope = 1.02). The lung has a volume of 63 ml for every kg of body mass, with the tidal volume at rest being 1/10 the lung volume. In addition, respiration costs with respect to oxygen consumption is scaled in the order of $M^{0.75}$ . This shows that mammals, regardless of size, have similarly scaled respiratory and cardiovascular systems and the same relative amount of blood: about 5.5% of body mass. This means that for similarly designed marine mammals, a larger individual can travel more efficiently, as it takes the same effort to move one body length. For example, large whales can migrate far distance in the oceans and not stop for rest. It is metabolically less expensive to be larger in body size. This goes for terrestrial and flying animals as well: smaller animals consume more oxygen per unit body mass than larger ones. The metabolic advantage in larger animals makes it possible for larger marine mammals to dive for longer durations of time than their smaller counterparts. That the heart rate is lower means that larger animals can carry more blood, which carries more oxygen. In conjuncture with the fact that mammals reparation costs scales in the order of $M^{0.75}$ , this shows having a larger body mass can be advantageous. More simply, a larger whale can hold more oxygen and at the same time demand less metabolically than a smaller whale.

Traveling long distances and deep dives are a combination of good stamina and also moving an efficient speed and in an efficient way to create laminar flow, reducing drag and turbulence. In sea water as the fluid, it traveling long distances in large mammals, such as whales, is facilitated by their neutral buoyancy and have their mass completely supported by the density of the sea water. On land, animals have to expend a portion of their energy during locomotion to fight the effects of gravity.

Flying organisms such as birds are also considered as moving through a fluid. In scaling birds of similar shape, it has also been seen that larger individuals have less metabolic costs per kg, as expected. Birds also have a variance in wing beat frequency. Beyond the compensation of larger wings per unit body mass, larger birds also have slower wing beat frequencies, allowing them to fly at higher altitudes, longer distances, and faster absolute speeds than smaller birds. Because of the dynamics of lift-based locomotion and the fluid dynamics, birds have a U-shaped curve for metabolic cost and velocity. Because flight, in air as the fluid, is metabolically more costly at the lowest and the highest velocities. On the other end, small organisms such as insects can make gain advantage from the viscosity of the fluid (air) that they are moving in. A wing-beat timed perfectly can effectively uptake energy from the previous stroke (Dickinson 2000). This form of wake capture allows an organism to recycle energy from the fluid or vortices within that fluid created by the organism itself. This same sort of wake capture occurs in aquatic organisms as well, and for organisms of all sizes. This dynamic of fluid locomotion allows smaller organisms to gain advantage because the effect on them from the fluid is much greater because of their relatively smaller size.

## Allometric engineering

Allometric engineering is a method for manipulating allometric relationships within or among groups.

## In characteristics of a city

Arguing that there are a number of analogous concepts and mechanisms between cities and biological entities, Bettencourt et al. showed a number of scaling relationships between observable properties of a city and the city size. GDP, "supercreative" employment, number of inventors, crime, spread of disease, and even pedestrian walking speeds scale with city population. This phenomenon goes under the name of urban scaling. Theoretical explanations for the presence of allometry in cities propose different mechanisms. Bettencourt’s model suggests that superlinear scaling arises from the quadratic growth of social interactions with population size under budget constraints. A different mechanism was proposed by Gomez-Lievano et al. in which superlinear scaling is linked to the exponential growth in outputs resulting from the combination of diverse, complementary factors (or capabilities) found in cities, which scale logarithmically with city size.

## Examples

Some examples of allometric laws:

- Kleiber's law, metabolic rate $q_{0}$ is proportional to body mass M raised to the $3/4$ power:

$q_{0}\sim M^{\frac {3}{4}}$

- breathing and heart rate t are both inversely proportional to body mass M raised to the $1/4$ power:

$t\sim M^{-{\frac {1}{4}}}$

- mass transfer contact area A and body mass M :

$A\sim M^{\frac {7}{8}}$

- the proportionality between the optimal cruising speed $V_{opt}$ of flying bodies (insects, birds, airplanes) and body mass M raised to the power $1/6$ :

$V_{\text{opt}}\sim M^{\frac {1}{6}}$

## Determinants of size in different species

Many factors go into the determination of body mass and size for a given animal. These factors often affect body size on an evolutionary scale, but conditions such as availability of food and habitat size can act much more quickly on a species. Other examples include the following:

- Physiological design

Basic physiological design plays a role in the size of a given species. For example, animals with a closed circulatory system are larger than animals with open or no circulatory systems.

- Mechanical design

Mechanical design can also determine the maximum allowable size for a species. Animals with tubular endoskeletons tend to be larger than animals with exoskeletons or hydrostatic skeletons.

- Habitat

An animal's habitat throughout its

evolution

is one of the largest determining factors in its size. On land, there is a positive correlation between body mass of the top species in the area and available land area.

However, there are a much greater number of "small" species in any given area. This is most likely determined by ecological conditions, evolutionary factors, and the availability of food; a small population of large predators depend on a much greater population of small prey to survive. In an aquatic environment, the largest animals can grow to have a much greater body mass than land animals where gravitational weight constraints are a factor.
