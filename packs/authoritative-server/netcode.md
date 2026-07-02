---
title: "Netcode"
source: https://en.wikipedia.org/wiki/Netcode
domain: authoritative-server
license: CC-BY-SA-4.0
tags: authoritative server, server authority netcode, client-server game, anti-cheat server
fetched: 2026-07-02
---

# Netcode

**Netcode** is a blanket term most commonly used by gamers relating to networking in online games, often referring to synchronization issues between clients and servers.

Players often blame "bad netcode" when they experience lag or reverse state transitions when synchronization between players is lost. Although these events are sometimes caused by bugs, other networking-related causes include high latency between server and client, packet loss, or network congestion. Depending on the game implementation, these issues can also be caused by non-network factors such as frame rendering time or inconsistent frame rate. Netcode is often designed to mask networking irregularities and create a synchronous and smooth gamestate across multiple users.

## Netcode types

Unlike a local game where the inputs of all players are executed instantly in the same simulation or instance of the game, in an online game there are several parallel simulations (one for each player) where the inputs from their respective players are received instantly, while the inputs for the same frame from other players arrive with a certain delay (greater or lesser depending on the physical distance between the players, the quality and speed of the players' network connections, etc.). During an online match, games must receive and process players' input within a certain time for each frame (roughly 16.5 ms per frame at 60 FPS), and if a remote player's input of a particular frame (for example, of frame number 10) arrives when another one is already running (for example, in frame number 20, roughly 170 ms later), desynchronization between player simulations is produced. There are two main resolutions to this conflict implemented in modern games: delay-based and rollback-based resolution.

### Delay-based

The classic solution to this problem is the use of a delay-based netcode. When the inputs of a remote player arrive late, the game delays the inputs of the local player accordingly to synchronize the two inputs and run them simultaneously. This added delay can be disruptive for players (especially when latency is high), but overall the change is not very noticeable. However, these delays can be inconsistent due to sudden fluctuations in current latency. Should the latency between players exceed an established buffer window for the remote player, the game must wait, causing the screens to "freeze". This occurs because a delay-based netcode does not allow the simulation to continue until it receives the inputs from all the players in the frame in question. This variable delay causes an inconsistent and unresponsive experience compared to offline play (or to a LAN game), and can negatively affect player performance in timing-sensitive and fast-paced genres such as fighting games.

### Rollback

An alternative system to the previous netcode is rollback netcode. This system immediately runs the inputs of the local player (so that they are not delayed as with delay-based netcode), as if it were an offline game, and predicts the inputs of the remote player or players instead of waiting for them (assuming they will make the same input as the one in the previous tick). Once these remote inputs arrive (suppose, e.g., 45 ms later), the game can act in two ways: if the prediction is correct, the game continues as-is, in a totally continuous way; if the prediction was incorrect, the game state is reverted and gameplay continues from the corrected state, seen as a "jump" to the other player or players (equivalent to 45 ms, following the example). Some games utilize a hybrid solution in order to disguise these "jumps" (which can become problematic as latency between players grows, as there is less and less time to react to other players' actions) with a fixed input delay and then rollback being used. Rollback is quite effective at concealing lag spikes or other issues related to inconsistencies in the users' connections, as predictions are often correct and players do not even notice. Nevertheless, this system can be troublesome whenever a client's game slows down (usually due to overheating), since rift problems can be caused leading to an exchange of tickets between machines at unequal rates. This generates visual glitches that interrupt the gameplay of those players that receive inputs at a slower pace, while the player whose game is slowed down will have an advantage over the rest by receiving inputs from others at a normal rate (this is known as one-sided rollback). To address this uneven input flow (and consequently, an uneven frame flow as well), there are standard solutions such as waiting for the late entries to arrive to all machines (similar to the delay-based netcode model) or more ingenious solutions as the one currently used in *Skullgirls*, which consists of the systematic omission of one frame every seven so that when the game encounters the problem in question it can recover the skipped frames in order to gradually synchronize the instances of the games on the various machines.

Rollback netcode requires the game engine to be able to turn back its state, which requires modifications to many existing engines, and therefore, the implementation of this system can be problematic and expensive in AAA type games (which usually have a solid engine and a high-traffic network), as commented by *Dragon Ball FighterZ* producer Tomoko Hiroki, among others.

Although this system is often associated with a peer-to-peer architecture and fighting games, there are forms of rollback networking that are also commonly used in client-server architectures (for instance, aggressive schedulers found in database management systems include rollback functionality) and in other video game genres.

There is a popular MIT-licensed library named GGPO designed to help implement rollback networking to games (mainly fighting games).

#### Games using rollback netcode

- *Super Street Fighter II Turbo HD Remix* (2008)
- *Marvel vs. Capcom 2: New Age of Heroes* (2009)
- *Touhou Suimusou: Immaterial and Missing Power* (2009)
- *Street Fighter X Tekken* (2012)
- *Touhou Hisoutensoku* (2012)
- *Killer Instinct* (2013)
- *Killer Instinct Classic* (2013)
- *Killer Instinct 2 Classic* (2014)
- *Eternal Fighter Zero* (2014)
- *Melty Blood Actress Again Current Code* (2015)
- *Brawlhalla* (2015)
- *Street Fighter V* (2016)
- *Mortal Kombat XL* (2016)
- *For Honor* (2017)
- *River City Ransom: Underground* (2017)
- *Injustice 2* (2017)
- *Marvel vs. Capcom: Infinite* (2017)
- *Umineko: Golden Fantasia* (2017)
- *Acceleration of Suguri 2* (2018)
- *The King of Fighters '97 Global Match* (2018)
- *Street Fighter 30th Anniversary Collection* (2018)
- *Lethal League Blaze* (2018)
- *Mortal Kombat 11* (2019)
- *Fight of Gods* (2019)
- *Samurai Shodown V Special* (2019)
- *Power Rangers: Battle for the Grid* (2019)
- *Fight of Animals* (2019)
- *Garou: Mark of the Wolves* (2020)
- *Maiden & Spell* (2020)
- *Mighty Fight Federation* (2020)
- *The Last Blade 2* (2020)
- *Samurai Shodown NeoGeo Collection* (2020)
- *Super Smash Bros. Melee* (2020)
- *Fighting EX Layer* (2020)
- *Spelunky 2* (2020)
- *The King of Fighters 2002: Unlimited Match* (2020)
- *Dual Souls: The Last Bearer* (2020)
- *Tough Love Arena* (2021)
- *Guilty Gear -Strive-* (2021)
- *Dengeki Bunko: Fighting Climax Ignition* (2021)
- *The King of Fighters All Star* (2021)
- *Rivals of Aether* (2021)
- *Petal Crash Online* (2021)
- *Nickelodeon All-Star Brawl* (2021)
- *The King of Fighters '98: Ultimate Match Final Edition* (2021)
- *Windjammers 2* (2022)
- *BlazBlue: Central Fiction* (2022)
- *BlazBlue: Cross Tag Battle* (2022)
- *The King of Fighters XV* (2022)
- *DNF Duel* (2022)
- *MultiVersus* (2022-2025)
- *Persona 4 Arena Ultimax* (2022)
- *Mega Man Battle Network* (2022)
- *Mega Man Battle Network 2* (2022)
- *Mega Man Battle Network 3* (2022)
- *Mega Man Battle Network 4* (2022)
- *Rockman EXE 4.5 Real Operation* (2022)
- *Mega Man Battle Network 5* (2022)
- *Mega Man Battle Network 6* (2022)
- *Capcom Fighting Collection* (2022)
- *Teenage Mutant Ninja Turtles: Tournament Fighters* (2022)
- *The Rumble Fish 2* (2022)
- *Guilty Gear Xrd REV 2* (2023)
- *IKEMEN-Go* (2023)
- *Street Fighter 6* (2023)
- *Mortal Kombat 1* (2023)
- *Nickelodeon All-Star Brawl 2* (2023)
- *The King of Fighters XIII: Global Match* (2023)
- *Granblue Fantasy Versus: Rising* (2023)
- *Tekken 8* (2024)
- *Dragon Ball FighterZ*(2024)
- *SNK vs. Capcom: SVC Chaos* (2024)
- Marvel vs. Capcom Fighting Collection: Arcade Classics (2024)
- *Virtua Fighter 5 R.E.V.O.* (2025)
- *Iron Saga VS* (2025)
- *Fatal Fury: City of the Wolves* (2025)
- *Capcom Fighting Collection 2* (2025)
- *Hunter × Hunter: Nen × Impact* (2025)
- *Stormgate* (2025)
- *Real Bout Fatal Fury 2: The Newcomers* (2025)
- *Kizuna Encounter: Super Tag Battle* (2025)
- *Mortal Kombat: Legacy Kollection* (2025)
- *Daemon Bride: Additional Gain* (2025)
- *2XKO* (2026)
- *Marvel MaXimum Collection* (2026)
- *Invincible VS* (2026)
- *World Heroes Perfect* (2026)
- *Ninja Master's: Haō Ninpō Chō* (2026)
- *Slayers for Hire* (TBA)
- *Fly Punch Boom!* (TBA)
- *Rushdown Revolt* (2023)
- *MerFight: Curse of the Arctic Prince* (2024)
- *Animation VERSUS* (2028)
- *Metal Revolution* (Cancelled)
- *Marvel Tokon: Fighting Souls* (2026)
- *Avatar Legends: The Fighting Game* (2026)
- *NBA The Run* (2026)
- Super Smash Bros. (2026)

## Potential causes of netcode issues

### Latency

Latency is unavoidable in online games, and the quality of the player's experience is strictly tied to this (the more latency there is between players, the greater the feeling that the game is not responsive to their inputs). The latency of the players' network (which is largely out of a game's control) is not the only factor in question, but also the latency inherent in the way the game simulations are run. There are several lag compensation methods used to disguise or cope with latency (especially with high latency values).

### Tick rate

A single update of a game simulation is known as a tick. The rate at which the simulation is run on a server is often referred to as the server's tickrate; this is essentially the server equivalent of a client's frame rate, absent any rendering system. Tickrate is limited by the length of time it takes to run the simulation, and is often intentionally limited further to reduce instability introduced by a fluctuating tickrate, and to reduce CPU and data transmission costs. A lower tickrate increases latency in the synchronization of the game simulation between the server and clients. Tickrate for games like first-person shooters is often between 128 ticks per second (such is Valorant's case)*,* 64 ticks per second (in games like Counter-Strike: Global Offensive and Overwatch), 30 ticks per second (like in Fortnite and Battlefield V's console edition) and 20 ticks per second (such are the controversial cases of Call of Duty: Modern Warfare, Call of Duty: Warzone and Apex Legends). A lower tickrate also naturally reduces the precision of the simulation, which itself might cause problems if taken too far, or if the client and server simulations are running at significantly different rates.

Because of limitations in the amount of available bandwidth and the CPU time that's taken by network communication, some games prioritize certain vital communications while limiting the frequency and priority of less important information. As with tickrate, this effectively increases synchronization latency. Game engines may limit the number of times that updates (of a simulation) are sent to a particular client and/or particular objects in the game's world in addition to reducing the precision of some values sent over the network to help with bandwidth use. This lack of precision may in some instances be noticeable.

### Software bugs

Various simulation synchronization errors between machines can also fall under the "netcode issues" blanket. These may include bugs which cause the simulation to proceed differently on one machine than on another, or which cause some things to not be communicated when the user perceives that they ought to be. Traditionally, real-time strategy games (such as Age of Empires) have used lockstep protocol peer-to-peer networking models where it is assumed the simulation will run exactly the same on all clients; if, however, one client falls out of step for any reason, the desynchronization may compound and be unrecoverable.

### Transport layer protocol and communication code: TCP and UDP

A game's choice of transport layer protocol (and its management and coding) can also affect perceived networking issues.

If a game uses Transmission Control Protocol (TCP), there will be increased latency between players. This protocol is based on the connection between two machines, in which they can exchange data and read it. These types of connections are very reliable, stable, ordered and easy to implement. These connections, however, are not quite suited to the network speeds that fast-action games require, as this type of protocol automatically groups data into packets (which will not be sent until a certain volume of information is reached, unless this algorithm — Nagle's algorithm — is disabled) which will be sent through the connection established between the machines, rather than directly (sacrificing speed for security). This type of protocol also tends to respond very slowly whenever they lose a packet, or when packets arrive in an incorrect order or duplicated, which can be very detrimental to a real-time online game (this protocol was not designed for this type of software).

If the game instead uses a User Datagram Protocol (UDP), the connection between machines will be very fast, because instead of establishing a connection between them the data will be sent and received directly. This protocol is much simpler than the previous one, but it lacks its reliability and stability and requires the implementation of own code to handle indispensable functions for the communication between machines that are handled by TCP (such as data division through packets, automatic packet loss detection, etc.); this increases the engine's complexity and might itself lead to issues.
