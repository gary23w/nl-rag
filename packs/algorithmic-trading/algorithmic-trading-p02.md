---
title: "Algorithmic trading (part 2/2)"
source: https://en.wikipedia.org/wiki/Algorithmic_trading
domain: algorithmic-trading
license: CC-BY-SA-4.0
tags: algorithmic trading, high frequency trading, electronic trading, market microstructure
fetched: 2026-07-02
part: 2/2
---

## Effects

One of the more ironic findings of academic research on algorithmic trading might be that individual trader introduce algorithms to make communication more simple and predictable, while markets end up more complex and more uncertain. Since trading algorithms follow local rules that either respond to programmed instructions or learned patterns, on the micro-level, their automated and reactive behavior makes certain parts of the communication dynamic more predictable. However, on the macro-level, it has been shown that the overall emergent process becomes both more complex and less predictable. This phenomenon is not unique to the stock market, and has also been detected with editing bots on Wikipedia.

Though its development may have been prompted by decreasing trade sizes caused by decimalization, algorithmic trading has reduced trade sizes further. Jobs once done by human traders are being switched to computers. The speeds of computer connections, measured in milliseconds and even microseconds, have become very important.

More fully automated markets such as NASDAQ, Direct Edge and BATS (formerly an acronym for Better Alternative Trading System) in the US, have gained market share from less automated markets such as the NYSE. Economies of scale in electronic trading have contributed to lowering commissions and trade processing fees, and contributed to international mergers and consolidation of financial exchanges.

Competition is developing among exchanges for the fastest processing times for completing trades. For example, in June 2007, the London Stock Exchange launched a new system called TradElect that promises an average 10 millisecond turnaround time from placing an order to final confirmation and can process 3,000 orders per second. Since then, competitive exchanges have continued to reduce latency with turnaround times of 3 milliseconds available. This is of great importance to high-frequency traders, because they have to attempt to pinpoint the consistent and probable performance ranges of given financial instruments. These professionals are often dealing in versions of stock index funds like the E-mini S&Ps, because they seek consistency and risk-mitigation along with top performance. They must filter market data to work into their software programming so that there is the lowest latency and highest liquidity at the time for placing stop-losses and/or taking profits. With high volatility in these markets, this becomes a complex and potentially nerve-wracking endeavor, where a small mistake can lead to a large loss. Absolute frequency data play into the development of the trader's pre-programmed instructions.

In the U.S., spending on computers and software in the financial industry increased to $26.4 billion in 2005.

Algorithmic trading has caused a shift in the types of employees working in the financial industry. For example, many physicists have entered the financial industry as quantitative analysts. Some physicists have even begun to do research in economics as part of doctoral research. This interdisciplinary movement is sometimes called econophysics. Some researchers also cite a "cultural divide" between employees of firms primarily engaged in algorithmic trading and traditional investment managers. Algorithmic trading has encouraged an increased focus on data and had decreased emphasis on sell-side research.


## Communication standards

Algorithmic trades require communicating considerably more parameters than traditional market and limit orders. A trader on one end (the "buy side") must enable their trading system (often called an "order management system" or "execution management system") to understand a constantly proliferating flow of new algorithmic order types. The R&D and other costs to construct complex new algorithmic orders types, along with the execution infrastructure, and marketing costs to distribute them, are fairly substantial. What was needed was a way that marketers (the "sell side") could express algo orders electronically such that buy-side traders could just drop the new order types into their system and be ready to trade them without constant coding custom new order entry screens each time.

FIX Protocol is a trade association that publishes free, open standards in the securities trading area. The FIX language was originally created by Fidelity Investments, and the association Members include virtually all large and many midsized and smaller broker dealers, money center banks, institutional investors, mutual funds, etc. This institution dominates standard setting in the pretrade and trade areas of security transactions. In 2006–2007, several members got together and published a draft XML standard for expressing algorithmic order types. The standard is called FIX Algorithmic Trading Definition Language (FIXatdl).
