---
title: "Nvidia (part 1/2)"
source: https://en.wikipedia.org/wiki/Nvidia
domain: tensorrt
license: CC-BY-SA-4.0
tags: tensorrt runtime, inference optimization, gpu acceleration, model quantization, low latency serving
fetched: 2026-07-02
part: 1/2
---

# Nvidia

Checked


## Page version status

This is an accepted version of this page

This is the

latest accepted revision

,

reviewed

on

1 July 2026

.

**Nvidia Corporation** (/ɛnˈvɪdiə/ *en-VID-ee-ə*) is an American multinational technology company headquartered in Santa Clara, California. The company develops graphics processing units (GPUs), systems on chips (SoCs), and application programming interfaces (APIs) for data science, high-performance computing, artificial intelligence (AI), and mobile and automotive applications. Founded in 1993 by Jensen Huang, Chris Malachowsky, and Curtis Priem, Nvidia has been widely described as a Big Tech company.

Originally focused on GPUs for video games, Nvidia broadened their use into other markets, including artificial intelligence (AI), professional visualization, and supercomputing. The company's product lines include GeForce GPUs for gaming and creative workloads, and professional GPUs for edge computing, scientific research, and industrial applications. As of the first quarter of 2025, Nvidia held a 92% share of the discrete desktop and laptop GPU market.

In the early-to-mid 2000s, the company invested over a billion dollars to develop CUDA, a software platform and API (Application Programming Interfaces) that enabled GPUs to run massively parallel programs for a broad range of compute-intensive applications. As a result, as of 2025, Nvidia controlled more than 80% of the market for GPUs used in training and deploying AI models, and provided chips for over 75% of the world's TOP500 supercomputers. The company has also expanded into gaming hardware and services, with products such as the Shield Portable, Shield Tablet, and Shield TV, and operates the GeForce Now cloud gaming service. Furthermore, it has developed the Tegra line of mobile processors for smartphones, tablets, and automotive infotainment systems.

In 2023, Nvidia became the seventh U.S. company to reach a US$1 trillion valuation. In 2025, amid increased demand for AI data center hardware in the midst of the AI boom, Nvidia became the first company in the world to surpass US$4 trillion and US$5 trillion in market capitalization. Because of its market capitalization and role in major technology indexes, Nvidia has been selected as one of Bloomberg's "Magnificent Seven", the seven biggest companies on the stock market in these regards.


## History

### Founding

Nvidia was founded on April 5, 1993, by Jensen Huang, a Taiwanese-American electrical engineer who was previously the director of CoreWare at LSI Logic and a microprocessor designer at AMD; Chris Malachowsky, an engineer who worked at Sun Microsystems; and Curtis Priem, who was previously a senior staff engineer and graphics chip designer at IBM and Sun Microsystems. In late 1992, the three men agreed to start the company in a meeting at a Denny's roadside diner on Berryessa Road in East San Jose.

At the time, Malachowsky and Priem were frustrated with Sun's management and were looking to leave, but Huang was on "firmer ground", in that he was already running his own division at LSI. The three co-founders discussed a vision of the future which was so compelling that Huang decided to leave LSI and become the chief executive officer of their new startup.

The three co-founders envisioned graphics-based processing as the best trajectory for tackling challenges that had eluded general-purpose computing methods. As Huang later explained: "We also observed that video games were simultaneously one of the most computationally challenging problems and would have incredibly high sales volume. Those two conditions don't happen very often. Video games was our killer app - a flywheel to reach large markets funding huge R&D to solve massive computational problems."

The first problem was who would quit first. Huang's wife, Lori, did not want him to resign from LSI unless Malachowsky resigned from Sun at the same time, and Malachowsky's wife, Melody, felt the same way about Huang. Priem broke that deadlock by resigning first from Sun, effective December 31, 1992. According to Priem, this put pressure on Huang and Malachowsky to not leave him to "flail alone", so they gave notice too. Huang left LSI and "officially joined Priem on February 17", which was also Huang's 30th birthday, while Malachowsky left Sun in early March. In early 1993, the three founders began working together on their new startup in Priem's townhouse in Fremont, California.

With $40,000 in the bank (equivalent to $89,000 in 2025), the company was born. The company subsequently received $20 million of venture capital funding from Sequoia Capital, Sutter Hill Ventures, and others.

During the late 1990s, Nvidia was one of 70 startup companies pursuing the idea that graphics acceleration for video games was the path to the future. Only two survived: Nvidia and ATI Technologies, the latter of which merged into AMD.

Nvidia initially had no name. Priem's first idea was "Primal Graphics", a syllabic abbreviation of two of the founders' last names, but that left out Huang. They soon discovered it was impossible to create a workable name with syllables from all three founders' names, after considering "Huaprimal", "Prihuamal", "Malluapri", etc. The next idea came from Priem's idea for the name of Nvidia's first product. Priem originally wanted to call it the "GXNV", as in the "next version" of the GX graphics chips which he had worked on at Sun. Then Huang told Priem to "drop the GX", resulting in the name "NV". Priem made a list of words with the letters "NV" in them. At one point, Malachowsky and Priem wanted to call the company NVision, but that name was already taken by a manufacturer of toilet paper. Both Priem and Huang have taken credit for coming up with the name Nvidia, from "invidia", the Latin word for "envy".

After the company outgrew Priem's townhouse, its original headquarters office was in Sunnyvale, California.

### First graphics accelerator

Nvidia's first graphics accelerator, the NV1, was designed to process quadrilateral primitives (forward texture mapping), a feature that set it apart from competitors, who preferred triangle primitives. However, when Microsoft introduced the DirectX platform, it chose not to support any other graphics software and announced that its Direct3D API would exclusively support triangles. As a result, the NV1 failed to gain traction in the market.

Nvidia had also entered into a partnership with Sega to supply the graphics chip for the Dreamcast console and worked on the project for about a year. However, Nvidia's technology was already lagging behind competitors. This placed the company in a difficult position: continue working on a chip that was likely doomed to fail or abandon the project, risking financial collapse.

In a pivotal moment, Sega's president, Shoichiro Irimajiri, visited Huang in person to inform him that Sega had decided to choose another vendor for the Dreamcast. However, Irimajiri believed in Nvidia's potential and persuaded Sega's management to invest $5 million into the company. Huang later reflected that this funding was all that kept Nvidia afloat, and that Irimajiri's "understanding and generosity gave us six months to live".

In 1996, Huang laid off more than half of Nvidia's employees-reducing headcount from 100 to 40-and focused the company's remaining resources on developing a graphics accelerator product optimized for processing triangle primitives: the RIVA 128. By the time the RIVA 128 was released in August 1997, Nvidia had only enough money left for one month's payroll. The sense of impending failure became so pervasive that it gave rise to Nvidia's unofficial company motto: "Our company is thirty days from going out of business." Huang began internal presentations to Nvidia staff with those words for many years.

Nvidia sold about a million RIVA 128 units within four months, and used the revenue to fund development of its next generation of products. In 1998, the release of the RIVA TNT helped solidify Nvidia's reputation as a leader in graphics technology.

### Public company

Nvidia went public on January 22, 1999. Investing in Nvidia after it had already failed to deliver on its contract turned out to be Irimajiri's best decision as Sega's president. After Irimajiri left Sega in 2000, Sega sold its Nvidia stock for $15 million.

In late 1999, Nvidia released the GeForce 256 (NV10), its first product expressly marketed as a GPU, which was most notable for introducing onboard transformation and lighting (T&L) to consumer-level 3D hardware. Running at 120 MHz and featuring four-pixel pipelines, it implemented advanced video acceleration, motion compensation, and hardware sub-picture alpha blending. The GeForce outperformed existing products by a wide margin.

Because its products were performing well, Nvidia won the contract to develop the graphics hardware for Microsoft's Xbox game console, which included a $200 million advance. However, the project took many of its best engineers away from other projects. In the short term this did not matter, and the GeForce 2 GTS shipped in the summer of 2000. In December 2000, Nvidia reached an agreement to acquire the intellectual assets of its one-time rival 3dfx, a pioneer in consumer 3D graphics technology leading the field from the mid-1990s until 2000. The acquisition process was finalized in April 2002.

In 2001, Standard & Poor's selected Nvidia to replace the departing Enron in the S&P 500 stock index, meaning that index funds would need to hold Nvidia shares going forward.

In July 2002, Nvidia acquired Exluna for an undisclosed sum. Exluna made software-rendering tools and its personnel were merged into Nvidia's Cg project. In August 2003, Nvidia acquired MediaQ for approximately US$70 million. It launched GoForce the following year. On April 22, 2004, Nvidia acquired iReady, also a provider of high-performance TCP offload engines and iSCSI controllers. In December 2004, it was announced that Nvidia would assist Sony with the design of the graphics processor (RSX) for the PlayStation 3 game console. On December 14, 2005, Nvidia acquired ULI Electronics, which at the time supplied third-party southbridge parts for chipsets to ATI, Nvidia's competitor. In March 2006, Nvidia acquired Hybrid Graphics. In December 2006, Nvidia, along with its main rival in the graphics industry AMD (which had acquired ATI), received subpoenas from the United States Department of Justice regarding possible antitrust violations in the graphics card industry.

### 2007–2014

*Forbes* named Nvidia its *Company of the Year* for 2007, citing the accomplishments it made during the said period as well as during the previous five years. On January 5, 2007, Nvidia announced that it had completed the acquisition of PortalPlayer, Inc. In February 2008, Nvidia acquired Ageia, developer of PhysX, a physics engine and physics processing unit. Nvidia announced that it planned to integrate the PhysX technology into its future GPU products.

In July 2008, Nvidia took a write-down of approximately $200 million on its first-quarter revenue, after reporting that certain mobile chipsets and GPUs produced by the company had "abnormal failure rates" due to manufacturing defects. Nvidia, however, did not reveal the affected products. In September 2008, Nvidia became the subject of a class action lawsuit over the defects, claiming that the faulty GPUs had been incorporated into certain laptop models manufactured by Apple Inc., Dell, and HP. In September 2010, Nvidia reached a settlement, in which it would reimburse owners of the affected laptops for repairs or, in some cases, replacement. On January 10, 2011, Nvidia signed a six-year, $1.5 billion cross-licensing agreement with Intel, ending all litigation between the two companies.

In November 2011, after initially unveiling it at Mobile World Congress, Nvidia released its ARM-based system on a chip for mobile devices, Tegra 3. Nvidia claimed that the chip featured the first-ever quad-core mobile CPU. In May 2011, it was announced that Nvidia had agreed to acquire Icera, a baseband chip making company in the UK, for $367 million. In January 2013, Nvidia unveiled the Tegra 4, as well as the Nvidia Shield, an Android-based handheld game console powered by the new system on a chip. On July 29, 2013, Nvidia announced that it acquired PGI from STMicroelectronics.

In February 2013, Nvidia announced its plans to build a new headquarters in the form of two giant triangle-shaped buildings on the other side of San Tomas Expressway (to the west of its existing headquarters complex). The company selected triangles as its design theme. As Huang explained in a blog post, the triangle is "the fundamental building block of computer graphics".

In 2014, Nvidia ported the Valve games *Portal* and *Half Life 2* to its Nvidia Shield Tablet as Lightspeed Studio. Since 2014, Nvidia has diversified its business focusing on three markets: gaming, automotive electronics, and mobile devices.

That same year, Nvidia also prevailed in litigation brought by the trustee of 3dfx's bankruptcy estate to challenge its 2000 acquisition of 3dfx's intellectual assets. On November 6, 2014, in an unpublished memorandum order, the United States Court of Appeals for the Ninth Circuit affirmed the "district court's judgment affirming the bankruptcy court's determination that [Nvidia] did not pay less than fair market value for assets purchased from 3dfx shortly before 3dfx filed for bankruptcy".

### 2016–2018

On May 6, 2016, Nvidia unveiled the first GPUs of the GeForce 10 series, the GTX 1080 and 1070, based on the company's new Pascal microarchitecture. Nvidia claimed that both models outperformed its Maxwell-based Titan X model; the models incorporate GDDR5X and GDDR5 memory respectively, and use a 16 nm manufacturing process. The architecture also supports a new hardware feature known as simultaneous multi-projection (SMP), which is designed to improve the quality of multi-monitor and virtual reality (VR) rendering. Laptops that include these GPUs and are sufficiently thin – as of late 2017, under 0.8 inches (20 mm) – have been designated as meeting Nvidia's "Max-Q" design standard.

In July 2016, Nvidia agreed to a settlement for a false advertising lawsuit regarding its GTX 970 model, as the models were unable to use all of their advertised 4 GB of VRAM due to limitations brought by the design of its hardware. In May 2017, Nvidia announced a partnership with Toyota which would use Nvidia's Drive PX-series artificial intelligence platform for its autonomous vehicles. In July 2017, Nvidia and Chinese search giant Baidu announced a far-reaching AI partnership that includes cloud computing, autonomous driving, consumer devices, and Baidu's open-source AI framework PaddlePaddle. Baidu unveiled that Nvidia's Drive PX 2 AI will be the foundation of its autonomous-vehicle platform.

Nvidia released the Titan V on December 7, 2017.

Nvidia released the Nvidia Quadro GV100 on March 27, 2018. Nvidia released the RTX 2080 GPUs on September 27, 2018. In 2018, Google announced that Nvidia's Tesla P4 graphic cards would be integrated into Google Cloud service's artificial intelligence.

In May 2018, on the Nvidia user forum, a thread was started asking the company to update users when it would release web drivers for its cards installed on legacy Mac Pro machines up to mid-2012 5,1 running the macOS Mojave operating system 10.14. Web drivers are required to enable graphics acceleration and multiple display monitor capabilities of the GPU. On its Mojave update info website, Apple stated that macOS Mojave would run on legacy machines with 'Metal compatible' graphics cards and listed Metal compatible GPUs, including some manufactured by Nvidia. However, this list did not include Metal compatible cards that currently work in macOS High Sierra using Nvidia-developed web drivers. In September, Nvidia responded, "Apple fully controls drivers for macOS. But if Apple allows, our engineers are ready and eager to help Apple deliver great drivers for macOS 10.14 (Mojave)." In October, Nvidia followed this up with another public announcement, "Apple fully controls drivers for macOS. Unfortunately, Nvidia currently cannot release a driver unless it is approved by Apple," suggesting a possible rift between the two companies. By January 2019, with still no sign of the enabling web drivers, Apple Insider weighed into the controversy with a claim that Apple management "doesn't want Nvidia support in macOS". The following month, Apple Insider followed this up with another claim that Nvidia support was abandoned because of "relational issues in the past", and that Apple was developing its own GPU technology. Without Apple-approved Nvidia web drivers, Apple users are faced with replacing their Nvidia cards with a competing supported brand, such as AMD Radeon from the list recommended by Apple.

### 2019 acquisition of Mellanox Technologies

On March 11, 2019, Nvidia announced a deal to buy Mellanox Technologies for $6.9 billion to substantially expand its footprint in the high-performance computing market. The acquisition of the Israeli firm, a longtime supplier to the Israeli military, led to the 2023 launch of "Israel-1," described as the country's most powerful AI supercomputer. In May 2019, Nvidia announced new RTX Studio laptops. The creators said that the new laptop was going to be seven times faster than a top-end MacBook Pro with a Core i9 and AMD's Radeon Pro Vega 20 graphics in apps like Maya and RedCine-X Pro. In August 2019, Nvidia announced *Minecraft RTX*, an official Nvidia-developed patch for the game *Minecraft* adding real-time DXR ray tracing exclusively to the Windows 10 version of the game. The whole game was, in Nvidia's words, "refit" with path tracing, which dramatically affects the way light, reflections, and shadows work inside the engine.

### 2020–2023

In May 2020, Nvidia announced it was acquiring Cumulus Networks. Post acquisition the company was absorbed into Nvidia's networking business unit, along with Mellanox.

In May 2020, Nvidia developed an open-source ventilator to address the shortage resulting from the global coronavirus pandemic. On May 14, 2020, Nvidia officially announced its Ampere GPU microarchitecture and the Nvidia A100 GPU accelerator. In July 2020, it was reported that Nvidia was in talks with SoftBank to buy Arm, a UK-based chip designer, for $32 billion.

On September 1, 2020, Nvidia officially announced the GeForce 30 series based on the company's new Ampere microarchitecture.

On September 13, 2020, Nvidia announced that it would buy Arm from SoftBank Group for $40 billion, subject to the usual scrutiny, with the latter retaining a 10% share of Nvidia.

In October 2020, Nvidia announced its plan to build the most powerful computer in Cambridge, England. The computer, called Cambridge-1, launched in July 2021 with a $100 million investment and will employ AI to support healthcare research. According to Jensen Huang, "The Cambridge-1 supercomputer will serve as a hub of innovation for the UK, and further the groundbreaking work being done by the nation's researchers in critical healthcare and drug discovery."

Also in October 2020, along with the release of the Nvidia RTX A6000, Nvidia announced it was retiring its workstation GPU brand Quadro, shifting its product name to Nvidia RTX for future products and the manufacturing to be Ampere architecture-based.

In August 2021, the proposed takeover of Arm was stalled after the UK's Competition and Markets Authority raised "significant competition concerns". In October 2021, the European Commission opened a competition investigation into the takeover. The Commission stated that Nvidia's acquisition could restrict competitors' access to Arm's products and provide Nvidia with too much internal information on its competitors due to their deals with Arm. SoftBank (the parent company of Arm) and Nvidia announced in early February 2022 that they "had agreed not to move forward with the transaction 'because of significant regulatory challenges'". The investigation was set to end on March 15, 2022. That same month, Nvidia was reportedly compromised by a cyberattack. This would have been the largest semiconductor acquisition in history.

In March 2022, Nvidia's CEO Jensen Huang mentioned that they were open to having Intel manufacture their chips in the future. This was the first time the company mentioned that it would work together with Intel's upcoming foundry services.

In April 2022, it was reported that Nvidia planned to open a new research center in Yerevan, Armenia.

In May 2022, Nvidia opened Voyager, the second of the two giant buildings at its new headquarters complex to the west of the old one. Unlike its smaller and older sibling Endeavor, the triangle theming is used more "sparingly" in Voyager.

In September 2022, Nvidia announced its next-generation automotive-grade chip, Drive Thor.

In September 2022, Nvidia announced a collaboration with the Broad Institute of MIT and Harvard related to the entire suite of Nvidia's AI-powered healthcare software suite called Clara, that includes Parabricks and MONAI.

Following United States Department of Commerce regulations which placed an embargo on exports to China of advanced microchips, which went into effect in October 2022, Nvidia saw its data center chip added to the export control list. The next month, the company unveiled a new advanced chip in China, called the A800 GPU, that met the export control rules.

In September 2023, Getty Images announced that it was partnering with Nvidia to launch Generative AI by Getty Images, a new tool that let people create images using Getty's library of licensed photos. Getty said they would use Nvidia's Edify model, which was available on Nvidia's generative AI model library Picasso.

On September 26, 2023, Denny's CEO Kelli Valade joined Huang in East San Jose to celebrate the founding of Nvidia at Denny's on Berryessa Road, where a plaque was installed to mark the relevant corner booth as the birthplace of a $1 trillion company. By then, Nvidia's H100 GPUs were in such demand that even other tech giants were beholden to how Nvidia allocated supply. Larry Ellison of Oracle Corporation said that month that during a dinner with Huang at Nobu in Palo Alto, he and Elon Musk of Tesla, Inc. and xAI "were begging" for H100s, "I guess is the best way to describe it. An hour of sushi and begging".

In October 2023, it was reported that Nvidia had quietly begun designing ARM-based central processing units (CPUs) for Microsoft's Windows operating system with a target to start selling them in 2025.

### 2024–2026

In January 2024, *Forbes* reported that Nvidia has increased its lobbying presence in Washington, D.C. as American lawmakers consider proposals to regulate artificial intelligence. From 2023 to 2024, the company reportedly hired at least four government affairs with professional backgrounds at agencies including the United States Department of State and the Department of the Treasury. It was noted that the $350,000 spent by the company on lobbying in 2023 was small compared to a number of major tech companies in the artificial intelligence space.

In January 2024, Raymond James Financial analysts estimated that Nvidia was selling the H100 GPU in the price range of $25,000 to $30,000 each, while on eBay, individual H100s cost over $40,000. Several major technology companies were purchasing tens or hundreds of thousands of GPUs for their data centers to run generative artificial intelligence projects; simple arithmetic implied that they were committing to billions of dollars in capital expenditures.

In February 2024, it was reported that Nvidia was the "hot employer" in Silicon Valley because it was offering interesting work and good pay at a time when other tech employers were downsizing. Half of Nvidia employees earned over $228,000 in 2023. By then, Nvidia GPUs had become so valuable that they needed special security while in transit to data centers. Cisco chief information officer Fletcher Previn explained at a CIO summit: "Those GPUs arrive by armored car".

On March 1, 2024, Nvidia became the third company in the history of the United States to close with a market capitalization in excess of $2 trillion. Nvidia needed only 180 days to get to $2 trillion from $1 trillion, while the first two companies, Apple and Microsoft, each took over 500 days. On March 18, Nvidia announced its new AI chip and microarchitecture Blackwell, named after mathematician David Blackwell.

In April 2024, Reuters reported that China had allegedly acquired banned Nvidia chips and servers from Supermicro and Dell via tenders.

In June 2024, the Federal Trade Commission (FTC) and the Justice Department (DOJ) began antitrust investigations into Nvidia, Microsoft and OpenAI, focusing on their influence in the AI industry. The FTC led the investigations into Microsoft and OpenAI, while the DOJ handled Nvidia. The probes centered on the companies' conduct rather than mergers. This development followed an open letter from OpenAI employees expressing concerns about the rapid AI advancements and lack of oversight.

The company became the world's most valuable, surpassing Microsoft and Apple, on June 18, 2024, after its market capitalization exceeded $3.3 trillion.

In June 2024, Trend Micro announced a partnership with Nvidia to develop AI-driven security tools, notably to protect the data centers where AI workloads are processed. This collaboration integrates Nvidia NIM and Nvidia Morpheus with Trend Vision One and its Sovereign and Private Cloud solutions to improve data privacy, real-time analysis, and rapid threat mitigation.

In October 2024, Nvidia introduced a family of open-source multimodal large language models called NVLM 1.0, which features a flagship version with 72 billion parameters, designed to improve text-only performance after multimodal training.

In October 2024, Nvidia reported that it had been collaborating with Raytheon (a RTX Corporation business) to “explore network pipelines that accelerate workloads on GPUs and use GPU acceleration software libraries”.

In November 2024, the company was added to the Dow Jones Industrial Average.

In November 2024, Morgan Stanley reported that "the entire 2025 production" of all of Nvidia's Blackwell chips was "already sold out".

Also in November 2024, the company bought 1.2 million shares of Nebius Group.

Nvidia was ranked #3 on Forbes' "Best Places to Work" list in 2024.

As of January 7, 2025, Nvidia's $3.66 trillion market cap was worth more than double of the combined value of AMD, ARM, Broadcom, and Intel.

In January 2025, Nvidia saw the largest one-day loss in market capitalization for a U.S. company in history at $600 billion. This was due to DeepSeek, a Chinese AI startup that developed an advanced AI model at a lower cost and computing power. DeepSeek's AI assistant, using the V3 model, surpassed ChatGPT as the highest-rated free app in the U.S. on Apple's App Store.

On April 7, 2025, Nvidia released the Llama-3.1-Nemotron-Ultra-253B-v1 reasoning large language model, under the Nvidia Open Model License. It comes in three sizes: Nano, Super and Ultra.

On May 28, 2025, Nvidia's second-quarter revenue forecast fell short of market estimates due to U.S. export restrictions impacting AI chip sales to China, yet the company's stock rose 5% as investors remained optimistic about long-term AI demand.

In July 2025, it was announced that Nvidia had acquired CentML, a Canadian-based AI firm.

On July 10, 2025, Nvidia closed for the first time with a market cap above $4 trillion, after its market cap briefly touched and then retreated from that number during the previous day. Nvidia became the first company to reach a market cap of $4 trillion. At that point, Nvidia was worth more than the combined value of all publicly traded companies in the United Kingdom.

On July 29, 2025, Nvidia ordered 300,000 H20 AI chips from Taiwan Semiconductor Manufacturing Company (TSMC) due to strong demand from Chinese tech firms like Tencent and Alibaba.

In August 2025, Nvidia and competitor Advanced Micro Devices agreed to pay 15% of the revenues from certain chip sales in China as part of an arrangement to obtain export licenses. Nvidia will pay only for sales of the H20 chips.

On September 17, 2025, Nvidia chief executive Jensen Huang said he was “disappointed” after the Cyberspace Administration of China (CAC) ordered companies including TikTok parent company ByteDance and Alibaba not to purchase the RTX Pro 6000D, a graphics chip made specifically for the Chinese market. China's internet regulator banned the country's largest technology companies from buying Nvidia's artificial intelligence chips as part of efforts to strengthen the domestic industry and compete with the United States. The CAC instructed companies this week to end both testing and orders of the RTX Pro 6000D, which Nvidia had designed as a tailor-made product for China, according to three people with knowledge of the matter.

On September 18, 2025, Nvidia announced it would invest $5 billion in Intel, backing the struggling U.S. chipmaker just weeks after the White House arranged a deal for the federal government to take a major stake in the company. The investment will give Nvidia an immediate holding of about 4% in Intel once new shares are issued to finalize the agreement. Nvidia's move provides Intel with fresh support following years of unsuccessful turnaround efforts and will allow Nvidia to offer its powerful GB300 data center servers based on Blackwell GPUs on Intel's X86 architecture.

On September 22, 2025, Nvidia and OpenAI announced a memorandum of understanding for a partnership wherein Nvidia would invest $100 billion into OpenAI, and OpenAI would use Nvidia chips and systems in new data centers. OpenAI will build new AI data centers using Nvidia systems, amounting to at least 10 gigawatts system power, which is the equivalent of energy produced by more than four Hoover Dams. The deal was meant to be a circular arrangement where OpenAI will pay back Nvidia's investment through the purchase of Nvidia's chips, which is a model common in AI partnerships. This "circularity" is estimated at $35 billion in new Nvidia chips bought by OpenAI, for every $10 billion Nvidia invests in OpenAI. As of January 2026, negotiations had not progressed beyond early stages, and the two companies were rethinking the partnership's structure. In the months leading up to this, chief executive Jensen Huang privately emphasized to industry associates that the original deal was non-binding and not finalized when announced.

In October 2025, a coalition of Nvidia, nonprofit Electric Power Research Institute and PJM Interconnection announced that the first commercial application of software-developed by startup Emerald AI (in which Nvidia invests), that adjusts the energy draw on a power grid in real time was to be deployed at a new data center under construction in Virginia. Dubbed "Aurora", the facility is expected to set a new flexible power standard.

A server farm dedicated to autonomous AI was also announced in October 2025, as a collaboration between SDS Schönfeld, a data services firm owned by UC Schönfeld, and VAST Data, an Israeli company specializing in AI storage management that collaborates closely with Nvidia. Reports indicate that approximately $30 billion has been secured for the Bet Yehoshua server farm. It is expected to feature "tens of petabytes of data infrastructure powered by VAST, along with thousands of Nvidia Blackwell GPUs and Nvidia network processors."

On October 29, 2025, Nvidia became the first company to reach a market capitalization of $5 trillion.

Nvidia's stock prices fell by 2% on November 11, 2025, as the SoftBank Group dumped its entire Nvidia portfolio worth $5.8 billion, redirecting the capital towards OpenAI instead.

On December 1, 2025, Nvidia released Alpamayo-R1, an open source, vision-language-action AI model for self-driving vehicles. This was done so that developers and researchers can understand how these models work and come up with standard ways on how the industry can evaluate how they work.

On December 15, 2025, Nvidia announced the Nemotron 3 family of models consisting of Nano, Super and Ultra models, built on a hybrid mixture-of-experts (MoE) architecture. Nvidia said Nano has around 30 billion parameters, Super 100 billion, and Ultra 500 billion.

On December 18, 2025, Nvidia announced plans to build a major new research and development campus in Kiryat Tivon, Israel, projected to employ more than 10,000 people and become one of the company's largest sites outside the United States. The 22-acre complex is scheduled to begin construction in 2027, with initial operations expected in 2031, and will include laboratories, green areas, and public facilities. The project reinforces Israel's role as Nvidia's principal international development hub in advanced AI and computing technologies.

In December 2025, it was announced that Nvidia had acquired SchedMD, the company behind the open-source workload manager Slurm, as part of an effort to expand its AI and high-performance computing software capabilities. Nvidia stated that Slurm would remain open-source and vendor-neutral after the acquisition, with no financial terms disclosed.

In December 2025, CNBC reported Nvidia had agreed to buy assets from Groq for $20 billion in cash. The deal included a non-exclusive licensing agreement with Nvidia for Groq's inference technology. Several of Groq's senior leaders, including its CEO, also agreed to join Nvidia as part of the deal. While both companies said Groq would continue to operate as an individual company, the transaction drew criticism from several industry analysts as a tactic to avoid regulatory scrutiny.

In late 2025, Nvidia entered advanced negotiations to acquire AI21 Labs, an Israeli developer of large language models, in a deal valued at as much as $2 billion to $3 billion. The proposed transaction is widely described as a talent-focused "acquihire" aimed at integrating AI21's workforce of approximately 200 specialists into Nvidia's global artificial intelligence operations. If completed, the transaction would be Nvidia's second-largest Israeli acquisition after its $7 billion purchase of Mellanox in 2020.

At CES 2026, CEO Jensen Huang unveiled Nvidia's Vera Rubin AI platform and the Alpamayo open-source model. Hesai was also picked as Nvidia's laser technology partner, supplying Lidar sensors to the company, streamlining software, hardware, and data in its autonomous driving products.

In January 2026, Nvidia launched a new weather forecasting service called Earth-2. It is an open-sourced platform that can be incorporated to improve the AI function across models used by scientists, businesses and local governments.

On February 24, 2026, Nvidia announced its acquisition of Israeli startup Illumex, a developer of generative semantic data infrastructure, in a deal reportedly valued at around $60 million.

On March 11, 2026, Nvidia announced that it will invest $2 billion in artificial intelligence cloud company Nebius.

In April 2026, Nvidia announced the release of a new group of open-source artificial intelligence models designed specifically for quantum computing. The development caused a noticeable market surge for allied quantum computing companies. During the same month, Nvidia's market momentum was further bolstered by its primary manufacturing partner, TSMC, which reported a 35.1% year-on-year revenue increase for the first quarter of 2026, largely driven by robust global demand for AI accelerators.

At the GTC conference in March 2026, Nvidia announced the "Vera Rubin" platform, the successor to its Blackwell architecture. The platform includes the Rubin GPU and Vera CPU, designed to scale "agentic AI" and offering significant performance improvements in large-scale AI factories.

In May 2026, Nvidia announced that it would be partnering with Corning and investing up to 3.2 billion to build 3 new advanced manufacturing facilities in North Carolina and Texas as part of a optical fiber deal.

On June 1, 2026, Nvidia released the RTX Spark chip intended for laptops.


## Corporate affairs

| Business unit | Sales (billion $) | Share |
|---|---|---|
| Compute & networking | 116.2 | 89.0% |
| Graphics | 14.3 | 11.0% |

| Region | Sales (billion $) | Share |
|---|---|---|
| United States | 61.3 | 46.9% |
| Singapore | 23.7 | 18.2% |
| Taiwan | 20.6 | 15.8% |
| China | 17.1 | 13.1% |
| Other countries | 7.9 | 6.0% |

### Leadership

Nvidia's key management as of March 2024 consists of:

- Jensen Huang, founder, president and chief executive officer
- Chris Malachowsky, founder and Nvidia fellow
- Colette Kress, executive vice president and chief financial officer
- Jay Puri, executive vice president of worldwide field operations
- Debora Shoquist, executive vice president of operations
- Tim Teter, executive vice president, general counsel and secretary

### Board of directors

As of January 2026, the company's board consisted of the following directors:

- Tench Coxe (former managing director of Sutter Hill Ventures)
- John Dabiri (engineer and professor at the California Institute of Technology)
- Jensen Huang (co-founder, CEO and president of Nvidia)
- Dawn Hudson (former chief marketing officer of the National Football League)
- Harvey C. Jones (managing partner of Square Wave Ventures)
- Melissa B. Lora (former president of Taco Bell International)
- Stephen Neal (lead independent director of Nvidia, former CEO and chairman emeritus and senior counsel of Cooley LLP)
- Brooke Seawell (venture partner at New Enterprise Associates)
- Aarti Shah (former senior vice president & chief information and digital officer at Eli Lilly and Company)
- Mark Stevens (managing partner at S-Cubed Capital)

### Finances

| Year | Revenue (bn. US$) | Net income (bn. US$) | Employees |
|---|---|---|---|
| 2016 | 5.0 | 0.61 | 9,227 |
| 2017 | 6.9 | 1.6 | 10,299 |
| 2018 | 9.7 | 3.0 | 11,528 |
| 2019 | 11.7 | 4.1 | 13,277 |
| 2020 | 10.9 | 2.7 | 13,775 |
| 2021 | 16.6 | 4.3 | 18,975 |
| 2022 | 26.9 | 9.7 | 22,473 |
| 2023 | 26.9 | 4.3 | 26,000 |
| 2024 | 60.9 | 29.7 | 29,600 |
| 2025 | 130 | 72.8 | 36,000 |
| 2026 | 215 | 120 | 42,000 |

For the fiscal year 2020, Nvidia reported earnings of US$2.796 billion, with an annual revenue of US$10.918 billion, a decline of 6.8% over the previous fiscal cycle. Nvidia's shares traded at over $531 per share, and its market capitalization was valued at over US$328.7 billion in January 2021.

For the Q2 of 2020, Nvidia reported sales of $3.87 billion, which was a 50% rise from the same period in 2019. The surge in sales was driven by people's higher demand for computer technology. According to the financial chief of the company, Colette Kress, the effects of the pandemic will "likely reflect this evolution in enterprise workforce trends with a greater focus on technologies, such as Nvidia laptops and virtual workstations, that enable remote work and virtual collaboration." In May 2023, Nvidia crossed $1 trillion in market valuation during trading hours, and grew to $1.2 trillion by the following November.

### Ownership

The 10 largest shareholders of Nvidia in early 2026 were:

- The Vanguard Group (9.33%)
- BlackRock (7.92%)
- State Street Global Advisors (4.03%)
- FMR LLC (3.71%)
- Jen-Hsun Huang (3.50%)
- Geode Capital Management (2.41%)
- T. Rowe Price (1.75%)
- Capital Research and Management Company (1.67%)
- JPMorgan Asset Management (1.39%)
- Norges Bank Investment Management (1.34%)

### Fabrication

Nvidia uses external suppliers for all phases of manufacturing, including wafer fabrication, assembly, testing, and packaging. Nvidia thus avoids most of the investment and production costs and risks associated with chip manufacturing, although it does sometimes directly procure some components and materials used in the production of its products (e.g., memory and substrates). Nvidia focuses its own resources on product design, quality assurance, marketing, and customer support.


## GPU Technology Conference

Nvidia's GPU Technology Conference (GTC) is a series of technical conferences held around the world. It originated in 2009 in San Jose, California, with an initial focus on the potential for solving computing challenges through GPUs. In recent years, the conference's focus has shifted to various applications of artificial intelligence and deep learning; including self-driving cars, healthcare, high-performance computing, and Nvidia Deep Learning Institute (DLI) training. GTC 2018 attracted over 8400 attendees. GTC 2020 was converted to a digital event and drew roughly 59,000 registrants. After several years of remote-only events, GTC in March 2024 returned to an in-person format in San Jose, California.

At GTC 2025, Nvidia unveiled its next-generation AI hardware, the Blackwell Ultra and Vera Rubin chips, signalling a leap toward agentic AI and reasoning-capable computing. Huang projected that AI-driven infrastructure would drive Nvidia's data center revenue to $1 trillion by 2028. The announcement also introduced Isaac GR00T N1 (humanoid robotics model), Cosmos (synthetic training data AI), and the Newton physics engine, developed in collaboration with DeepMind and Disney Research.


## Product families

Nvidia's product families include graphics processing units, wireless communication devices, and automotive hardware and software, such as:

- GeForce, consumer-oriented graphics processing products
- RTX, professional visual computing graphics processing products (replacing GTX and Quadro)
- NVS, a multi-display business graphics processor
- Tegra, a system on a chip series for mobile devices
- Tesla, line of dedicated general-purpose GPUs for high-end image generation applications in professional and scientific fields
- nForce, a motherboard chipset created by Nvidia for Intel (Celeron, Pentium and Core 2) and AMD (Athlon and Duron) microprocessors
- GRID, a set of hardware and services by Nvidia for graphics virtualization
- Shield, a range of gaming hardware including the Shield Portable, Shield Tablet and Shield TV
- Drive, a range of hardware and software products for designers and manufacturers of autonomous vehicles. The Drive PX-series is a high-performance computer platform aimed at autonomous driving through deep learning, while Driveworks is an operating system for driverless cars.
- BlueField, a range of data processing units, initially inherited from its acquisition of Mellanox Technologies
- Datacenter/server class CPU, codenamed Grace, released in 2023
- DGX, an enterprise platform designed for deep learning applications
- Maxine, a platform providing developers a suite of AI-based conferencing software
- Omniverse, a platform for creating and operating metaverse applications


## Open-source software support

Until September 23, 2013, Nvidia had not published any documentation for its advanced hardware, meaning that programmers could not write free and open-source device drivers for its products without resorting to reverse engineering. Additionally, features like its compute platform CUDA and the DLSS technology suite are proprietary and only available on its hardware. As such, Nvidia has been notable for proprietization and vendor-locking practices.

Nvidia has released Linux <open-source GPU kernel modules> under dual GPL/MIT licensing, allowing developers to inspect the driver module code and contribute improvements in collaboration with the community.[1] The Nvidia open-gpu-kernel-modules repository on GitHub provides the publicly accessible source code for these modules, supporting modern GPU architectures in Linux environments. Furthermore, Nvidia's acquisition of SchedMD and the release of new open-source AI models highlight its broader commitment to open-source software and the AI ecosystem.[2]

Instead, Nvidia provides its own binary GeForce graphics drivers for X.Org and an open-source library that interfaces with the Linux, FreeBSD or Solaris kernels and the proprietary graphics software. Nvidia also provided but stopped supporting an obfuscated open-source driver that only supports two-dimensional hardware acceleration and ships with the X.Org distribution.

The proprietary nature of Nvidia's drivers has generated dissatisfaction within free-software communities. In a 2012 talk, Linus Torvalds gave a middle-finger gesture and criticized Nvidia's stance toward Linux. Some Linux and BSD users insist on using only open-source drivers and regard Nvidia's insistence on providing nothing more than a binary-only driver as inadequate, given that competing manufacturers such as Intel offer support and documentation for open-source developers, and others like AMD release partial documentation and provide some active development.

Nvidia only provides x86/x64 and ARMv7-A versions of its proprietary driver; as a result, features like CUDA are unavailable on other platforms. Some users claim that Nvidia's Linux drivers impose artificial restrictions, like limiting the number of monitors that can be used at the same time, but the company has not commented on these accusations.

In 2014, with its Maxwell GPUs, Nvidia started to require firmware by it to unlock all features of its graphics cards.

On May 12, 2022, Nvidia announced that it is opensourcing its GPU kernel modules. Support for Nvidia's firmware was implemented in nouveau in 2023, which allows proper power management and GPU reclocking for Turing and newer graphics card generations.

On July 21, 2025, Nvidia announced to extend CUDA support to RISC-V.

As of 2026, NVIDIA has over a 100 different open-source projects available on GitHub in different areas such as computer vision, networking, cybersecurity, AR/VR, Robotics, Generative AI etc.

### Partial list of Nvidia open-source projects

- garak
- GR00T
- Nouveau
- NVDLA
- Nvidia Collective Communications Library
- PhysX (since 2018)
- TensorRT-LLM
- VDPAU
- Vibrante
- NemoClaw


## Nvidia proprietary software

- CUDA
- DLSS
- GameWorks
- Omniverse
- OptiX
- TensorRT
