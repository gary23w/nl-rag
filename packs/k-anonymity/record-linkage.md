---
title: "Record linkage"
source: https://en.wikipedia.org/wiki/Record_linkage
domain: k-anonymity
license: CC-BY-SA-4.0
tags: k anonymity, l diversity, t closeness, quasi identifier, data re identification
fetched: 2026-07-02
---

# Record linkage

**Record linkage** (also known as **data matching**, **data linkage**, **entity resolution**, and many other terms) is the task of finding records in a data set that refer to the same entity across different data sources (e.g., data files, books, websites, and databases). Record linkage is necessary when joining different data sets based on entities that may or may not share a common identifier (e.g., database key, URI, National identification number), which may be due to differences in record shape, storage location, or curator style or preference. A data set that has undergone RL-oriented reconciliation may be referred to as being *cross-linked*.

## Naming conventions

"Record linkage" is the term used by statisticians, epidemiologists, and historians, among others, to describe the process of joining records from one data source with another that describe the same entity. However, many other terms are used for this process. Unfortunately, this profusion of terminology has led to few cross-references between these research communities.

Computer scientists often refer to it as "data matching" or as the "object identity problem". Commercial mail and database applications refer to it as "merge/purge processing" or "list washing". Other names used to describe the same concept include: "coreference/entity/identity/name/record resolution", "entity disambiguation/linking", "fuzzy matching", "duplicate detection", "deduplication", "record matching", "(reference) reconciliation", "object identification", "data/information integration" and "conflation".

While they share similar names, record linkage and linked data are two separate approaches to processing and structuring data. Although both involve identifying matching entities across different data sets, record linkage standardly equates "entities" with human individuals; by contrast, Linked Data is based on the possibility of interlinking any web resource across data sets, using a correspondingly broader concept of identifier, namely a URI.

## History

The initial idea of record linkage goes back to Halbert L. Dunn in his 1946 article titled "Record Linkage" published in the *American Journal of Public Health*.

Howard Borden Newcombe then laid the probabilistic foundations of modern record linkage theory in a 1959 article in *Science*. These were formalized in 1969 by Ivan Fellegi and Alan Sunter, in their pioneering work "A Theory For Record Linkage", where they proved that the probabilistic decision rule they described was optimal when the comparison attributes were conditionally independent. In their work they recognized the growing interest in applying advances in computing and automation to large collections of administrative data, and the *Fellegi-Sunter theory* remains the mathematical foundation for many record linkage applications.

Since the late 1990s, various machine learning techniques have been developed that can, under favorable conditions, be used to estimate the conditional probabilities required by the Fellegi-Sunter theory. Several researchers have reported that the conditional independence assumption of the Fellegi-Sunter algorithm is often violated in practice; however, published efforts to explicitly model the conditional dependencies among the comparison attributes have not resulted in an improvement in record linkage quality. On the other hand, machine learning or neural network algorithms that do not rely on these assumptions often provide far higher accuracy, when sufficient labeled training data is available.

Record linkage can be done entirely without the aid of a computer, but the primary reasons computers are often used to complete record linkages are to reduce or eliminate manual review and to make results more easily reproducible. Computer matching has the advantages of allowing central supervision of processing, better quality control, speed, consistency, and better reproducibility of results.

## Methods

### Data preprocessing

Record linkage is highly sensitive to the quality of the data being linked, so all data sets under consideration (particularly their key identifier fields) should ideally undergo a data quality assessment before record linkage. Many key identifiers for the same entity can be presented quite differently between (and even within) data sets, which can greatly complicate record linkage unless understood ahead of time. For example, key identifiers for a man named William J. Smith might appear in three different data sets as follows:

| Data set | Name | Date of birth | City of residence |
|---|---|---|---|
| Data set 1 | William J. Smith | 1/2/73 | Berkeley, California |
| Data set 2 | Smith, W. J. | 1973.1.2 | Berkeley, CA |
| Data set 3 | Bill Smith | Jan 2, 1973 | Berkeley, Calif. |

In this example, the different formatting styles lead to records that look different but in fact all refer to the same entity with the same logical identifier values. Most, if not all, record linkage strategies would result in more accurate linkage if these values were first *normalized* or *standardized* into a consistent format (e.g., all names are "Surname, Given name", and all dates are "YYYY/MM/DD"). Standardization can be accomplished through simple rule-based data transformations or more complex procedures such as lexicon-based tokenization and probabilistic hidden Markov models. Several of the packages listed in the *Software Implementations* section provide some of these features to simplify the process of data standardization.

### Entity resolution

**Entity resolution** is an operational intelligence process, typically powered by an entity resolution engine or middleware, whereby organizations can connect disparate data sources with a view to understand possible entity matches and non-obvious relationships across multiple data silos. It analyzes all of the information relating to individuals and/or entities from multiple sources of data, and then applies likelihood and probability scoring to determine which identities are a match and what, if any, non-obvious relationships exist between those identities.

Entity resolution engines are typically used to uncover risk, fraud, and conflicts of interest, but are also useful tools for use within customer data integration (CDI) and master data management (MDM) requirements. Typical uses for entity resolution engines include terrorist screening, insurance fraud detection, USA Patriot Act compliance, organized retail crime ring detection and applicant screening.

For example, across different data silos – employee records, vendor data, watch lists, etc. – an organization may have several variations of an entity named ABC, which may or may not be the same individual. These entries may, in fact, appear as ABC1, ABC2, or ABC3 within those data sources. By comparing similarities between underlying attributes such as address, date of birth, or social security number, the user can eliminate some possible matches and confirm others as very likely matches.

Entity resolution engines then apply rules, based on common sense logic, to identify hidden relationships across the data. In the example above, perhaps ABC1 and ABC2 are not the same individual, but rather two distinct people who share common attributes such as address or phone number.

#### Data matching

While entity resolution solutions include data matching technology, many data matching offerings do not fit the definition of entity resolution. Here are four factors that distinguish entity resolution from data matching, according to John Talburt, director of the UALR Center for Advanced Research in Entity Resolution and Information Quality:

- Works with both structured and unstructured records, and it entails the process of extracting references when the sources are unstructured or semi-structured
- Uses elaborate business rules and concept models to deal with missing, conflicting, and corrupted information
- Utilizes non-matching, asserted linking (associate) information in addition to direct matching
- Uncovers non-obvious relationships and association networks (i.e. who's associated with whom)

In contrast to data quality products, more powerful identity resolution engines also include a rules engine and workflow process, which apply business intelligence to the resolved identities and their relationships. These advanced technologies make automated decisions and impact business processes in real time, limiting the need for human intervention.

### Deterministic record linkage

The simplest kind of record linkage, called *deterministic* or *rules-based record linkage*, generates links based on the number of individual identifiers that match among the available data sets. Two records are said to match via a deterministic record linkage procedure if all or some identifiers (above a certain threshold) are identical. Deterministic record linkage is a good option when the entities in the data sets are identified by a common identifier, or when there are several representative identifiers (e.g., name, date of birth, and sex when identifying a person) whose quality of data is relatively high.

As an example, consider two standardized data sets, Set A and Set B, that contain different bits of information about patients in a hospital system. The two data sets identify patients using a variety of identifiers: Social Security Number (SSN), name, date of birth (DOB), sex, and ZIP code (ZIP). The records in two data sets (identified by the "#" column) are shown below:

| Data Set | # | SSN | Name | DOB | Sex | ZIP |
|---|---|---|---|---|---|---|
| Set A | 1 | 000956723 | Smith, William | 1973/01/02 | Male | 94701 |
| 2 | 000956723 | Smith, William | 1973/01/02 | Male | 94703 |   |
| 3 | 000005555 | Jones, Robert | 1942/08/14 | Male | 94701 |   |
| 4 | 123001234 | Sue, Mary | 1972/11/19 | Female | 94109 |   |
| Set B | 1 | 000005555 | Jones, Bob | 1942/08/14 |   |   |
| 2 |   | Smith, Bill | 1973/01/02 | Male | 94701 |   |

The most simple deterministic record linkage strategy would be to pick a single identifier that is assumed to be uniquely identifying, say SSN, and declare that records sharing the same value identify the same person while records not sharing the same value identify different people. In this example, deterministic linkage based on SSN would create entities based on A1 and A2; A3 and B1; and A4. While A1, A2, and B2 appear to represent the same entity, B2 would not be included in the match because it is missing a value for SSN.

Handling exceptions such as missing identifiers involves the creation of additional record linkage rules. One such rule in the case of a missing SSN might be to compare name, date of birth, sex, and ZIP code with other records in hopes of finding a match. In the above example, this rule would still not match A1/A2 with B2 because the names are still slightly different: standardization put the names into the proper (Surname, Given name) format but could not discern "Bill" as a nickname for "William". Running names through a phonetic algorithm such as Soundex, NYSIIS, or metaphone can help to resolve these types of problems. However, they may still stumble over surname changes as a result of marriage or divorce, but then B2 would be matched only with A1 since the ZIP code in A2 is different. Thus, another rule would need to be created to determine whether differences in particular identifiers are acceptable (such as ZIP code) and which are not (such as date of birth).

As this example demonstrates, even a small decrease in data quality or a small increase in the complexity of the data can result in a very large increase in the number of rules necessary to link records properly. Eventually, these linkage rules will become too numerous and interrelated to build without the aid of specialized software tools. In addition, linkage rules are often specific to the nature of the data sets they are designed to link together. One study was able to link the Social Security Death Master File with two hospital registries from the Midwestern United States using SSN, NYSIIS-encoded first name, birth month, and sex, but these rules may not work as well with data sets from other geographic regions or with data collected on younger populations. Thus, continuous maintenance testing of these rules is necessary to ensure they continue to function as expected as new data enter the system and need to be linked. New data that exhibit different characteristics than were initially expected could require a complete rebuilding of the record linkage rule set, which could be a very time-consuming and expensive endeavor.

### Probabilistic record linkage

*Probabilistic record linkage*, sometimes called *fuzzy matching* (also *probabilistic merging* or *fuzzy merging* in the context of merging of databases), takes a different approach to the record linkage problem by taking into account a wider range of potential identifiers, computing weights for each identifier based on its estimated ability to correctly identify a match or a non-match, and using these weights to calculate the probability that two given records refer to the same entity. Record pairs with probabilities above a certain threshold are considered to be matches, while pairs with probabilities below another threshold are considered to be non-matches; pairs that fall between these two thresholds are considered to be "possible matches" and can be dealt with accordingly (e.g., human reviewed, linked, or not linked, depending on the requirements). Whereas deterministic record linkage requires a series of potentially complex rules to be programmed ahead of time, probabilistic record linkage methods can be "trained" to perform well with much less human intervention.

Many probabilistic record linkage algorithms assign match/non-match weights to identifiers by means of two probabilities called u and m . The u probability is the probability that an identifier in two *non-matching* records will agree purely by chance. For example, the u probability for birth month (where twelve values are approximately uniformly distributed) is $1/12\approx 0.083$ ; identifiers with values that are not uniformly distributed will have different u probabilities for different values (possibly including missing values). The m probability is the probability that an identifier in *matching* pairs will agree (or be sufficiently similar, such as strings with low Jaro-Winkler or Levenshtein distance). This value would be $1.0$ in the case of perfect data, but given that this is rarely (if ever) true, it can instead be estimated. This estimation may be done based on prior knowledge of the data sets, by manually identifying a large number of matching and non-matching pairs to "train" the probabilistic record linkage algorithm, or by iteratively running the algorithm to obtain closer estimations of the m probability. If a value of $0.95$ were to be estimated for the m probability, then the match/non-match weights for the birth month identifier would be:

| Outcome | Proportion of links | Proportion of non-links | Frequency ratio | Weight |
|---|---|---|---|---|
| Match | $m=0.95$ | $u\approx 0.083$ | $m/u\approx 11.4$ | $\log _{2}{m/u}\approx 3.51$ |
| Non-match | $1-m=0.05$ | $1-u\approx 0.917$ | $(1-m)/(1-u)\approx 0.0545$ | $\log _{2}{(1-m)/(1-u)}\approx -4.20$ |

The same calculations would be done for all other identifiers under consideration to find their match/non-match weights. Then, every identifier of one record would be compared with the corresponding identifier of another record to compute the total weight of the pair: the *match* weight is added to the running total whenever a pair of identifiers agree, while the *non-match* weight is added (i.e. the running total decreases) whenever the pair of identifiers disagrees. The resulting total weight is then compared to the aforementioned thresholds to determine whether the pair should be linked, non-linked, or set aside for special consideration (e.g. manual validation).

#### Blocking

Determining where to set the match/non-match thresholds is a balancing act between obtaining an acceptable sensitivity (or *recall*, the proportion of truly matching records that are linked by the algorithm) and positive predictive value (or *precision*, the proportion of records linked by the algorithm that truly do match). Various manual and automated methods are available to predict the best thresholds, and some record linkage software packages have built-in tools to help the user find the most acceptable values. Because this can be a very computationally demanding task, particularly for large data sets, a technique known as *blocking* is often used to improve efficiency. Blocking attempts to restrict comparisons to just those records for which one or more particularly discriminating identifiers agree, which has the effect of increasing the positive predictive value (precision) at the expense of sensitivity (recall). For example, blocking based on a phonetically coded surname and ZIP code would reduce the total number of comparisons required and would improve the chances that linked records would be correct (since two identifiers already agree), but would potentially miss records referring to the same person whose surname or ZIP code was different (due to marriage or relocation, for instance). Blocking based on birth month, a more stable identifier that would be expected to change only in the case of data error, would provide a more modest gain in positive predictive value and loss in sensitivity, but would create only twelve distinct groups which, for extremely large data sets, may not provide much net improvement in computation speed. Thus, robust record linkage systems often use multiple blocking passes to group data in various ways in order to come up with groups of records that should be compared to each other.

### Machine learning

In recent years, a variety of machine learning techniques have been used in record linkage. It has been recognized that the classic Fellegi-Sunter algorithm for probabilistic record linkage outlined above is equivalent to the Naive Bayes algorithm in the field of machine learning, and suffers from the same assumption of the independence of its features (an assumption that is typically not true). Higher accuracy can often be achieved by using various other machine learning techniques, including a single-layer perceptron, random forest, and SVM. In conjunction with distributed technologies, accuracy and scale for record linkage can be improved further.

### Human-machine hybrid record linkage

High quality record linkage often requires a human–machine hybrid system to safely manage uncertainty in the ever changing streams of chaotic big data. Recognizing that linkage errors propagate into the linked data and its analysis, interactive record linkage systems have been proposed. Interactive record linkage is defined as people iteratively fine-tuning the results from the automated methods and managing the uncertainty and its propagation to subsequent analyses. The main objectives of interactive record linkage systems is to manually resolve uncertain linkages and validate the results until it is at acceptable levels for the given application. Variations of interactive record linkage that enhance privacy during the human interaction steps have also been proposed.

### Privacy-preserving record linkage

Record linkage is increasingly required across databases held by different organisations, where the complementary data held by these organisations can, for example, help to identify patients who are susceptible to certain adverse drug reactions (linking hospital, doctor, and pharmacy databases). In many such applications, however, the databases to be linked contain sensitive information about people which cannot be shared between the organisations.

Privacy-preserving record linkage (PPRL) methods have been developed to link databases without the need to share the original sensitive values between the organisations that participate in a linkage. In PPRL, generally the attribute values of records to be compared are encoded or encrypted in some form. A popular such encoding technique used are Bloom filter, which allows approximate similarities to be calculated between encoded values without the need for sharing the corresponding sensitive plain-text values. At the end of the PPRL process only limited information about the record pairs classified as matches is revealed to the organisations that participate in the linkage process. The techniques used in PPRL must guarantee that no participating organisation, nor any external adversary, can compromise the privacy of the entities that are represented by records in the databases being linked.

## Mathematical model

In an application with two files, A and B, denote the rows (*records*) by $\alpha (a)$ in file A and $\beta (b)$ in file B. Assign K *characteristics* to each record. The set of records that represent identical entities is defined by

$M=\left\{(a,b);a=b;a\in A;b\in B\right\}$

and the complement of set M , namely set U representing different entities is defined as

$U=\{(a,b);a\neq b;a\in A;b\in B\}$ .

A vector, $\gamma$ is defined that contains the coded agreements and disagreements on each characteristic:

$\gamma \left[\alpha (a),\beta (b)\right]=\{\gamma ^{1}\left[\alpha (a),\beta (b)\right],...,\gamma ^{K}\left[\alpha (a),\beta (b)\right]\}$

where K is a subscript for the characteristics (sex, age, marital status, etc.) in the files. The conditional probabilities of observing a specific vector $\gamma$ given $(a,b)\in M$ , $(a,b)\in U$ are defined as

$m(\gamma )=P\left\{\gamma \left[\alpha (a),\beta (b)\right]|(a,b)\in M\right\}=\sum _{(a,b)\in M}P\left\{\gamma \left[\alpha (a),\beta (b)\right]\right\}\cdot P\left[(a,b)|M\right]$

and

$u(\gamma )=P\left\{\gamma \left[\alpha (a),\beta (b)\right]|(a,b)\in U\right\}=\sum _{(a,b)\in U}P\left\{\gamma \left[\alpha (a),\beta (b)\right]\right\}\cdot P\left[(a,b)|U\right],$ respectively.

## Applications

### Master data management

Most Master data management (MDM) products use a record linkage process to identify records from different sources representing the same real-world entity. This linkage is used to create a "golden master record" containing the cleaned, reconciled data about the entity. The techniques used in MDM are the same as for record linkage generally. MDM expands this matching not only to create a "golden master record" but also to infer relationships. (i.e. a person has the same/similar surname and same/similar address, this might imply they share a household relationship).

### Data warehousing and business intelligence

Record linkage plays a key role in data warehousing and business intelligence. Data warehouses serve to combine data from many different operational source systems into one logical data model, which can then be subsequently fed into a business intelligence system for reporting and analytics. Each operational source system may have its own method of identifying the same entities used in the logical data model, so record linkage between the different sources becomes necessary to ensure that the information about a particular entity in one source system can be seamlessly compared with information about the same entity from another source system. Data standardization and subsequent record linkage often occur in the "transform" portion of the extract, transform, load (ETL) process.

### Historical research

Record linkage is important to social history research since most data sets, such as census records and parish registers were recorded long before the invention of National identification numbers. When old sources are digitized, linking of data sets is a prerequisite for longitudinal study. This process is often further complicated by a lack of standard spelling of names, family names that change according to place of dwelling, changing of administrative boundaries, and problems of checking the data against other sources. Record linkage was among the most prominent themes in the History and computing field in the 1980s, but has since been subject to less attention in research.

### Medical practice and research

Record linkage is an important tool in creating data required for examining the health of the public and of the health care system itself. It can be used to improve data holdings, data collection, quality assessment, and the dissemination of information. Data sources can be examined to eliminate duplicate records, to identify under-reporting and missing cases (e.g., census population counts), to create person-oriented health statistics, and to generate disease registries and health surveillance systems. Some cancer registries link various data sources (e.g., hospital admissions, pathology and clinical reports, and death registrations) to generate their registries. Record linkage is also used to create health indicators. For example, fetal and infant mortality is a general indicator of a country's socioeconomic development, public health, and maternal and child services. If infant death records are matched to birth records, it is possible to use birth variables, such as birth weight and gestational age, along with mortality data, such as cause of death, in analyzing the data. Linkages can help in follow-up studies of cohorts or other groups to determine factors such as vital status, residential status, or health outcomes. Tracing is often needed for follow-up of industrial cohorts, clinical trials, and longitudinal surveys to obtain the cause of death and/or cancer. An example of a successful and long-standing record linkage system allowing for population-based medical research is the Rochester Epidemiology Project based in Rochester, Minnesota.

## Criticism of existing software implementations

The main reasons cited are:

- **Project costs**: costs typically in the hundreds of thousands of dollars
- **Time**: lack of enough time to deal with large-scale data cleansing software
- **Security**: concerns over sharing information, giving an application access across systems, and effects on legacy systems
- **Scalability**: Due to the absence of unique identifiers in records, record linkage is computationally expensive and difficult to scale.
- **Accuracy**: Changing business data and capturing all rules for linking is a tough and extensive exercise
