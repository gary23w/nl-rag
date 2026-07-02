---
title: "Facial recognition system (part 2/2)"
source: https://en.wikipedia.org/wiki/Facial_recognition_system
domain: image-recognition
license: CC-BY-SA-4.0
tags: image recognition, image classification, visual recognition, convolutional network, feature learning
fetched: 2026-07-02
part: 2/2
---

## Advantages and disadvantages

### Compared to other biometric systems

In 2006, the performance of the latest face recognition algorithms was evaluated in the Face Recognition Grand Challenge (FRGC). High-resolution face images, 3-D face scans, and iris images were used in the tests. The results indicated that the new algorithms are 10 times more accurate than the face recognition algorithms of 2002 and 100 times more accurate than those of 1995. Some of the algorithms were able to outperform human participants in recognizing faces and could uniquely identify identical twins.

One key advantage of a facial recognition system that it is able to perform mass identification as it does not require the cooperation of the test subject to work. Properly designed systems installed in airports, multiplexes, and other public places can identify individuals among the crowd, without passers-by even being aware of the system. However, as compared to other biometric techniques, face recognition may not be most reliable and efficient. Quality measures are very important in facial recognition systems as large degrees of variations are possible in face images. Factors such as illumination, expression, pose and noise during face capture can affect the performance of facial recognition systems. Among all biometric systems, facial recognition has the highest false acceptance and rejection rates, thus questions have been raised on the effectiveness of or bias of face recognition software in cases of railway and airport security, law enforcement and housing and employment decisions.

### Weaknesses

Ralph Gross, a researcher at the Carnegie Mellon Robotics Institute in 2008, describes one obstacle related to the viewing angle of the face: "Face recognition has been getting pretty good at full frontal faces and 20 degrees off, but as soon as you go towards profile, there've been problems." Besides the pose variations, low-resolution face images are also very hard to recognize. This is one of the main obstacles of face recognition in surveillance systems. It has also been suggested that camera settings can favour sharper imagery of white skin than of other skin tones.

Face recognition is less effective if facial expressions vary. A big smile can render the system less effective. For instance: Canada, in 2009, allowed only neutral facial expressions in passport photos.

There is also inconstancy in the datasets used by researchers. Researchers may use anywhere from several subjects to scores of subjects and a few hundred images to thousands of images. Data sets may be diverse and inclusive or mainly contain images of white males. It is important for researchers to make available the datasets they used to each other, or have at least a standard or representative dataset.

Although high degrees of accuracy have been claimed for some facial recognition systems, these outcomes are not universal. The consistently worst accuracy rate is for those who are 18 to 30 years old, Black and female.

### Racial bias and skin tone

Studies have shown that facial recognition algorithms tend to perform better on individuals with lighter skin tones compared to those with darker skin tones. For example, a 2018 study found that leading commercial gender classification models, which are facial recognition models, have an error rate up to 7 times higher for those with darker skin tones compared to those with lighter skin tones. Initially this disparity was attributed to the imbalance in training datasets, which often overrepresent lighter-skinned individuals, leading to higher error rates for darker-skinned people. However, later studies showed that dataset imbalance is not the sole cause for difference in performance.

Common image compression methods, such as JPEG chroma subsampling, have been found to disproportionately degrade performance for darker-skinned individuals. These methods inadequately represent color information, which adversely affects the ability of algorithms to recognize darker-skinned individuals accurately.

### Cross-race effect bias

Facial recognition systems often demonstrate lower accuracy when identifying individuals with non-Eurocentric facial features. Known as the Cross-race effect, this bias occurs when systems perform better on racial or ethnic groups that are overrepresented in their training data, resulting in reduced accuracy for underrepresented groups. The overrepresented group is generally the more populous group in the location that the model is being developed. For example, models developed in Asian cultures generally perform better on Asian facial features than Eurocentric facial features due to overrepresentation in the developers training dataset. The opposite is observed in models developed in Eurocentric cultures.

The systems used for facial recognition often lack the sufficient training needed to fully recognize those features not of Eurocentric descent. When the training and databases for these Machine Learning (ML) models do not contain a diverse representation, the models fail to identify the missed population, adding to their racial biases.

The cross-race effect is not exclusive to machines; humans also experience difficulty recognizing faces from racial or ethnic groups different from their own. This is an example of inherent human biases being perpetuated in training datasets.

### Challenges for individuals with disabilities

Facial recognition technologies encounter significant challenges when identifying individuals with disabilities. For instance, systems have been shown to perform worse when recognizing individuals with Down syndrome, often leading to increased false match rates. This is due to distinct facial structures associated with the condition that are not adequately represented in training datasets.

More broadly, facial recognition systems tend to overlook diverse physical characteristics related to disabilities. The lack of representative data for individuals with varying disabilities further emphasizes the need for inclusive algorithmic designs to mitigate bias and improve accuracy.

Additionally, facial expression recognition technologies often fail to accurately interpret the emotional states of individuals with intellectual disabilities. This shortcoming can hinder effective communication and interaction, underscoring the necessity for systems trained on diverse datasets that include individuals with intellectual disabilities.

Furthermore, biases in facial recognition algorithms can lead to discriminatory outcomes for people with disabilities. For example, certain facial features or asymmetries may result in misidentification or exclusion, highlighting the importance of developing accessible and fair biometric systems.

### Advancements in fairness and mitigation strategies

A review in 2025 showed improved mitigation of demographic biases in face recognition: by processing at input, model, or output stages.

Additionally, targeted dataset collection has been shown to improve racial equity in facial recognition systems. By prioritizing diverse data inputs, researchers demonstrated measurable reductions in performance disparities between racial groups.

### Ineffectiveness

Critics of the technology complain that the London Borough of Newham scheme has, as of 2004, never recognized a single criminal, despite several criminals in the system's database living in the Borough and the system has been running for several years. "Not once, as far as the police know, has Newham's automatic face recognition system spotted a live target." This information seems to conflict with claims that the system was credited with a 34% reduction in crime (hence why it was rolled out to Birmingham also).

An experiment in 2002 by the local police department in Tampa, Florida, had similarly disappointing results. A system at Boston's Logan Airport was shut down in 2003 after failing to make any matches during a two-year test period.

In 2014, Facebook stated that in a standardized two-option facial recognition test, its online system scored 97.25% accuracy, compared to the human benchmark of 97.5%.

Systems are often advertised as having accuracy near 100%; this is misleading as the outcomes are not universal. The studies often use samples that are smaller and less diverse than would be necessary for large scale applications. Because facial recognition is not completely accurate, it creates a list of potential matches. A human operator must then look through these potential matches and studies show the operators pick the correct match out of the list only about half the time. This causes the issue of targeting the wrong suspect.


## Controversies

### Privacy violations

Civil rights organizations and privacy campaigners such as the Electronic Frontier Foundation, Big Brother Watch and the ACLU express concern that privacy is being compromised by the use of surveillance technologies. Face recognition can be used not just to identify an individual, but also to unearth other personal data associated with an individual – such as other photos featuring the individual, blog posts, social media profiles, Internet behavior, and travel patterns. Concerns have been raised over who would have access to the knowledge of one's whereabouts and people with them at any given time. Moreover, individuals have limited ability to avoid or thwart face recognition tracking unless they hide their faces. This fundamentally changes the dynamic of day-to-day privacy by enabling any marketer, government agency, or random stranger to secretly collect the identities and associated personal information of any individual captured by the face recognition system. Consumers may not understand or be aware of what their data is being used for, which denies them the ability to consent to how their personal information gets shared.

In July 2015, the United States Government Accountability Office conducted a Report to the Ranking Member, Subcommittee on Privacy, Technology and the Law, Committee on the Judiciary, U.S. Senate. The report discussed facial recognition technology's commercial uses, privacy issues, and the applicable federal law. It states that previously, issues concerning facial recognition technology were discussed and represent the need for updating the privacy laws of the United States so that federal law continually matches the impact of advanced technologies. The report noted that some industry, government, and private organizations were in the process of developing, or have developed, "voluntary privacy guidelines". These guidelines varied between the stakeholders, but their overall aim was to gain consent and inform citizens of the intended use of facial recognition technology. According to the report the voluntary privacy guidelines helped to counteract the privacy concerns that arise when citizens are unaware of how their personal data gets put to use.

In 2016, Russian company NtechLab caused a privacy scandal in the international media when it launched the FindFace face recognition system with the promise that Russian users could take photos of strangers in the street and link them to a social media profile on the social media platform Vkontakte (VK). In December 2017, Facebook rolled out a new feature that notifies a user when someone uploads a photo that includes what Facebook thinks is their face, even if they are not tagged. Facebook has attempted to frame the new functionality in a positive light, amidst prior backlashes. Facebook's head of privacy, Rob Sherman, addressed this new feature as one that gives people more control over their photos online. "We've thought about this as a really empowering feature," he says. "There may be photos that exist that you don't know about." Facebook's DeepFace has become the subject of several class action lawsuits under the Biometric Information Privacy Act, with claims alleging that Facebook is collecting and storing face recognition data of its users without obtaining informed consent, in direct violation of the 2008 Biometric Information Privacy Act (BIPA). The most recent case was dismissed in January 2016 because the court lacked jurisdiction. In the US, surveillance companies such as Clearview AI are relying on the First Amendment to the United States Constitution to data scrape user accounts on social media platforms for data that can be used in the development of facial recognition systems.

In 2019, the *Financial Times* first reported that facial recognition software was in use in the King's Cross area of London. The development around London's King's Cross mainline station includes shops, offices, Google's UK HQ and part of St Martin's College. According to the UK Information Commissioner's Office: "Scanning people's faces as they lawfully go about their daily lives, in order to identify them, is a potential threat to privacy that should concern us all." The UK Information Commissioner Elizabeth Denham launched an investigation into the use of the King's Cross facial recognition system, operated by the company Argent. In September 2019 it was announced by Argent that facial recognition software would no longer be used at King's Cross. Argent claimed that the software had been deployed between May 2016 and March 2018 on two cameras covering a pedestrian street running through the centre of the development. In October 2019, a report by the deputy London mayor Sophie Linden revealed that in a secret deal the Metropolitan Police had passed photos of seven people to Argent for use in their King's cross facial recognition system.

Automated Facial Recognition was trialled by the South Wales Police on multiple occasions between 2017 and 2019. The use of the technology was challenged in court by a private individual, Edward Bridges, with support from the charity Liberty (case known as R (Bridges) v Chief Constable South Wales Police). The case was heard in the Court of Appeal and a judgement was given in August 2020. The case argued that the use of Facial Recognition was a privacy violation on the basis that there was insufficient legal framework or proportionality in the use of Facial Recognition and that its use was in violation of the Data Protection Acts 1998 and 2018. The case was decided in favour of Bridges and did not award damages. The case was settled via a declaration of wrongdoing. In response to the case, the British Government has repeatedly attempted to pass a Bill regulating the use of Facial Recognition in public spaces. The proposed Bills have attempted to appoint a Commissioner with the ability to regulate Facial Recognition use by Government Services in a similar manner to the Commissioner for CCTV. Such a Bill has yet to come into force [correct as of September 2021].

In January 2023, New York Attorney General Letitia James asked for more information on the use of facial recognition technology from Madison Square Garden Entertainment following reports that the firm used it to block lawyers involved in litigation against the company from entering Madison Square Garden. She noted such a move would could go against federal, state, and local human rights laws.

### Imperfect technology in law enforcement

As of 2018, it is still contested as to whether or not facial recognition technology works less accurately on people of color. One study by Joy Buolamwini (MIT Media Lab) and Timnit Gebru (Microsoft Research) found that the error rate for gender recognition for women of color within three commercial facial recognition systems ranged from 23.8% to 36%, whereas for lighter-skinned men it was between 0.0 and 1.6%. Overall accuracy rates for identifying men (91.9%) were higher than for women (79.4%), and none of the systems accommodated a non-binary understanding of gender. It also showed that the datasets used to train commercial facial recognition models were unrepresentative of the broader population and skewed toward lighter-skinned males. However, another study showed that several commercial facial recognition software sold to law enforcement offices around the country had a lower false non-match rate for black people than for white people.

Experts fear that face recognition systems may actually be hurting citizens the police claims they are trying to protect. It is considered an imperfect biometric, and in a study conducted by Georgetown University researcher Clare Garvie, she concluded that "there's no consensus in the scientific community that it provides a positive identification of somebody." It is believed that with such large margins of error in this technology, both legal advocates and facial recognition software companies say that the technology should only supply a portion of the case – no evidence that can lead to an arrest of an individual. The lack of regulations holding facial recognition technology companies to requirements of racially biased testing can be a significant flaw in the adoption of use in law enforcement. CyberExtruder, a company that markets itself to law enforcement said that they had not performed testing or research on bias in their software. CyberExtruder did note that some skin colors are more difficult for the software to recognize with current limitations of the technology. "Just as individuals with very dark skin are hard to identify with high significance via facial recognition, individuals with very pale skin are the same," said Blake Senftner, a senior software engineer at CyberExtruder.

The United States' National Institute of Standards and Technology (NIST) carried out extensive testing of FRT system 1:1 verification and 1:many identification. It also tested for the differing accuracy of FRT across different demographic groups. The independent study concluded at present, no FRT system has 100% accuracy.

### Data protection

In 2010, Peru passed the Law for Personal Data Protection, which defines biometric information that can be used to identify an individual as sensitive data. In 2012, Colombia passed a comprehensive Data Protection Law which defines biometric data as sensitive information. According to Article 9(1) of the EU's 2016 General Data Protection Regulation (GDPR) the processing of biometric data for the purpose of "uniquely identifying a natural person" is sensitive and the facial recognition data processed in this way becomes sensitive personal data. In response to the GDPR passing into the law of EU member states, EU based researchers voiced concern that if they were required under the GDPR to obtain individual's consent for the processing of their facial recognition data, a face database on the scale of MegaFace could never be established again. In September 2019 the Swedish Data Protection Authority (DPA) issued its first ever financial penalty for a violation of the EU's General Data Protection Regulation (GDPR) against a school that was using the technology to replace time-consuming roll calls during class. The DPA found that the school illegally obtained the biometric data of its students without completing an impact assessment. In addition the school did not make the DPA aware of the pilot scheme. A 200,000 SEK fine (€19,000/$21,000) was issued.

In the United States of America several U.S. states have passed laws to protect the privacy of biometric data. Examples include the Illinois Biometric Information Privacy Act (BIPA) and the California Consumer Privacy Act (CCPA). In March 2020 California residents filed a class action against Clearview AI, alleging that the company had illegally collected biometric data online and with the help of face recognition technology built up a database of biometric data which was sold to companies and police forces. At the time Clearview AI already faced two lawsuits under BIPA and an investigation by the Privacy Commissioner of Canada for compliance with the Personal Information Protection and Electronic Documents Act (PIPEDA).


## Bans on the use of facial recognition technology

### United States of America

In May 2019, San Francisco, California became the first major United States city to ban the use of facial recognition software for police and other local government agencies' usage. San Francisco Supervisor, Aaron Peskin, introduced regulations that will require agencies to gain approval from the San Francisco Board of Supervisors to purchase surveillance technology. The regulations also require that agencies publicly disclose the intended use for new surveillance technology. In June 2019, Somerville, Massachusetts became the first city on the East Coast to ban face surveillance software for government use, specifically in police investigations and municipal surveillance. In July 2019, Oakland, California banned the usage of facial recognition technology by city departments.

The American Civil Liberties Union ("ACLU") has campaigned across the United States for transparency in surveillance technology and has supported both San Francisco and Somerville's ban on facial recognition software. The ACLU works to challenge the secrecy and surveillance with this technology.

During the George Floyd protests, use of facial recognition by city government was banned in Boston, Massachusetts. As of June 10, 2020, municipal use has been banned in:

- Berkeley, California
- Oakland, California
- Boston, Massachusetts – June 30, 2020
- Brookline, Massachusetts
- Cambridge, Massachusetts
- Northampton, Massachusetts
- Springfield, Massachusetts
- Somerville, Massachusetts
- Portland, Oregon – September 2020

The West Lafayette, Indiana City Council passed an ordinance banning facial recognition surveillance technology.

On October 27, 2020, 22 human rights groups called upon the University of Miami to ban facial recognition technology. This came after the students accused the school of using the software to identify student protesters. The allegations were, however, denied by the university.

A state police reform law in Massachusetts will take effect in July 2021; a ban passed by the legislature was rejected by governor Charlie Baker. Instead, the law requires a judicial warrant, limit the personnel who can perform the search, record data about how the technology is used, and create a commission to make recommendations about future regulations.

Reports in 2024 revealed that some police departments, including San Francisco Police Department, had skirted bans on facial recognition technology that had been enacted in their respective cities.

### European Union

In January 2020, the European Union suggested, but then quickly scrapped, a proposed moratorium on facial recognition in public spaces.

The European "Reclaim Your Face" coalition launched in October 2020. The coalition calls for a ban on facial recognition and launched a European Citizens' Initiative in February 2021. More than 60 organizations call on the European Commission to strictly regulate the use of biometric surveillance technologies.


## Emotion recognition

In the 18th and 19th century, the belief that facial expressions revealed the moral worth or true inner state of a human was widespread and physiognomy was a respected science in the Western world. From the early 19th century onwards photography was used in the physiognomic analysis of facial features and facial expression to detect insanity and dementia. In the 1960s and 1970s the study of human emotions and its expressions was reinvented by psychologists, who tried to define a normal range of emotional responses to events. The research on automated emotion recognition has since the 1970s focused on facial expressions and speech, which are regarded as the two most important ways in which humans communicate emotions to other humans. In the 1970s the Facial Action Coding System (FACS) categorization for the physical expression of emotions was established. Its developer Paul Ekman maintains that there are six emotions that are universal to all human beings and that these can be coded in facial expressions. Research into automatic emotion specific expression recognition has in the past decades focused on frontal view images of human faces. Facial thermography can be considered as a promising tool of emotion recognition.

In 2016, facial feature emotion recognition algorithms were among the new technologies, alongside high-definition CCTV, high resolution 3D face recognition and iris recognition, that found their way out of university research labs. In 2016, Facebook acquired FacioMetrics, a facial feature emotion recognition corporate spin-off by Carnegie Mellon University. In the same year Apple Inc. acquired the facial feature emotion recognition start-up Emotient. By the end of 2016, commercial vendors of facial recognition systems offered to integrate and deploy emotion recognition algorithms for facial features. The MIT's Media Lab spin-off Affectiva by late 2019 offered a facial expression emotion detection product that can recognize emotions in humans while driving.


## Anti-facial recognition systems

The development of anti-facial recognition technology is effectively an arms race between privacy researchers and big data companies. Big data companies increasingly use convolutional AI technology to create ever more advanced facial recognition models. Solutions to block facial recognition may not work on newer software, or on different types of facial recognition models. One popular cited example of facial-recognition blocking is the CVDazzle makeup and haircut system, but the creators note on their website that it has been outdated for quite some time as it was designed to combat a particular facial recognition algorithm and may not work. Another example is the emergence of facial recognition that can identify people wearing facemasks and sunglasses, especially after the COVID-19 pandemic.

Given that big data companies have much more funding than privacy researchers, it is very difficult for anti-facial recognition systems to keep up. There is also no guarantee that obfuscation techniques that were used for images taken in the past and stored, such as masks or software obfuscation, would protect users from facial-recognition analysis of those images by future technology.

In January 2013, Japanese researchers from the National Institute of Informatics created 'privacy visor' glasses that use nearly infrared light to make the face underneath it unrecognizable to face recognition software that use infrared. The latest version uses a titanium frame, light-reflective material and a mask which uses angles and patterns to disrupt facial recognition technology through both absorbing and bouncing back light sources. However, these methods are used to prevent infrared facial recognition and would not work on AI facial recognition of plain images. Some projects use adversarial machine learning to come up with new printed patterns that confuse existing face recognition software.

One method that may work to protect from facial recognition systems are specific haircuts and make-up patterns that prevent the used algorithms to detect a face, known as computer vision dazzle. Incidentally, the makeup styles popular with Juggalos may also protect against facial recognition.

Facial masks that are worn to protect from contagious viruses can reduce the accuracy of facial recognition systems. A 2020 NIST study, tested popular one-to-one matching systems and found a failure rate between five and fifty percent on masked individuals. *The Verge* speculated that the accuracy rate of mass surveillance systems, which were not included in the study, would be even less accurate than the accuracy of one-to-one matching systems. The facial recognition of Apple Pay can work through many barriers, including heavy makeup, thick beards and even sunglasses, but fails with masks. However, facial recognition of masked faces is increasingly getting more reliable.

Another solution is the application of obfuscation to images that may fool facial recognition systems while still appearing normal to a human user. These could be used for when images are posted online or on social media. However, as it is hard to remove images once they are on the internet, the obfuscation on these images may be defeated and the face of the user identified by future advances in technology. Two examples of this technique, developed in 2020, are the ANU's 'Camera Adversaria' camera app, and the University of Chicago's Fawkes image cloaking software algorithm which applies obfuscation to already taken photos. However, by 2021 the Fawkes obfuscation algorithm had already been specifically targeted by Microsoft Azure which changed its algorithm to lower Fawkes' effectiveness.
