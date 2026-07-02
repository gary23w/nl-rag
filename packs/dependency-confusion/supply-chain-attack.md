---
title: "Supply chain attack"
source: https://en.wikipedia.org/wiki/Supply_chain_attack
domain: dependency-confusion
license: CC-BY-SA-4.0
tags: dependency confusion attack, package namespace hijack, internal registry precedence, supply chain package pinning
fetched: 2026-07-02
---

# Supply chain attack

A **supply chain attack** is a cyber-attack that seeks to damage an organization by targeting less secure elements in the supply chain. A supply chain attack can occur in any industry, from the financial sector, oil industry, to a government sector. A supply chain attack can happen in software or hardware. Cybercriminals typically tamper with the manufacturing or distribution of a product by installing malware or hardware-based spying components. Symantec's 2019 Internet Security Threat Report states that supply chain attacks increased by 78 percent in 2018.

A supply chain is a system of activities involved in handling, distributing, manufacturing, and processing goods in order to move resources from a vendor into the hands of the final consumer. A supply chain is a complex network of interconnected players governed by supply and demand.

Although supply chain attack is a broad term without a universally agreed upon definition, in reference to cyber-security, a supply chain attack can involve physically tampering with electronics (computers, ATMs, power systems, factory data networks) in order to install undetectable malware for the purpose of bringing harm to a player further down the supply chain network. Alternatively, the term can be used to describe attacks exploiting the software supply chain, in which an apparently low-level or unimportant software component used by other software can be used to inject malicious code into the larger software that depends on the component.

In a more general sense, a supply chain attack may not necessarily involve electronics. In 2010 when burglars gained access to the pharmaceutical giant Eli Lilly's supply warehouse, by drilling a hole in the roof and loading $80 million worth of prescription drugs into a truck, they could also have been said to carry out a supply chain attack. However, this article will discuss cyber attacks on physical supply networks that rely on technology; hence, a supply chain attack is a method used by cyber-criminals.

## Attack framework

Generally, supply chain attacks on information systems begin with an advanced persistent threat (APT) that determines a member of the supply network with the weakest cyber security in order to affect the target organization. Hackers don't usually directly target a larger entity, such as the United States Government, but instead target the entity's software. The third-party software is often less protected, leading to an easier target. According to an investigation produced by Verizon Enterprise, 92% of the cyber security incidents analyzed in their survey occurred among small firms. Supply chain networks are considered to be particularly vulnerable due to their multiple interconnected components.

APTs can often gain access to sensitive information by physically tampering with the production of the product. In October 2008, European law-enforcement officials "uncovered a highly sophisticated credit-card fraud ring" that stole customer's account details by using untraceable devices inserted into credit-card readers made in China to gain access to account information and make repeated bank withdrawals and Internet purchases, amounting to an estimated $100 million in losses.

## Risks

The threat of a supply chain attack poses a significant risk to modern day organizations and attacks are not solely limited to the information technology sector; supply chain attacks affect the oil industry, large retailers, the pharmaceutical sector and virtually any industry with a complex supply network.

The Information Security Forum explains that the risk derived from supply chain attacks is due to information sharing with suppliers, it states that "sharing information with suppliers is essential for the supply chain to function, yet it also creates risk... information compromised in the supply chain can be just as damaging as that compromised from within the organization".

While Muhammad Ali Nasir of the National University of Computer and Emerging Sciences, associates the above-mentioned risk with the wider trend of globalization stating "…due to globalization, decentralization, and outsourcing of supply chains, numbers of exposure points have also increased because of the greater number of entities involved and that too are scattered all around the globe… [a] cyber-attack on [a] supply chain is the most destructive way to damage many linked entities at once due to its ripple effect."

Poorly managed supply chain management systems can become significant hazards for cyber attacks, which can lead to a loss of sensitive customer information, disruption of the manufacturing process, and could damage a company's reputation.

## Examples

### Compiler attacks

Wired reported a connecting thread in recent software supply chain attacks, as of 3 May 2019. These have been surmised to have spread from infected, pirated, popular compilers posted on pirate websites. That is, corrupted versions of Apple's Xcode and Microsoft Visual Studio. (In theory, alternating compilers might detect compiler attacks, when the compiler is the trusted root.)

### Target

At the end of 2013, Target, a US retailer, was hit by one of the largest data breaches in the history of the retail industry.

Between 27 November and 15 December 2013, Target's American brick-and-mortar stores experienced a data hack. Around 40 million customers' credit and debit cards became susceptible to fraud after malware was introduced into the POS system in over 1,800 stores. The data breach of Target's customer information saw a direct impact on the company's profit, which fell 46 percent in the fourth quarter of 2013.

Six months prior the company began installing a $1.6 million cyber security system. Target had a team of security specialists to monitor its computers constantly. Nonetheless, the supply chain attack circumvented these security measures.

It is believed that cyber criminals infiltrated a third party supplier to gain access to Target's main data network. Although not officially confirmed, investigation officials suspect that the hackers first broke into Target's network on 15 November 2013 using passcode credentials stolen from Fazio Mechanical Services, a Pennsylvania-based provider of HVAC systems.

Ninety lawsuits have been filed against Target by customers for carelessness and compensatory damages. Target spent around $61 million responding to the breach, according to its fourth-quarter report to investors.

### Stuxnet

Stuxnet is a computer worm that is widely believed to be a joint U.S.-Israeli cyber operation, though neither government has officially confirmed involvement. The worm specifically targets industrial control systems, particularly those that automate electromechanical processes, such as factory machinery and nuclear enrichment equipment. Stuxnet was designed to manipulate programmable logic controllers (PLCs), disrupting industrial equipment by issuing unauthorized commands while simultaneously feeding falsified operations data to monitoring systems to conceal its activity.

Stuxnet is widely believed to have been developed to disrupt Iran's enriched uranium programs. Kevin Hogan, Senior Director of Security Response at Symantec, stated that most infections occurred in Iran. Analysts suggest that its primary target was the Natanz uranium enrichment facility.

Stuxnet was initially introduced into Iran's Natanz facility via infected USB flash drives, requiring physical access to the target network. According to reports, engineers or maintenance workers, either knowingly or unknowingly, facilitated its entry into the plant. Once inside, the worm spread autonomously, exploiting multiple zero-day vulnerabilities in Windows systems to propagate across networked machines running Siemens industrial control software.

### ATM malware

In recent years malware known as Suceful, Plotus, Tyupkin and GreenDispenser have affected automated teller machines globally, especially in Russia and Ukraine. GreenDispenser specifically gives attackers the ability to walk up to an infected ATM system and remove its cash vault. When installed, GreenDispenser may display an 'out of service' message on the ATM, but attackers with the right access credentials can drain the ATM's cash vault and remove the malware from the system using an untraceable delete process.

The other types of malware usually behave in a similar fashion, capturing magnetic stripe data from the machine's memory storage and instructing the machines to withdraw cash. The attacks require a person with insider access, such as an ATM technician or anyone else with a key to the machine, to place the malware on the ATM.

The Tyupkin malware active in March 2014 on more than 50 ATMs at banking institutions in Eastern Europe, is believed to have also spread at the time to the U.S., India, and China. The malware affects ATMs from major manufacturers running Microsoft Windows 32-bit operating systems. The malware displays information on how much money is available in every machine and allows an attacker to withdraw 40 notes from the selected cassette of each ATM.

### NotPetya / M.E.Doc

In June 2017, the financial software M.E.Doc, widely used in Ukraine, was identified by security researchers as a likely initial vector for the spread of the NotPetya malware. Security researchers, including those from Microsoft, indicated that NotPetya infections may have originated from a compromised update issued through M.E.Doc. Some analysts described this as a supply chain attack, though the exact method of compromise was not definitively identified. The software's developers denied the claim but later deleted their statement and stated that they were cooperating with investigators.

NotPetya was initially identified as ransomware because it encrypted hard drives and displayed a ransom demand in bitcoin. However, the email account used to provide decryption keys was shut down, leaving victims without a way to recover their files. Unlike WannaCry, NotPetya had no built-in kill switch, making it harder to stop. The attack affected multiple industries in Ukraine, including banks, an airport, the Kyiv Metro, pharmaceutical companies, and Chernobyl's radiation detection systems. It also spread globally, impacting organizations in Russia, the United Kingdom, India, and the United States.

NotPetya spread using EternalBlue, a vulnerability originally developed by the U.S. National Security Agency (NSA) and later leaked. EternalBlue had previously been used in the WannaCry cyberattack in May 2017. This exploit enabled NotPetya to spread through the Windows Server Message Block (SMB) protocol. The malware also used PsExec and the Windows Management Instrumentation (WMI) to spread within networks. Due to these exploits, once a device on a network was infected, the malware could rapidly spread to other connected systems.

Ukrainian police stated that M.E.Doc employees could face criminal liability for negligence, citing repeated warnings from antivirus firms about security vulnerabilities in the company's cybersecurity infrastructure. The head of Ukraine's CyberPolice, Colonel Serhiy Demydiuk, alleged that M.E.Doc had been repeatedly warned by security firms about weaknesses in its systems but failed to act, stating, "They knew about it." Authorities later reported that M.E.Doc cooperated with investigators.

### British Airways

From August 21 until September 5, 2018 British Airways was under attack. The British Airways website payment section contained a code that harvested customer payment data. The injected code was written specifically to route credit card information to a domain baways.com, which could erroneously be thought to belong to British Airways.

Magecart is the entity believed to be behind the attack. Magecart is a name attributed to multiple hacker groups that use skimming practices in order to steal customer information through online payment processes. Approximately 380,000 customers had their personal and financial data compromised as a result of the attack. British Airways later reported in October, 2018 that an additional 185,000 customers may have had their personal information stolen as well.

### SolarWinds

The 2020 SolarWinds cyberattack was linked to a supply chain compromise targeting the IT infrastructure company SolarWinds, which provided software used by multiple U.S. federal institutions, including networks within the National Nuclear Security Administration (NNSA). Russian hackers compromised Orion, a widely used network management software developed by SolarWinds, by injecting malicious code into software updates. This allowed them to gain unauthorized access to numerous organizations, including multiple U.S. government agencies that relied on Orion for IT monitoring and management.

On December 13, 2020, the U.S. Department of Homeland Security issued Emergency Directive 21-01, "*Mitigate SolarWinds Orion Code Compromise",* requiring affected federal agencies to disconnect compromised Windows host OS instances from their enterprise domain and rebuild those hosts using trusted sources. These compromised systems had been running SolarWinds Orion.

In December 2020, FireEye identified a cyber breach involving the SolarWinds Orion software, which had been compromised prior to its discovery. Microsoft was among the organizations affected, detecting and removing malicious files linked to the breach. Microsoft has since collaborated with FireEye as part of an ongoing investigation into the incident. The cyberattack targeted supply chain software used across various industries, including government, consulting, technology, telecommunications, and extractive sectors in North America, Europe, Asia and the Middle East.

On January 5, 2021, a joint statement from the Federal Bureau of Investigation (FBI), the Cybersecurity and Infrastructure Security Agency (CISA), the Office of the Director of National Intelligence (ODNI), and the National Security Agency (NSA) indicated that, while approximately 18,000 public and private sector entities were affected by the SolarWinds breach, fewer than ten U.S. government agencies were confirmed to have been compromised.

### Microsoft Exchange Server

In February 2021 Microsoft determined that the attackers had downloaded a few files "(subsets of service, security, identity)" apiece from

- "a small subset of Azure components"
- "a small subset of Intune components"
- "a small subset of Exchange components"

None of the Microsoft repositories contained production credentials. The repositories were secured in December, and those attacks ceased in January. However, in March 2021 more than 20,000 US organizations were compromised through a back door that was installed via flaws in Exchange Server. The affected organizations use self-hosted e-mail (on-site rather than cloud-based) such as credit unions, town governments, and small businesses. The flaws were patched on 2 March 2021, but by 5 March 2021 only 10% of the compromised organizations had implemented the patch; the back door remains open. The US officials are attempting to notify the affected organizations which are smaller than the organizations that were affected in December 2020.

Microsoft has updated its Indicators of Compromise tool and has released emergency mitigation measures for its Exchange Server flaws. The attacks on SolarWinds and Microsoft software are currently thought to be independent, as of March 2021. The Indicators of Compromise tool allows customers to scan their Exchange Server log files for compromise. At least 10 attacking groups are using the Exchange Server flaws. Web shells can remain on a patched server; this still allows cyberattacks based on the affected servers. As of 12 March 2021 exploit attempts are doubling every few hours, according to Check Point Research, some in the name of security researchers themselves.

By 14 April 2021 the FBI had completed a covert cyber operation to remove the web shells from afflicted servers and was informing the servers' owners of what had been done.

In May 2021 Microsoft identified 3000 malicious emails to 150 organizations in 24 countries, that were launched by a group that Microsoft has denoted 'Nobelium'. Many of those emails were blocked before delivery. 'Nobelium' gained access to a Constant Contact "email marketing account used by the US Agency for International Development (USAID)". Security researchers assert that 'Nobelium' crafts spear-phishing email messages which get clicked on by unsuspecting users; the links then direct installation of malicious 'Nobelium' code to infect the users' systems, making them subject to ransom, espionage, disinformation, etc. The US government has identified 'Nobelium' as stemming from Russia's Federal Security Service. By July 2021 the US government is expected to name the initiator of the Exchange Server attacks: "China's Ministry of State Security has been using criminal contract hackers".

In September 2021 the Securities and Exchange Commission (SEC) enforcement staff have requested that any companies which have downloaded any compromised SolarWinds updates, voluntarily turn over data to the SEC if they have installed the compromised updates on their servers.

In July 2022 SessionManager, a malicious module hosted by IIS (installed by default on Exchange Servers), was discovered to have infected Exchange Servers since March 2021; SessionManager searches memory for passwords, and downloads new modules, to hijack the server.

### Golden SAML

Mandiant, a security firm, has shown that nation-state-sponsored groups, once they have gained access to corporate clouds, can now exploit Security assertion markup language (SAML), to gain federated authentication to Active Directory and similar services, at will. Once the attackers gain access, they are able to infiltrate any information or assets belonging to the organization. This is because this technique allows attackers to pose as any member of the targeted organization. These attacks are progressively becoming more desirable to malicious actors as companies and agencies continue to move assets to cloud services.

In 2020, SolarWinds was subject to what is described as the first documented Golden SAML attack, often referred to as "Solorigate". A malicious actor infected the source code of a software update with a backdoor code made to look legitimate. Customers began installing the faulty update to their systems, ultimately affecting over 18,000 individuals globally. The attack affected a number of United States government agencies and private sector agencies as well.

### Colonial Pipeline

In May 2021, a ransomware attack on Colonial Pipeline forced a temporary shutdown of a major fuel distribution network, disrupting the supply of gasoline, diesel, and jet fuel to the U.S. East Coast. The Biden administration invoked emergency powers to prevent shortages, while experts described the incident as the worst-ever cyberattack on U.S. infrastructure. The attack, attributed to the Russian-linked cybercriminal group DarkSide, raised concerns about vulnerabilities in critical energy systems, as fuel traders sought alternative supply routes and fears of price spikes emerged.

On June 16, 2021, President Biden stated to President Putin that cyberattacks on 16 critical infrastructure sectors were off-limits and said that the U.S. would respond to future cyber threats. The 16 critical infrastructure sectors, as designated by the U.S. Cybersecurity and Infrastructure Security Agency (CISA), include energy, food and agriculture, emergency services, healthcare, and other essential industries such as financial services, communications, and transportation systems.

### Kaseya VSA ransomware attack

On 2 July 2021, about 60 managed service providers (MSPs) and their customers became victims of a ransomware attack perpetrated by the REvil group, causing downtime for over 1,000 companies. REvil carried out the attack by exploiting a vulnerability in VSA (Virtual System Administrator), a remote monitoring and management software package developed by Kaseya. This was a form of supply chain attack on a software supply chain. REvil demanded about 70 million USD in Bitcoin as a ransom. On 23 July 2021, Kaseya announced that it had received a universal decryptor tool from a "trusted third party", and it helped customers restore their data. Kaseya said it did not pay the ransom. Two suspects were identified and one sentenced.

### 3CX attack

In March 2023, the voice and video chat app 3CX Phone System was thought to have been subject to a supply chain attack due to detection of malicious activity on the software. The app is used in a wide variety of industries from food to automotive and an attack has the potential to impact hundreds of thousands of users worldwide. The malware infects the host device through the installation process, acting as a Trojan horse virus spread through both Mac OS and Microsoft installers. They employed an infostealer through a malicious payload that connected to a C2 server controlled by the threat actor.

The attack utilized the Gopuram backdoor, originally discovered by the Russian cybersecurity company Kaspersky in 2020. The use of this backdoor suggested that the attack was executed by the North Korean cybercrime group known as Lazarus due to their use of this same backdoor in a 2020 attack against a South Asian cryptocurrency company. The Gopuram backdoor has been utilized in other past attacks against cryptocurrency agencies, which Lazarus has been known to target.

### United States Department of State attack

In July 2023, Chinese state-sponsored hackers targeted the United States Department of State, hacking several government employees' Microsoft email accounts, which gave them access to classified information. They stole information from about 60,000 emails from several Department of State employees. Department of State officials have stated that the information stolen includes "victims' travel itineraries and diplomatic deliberations". If used in a malicious manner, this information could be used to monitor important government officials and track United States communications that are meant to be confidential. The Department of State hack occurred due to vulnerabilities in Microsoft Exchange Server, classifying it as a supply-chain attack.

### XZ Utils backdoor

In March 2024, a backdoor in xz/liblzma in XZ Utils was suspected, with malicious code known to be in version 5.6.0 and 5.6.1. While the exploit remained dormant unless a specific third-party patch of the SSH server is used, under the right circumstances this interference could potentially enable a malicious actor to break sshd authentication and gain unauthorized access to the entire system remotely.

The list of affected Linux distributions includes Debian unstable, Fedora Rawhide, Kali Linux, and OpenSUSE Tumbleweed. Most Linux distributions that followed a stable release update model were not affected, since they were carrying older versions of xz. Arch Linux issued an advisory for users to update immediately, although it also noted that Arch's OpenSSH package does not include the common third-party patch necessary for the backdoor. FreeBSD is not affected by this attack, as all supported FreeBSD releases include versions of xz that predate the affected releases and the attack targets Linux's glibc.

### Ethereum Smart Contract and NPM Library typosquat attack

On October 31, 2024, cybersecurity researchers from several security firms such as Phylum, Socket, and Checkmarx detected an attack on users of the open-source Node Package Manager (NPM) library. Unidentified attackers published more than 287 packages in an attempt to trick users of the platform into downloading malicious code. The attack used a technique called typosquatting, which copies the names of legitimate packages closely, tricking unsuspecting developers into accidentally downloading the wrong one. For the package Fetch-mock-jest, the attacker rearranged the order of the words and misspelled the word fetch creating the name "jest-fet-mock". Based on the kind of packages mimicked, researchers believe this attack widely targeted software developers using NPM. Packages targeted are mostly mock HTTP requests and cryptocurrency-related, including Puppeteer, Bignum.js, and Fetch-mock-jest, which are mainly used in development environments.

Phylum researchers noted that these typosquatted packages seemed normal at first glance, but upon closer inspection, they contained obfuscated code that could not be understood. After de-obfuscating the code, researchers found that after the malicious package is mistakenly downloaded it automatically runs a script that interacts with an Ethereum smart contract to retrieve the IP addresses of the command and control server (C2) used by the attackers. The script then identifies the operating system used by the victim machine and downloads compatible malware from the IP address it received from the contract. This malware maintains persistent communication with the attacker's C2 server, periodically leaking the user's system information such as the operating system version, GPU, CPU, the amount of memory on the machine, and username.

Checkmarkx researcher Yahud Gelb explains that if researchers attempt to take down a C2 server at a specific IP address, the attacker can just update the Ethereum contract so that it returns a different address. When describing the mechanism behind the contract he wrote: "Think of a smart contract on the Ethereum blockchain as a public bulletin board – anyone can read what's posted, but only the owner has the ability to update it". This complicates the issue because the malware can always query the smart contract to update the stored address of the C2 server in case the current one has been taken down by authorities.

Researchers worried that several companies' software development supply chains can be put at risk when attackers typosquat them. They elaborate that the untraceable nature of the attack combined with its precisely engineered methods of persistence only adds to the looming threat. Furthermore, company employees usually have elevated system privileges and access to CI/CD pipelines when using development environments, further endangering the company's and their customer's data. They warned that developers who use npm packages like the ones above at any stage of the software development lifecycle must take caution and implement robust dependency scanning before performing any installations.

There is little to no information on the attackers' identity or their motive. However, researchers did find error messages written in Russian within the de-obfuscated code of the malicious packages, but they speculate that this could be a misdirect set up by the real culprits trying to throw off any suspicions. Phylum, Checkmarx, and Socket researchers brought to attention the ever-evolving nature of supply chain attacks, and how threat actors have had to continuously come up with creative ways to subvert detection of the servers under their control, highlighting the importance of double-checking any dependencies downloaded during the development phase of a project.

### Notepad++ compromise

In 2025, the popular text editor Notepad++ was subjected to a sophisticated supply chain attack when threat actors compromised the application's update infrastructure at the hosting provider level. The attack, which began in June 2025 and continued through December 2025, involved the interception and redirection of update traffic from the official notepad-plus-plus.org domain to attacker-controlled servers. According to the Notepad++ maintainer, the shared hosting server was fully compromised until September 2, 2025, after which attackers maintained access to internal service credentials until December 2, 2025, allowing them to continue redirecting update traffic. Multiple independent security researchers assessed the threat actor to be a Chinese state-sponsored group, with the campaign demonstrating highly selective targeting primarily against organizations in the telecommunications and financial sectors across East Asia, as well as government entities in the Philippines and Vietnam. Kaspersky researchers identified three primary execution chains used between July and October 2025, with attackers constantly changing command-and-control server addresses, downloaders, and final payloads to evade detection. Security firm Rapid7 attributed the campaign to the Lotus Blossom group (also known as Violet Typhoon or APT31), linking the attacks to infrastructure and tactics previously observed in campaigns targeting cryptocurrency companies and critical infrastructure.

### eScan updates compromise

On January 20, 2026, the eScan antivirus software, developed by Indian cybersecurity firm MicroWorld Technologies, was compromised in a supply chain attack when threat actors breached one of the company's regional update servers and deployed malware to customer systems. The incident lasted approximately one hour before being detected by security researchers at Morphisec and Kaspersky. The attack primarily affected users in South Asia, including India, Bangladesh, Sri Lanka, and the Philippines. Attackers replaced the legitimate Reload.exe component of eScan with a malicious executable that disabled future antivirus updates and downloaded additional payloads from command-and-control servers. This marked the second breach of eScan's infrastructure, following a 2024 incident where North Korean state-sponsored group Kimsuky exploited the same update mechanism to deploy backdoors and cryptocurrency miners. No attribution has been made for the 2026 attack.

## Prevention

On 12 May 2021, Executive Order 14028 (the EO), *Improving the nation's cybersecurity*, tasked NIST as well as other US government agencies with enhancing the cybersecurity of the United States. On 11 July 2021 (day 60 of the EO timeline) NIST, in consultation with the Cybersecurity and Infrastructure Security Agency (CISA) and the Office of Management and Budget (OMB), delivered '4i': guidance for users of critical software, as well as '4r': for minimum vendor testing of the security and integrity of the software supply chain.

- Day 30: solicit input
- Day 45: define 'critical software'
- Day 60: EO task 4i, 4r: user guidance, and vendor testing
- Day 180: EO task 4c: guidelines for enhancing supply chain software security
- Day 270: EO task 4e, 4s, 4t, 4u: guidelines for enhancing supply chain software
- Day 360: EO task 4d: guidelines for review and update procedures of supply chain software
- Day 365: EO task 4w: summary support of the pilot

### Government

The Comprehensive National Cybersecurity Initiative and the Cyberspace Policy Review passed by the Bush and Obama administrations respectively, direct U.S. federal funding for development of multi-pronged approaches for global supply chain risk management. According to Adrian Davis of the Technology Innovation Management Review, securing organizations from supply chain attacks begins with building cyber-resilient systems. Supply chain resilience is, according to supply chain risk management expert Donal Walters, "the ability of the supply chain to cope with unexpected disturbances" and one of its characteristics is a company-wide recognition of where the supply chain is most susceptible to infiltration. Supply chain management plays a crucial role in creating effective supply chain resilience.

In March 2015, under the Conservative and Liberal democratic government coalition, the UK Department for Business outlined new efforts to protect SMEs from cyber attacks, which included measures to improve supply chain resilience.

The UK government has produced the Cyber Essentials Scheme, which trains firms for good practices to protect their supply chain and overall cyber security.

### Financial institutions

The Depository Trust and Clearing Group, an American post-trade company, in its operations has implemented governance for vulnerability management throughout its supply chain and looks at IT security along the entire development lifecycle; this includes where software was coded and hardware manufactured.

In a 2014 PwC report, titled "Threat Smart: Building a Cyber Resilient Financial Institution", the financial services firm recommends the following approach to mitigating a cyber attack:

> "To avoid potential damage to a financial institution's bottom line, reputation, brand, and intellectual property, the executive team needs to take ownership of cyber risk. Specifically, they should collaborate up front to understand how the institution will defend against and respond to cyber risks, and what it will take to make their organization cyber resilient.

### Cyber security firms

FireEye, a US network security company that provides automated threat forensics and dynamic malware protection against advanced cyber threats, such as advanced persistent threats and spear phishing, recommends firms to have certain principles in place to create resilience in their supply chain, which includes having:

- **A small supplier base:** This allows a firm to have tighter control over its suppliers.
- **Stringent vendor controls:** Imposing stringent controls on suppliers in order to abide by lists of an approved protocols. Also conducting occasional site audits at supplier locations and having personnel visiting the sites on a regular basis for business purposes allows greater control.
- **Security built into design:** Security features, such as check digits, should be designed into the software to detect any previous unauthorized access to the code. An iterative testing process to get the code functionally hardened and security-hardened is a good approach.

On 27 April 2015, Sergey Lozhkin, a Senior Security Researcher with GReAT at Kaspersky Lab, spoke about the importance of managing risk from targeted attacks and cyber-espionage campaigns, during a conference on cyber security he stated:

> "Mitigation strategies for advanced threats should include security policies and education, network security, comprehensive system administration and specialized security solutions, like... software patching features, application control, whitelisting and a default deny mode."

In 2025, a study by the Austrian Chamber of Commerce (WKO) and AV-Comparatives identified what cybersecurity firms should do to assure their customers about supply chain security. This includes disclosing a software bill of materials, maintaining transparent data storage practices, providing detailed incident reports, and offering facilities where customers can inspect source codes and updates for the cybersecurity product. Only 3 of the 14 vendors examined provided such assurances.

## Regulatory response

Supply chain attacks have prompted regulatory bodies to address third-party risk management requirements. The Health Insurance Portability and Accountability Act (HIPAA) Security Rule requires covered entities to obtain satisfactory assurances from business associates that they will appropriately safeguard electronic protected health information, typically through business associate agreements (45 CFR 164.308(b)(1)-(b)(4)). The December 2024 HIPAA Security Rule NPRM proposed requiring regulated entities to verify at least once every twelve months that their business associates have deployed technical safeguards consistent with the Security Rule, including verification of patch management and vulnerability remediation practices.

The Cybersecurity and Infrastructure Security Agency (CISA) issued Binding Operational Directive 22-01, requiring federal agencies to remediate known exploited vulnerabilities within specified timeframes. NIST Special Publication 800-161 *Cybersecurity Supply Chain Risk Management Practices* provides a framework for organizations to identify, assess, and mitigate supply chain risks throughout the system development life cycle.
