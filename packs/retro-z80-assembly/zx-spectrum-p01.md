---
title: "ZX Spectrum (part 1/2)"
source: https://en.wikipedia.org/wiki/ZX_Spectrum
domain: retro-z80-assembly
license: CC-BY-SA-4.0
tags: z80 assembly, zilog z80, z80 opcode, intel 8080
fetched: 2026-07-02
part: 1/2
---

# ZX Spectrum

The **ZX Spectrum** (UK: /zɛd ɛks/) is an 8-bit home computer developed and marketed by Sinclair Research. The Spectrum played a pivotal role in the history of personal computers and video games, especially in the United Kingdom. It was one of the all-time bestselling British computers with over five million units sold. It was first released in Britain on 23 April 1982 with releases in some other regions, including West Germany and the United States, after that year.

The machine was designed by the English entrepreneur and inventor Sir Clive Sinclair and his small team in Cambridge, and was manufactured in Dundee, Scotland by Timex Corporation. It was made to be small, simple, and most importantly inexpensive, with as few components as possible. The addendum "Spectrum" was chosen to highlight the machine's colour display, which differed from the black-and-white display of its predecessor, the ZX81. Rick Dickinson designed its distinctive case, rainbow motif, and rubber keyboard. Video output is transmitted to a television set rather than a dedicated monitor, while application software is loaded and saved onto compact audio cassettes.

The ZX Spectrum was initially distributed by mail order, but after severe backlogs it was sold through High Street chains in the United Kingdom. It was released in the US as the Timex Sinclair 2068 in 1983, and in some parts of Europe as the Timex Computer 2048. There are seven models overall, ranging from the entry level with 16 KB RAM released in 1982 to the ZX Spectrum +3 with 128 KB RAM and built-in floppy disk drive in 1987. The machine primarily competed with the Commodore 64, BBC Micro, Dragon 32, and the Amstrad CPC range. Over 24,000 software products were released for the ZX Spectrum.

Its introduction led to a boom in companies producing software and hardware, the effects of which are still seen. It was among the first home computers aimed at a mainstream UK audience, with some crediting it for launching the British information technology industry. The Spectrum was Britain's top-selling computer until the Amstrad PCW surpassed it in the 1990s. It was discontinued in 1992.


## History

The ZX Spectrum was conceived and designed by engineers at Sinclair Research, founded by English entrepreneur and inventor Clive Sinclair, who was well known for his eccentricity and pioneering ethic. On 25 July 1961, three years after passing his A-levels, he founded Sinclair Radionics to advertise his inventions and buy components. In 1972, Sinclair competed with Texas Instruments to produce the world's first pocket calculator, the Sinclair Executive. By the mid 1970s, Sinclair Radionics was producing handheld electronic calculators, miniature televisions, and the ill-fated digital Black Watch wristwatch. Due to financial losses, Sinclair sought investors from the National Enterprise Board (NEB), who had bought a 43% interest in the company and streamlined his product line. Sinclair's relationship with the NEB had worsened, and by 1979 it opted to break up Sinclair Radionics entirely, selling off its television division to Binatone and its calculator division to ESL Bristol.

After incurring a £7 million investment loss, Sinclair was given a golden handshake and an estimated £10,000 severance package. He had a former employee, Christopher Curry, establish a "corporate lifeboat" company named Science of Cambridge Ltd, in July 1977, called such as they were located near the University of Cambridge. By this time inexpensive microprocessors had started appearing on the market, which prompted Sinclair to start producing the MK14, a computer teaching kit which sold well at a very low price. Encouraged by this success, Sinclair renamed his company to Sinclair Research, and started looking to manufacture personal computers. Keeping the cost low was essential for Sinclair to avoid his products from becoming outpriced by American or Japanese equivalents as had happened to several of the previous Sinclair Radionics products. On 29 January 1980, the ZX80 home computer was launched to immediate popularity; notable for being one of the first computers available in the United Kingdom for less than £100. The company conducted no market research whatsoever prior to the launch of the ZX80; according to Sinclair, he "simply had a hunch" that the public was sufficiently interested to make such a project feasible and went ahead with ordering 100,000 sets of parts so that he could launch at high volume.

On 5 March 1981, the ZX81 was launched worldwide to immense success with more than 1.5 million units sold, 60% of which was outside Britain. According to Ben Rosen, by pricing the ZX81 so low, the company had "opened up a completely new market among people who had never previously considered owning a computer". After its release, computing in Britain became an activity for the general public rather than the preserve of office workers and hobbyists. The ZX81's commercial success made Sinclair Research one of Britain's leading computer manufacturers, with Sinclair himself reportedly "amused and gratified" by the attention the machine received.

### Development

Development of the ZX Spectrum began in September 1981, a few months after the release of the ZX81. Sinclair resolved to make his own products obsolete before his rivals developed the products that would do so. Parts of designs from the ZX80 and ZX81 were reused to ensure a speedy and cost-effective manufacturing process. The team consisted of 20 engineers housed in a small office at 6 King's Parade, Cambridge. During early production, the machine was known as the ZX81 Colour or the ZX82 to highlight the machine's colour display, which differed from the black and white of its predecessors. The addendum "Spectrum" was added later on, to emphasise its 15-colour palette. Aside from a new crystal oscillator and extra chips to add additional kilobytes of memory, the ZX Spectrum was intended to be, as quoted by Sinclair's marketing manager, essentially a "ZX81 with colour". According to Sinclair, the team also wanted to combine the ZX81's separate random-access memory sections for audio and video into a single bank.

Chief engineer Richard Altwasser was responsible for the ZX Spectrum's hardware design. His main contribution was the design of the semi-custom uncommitted logic array (ULA) integrated circuit, which integrated, on a single chip, the essential hardware functions. Altwasser designed a graphics mode that required less than 7 kilobytes of memory and implemented it on the ULA. Vickers wrote most of the ROM code. Lengthy discussions between Altwasser and Sinclair engineers resulted in a broad agreement that the ZX Spectrum must have high-resolution graphics, 16 kilobytes of memory, an improved cassette interface, and an impressive colour palette. To achieve this, the team had to divorce the central processing unit (CPU) away from the main display to enable it to work at full efficiency – a method which contrasted with the ZX81's integrated CPU. The inclusion of colour proved a major obstacle to the engineers. A Teletext-like approach was briefly considered, in which each line of text would have colour-change codes inserted into it. This was deemed unsuitable for high-resolution graphs or diagrams that involved multiple colour changes. Altwasser devised the idea of allocating a colour attribute to each character position on the screen. This ultimately used eight bits of memory for each character position; three bits to provide any one of eight foreground colours and three bits for the eight background colours, one bit for extra brightness and one bit for flashing. Overall, the system took up slightly less than 7 kilobytes of memory, leaving an additional 9 kilobytes to write programs – a figure that pleased the team.

Much of the firmware was written by computer scientist Steve Vickers from Nine Tiles, who compiled all control routines to produce the Sinclair BASIC interpreter, a custom variant of the general purpose BASIC programming language. Making a custom interpreter made it possible to fit all of its functionality into a very small amount of read-only memory (ROM). The development process of the software was marked by disagreements between Nine Tiles and Sinclair Research. Sinclair placed an emphasis on expediting the release of the Spectrum, primarily by minimising alterations in the software from the ZX81, which had in turn been based on the ZX80's software. The software architecture of the ZX80, however, had been tailored for a severely constrained memory system, and in Nine Tiles' opinion was unsuitable for the enhanced processing demands of the ZX Spectrum. Sinclair favoured solving this with expansion modules on the existing framework like with the ZX81, which Nine Tiles disagreed with. Ultimately, both designs were developed, but Vickers and Nine Tiles were unable to finish their version before the launch of the Spectrum and it was not used.

The distinctive case and colourful design of the ZX Spectrum was the creation of Rick Dickinson, a young British industrial designer who had been hired by Sinclair to design the ZX81. Dickinson was tasked to design a sleeker and more "marketable" appearance to the new machine, whilst ensuring all 192 BASIC functions could fit onto 40 physical keys. Early sketches from August 1981 showed the case was to be more angular and wedge-like, in similar vein to an upgraded ZX81 model. Dickinson later settled on a flatter design with a raised rear section and rounded sides in order to depict the machine as "more advanced" as opposed to a mere upgrade. In drawing up potential logos, Dickinson proposed a series of different logotypes which all featured rainbow slashes across the keyboard.

The design of the Spectrum's rubber keyboard was simplified from several hundred components to a conventional moving keyboard down to "four to five" moving parts using a new technology. The keyboard was still undergoing changes as late as February 1982; some sketches included a roundel-on-square key design which was later featured on the later Spectrum+ model. Dickinson recalled in 2007 that "everything was cost driven" and that the minimalist, Bauhaus approach to the Spectrum gave it an elegant yet "[non] revolutionary" form. The drawing board on which Dickinson designed the ZX Spectrum is now on display in the Science Museum in London.

The need for an improved cassette interface was apparent from ZX81 users who encountered problems trying to save and load programs. To increase the data transfer speed, the team decreased the length of tones that represent binary data. Originally, the team aimed for 1000 baud, but succeeded in reaching a considerably faster 1500 baud. To increase reliability, a leading period of constant tone was introduced, allowing the cassette recorder's automatic gain control to settle down, eliminating hisses on the tape. A Schmitt trigger was added inside the ULA to reduce noise of the received signal. Unlike the ZX81, the Spectrum is able to maintain its display during data transfer, allowing programs to show a splash screen whilst loading.

As with the ZX81, the ZX Spectrum was manufactured in Dundee, Scotland, by Timex Corporation at the Dryburgh factory. Prior to the ZX81, Timex was an established manufacturer of mechanical watches, but had little experience in assembling electronics. Timex's director, Fred Olsen, determined that the company would diversify into other areas and signed a contract with Sinclair.

### Launch

The ZX Spectrum was officially revealed before journalists by Sinclair at the Churchill Hotel in Marylebone, London, on 23 April 1982. Later that week, the machine was presented in a "blaze of publicity" at the Earl's Court Computer Show in London, and the ZX Microfair in Manchester. The ZX Spectrum was launched with two models: a 16KB 'basic' version, and an enhanced 48KB variant. The former model had an undercutting price of £125, significantly lower than its main competitor the BBC Micro, whilst the latter model's price of £175 was comparable to a third of an Apple II computer. Upon release, the keyboard surprised many users due to its use of rubber keys, described as offering the feel of "dead flesh". Sinclair himself remarked that the keyboard's rubber mould was "unusual", but consumers were undeterred.

Despite very high demand, Sinclair Research was "notoriously late" in delivering the ZX Spectrum. Their practice of offering mail-order sales before units were ready ensured a constant cash flow, but meant a lacking distribution. Nigel Searle, the newly-appointed chief of Sinclair's computer division, said in June 1982 the company had no plans to stock the new machine in WHSmith, which was at the time Sinclair's only retailer. Searle explained that the mail-order system was in place due to there being no "obvious" retail outlets in the United Kingdom which could sell personal computers, and it made "better sense" financially to continue selling through mail-order. The company's conservative approach to distributing the machine was criticised, with disillusioned customers telephoning and writing letters. Demand sky-rocketed beyond Sinclair's planned 20,000 monthly unit output to a backlog of 30,000 orders by July 1982. Due to a scheduled holiday at the Timex factory that summer, the backlog had risen to 40,000 units. Sinclair issued a public apology in September that year, and promised that the backlog would be cleared by the end of that month. Supply did not return to normal until the 1982 Christmas season.

Production of the machine rapidly increased with the arrival of the less expensive Issue 2 motherboard, a redesign of the main circuit board which addressed hardware manufacturing defects that affected production of the first model. Sales of the ZX Spectrum reached 200,000 in its first nine months, rising to 300,000 for the whole of the first year. By August 1983 total sales in Britain and Europe had exceeded 500,000, with the millionth Spectrum manufactured on 9 December 1983. By this point, an average of 50,000 units were being purchased each month.

In July 1983, an enhanced version of the ZX Spectrum was launched in the United States as the Timex Sinclair 2068. Advertisements described it as having 72 kilobytes of memory and a full range of colour and sound for under $200. Despite the improvements upon its British counterpart, sales were poor and Timex Sinclair collapsed the following year.

### Success and market domination

A crucial part of the company's marketing strategy was to implement regular price-cutting at strategic intervals to maintain market share. Ian Adamson and Richard Kennedy noted that Sinclair's method was driven by securing his leading position through "panicking" the competition. While most companies at the time reduced prices of their products while their market share was dwindling, Sinclair Research discounted theirs shortly after sales had peaked, throwing the competition into "utter disarray". Sinclair Research made a profit of £14 million in 1983, compared to £8.5 million the previous year. Turnover doubled from £27.2 million to £54.5 million, which equated to roughly £1 million for each person employed directly by the company.

Clive Sinclair became a focal point during the ZX Spectrum's marketing campaign by putting a human face onto the business. Sinclair Research was portrayed in the media as a "plucky" British challenger taking on the technical and marketing might of giant American and Japanese corporations. As David O'Reilly noted in 1986, "by astute use of public relations, particularly playing up his image of a Briton taking on the world, Sinclair has become the best-known name in micros." The media latched onto Sinclair's image; his "Uncle Clive" persona is said to have been created by the gossip columnist for *Personal Computer World*. The press praised Sinclair as a visionary genius, with *The Sun* lauding him as "the most prodigious inventor since Leonardo da Vinci". Adamson and Kennedy wrote that Sinclair outgrew the role of microcomputer manufacturer and "accepted the mantle of pioneering boffin leading Britain into a technological utopia". Sinclair's contribution to the technology sector resulted in him being knighted upon the recommendation of Margaret Thatcher in the Queen's 1983 Birthday Honours List.

The United Kingdom was largely immunised from the effects of the video game crash of 1983, due to the saturation of home computers such as the ZX Spectrum. The microcomputer market continued to grow and game development was unhindered despite the turbulence in the American markets. Computer games remained the dominant sector of the British home video game market up until they were surpassed by Sega and Nintendo consoles in 1991. By the end of 1983 there were more than 450 companies in Britain selling video games on cassette, compared to 95 the year before. An estimated 10,000 to 50,000 people, mostly young men, were developing games out of their homes based on advertisements in popular magazines. The growth of video games during this period has been compared to the punk subculture, fuelled by young people making money from their games.

By the mid 1980s, Sinclair Research's share of the British home computer market had climbed to a high of 40 per cent. Sales in the 1984 Christmas season were described as "extremely good". In early 1985 the British press reported the home computer boom to have ended, leaving many companies slashing prices of their hardware to anticipate lower sales. Despite this, celebration of Sinclair's success in the computing market continued at the *Which Computer?* show in Birmingham, where the five-millionth Sinclair machine (a gold coloured QL) was issued as a prize.

### Later years and company decline

The ZX Spectrum's successor, the Sinclair QL, was officially announced on 12 January 1984, shortly before the Macintosh 128K went on sale. Contrasting with its predecessors, the QL was aimed at more serious, professional home users. Fully operational QLs were not available until the late summer, and complaints against Sinclair concerning delays were upheld by the Advertising Standards Authority (ASA) in May of that year. Particularly serious were allegations that Sinclair was cashing cheques months before machines were shipped. By autumn 1984, Sinclair was still publicly forecasting that it would be a "million seller" and that 250,000 units would be sold by the end of the year. QL production was suspended in February 1985, and the price was halved by the end of the year. It ultimately flopped, with 139,454 units being manufactured.

The ZX Spectrum+, a rebranded ZX Spectrum with identical technical specifications except for the QL-like keyboard, was introduced in October 1984 and made available in WHSmith's stores the day after its launch. Retailers stocked the device in high quantities, anticipating robust Christmas sales. It did not perform as well as projected, leading to a significant drop in Sinclair's income from orders in January, as retailers were left with surplus stock. An upgraded model, the ZX Spectrum 128, was released in Spain in September 1985, financed by the Spanish distributor Investrónica. The UK launch was postponed until January 1986 due to the substantial leftover inventory of the prior model.

While the Sinclair QL was in development, Sinclair also hoped to repeat his success with the Spectrum in the fledgling electric vehicle market, which he saw as ripe for a new approach. On 10 January 1985, Sinclair unveiled the Sinclair C5, a small one-person battery electric recumbent tricycle. It marked the culmination of Sir Clive's long-running interest in electric vehicles. The C5 turned out to be a significant commercial failure, selling only 17,000 units and losing Sinclair £7 million. It has since been described as "one of the great marketing bombs of postwar British industry". The ASA ordered Sinclair to withdraw advertisements for the C5 after finding that the company's claims about its safety could not be justified.

The combined failures of the C5 and QL caused investors to lose confidence in Sinclair's judgement. In May 1985, Sinclair Research announced their intention to raise an additional £10 to £15 million to restructure the organisation, but securing the funds proved challenging. In June 1985, business magnate Robert Maxwell disclosed a takeover bid for Sinclair Research through Hollis Brothers, a subsidiary of his Pergamon Press. However, the deal was terminated in August 1985. On 7 April 1986 the company sold their entire computer product range, along with the "Sinclair" brand name, to Alan Sugar's Amstrad for £5 million. The takeover sent ripples through the London Stock Exchange, but Amstrad's shares soon recovered, with one stock broker affirming that "the City appears to have taken the news in its stride". Amstrad's acquisition saw the release of three improved ZX Spectrum models throughout the late 1980s.

By 1990, Sinclair Research consisted of Sinclair and two other employees down from 130 employees at its peak in 1985. The ZX Spectrum was officially discontinued in 1992, after ten years on the market.


## Hardware

The central processing unit is a Zilog Z80, an 8-bit microprocessor, with a clock rate of 3.5 MHz. The original model Spectrum has 16 KB of ROM and either 16 KB or 48 KB of RAM.

### Graphics

Video output is channelled through an RF modulator, intended for use with contemporary television sets. Text is displayed using a grid of 32 columns × 24 rows of characters from the ZX Spectrum character set, or from a custom set. There is a colour palette of 15 colours: seven saturated colours at two levels of brightness and black. The image resolution is 256 × 192 pixels, subject to the same colour limitations. Colour is stored separately from the pixel bitmap in a 32 × 24 grid corresponding to the character cells. This means that all pixels within an 8 × 8 character block share one foreground colour and one background colour. Altwasser received a patent for this design.

An "attribute" consists of a foreground and a background colour, a brightness level (normal or bright) and a flashing "flag" which causes the two colours to swap at regular intervals. This scheme leads to what is dubbed attribute clash, where a desired colour of a specific pixel cannot be selected, but only the colour attributes of an 8 × 8 block. This became a distinctive feature of the Spectrum, requiring games and other programs to be designed with this limitation in mind. Other machines, such as the Amstrad CPC and Commodore 64, do not suffer from this limitation. While the C64 also uses colour attributes, it has a special multicolour mode and hardware sprites which do not involve attribute clash.

### Sound

Sound is produced through a single-channel beeper capable of generating ten octaves. Sounds are generated by toggling a single bit on and off. From BASIC, the BEEP command plays sounds of specified pitch and duration. The processor is occupied exclusively with BEEP until the sound completes, limiting concurrent operations. Despite these constraints, it was a significant step forward from the silence of the ZX81. Programmers devised workarounds and explored unconventional methods such as programming the beeper to emit multiple pitches.

Later software allows for two-channel sound playback. The machine includes an expansion bus edge connector and 3.5 mm audio in/out ports, for connecting a cassette recorder to load and save programs and data. The EAR port has a higher output than the MIC and is recommended for headphones, while the MIC port is intended for attachment to other audio devices as a line-in source.

### Firmware

The machine's Sinclair BASIC interpreter is stored in 16 KiB ROM, along with essential system routines. The ROM code, responsible for tasks such as floating point calculations and expression parsing, exhibited significant similarities to ZX81, although a few outdated routines remained in the Spectrum ROM. The Spectrum's keyboard is imprinted with BASIC keywords. To input a command in BASIC, many keywords require a single keyboard stroke. Other keywords require a change of keyboard mode by a few keystrokes.

The BASIC interpreter is derived from the one used on the ZX81. A BASIC program for ZX81 can be entered into a ZX Spectrum with minimal modifications. However, Spectrum BASIC introduced numerous additional features, enhancing its usability. The ZX Spectrum character set was expanded compared to that of the ZX81, which lacked lowercase letters. Spectrum BASIC incorporated extra keywords for better graphics and sound functionality, and support for multi-statement lines was added. The built-in ROM tape modulation software routines for cassette data storage enable data transfers at an average speed of 171 bytes per second, with a theoretical peak speed of 256 bytes/s. The tape modulation is significantly more advanced than the ZX81, with approximately four times faster average speeds.


## Sinclair Research models

### ZX Spectrum

The original ZX Spectrum is remembered for its rubber chiclet keyboard, diminutive size and distinctive rainbow motif. It was originally released on 23 April 1982 with 16 KB of RAM for £125 (equivalent to £446 in 2025) or with 48 KB for £175 (equivalent to £624 in 2025); these prices were reduced to £99 (equivalent to £337 in 2025) and £129 (equivalent to £439 in 2025) respectively in 1983. Owners of the 16 KB model could purchase an internal 32 KB RAM upgrade, which for early "Issue 1" machines consisted of a daughterboard. Later issue machines required the fitting of 8 dynamic RAM chips and a few TTL chips. Users could mail their 16K Spectrums to Sinclair to be upgraded to 48 KB versions. Later revisions contained 64 KB of memory but were configured such that only 48 KB were usable. External 32 KB RAM packs that mounted in the rear expansion slot were available from third parties. Both machines had 16 KB of onboard ROM.

An "Issue 1" ZX Spectrum can be distinguished from Issue 2 or 3 models by the colour of the keys – light grey for Issue 1, blue-grey for later machines. Although the official service manual states that approximately 26,000 of these original boards were manufactured, subsequent serial number analysis shows that only 16,000 were produced, almost all of which fell in the serial number range 001-000001 to 001-016000. An online tool now exists to allow users to ascertain the likely issue number of their ZX Spectrum by inputting the serial number.

These models experienced numerous changes to its motherboard design throughout its life; mainly to improve manufacturing efficiencies, but also to correct bugs from previous boards. Another issue was with the Spectrum's power supply. In March 1983, Sinclair issued an urgent product recall warning for all owners of models bought after 1 January 1983. Plugs with a non-textured surface were at risk of causing shock, and were asked to be sent back to a warehouse in Cambridgeshire which would supply a replacement within 48 hours.

### ZX Spectrum+

Development of the *ZX Spectrum+* began in June 1984, and was released on 15 October that year at £179. It was assembled by AB Electronics in South Wales and Samsung in South Korea. This 48 KB Spectrum introduced a new QL-style case with an injection-moulded keyboard and a reset button that functions as a switch shorting across the CPU reset capacitor. Electronically, it was identical to the previous 48 KB model, and motherboards could be removed from original Spectrums and placed in the Spectrum+ case. These cases were sold to the public as a DIY upgrade. Some retailers reported a failure rate of up to 30%, compared with a more typical 5–6% for the older model. In early 1985, the original Spectrum was officially discontinued, and the ZX Spectrum+ was reduced in price to £129.

### ZX Spectrum 128

In 1985, Sinclair developed the ZX Spectrum 128 (codenamed *Derby*) in conjunction with their Spanish distributor Investrónica (a subsidiary of El Corte Inglés department store group). Investrónica had helped adapt the ZX Spectrum+ to the Spanish market after their government introduced a special tax on all computers with 64 KB RAM or less, and a law which obliged all computers sold in Spain to support the Spanish alphabet and show messages in Spanish.

The appearance of the ZX Spectrum 128 is similar to the ZX Spectrum+, with the addition of a large external heatsink for the internal 7805 voltage regulator to the right-hand end of the case, replacing the internal heatsink in previous versions. This external heatsink led to the system's nickname, "The Toast Rack". New features included 128 KB RAM with RAM disc commands, three-channel audio via the AY-3-8912 chip, MIDI compatibility, an RS-232 serial port, an RGB monitor port, 32 KB of ROM including an improved BASIC editor, and an external keypad.

The machine was simultaneously unveiled for the first time and launched in September 1985 at the SIMO '85 trade show in Spain, with a price of 44,250 pesetas. Sinclair later presented the ZX Spectrum 128 at The May Fair Hotel's Crystal Rooms in London, where he acknowledged that entertainment was the most common use of home computers. Due to the large number of unsold Spectrum+ models, Sinclair decided not to start it selling in the United Kingdom until January 1986 at a price of £179.

The Zilog Z80 processor used in the Spectrum has a 16-bit address bus, which means only 64 KB of memory can be directly addressed. To facilitate the extra 80 KB of RAM the designers used bank switching so the new memory would be available as eight pages of 16 KB at the top of the address space. The same technique was used to page between the new 16 KB editor ROM and the original 16 KB BASIC ROM at the bottom of the address space.

The new sound chip and MIDI out abilities were exposed to the BASIC programming language with the command `PLAY` and a new command `SPECTRUM` was added to switch the machine into 48K mode, keeping the current BASIC program intact (although there is no command to switch back to 128K mode). To enable BASIC programmers to access the additional memory, a RAM disk was created where files could be stored in the additional 80 KB of RAM. The new commands took the place of two existing user-defined-character spaces causing compatibility problems with certain BASIC programs. Unlike its predecessors, it has no internal speaker, and can only produce sound from a television speaker.


## Amstrad models

### ZX Spectrum +2

The ZX Spectrum +2 marked Amstrad's entry into the Spectrum market shortly after their acquisition of the Spectrum range and "Sinclair" brand in 1986. It has a grey case with a spring-loaded keyboard, dual joystick ports, and an integrated cassette recorder known as the "Datacorder" (akin to the Amstrad CPC 464). The boot-up message reads "© 1986 Amstrad". It is largely identical to the ZX Spectrum 128 in most technical aspects. The machine retailed for £149.

The new keyboard does not have the BASIC keyword markings of earlier Spectrums, except for `LOAD`, `CODE`, and `RUN` markings. Instead, the +2 has a menu system, almost identical to that of the ZX Spectrum 128, allowing users to switch between 48K BASIC programming with keywords and 128K BASIC programming, where all words, both keywords and others, need to be typed out in full. Despite these changes, the layout remained identical to that of the 128.

### ZX Spectrum +3

The ZX Spectrum +3, launched in 1987, replaces the cassette drive with a built-in 3-inch floppy disk. Initially £249, it later retailed for £199. It is the only Spectrum model capable of running the CP/M operating system without additional hardware. Unlike its predecessors, the ZX Spectrum +3 power supply uses a DIN connector.

Significant alterations caused a series of incompatibilities. The removal of several lines on the expansion bus edge connector caused complications for some peripherals. Additionally, changes in memory timing led to certain RAM banks being contended, causing failures in high-speed colour-changing effects. The keypad scanning routines from the ROM were also eliminated, so some older 48K and 128K games no longer worked. The ZX Interface 1 was also incompatible because of disparities in ROM and expansion connectors, making it impossible to connect and use the Microdrive units.

Production of the +3 was discontinued in December 1990, reportedly in response to Amstrad's relaunch of their CPC range, with an estimated 15% of ZX Spectrums sold being +3 models at the time. The +2B model, the only other model still in production at this point, continued to be manufactured, as it was believed not to be in direct competition with other computers in Amstrad's product range.

### ZX Spectrum +2A, +2B and +3B

The ZX Spectrum +2A was a new version of the Spectrum +2 using the same circuit board as the Spectrum +3. It was sold from late 1988 and unlike the original grey +2 is housed in a black case. The six datacorder buttons are blank on the black +2A/B with the function graphics (play, pause, eject etc.) being printed above them on the case, whereas the graphics are directly on the datacorder buttons of the grey +2. The Spectrum +2A/+3 motherboard (AMSTRAD part number Z70830) was designed so that it could be assembled with a +2 style "datacorder" connected instead of the floppy disk controller. The power supply of the ZX Spectrum +2A uses the same pinout as the +3.

The ZX Spectrum +2B and ZX Spectrum +3B were released in 1989. They are functionally similar in design to the Spectrum +2A and +3, though changes to the generation of the audio output signal were made to resolve problems with clipping. The +2B board has no provision for floppy disk controller circuitry, while the +3B motherboard has no provision for connecting an internal tape drive. Production of all Amstrad Spectrum models ended in 1992.


## Licences and clones

### Official licences

Sinclair Research granted a licence for the ZX Spectrum design to the Timex Corporation in the United States. Timex marketed several computer models under the Timex Sinclair brand. They introduced an enhanced variant of the original Spectrum in the US, known as the Timex Sinclair 2068. This upgraded model features improvements in sound, graphics, and various other aspects. However, Timex's versions were generally not compatible with Sinclair systems.

Timex of Portugal developed and produced several branded computers, including a PAL region-compatible version of the Timex Sinclair 2068, known as the Timex Computer 2048. This variant features distinct buffers for both the ULA and the CPU, significantly enhancing compatibility with ZX Spectrum software compared to the American model. Software developed for the Portuguese-made 2048 remained fully compatible with its American counterpart, as the ROMs were left unaltered. Timex of Portugal also created a ZX Spectrum "emulator" in cartridge form. Several other upgrades were introduced, including a BASIC64 cartridge enabling it to utilise high-resolution (512x192) modes. This model saw significant success in both Portugal and Poland.

In India, Deci Bells Electronics Limited based in Pune, introduced a licensed version of the Spectrum+ in 1988. Dubbed the "dB Spectrum+", it performed well in the Indian market, selling over 50,000 units and achieving an 80% market share.

### Unofficial clones

Numerous unofficial Spectrum clones were produced, especially in Eastern Europe. Many small start-ups in the Soviet Union assembled various clones, distributed through poster adverts and street stalls. Over 50 such clone models existed in total. In Czechoslovakia, the first production ZX Spectrum clone was the Didaktik Gama, sporting two switched 32 KB memory banks and 16 KB of slower RAM containing graphical data for video output, followed by Didaktik M, with later availability of a 5.25"/3.5" floppy disk drives; and a Didaktik Kompakt clone with a built-in floppy drive. There were also clones produced in South America, such as the Brazilian-made TK90X and TK95, as well as the Argentine Czerweny CZ models.

In the United Kingdom, Spectrum peripheral vendor Miles Gordon Technology (MGT) released the SAM Coupé 8-bit home computer in December 1989. It was designed to be fully compatible with the ZX Spectrum 48K, housing a Zilog Z80B processor clocked at 6 MHz and 256KB of RAM. By this point, the Amiga and Atari ST had taken hold of the market, leaving MGT in eventual receivership in June 1990. In his book *Retro Tech*, Peter Leigh considers the Sam Coupé to be the "true" successor of the ZX Spectrum. In 2024, Retro Games released their unnofficial clone of the ZX Spectrum titled "The Spectrum" — named generically so because the ZX trademark is unlicensed from Sinclair — which would include 48 built-in games, a save game option, rewind mode and pre-owned titles load up.


## Peripherals

Official peripherals:

ZX Printer

,

ZX Interface 2

,

ZX Interface 1

, and

ZX Microdrive

Several peripherals were developed and marketed by Sinclair. The ZX Printer, a small spark printer, was already on the market upon the ZX Spectrum's release, as its computer bus was partially backward-compatible with that of its predecessor, the ZX81. It uses two electrically charged styli to burn away the surface of aluminium-coated paper to reveal the black underlay.

The ZX Interface 1 add-on module, launched in 1983, includes 8 KB of ROM, an RS-232 serial port, a proprietary local area network (LAN) interface known as ZX Net, and a port for connecting up to eight ZX Microdrives – tape-loop cartridge storage devices released in July 1983, known for their speed, albeit with some reliability concerns. Sinclair Research also introduced the ZX Interface 2, which added two joystick ports and a ROM cartridge port. Although the ZX Microdrives were initially greeted with good reviews, they never became a popular distribution method due to fears over cartridge quality and piracy.

Third-party hardware add-ons were available throughout the machine's life, including the Kempston joystick interface, the Morex Peripherals Centronics/RS-232 interface, the Currah Microspeech unit for speech synthesis, Videoface Digitiser, the SpecDrum drum machine, and the Multiface, a snapshot and disassembly tool from Romantic Robot. After the original ZX Spectrum's keyboard received criticism for its "dead flesh" feel, external keyboards became popular. In 1983, DK'Tronics launched a Light Pen compatible with some drawing software.

The Abbeydale Designers/Watford Electronics SPDOS and KDOS disk drive interfaces were bundled with office productivity software, including the Tasword word processor, Masterfile database, and Omnicalc spreadsheet. This bundle, along with OCP's Stock Control, Finance, and Payroll systems, introduced small businesses to streamlined computerised operations. In 1987 and 1988, Miles Gordon Technology released the DISCiPLE and +D systems. These systems had the capability to store memory images as disk snapshots, allowing users to restore the Spectrum to its exact previous state. Both systems were compatible with the Microdrive command syntax, simplifying the porting of existing software.

In the mid-1980s, Telemap Group launched a fee-based service allowing ZX Spectrum users to connect their machines to the Micronet 800 information provider via a Prism Micro Products VTX5000 modem. Micronet 800, hosted by Prestel, provided news and information about microcomputers and offered a form of instant messaging and online shopping.


## Software

Screenshots from the games

Rebelstar

(1984) and

Laser Squad

(1988)

Most Spectrum software was originally distributed on audio cassette tapes, intended to work with consumer cassette recorders. Software was also distributed through type-in program listings in magazines and books. The reader entered a program by hand and saved it to cassette for later use. Some magazines distributed 7" 331⁄3 rpm flexi disc records, or "Floppy ROMs", a variant of regular vinyl records which could be played on a standard record player. Some radio stations broadcast audio stream data via frequency modulation or medium wave so listeners could directly record it onto an audio cassette themselves. ZX Spectrum-focused radio programmes existed in the United Kingdom, which were received over long distances on domestic radio receivers.

Software released for the machine includes programming languages, databases, word processors (*Tasword* being the most prominent), spreadsheets, drawing and painting tools (e.g. OCP Art Studio), 3D-modelling (e.g. VU-3D) and archaeology software. Over 24,000 different software titles were released for the ZX Spectrum throughout its lifespan. Beginning in August 1982 the ZX Spectrum was bundled with *Horizons: Software Starter Pack*, a compilation of ten demonstration programs.

The ZX Spectrum has an extensive library of video games which established it as a prominent gaming platform in the 1980s, including *Manic Miner*, *Jet Set Willy*, *Chuckie Egg*, *Elite*, *Sabre Wulf*, *Knight Lore*, and *The Hobbit*. *Ant Attack* is the first video game with isometric graphics, *Turbo Esprit*, the first open world driving game, and *Redhawk* features the first superhero created specifically for a video game. Many ZX81 games were rewritten for the Spectrum to take advantage of the newer machine's colour and sound, such as Psion's *Flight Simulation*. Hardware limitations of the machine required a level of creativity from video game designers.


## Reception

Initial reception of the ZX Spectrum was generally positive. Critics in Britain welcomed the new machine as a worthy successor to the ZX81; Robin Bradbeer of *Sinclair User* praised the additional keyboard functions the Spectrum had to offer, and lauded the "strength" of its ergonomic and presentable design. Tim Hartnell from *Your Computer* noted that Sinclair had improved on the shortcomings of the ZX80 and ZX81 by revamping the Spectrum's load and save functions, noting that it made working with the machine "a pleasure". Hartnell concluded that despite minor faults, the machine was "way ahead" of its competitors, and its specification exceeded that of the BBC Micro Model A.

*Computer and Video Games*' Terry Pratt compared the Spectrum's keyboard negatively to the typewriter-style used on the BBC Micro, opining that it was an improvement over the ZX81 but unsuited for "typists". In similar vein, David Tebbutt from *Personal Computer World* felt that the Spectrum's keyboard felt more like a calculator than typewriter, but praised its functional versatility. Likewise, Gregg Williams from *BYTE* criticised the keyboard, declaring that despite the machine's attractive price the layout "is impossible to justify" and "poorly designed" in several respects. Williams was sceptical of the computer's appeal to American consumers if sold for US$220 – "hardly competitive with comparable low-cost American units" – and expected that Timex would sell it for $125–150. A more negative review came from Jim Lennox of *Technology Week*, who wrote that "after using it [...] I find Sinclair's claim that it is the most powerful computer under £500 unsustainable. Compared to more powerful machines, it is slow, its colour graphics are disappointing, its BASIC limited and its keyboard confusing".
