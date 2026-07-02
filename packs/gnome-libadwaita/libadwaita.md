---
title: "Adwaita (design language)"
source: https://en.wikipedia.org/wiki/Libadwaita
domain: gnome-libadwaita
license: CC-BY-SA-4.0
tags: libadwaita library, gnome human interface, adwaita styling, adaptive gnome widgets
fetched: 2026-07-02
---

# Adwaita (design language)

(Redirected from

Libadwaita

)

**Adwaita** is the design language of the GNOME desktop environment GUI interface. As an implementation, it exists as the default theme and icon set of the GNOME Shell and Phosh, and as widgets for applications targeting usage in GNOME. Adwaita first appeared in 2011 with the release of GNOME 3.0 as a replacement for the design principles used in Clearlooks, and with incremental modernization and refinements, continues with current version releases.

Until 2021, Adwaita's theme was included as a part of the GTK widget toolkit, but in an effort to further increase independence and divergent release schedules of GTK from that of GNOME, it has since been migrated to libadwaita, which as an overall project, serves to extend GTK's base widgets with those specifically conforming to the GNOME human interface guidelines.

## Development

Prior to version 3.0, the GNOME desktop environment utilized the Clearlooks theme. In October 2008, designers and developers met at the GNOME User Experience Hackfest in Boston. During this event, the concept of a GNOME Shell was conceived. Some very early mockups were produced that entertained the possibility of differing design from the previous incarnation of GNOME. Red Hat designers Jon McCann and Jeremy Perry authored a document, drawn from a broad consensus of collaborative effort, that aimed to set standards and direction for GNOME's design. In February 2010, GNOME designers met again, and produced several more publicly-available mockups.

Also produced from the 2010 meeting was the decision to use Cantarell as the default typeface. Cantarell had been designed by Dave Crossland during his studies in the Department of Typography and Graphic Communication at the University of Reading the previous year. It was officially added to GNOME Shell in February 2011, and the GNOME Project agreed to maintain and extend the font as needed.

On January 19, 2011, Carlos Garnacho announced his completion of a tangible GTK theme implementation of Adwaita that could then be utilized by GNOME.

The first major Linux distribution to ship with GNOME 3.0 and Adwaita as a default was Fedora Linux when it released version 15 on May 24, 2011.

Due to GTK's strong ties with GNOME, Adwaita's theme had replaced "Raleigh" as the default GTK theme in 2014; however, in preparation for the release of libadwaita, the theme was removed from GTK in favor of a divergent, simpler one on January 14, 2021. This clear demarcation allowed for both GNOME, with its own design needs, and GTK, with its need for a simple theme that could be extended by downstream projects, to simultaneously prosper. Libadwaita first shipped with the release of GNOME 42.

With the release of the GNOME 48 Alpha release in January 24th, 2025, it was announced that Cantarell would be replaced as the default font by the brand new font Adwaita Sans, based on the popular font Inter; as well as the default monospaced font switching from Source Code Pro to Adwaita Mono, based on Iosevka.

## Design language

Adwaita is characterized by its clean, modern aesthetic and focus on usability. Through the GNOME Human Interface Guidelines, Adwaita's design principles are rooted in simplicity, consistency, and accessibility.

## Libadwaita

The libadwaita library was created to further develop Adwaita as a more closely-adherent component of the GNOME Human Interface Guidelines. Libadwaita is a library augmenting the GTK widget toolkit in a manner conformant with the GNOME Human Interface Guidelines. It lets applications change their layout based on the available screen space, integrates the Adwaita stylesheet, allows runtime recoloring with named colors and adds APIs to support the cross-desktop dark style preference.

### Responsive design and Linux smartphones

Libadwaita offers tools for creating applications with responsive design, allowing applications to adapt their layouts based on the available screen space, which aids in the development of smartphone-compatible GNOME applications.

### Libhandy

Libhandy is a library sponsored by Purism, which was the predecessor of Libadwaita. The libhandy project was used as the basis for libadwaita.

## GNOME Human Interface Guidelines

The GNOME Human Interface Guidelines (HIG) serve as a comprehensive guide to designing applications for the GNOME desktop environment. It helps with creation of user interfaces that align with GNOME's design philosophy, and is the basis for Adwaita's own style and design standards.

## Elements

### Color

Adwaita's color palette is used in design of application icons and in illustrations. It consists of several color shade families that are not named beyond their number designations. Those lacking saturation are known as "light" and "dark". This naming convention extends into the applied concept of user interface styles, where users can choose a base style for on-screen widget components that creates a light or dark overall look and feel.

Colors

Name

Hex

(RGB)

Red

(RGB)

Green

(RGB)

Blue

(RGB)

Hue

(HSL/HSV)

Satur.

(HSL)

Light

(HSL)

Satur.

(HSV)

Value

(HSV)

Blue 1

#99C1F1

60%

76%

95%

213

°

76%

77%

37%

95%

Blue 2

#62A0EA

38%

63%

92%

213

°

76%

65%

58%

92%

Blue 3

#3584E4

21%

52%

89%

213

°

76%

55%

77%

89%

Blue 4

#1C71D8

11%

44%

85%

213

°

77%

48%

87%

85%

Blue 5

#1A5FB4

10%

37%

71%

213

°

75%

40%

86%

71%

Green 1

#8FF0A4

56%

94%

64%

133

°

76%

75%

40%

94%

Green 2

#57E389

34%

89%

54%

141

°

71%

62%

62%

89%

Green 3

#33D17A

20%

82%

48%

147

°

63%

51%

76%

82%

Green 4

#2EC27E

18%

76%

49%

152

°

62%

47%

76%

76%

Green 5

#26A269

15%

64%

41%

152

°

62%

39%

77%

64%

Yellow 1

#F9F06B

98%

94%

42%

56

°

92%

70%

57%

98%

Yellow 2

#F8E45C

97%

89%

36%

52

°

92%

67%

63%

97%

Yellow 3

#F6D32D

96%

83%

18%

50

°

92%

57%

82%

97%

Yellow 4

#F5C211

96%

76%

7%

47

°

92%

51%

93%

96%

Yellow 5

#E5A50A

90%

65%

4%

43

°

92%

47%

96%

90%

Orange 1

#FFBE6F

100%

75%

44%

33

°

100%

72%

57%

100%

Orange 2

#FFA348

100%

64%

28%

30

°

100%

64%

72%

100%

Orange 3

#FF7800

100%

47%

0%

28

°

100%

50%

100%

100%

Orange 4

#E66100

90%

38%

0%

25

°

100%

45%

100%

90%

Orange 5

#C64600

78%

27%

0%

21

°

100%

39%

100%

78%

Red 1

#F66151

96%

38%

32%

6

°

90%

64%

67%

97%

Red 2

#ED333B

93%

20%

23%

357

°

84%

57%

79%

93%

Red 3

#E01B24

88%

11%

14%

357

°

79%

49%

88%

88%

Red 4

#C01C28

75%

11%

16%

356

°

75%

43%

85%

75%

Red 5

#A51D2D

65%

11%

18%

353

°

70%

38%

82%

65%

Purple 1

#DC8ADD

86%

54%

87%

299

°

55%

70%

38%

87%

Purple 2

#C061CB

75%

38%

80%

294

°

51%

59%

52%

80%

Purple 3

#9141AC

57%

25%

67%

285

°

45%

47%

62%

68%

Purple 4

#813D9C

51%

24%

61%

283

°

44%

43%

61%

61%

Purple 5

#613583

38%

21%

51%

274

°

42%

36%

60%

51%

Brown 1

#CDAB8F

80%

67%

56%

27

°

38%

68%

30%

80%

Brown 2

#B5835A

71%

51%

35%

27

°

38%

53%

50%

71%

Brown 3

#986A44

60%

42%

27%

27

°

38%

43%

55%

60%

Brown 4

#865E3C

53%

37%

24%

28

°

38%

38%

55%

53%

Brown 5

#63452C

39%

27%

17%

27

°

39%

28%

56%

39%

Light 1

#FFFFFF

100%

100%

100%

0

°

0%

100%

0%

100%

Light 2

#F6F5F4

96%

96%

96%

30

°

10%

96%

1%

97%

Light 3

#DEDDDA

87%

87%

85%

45

°

6%

86%

2%

87%

Light 4

#C0BFBC

75%

75%

74%

45

°

3%

75%

2%

75%

Light 5

#9A9996

60%

60%

59%

45

°

2%

60%

3%

60%

Dark 1

#77767B

47%

46%

48%

252

°

2%

47%

4%

48%

Dark 2

#5E5C64

37%

36%

39%

255

°

4%

38%

8%

39%

Dark 3

#3D3846

24%

22%

27%

261

°

11%

25%

20%

28%

Dark 4

#241F31

14%

12%

19%

257

°

23%

16%

37%

19%

Dark 5

#000000

0%

0%

0%

0

°

0%

0%

0%

0%

### Typography

Beginning with GNOME 48, Adwaita adopted a new typeface family known as "Adwaita Fonts". The Adwaita Fonts family is a slight modification of the Inter typeface family, however it also includes a monospaced font known as "Adwaita Mono", which is a modified version of Iosevka. With this change, the default typeface for GNOME will be known as "Adwaita Sans".

Previously, Adwaita used the contemporary humanist sans-serif Cantarell typeface that was designed by Dave Crossland. Corresponding with the 3.28 version release of GNOME in 2018, Cantarell was expanded to include light and extra bold weights.

### Iconography

Adwaita defines two separate style classes of icons that are meant to differentiate between concepts used for applications and user interfaces. Whereas applications use full-color in their primary icons, "symbolic" icons, monochromatic by design, are meant for user interfaces.

#### App icons

Each app targeted for GNOME should have a primary icon. The GNOME Human Interface Guidelines prescribe that an app's icon should correspond to a simple, recognizable metaphor. They are not meant to be flat, but rather simplistic, and can contain some depth. However, shadows are to be avoided. App developers can request an icon from the GNOME Design Team in a GitLab repository.

#### Symbolic icons

In user interfaces, even simpler, monochromatic icons that work well when viewed at small sizes are used. If color is needed, it is expected that they should be programmatically re-colored.

## Implementations

The GNOME Shell was the primary vehicle for the original development of Adwaita's theme and icons. It remains a major implementation. Similarly, Phosh, Purism's mobile shell, serves in the same role.
