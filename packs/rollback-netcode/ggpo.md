---
title: "GGPO"
source: https://en.wikipedia.org/wiki/GGPO
domain: rollback-netcode
license: CC-BY-SA-4.0
tags: rollback netcode, ggpo netcode, deterministic rollback, fighting game netcode
fetched: 2026-07-02
---

# GGPO

**GGPO** (**Good Game Peace Out**) is middleware designed to help create a near-lagless online experience for various emulated arcade games and fighting games. The program was created by Tony Cannon, co-founder of fighting game community site *Shoryuken* and the popular Evolution Championship Series.

## History

Before its creation, GGPO creator Tony Cannon was completely dissatisfied with the 2006 Xbox 360 re-release of *Street Fighter II: Hyper Fighting* after experiencing its criticized online capabilities. As a reaction to its service, Cannon began development on GGPO and released the first version in late 2006. Cannon later demonstrated GGPO to Capcom, and it was positively received.

The downloadable GGPO client supported many games from Capcom and SNK, including *Super Street Fighter II Turbo*, *The King of Fighters 2002*, and Metal Slug X through the use of a built-in emulator. Video game companies have also implemented a licensed version of GGPO. Games using it include *Skullgirls* and *Street Fighter III: 3rd Strike Online Edition*.

On October 9, 2019, Cannon announced on his Twitter account that GGPO was now open source and available under the MIT License.

## Design

GGPO uses a netcode technique called "rollback". Rather than waiting for input to be received from other players before simulating the next frame, GGPO predicts the inputs they will send and simulates the next frame without delay using that assumption. When other players’ inputs arrive, if any input didn't match the prediction, GGPO rolls back the state of the game to the last correct state, then replays all players’ revised inputs back until the current frame. The hope is that the predictions will be correct most of the time, allowing smooth play with minimal sudden changes to the game state. The system in itself is highly similar to client-side prediction, but applied to a peer-to-peer setup.

The client program can allow players to manually adjust native input delay in high-ping situations, either creating a possibly-jerky yet accurate representation or a smoother game with input delay.

## GGPO client

GGPO was originally bundled with a client which enabled users to play supported games online with other players. A matchmaking system allowed players to request challenges from other users, while non-participants could spectate the match and chat. Once a challenge initiated, the match ran a ROM through its prepackaged emulator, FinalBurn Alpha. This client was discontinued, and superseded by other clients which make use of GGPO's networking middleware, such as Fightcade or RedGGPO.

## Games using GGPO

- *Final Fight: Double Impact* (2010)
- *Dragon Ball: Zenkai Battle* (2011)
- *Street Fighter III: 3rd Strike Online Edition* (2011)
- *Skullgirls* (2012)
- *Marvel vs. Capcom Origins* (2012)
- *Darkstalkers Resurrection* (2013)
- *Dungeons & Dragons: Chronicles of Mystara* (2013)
- *Divekick* (2013)
- *Metal Slug 3* (2014)
- *Lethal League* (2014)
- *Rising Thunder* (2015)
- *Skullgirls (mobile)* (2017)
- *Pocket Rumble* (2017)
- *Windjammers* (2017)
- *Punch Planet* (2017)
- *Omen of Sorrow* (2018)
- *Fantasy Strike* (2019)
- *Them's Fightin' Herds* (2020)
- *FOOTSIES Rollback Edition* (2020)
- *Terrordrome - Reign of the Legends* (2020)
- *Guilty Gear XX Accent Core Plus R* (2020)
- *Melty Blood: Type Lumina* (2021)
- *The King of Fighters XV* (2022)
- *Breakers Collection* (2023)
- *Samurai Shodown (2019)*(2023)
- *Under Night In-Birth II [Sys:Celes]* (2024)
- *Blazing Strike* (2024)
- *Coreupt* (2024)
