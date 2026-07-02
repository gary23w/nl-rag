---
title: "Spreadsheet (part 2/2)"
source: https://en.wikipedia.org/wiki/Spreadsheet
domain: openpyxl-excel
license: CC-BY-SA-4.0
tags: python openpyxl, openpyxl excel, xlsx spreadsheet python
fetched: 2026-07-02
part: 2/2
---

## Shortcomings

While spreadsheets represented a major step forward in quantitative modeling, they have deficiencies. Their shortcomings include the perceived unfriendliness of alpha-numeric cell addresses.

- Research by ClusterSeven has shown huge discrepancies in the way financial institutions and corporate entities understand, manage and police their often vast estates of spreadsheets and unstructured financial data (including comma-separated values (CSV) files and Microsoft Access databases). One study in early 2011 of nearly 1,500 people in the UK found that 57% of spreadsheet users have never received formal training on the spreadsheet package they use. 72% said that no internal department checks their spreadsheets for accuracy. Only 13% said that Internal Audit reviews their spreadsheets, while a mere 1% receive checks from their risk department.

- Spreadsheets can have reliability problems. Research studies estimate that around 1% of all formulas in operational spreadsheets are in error.

Despite the high error risks often associated with spreadsheet authorship and use, specific steps can be taken to significantly enhance control and reliability by structurally reducing the likelihood of error occurrence at their source.

- The practical expressiveness of spreadsheets can be limited unless their modern features are used. Several factors contribute to this limitation. Implementing a complex model on a cell-at-a-time basis requires tedious attention to detail. Authors have difficulty remembering the meanings of hundreds or thousands of cell addresses that appear in formulas.

These drawbacks are mitigated by the use of named variables for cell designations, and employing variables in formulas rather than cell locations and cell-by-cell manipulations. Graphs can be used to show instantly how results are changed by changes in parameter values. The spreadsheet can be made invisible except for a transparent user interface that requests pertinent input from the user, displays results requested by the user, creates reports, and has built-in error traps to prompt correct input.

- Similarly, formulas expressed in terms of cell addresses are hard to keep straight and hard to audit. Research shows that spreadsheet auditors who check numerical results and cell formulas find no more errors than auditors who only check numerical results. That is another reason to use named variables and formulas employing named variables.

Specifically, spreadsheets typically contain many copies of the same formula. When the formula is modified, the user has to change every cell containing that formula. In contrast, most computer languages allow a formula to appear only once in the code and achieve repetition using loops: making them much easier to implement and audit.

- The alteration of a dimension demands major surgery. When rows (or columns) are added to or deleted from a table, one has to adjust the size of many downstream tables that depend on the table being changed. In the process, it is often necessary to move other cells around to make room for the new columns or rows and to adjust graph data sources. In large spreadsheets, this can be extremely time-consuming.
- Adding or removing a dimension is so difficult, one generally has to start over. The spreadsheet as a paradigm forces one to decide on dimensionality right of the beginning of one's spreadsheet creation, even though it is often most natural to make these choices after one's spreadsheet model has matured. The desire to add and remove dimensions also arises in parametric and sensitivity analyses.
- Collaboration in authoring spreadsheet formulas can be difficult when such collaboration occurs at the level of cells and cell addresses.

Other problems associated with spreadsheets include:

- Some sources advocate the use of specialized software instead of spreadsheets for some applications (budgeting, statistics)
- The Microsoft xls file format which is the default file format used in versions prior to 2007 had a capacity limit of 65,536 rows by 256 columns (216 and 28 respectively). This presents a problem for people using larger datasets, and can result in data loss. In spite of the time passed, a recent example is the loss of COVID-19 positives in the British statistics for September and October 2020 when the Microsoft xls file format had been used in a legacy computer system.
- Lack of auditing and revision control. This makes it difficult to determine who changed what and when. This can cause problems with regulatory compliance. Lack of revision control greatly increases the risk of errors due to the inability to track, isolate and test changes made to a document. Modern spreadsheets include revision control.
- Lack of security. Spreadsheets lack controls on who can see and modify particular data. This, combined with the lack of auditing above, can make it easy for someone to commit fraud.
- Because they are loosely structured, it is easy for someone to introduce an error, either accidentally or intentionally, by entering information in the wrong place or expressing dependencies among cells (such as in a formula) incorrectly.
- The results of a formula (example "=A1*B1") applies only to a single cell (that is, the cell the formula is located in—in this case perhaps C1), even though it can "extract" data from many other cells, and even real-time dates and actual times. This means that to cause a similar calculation on an array of cells, an almost identical formula (but residing in its own "output" cell) must be repeated for each row of the "input" array. This differs from a "formula" in a conventional computer program, which typically makes one calculation that it applies to all the input in turn. With current spreadsheets, this forced repetition of near-identical formulas can have detrimental consequences from a quality assurance standpoint and is often the cause of many spreadsheet errors. Some spreadsheets have array formulas to address this issue.
- Trying to manage the sheer volume of spreadsheets that may exist in an organization without proper security, audit trails, the unintentional introduction of errors, and other items listed above can become overwhelming.

While there are built-in and third-party tools for desktop spreadsheet applications that address some of these shortcomings, awareness, and use of these is generally low. Many professionals in the financial field "don't know" how their spreadsheets are audited; only 6% invest in a third-party solution.


## Spreadsheet risk

Spreadsheet risk is the risk associated with deriving a materially incorrect value from a spreadsheet application that will be utilized in making a related (usually numerically based) decision. Examples include the valuation of an asset, the determination of financial accounts, the calculation of medicinal doses, or the size of a load-bearing beam for structural engineering. The risk may arise from inputting erroneous or fraudulent data values, from mistakes (or incorrect changes) within the logic of the spreadsheet or the omission of relevant updates (e.g., out of date exchange rates). Some single-instance errors have exceeded US$1 billion. Because spreadsheet risk is principally linked to the actions (or inaction) of individuals it is defined as a sub-category of operational risk.

Despite this, research carried out by ClusterSeven revealed that around half (48%) of c-level executives and senior managers at firms reporting annual revenues over £50m said there were either no usage controls at all or poorly applied manual processes over the use of spreadsheets at the firms.

In 2013 Thomas Herndon, a graduate student of economics at the University of Massachusetts Amherst, found major coding flaws in the spreadsheet used by the economists Carmen Reinhart and Kenneth Rogoff in *Growth in a Time of Debt*, a very influential 2010 journal article which was widely used as justification to drive 2010–2013 European austerity programs.
