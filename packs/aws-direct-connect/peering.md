---
title: "Peering"
source: https://en.wikipedia.org/wiki/Peering
domain: aws-direct-connect
license: CC-BY-SA-4.0
tags: aws direct connect, dedicated network connection, private cloud link, hybrid network
fetched: 2026-07-02
---

# Peering

In computer networking, **peering** is a voluntary interconnection of administratively separate Internet networks for the purpose of exchanging traffic between the "down-stream" users of each network. Peering is settlement-free, also known as "bill-and-keep" or "sender keeps all", meaning that neither party pays the other in association with the exchange of traffic; instead, each derives and retains revenue from its own customers.

An agreement by two or more networks to peer is instantiated by a physical interconnection of the networks, an exchange of routing information through the Border Gateway Protocol (BGP), tacit agreement to norms of conduct and, in some extraordinarily rare cases (0.07%), a formalized contractual document.

In 0.02% of cases the word "peering" is used to describe situations where there is some settlement involved. Because these outliers can be viewed as creating ambiguity, the phrase "settlement-free peering" is sometimes used to explicitly denote normal cost-free peering.

## History

The first Internet exchange point was the Commercial Internet eXchange (CIX), formed by Alternet/UUNET (now Verizon Business), PSI, and CERFNET to exchange traffic without regard for whether the traffic complied with the acceptable use policy (AUP) of the NSFNet or ANS' interconnection policy. The CIX infrastructure consisted of a single router, managed by PSI, and was initially located in Santa Clara, California. Paying CIX members were allowed to attach to the router directly or via leased lines. After some time, the router was also attached to the Pacific Bell SMDS cloud. The router was later moved to the Palo Alto Internet Exchange, or PAIX, which was developed and operated by Digital Equipment Corporation (DEC). Because the CIX operated at OSI layer 3, rather than OSI layer 2, and because it was not neutral, in the sense that it was operated by one of its participants rather than by all of them collectively, and it conducted lobbying activities supported by some of its participants and not by others, it would not today be considered an Internet exchange point. Nonetheless, it was the first thing to bear that name.

The first exchange point to resemble modern, neutral, Ethernet-based exchanges was the Metropolitan Area Ethernet, or MAE, in Tysons Corner, Virginia. When the United States government de-funded the NSFNET backbone, Internet exchange points were needed to replace its function, and initial governmental funding was used to aid the preexisting MAE and bootstrap three other exchanges, which they dubbed NAPs, or "Network Access Points," in accordance with the terminology of the National Information Infrastructure document. All four are now defunct or no longer functioning as Internet exchange points:

- MAE-East – Located in Tysons Corner, Virginia, and later relocated to Ashburn, Virginia
- Chicago NAP – Operated by Ameritech and located in Chicago, Illinois
- New York NAP – Operated by Sprint and located in Pennsauken, New Jersey
- San Francisco NAP – Operated by PacBell and located in the Bay Area

As the Internet grew, and traffic levels increased, these NAPs became a network bottleneck. Most of the early NAPs utilized FDDI technology, which provided only 100 Mbit/s of capacity to each participant. Some of these exchanges upgraded to ATM technology, which provided OC-3 (155 Mbit/s) and OC-12 (622 Mbit/s) of capacity.

Other prospective exchange point operators moved directly into offering Ethernet technology, such as gigabit Ethernet (1,000 Mbit/s), which quickly became the predominant choice for Internet exchange points due to the reduced cost and increased capacity offered. Today, almost all significant exchange points operate solely over Ethernet, and most of the largest exchange points offer 10, 40, and even 100 gigabit service.

During the dot-com boom, many exchange point and carrier-neutral colocation providers had plans to build as many as 50 locations to promote carrier interconnection in the United States alone. Essentially all of these plans were abandoned following the dot-com bust, and today it is considered both economically and technically infeasible to support this level of interconnection among even the largest of networks.

## How peering works

The Internet is a collection of separate and distinct networks referred to as autonomous systems, each one consisting of a set of globally unique IP addresses and a unique global BGP routing policy.

The interconnection relationships between Autonomous Systems are of exactly two types:

- Peering - Two networks exchange traffic between their users freely, and for mutual benefit.
- Transit – One network pays another network for access to the Internet.

Therefore, in order for a network to reach any specific other network on the Internet, it must either:

- Sell transit service to that network or a chain of resellers ending at that network (making them a 'customer'),
- Peer with that network or with a network which sells transit service to that network, or
- Buy transit service from any other network (which is then responsible for providing interconnection to the rest of the Internet).

The Internet is based on the principle of *global* or *end-to-end reachability*, which means that any Internet user can transparently exchange traffic with any other Internet user. Therefore, a network is connected to the Internet if and only if it buys transit, or peers with every other network which also does not purchase transit (which together constitute a "default free zone" or "DFZ").

Public peering is done at Internet exchange points (IXPs), while private peering can be done with direct links between networks.

## Motivations for peering

Peering involves two networks coming together to exchange traffic with each other freely, and for mutual benefit. This 'mutual benefit' is most often the motivation behind peering, which is often described solely by "reduced costs for transit services". Other less tangible motivations can include:

- Increased redundancy (by reducing dependence on one or more transit providers).
- Increased capacity for extremely large amounts of traffic (distributing traffic across many networks).
- Increased routing control over one's traffic.
- Improved performance (attempting to bypass potential bottlenecks with a "direct" path).
- Improved perception of one's network (being able to claim a "higher tier").
- Ease of requesting for emergency aid (from friendly peers).

## Physical interconnections for peering

The physical interconnections used for peering are categorized into two types:

- Public peering – Interconnection utilizing a multi-party shared switch fabric such as an Ethernet switch.
- Private peering – Interconnection utilizing a point-to-point link between two parties.

### Public peering

**Public peering** is accomplished across a Layer 2 access technology, generally called a *shared fabric*. At these locations, multiple carriers interconnect with one or more other carriers across a single physical port. Historically, public peering locations were known as network access points (NAPs). Today they are most often called exchange points or *Internet exchanges* ("IXP"). Many of the largest exchange points in the world can have hundreds of participants, and some span multiple buildings and colocation facilities across a city.

Since public peering allows networks interested in peering to interconnect with many other networks through a single port, it is often considered to offer "less capacity" than private peering, but to a larger number of networks. Many smaller networks, or networks which are just beginning to peer, find that public peering exchange points provide an excellent way to meet and interconnect with other networks which may be open to peering with them. Some larger networks utilize public peering as a way to aggregate a large number of "smaller peers", or as a location for conducting low-cost "trial peering" without the expense of provisioning private peering on a temporary basis, while other larger networks are not willing to participate at public exchanges at all.

A few exchange points, particularly in the United States, are operated by commercial carrier-neutral third parties which often are data centers, which are critical for achieving cost-effective data center connectivity.

### Private peering

**Private peering** is the direct interconnection between only two networks, across a Layer 1 or 2 medium that offers dedicated capacity that is not shared by any other parties. Early in the history of the Internet, many private peers occurred across "telco" provisioned SONET circuits between individual carrier-owned facilities. Today, most private peering interconnections occur at carrier hotels data centers or carrier neutral colocation facilities, where a direct crossconnect (private network interconnect, PNI) can be provisioned between participants within the same building, usually for a much lower cost than telco circuits. Colocation centers often host private peering connections between their customers, internet transit providers and cloud providers, meet-me rooms for connecting customers together, Internet exchange points, and landing points and terminal equipment for fiber optic submarine communication cables, connecting the internet.

Most of the traffic on the Internet, especially traffic between the largest networks, occurs via private peering. However, because of the resources required to provision each private peer, many networks are unwilling to provide private peering to "small" networks, or to "new" networks which have not yet proven that they will provide a mutual benefit.

Tier 1 networks often do not participate in public Internet Exchanges but rather sell transit services to their participants and engage in private peering. Colocation centers often host private peering connections between their customers, internet transit (tier 1) providers and cloud providers.

## Peering agreement

Throughout the history of the Internet, there have been a spectrum of kinds of agreements between peers, ranging from handshake agreements to written contracts as required by one or more parties. Such agreements set forth the details of how traffic is to be exchanged, along with a list of expected activities which may be necessary to maintain the peering relationship, a list of activities which may be considered abusive and result in termination of the relationship, and details concerning how the relationship can be terminated. Detailed contracts of this type are typically used between the largest ISPs, as well as the ones operating in the most heavily regulated economies. As of 2011, such contracts account for less than 0.5% of all peering agreements.

## Depeering

By definition, peering is the voluntary and free exchange of traffic between two networks, for mutual benefit. If one or both networks believes that there is no longer a mutual benefit, they may decide to cease peering: this is known as **depeering**. Some of the reasons why one network may wish to depeer another include:

- A desire that the other network pay settlement, either in exchange for continued peering or for transit services.
- A belief that the other network is "profiting unduly" from the no-settlement interconnection.
- Concern over *traffic ratios*, which is related to the fair sharing of cost for the interconnection.
- A desire to peer with the upstream transit provider of the peered network.
- Abuse of the interconnection by the other party, such as *pointing default* or utilizing the peer for transit.
- Instability of the peered network, repeated routing leaks, lack of response to network abuse issues, etc.
- The inability or unwillingness of the peered network to provision additional capacity for peering.
- The belief that the peered network is unduly peering with one's customers.
- Various external political factors (including personal conflicts between individuals at each network).

In some situations, networks which are being depeered have been known to attempt to fight to keep the peering by intentionally breaking the connectivity between the two networks when the peer is removed, either through a deliberate act or an act of omission. The goal is to force the depeering network to have so many customer complaints that they are willing to restore peering. Examples of this include forcing traffic via a path that does not have enough capacity to handle the load, or intentionally blocking alternate routes to or from the other network. Some notable examples of these situations have included:

- BBN Planet *vs* Exodus Communications
- PSINet *vs* Cable & Wireless
- AOL Transit Data Network (ATDN) *vs* Cogent Communications
- France Telecom *vs* Cogent Communications
- France Telecom (Wanadoo) *vs* Proxad (Free)
- Level 3 Communications *vs* XO Communications
- Level 3 Communications *vs* Cogent Communications
- Telecom/Telefónica/Impsat/Prima *vs* CABASE (Argentina)
- Cogent Communications *vs* TeliaSonera
- Sprint-Nextel *vs* Cogent Communications
- SFR *vs* OVH
- The French ISP 'Free' *vs* YouTube

## Modern peering

### Donut peering model

The "donut peering" model describes the intensive interconnection of small and medium-sized regional networks that make up much of the Internet. Traffic between these regional networks can be modeled as a toroid, with a core "donut hole" that is poorly interconnected to the networks around it.

As detailed above, some carriers attempted to form a cartel of self-described Tier 1 networks, nominally refusing to peer with any networks outside the oligopoly. Seeking to reduce transit costs, connections between regional networks bypass those "core" networks. Data takes a more direct path, reducing latency and packet loss. This also improves resiliency between consumers and content providers via multiple connections in many locations around the world, in particular during business disputes between the core transit providers.

### Multilateral peering

The majority of BGP AS-AS adjacencies are the product of multilateral peering agreements, or MLPAs. In multilateral peering, an unlimited number of parties agree to exchange traffic on common terms, using a single agreement to which they each accede. The multilateral peering is typically technically instantiated in a route server or route reflector (which differ from looking glasses in that they serve routes back out to participants, rather than just listening to inbound routes) to redistribute routes via a BGP hub-and-spoke topology, rather than a partial-mesh topology. The two primary criticisms of multilateral peering are that it breaks the shared fate of the forwarding and routing planes, since the layer-2 connection between two participants could hypothetically fail while their layer-2 connections with the route server remained up, and that they force all participants to treat each other with the same, undifferentiated, routing policy. The primary benefit of multilateral peering is that it minimizes configuration for each peer, while maximizing the efficiency with which new peers can begin contributing routes to the exchange. While optional multilateral peering agreements and route servers are now widely acknowledged to be a good practice, mandatory multilateral peering agreements (MMLPAs) have long been agreed to not be a good practice.

### Peering locations

The modern Internet operates with significantly more peering locations than at any time in the past, resulting in improved performance and better routing for the majority of the traffic on the Internet. However, in the interests of reducing costs and improving efficiency, most networks have attempted to standardize on relatively few locations within these individual regions where they will be able to quickly and efficiently interconnect with their peering partners.

### Exchange points

As of 2021, the largest exchange points in the world are Ponto de Troca de Tráfego Metro São Paulo, in São Paulo, with 2,289 peering networks; OpenIXP in Jakarta, with 1,097 peering networks; and DE-CIX in Frankfurt, with 1,050 peering networks. The United States, with a historically larger focus on private peering and commercial public peering, has much less traffic visible on public peering switch-fabrics compared to other regions that are dominated by non-profit membership exchange points. Collectively, the many exchange points operated by Equinix are generally considered to be the largest, though traffic figures are not generally published. Other important exchange points include AMS-IX in Amsterdam, LINX and LONAP in London, and NYIIX in New York.

URLs to some public traffic statistics of exchange points include:

| AMS-IX DE-CIX | LINX MSK-IX | TORIX NYIIX | LAIIX TOP-IX | Netnod Mix Milano | ix.br SP SFMIX |
|---|---|---|---|---|---|

## Peering and BGP

A great deal of the complexity in the BGP routing protocol exists to aid the enforcement and fine-tuning of peering and transit agreements. BGP allows operators to define a policy that determines where traffic is routed. Three things are commonly used to determine routing: local-preference, multi exit discriminators (MEDs) and AS-Path. Local-preference is used internally within a network to differentiate classes of networks. For example, a particular network will have a higher preference set on internal and customer advertisements. Settlement free peering is then configured to be preferred over paid IP transit.

Networks that speak BGP to each other can engage in multi exit discriminator exchange with each other, although most do not. When networks interconnect in several locations, MEDs can be used to reference that network's interior gateway protocol cost. This results in both networks sharing the burden of transporting each other's traffic on their own network (or *cold potato*). *Hot-potato* or nearest-exit routing, which is typically the normal behavior on the Internet, is where traffic destined to another network is delivered to the closest interconnection point.

## Law and policy

Internet interconnection is not regulated in the same way that public telephone network interconnection is regulated. Nevertheless, Internet interconnection has been the subject of several areas of federal policy in the United States. Perhaps the most dramatic example of this is the attempted MCI Worldcom/Sprint merger. In this case, the Department of Justice blocked the merger specifically because of the impact of the merger on the Internet backbone market (thereby requiring MCI to divest itself of its successful "internetMCI" business to gain approval). In 2001, the Federal Communications Commission's advisory committee, the Network Reliability and Interoperability Council recommended that Internet backbones publish their peering policies, something that they had been hesitant to do beforehand. The FCC has also reviewed competition in the backbone market in its Section 706 proceedings which review whether advanced telecommunications are being provided to all Americans in a reasonable and timely manner.

Finally, Internet interconnection has become an issue in the international arena under something known as the International Charging Arrangements for Internet Services (ICAIS). In the ICAIS debate, countries underserved by Internet backbones have complained that it is unfair that they must pay the full cost of connecting to an Internet exchange point in a different country, frequently the United States. These advocates argue that Internet interconnection should work like international telephone interconnection, with each party paying half of the cost. Those who argue against ICAIS point out that much of the problem would be solved by building local exchange points. A significant amount of the traffic, it is argued, that is brought to the US and exchanged then leaves the US, using US exchange points as switching offices but not terminating in the US. In some worst-case scenarios, traffic from one side of a street is brought all the way to a distant exchange point in a foreign country, exchanged, and then returned to another side of the street. Countries with liberalized telecommunications and open markets, where competition between backbone providers occurs, tend to oppose ICAIS.
