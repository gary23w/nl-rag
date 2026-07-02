---
title: "Data security"
source: https://en.wikipedia.org/wiki/Data_security
domain: dspm
license: CC-BY-SA-4.0
tags: data security posture management, sensitive data discovery, data classification governance, data access risk, cloud data protection
fetched: 2026-07-02
---

# Data security

**Data security** or **data protection** is the process of securing digital information to protect it from online threats. Data security or protection means protecting digital data, such as those in a database, from destructive forces and from the unwanted actions of unauthorized users, such as a cyberattack or a data breach. Data security protects computer hardware, software, storage devices, and the data of user devices. Data security also protects the data of organizations, companies and administrative controls.

Proper data security practices reduce the risk of data breaches, including unauthorized access, theft and loss of individual data such as identity documents and bank data. Data security is part of information security.

## Technologies

### Disk encryption

Disk encryption refers to encryption technology that encrypts data on a hard disk drive. It takes data from a storage device and coverts it into an unreadable format. Disk encryption typically takes form in either software (see disk encryption software) or hardware (see disk encryption hardware) which can be used together. Disk encryption is often referred to as on-the-fly encryption (OTFE) or transparent encryption. Full disk encryption encrypts each individual sector of a disk volume. Files and user data are encrypted to hinder unauthorized users from accessing without a decryption key. A diversifier permits a plaintext of a specific disk sector to be encrypted into different ciphertexts, which does not require additional storage, such as an initialization vector (IV) or message authentication code (MAC).

### Software versus hardware-based mechanisms for protecting data

Software-based security solutions encrypt the data to protect it from theft. However, a malicious program or a hacker could corrupt the data to make it unrecoverable, making the system unusable. Hardware-based security solutions prevent read and write access to data, which provides very strong protection against tampering and unauthorized access.

Hardware-based security or assisted computer security offers an alternative to software-only computer security. Security tokens such as those using PKCS#11 or a mobile phone may be more secure due to the physical access required in order to be compromised. Access is enabled only when the token is connected and the correct PIN is entered (see two-factor authentication). However, dongles can be used by anyone who can gain physical access to it. Newer technologies in hardware-based security solve this problem by offering full proof of security for data.

Working off hardware-based security: A hardware device allows a user to log in, log out and set different levels through manual actions. Many devices use biometric technology to prevent malicious users from logging in, logging out, and changing privilege levels. The current state of a user of the device is read by controllers in peripheral devices such as hard disks. Illegal access by a malicious user or a malicious program is interrupted based on the current state of a user by hard disk and DVD controllers making illegal access to data impossible. Hardware-based access control is more secure than the protection provided by the operating systems as operating systems are vulnerable to malicious attacks by viruses and hackers. The data on hard disks can be corrupted after malicious access is obtained. With hardware-based protection, the software cannot manipulate the user privilege levels. A hacker or a malicious program cannot gain access to secure data protected by hardware or perform unauthorized privileged operations. This assumption is broken only if the hardware itself is malicious or contains a backdoor. The hardware protects the operating system image and file system privileges from being tampered with. Therefore, a completely secure system can be created using a combination of hardware-based security and secure system administration policies.

### Backups

Backup is the process of reproducing copies of essential data and storing in a separate, secured place. It is used to ensure data that is lost can be recovered from another source. Backups contains a minimum of one copy of the data that requires preservation. It is considered essential to keep a backup of any data in most industries and the process is recommended for any files of importance to a user.

There are 3 types of backups; full backups, incremental backups, and differential backups. Full backups secure all data from a production system, such as a server, database, or other connected data source. It is impossible to lose all data in a full backup if a breach or corruption were to occur. Full backups require a significantly large amount of time to back up and may be time-consuming taking hours to days to complete. Incremental backups only secures changed data since last backup. While all backups are done in full backups, incremental backups only save data that is recently or frequently changed. Incremental backups require lower storage costs making it a prominent solution for growing datasets.

### Data Privacy

Data privacy (or information privacy) is the right for individual's data to be secured to obstruct the use of unauthorized access. It gives individuals control over their data and how it can be shared to third parties. The U.S Privacy Protection Law (see Privacy laws of the United States) requires organizations to inform individuals of how their data is collected and when a data breach occurs. By implementing an encryption, it ensures that private data is unreadable to cybercriminals.

### Data masking

Data masking of structured data is the process of obscuring (masking) specific data within a database table or cell to ensure that data security is maintained and sensitive information is not exposed to unauthorized personnel. This may include masking the data from users (for example so banking customer representatives can only see the last four digits of a customer's national identity number), developers (who need real production data to test new software releases but should not be able to see sensitive financial data), outsourcing vendors, etc. Data masking is a form of encryption, as it obscures data by modifying particular letters and numbers to keep data concealed and protected from potential hackers. The individual that has access to the code that decrypts the replaced characters are the only ones that can uncover the data.

### Data erasure

Data erasure (or data deletion, data destruction) is a method of software-based overwriting that permanently clears all electronic data residing on a hard drive or other digital media to ensure that no sensitive data is lost when an asset is retired or reused. Article 17: Right to be Forgotten states that users have the right to permanently remove all of their private information from their old devices/services to give people more control over their data. Users are able to switch between devices efficiently.

## Threats

### Malware

Malware (or malicious software) is designed to destroy, corrupt or gain unauthorized access to a computer for the purpose of stealing, or destroying data. Hackers who use malware typically utilize many types of malware, which includes computer virus, computer worms, ransomware, spyware and Trojan horse to create a vast system of disruption and cause easy data theft. One of the victims of the vast system of disruption includes healthcare workers, who are targeted by compromised systems by infections and then having their data attacked.

### Phishing

Phishing is a type of scam that allows hackers to hoax people using psychological and social engineering (using human emotions such as their trust and fear) tactics into giving personal data through emails and messages, and install computer viruses if the individual were to click on a malicious link unknowingly. Attackers are able to create websites that are very similar to original websites, which makes it difficult to detect a fake website, causing individuals to fall for giving in information. Phishing attackers use human emotion to exploit them, such as making them feel fear, urgency, sympathy with the message being sent by the sender. Emails (Or Email spoofing) with impersonated companies and fake websites copying the original are ways to exploit people. Email spoofing show false names and emails of the original ones to copy several banks, companies and agencies, using warnings to manipulate people into feeling urgent about the email.

## International laws and standards

### International laws

In the UK, the Data Protection Act is used to ensure that personal data is accessible to those whom it concerns, and provides redress to individuals if there are inaccuracies. This is particularly important to ensure individuals are treated fairly, for example for credit checking purposes. The Data Protection Act states that only individuals and companies with legitimate and lawful reasons can process personal information and cannot be shared. Data Privacy Day is an international holiday started by the Council of Europe that occurs every January 28.

Since the General Data Protection Regulation (GDPR) of the European Union (EU) became law on May 25, 2018, organizations may face significant penalties of up to €20 million or 4% of their annual revenue if they do not comply with the regulation. It is intended that GDPR will force organizations to understand their data privacy risks and take the appropriate measures to reduce the risk of unauthorized disclosure of consumers’ private information.

### International standards

The international standards ISO/IEC 27001:2013 and ISO/IEC 27002:2013 cover data security under the topic of information security, and one of its cardinal principles is that all stored information, i.e. data, should be owned so that it is clear whose responsibility it is to protect and control access to that data. The following are examples of organizations that help strengthen and standardize computing security:

The Trusted Computing Group is an organization that helps standardize computing security technologies.

The Payment Card Industry Data Security Standard (PCI DSS) is a proprietary international information security standard for organizations that handle cardholder information for the major debit, credit, prepaid, e-purse, automated teller machines, and point of sale cards.

The General Data Protection Regulation (GDPR) proposed by the European Commission will strengthen and unify data protection for individuals within the EU, whilst addressing the export of personal data outside the EU.

## Safeguards

The four types of technical safeguards are access controls, flow controls, inference controls, and data encryption. Access controls manage user entry and data manipulation, while flow controls regulate data dissemination. Inference controls prevent deduction of confidential information from statistical databases and data encryption prevents unauthorized access to confidential information. Health Insurance Portability and Accountability Act (HIPAA) is a law that requires entities such as healthcare providers to keep patient confidentiality for three required safeguards: administrative, physical, and technical.
