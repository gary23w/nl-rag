---
title: "Digital identity"
source: https://en.wikipedia.org/wiki/Digital_identity
domain: self-sovereign-identity
license: CC-BY-SA-4.0
tags: self sovereign identity, user controlled identity, decentralized identifier wallet, verifiable credential holder, digital identity ownership
fetched: 2026-07-02
---

# Digital identity

A **digital identity** is data stored on computer systems relating to an individual, organization, application, or device. For individuals, it involves the collection of personal data that is essential for facilitating automated access to digital services, confirming one's identity on the internet, and allowing digital systems to manage interactions between different parties. It is a component of a person's social identity in the digital realm, often referred to as their online identity.

Digital identities are composed of the full range of data produced by a person's activities on the internet, which may include usernames and passwords, search histories, dates of birth, social security numbers, and records of online purchases. When such personal information is accessible in the public domain, it can be used by others to piece together a person's offline identity. Furthermore, this information can be compiled to construct a data double, a comprehensive profile created from a person's scattered digital footprints across various platforms. These profiles enable personalized experiences on the internet and within different digital services.

## Background

A critical problem in cyberspace is knowing who one is interacting with. Using only static identifiers such as passwords and email, there is no way to precisely determine the identity of a person in cyberspace because this information can be stolen or used by many individuals acting as one. Digital identity based on dynamic entity relationships captured from behavioral history across multiple websites and mobile apps can verify and authenticate identity with up to 95% accuracy.

By comparing a set of entity relationships between a new event (e.g., login) and past events, a pattern of convergence can verify or authenticate the identity as legitimate whereas divergence indicates an attempt to mask an identity. Data used for digital identity is generally encrypted using a one-way hash, thereby avoiding privacy concerns. Because it is based on behavioral history, a digital identity is very hard to fake or steal.

A digital identity may also be referred to as a *digital subject* or *digital entity*. They are the digital representation of a set of claims made by one party about itself or another person, group, thing, or concept. A digital twin which is also commonly known as a data double or virtual twin is a secondary version of the original user's data. Which is used both as a way to observe what said user does on the internet as well as customize a more personalized internet experience. Due to the collection of personal data, there have been many social, political, and legal controversies tying into data doubles.

While in manufacturing and other multi-organization environments, digital identity is used to enable secure interactions between separate organizations. For a secure federated digital thread, participating systems rely on verified digital identities to authenticate organizations before exchanging product lifecycle data, supporting trust and controlled data sharing across organizational boundaries.

#### Attributes, preferences, and traits

The attributes of a digital identity are acquired and contain information about a user, such as medical history, purchasing behavior, bank balance, age, and so on. Preferences retain a user's choices such as favorite brand of shoes, and preferred currency. Traits are features of the user that are inherent, such as eye color, nationality, and place of birth. Although attributes of a user can change easily, traits change slowly, if at all. A digital identity also has entity relationships derived from the devices, environment, and locations from which an individual is active on the Internet. Some of those include facial recognition, fingerprints, photos, and so many more personal attributes/preferences.

## Technical aspects

### Issuance

Digital identities can be issued through digital certificates. These certificates contain data associated with a user and are issued with legal guarantees by recognized certification authorities.

### Trust, authentication and authorization

In order to assign a digital representation to an entity, the attributing party must trust that the claim of an attribute (such as name, location, role as an employee, or age) is correct and associated with the person or thing presenting the attribute. Conversely, the individual claiming an attribute may only grant selective access to its information (e.g., proving identity in a bar or PayPal authentication for payment at a website). In this way, digital identity is better understood as a particular viewpoint within a mutually-agreed relationship than as an objective property.

#### Authentication

*Authentication* is the assurance of the identity of one entity to another. It is a key aspect of digital trust. In general, business-to-business authentication is designed for security, but user-to-business authentication is designed for simplicity.

Authentication techniques include the presentation of a unique object such as a bank credit card, the provision of confidential information such as a password or the answer to a pre-arranged question, the confirmation of ownership of an email address, and more robust but costly techniques using encryption. Physical authentication techniques include iris scanning, fingerprinting, and voice recognition; those techniques are called *biometrics*. The use of both static identifiers (e.g., username and password) and personal unique attributes (e.g., biometrics) is called *multi-factor authentication* and is more secure than the use of one component alone.

Whilst technological progress in authentication continues to evolve, these systems do not prevent aliases from being used. To address this, proof of personhood protocols such as World ID by Tool for Humanity, Humanode, and BrightID are increasingly employed to verify that a digital identity belongs to a unique, living human, effectively preventing the creation of duplicate accounts or automated Sybil identities. In blockchain systems, account-based identity approaches include ERC-725, a draft Ethereum standard for smart-contract accounts with generic data storage and execution, and LUKSO Universal Profiles, which use ERC-725/LSP0 to combine profile metadata with account permissions. The introduction of strong authentication for online payment transactions within the European Union now links a verified person to an account, where such person has been identified in accordance with statutory requirements prior to account being opened. Verifying a person opening an account online typically requires a form of device binding to the credentials being used. This verifies that the device that stands in for a person on the Internet is actually the individual's device and not the device of someone simply claiming to be the individual. The concept of reliance authentication makes use of pre-existing accounts, to piggy back further services upon those accounts, providing that the original source is reliable. The concept of reliability comes from various anti-money laundering and counter-terrorism funding legislation in the US, EU28, Australia, Singapore and New Zealand where second parties may place reliance on the customer due diligence process of the first party, where the first party is say a financial institution. An example of reliance authentication is PayPal's verification method.

#### Authorization

*Authorization* is the determination of any entity that controls resources that the authenticated can access those resources. Authorization depends on authentication, because authorization requires that the critical attribute (i.e., the attribute that determines the authorizer's decision) must be verified. For example, authorization on a credit card gives access to the resources owned by Amazon, e.g., Amazon sends one a product. Authorization of an employee will provide that employee with access to network resources, such as printers, files, or software. For example, a database management system might be designed so as to provide certain specified individuals with the ability to retrieve information from a database but not the ability to change data stored in the database, while giving other individuals the ability to change data.

Consider the person who rents a car and checks into a hotel with a credit card. The car rental and hotel company may request authentication that there is credit enough for an accident, or profligate spending on room service. Thus a card may later be refused when trying to purchase an activity such as a balloon trip. Though there is adequate credit to pay for the rental, the hotel, and the balloon trip, there is an insufficient amount to also cover the authorizations. The actual charges are authorized after leaving the hotel and returning the car, which may be too late for the balloon trip.

Valid online authorization requires analysis of information related to the digital event including device and environmental variables. These are generally derived from the data exchanged between a device and a business server over the Internet.

### Verification

Businesses use identity verification services to check whether a person has provided information associated with the identity of a real person. This is a form of electronic authentication. Some websites with user accounts, such as social media services, offer account verification to show that an account is operated by a specific person.

#### Rel="me" verification

Some decentralized identity verification systems, such as within the Fediverse and Mastodon, use a web standard microformat called `rel="me"`. The `rel="me"` value is an HTML link relationship attribute used to indicate that two web resources represent the same person or entity. It originated as part of early web microformats and has been used in decentralized identity systems to associate profiles and websites controlled by a single individual.

### Digital identifiers

Digital identity requires digital identifiers—strings or tokens that are unique within a given scope (globally or locally within a specific domain, community, directory, application, etc.).

Identifiers may be classified as *omnidirectional* or *unidirectional*. Omnidirectional identifiers are public and easily discoverable, whereas unidirectional identifiers are intended to be private and used only in the context of a specific identity relationship.

Identifiers may also be classified as *resolvable* or *non-resolvable*. Resolvable identifiers, such as a domain name or email address, may be easily dereferenced into the entity they represent, or some current state data providing relevant attributes of that entity. Non-resolvable identifiers, such as a person's real name, or the name of a subject or topic, can be compared for equivalence but are not otherwise machine-understandable.

There are many different schemes and formats for digital identifiers. Uniform Resource Identifier (URI) and the internationalized version Internationalized Resource Identifier (IRI) are the standard for identifiers for websites on the World Wide Web. OpenID and Light-weight Identity are two web authentication protocols that use standard HTTP URIs (often called URLs). A Uniform Resource Name is a persistent, location-independent identifier assigned within the defined namespace.

### Digital object architecture

Digital object architecture is a means of managing digital information in a network environment. In digital object architecture, a digital object has a machine and platform independent structure that allows it to be identified, accessed and protected, as appropriate. A digital object may incorporate not only informational elements, i.e., a digitized version of a paper, movie or sound recording, but also the unique identifier of the digital object and other metadata about the digital object. The metadata may include restrictions on access to digital objects, notices of ownership, and identifiers for licensing agreements, if appropriate.

### Handle System

The Handle System is a general purpose distributed information system that provides efficient, extensible, and secure identifier and resolution services for use on networks such as the internet. It includes an open set of protocols, a namespace, and a reference implementation of the protocols. The protocols enable a distributed computer system to store identifiers, known as handles, of arbitrary resources and resolve those handles into the information necessary to locate, access, contact, authenticate, or otherwise make use of the resources. This information can be changed as needed to reflect the current state of the identified resource without changing its identifier, thus allowing the name of the item to persist over changes of location and other related state information. The original version of the Handle System technology was developed with support from the Defense Advanced Research Projects Agency.

### Extensible resource identifiers

A new OASIS standard for abstract, structured identifiers, XRI (Extensible Resource Identifiers), adds new features to URIs and IRIs that are especially useful for digital identity systems. OpenID also supports XRIs, which are the basis for i-names.

### Risk-based authentication

Risk-based authentication is an application of digital identity whereby multiple entity relationship from the device (e.g., operating system), environment (e.g., DNS Server) and data entered by a user for any given transaction is evaluated for correlation with events from known behaviors for the same identity. Analysis are performed based on quantifiable metrics, such as transaction velocity, locale settings (or attempts to obfuscate), and user-input data (such as ship-to address). Correlation and deviation are mapped to tolerances and scored, then aggregated across multiple entities to compute a transaction risk-score, which assess the risk posed to an organization.

### Taxonomies of identity

Digital identity attributes exist within the context of ontologies.

The development of digital identity network solutions that can interoperate taxonomically diverse representations of digital identity is a contemporary challenge. Free-tagging has emerged recently as an effective way of circumventing this challenge (to date, primarily with application to the identity of digital entities such as bookmarks and photos) by effectively flattening identity attributes into a single, unstructured layer. However, the organic integration of the benefits of both structured and fluid approaches to identity attribute management remains elusive.

### Networked identity

Identity relationships within a digital network may include multiple identity entities. However, in a decentralized network like the Internet, such extended identity relationships effectively requires both the existence of independent trust relationships between each pair of entities in the relationship and a means of reliably integrating the paired relationships into larger relational units. And if identity relationships are to reach beyond the context of a single, federated ontology of identity (see Taxonomies of identity above), identity attributes must somehow be matched across diverse ontologies. The development of network approaches that can embody such integrated "compound" trust relationships is currently a topic of much debate in the blogosphere.

Integrated compound trust relationships allow, for example, entity A to accept an assertion or claim about entity B by entity C. C thus vouches for an aspect of B's identity to A.

A key feature of "compound" trust relationships is the possibility of selective disclosure from one entity to another of locally relevant information. As an illustration of the potential application of selective disclosure, let us suppose a certain Diana wished to book a hire car without disclosing irrelevant personal information (using a notional digital identity network that supports compound trust relationships). As an adult, UK resident with a current driving license, Diana might have the UK's Driver and Vehicle Licensing Agency vouch for her driving qualification, age, and nationality to a car-rental company without having her name or contact details disclosed. Similarly, Diana's bank might assert just her banking details to the rental company. Selective disclosure allows for appropriate privacy of information within a network of identity relationships.

A classic form of networked digital identity based on international standards is the "White Pages".

An electronic white pages links various devices, like computers and telephones, to an individual or organization. Various attributes such as X.509v3 digital certificates for secure cryptographic communications are captured under a schema, and published in an LDAP or X.500 directory. Changes to the LDAP standard are managed by working groups in the IETF, and changes in X.500 are managed by the ISO. The ITU did significant analysis of gaps in digital identity interoperability via the FGidm (ƒfocus group on identity management).

Implementations of X.500[2005] and LDAPv3 have occurred worldwide but are primarily located in major data centers with administrative policy boundaries regarding sharing of personal information. Since combined X.500 [2005] and LDAPv3 directories can hold millions of unique objects for rapid access, it is expected to play a continued role for large scale secure identity access services. LDAPv3 can act as a lightweight standalone server, or in the original design as a TCP-IP based Lightweight Directory Access Protocol compatible with making queries to an X.500 mesh of servers which can run the native OSI protocol.

This will be done by scaling individual servers into larger groupings that represent defined "administrative domains", (such as the country level digital object) which can add value not present in the original "White Pages" that was used to look up phone numbers and email addresses, largely now available through non-authoritative search engines.

The ability to leverage and extend a networked digital identity is made more practicable by the expression of the level of trust associated with the given identity through a common Identity Assurance Framework.

### Digital rhetoric

In digital rhetoric, digital identity is treated as a rhetorical construction shaped by the choices users make in how they represent themselves online, rather than as a fixed attribute of a person. Researchers in the field study how those self-representations are influenced by platform design, audience, and the technical affordances available for self-presentation.

Sherry Turkle, in *Life on the Screen* (1995), argued that online environments allow users to present multiple, fluid versions of the self that are less anchored to physical embodiment than offline identity. Later scholarship has questioned how far this separation extends in practice, arguing that characteristics such as race, gender, and class continue to shape how users are perceived and treated online.

### Legal issues

Clare Sullivan presents the grounds for digital identity as an emerging legal concept. The UK's Identity Cards Act 2006 confirms Sullivan's argument and unfolds the new legal concept involving database identity and transaction identity. Database identity is the collection of data that is registered about an individual within the databases of the scheme and transaction identity is a set of information that defines the individual's identity for transactional purposes. Although there is reliance on the verification of identity, none of the processes used are entirely trustworthy. The consequences of digital identity abuse and fraud are potentially serious since in possible implications the person is held legally responsible.

Legal scholars Lusine Vardanyan, Ondrej Hamulak, and Hovsep Kocharyan from Palacký University in Olomouc have analyzed the complexities of digital identity and its regulation. Their research highlights the difficulties that current legal frameworks face in adequately safeguarding digital identity against manipulation, unauthorized use, and opaque profiling mechanisms. They argue that existing data protection regimes predominantly focus on the protection of information rather than the individual as a whole, which may contribute to a loss of control over one's digital presence. A key concept proposed to address these issues is the right to informational self-determination, which would provide individuals with greater control over the collection, use, and dissemination of their personal data. This right is seen as essential in ensuring personal autonomy, enabling individuals to shape and manage their digital identities in alignment with their real-world personas. Proponents argue that the development of legal tools for digital identity management should be grounded in principles such as informed consent, transparency, and self-governance. The work of scholars such as Shoshana Zuboff has been influential in highlighting the risks associated with the commodification of personal data and the erosion of individual agency in digital spaces. Recognizing informational self-determination as a fundamental right is viewed as a critical step in enhancing data protection and ensuring security and autonomy in an increasingly networked society.

### Business aspects

Corporations are recognizing the power of the internet to tailor their online presence to each individual customer. Purchase suggestions, personalized adverts, and other tailored marketing strategies are a great success for businesses. Such tailoring, however, depends on the ability to connect attributes and preferences to the identity of the visitor.

As the internet becomes more attuned to privacy concerns, media publishers, application developers, and online retailers are re-evaluating their strategies, sometimes reinventing their business models completely. Increasingly, the trend is shifting towards monetizing online offerings directly, with users being asked to pay for access through subscriptions and other forms of payment, moving away from the reliance on collecting personal data.

### Digital death

Digital death is the phenomenon of people continuing to have Internet accounts after their deaths. This results in several ethical issues concerning how the information stored by the deceased person may be used or stored or given to the family members. It also may result in confusion due to automated social media features such as birthday reminders, as well as uncertainty about the deceased person's willingness to pass their personal information to a third party. Many social media platforms do not have clear policies about digital death. Many companies secure digital identities after death or legally pass those on to the deceased people's families. Some companies will also provide options for digital identity erasure after death. Facebook/Meta is a clear-cut example of a company that provides digital options after death. Descendants or friends of the deceased individual can let Facebook know about the death and have all of their previous digital activity removed. Digital activity is but not limited to messages, photos, posts, comments, reactions, stories, archived history, etc. Furthermore, the entire Facebook account will be deleted upon request.

### Policy aspects

There are proponents of treating self-determination and freedom of expression of digital identity as a new human right. Some have speculated that digital identities could become a new form of legal entity. As technology develops so does the intelligence of certain digital identities, moving forward many believe that there should be more developments in legal aspects that regulate online presences and collection.

Digital identity can be a component to techno-authoritarianism.

### Security and privacy issues

Several writers have pointed out the tension between services that use digital identity on the one hand and user privacy on the other.[1][2][3][4][5] Services that gather and store data linked to a digital identity, which in turn can be linked to a user's real identity, can learn a great deal about individuals. GDPR is one attempt to address this concern using the regulation. This regulation tactic was introduced by the European Union (EU) in 2018 for addressing concerns about the privacy and personal data of EU citizens. GDPR applies to all companies, regardless of location, that handle users within the EU. Any company that collects, stores, and operates with data from EU citizens must disclose key details about the management of that data to EU individuals. EU citizens can also request for certain aspects of their collected data to be deleted. To help enforce GDPR, the EU has applied penalties to companies that operate with data from EU citizens but fail to follow the regulations

Many systems provide privacy-related mitigations when analyzing data linked to digital identities. One common mitigation is data anonymization, such as hashing user identifiers with a cryptographic hash function. Another popular technique is adding statistical noise to a data set to reduce identifiability, such as in differential privacy. Although a digital identity allows consumers to transact from anywhere and more easily manage various ID cards, it also poses a potential single point of compromise that malicious hackers can use to steal all of that personal information.

Hence, several different account authentication methods have been created to protect users. Initially, these authentication methods will require a setup from the user to enable these security features when attempting a login.

- Two-factor Authentication: This form of authentication is a two-layered security process. The first layer will require the password for the account the user is trying to access. Following a successful password input, the second layer of security will then prompt the user to prove that they have access to something which they would only have. Typically, these are unique one-time generated security codes that will be sent to the email or phone number registered on the account. Successful input of these unique one-time generated security codes will then grant the user permission into the account. There are also maybe options for answering security questions that will grant access to the account, something which only the actual user would know the answers too. The second layer of the two-factor authentication process can also include face biometric factors such as facial scans, fingerprints, or a voice print rather than one-time generates security codes or answering security questions. Two-factor authentication will typically be required every time when attempting a login to an account
- Certificate-Based Authentication: This form of authentication prioritizes the use of digital certificates, typically an individual's driver's license or a passport as a form of an electronic document. A certification authority will then prove ownership of a public key to the owner of that digital certificate. Certificate-based authorities will prioritize these electronic documents to identify a user. When signing into a server, the individual presents their digital certificate, the server will then verify the credibility of that digital certificate through cryptography, and the authentication process is finally complete when that private key is certified

## National digital identity systems

Although many facets of digital identity are universal owing in part to the ubiquity of the Internet, some regional variations exist due to specific laws, practices, and government services that are in place. For example, digital identity can use services that validate driving licences, passports, and other physical documents online to help improve the quality of a digital identity. Also, strict policies against money laundering mean that some services, such as money transfers, need a stricter level of validation of digital identity. Digital identity in the national sense can mean a combination of single sign-on and/or validation of assertions by trusted authorities (generally the government).

Countries or regions with official or unofficial digital identity systems include:

- China
- India (Aadhaar card)
- Iran (Iranian National smart card ID)
- Singapore (SingPass and CorpPass)
- Estonia (Estonian identity card)
- Germany
- Italy (Sistema Pubblico di Identità Digitale and Italian electronic identity card)
- Mauritius
- Monaco
- Poland (mObywatel)
- Russia (Universal electronic card)
- Ukraine (Diia)
- UK (GOV.UK Verify)
- Australia (MyGovID and Australia Post Digital iD)
- United States (Social Security numbers)
  - In 2021, the 117th Congressional session introduced H.R. 4258, also named Improving Digital Identity Act of 2021, in an effort to establish a governmentwide approach to improving digital ID. It was turned over to the Committee on Oversight and Reform. Additional efforts were ordered in October 2022 by U.S. Senators Kyrsten Sinema, D-Ariz., and Cynthia Lummis, R-Wy. with S. 4528, Improving Digital Identity Act of 2022, from the Senate Committee on Homeland Security and Governmental Affairs. This new order is trying to establish a task force to coordinate federal, state, and private-sector efforts to develop digital identity credentials, such as driver's licenses, passports, and birth certificates.
  - In 2019, Colorado became the first state to accept Digital ID via its myColorado app. Because the myColorado app can be downloaded via Google Play Store or Apple App Store, it has simplified identification, gaining over 1 million users.
  - In 2022, the US State of California started piloting a Digital ID program for their citizens for access to digital government services.
- Dominican Republic
- Canada
  - Canada is actively working on providing its citizens with forms of Digital ID in partnership with the non-profit Digital ID & Authentical Council of Canada (DIACC). DIACC will also oversee the Voila Verified Trustmark Program which will provide verification of compliance standards, specifically ISO standards, as a way to certify Digital ID service providers against the Pan-Canadian Trust Framework. As of 2023, there is not a nationwide Digital ID program; however, the province of Alberta supports its own unique version of a Digital ID. Ontario and Quebec have plans to launch their Digital ID but were delayed by the COVID-19 Pandemic.
  - The Canadian Public Sector has developed the Public Sector Profile of the Pan-Canadian Trust Framework. This framework has been used by the Government of Canada to assess the Province of Alberta and the Province of British Columbia and accepted their program as trusted digital identities for use by federal government services. Provincial residents can now register and sign in with their province their My Service Canada Account
  - The Digital Governance Council, an accredited standards development organization, has published a national standard CAN/CIOSC 103:2020 Digital Trust and Identity and is developing conformity assessment schemes for public sector and regulated programs.
- Bhutan

Countries or regions with proposed digital identity systems include:

- European Union (European Digital Identity) In April 2024, the EU adopted Regulation (EU) 2024/1183 to establish the European Digital Identity framework, including provisions for an EU Digital Identity Wallet.
- Jamaica
- Turks and Caicos/Caribbean
