---
title: "Mercator projection"
source: https://en.wikipedia.org/wiki/Mercator_projection
domain: map-projections
license: CC-BY-SA-4.0
tags: map projection, mercator projection, coordinate reference system, geodetic datum
fetched: 2026-07-02
---

# Mercator projection

The **Mercator projection** (/mərˈkeɪtər/) is a conformal cylindrical map projection first presented by Flemish geographer and mapmaker Gerardus Mercator in 1569. In the 18th century, it became the standard map projection for navigation due to its property of representing rhumb lines as straight lines. When applied to world maps, the Mercator projection inflates the size of lands the farther they are from the equator. Therefore, landmasses such as Greenland and Antarctica appear far larger than they actually are relative to landmasses near the equator. Its use for maps other than marine charts declined throughout the 20th century, but resurged in the 21st century due to characteristics favorable for World-Wide-Web maps.

## History

Joseph Needham, a historian of China, speculated that some star charts of the Chinese Song dynasty may have been drafted on the Mercator projection; however, this claim was presented without evidence, and astronomical historian Kazuhiko Miyajima concluded using cartometric analysis that these charts used an equirectangular projection instead.

In the 13th century, the earliest extant portolan charts of the Mediterranean sea, which are generally not believed to be based on any deliberate map projection, included windrose networks of criss-crossing lines which could be used to help set a ship's bearing in sailing between locations on the chart; the region of Earth covered by such charts was small enough that a course of constant bearing would be approximately straight on the chart. The charts have startling accuracy not found in the maps constructed by contemporary European or Arab scholars, and their construction remains enigmatic; based on cartometric analysis which seems to contradict the scholarly consensus, they have been speculated to have originated in some unknown pre-medieval cartographic tradition, possibly evidence of some ancient understanding of the Mercator projection.

German polymath Erhard Etzlaub engraved miniature "compass maps" (about 10×8 cm) of Europe and parts of Africa that spanned latitudes 0°–67° to allow adjustment of his portable pocket-size sundials. The projection found on these maps, dating to 1511, was stated by John Snyder in 1987 to be the same projection as Mercator's. However, given the geometry of a sundial, these maps may well have been based on the similar central cylindrical projection, a limiting case of the gnomonic projection, which is the basis for a sundial. Snyder amended his assessment to "a similar projection" in 1993.

Portuguese mathematician and cosmographer Pedro Nunes first described the mathematical principle of the rhumb line or loxodrome, a path with constant bearing as measured relative to true north, which can be used in marine navigation to pick which compass bearing to follow. In 1537, he proposed constructing a nautical atlas composed of several large-scale sheets in the equirectangular projection as a way to minimize distortion of directions. If these sheets were brought to the same scale and assembled, they would approximate the Mercator projection.

In 1541, Flemish geographer and mapmaker Gerardus Mercator included a network of rhumb lines on a terrestrial globe he made for Nicolas Perrenot.

In 1569, Mercator announced a new projection by publishing a large world map measuring 202 by 124 cm (80 by 49 in) and printed in eighteen separate sheets. Mercator titled the map *Nova et Aucta Orbis Terrae Descriptio ad Usum Navigantium Emendata*: "A new and augmented description of Earth corrected for the use of sailors". This title, along with an elaborate explanation for using the projection that appears as a section of text on the map, shows that Mercator understood exactly what he had achieved and that he intended the projection to aid navigation. Mercator never explained the method of construction or how he arrived at it. Various hypotheses have been tendered over the years, but in any case Mercator's friendship with Pedro Nunes and his access to the loxodromic tables Nunes created likely aided his efforts.

English mathematician Edward Wright published the first accurate tables for constructing the projection in 1599 and, in more detail, in 1610, calling his treatise "Certaine Errors in Navigation". The first mathematical formulation was publicized around 1645 by a mathematician named Henry Bond (c. 1600–1678). However, the mathematics involved were developed but never published by mathematician Thomas Harriot starting around 1589.

The development of the Mercator projection represented a major breakthrough in the nautical cartography of the 16th century. However, it was much ahead of its time, since the old navigational and surveying techniques were not compatible with its use in navigation. Two main problems prevented its immediate application: the impossibility of determining the longitude at sea with adequate accuracy and the fact that magnetic directions, instead of geographical directions, were used in navigation. Only in the middle of the 18th century, after the marine chronometer was invented and the spatial distribution of magnetic declination was known, could the Mercator projection be fully adopted by navigators.

Despite those position-finding limitations, the Mercator projection can be found in many world maps in the centuries following Mercator's first publication. However, it did not begin to dominate world maps until the 19th century, when the problem of position determination had been largely solved. Once the Mercator became the usual projection for commercial and educational maps, it came under persistent criticism from cartographers for its unbalanced representation of landmasses and its inability to usefully show the polar regions.

The criticisms leveled against inappropriate use of the Mercator projection resulted in a flurry of new inventions in the late 19th and early 20th century, often directly touted as alternatives to the Mercator. Due to these pressures, publishers gradually reduced their use of the projection over the course of the 20th century. However, the advent of Web mapping gave the projection an abrupt resurgence in the form of the Web Mercator projection.

Today, the Mercator can be found in marine charts, occasional world maps, and Web mapping services, but commercial atlases have largely abandoned it, and wall maps of the world can be found in many alternative projections. Google Maps, which relied on it since 2005, still uses it for local-area maps but dropped the projection from desktop platforms in 2017 for maps that are zoomed out of local areas. Many other online mapping services still exclusively use the Web Mercator.

## Properties

The Mercator projection can be visualized as the result of wrapping a cylinder tightly around a sphere, with the two surfaces *tangent* to (touching) each other along a circle halfway between the poles of their common axis, and then conformally unfolding the surface of the sphere outward onto the cylinder, meaning that at each point the projection uniformly scales the image of a small portion of the spherical surface without otherwise distorting it, preserving angles between intersecting curves. Afterward, this cylinder is unrolled onto a flat plane to make a map. In this interpretation, the scale of the surface is preserved exactly along the circle where the cylinder touches the sphere, but increases nonlinearly for points further from the contact circle. However, by uniformly shrinking the resulting flat map, as a final step, any pair of circles parallel to and equidistant from the contact circle can be chosen to have their scale preserved, called the *standard parallels*; then the region between chosen circles will have its scale smaller than on the sphere, reaching a minimum at the contact circle. This is sometimes visualized as a projection onto a cylinder which is *secant* to (cuts) the sphere, though this picture is misleading insofar as the standard parallels are not spaced the same distance apart on the map as the shortest distance between them through the interior of the sphere.

The original and most common aspect of the Mercator projection for maps of Earth is the normal aspect, for which the axis of the cylinder is Earth's axis of rotation which passes through the North and South poles, and the contact circle is Earth's equator. As for all cylindrical projections in normal aspect, circles of latitude and meridians of longitude are straight and perpendicular to each other on the map, forming a grid of rectangles. While circles of latitude on Earth are smaller the closer they are to the poles, they are stretched in an East–West direction to have uniform length on any cylindrical map projection. Among cylindrical projections, the Mercator projection is the unique projection which balances this East–West stretching by a precisely corresponding North–South stretching, so that at every location the scale is locally uniform and angles are preserved.

The Mercator projection in normal aspect maps trajectories of constant bearing (called *rhumb lines* or *loxodromes*) on a sphere to straight lines on the map, and is thus uniquely suited to marine navigation: courses and bearings are measured using a compass rose or protractor, and the corresponding directions are easily transferred from point to point, on the map, e.g. with the help of a parallel ruler.

Because the linear scale of a Mercator map in normal aspect increases with latitude, it distorts the size of geographical objects far from the equator and conveys a distorted perception of the overall geometry of the planet. At latitudes greater than 70° north or south, the Mercator projection is practically unusable, because the linear scale becomes infinitely large at the poles. A Mercator map can therefore never fully show the polar areas (but see Uses below for applications of the oblique and transverse Mercator projections).

The Mercator projection is often compared to and confused with the central cylindrical projection, which is the result of projecting points from the sphere onto a tangent cylinder along straight radial lines, as if from a light source placed at Earth's center. Both have extreme distortion far from the equator and cannot show the poles. However, they are different projections and have different properties.

## Distortion of sizes

As with all map projections, the shapes or sizes are distortions of the true layout of Earth's surface. The Mercator projection exaggerates areas far from the equator; the closer to Earth's poles, the greater the distortion.

### Examples of size distortion

- Greenland appears the same size as Africa, when in reality Africa's area is 14 times as large.
  - Greenland's real area is comparable to the Democratic Republic of the Congo's alone.
- Africa appears to be roughly the same size as South America, when in reality Africa is over one and a half times as large.
- Alaska appears to be the same size as Australia, although Australia is actually 4.5 times as large.
  - Alaska also takes as much area on the map as Brazil, whereas Brazil's area is nearly 5 times that of Alaska.
- Madagascar and Great Britain look about the same size, while Madagascar is actually more than twice as large as Great Britain.
- Antarctica, being located in the southernmost point of Earth where all longitudes converge, appears infinitely large.

### Criticism

Because of great land area distortions, critics like George Kellaway and Irving Fisher consider the projection unsuitable for general world maps. It has been conjectured to have influenced people's views of the world: because it shows countries near the Equator as too small when compared to those of Europe and North America, it has been supposed to cause people to consider those countries as less important. The areal exaggerations of the Mercator projection were suspected to have fuelled Donald Trump's attempt to annex Greenland in 2025, particularly in light of Trump's previous exclamation that "I love maps. And I always said, 'Look at the size of this. It's massive, and that should be part of the United States.'"

Mercator himself used the equal-area sinusoidal projection to show relative areas. However, despite such criticisms, the Mercator projection was, especially in the late 19th and early 20th centuries, perhaps the most common projection used in world maps. Atlases largely stopped using the Mercator projection for world maps or for areas distant from the equator in the 1940s, preferring other cylindrical projections, or forms of equal-area projection. The Mercator projection is, however, still commonly used for areas near the equator where distortion is minimal. It is also frequently found in maps of time zones.

Arno Peters stirred controversy beginning in 1972 when he proposed what is now usually called the Gall–Peters projection to remedy the problems of the Mercator, claiming it to be his own original work without referencing prior work by cartographers such as Gall's work from 1855. The projection he promoted is a specific parameterization of the cylindrical equal-area projection. In response, a 1989 resolution by seven North American geographical groups disparaged using cylindrical projections for general-purpose world maps, which would include both the Mercator and the Gall–Peters.

As of 2025 the African Union supports a campaign favoring the Equal Earth projection over the Mercator projection.

## Uses

Practically every marine chart in print is based on the Mercator projection due to its uniquely favorable properties for navigation. It is also commonly used by street map services hosted on the Internet, due to its uniquely favorable properties for local-area maps computed on demand. Mercator projections were also important in the mathematical development of plate tectonics in the 1960s.

### Marine navigation

The Mercator projection was designed for use in marine navigation because of its unique property of representing any course of constant bearing as a straight segment. Such a course, known as a rhumb (alternately called a rhumb line or loxodrome) is preferred in marine navigation because ships can sail in a constant compass direction. This reduces the difficult, error-prone course corrections that otherwise would be necessary when sailing a different course.

For small distances (compared to the radius of Earth), the difference between the rhumb and the great circle course is negligible. Even for longer distances, the simplicity of the constant bearing makes it attractive. As observed by Mercator, on such a course the ship would not arrive by the shortest route but it will surely arrive. Sailing a rhumb meant that all that the sailors had to do was keep a constant course as long as they knew where they were when they started, where they intended to be when they finished, and had a map in Mercator projection that correctly showed those two coordinates.

### Web Mercator

Many major online street mapping services (Bing Maps, Google Maps, Mapbox, MapQuest, OpenStreetMap, Yahoo! Maps, and others) use a variant of the Mercator projection for their map images called Web Mercator or Google Web Mercator. Despite its obvious scale variation at the world level (small scales), the projection is well-suited as an interactive world map that can be zoomed seamlessly to local (large-scale) maps, where there is relatively little distortion due to the variant projection's near-conformality.

The major online street mapping services' tiling systems display most of the world at the lowest zoom level as a single square image, excluding the polar regions by truncation at latitudes of *φ*max = ±85.05113°. (See below.) Latitude values outside this range are mapped using a different relationship that does not diverge at *φ* = ±90°.

### Transverse Mercator

A transverse Mercator projection tilts the cylinder axis so that it is perpendicular to Earth's axis. The tangent standard line then coincides with a meridian and its opposite meridian, giving a constant scale factor along those meridians, and a near-constant one within a band of a few degrees of longitude around them. This property makes such a projection useful for mapping regions that are either compact or predominately north–south in extent. In its more complex ellipsoidal form, most national grid systems around the world use the transverse Mercator, as does the Universal Transverse Mercator coordinate system.

### Oblique Mercator

An oblique Mercator projection tilts the cylinder axis away from Earth's axis to an angle of one's choosing, so that its tangent or secant lines of contact are circles that are also tilted relative to Earth's parallels of latitude. Practical uses for the oblique projection, such as national grid systems, use ellipsoidal developments of the oblique Mercator in order to keep scale variation low along the surface projection of the cylinder's axis.

The animation below shows a continuous transformation between the normal Mercator projection and the transverse projection, running through the intermediate oblique states. A rhumb line (blue) and great circle (red) from Tokyo, Japan, to Callao, Peru, change according to the projection's aspect. The rhumb between them is straight only on the normal projection. On one of the intermediate oblique projections, the great-circle path between the two cities is straight. In this plot the y-axis is always the projected axis of the cylinder. The sphere is rotated inside the cylinder to change aspect. Initially the axis is normal to the equator (projected as the thick green line) but ends transverse to it, when the projected equator extends to infinity in the vertical direction.

## Mathematics

A simple expression for the spherical form of the Mercator projection is:

$x=R(\lambda -\lambda _{0}),\qquad y=R\,{\ln }{\bigl (}{\tan }{\bigl (}{\tfrac {1}{4}}\pi +{\tfrac {1}{2}}\varphi {\bigr )}{\bigr )},$

where ⁠ R ⁠ is an arbitrary scale factor which determines the size of the resulting map, ln is the natural logarithm, and tan is the trigonometric tangent function.

### Cylindrical projections

Although the surface of Earth is better modelled by an oblate ellipsoid of revolution, for small scale maps the ellipsoid is approximated by a sphere of radius *a*, where *a* is approximately 6,371 km. This spherical approximation of Earth can be modelled by a smaller sphere of radius *R*, called the *globe* in this section. The globe determines the scale of the map. The various cylindrical projections specify how the geographic detail is transferred from the globe to a cylinder tangential to it at the equator. The cylinder is then unrolled to give the planar map. The fraction ⁠*R*/*a*⁠ is called the representative fraction (RF) or the principal scale of the projection. For example, a Mercator map printed in a book might have an equatorial width of 13.4 cm corresponding to a globe radius of 2.13 cm and an RF of approximately ⁠1/300M⁠ (M is used as an abbreviation for 1,000,000 in writing an RF) whereas Mercator's original 1569 map has a width of 198 cm corresponding to a globe radius of 31.5 cm and an RF of about ⁠1/20M⁠.

A cylindrical map projection is specified by formulae linking the geographic coordinates of latitude *φ* and longitude *λ* to Cartesian coordinates on the map with origin on the equator and *x*-axis along the equator. By construction, all points on the same meridian lie on the same *generator* of the cylinder at a constant value of *x*, but the distance *y* along the generator (measured from the equator) is an arbitrary function of latitude, *y*(*φ*). In general this function does not describe the geometrical projection (as of light rays onto a screen) from the centre of the globe to the cylinder, which is only one of an unlimited number of ways to conceptually project a cylindrical map.

Since the cylinder is tangential to the globe at the equator, the scale factor between globe and cylinder is unity on the equator but nowhere else. In particular since the radius of a parallel, or circle of latitude, is *R* cos *φ*, the corresponding parallel on the map must have been stretched by a factor of ⁠1/cos *φ*⁠ = sec *φ*. This scale factor on the parallel is conventionally denoted by *k* and the corresponding scale factor on the meridian is denoted by *h*.

### Scale factor

The Mercator projection is conformal. One implication of that is the "isotropy of scale factors", which means that the point scale factor is independent of direction, so that small shapes are preserved by the projection. This implies that the vertical scale factor, *h*, equals the horizontal scale factor, *k*. Since *k* = sec *φ*, so must *h*.

The graph shows the variation of this scale factor with latitude. Some numerical values are listed below.

at latitude 30° the scale factor is

k

= sec 30° ≈ 1.15,

at latitude 45° the scale factor is

k

= sec 45° ≈ 1.41,

at latitude 60° the scale factor is

k

= sec 60° = 2,

at latitude 80° the scale factor is

k

= sec 80° ≈ 5.76,

at latitude 85° the scale factor is

k

= sec 85° ≈ 11.5

The area scale factor is the product of the parallel and meridian scales *hk* = sec2*φ*. For Greenland, taking 73° as a median latitude, *hk* = 11.7. For Australia, taking 25° as a median latitude, *hk* = 1.2. For Great Britain, taking 55° as a median latitude, *hk* = 3.04.

The variation with latitude is sometimes indicated by multiple bar scales as shown below.

The classic way of showing the distortion inherent in a projection is to use Tissot's indicatrix. Nicolas Tissot noted that the scale factors at a point on a map projection, specified by the numbers *h* and *k*, define an ellipse at that point. For cylindrical projections, the axes of the ellipse are aligned to the meridians and parallels. For the Mercator projection, *h* = *k*, so the ellipses degenerate into circles with radius proportional to the value of the scale factor for that latitude. These circles are rendered on the projected map with extreme variation in size, indicative of Mercator's scale variations.

### Mercator projection transformations

#### Integral of the secant

As discussed above, the isotropy condition implies that ⁠ $h=k=\sec \varphi$ ⁠. Consider a point on the globe of radius ⁠ R ⁠ with longitude ⁠ $\lambda$ ⁠ and latitude ⁠ $\varphi$ ⁠, expressed in radians. If ⁠ $\varphi$ ⁠ is increased by an infinitesimal amount ⁠ $d\varphi$ ⁠, the point moves ⁠ $R\,d\varphi$ ⁠ along a meridian of the globe of radius ⁠ R ⁠, so the corresponding change in ⁠ y ⁠ is ⁠ $dy=hR\,d\varphi =R\sec \varphi \,d\varphi$ ⁠. Therefore ⁠ $y'(\varphi )=R\sec \varphi$ ⁠. Similarly, increasing ⁠ $\lambda$ ⁠ by ⁠ $d\lambda$ ⁠ moves the point ⁠ $R\cos \varphi \,d\lambda$ ⁠ along a parallel of the globe, so ⁠ $dx=kR\cos \varphi \,d\lambda =Rd\lambda$ ⁠. That is, ⁠ $x'(\lambda )=R$ ⁠. Integrating these two equations

$x'(\lambda )=R,\qquad y'(\varphi )=R\sec \varphi ,$

with ⁠ $x(\lambda _{0})=0$ ⁠ and ⁠ $y(0)=0$ ⁠ gives

$x(\lambda )=\int _{\lambda _{0}}^{\lambda }R\,du,\qquad y(\varphi )=\int _{0}^{\varphi }R\sec v\,dv.$

The value ⁠ $\lambda _{0}$ ⁠ is the longitude of an arbitrary central meridian, often the prime meridian ⁠ $\lambda _{0}=0$ ⁠. The definite integral of the secant function up to an angle ⁠ $\varphi$ ⁠ is an associated hyperbolic angle called the *anti-gudermannian* or *lambertian* of ⁠ $\varphi$ ⁠,

$x=R(\lambda -\lambda _{0}),\qquad y=R\operatorname {gd} ^{-1}(\varphi )=R\,{\ln }{\bigl (}{\tan }{\bigl (}{\tfrac {1}{4}}\pi +{\tfrac {1}{2}}\varphi {\bigr )}{\bigr )}.$

The vertical coordinate ⁠ y ⁠ was historically called the *meridional part* of ⁠ $\varphi$ ⁠. In the figure, ⁠ y ⁠ is plotted against ⁠ $\varphi$ ⁠ for the case ⁠ $R=1$ ⁠, such that it equals the anti-gudermannian of ⁠ $\varphi$ ⁠; it tends to infinity at the poles. The numerical value of ⁠ y ⁠ is not usually shown on printed maps; some maps show a non-linear scale of latitudes, but more often than not maps show only a graticule of selected meridians and parallels.

#### Complex logarithm

As a conformal map, the Mercator projection can be conveniently expressed using a single complex number to represent each point on the sphere rather than a pair of real-number coordinates. The complex number representing each point on this so-called Riemann sphere is found by conformally mapping the sphere onto the complex plane via the stereographic projection. From there, the Mercator projection is just the complex logarithm, ⁠ $z\mapsto \log z$ ⁠, a conformal map of the complex plane (with the exception of the origin, whose logarithm is undefined) onto a two-infinite-ended cylinder. Starting from geographic coordinates ⁠ $(\lambda ,\varphi )$ ⁠ in radians, the stereographic projection yields a complex number ⁠ $\textstyle z=e^{\lambda i}\tan {\bigl (}{\tfrac {1}{4}}\pi -{\tfrac {1}{2}}\varphi {\bigr )}$ ⁠, with the North Pole mapped to the origin. Thus the following function ⁠ M ⁠ is a complex-valued Mercator projection of geographical coordinates:

${\begin{aligned}M(\lambda ,\varphi )&={\log }{\bigl (}e^{\lambda i}\,{\tan }{\bigl (}{\tfrac {1}{4}}\pi -{\tfrac {1}{2}}\varphi {\bigr )}{\bigr )}\\[3mu]&={\log }{\bigl (}{\tan }{\bigl (}{\tfrac {1}{4}}\pi -{\tfrac {1}{2}}\varphi {\bigr )}{\bigr )}+\lambda i.\end{aligned}}$

The imaginary part of the resulting complex number represents the longitude and its real part represents the negative projected latitude. To better match prevailing conventions about the plotting of complex numbers and world maps it can be rotated a quarter turn and scaled arbitrarily by multiplying by a scaling factor ⁠ $-Ri$ ⁠.

#### Inverse transformations

Finding the longitude as an inverse of the ⁠ x ⁠ coordinate is trivial. The latitude can be found as an inverse of ⁠ y ⁠ as the gudermannian of ⁠ $y/R$ ⁠.

$\lambda =\lambda _{0}+{\frac {x}{R}},\qquad \varphi =\operatorname {gd} \left({\frac {y}{R}}\right)=2\tan ^{-1}\left(\exp \left({\frac {y}{R}}\right)\right)-{\frac {\pi }{2}}.$

#### Alternative expressions

There are many identities relating the circular angle ⁠ $\varphi$ ⁠ to its anti-gudermannian ⁠ $\operatorname {gd} ^{-1}\varphi =y/R$ ⁠, a hyperbolic angle, which can be used to construct alternate expressions for the functions from one to the other. (See Gudermannian function.) For a real value of ⁠ $\varphi$ ⁠, a well-behaved expression for computation is:

${\begin{aligned}y/R=\operatorname {gd} ^{-1}(\varphi )&=\sinh ^{-1}(\tan \varphi ),\\[5mu]\varphi =\operatorname {gd} (y/R)&={\tan ^{-1}}{\bigl (}{\sinh(y/R)}{\bigr )},\end{aligned}}$

where sinh is the hyperbolic sine function. An alternative expression, valid throughout the complex plane, is

${\begin{aligned}y/R=\operatorname {gd} ^{-1}\varphi &={2\tanh ^{-1}}{\bigl (}{\tan {\tfrac {1}{2}}\varphi }{\bigr )},\\[5mu]\varphi =\operatorname {gd} (y/R)&={2\tan ^{-1}}{\bigl (}{\tanh {\tfrac {1}{2}}(y/R)}{\bigr )},\end{aligned}}$

where tanh is the hyperbolic tangent function.

The above formulae are written in terms of the globe radius ⁠ R ⁠. It is often convenient to work directly with the map width ⁠ W ⁠, in terms of which, assuming the map shows the whole globe, ⁠ $R=W/2\pi$ ⁠.

#### Truncation and aspect ratio

The ordinate *y* of the Mercator projection becomes infinite at the poles and the map must be truncated at some latitude less than ninety degrees. This need not be done symmetrically. Mercator's original map is truncated at 80°N and 66°S with the result that European countries were moved toward the centre of the map. The aspect ratio of his map is ⁠198/120⁠ = 1.65. Even more extreme truncations have been used: a Finnish school atlas was truncated at approximately 76°N and 56°S, an aspect ratio of 1.97.

Much Web-based mapping uses a zoomable version of the Mercator projection with an aspect ratio of one. In this case the maximum latitude attained must correspond to *y* = ±⁠*W*/2⁠, or equivalently ⁠*y*/*R*⁠ = π. Any of the inverse transformation formulae may be used to calculate the corresponding latitudes:

$\varphi =\tan ^{-1}\left[\sinh \left({\frac {y}{R}}\right)\right]=\tan ^{-1}\left[\sinh \pi \right]=\tan ^{-1}\left[11.5487\right]=85.05113^{\circ }.$

### Small element geometry

The relations between *y*(*φ*) and properties of the projection, such as the transformation of angles and the variation in scale, follow from the geometry of corresponding *small* elements on the globe and map. The figure below shows a point P at latitude *φ* and longitude *λ* on the globe and a nearby point Q at latitude *φ* + *δφ* and longitude *λ* + *δλ*. The vertical lines PK and MQ are arcs of meridians of length *Rδφ*. The horizontal lines PM and KQ are arcs of parallels of length *R*(cos *φ*)*δλ*. The corresponding points on the projection define a rectangle of width *δx* and height *δy*.

For small elements, the angle PKQ is approximately a right angle and therefore

$\tan \alpha \approx {\frac {R\cos \varphi \,\delta \lambda }{R\,\delta \varphi }},\qquad \qquad \tan \beta ={\frac {\delta x}{\delta y}},$

The previously mentioned scaling factors from globe to cylinder are given by

parallel scale factor

$\quad k(\varphi )\;=\;{\frac {P'M'}{PM}}\;=\;{\frac {\delta x}{R\cos \varphi \,\delta \lambda }},$

meridian scale factor

$\quad h(\varphi )\;=\;{\frac {P'K'}{PK}}\;=\;{\frac {\delta y}{R\delta \varphi \,}}.$

Since the meridians are mapped to lines of constant *x*, we must have *x* = *R*(*λ* − *λ*0) and *δx* = *Rδλ*, (*λ* in radians). Therefore, in the limit of infinitesimally small elements

$\tan \beta ={\frac {R\sec \varphi }{y'(\varphi )}}\tan \alpha \,,\qquad k=\sec \varphi \,,\qquad h={\frac {y'(\varphi )}{R}}.$

In the case of the Mercator projection, *y'*(*φ*) = *R* sec *φ*, so this gives us *h* = *k* and *α* = *β*. The fact that *h* = *k* is the isotropy of scale factors discussed above. The fact that *α* = *β* reflects another implication of the mapping being conformal, namely the fact that a sailing course of constant azimuth on the globe is mapped into the same constant grid bearing on the map.

### Formulae for distance

Converting ruler distance on the Mercator map into true (great circle) distance on the sphere is straightforward along the equator, but not at other latitudes. One problem is the variation of scale with latitude. Another problem is that straight lines on the map (rhumb lines), other than the meridians or the equator, do not correspond to great circles.

The distinction between rhumb (sailing) distance and great circle (true) distance was understood by Mercator. (See Legend 12 on the 1569 map.) He asserted that the rhumb line distance is an acceptable approximation for true great circle distance for courses of short or moderate distance, particularly at lower latitudes. He quantified his statement: "When the great circle distances which are to be measured in the vicinity of the equator do not exceed 20 degrees of a great circle, or 15 degrees near Spain and France, or 8 and even 10 degrees in northern parts it is convenient to use rhumb line distances".

For a ruler measurement of a *short* line, with midpoint at latitude *φ*, where the scale factor is *k* = sec *φ* = ⁠1/cos *φ*⁠:

True distance = rhumb distance ≅ ruler distance × cos

φ

/ RF.   (short lines)

With radius and great circle circumference equal to 6,371 km and 40,030 km respectively an RF of ⁠1/300M⁠, for which *R* = 2.12 cm and *W* = 13.34 cm, implies that a ruler measurement of 3 mm. in any direction from a point on the equator corresponds to approximately 900 km. The corresponding distances for latitudes 20°, 40°, 60° and 80° are 846 km, 689 km, 450 km and 156 km respectively.

Longer distances require various approaches.

#### On the equator

Scale is unity on the equator (for a non-secant projection). Therefore, interpreting ruler measurements on the equator is:

True distance = ruler distance / RF     (equator)

For the above model, with RF = ⁠1/300M⁠, 1 cm corresponds to 3,000 km.

#### On other parallels

On any other parallel the scale factor is sec *φ* so that

Parallel distance = ruler distance × cos

φ

/ RF     (parallel).

For the above model 1 cm corresponds to 1,500 km at a latitude of 60°.

This is not the shortest distance between the chosen endpoints on the parallel because a parallel is not a great circle. The difference is small for short distances but increases as *λ*, the longitudinal separation, increases. For two points, A and B, separated by 10° of longitude on the parallel at 60° the distance along the parallel is approximately 0.5 km greater than the great circle distance. (The distance AB along the parallel is (*a* cos *φ*) *λ*. The length of the chord AB is 2(*a* cos *φ*) sin ⁠*λ*/2⁠. This chord subtends an angle at the centre equal to 2arcsin(cos *φ* sin ⁠*λ*/2⁠) and the great circle distance between A and B is 2*a* arcsin(cos *φ* sin ⁠*λ*/2⁠).) In the extreme case where the longitudinal separation is 180°, the distance along the parallel is one half of the circumference of that parallel; i.e., 10,007.5 km. On the other hand, the geodesic between these points is a great circle arc through the pole subtending an angle of 60° at the center: the length of this arc is one sixth of the great circle circumference, about 6,672 km. The difference is 3,338 km so the ruler distance measured from the map is quite misleading even after correcting for the latitude variation of the scale factor.

#### On a meridian

A meridian of the map is a great circle on the globe but the continuous scale variation means ruler measurement alone cannot yield the true distance between distant points on the meridian. However, if the map is marked with an accurate and finely spaced latitude scale from which the latitude may be read directly—as is the case for the Mercator 1569 world map (sheets 3, 9, 15) and all subsequent nautical charts—the meridian distance between two latitudes *φ*1 and *φ*2 is simply

$m_{12}=a|\varphi _{1}-\varphi _{2}|.$

If the latitudes of the end points cannot be determined with confidence then they can be found instead by calculation on the ruler distance. Calling the ruler distances of the end points on the map meridian as measured from the equator *y*1 and *y*2, the true distance between these points on the sphere is given by using any one of the inverse Mercator formulae:

$m_{12}=a\left|\tan ^{-1}\left[\sinh \left({\frac {y_{1}}{R}}\right)\right]-\tan ^{-1}\left[\sinh \left({\frac {y_{2}}{R}}\right)\right]\right|,$

where *R* may be calculated from the width *W* of the map by *R* = ⁠*W*/2π⁠. For example, on a map with *R* = 1 the values of *y* = 0, 1, 2, 3 correspond to latitudes of *φ* = 0°, 50°, 75°, 84° and therefore the successive intervals of 1 cm on the map correspond to latitude intervals on the globe of 50°, 25°, 9° and distances of 5,560 km, 2,780 km, and 1,000 km on Earth.

#### On a rhumb

A straight line on the Mercator map at angle *α* to the meridians is a rhumb line. When *α* = ⁠π/2⁠ or ⁠3π/2⁠ the rhumb corresponds to one of the parallels; only one, the equator, is a great circle. When *α* = 0 or π it corresponds to a meridian great circle (if continued around the globe). For all other values it is a spiral from pole to pole on the globe intersecting all meridians at the same angle, and is thus not a great circle. This section discusses only the last of these cases.

If *α* is neither 0 nor π then the above figure of the infinitesimal elements shows that the length of an infinitesimal rhumb line on the sphere between latitudes *φ*; and *φ* + *δφ* is *a* sec *α* *δφ*. Since *α* is constant on the rhumb this expression can be integrated to give, for finite rhumb lines on Earth:

$r_{12}=a\sec \alpha \,|\varphi _{1}-\varphi _{2}|=a\,\sec \alpha \;\Delta \varphi .$

Once again, if Δ*φ* may be read directly from an accurate latitude scale on the map, then the rhumb distance between map points with latitudes *φ*1 and *φ*2 is given by the above. If there is no such scale then the ruler distances between the end points and the equator, *y*1 and *y*2, give the result via an inverse formula:

$r_{12}=a\sec \alpha \left|\tan ^{-1}\sinh \left({\frac {y_{1}}{R}}\right)-\tan ^{-1}\sinh \left({\frac {y_{2}}{R}}\right)\right|.$

These formulae give rhumb distances on the sphere which may differ greatly from true distances whose determination requires more sophisticated calculations.

### Generalization to the ellipsoid

When Earth is modelled by a spheroid (ellipsoid of revolution) the Mercator projection must be modified if it is to remain conformal. The transformation equations and scale factor for the non-secant version are ${\begin{aligned}x&=R\left(\lambda -\lambda _{0}\right),\\y&=R\ln \left[\tan \left({\frac {\pi }{4}}+{\frac {\varphi }{2}}\right)\left({\frac {1-e\sin \varphi }{1+e\sin \varphi }}\right)^{\frac {e}{2}}\right]=R\left(\sinh ^{-1}\left(\tan \varphi \right)-e\tanh ^{-1}(e\sin \varphi )\right),\\k&=\sec \varphi {\sqrt {1-e^{2}\sin ^{2}\varphi }}.\end{aligned}}$

The scale factor *k* is unity on the equator, as it must be since the cylinder is tangential to the ellipsoid at the equator. The ellipsoidal correction of the scale factor increases with latitude but it is never greater than *e*2, a correction of less than 1%. The value of *e*2 is about 0.006 for all reference ellipsoids. This is much smaller than the scale inaccuracy, except very close to the equator. Only accurate Mercator projections of regions near the equator will necessitate the ellipsoidal corrections.

The inverse is solved iteratively, as the isometric latitude is involved.
