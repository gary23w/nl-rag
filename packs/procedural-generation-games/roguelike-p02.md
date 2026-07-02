---
title: "Roguelike (part 2/2)"
source: https://en.wikipedia.org/wiki/Roguelike
domain: procedural-generation-games
license: CC-BY-SA-4.0
tags: procedural generation, procedural content generation, roguelike generation, seeded generation
fetched: 2026-07-02
part: 2/2
---

## History

### Early history (1975–1980)

The creation of roguelike games came from hobbyist programmers and computer hackers, attempting to create games for the nascent computer field in the early 1980s, particularly influenced by the 1975 text adventure game *Colossal Cave Adventure* (often simply titled *Adventure*, or *advent* on filesystems without long filenames), and from the high fantasy setting of the tabletop game *Dungeons & Dragons*. Some elements of the roguelike genre were present in dungeon crawlers written for the PLATO system. This includes *pedit5* (1975) believed to be the first dungeon crawl game, and featured random monster encounters, though only used a single fixed dungeon level. *pedit5* inspired similar PLATO-based dungeon crawlers *dnd* (1975), *orthanc* (1978), *Moria* (1978), and *avatar* (1979). It is unclear if these PLATO games inspired the roguelike genre as there is no evidence that the early roguelike creators had access to these games. The core roguelike games were developed independently of each other, many of the developers not learning about their respective projects until several years after the genre took off.

Roguelike games were initially developed for computing environments with limited memory, including shared mainframe systems and early home computers; this limitation prevented developers from retaining all but a few dungeon levels in memory while the game was running, leading to procedural generation to avoid the memory storage issue. Procedural generation led to high replayability, as no two games were alike.

#### Concurrent variants

Though the term "roguelike" derives from the 1980 game *Rogue*, the first known game with the core roguelike gameplay elements was *Beneath Apple Manor* (1978), written by Don Worth for the Apple II; *Beneath Apple Manor* is also recognized as the first commercial roguelike game. The game, inspired by Worth's enjoyment of *Dungeons & Dragons* roleplaying, included procedural generation using a modification of the random maze generator from the game *Dragon Maze*, role-playing elements for the characters, tile-based movement and turn-based combat. Though *Beneath Apple Manor* predated *Rogue*, it was not as popular as *Rogue*: *Rogue* had advantage of being distributed over ARPANET which many college students had easy access to, while *Beneath Apple Manor* was packaged and sold by hand by Worth either at local stores or through mail fulfillment.

Another early roguelike whose development pre-dated *Rogue* was *Sword of Fargoal* (1982), developed by Jeff McCord starting in 1979. The game was based on *GammaQuest*, an earlier title McCord had created on the Commodore PET which he shared locally with friends while a student at Henry Clay High School in Kentucky; the game itself was based on a *Dungeons & Dragons* campaign he had run himself in the prior years. Before graduating and attending the University of Tennessee in 1981, he had started work on *GammaQuest II*, which required the player to navigate through randomly generated dungeon levels, acquire a sword, and make it back to the surface with that sword through more randomly generated levels. The more advanced computers available at the school, such as the VIC-20, enabled him to expand out the game further from the highly limited memory on the PET. On seeing the prospects of selling computer software, he eventually got a publication deal with Epyx, where they helped him to refine the marketing of the game, renaming it *Sword of Fargoal*, and giving him access to the more powerful Commodore 64, enabling him to use graphics and sound as part of the game. The game was considered a success, and when it was ported to the PC in 1983, it out-shone *Rogue*'s PC release the same year due to *Sword of Fargoal*'s superior graphics and sound.

#### *Rogue*

*Rogue* was written by Glenn Wichman and Michael Toy in 1980 while students at the University of California, Santa Cruz. The game was inspired by Toy's prior experience in playing the 1971 *Star Trek* game and programming clones of it for various other computer systems. It was also inspired by interactive fiction *Adventure*. While looking for a way to randomize the experience of *Adventure*, they came across Ken Arnold's curses library that enabled them to better manipulate characters on the terminal screen, prompting Toy and Wichman to create a graphical-like randomized adventure game. They created the story of the game by having the player seek out the "Amulet of Yendor", "Yendor" being "Rodney" spelled backwards, the name of the wizard they envisioned had created the dungeon. *Rogue* was originally executed on a VAX-11/780 computer; its limited memory forced them to use a simple text-based interface for the game. Toy eventually dropped out of school but got a job at the computing labs at University of California, Berkeley, where he met with Arnold. Arnold helped to optimize the curses code and implement more features into the game.

*Rogue* proved popular with college students and computer researchers at the time, including Ken Thompson; Dennis Ritchie had joked at the time that *Rogue* was "the biggest waste of CPU cycles in history". Its popularity led to the game's inclusion on BSD UNIX v4.2 in 1984, though at that time, without its source code. Toy and Arnold had anticipated selling *Rogue* commercially and were hesitant about releasing it; Toy would go on to meet Jon Lane at Olivetti, and together they would go on to create the company A.I. Design to port the games for various home systems along with publishing support by Epyx, later bringing Wichman back to help.

### Following evolution (1980–1995)

Rogue

1980

Other Variants

Hack

1982

Other Variants

Moria

1983

NetHack

1987

Other Variants

UMoria

1988

ADOM

1994

Angband

1990

Other Variants

ZAngband

1994

Other Variants

Tales of Maj'Eyal

2009

The hierarchy of the major Roguelike games that are known to descend from

Rogue

. Solid lines represent games developed from the parent's source code, while dotted lines represent games that were inspired by the parent game.

The popularity of *Rogue* led developers to create their own versions of the game, though their efforts were originally limited by the lack of access to *Rogue*'s source, which was not released until BSD v4.3 in 1986. These developers resorted to building games from scratch similar to *Rogue* but with features that they wanted to see. These versions would be distributed with source code, and along with the original *Rogue* source, other developers were able to create software forks of the games, adding in new monsters, items, and gameplay features, creating several dozen variants. This process was aided by switching code to languages with better data typing, including object-oriented and scripting languages, and cleaning up and modularizing the code so that contributors can better follow where changes can be made.

While there are some direct variants of *Rogue*, such as *Brogue*, most variants of *Rogue* could be classified into two branches based on two key games, *Moria* and *Hack*, that were developed in the spirit of *Rogue*.

#### *Moria*-based

*Moria* (1983) was developed by Robert Alan Koeneke while a student at University of Oklahoma, inspired by both *Adventure* and *Rogue*. Having access to a VAX-11/780, but without the source to *Rogue* due to computer administrator restrictions, he began trying to recreate *Rogue* but specifically flavored with the complex cave maze of the same name in J.R.R. Tolkien's Middle Earth stories. Following Tolkien's fiction, the player's goal was to descend to the depths of Moria to defeat the Balrog, akin to a boss battle. As with *Rogue*, levels were not persistent: when the player left the level and then tried to return, a new level would be procedurally generated. Among other improvements to *Rogue*, Koeneke included a persistent town at the highest level where players could buy and sell equipment, and the use of data structures within the Pascal language allowed him to create a more diverse bestiary within the game. He got help from several playtesters as well as another student, Jimmey Wayne Todd, who helped to program a deeper character generation system. *UMoria* (short for *UNIX Moria*) is a close variation on *Moria* by Jim E. Wilson, making the game more portable to a larger variety of computers while fixing various bugs.

*Angband* (1990) was developed by Alex Cutler and Andy Astrand while attending the University of Warwick. Having played *UMoria*, they wanted to expand the game even further. Working from *UMoria*'s code, they increased the number of levels and monsters, flavored the game based on Angband, the massive fortress controlled by Morgoth from Tolkien's fiction, and incorporated more of the deadlier creatures described within the Middle Earth mythology. They kept the Balrog as a difficult creature that must be overcome at a mid-game level, while Morgoth became the final boss the player must defeat to win the game. Following Cutler and Astrand's graduation, Sean March and Geoff Hill took over the development to see the game through to a public release outside of the university, adding in elements such as giving the player a sense of the rewards and dangers of a level when they entered it the first time.

Once *Angband* was released to the public via USENET, there were efforts to have code maintainers (the "devteam") to fix bugs, clean up the code and implement suggestions into the code. Due to numerous shifts in those maintaining the code (due to other obligations), and the number of potential user suggestions to include, *Angband* would become highly forked, leading to a number of *Angband* variants; at least sixty known variants exist with about a half dozen still under active development. One significant fork was *ZAngband* (1994) (short for *Zelazny Angband*), which expanded on *Angband* and altered the theme towards Roger Zelazny's *The Chronicles of Amber*. The *ZAngband* codebase would be used to create *Troubles of Middle Earth* (*ToME*) in 2002, which later swapped out the Tolkien and Zelazny fiction setting for a new original one to become *Tales of Maj'Eyal* (2009). The vanilla *Angband* remains in development today by the devteam.

#### *Hack*-based

*Hack* (1982) was developed by Jay Fenlason with help from Kenny Woodland, Mike Thome, and Jonathan Payne, students at Lincoln-Sudbury Regional High School at the time, while participating in the school's computer lab overseen by Brian Harvey. Harvey had been able to acquire a PDP-11/70 minicomputer for the school and instituted a course curriculum that allowed students to do whatever they wanted on the computers, including playing games, as long as they had completed assignments by the end of each semester. Fenlason, Woodland, Thome, and Payne met through these courses and became a close group of friends and competent programmers. Harvey had invited the group to the computer labs at UC Berkeley where they had the opportunity to use the mainframe systems there, and were introduced to *Rogue*, inspiring them to create their own version as their class project. Fenlason had created a list of features they wanted to improve upon in *Rogue* such as having a level's layout saved once the player moved off that level. They approached Toy and Arnold at a local USENIX conference for the source code to *Rogue*, but were refused, forcing them to develop the routines from scratch. The resulting program, *Hack*, stayed true to the original *Dungeons and Dragons* influences, and derived its name from being both a "hack and slash" game as well as a programming hack to recreate *Rogue* without having access to its source code. Fenlason was not able to include all the desired features, and his involvement in *Hack*'s development concluded after the students had left the school. Fenlason had provided the source code to *Hack* to the USENIX conferences to be distributed on their digital tapes, from which it was later discovered and built upon through USENET newsgroups, porting it to various systems. Like *Angband*, the maintainership of the *Hack* code passed through several hands, and some variants were created by different forks.

*Hack* would eventually be dropped in favor of *NetHack* (1987). When Mike Stephenson, an analyst at a computer hardware manufacturer, took maintainership of *Hack*'s code, he improved it, taking suggestions from Izchak Miller, a philosophy professor at University of Pennsylvania, and Janet Walz, another computer hacker. Calling themselves the DevTeam, they began to make major modifications to *Hack*'s code. They named their new version *NetHack*, in part due to their collaboration over the game being done through USENET. *NetHack*'s major deviations from *Hack* were the introduction of a wider variety of monsters, borrowing from other mythologies and lores, including anachronistic and contemporary cultural elements (such as a tourist class with a flash-bulb camera inspired by Terry Pratchett's *Discworld* series) in the high fantasy setting, and the use of pre-defined levels with some procedural elements that the player would encounter deeper in the dungeons. Further iterations of the game included branching pathways through the dungeon and optional character-based quests that could grant the player an extremely useful item to complete the game. Though the DevTeam released the code publicly, they carefully maintained who could contribute to the code base to avoid excessive forking of the vanilla game, and remain relatively quiet about suggested improvements to each release, working in relatively secrecy from its player base.

*Ancient Domains of Mystery* (1994), or *ADOM* for short, derived from concepts presented in *NetHack*. *ADOM* was originally developed by Thomas Biskup while a student at Technical University of Dortmund. After playing through *Rogue* and *Hack*, he came to *NetHack* and was inspired by the game but dismayed at the complexity and elements he found unnecessary or distracting. Biskup created *ADOM* from scratch with the aim of creating a more story-driven game than *NetHack* that kept the depth of gameplay with a focused theme and setting. The resulting game featured several different dungeons, many generated procedurally, connected through an overworld map of the fictional realm of Ancardia, and would have the player complete various quests in those dungeons to progress the game. A major feature was the influence of Chaos forces through unsealed portals, which the player would have to close. While in areas affected by Chaos, the player's character would become tainted, causing mutations that could be either detrimental or beneficial. *ADOM*, like *NetHack* and *Angband*, would gain a devteam to maintain the code and implement updates and patches to avoid excessive forking.

#### Other variants

Not all early roguelikes were readily classified as *Hack* or *Moria* descendants. *Larn* (1986), developed by Noah Morgan, borrowed concepts from both *Hack* (in that there are persistent and fixed levels) and *Moria* (in the availability of a shop level and general difficulty increasing with dungeon level), but while these two games have spiraled in size to take multiple play sessions to complete, *Larn* was aimed to be completed in a single session. *Larn* also uses a fixed-time feature, in that the player had only so many turns to complete a goal, though there were ways to jump back in time as to extend play. *Omega*, developed by Laurence Brothers in the late 1980s, is credited with introducing an overworld concept to the roguelike genre, prior to the feature's appearance in *ADOM*. *Omega* was often remembered for its odd inventory approach in which the player would have to pick up an object, considering it being held, and then moving that object to a bag or an equipment slot. *Linley's Dungeon Crawl* (1995) was created by Linley Henzell and featured a skill-based character progression system, in which experience points could be used to improve specific skills, such as weapon proficiency or trap detection. One fork of this would form the basis for *Dungeon Crawl Stone Soup* (2006). SSI's *Dungeon Hack* (1993) offered randomized dungeons and permadeath within AD&D 2nd Edition rules.

### *Mystery Dungeon* games (1993–onward)

Through 1993, roguelikes primarily existed in computer space, and no home console variants had yet existed. Two of the earliest-known attempts were Sega's *Fatal Labyrinth* (1990) and *Dragon Crystal* (1990), but which lacked the depth of a typical computer-based roguelike. Neither proved to be successful games. There was also the 1991 Japanese exclusive Game Boy game *Cave Noire* from Konami, that centred on four distinct roguelike questlines divided into ten difficulty levels.

Chunsoft had gained success by developing the *Dragon Quest* series, a series which established fundamental aspects of the computer role-playing game genre, popular for Western computer audiences, into a more streamlined approach better suited for Japanese players that preferred consoles. With roguelikes starting to gain popularity, Chunsoft's developers believed they could do a similar treatment for that genre to make it better suited for Japanese audiences. Chunsoft's Koichi Nakamura stated their intent was to take *Rogue* and make it "more understandable, more easy-to-play version" of the title that could be played on consoles. This led to the creation of the *Mystery Dungeon*, with the first title being *Torneko no Daibōken: Fushigi no Dungeon* (トルネコの大冒険 不思議のダンジョン, *Torneko's Great Adventure: Mystery Dungeon*) (1993) based on the *Dragon Quest* series. Several changes to the roguelike formula had to be made for this conversion: they had developed ways to reduce the difficulty of the roguelike by using progressively more difficult dungeons that were randomly generated, and made permadeath an option by selection of difficulty level. An added benefit for *Torneko no Daibōken* was that it used the established *Dragon Quest 4* setting and the character Torneko, helping to make the game familiar to its planned audience and giving a story for the player to follow. While *Torneko no Daibōken* did not sell as well as typical *Dragon Quest* games, it was successful enough for Chunsoft to develop a second title based on a wholly original character and setting, *Mystery Dungeon: Shiren the Wanderer*, released in 1995. Chunsoft found that they were more creative with how they developed the game without the need to respect an existing property. Since then, Chunsoft has developed over 25 games in the *Mystery Dungeon* series for various platforms, In addition to their *Shiren* titles, many of the other Chunsoft *Mystery Dungeon* games span various franchises, including *Chocobo* series based on *Final Fantasy*, *Pokémon Mystery Dungeon* based on *Pokémon*, and a crossover with Atlus' *Etrian Odyssey* in *Etrian Mystery Dungeon*. Several titles in the *Mystery Dungeon* series were popular, and would become a staple of the Japanese video game market.

A primary difference between the *Mystery Dungeon* games and Western roguelikes following the Berlin Interpretation is the lack of permadeath—in *Mystery Dungeon* games, player-characters may die or become too injured, resetting their progress to the start of the dungeon, but the games typically provide means to store and recover equipment and other items from the previous run. The *Mystery Dungeon* games were not as successful in Western markets when published there, as the target players—younger players who likely had not experienced games like *Rogue*—found the lack of a traditional role-playing game save system odd.

Other Japanese role-playing games would incorporate random dungeon generation as part of their design, mimicking part of the nature of roguelikes, and were considered roguelike titles when published in Western markets. Such titles include *Azure Dreams*, *Dark Cloud*, *Shining Soul*, and *Baroque*. The massively multiplayer online role-playing game *Final Fantasy XIV* added a randomly generated Deep Dungeon that was inspired by the procedural generation of roguelikes.

### Continued development in Western markets (2002–onward)

Though new classical roguelike variants would continue to be developed within the Western market, the genre languished as more advanced personal computers capable of improved graphics capabilities and games that utilized these features became popular. However, some of these new graphical games drew influence for roguelike concepts, notably action role-playing games like Blizzard Entertainment's *Diablo* (1996). *Diablo*'s creator, David Brevik, acknowledged that games like *Rogue*, *NetHack*, *Telengard* and other roguelikes influenced the design of *Diablo*, including the nature of randomly generated dungeons and loot.

Existing roguelikes continue to be developed: a sequel to *ADOM* successfully received crowd funding in 2012, while *NetHack*'s first major release in ten years in 2015 is set to help the DevTeam expand the game further. New roguelikes that adhere to core Berlin Interpretation rules are still being created, including *Dungeon Crawl Stone Soup* (2006), *Dungeons of Dredmor* (2011), and *Dragon Fin Soup* (2015). A subclass of "coffeebreak roguelikes" that could be completed in a short period of time have developed, often derived from entries in the Seven Day Roguelike Challenge; examples include such as *DoomRL* (2013) and *Desktop Dungeons* (2013) Some games would also take advantage of the ease of developing in the tile-based ASCII interfaces common to roguelikes. For example, the highly popular *Dwarf Fortress* (2006) uses the roguelike interface atop a construction and management simulation, and would serve as a major inspiration for *Minecraft*, while *SanctuaryRPG* (2014) is a more traditional turn-based role-playing game featuring a scripted story that uses an ASCII interface and roguelike gameplay elements. *UnReal World* (1992), the game that is considered to be the forerunner of the survival game genre, and which frequently uses procedural generation to create the worlds that players must survive in, was developed by Sami Maaranen and was influenced by roguelikes, with its initial interface being similar to that of *NetHack*.

### Growth of the rogue-lite (2005–onward)

The roguelike genre saw a resurgence in Western markets after 2000 through independent developers who created a new subgenre designated "rogue-lite", though the games are also sometimes called "roguelike-likes". Indie developers began to incorporate roguelike elements into genres not normally associated with roguelikes, creating games that would form the basis of this new subgenre. Two of the earliest cited examples of rogue-lites are *Strange Adventures in Infinite Space* (2002) and its sequel *Weird Worlds: Return to Infinite Space* (2005) by Digital Eel, both space exploration games that included randomly generated planets and encounters, and permadeath. Digital Eel based their work on the space exploration game *Starflight* along with roguelikes like *NetHack* but wanted to provide a shorter experience that would be easier to replay, akin to tabletop beer and pretzels games like *Deathmaze* and *The Sorcerer's Cave* that has elements in common with roguelikes.

*Spelunky* (2008), released shortly after the formation of the Berlin Interpretation, is considered to be a major contribution to the growth of indie-developed rogue-lites. *Spelunky* was developed by Derek Yu, who wanted to take the deep gameplay that is offered by roguelikes and combine it with the ease and pick-up-and-play of a platformer. The result was a platform game incorporating the notion of permadeath in which the player takes an explorer character through randomly generated caves. The intent was to create "deep" gameplay in which the game could be replayed over and over again, with the randomly generated situations driving the need for the player to develop novel, emergent strategies on the fly. Developer Jason Rohrer stated that *Spelunky* "totally revamped my thinking about single-player videogame design". Edmund McMillen, the developer of *The Binding of Isaac* (2011), and Kenny and Teddy Lee, the co-developers of *Rogue Legacy* (2012), credit Yu's approach with *Spelunky* as showing how to distill down the nature of a traditional roguelike to apply it to other gaming genres which they had done for their rogue-lites. Jay Ma and Matthew Davis, the co-developers of *FTL: Faster Than Light* (2012), credited both *Weird Worlds: Return to Infinite Space* and *Spelunky* as part of their influence for *FTL*. All of these games earned critical praise, and their success has led to a more modern resurgence in rogue-lites since their release.

The newfound success in rogue-lites is considered part of a larger trend in those that play both board and computer games, looking for "rich play experiences", as described by *100 Rogues* developer Keith Burgun, that more popular titles may not always offer. David Bamguart of Gaslamp Games stated that there is a thrill of the risk inherent in rogue-lites with random generation and permadeath, helping the player become more invested in the fate of their player character: "The deadly precariousness inherent to the unknown environments of roguelikes gives that investment a great deal of meaning." Additionally, many of these newer rogue-lites strive to address the apparent high difficulty and ruthlessness that traditional roguelikes were known for, and newer players will be able to find more help through user-generated game guides and walkthroughs made possible through wide Internet accessibility. Fabien Fischer offers that players have taken to independently developed rogue-lites as they have tired from "superficial gameplay, whitewashing spectacle, the content craze, and Skinner Box design" in titles produced by AAA developers and publishers.

McMillen of *The Binding of Isaac* said that including roguelike elements into other game mechanics can be difficult due to the complex interfaces roguelikes tend to have, but eventually "it becomes an increasingly beautiful, deep, and everlasting design that allows you to generate a seemingly dynamic experience for players, so that each time they play your game they're getting a totally new adventure". Procedural-generated world lets developers create many hours worth of game content without spending resources on designing detailed worlds.

Examples of successful games that have integrated roguelike components into other genres include:

- *Dead Cells*, a roguelike incorporated with Metroidvania-style of platform games
- *Slay the Spire*, bringing roguelike progression to a deck building game
- *Crypt of the Necrodancer* which uses a rhythm game-style approach in a roguelike dungeon
- *Enter the Gungeon* which establishes roguelike progression in a shoot 'em up
- *Vampire Survivors*, a minimalistic roguelike shoot 'em up.
- *Balatro*, a score attack style roguelike based on playing poker hands.
- *Blue Prince*, a roguelike with several puzzle game features as to solve a mystery.

*Hades*, a roguelite action role-playing game, was built to strongly incorporate elements of non-linear narrative into the game, giving the reason for the player to continually delve into replaying the game, and helped to draw in players to the roguelike genre that otherwise had been put off by its high difficulty level before.


## Community

The roguelike genre has developed with the expansion of both classical roguelikes and rogue-lite titles, a dedicated fan community has come about to not only discuss games within it but to craft their own tales of near-death adventures or amusing stories in roguelikes. Within this community, there is strong interest in developing roguelikes. The 7 Day Roguelike challenge (7DRL) was born out of a USENET newsgroup in 2005 for roguelike developers, informally challenging them to create the core of a novel roguelike within 7 days to be submitted for judging and play by the public. The competition has continued annually each year, since growing from 5–6 entries in 2005 to over 130 in 2014. In the spirit of the 2008 International Roguelike Conference, the "Roguelike Celebration" was held for the first time in September 2016 in San Francisco where several past and present roguelike developers gathered to discuss the history and future direction of the genre. It has since been organized again in 2017, 2018 and 2019 in San Francisco, and as virtual events in 2020, 2021, 2022, 2023 and 2024.
