---
title: "Electron (software framework)"
source: https://en.wikipedia.org/wiki/Electron_(software_framework)
domain: electron-framework
license: CC-BY-SA-4.0
tags: electron framework, chromium desktop app, node desktop runtime, web technology packaging
fetched: 2026-07-02
---

# Electron (software framework)

**Electron** (formerly known as **Atom Shell**) is a free and open-source software framework developed and maintained by OpenJS Foundation. The framework is designed to create desktop applications using web technologies (mainly HTML, CSS and JavaScript, although other technologies such as front-end frameworks and WebAssembly are possible) that are rendered using a version of the Chromium browser engine and a back end using the Node.js runtime environment. It also uses various APIs to enable functionality such as native integration with Node.js services and an inter-process communication module.

Electron was originally built for Atom and is the main GUI framework behind several other open-source projects including GitHub Desktop, Light Table, WordPress Desktop, and Eclipse Theia. It is also used in Microsoft's proprietary code editor Visual Studio Code.

## Architecture

Chromium forms the basis of a managed runtime, allowing application developers to write cross-platform applications in memory-safe JavaScript or TypeScript and target Web browser technologies including HTML, CSS, and SVG for graphics.

Electron-based applications include a "main" process and several "renderer" processes. The main process runs the logic for the application (e.g., menus, shell commands, lifecycle events), and can then launch multiple renderer processes by instantiating an instance of the `BrowserWindow` class, which loads a window that appears on the screen to render HTML, CSS, etc.

Both the main and renderer processes can run with Node.js integration if the `nodeIntegration` field in the main process is set to `true`.

Most of Electron's APIs are written in C++ or Objective-C and are exposed directly to the application code through JavaScript bindings.

## History

In September 2021, Electron moved to an eight-week release cycle between major versions to match the release cycle of Chromium Extended Stable and to comply with a new requirement from the Microsoft Store that requires browser-based apps to be within two major versions of the latest release of the browser engine.

Electron frequently releases new major versions along every other Chromium release. The latest three stable versions are supported by the Electron team.

Version history

Release

Status

Release date

End of life date

Chromium version

Node.js version

Module version

N-API version

ICU version

Unsupported:

v1.8.x

End-of-Life

12 December 2017

20 December 2018

59

8.2

57

?

?

Unsupported:

v2.0.x

End-of-Life

1 May 2018

24 April 2019

61

8.9

57

?

?

Unsupported:

v3.1.x

End-of-Life

18 September 2018

29 July 2019

66

10.2

64

3

?

Unsupported:

v4.2.x

End-of-Life

20 December 2018

22 October 2019

69

10.11

69

3

62.2

Unsupported:

v5.1.x

End-of-Life

24 April 2019

4 February 2020

73

12.0

70

4

63.1

Unsupported:

v6.1.x

End-of-Life

29 July 2019

18 May 2020

76

12.4

73

4

64.2

Unsupported:

v7.3.x

End-of-Life

22 October 2019

25 August 2020

78

12.8

75

4

64.2

Unsupported:

v8.3.x

End-of-Life

4 February 2020

16 November 2020

80

12.13

76

5

65.1

Unsupported:

v9.4.x

End-of-Life

18 May 2020

2 March 2021

83

12.14

80

5

65.1

Unsupported:

v10.4.x

End-of-Life

25 August 2020

25 May 2021

85

12.16

82

5

65.1

Unsupported:

v11.4.x

End-of-Life

16 November 2020

30 August 2021

87

12.18

85

5

65.1

Unsupported:

v12.0.x

End-of-Life

2 March 2021

15 November 2021

89

14.16

87

7

68.1

Unsupported:

v13.x.y

End-of-Life

25 May 2021

31 January 2022

91

14.16

89

7

68.1

Unsupported:

v14.x.y

End-of-Life

30 August 2021

29 March 2022

92

14.17

89

8

69.1

Unsupported:

v15.x.y

End-of-Life

21 September 2021

24 May 2022

94

16.5

98

?

?

Unsupported:

v16.x.y

End-of-Life

15 November 2021

24 May 2022

96

16.9

99

?

?

Unsupported:

v17.x.y

End-of-Life

1 February 2022

2 August 2022

98

16.13

101

?

?

Unsupported:

v18.x.y

End-of-Life

29 March 2022

26 September 2022

100

16.13

103

?

?

Unsupported:

v19.x.y

End-of-Life

24 May 2022

29 November 2022

102

16.14

106

?

?

Unsupported:

v20.x.y

End-of-Life

2 August 2022

7 February 2023

104

16.15

?

?

?

Unsupported:

v21.x.y

End-of-Life

26 September 2022

4 April 2023

106

16.16

?

?

?

Unsupported:

v22.x.y

End-of-Life

30 November 2022

10 October 2023

108

16.17

?

?

?

Unsupported:

v23.x.y

End-of-Life

30 November 2022

15 August 2023

110

18.12

?

?

?

Unsupported:

v24.x.y

End-of-Life

4 April 2023

10 October 2023

112

18.14

?

?

?

Unsupported:

v25.x.y

End-of-Life

30 May 2023

5 December 2023

114

18.15

?

?

?

Unsupported:

v26.x.y

End-of-Life

15 August 2023

20 February 2024

116

18.16

?

?

?

Unsupported:

v27.x.y

End-of-Life

10 October 2023

16 April 2024

118

18.17

?

?

?

Unsupported:

v28.x.y

End-of-Life

5 December 2023

11 June 2024

120

18.18

?

?

?

Unsupported:

v29.x.y

End-of-Life

20 February 2024

20 August 2024

122

20.9

?

?

?

Unsupported:

v30.x.y

End-of-Life

16 April 2024

15 October 2024

124

20.11

?

?

?

Unsupported:

v31.x.y

End-of-Life

11 June 2024

7 January 2025

126

20.14

?

?

?

Unsupported:

v32.x.y

End-of-Life

20 August 2024

4 March 2025

128

20.16

?

?

?

Unsupported:

v33.x.y

End-of-Life

15 October 2024

29 April 2025

130

20.18

?

?

?

Unsupported:

v34.x.y

End-of-Life

14 January 2025

24 June 2025

132

20.18

?

?

?

Unsupported:

v35.x.y

End-of-Life

4 March 2025

2 September 2025

134

22.14

?

?

?

Unsupported:

v36.x.y

End-of-Life

29 April 2025

28 October 2025

136

22.14

?

?

?

Unsupported:

v37.x.y

End-of-Life

24 June 2025

13 January 2026

138.0.7204.251

22.21.1

?

?

?

Unsupported:

v38.x.y

End-of-Life

2 September 2025

10 March 2026

140.0.7339.249

22.21.1

?

?

?

Unsupported:

v39.x.y

End-of-Life

28 October 2025

5 May 2026

142.0.7444.235

22.21.1

?

?

?

Unsupported:

v40.x.y

End-of-Life

13 January 2026

30 June 2026

144.0.7547.0

24.11.1

?

?

?

Supported:

v41.x.y

Active

10 March 2026

25 August 2026

146.0.7650.0

24.14.0

?

?

?

Supported:

v42.x.y

Active

5 May 2026

20 October 2026

148.0.7778.96

24.15.0

?

?

?

Latest version:

v43.x.y

Current

30 June 2026

5 January 2027

150.0.7871.46

24.17.0

?

?

?

Preview version:

v44.x.y

Nightly

25 August 2026

2 March 2027

149.0.7827.0

24.15.0

?

?

?

## Usage

Desktop applications built with Electron include Atom, balenaEtcher, Discord, Slack, and Visual Studio Code. The Brave browser was based on Electron before it was rewritten to use Chromium directly, while Microsoft Teams used Electron before 2.0.

## Reception

The most common criticism of Electron is that it necessitates software bloat when used for simple programs. As a result, Michael Larabel has referred to the framework as "notorious among most Linux desktop users for being resource heavy, not integrating well with most desktops, and generally being despised". Researchers have shown that Electron's large feature set can be hijacked by bad actors with write access to the source JavaScript files. This requires root access on Unix-like systems and is not considered to be a vulnerability by the Electron developers. Those who are concerned that Electron is not always based on the newest version of Chromium have recommended progressive web applications as an alternative.
