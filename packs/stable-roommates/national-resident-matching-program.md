---
title: "National Resident Matching Program"
source: https://en.wikipedia.org/wiki/National_Resident_Matching_Program
domain: stable-roommates
license: CC-BY-SA-4.0
tags: stable roommates problem, irving algorithm, stable matching, preference list
fetched: 2026-07-02
---

# National Resident Matching Program

The **National Resident Matching Program** (**NRMP**), also called **The Match**, is a United States–based private non-profit non-governmental organization created in 1952 to place U.S. medical school students into residency training programs located in United States teaching hospitals. Its mission has since expanded to include the placement of U.S. citizen and non-U.S. citizen international medical school students and graduates into residency and fellowship training programs. In addition to the annual Main Residency Match that in 2021 encompassed more than 48,000 applicants and 38,000 positions, the NRMP conducts Fellowship Matches for more than 60 subspecialties through its Specialties Matching Service (SMS). The NRMP is sponsored by a board of directors that includes medical school deans, teaching hospital executives, graduate medical education program directors, medical students and residents, and one public member.

NRMP International, a subsidiary of the National Resident Matching Program, was established in 2010 to provide medical matching services outside the United States and Canada.

## History

From shortly after the first residency programs were formally introduced in the 1920s, the hiring process was "characterized by intense competition among hospitals for (an inadequate supply) of interns." In general, hospitals benefited from filling their positions as early as possible, and applicants benefited from delaying acceptance of positions. The combination of those factors led to offers being made for positions up to two years in advance of the start of postgraduate training.

In 1945, medical schools decided not to release any transcripts or permit any letters of recommendation to be written until a particular date. In that way, they managed to move the date of residency selection back to the fourth year of medical school. However, the competition for residents simply took on another form. Programs began to issue offers with a time limit for reply. The time limit rapidly decreased from 10 days in 1945 to less than 12 hours in 1950. Students were being issued "exploding" offers that required them to make a decision about training before hanging up the telephone.

In the early 1950s, the National Interassociation Committee on Internships (NICI) examined existing matching plans and chose the Boston Pool Plan, utilized at the time by Boston-area programs, as the model for a trial run of a new centralized system. In October 1951, student representatives from 79 medical schools formed the National Student Internship Committee (NSIC) to discuss the findings of the NICI trial Match and consider an NICI proposal to replicate the Boston Pool Plan at the national level. NSIC petitioned to have the algorithm modified to more equitably represent applicants, and the modified algorithm was adopted and used for the first Match on 1952. That Match was a success, and the NICI recommended the creation of an organization to administer and oversee the running of the Match. The organization, known as the National Intern Matching Program (NIMP), was established in 1952 at the request of medical students.

Modifications to the algorithm proposed by students in 1951 were based on concerns that the matching process favored hospitals over applicants. The students believed the algorithm gave them incentives to misrepresent their true preferences. A publication in 1962 by David Gale & Lloyd Shapley noted that there always exists a stable solution when colleges are matching with students, but that it is possible to favor colleges as a group over applicants as a group (and vice versa). That is, Gale and Shapley found that there is a college-optimal stable match and an applicant-optimal stable match. Lloyd Shapley along with Alvin Roth, would go on to win the 2012 Nobel Prize in Economics for their work on stable allocations.

A debate arose regarding whether the matching program was susceptible to manipulation or unreasonably fair to programs. Indeed, it was shown that in simple cases (i.e. those that exclude couples, second-year programs, and special cases for handling unfilled slots) that had multiple "stable" matchings, the algorithm would return the solution that preferred the preferences of programs over applicants. A correspondence in *New England Journal of Medicine* in 1981 recognized that the algorithm in use was program-optimal for individual applicants.

Later researchers, such as Marilda Sotomayor in 1983, Alvin Roth in 1984, and Klaus et al. in 2007, found that when couples are allowed to match together, there may exist no stable matching. However, Fuhito Kojima and Parag Pathak in 2009 demonstrated that if the market is large and the fraction of couples is small, then a stable matching exists with high probability.

The NRMP algorithm saw only minor and incremental changes after its institution in 1952. However, in the fall of 1995 the NRMP Board of Directors commissioned a preliminary research study to evaluate the current algorithm and recommend changes to be considered in its operation and description, as well as a study comparing a new algorithm with the existing one. A new applicant-proposing algorithm was adopted in May 1997 and has been in use since its first application in March 1998, although the study showed that the net effect of the change on actual matches has been minimal.

## Matching algorithm

Matching applicants to programs is a generalization of the stable marriage problem; as a result, the solutions are very similar. A simplified version of the algorithm that is used to perform the matching process is described below and on the NRMP website. However, this description does not include the handling of couples (pairs of applicants who participate in a Match together, perhaps to stay in the same geographic location), second-year positions, or special handling of residency positions that remain unfilled. The full algorithm is described in Roth & Peranson 1999.

### Inputs

The application process for residency training begins prior to the opening of the Main Residency Match in September. Applications usually are sent to programs through the Electronic Residency Application Service (ERAS), a service of the Association of American Medical Colleges. After applicants apply to programs, programs review applications and invite selected candidates for interviews held between October and February. After the interview period is over, programs and applicants each compile "rank order lists" that they submit to the NRMP. Programs list applicants, ranked in order from most to least preferred, whom they wish to train. Similarly, applicants rank programs where they wish to train. For applicants matching as a couple, the rank order lists include pairs of program choices that are considered simultaneously by the matching algorithm. Applicants' rank order lists can include a combination of categorical programs (training that is 3–5 years in length and begins in the first post-graduate year); preliminary programs (training that is one year in length and begins in the first post-graduate year); or advanced programs (training that is 3–4 years in length and begins after one or more years of preliminary training). For advanced programs on the rank order list, applicants can append a supplemental list of preliminary programs to attempt to match to a full course of training.

### Simple case

The matching process begins with an attempt to match an applicant to the program most preferred on that applicant's rank order list (ROL). If the applicant cannot be matched to that first choice program, an attempt is made to place the applicant into the second choice program, and so on, until the applicant is tentatively matched to a program that has an open position and who prefers that applicant or all the applicant's choices on the ROL have been exhausted. This process is carried out for all applicants until each applicant has either been tentatively matched to the most preferred choice possible or all choices submitted by all applicants have been exhausted. Tentative matches then become final.

To understand how the current NRMP algorithm works, it is helpful to begin by considering the simpler case where there are no couples or secondary programs.

As in the stable marriage problem, the basic goal is to match applicants to programs so that the results are "stable". "Stability" in this case means that there is no applicant A and program P such that both of the following are true:

- A is unmatched or would prefer to go to P over the program to which A matched
- P has a free slot or would prefer A over one of the other applicants matched to the program.

It can be shown that for any instance of the problem, there is at least one valid solution. Under the old (pre-1995) NRMP algorithm that favored programs' preferences over applicants', programs could benefit in certain cases from lying about their preferences. This is no longer possible under the current algorithm. Applicants cannot benefit by lying about their preferences, even if they have perfect knowledge of everyone's preferences.

Under the current system, it also is impossible for an applicant to be harmed by including more residency programs at the bottom of a list if those programs are indeed preferable to not being matched.

### Couples

Couples' rank order lists are processed simultaneously by the matching algorithm, which complicates the problem. In some cases there exists no stable solution (with stable defined the way it is in the simple case). In fact, the problem of determining whether there is a stable solution and finding it if it exists has been proven NP-complete. Also, while there is no randomization in the NRMP algorithm—so it will always return the same output when given exactly the same input—different outcomes can be produced by changing trivial features of the data such as the order in which applicants and programs are processed. However, in initial testing of the algorithm over 5 years of residency match data and a variety of different initial conditions, the current NRMP algorithm always terminated quickly on a stable solution. Testing also showed that "none of [the trivial] sequencing decisions had a large or systematic effect on the matching produced"—the maximum number of applicants ever observed to be affected in a single run was 12 out of 22,938.

In general *once the programs' rank order lists have been set*, there is no way for an applicant to match into a better position by deciding to match as part of a couple. For example, if a very strong applicant and a very weak applicant match as a couple, there is no mechanism *in the algorithm* that allows the stronger applicant to somehow improve the desirability of the weaker applicant. (Of course, if the programs know prior to processing the matching algorithm that the stronger and weaker applicant are participating in the Match as a couple, they are free to change their lists accordingly, which could affect the outcome.)

## Failure to match

It is possible for an applicant not to match to a program. Until the 2010 Main Residency Match, applicants who did not obtain a position went through a process called the Scramble. At 12:00 p.m. on Monday of Match Week, the NRMP notified applicants whether they had matched to a program (but did not release the name of the program) and released a list of unfilled programs. Applicants then applied en masse to programs that had unfilled positions, frequently having to change their preferred specialty in the process. The Scramble was widely recognized to be chaotic, disorganized, and lacking in transparency. The Scramble ended on Match Day, which was Thursday of Match Week. Most positions filled within the first few hours, and nearly all in the first 48 hours. Scrambling was extremely competitive: in 2008, roughly 10,600 applicants, many of whom were foreign-trained, scrambled for only 1,392 residency positions.

After the 2010 Main Residency Match, the Scramble was replaced by the Supplemental Offer and Acceptance Program, or SOAP. In SOAP, unmatched applicants are offered positions in unfilled programs through a series of rounds, creating a systematic way for applicants to find training positions without the chaos of the Scramble. In SOAP, all appointments are made through the NRMP (no direct matching allowed, unlike the Scramble), and unmatched applicant data and unfilled program data are released at the same time on Monday of Match Week. Match Day is now Friday of Match Week.

## Results

Of the 35,476 total active applicants who participated in The National Resident Matching Program in 2016, 75.6% (26,836) were able to find PGY-1 (R-1) matches. Out of the total active applicants, 51.27% (18,187) were graduates of conventional US medical schools; 93.8% (17,057) were able to find a match. In comparison, match rates were 80.3% of osteopathic graduates, 53.9% of US citizen international medical school graduates, and 50.5% of non-US citizen international medical schools graduates.

In 2021, there were a total of 48,700 registered applicants. A total of 38,106 positions were offered in the match. 94.9% of them were filled. 92.8% U.S. MD seniors matched to PGY1 positions, while the percentage for U.S. DO seniors was 89.1%.

## International medical graduates

To participate in the NRMP, an international medical graduate must have ECFMG ID. USMLE ID is not required for IMGs, but it can be entered. It is the same as the ECFMG ID. IMGs must not be completely ECFMG certified but most programs require USMLE Step 2 before "Rank Order List Submission Deadline". Many programs require ECFMG certificate submitted with the initial application.

In comparison, students and graduates from medical schools in the United States are bound to the graduation requirements of their individual schools. Both U.S. and foreign-trained applicants can participate in the NRMP while completing their final year of medical school before acquiring their medical diplomas.

## Lawsuit

In 2002, 16 law firms filed a lawsuit on behalf of three residents seeking to represent all residents matching through the NRMP. The plaintiffs put forward a case which sought to show that the NRMP colluded with other national medical and medical education organizations and with residency-sponsoring institutions to depress resident wages, operating in violation of United States antitrust legislation.

In 2004, after a lobbying effort by the Association of American Medical Colleges and the American Hospital Association, a rider that granted specific immunity to the NRMP was added to a pension act signed into law by President George W. Bush. The provision was sponsored by Senators Edward M. Kennedy, Democrat of Massachusetts, and Judd Gregg, Republican of New Hampshire. Subsequently, a federal district court dismissed the case.

## Implementations in software packages

- Python: A variant of the Roth-Peranson algorithm, as presented in Roth (1984), is available as part of the `matching` library.
- R: The Roth-Peranson algorithm used in the NRMP is available as part of the `matchingMarkets` package.
- API: The MatchingTools API provides a free application programming interface for the Roth-Peranson algorithm used in the NRMP.
