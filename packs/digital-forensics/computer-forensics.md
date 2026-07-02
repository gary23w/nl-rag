---
title: "Computer forensics"
source: https://en.wikipedia.org/wiki/Computer_forensics
domain: digital-forensics
license: CC-BY-SA-4.0
tags: digital forensics, computer forensics, forensic data recovery, memory forensics, chain of custody
fetched: 2026-07-02
---

# Computer forensics

**Computer forensics** (also known as **computer forensic science**) is a branch of digital forensic science pertaining to evidence found in computers and digital storage media. The goal of computer forensics is to examine digital media in a forensically sound manner with the aim of identifying, preserving, recovering, analyzing, and presenting facts and opinions about the digital information.

Although it is most often associated with the investigation of a wide variety of computer crime, computer forensics may also be used in civil proceedings. The discipline involves similar techniques and principles to data recovery, but with additional guidelines and practices designed to create a legal audit trail.

Evidence from computer forensics investigations is usually subjected to the same guidelines and practices as other digital evidence. It has been used in a number of high-profile cases and is accepted as reliable within U.S. and European court systems.

## Overview

In the early 1980s, personal computers became more accessible to consumers, leading to their increased use in criminal activity (for example, to help commit fraud). At the same time, several new "computer crimes" were recognized (such as cracking). The discipline of computer forensics emerged during this time as a method to recover and investigate digital evidence for use in court. Since then, computer crime and computer-related crime has grown, with the FBI reporting a suspected 791,790 internet crimes in 2020, a 69% increase over the amount reported in 2019. Today, computer forensics is used to investigate a wide variety of crimes, including child pornography, fraud, espionage, cyberstalking, murder, and rape. The discipline also features in civil proceedings as a form of information gathering (e.g., Electronic discovery).

Forensic techniques and expert knowledge are used to explain the current state of a *digital artifact*, such as a computer system, storage medium (e.g., hard disk or CD-ROM), or an electronic document (e.g., an email message or JPEG image). The scope of a forensic analysis can vary from simple information retrieval to reconstructing a series of events. In a 2002 book, *Computer Forensics*, authors Kruse and Heiser define computer forensics as involving "the preservation, identification, extraction, documentation and interpretation of computer data". They describe the discipline as "more of an art than a science," indicating that forensic methodology is backed by flexibility and extensive domain knowledge. However, while several methods can be used to extract evidence from a given computer, the strategies used by law enforcement are fairly rigid and lack the flexibility found in the civilian world.

### Cybersecurity

Computer forensics is often confused with cybersecurity. Cybersecurity focuses on prevention and protection, while computer forensics is more reactionary and active, involving activities such as tracking and exposing. System security usually encompasses two teams: cybersecurity and computer forensics, which work together. A cybersecurity team creates systems and programs to protect data; if these fail, the computer forensics team recovers the data and investigates the intrusion and theft. Both areas require knowledge of computer science.

Computer forensics are used to convict those involved in physical and digital crimes. Some of these computer-related crimes include interruption, interception, copyright infringement, and fabrication. *Interruption* relates to the destruction and stealing of computer parts and digital files. *Interception* is the unauthorized access of files and information stored on technological devices. Copyright infringement refers to using, reproducing, and distributing copyrighted information, including software piracy. *Fabrication* involves accusing someone of using false data and information inserted into the system through an unauthorized source. Examples of interceptions include the Bank NSP case, Sony.Sambandh.com case, and business email compromise scams.

## Use as evidence

In court, computer forensic evidence is subject to the usual requirements for digital evidence. This requires that information be authentic, reliably obtained, and admissible. Different countries have specific guidelines and practices for evidence recovery. In the United Kingdom, examiners often follow Association of Chief Police Officers guidelines that help ensure the authenticity and integrity of evidence. While voluntary, the guidelines are widely accepted in British courts.

Computer forensics has been used as evidence in criminal law since the mid-1980s. Some notable examples include:

- BTK Killer: Dennis Rader was convicted of a string of serial killings over sixteen years. Towards the end of this period, Rader sent letters to the police on a floppy disk. Metadata within the documents implicated an author named "Dennis" at "Christ Lutheran Church," helping lead to Rader's arrest.
- Joseph Edward Duncan: A spreadsheet recovered from Duncan's computer contained evidence showing him planning his crimes. Prosecutors used this to demonstrate premeditation and secure the death penalty.
- Sharon Lopatka: Hundreds of emails on Lopatka's computer led investigators to her killer, Robert Glass.
- Corcoran Group: In this case, computer forensics confirmed parties' duties to preserve digital evidence when litigation had commenced or was reasonably anticipated. Hard drives were analyzed, though the expert found no evidence of deletion, and evidence showed that the defendants intentionally destroyed emails.
- Dr. Conrad Murray: Dr. Conrad Murray, the doctor of Michael Jackson, was convicted partially by digital evidence, including medical documentation showing lethal amounts of propofol.
- Mark Twitchell, also known as the "Dexter Killer," Twitchell was convicted with the help of a deleted document recovered from his laptop titled "SKConfessions." This file, which detailed his criminal activities, served as a key piece of evidence in the case.

## Forensic process

Computer forensic investigations typically follow the standard digital forensic process, consisting of four phases: acquisition, examination, analysis, and reporting. Investigations are usually performed on static data (i.e., acquired images) rather than "live" systems. This differs from early forensic practices, when a lack of specialized tools often required investigators to work on live data.

### Computer forensics lab

The computer forensics lab is a secure environment where electronic data can be preserved, managed, and accessed under controlled conditions, minimizing the risk of damage or alteration to the evidence. Forensic examiners are provided with the resources necessary to extract meaningful data from the devices they examine.

### Techniques

Various techniques are used in computer forensic investigations, including:

**Cross-drive analysis**

This technique correlates information found on multiple

hard drives

and can be used to identify

social networks

or detect anomalies.

**Live analysis**

The examination of computers from within the operating system using forensic or existing

sysadmin tools

to extract evidence. This technique is particularly useful for dealing with

encrypting file systems

where encryption keys can be retrieved, or for imaging the logical hard drive volume (a live acquisition) before shutting down the computer. Live analysis is also beneficial when examining networked systems or cloud-based devices that cannot be accessed physically.

**Deleted files**

A common forensic technique involves recovering deleted files. Most

operating systems

and

file systems

do not erase the physical file data, allowing investigators to reconstruct it from the physical

disk sectors

. Forensic software can "carve" files by searching for known file headers and reconstructing deleted data.

**Stochastic forensics**

This method leverages the stochastic properties of a system to investigate activities without traditional digital artifacts, often useful in cases of

data theft

.

**Steganography**

Steganography involves concealing data within another file, such as hiding illegal content within an image. Forensic investigators detect steganography by comparing file hashes, as any hidden data will alter the hash value of the file.

### Mobile device forensics

**Phone logs**

Phone companies typically retain logs of received calls, which can help create timelines and establish suspects' locations at the time of a crime.

**Contacts**

Contact lists

are useful in narrowing down suspects based on their connections to the victim.

**Text messages**

Text messages contain timestamps and remain in company servers, often indefinitely, even if deleted from the device. These records are valuable evidence for reconstructing communication between individuals.

**Photos**

Photos can provide critical evidence, supporting or disproving alibis by showing the location and time they were taken.

**Audio recordings**

Some victims may have recorded pivotal moments, capturing details like the attacker's voice, which could provide crucial evidence.

### Volatile data

Volatile data is stored in memory or in transit and is lost when the computer is powered down. It resides in locations such as registries, cache, and RAM. The investigation of volatile data is referred to as "live forensics."

When seizing evidence, if a machine is still active, volatile data stored solely in RAM may be lost if not recovered before shutting down the system. "Live analysis" can be used to recover RAM data (e.g., using Microsoft's COFEE tool, WinDD, WindowsSCOPE) before removing the machine. Tools like CaptureGUARD Gateway allow for the acquisition of physical memory from a locked computer.

RAM data can sometimes be recovered after power loss, as the electrical charge in memory cells dissipates slowly. Techniques like the cold boot attack exploit this property. Lower temperatures and higher voltages increase the chance of recovery, but it is often impractical to implement these techniques in field investigations.

Tools that extract volatile data often require the computer to be in a forensic lab to maintain the chain of evidence. In some cases, a live desktop can be transported using tools like a mouse jiggler to prevent sleep mode and an uninterruptible power supply (UPS) to maintain power.

Page files from file systems with journaling features, such as NTFS and ReiserFS, can also be reassembled to recover RAM data stored during system operation.

### Analysis tools

Numerous open-source and commercial tools exist for computer forensics. Common forensic analysis includes manual reviews of media, Windows registry analysis, password cracking, keyword searches, and the extraction of emails and images. Tools such as Autopsy (software), Belkasoft Evidence Center X, Forensic Toolkit (FTK), and EnCase are widely used in digital forensics.

## Professional education and careers

### Digital forensics analyst

A digital forensics analyst is responsible for preserving digital evidence, cataloging collected evidence, analyzing evidence relevant to the ongoing case, responding to cyber breaches (often in a corporate context), writing reports containing findings, and testifying in court. A digital forensic analyst may also be referred to as a computer forensic analyst, digital forensic examiner, cyber forensic analyst, forensic technician, or other similarly named titles, though these roles perform similar duties.

### Certifications

Several computer forensics certifications are available, such as the ISFCE Certified Computer Examiner, Digital Forensics Investigation Professional (DFIP), and IACRB Certified Computer Forensics Examiner. The top vendor-independent certification, particularly within the EU, is the Certified Cyber Forensics Professional (CCFP).

Many commercial forensic software companies also offer proprietary certifications.
