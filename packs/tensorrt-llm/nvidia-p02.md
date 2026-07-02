---
title: "Nvidia (part 2/2)"
source: https://en.wikipedia.org/wiki/Nvidia
domain: tensorrt-llm
license: CC-BY-SA-4.0
tags: tensorrt inference, gpu kernel optimization, half precision inference, cuda acceleration
fetched: 2026-07-02
part: 2/2
---

## Deep learning

Nvidia GPUs are used in deep learning, and accelerated analytics due to Nvidia's CUDA software platform and API which allows programmers to utilize the higher number of cores present in GPUs to parallelize BLAS operations which are extensively used in machine learning algorithms. They were included in many Tesla, Inc. vehicles before Musk announced at Tesla Autonomy Day in 2019 that the company developed its own SoC and full self-driving computer now and would stop using Nvidia hardware for their vehicles. These GPUs are used by researchers, laboratories, tech companies and enterprise companies. In 2009, Nvidia was involved in what was called the "big bang" of deep learning, "as deep-learning neural networks were combined with Nvidia graphics processing units (GPUs)". That year, the Google Brain team used Nvidia GPUs to create deep neural networks capable of machine learning, where Andrew Ng determined that GPUs could increase the speed of deep learning systems by about 100 times.

### DGX

DGX is a line of supercomputers by Nvidia.

In April 2016, Nvidia produced the DGX-1 based on an 8 GPU cluster, to improve the ability of users to use deep learning by combining GPUs with integrated deep learning software. Nvidia gifted its first DGX-1 to OpenAI in August 2016 to help it train larger and more complex AI models with the capability of reducing processing time from six days to two hours. It also developed Nvidia Tesla K80 and P100 GPU-based virtual machines, which are available through Google Cloud, which Google installed in November 2016. Microsoft added GPU servers in a preview offering of its N series based on Nvidia's Tesla K80s, each containing 4992 processing cores. Later that year, AWS's P2 instance was produced using up to 16 Nvidia Tesla K80 GPUs. That month Nvidia also partnered with IBM to create a software kit that boosts the AI capabilities of Watson, called IBM PowerAI. Nvidia also offers its own Nvidia Deep Learning software development kit. In 2017, the GPUs were also brought online at the Riken Center for Advanced Intelligence Project for Fujitsu. The company's deep learning technology led to a boost in its 2017 earnings.

In 2018, Nvidia researchers demonstrated imitation-learning techniques for industrial robots. They have created a system that, after a short revision and testing, can already be used to control the universal robots of the next generation. In addition to GPU manufacturing, Nvidia provides parallel processing capabilities to researchers and scientists that allow them to efficiently run high-performance applications.

### Robotics

In 2020, Nvidia unveiled "Omniverse", a virtual environment designed for engineers. Nvidia also open-sourced Isaac Sim, which makes use of this Omniverse to train robots through simulations that mimic the physics of the robots and the real world.

In 2024, Huang oriented Nvidia's focus towards humanoid robots and self-driving cars, which he expects to gain widespread adoption.

In 2025, Nvidia announced Isaac GR00T N1, an open-source foundation model "designed to expedite the development and capabilities of humanoid robots". Neura Robotics, 1X Technologies and Vention are among the first companies to use the model.

### Automotive

NVIDIA has been involves in the automotive industry since introducing NVIDIA drive in CES 2015.

In April 2021, NVIDIA announced "DRIVE Sim" - A simulation platform for autonomous vehicles based on the Omniverse platform, which according to NVIDIA brought high fidelity, and was much more physically accurate and fully repeatable which is required for V&V.

In January 2026, NVIDIA announced Alpamayo, "family of open AI models, simulation tools and datasets designed to accelerate the next era of safe, reasoning‑based autonomous vehicle (AV) development.".


## Inception Program

Nvidia's Inception Program was created to support startups making exceptional advances in the fields of artificial intelligence and data science. Award winners are announced at Nvidia's GTC Conference. In May 2017, the program had 1,300 companies. As of March 2018, there were 2,800 startups in the Inception Program. As of August 2021, the program has over 8,500 members in 90 countries, with cumulative funding of US$60 billion.


## Controversies

### GTX 970 hardware specifications advertising dispute

Issues with the GeForce GTX 970's specifications were first brought up by users when they found out that the cards, while featuring 4 GB of memory, rarely accessed memory over the 3.5 GB boundary. Further testing and investigation eventually led to Nvidia issuing a statement that the card's initially announced specifications had been altered without notice before the card was made commercially available, and that the card took a performance hit once memory over the 3.5 GB limit were put into use.

The card's back-end hardware specifications, initially announced as being identical to those of the GeForce GTX 980, differed in the amount of L2 cache (1.75 MB versus 2 MB in the GeForce GTX 980) and the number of ROPs (56 versus 64 in the 980). Additionally, it was revealed that the card was designed to access its memory as a 3.5 GB section, plus a 0.5 GB one, access to the latter being 7 times slower than the first one. The company then went on to promise a specific driver modification to alleviate the performance issues produced by the cutbacks suffered by the card. However, Nvidia later clarified that the promise had been a miscommunication and there would be no specific driver update for the GTX 970. Nvidia claimed that it would assist customers who wanted refunds in obtaining them. On February 26, 2015, Nvidia CEO Jensen Huang went on record in Nvidia's official blog to apologize for the incident. In February 2015 a class-action lawsuit alleging false advertising was filed against Nvidia and Gigabyte Technology in the United States District Court for the Northern District of California.

Nvidia revealed that it is able to disable individual units, each containing 256 KB of L2 cache and 8 ROPs, without disabling whole memory controllers. This comes at the cost of dividing the memory bus into high speed and low speed segments that cannot be accessed at the same time unless one segment is reading while the other segment is writing because the L2/ROP unit managing both of the GDDR5 controllers shares the read return channel and the write data bus between the two GDDR5 controllers and itself. This is used in the GeForce GTX 970, which therefore can be described as having 3.5 GB in its high speed segment on a 224-bit bus and 0.5 GB in a low speed segment on a 32-bit bus.

On July 27, 2016, Nvidia agreed to a preliminary settlement of the U.S. class action lawsuit, offering a $30 refund on GTX 970 purchases. The agreed upon refund represents the portion of the cost of the storage and performance capabilities the consumers assumed they were obtaining when they purchased the card.

### GeForce Partner Program

The Nvidia GeForce Partner Program was a marketing program designed to provide partnering companies with benefits such as public relations support, video game bundling, and marketing development funds. The program proved to be controversial, with complaints about it possibly being an anti-competitive practice.

First announced in a blog post on March 1, 2018, it was canceled on May 4, 2018.

### Hardware Unboxed

On December 10, 2020, Nvidia told YouTube tech reviewer Steven Walton of Hardware Unboxed that it would no longer supply him with GeForce Founders Edition graphics card review units. In a Twitter message, Hardware Unboxed said, "Nvidia have officially decided to ban us from receiving GeForce Founders Edition GPU review samples. Their reasoning is that we are focusing on rasterization instead of ray tracing. They have said they will revisit this 'should your editorial direction change.'"

In emails that were disclosed by Walton from Nvidia Senior PR Manager Bryan Del Rizzo, Nvidia had said:

> ...your GPU reviews and recommendations have continued to focus singularly on rasterization performance, and you have largely discounted all of the other technologies we offer gamers. It is very clear from your community commentary that you do not see things the same way that we, gamers, and the rest of the industry do.

TechSpot, partner site of Hardware Unboxed, said, "this and other related incidents raise serious questions around journalistic independence and what they are expecting of reviewers when they are sent products for an unbiased opinion."

A number of technology reviewers came out strongly against Nvidia's move. Linus Sebastian, of Linus Tech Tips, titled the episode of his weekly WAN Show, "NVIDIA might ACTUALLY be EVIL..." and was highly critical of the company's move to dictate specific outcomes of technology reviews. The review site Gamers Nexus said it was, "Nvidia's latest decision to shoot both its feet: They've now made it so that any reviewers covering RT will become subject to scrutiny from untrusting viewers who will suspect subversion by the company. Shortsighted self-own from NVIDIA."

Two days later, Nvidia reversed its stance. Hardware Unboxed sent out a Twitter message, "I just received an email from Nvidia apologizing for the previous email & they've now walked everything back." On December 14, Hardware Unboxed released a video explaining the controversy from their viewpoint. Via Twitter, they also shared a second apology sent by Nvidia's Del Rizzo that said "to withhold samples because I didn't agree with your commentary is simply inexcusable and crossed the line."

### Improper disclosures about cryptomining

In 2018, Nvidia's chips became popular for cryptomining, the process of obtaining crypto rewards in exchange for verifying transactions on distributed ledgers, the United States Securities and Exchange Commission (SEC) said. However, the company failed to disclose that it was a "significant element" of its revenue growth from sales of chips designed for gaming, the SEC further added in a statement and charging order. Those omissions misled investors and analysts who were interested in understanding the impact of cryptomining on Nvidia's business, the SEC emphasized. Nvidia, which did not admit or deny the findings, has agreed to pay $5.5 million to settle civil charges, according to a statement made by the SEC in May 2022.

### French Competition Authority investigation

On September 26, 2023, Nvidia's French offices were searched by the French Competition Authority. The raid, authorized by a judge, was part of an investigation into suspected anti-competitive practices in the graphics card sector. Nvidia has not publicly commented on the incident.

### Chinese market halt

In August 2025, Nvidia ordered suppliers to halt production of its H20 AI chip following Chinese government directives warning domestic companies against purchasing the processor due to security concerns. The company directed suppliers including Taiwan Semiconductor Manufacturing Company, Samsung Electronics, and Amkor Technology to suspend work on the China-focused processor.

The H20 was developed in late 2023 specifically for the Chinese market to comply with U.S. export restrictions, featuring 96GB of HBM3 memory and 4.0 TB/s memory bandwidth-higher than the H100-but with significantly reduced computational power at 296 TFLOPs compared to the H100's 1979 TFLOPs. Despite lower raw performance, the H20 demonstrated over 20% faster performance than the H100 in large language model inference tasks due to architectural optimizations.

Prior to the production halt, Nvidia had placed substantial orders for the H20, including 300,000 units from TSMC in July 2025, driven by strong demand from Chinese technology companies. Despite China's efforts to shape technical standards, still, American products and ecosystem retain strong appeal, raising government experts concern. CEO Jensen Huang denied allegations that the H20 contained security backdoors, stating the chips were designed solely for commercial use. The production suspension occurred as Nvidia was developing the B30A, a new chip based on its Blackwell architecture intended to succeed the H20 in the Chinese market.

Despite criticism, the United States announced in 2026 that it would permit the export of newer H200 chips to China under specified conditions. The move was expected to stimulate market activity and U.S. influence. The Chinese market, estimated to be worth hundreds of billions and potentially trillions of U.S. dollars, presents significant profit opportunities for American firms, with revenues reinforcing leading positions. However, China quickly responded by imposing restrictions on certain foreign chips to be imported. China is leveraging the sanction to advance its domestic technology sector, while concerns have also emerged over possible fragmentation and reduced reinvestment in its own artificial intelligence development. China’s refusal to buy them could cost the company $30 billion.

### Data scraping and Anna's Archive piracy

Nvidia has been involved in heavy data scraping for illegal AI model training. In 2024, internal conversations revealed that Nvidia was scraping large amounts of videos from YouTube without permission, and by circumventing protection measures. In January 2026, a court filing revealed that Nvidia developers contacted shadow library Anna's Archive to evaluate the use of pirated content for model training, which management gave green light for despite legality concerns from the site. Nvidia denied the allegations and filed a motion to dismiss the lawsuit.
