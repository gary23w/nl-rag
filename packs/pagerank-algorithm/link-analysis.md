---
title: "Link analysis"
source: https://en.wikipedia.org/wiki/Link_analysis
domain: pagerank-algorithm
license: CC-BY-SA-4.0
tags: pagerank algorithm, link analysis, power iteration, markov chain
fetched: 2026-07-02
---

# Link analysis

In network theory, **link analysis** is a data-analysis technique used to evaluate relationships between nodes. Relationships may be identified among various types of nodes, including organizations, people and transactions. Link analysis has been used for investigation of criminal activity (fraud, counterterrorism, and intelligence), computer security analysis, search engine optimization, market research, medical research, and art.

## Knowledge discovery

Knowledge discovery is an iterative and interactive process used to identify, analyze and visualize patterns in data. Network analysis, link analysis and social network analysis are all methods of knowledge discovery, each a corresponding subset of the prior method. Most knowledge discovery methods follow these steps (at the highest level):

1. Data processing
2. Transformation
3. Analysis
4. Visualization

Data gathering and processing requires access to data and has several inherent issues, including information overload and data errors. Once data is collected, it will need to be transformed into a format that can be effectively used by both human and computer analyzers. Manual or computer-generated visualizations tools may be mapped from the data, including network charts. Several algorithms exist to help with analysis of data – Dijkstra's algorithm, breadth-first search, and depth-first search.

Link analysis focuses on analysis of relationships among nodes through visualization methods (network charts, association matrix). Here is an example of the relationships that may be mapped for crime investigations:

| Relationship/Network | Data Sources |
|---|---|
| 1. Trust | Prior contacts in family, neighborhood, school, military, club or organization. Public and court records. Data may only be available in suspect's native country. |
| 2. Task | Logs and records of phone calls, electronic mail, chat rooms, instant messages, Web site visits. Travel records. Human intelligence: observation of meetings and attendance at common events. |
| 3. Money & Resources | Bank account and money transfer records. Pattern and location of credit card use. Prior court records. Human intelligence: observation of visits to alternate banking resources such as Hawala. |
| 4. Strategy & Goals | Web sites. Videos and encrypted disks delivered by courier. Travel records. Human intelligence: observation of meetings and attendance at common events. |

Link analysis is used for 3 primary purposes:

1. Find matches in data for known patterns of interest;
2. Find anomalies where known patterns are violated;
3. Discover new patterns of interest (social network analysis, data mining).

## History

Klerks categorized link analysis tools into 3 generations. The first generation was introduced in 1975 as the Anacpapa Chart of Harper and Harris. This method requires that a domain expert review data files, identify associations by constructing an association matrix, create a link chart for visualization and finally analyze the network chart to identify patterns of interest. This method requires extensive domain knowledge and is extremely time-consuming when reviewing vast amounts of data.

In addition to the association matrix, the activities matrix can be used to produce actionable information, which has practical value and use to law-enforcement. The activities matrix, as the term might imply, centers on the actions and activities of people with respect to locations. Whereas the association matrix focuses on the relationships between people, organizations, and/or properties. The distinction between these two types of matrices, while minor, is nonetheless significant in terms of the output of the analysis completed or rendered.

Second generation tools consist of automatic graphics-based analysis tools such as IBM i2 Analyst's Notebook, Netmap, ClueMaker and Watson. These tools offer the ability to automate the construction and updates of the link chart once an association matrix is manually created, however, analysis of the resulting charts and graphs still requires an expert with extensive domain knowledge.

The third generation of link-analysis tools like DataWalk allow the automatic visualization of linkages between elements in a data set, that can then serve as the canvas for further exploration or manual updates.

## Applications

- FBI Violent Criminal Apprehension Program (ViCAP)
- Iowa State Sex Crimes Analysis System
- Minnesota State Sex Crimes Analysis System (MIN/SCAP)
- Washington State Homicide Investigation Tracking System (HITS)
- New York State Homicide Investigation & Lead Tracking (HALT)
- New Jersey Homicide Evaluation & Assessment Tracking (HEAT)
- Pennsylvania State ATAC Program.
- Violent Crime Linkage Analysis System (ViCLAS)

## Issues with link analysis

### Information overload

With the vast amounts of data and information that are stored electronically, users are confronted with multiple unrelated sources of information available for analysis. Data analysis techniques are required to make effective and efficient use of the data. Palshikar classifies data analysis techniques into two categories – (statistical models, time-series analysis, clustering and classification, matching algorithms to detect anomalies) and artificial intelligence (AI) techniques (data mining, expert systems, pattern recognition, machine learning techniques, neural networks).

Bolton & Hand define statistical data analysis as either supervised or unsupervised methods. Supervised learning methods require that rules are defined within the system to establish what is expected or unexpected behavior. Unsupervised learning methods review data in comparison to the norm and detect statistical outliers. Supervised learning methods are limited in the scenarios that can be handled as this method requires that training rules are established based on previous patterns. Unsupervised learning methods can provide detection of broader issues, however, may result in a higher false-positive ratio if the behavioral norm is not well established or understood.

Data itself has inherent issues including integrity (or lack of) and continuous changes. Data may contain "errors of omission and commission because of faulty collection or handling, and when entities are actively attempting to deceive and/or conceal their actions". Sparrow highlights incompleteness (inevitability of missing data or links), fuzzy boundaries (subjectivity in deciding what to include) and dynamic changes (recognition that data is ever-changing) as the three primary problems with data analysis.

Once data is transformed into a usable format, open texture and cross referencing issues may arise. Open texture was defined by Waismann as the unavoidable uncertainty in meaning when empirical terms are used in different contexts. Uncertainty in meaning of terms presents problems when attempting to search and cross reference data from multiple sources.

The primary method for resolving data analysis issues is reliance on domain knowledge from an expert. This is a very time-consuming and costly method of conducting link analysis and has inherent problems of its own. McGrath et al. conclude that the layout and presentation of a network diagram have a significant impact on the user's "perceptions of the existence of groups in networks". Even using domain experts may result in differing conclusions as analysis may be subjective.

### Prosecution vs. crime prevention

Link analysis techniques have primarily been used for prosecution, as it is far easier to review historical data for patterns than it is to attempt to predict future actions.

Krebs demonstrated the use of an association matrix and link chart of the terrorist network associated with the 19 hijackers responsible for the September 11th attacks by mapping publicly available details made available following the attacks. Even with the advantages of hindsight and publicly available information on people, places and transactions, it is clear that there is missing data.

Alternatively, Picarelli argued that use of link analysis techniques could have been used to identify and potentially prevent illicit activities within the Aum Shinrikyo network. "We must be careful of 'guilt by association'. Being linked to a terrorist does not prove guilt – but it does invite investigation." Balancing the legal concepts of probable cause, right to privacy and freedom of association become challenging when reviewing potentially sensitive data with the objective to prevent crime or illegal activity that has not yet occurred.

## Proposed solutions

There are four categories of proposed link analysis solutions:

1. Heuristic-based
2. Template-based
3. Similarity-based
4. Statistical

Heuristic-based tools utilize decision rules that are distilled from expert knowledge using structured data. Template-based tools employ Natural Language Processing (NLP) to extract details from unstructured data that are matched to pre-defined templates. Similarity-based approaches use weighted scoring to compare attributes and identify potential links. Statistical approaches identify potential links based on lexical statistics.

### CrimeNet explorer

J.J. Xu and H. Chen propose a framework for automated network analysis and visualization called CrimeNet Explorer. This framework includes the following elements:

- Network Creation through a concept space approach that uses "co-occurrence weight to measure the frequency with which two words or phrases appear in the same document. The more frequently two words or phrases appear together, the more likely it will be that they are related".
- Network Partition using "hierarchical clustering to partition a network into subgroups based on relational strength".
- Structural Analysis through "three centrality measures (degree, betweenness, and closeness) to identify central members in a given subgroup. CrimeNet Explorer employed Dijkstra's shortest-path algorithm to calculate the betweenness and closeness from a single node to all other nodes in the subgroup.
- Network Visualization using Torgerson's metric multidimensional scaling (MDS) algorithm.
