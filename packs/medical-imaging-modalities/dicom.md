---
title: "DICOM"
source: https://en.wikipedia.org/wiki/DICOM
domain: medical-imaging-modalities
license: CC-BY-SA-4.0
tags: medical imaging, diagnostic radiology, image reconstruction, digital imaging communications
fetched: 2026-07-02
---

# DICOM

**Digital Imaging and Communications in Medicine** (**DICOM**) is a technical standard for the digital storage and transmission of medical images and related information. It includes information object definitions (i.e. message formats); service definitions; a file format definition, which specifies the structure of a **DICOM file**; and a network communication protocol that uses either TCP/IP or HTTPS to communicate between systems. The primary purpose of the standard is to facilitate communication between the software and hardware entities involved in medical imaging, especially those that are created by different manufacturers. Entities that utilize DICOM files include components of picture archiving and communication systems (PACS), such as imaging machines (modalities), radiological information systems (RIS), scanners, printers, computing servers, and networking hardware.

The DICOM standard has been widely adopted by hospitals, large clinics, and the medical software industry. It is sometimes used in smaller-scale applications, such as dentists' and doctors' offices. DICOM is also used in veterinary medicine and in research.

The National Electrical Manufacturers Association (NEMA) holds the copyright to the published standard, which was developed by the DICOM Standards Committee (which includes some NEMA members). It is also known as NEMA standard PS3 and as ISO standard 12052:2017: *"Health informatics – Digital imaging and communication in medicine (DICOM) including workflow and data management"*.

## Applications

DICOM is used worldwide to store, exchange, and transmit medical images. DICOM has been central to the development of modern radiological imaging; DICOM incorporates standards for imaging modalities such as radiography, ultrasonography, computed tomography (CT), magnetic resonance imaging (MRI), and radiation therapy. DICOM includes protocols for image exchange (e.g., via portable media such as DVDs), image compression, 3-D visualization, image presentation, and results reporting.

## History

DICOM is a standard developed by the American College of Radiology (ACR) and the National Electrical Manufacturers Association (NEMA).

In the beginning of the 1980s, it was difficult for anyone other than manufacturers of computed tomography or magnetic resonance imaging devices to decode the images that the machines generated. Radiologists and medical physicists sought the images for dose-planning in radiation therapy. ACR and NEMA collaborated and formed a standard committee in 1983. Their first standard, ACR/NEMA 300, entitled "Digital Imaging and Communications", was released in 1985. Very soon after its release, it became clear that improvements were needed. The text was vague and had internal contradictions.

In 1988 the second version was released. This version gained more acceptance among vendors. The image transmission was specified as over a dedicated 2 pair cable (EIA-485). The first demonstration of ACR/NEMA V2.0 interconnectivity technology was held at Georgetown University, May 21–23, 1990. Six companies participated in this event, DeJarnette Research Systems, General Electric Medical Systems, Merge Technologies, Siemens Medical Systems, Vortech (acquired by Kodak that same year) and 3M. Commercial equipment supporting ACR/NEMA 2.0 was presented at the annual meeting of the Radiological Society of North America (RSNA) in 1990 by these same vendors. Many soon realized that the second version also needed improvement. Several extensions to ACR/NEMA 2.0 were created, like Papyrus (developed by the University Hospital of Geneva, Switzerland) and SPI (Standard Product Interconnect), driven by Siemens Medical Systems and Philips Medical Systems.

The first large-scale deployment of ACR/NEMA technology was made in 1992 by the US Army and Air Force, as part of the MDIS (Medical Diagnostic Imaging Support) program based at Ft. Detrick, Maryland. Loral Aerospace and Siemens Medical Systems led a consortium of companies in deploying the first US military PACS (Picture Archiving and Communications System) at all major Army and Air Force medical treatment facilities and teleradiology nodes at a large number of US military clinics. DeJarnette Research Systems and Merge Technologies provided the modality gateway interfaces from third party imaging modalities to the Siemens SPI network. The Veterans Administration and the Navy also purchased systems from this contract.

In 1993 the third version of the standard was released. Its name was then changed to "Digital Imaging and Communications in Medicine", abbreviated DICOM. New service classes were defined, network support added and the Conformance Statement was introduced. Initially the DICOM standard was referred to as "DICOM 3.0" to distinguish it from its predecessors. DICOM has been constantly updated and extended since 1993, with the intent that changes are backward compatible, except in rare cases where the earlier specification was incorrect or ambiguous. Officially there is no "version" of the standard except the current standard, hence the "3.0" version number is no longer used. There are no "minor" versions to the standard (e.g., no such thing as "DICOM 3.1") and there are no current plans to develop a new, incompatible, version of the standard (i.e., no "DICOM 4.0"). The standard should be referenced without specification of the date of release of a particular published edition, except when specific conformance requirements are invoked that depend on a retired feature that is no longer documented in the current standard.

While the DICOM standard has achieved a near universal level of acceptance among medical imaging equipment vendors and healthcare IT organizations, the standard has its limitations. DICOM is a standard directed at addressing technical interoperability issues in medical imaging. It is not a framework or architecture for achieving a useful clinical workflow. The Integrating the Healthcare Enterprise (IHE) initiative layered on top of DICOM (and HL-7) defines profiles to select features from these standards to implement transactions for specific medical imaging interoperability use cases.

Though always Internet compatible and based on transport over TCP, over time there has been an increasing need to support port 80 HTTP transport to make use easier within the web browser. Most recently, a family of DICOM RESTful web services have been defined to allow mobile device friendly access to DICOM objects and services, which include WADO-RS, STOW-RS and QIDO-RS, which together constitute the DICOMweb initiative.

## Derivations

There are some derivations from the DICOM standard into other application areas. These include DICONDE (*Digital Imaging and Communication in Nondestructive Evaluation*) that was established by ASTM International and DICOS (*Digital Imaging and Communication in Security*).

### DICONDE

DICONDE was established in 2004 as a way for nondestructive testing manufacturers and users to share image data. DICONDE can be used for computed radiography, digital radiography, computed tomography, ultrasonic testing, eddy-current testing, and thermographic testing. DICONDE is used worldwide to store, send, and exchange data from nondestructive material testing. Unlike DICOM in the medical field, the adoption of DICONDE has been slower due to the lack of regulatory requirements for manufacturer-independent interoperability. DICONDE is also gaining importance in the context of Industry 4.0 due to its extensive capabilities for networking systems from different manufacturers.

### DICOS

DICOS was established in 2009 to be used for image sharing in airport security, cargo scanning, and other security applications.

The standard is published by the National Electrical Manufacturers Association (NEMA) as NEMA IIC 1, and was developed in cooperation with the U.S. Department of Homeland Security's Science and Technology Directorate and the Transportation Security Administration (TSA).

## Data format

DICOM groups information into data sets. For example, a file of a chest x-ray image may contain the patient ID within the file, so that the image can never be separated from this information by mistake. This is similar to the way that image formats such as JPEG can also have embedded tags to identify and otherwise describe the image.

A DICOM data object consists of a number of attributes, including items such as name, ID, etc., and also one special attribute containing the image pixel data (i.e. logically, the main object has no "header" as such, being merely a list of attributes, including the pixel data). A single DICOM object can have only one attribute containing pixel data. For many modalities, this corresponds to a single image. However, the attribute may contain multiple "frames", allowing storage of cine loops or other multi-frame data. Another example is NM data, where an NM image, by definition, is a multi-dimensional multi-frame image. In these cases, three- or four-dimensional data can be encapsulated in a single DICOM object. Pixel data can be compressed using a variety of standards, including JPEG, lossless JPEG, JPEG 2000, and run-length encoding (RLE). LZW (zip) compression can be used for the whole data set (not just the pixel data), but this has rarely been implemented.

DICOM uses three different data element encoding schemes. With explicit value representation (VR) data elements, for VRs that are not OB, OW, OF, SQ, UT, or UN, the format for each data element is: GROUP (2 bytes) ELEMENT (2 bytes) VR (2 bytes) LengthInByte (2 bytes) Data (variable length). For the other explicit data elements or implicit data elements, see section 7.1 of Part 5 of the DICOM Standard.

The same basic format is used for all applications, including network and file usage, but when written to a file, usually a true "header" (containing copies of a few key attributes and details of the application that wrote it) is added.

## Image display

To promote identical grayscale image display on different monitors and consistent hard-copy images from various printers, the DICOM committee developed a lookup table to display digitally assigned pixel values. To use the **DICOM grayscale standard display function (GSDF)**, images must be viewed (or printed) on devices that have this lookup curve or on devices that have been calibrated to the GSDF curve.

## Value representations

In addition to a value representation, each attribute also has a *value multiplicity* to indicate the number of data elements contained in the attribute. For character string value representations, if more than one data element is being encoded, the successive data elements are separated by the backslash character "\".

## Services

DICOM consists of services, most of which involve transmission of data over a network. The file format for offline media is a later addition to the standard.

### Store

The DICOM Store service is used to send images or other persistent objects (structured reports, etc.) to a picture archiving and communication system (PACS) or workstation.

### Storage commitment

The DICOM storage commitment service is used to confirm that an image has been permanently stored by a device (either on redundant disks or on backup media, e.g. burnt to a CD). The Service Class User (SCU: similar to a client), a modality or workstation, etc., uses the confirmation from the Service Class Provider (SCP: similar to a server), an archive station for instance, to make sure that it is safe to delete the images locally.

### Query/retrieve

This enables a workstation to find lists of images or other such objects and then retrieve them from a picture archiving and communication system.

### Modality worklist

The DICOM modality worklist service provides a list of imaging procedures that have been scheduled for performance by an image acquisition device (sometimes referred to as a modality system). The items in the worklist include relevant details about the subject of the procedure (patient ID, name, sex, and age), the type of procedure (equipment type, procedure description, procedure code) and the procedure order (referring physician, accession number, reason for exam). An image acquisition device, such as a CT scanner, queries a service provider, such as a RIS, to get this information which is then presented to the system operator and is used by the imaging device to populate details in the image metadata.

Prior to the use of the DICOM modality worklist service, the scanner operator was required to manually enter all the relevant details. Manual entry is slower and introduces the risk of misspelled patient names, and other data entry errors.

### Modality performed procedure step

A complementary service to modality worklist, this enables the modality to send a report about a performed examination including data about the images acquired, beginning time, end time, and duration of a study, dose delivered, etc. It helps give the radiology department a more precise handle on resource (acquisition station) use. Also known as MPPS, this service allows a modality to better coordinate with image storage servers by giving the server a list of objects to send before or while actually sending such objects.

### Print

The DICOM print service is used to send images to a DICOM printer, normally to print an "X-Ray" film. There is a standard calibration (defined in DICOM Part 14) to help ensure consistency between various display devices, including hard copy printout.

### Offline media (files)

The format for offline media files is specified in Part 10 of the DICOM Standard. Such files are sometimes referred to as "Part 10 files".

DICOM restricts the filenames on DICOM media to 8 characters (some systems wrongly use 8.3, but this does not conform to the standard). No information must be extracted from these names (PS3.10 Section 6.2.3.2). This is a common source of problems with media created by developers who did not read the specifications carefully. This is a historical requirement to maintain compatibility with older existing systems. It also mandates the presence of a media directory, the DICOMDIR file, which provides index and summary information for all the DICOM files on the media. The DICOMDIR information provides substantially greater information about each file than any filename could, so there is less need for meaningful file names.

DICOM files typically have a .dcm file extension if they are not part of a DICOM media (which requires them to be without extension).

The MIME type for DICOM files is defined by RFC 3240 as `application/dicom`.

The Uniform Type Identifier type for DICOM files is `org.nema.dicom`.

There is also an ongoing media exchange test and "connectathon" process for CD media and network operation that is organized by the IHE organization.

## Application areas

The core application of the DICOM standard is to capture, store and distribute medical images. The standard also provides services related to imaging such as managing imaging procedure worklists, printing images on film or digital media like DVDs, reporting procedure status like completion of an imaging acquisition, confirming successful archiving of images, encrypting datasets, removing patient identifying information from datasets, organizing layouts of images for review, saving image manipulations and annotations, calibrating image displays, encoding ECGs, encoding CAD results, encoding structured measurement data, and storing acquisition protocols.

### Types of equipment

The DICOM information object definitions encode the data produced by a wide variety of imaging device types, including, CT (computed tomography), MRI (magnetic resonance imaging), ultrasound, X-ray, fluoroscopy, angiography, mammography, breast tomosynthesis, PET (positron emission tomography), SPECT (single-photon emission computed tomography), Endoscopy, microscopy, and whole slide imaging, OCT (optical coherence tomography).

DICOM is also implemented by devices associated with images or imaging workflow including, PACS (picture archiving and communication systems), image viewers and display stations, CAD (computer-aided detection/diagnosis systems), 3D visualization systems, clinical analysis applications, image printers, Film scanners, media burners (that export DICOM files onto CDs, DVDs, etc.), media importers (that import DICOM files from CDs, DVDs, USBs, etc.), RIS (radiology information systems), VNA (vendor-neutral archives), EMR (electronic medical record) systems, and radiology reporting systems

### Fields of medicine

Many fields of medicine have a dedicated Working Group within DICOM, and DICOM is applicable to any field of medicine in which imaging is prevalent, including: radiology, cardiology, oncology, nuclear medicine, radiotherapy, neurology, orthopedics, obstetrics, gynecology, ophthalmology, dentistry, maxillofacial surgery, dermatology, pathology, clinical trials, veterinary medicine, and medical/clinical photography

## Port numbers over IP

DICOM has reserved the following TCP and UDP port numbers by the Internet Assigned Numbers Authority (IANA): 104 well-known port for DICOM over Transmission Control Protocol (TCP) or User Datagram Protocol (UDP). Since 104 is in the reserved subset, many operating systems require special privileges to use it; 2761 registered port for DICOM using Integrated Secure Communication Layer (ISCL) over TCP or UDP; 2762 registered port for DICOM using Transport Layer Security (TLS) over TCP or UDP; 11112 registered port for DICOM using standard, open communication over TCP or UDP. The standard recommends but does not require the use of these port numbers.

## Disadvantages

According to a paper presented at an international symposium in 2008, the DICOM standard has problems related to data entry. "A major disadvantage of the DICOM Standard is the possibility for entering probably too many optional fields. This disadvantage is mostly showing in inconsistency of filling all the fields with the data. Some image objects are often incomplete because some fields are left blank and some are filled with incorrect data."

Another disadvantage is that the file format admits executable code and may contain malware.

- DVTk is an Open Source project for testing, validating and diagnosing communication protocols and scenarios in medical environments. It supports DICOM, HL7 and IHE integration profiles.
- Health Level 7 is a non-profit organization involved in the development of international healthcare informatics interoperability standards. HL7 and DICOM manage a joint Working Group to harmonize areas where the two standards overlap and address imaging integration in the electronic medical record.
- Integrating the Healthcare Enterprise (IHE) is an industry sponsored non-profit organization that profiles the use of standards to address specific healthcare use cases. DICOM is incorporated in a variety of imaging related IHE profiles.
- Systematized Nomenclature of Medicine (SNOMED) is a systematic, computer-processable collection of medical terms, in human and veterinary medicine, to provide codes, terms, synonyms and definitions which cover anatomy, diseases, findings, procedures, microorganisms, substances, etc. DICOM data makes use of SNOMED to encode relevant concepts.
- XnView supports `.dic` / `.dicom` for MIME type `application/dicom`

## Standards used by DICOM

The best known standards and protocols used by DICOM are:

- DICOM makes use of the OSI network model. It uses the 2 network protocols on which the Internet is based and which allow data transfer, TCP / IP, and the HTTP hypertext transfer protocol. Additionally DICOM has its own MIME content type.
- DICOM uses other protocols such as DHCP, SAML ...
- DICOM makes use of a coding system called SNOMED CT that is based on medical and clinical terms.
- DICOM uses an external alphabet known as LOINC.
- In the case of breast images, use is made of other types of structured files known as BI-RADS.

## Standards that use DICOM

The DICOM standard is used in a wide variety of resources (IHE, HL7 ... a) that are related to images.

The ISO12052: 2017 and CEN 12052 standards refer to the DICOM standard.

## Security

In December 2023, cybersecurity researcher Sina Yazdanmehr unveiled a critical security issue within the Store service. This revelation, presented at Black Hat Briefings, demonstrated the potential for malicious actors to manipulate existing series of medical images. Yazdanmehr's research highlighted the alarming capability of attackers to destroy a series of images or introduce misleading indicators of illness.

Ensuring the security of patient data within DICOM is critical, as these files often contain sensitive personal health information (PHI). Security measures for DICOM data include encryption, access control, and auditing mechanisms to prevent unauthorized access, modification, or disclosure of patient information. Compliance with regulations such as the Health Insurance Portability and Accountability Act (HIPAA) in the United States and the General Data Protection Regulation (GDPR) in Europe is essential for protecting patient privacy and ensuring the integrity of medical records.

### De-identification of DICOM

De-identification of DICOM refers to the process of removing or anonymizing personal health information (PHI) from medical images to protect patient privacy. This process is vital for sharing medical data for research, educational purposes, or public health activities while complying with privacy regulations. Techniques for de-identification involve stripping out or masking identifiable data elements within the DICOM metadata, such as patient names, birth dates, and other unique identifiers. Ensuring thorough de-identification is crucial to balance the benefits of data sharing with the obligation to maintain patient confidentiality.
