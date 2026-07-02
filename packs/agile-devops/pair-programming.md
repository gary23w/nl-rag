---
title: "Pair programming"
source: https://en.wikipedia.org/wiki/Pair_programming
domain: agile-devops
license: CC-BY-SA-4.0
tags: agile, scrum, kanban, devops, continuous delivery, pair programming
fetched: 2026-07-02
---

# Pair programming

**Pair programming** is a software development technique in which two programmers work together at one workstation. One, the *driver*, writes code while the other, the *observer* or *navigator*, reviews each line of code as it is typed in. The two programmers switch roles frequently.

While reviewing, the observer also considers the "strategic" direction of the work, coming up with ideas for improvements and likely future problems to address. This is intended to free the driver to focus all of their attention on the "tactical" aspects of completing the current task, using the observer as a safety net and guide.

## Economics

Pair programming increases the human-hours required to deliver code compared to programmers working individually. However, the resulting code has fewer defects. Along with code development time, other factors like field support costs and quality assurance also figure into the return on investment. Pair programming might theoretically offset these expenses by reducing defects in the programs.

In addition to preventing mistakes as they are made, other intangible benefits may exist. For example, the courtesy of rejecting phone calls or other distractions while working together, taking fewer breaks at agreed-upon intervals or sharing breaks to return phone calls (but returning to work quickly since someone is waiting). One member of the team might have more focus and help drive or awaken the other if they lose focus, and that role might periodically change. One member might know about a topic or technique that the other does not, which might eliminate delays to finding or testing a solution, or allow for a better solution, thus effectively expanding the skill set, knowledge, and experience of a programmer as compared to working alone. Each of these intangible benefits, and many more, may be challenging to accurately measure but can contribute to more efficient working hours.

## Design quality

A system with two programmers possesses greater potential for the generation of more diverse solutions to problems for three reasons:

1. the programmers bring different prior experiences to the task;
2. they may assess information relevant to the task in different ways;
3. they stand in different relationships to the problem by their functional roles.

In an attempt to share goals and plans, the programmers must overtly negotiate a shared course of action when a conflict arises between them. In doing so, they consider a larger number of ways of solving the problem than a single programmer alone might do. This significantly improves the design quality of the program as it reduces the chances of selecting a poor method.

## Satisfaction

In an online survey of pair programmers from 2000, 96% of programmers stated that they enjoyed working more while pair programming than programming alone. Furthermore, 95% said that they were more confident in their work when they pair programmed. However, as the survey was among self-selected pair programmers, it did not account for programmers who were forced to pair program.

## Learning

Knowledge is constantly shared between pair programmers, whether in the industry or in a classroom. Many sources suggest that students show higher confidence when programming in pairs, and many learn whether it be from tips on programming language rules to overall design skills. In "promiscuous pairing", each programmer communicates and works with all the other programmers on the team rather than pairing only with one partner, which causes knowledge of the system to spread throughout the whole team. Pair programming allows programmers to examine their partner's code and provide feedback, which is necessary to increase their own ability to develop monitoring mechanisms for their own learning activities.

## Team-building and communication

Pair programming allows team members to share quickly, making them less likely to have agendas hidden from each other. This helps pair programmers learn to communicate more easily. "This raises the communication bandwidth and frequency within the project, increasing overall information flow within the team."

## Studies

There are both empirical studies and meta-analyses of pair programming. The empirical studies tend to examine the level of productivity and the quality of the code, while meta-analyses may focus on biases introduced by the process of testing and publishing.

A meta-analysis found pairs typically consider more design alternatives than programmers working alone, arrive at simpler, more maintainable designs, and catch design defects earlier. However, it raised concerns that its findings may have been influenced by "signs of publication bias among published studies on pair programming." It concluded that "pair programming is not uniformly beneficial or effective."

Although pair programmers may complete a task faster than a solo programmer, the total number of human-hours increases. A manager would have to balance faster completion of the work and reduced testing and debugging time against the higher cost of coding. The relative weight of these factors can vary by project and task.

The benefit of pairing is greatest on tasks that the programmers do not fully understand before they begin: that is, challenging tasks that call for creativity and sophistication, and for novices as compared to experts. Pair programming could be helpful for attaining high quality and correctness on complex programming tasks, but it would also increase the development effort (cost) significantly.

On simple tasks, which the pair already fully understands, pairing results in a net drop in productivity. It may reduce the code development time but also risks reducing the quality of the program. Productivity can also drop when novice–novice pairing is used without sufficient availability of a mentor to coach them.

A study of programmers using AI assistance tools such as GitHub Copilot found that while some programmers conceived of AI assistance as similar to pair programming, in practice the use of such tools is very different in terms of the programmer experience, with the human programmer having to transition repeatedly between driver and navigator roles.

## Indicators of non-performance

There are indicators that a pair is not performing well:

- *Disengagement* may present as one of the members physically withdraws away from the keyboard, accesses email, or even falls asleep.
- The *"Watch the Master"* phenomenon can arise if one member is more experienced than the other. In this situation, the junior member may take the observer role, deferring to the senior member of the pair for the majority of coding activity. This can easily lead to disengagement.

## Pairing variations

**Expert–expert**

Expert–expert pairing may seem to be the obvious choice for the highest productivity and can produce great results, but it often yields little insight into new ways to solve problems, as both parties are unlikely to question established practices.

**Expert–novice**

Expert–novice pairing creates many opportunities for the expert to mentor the novice. This pairing can also introduce new ideas, as the novice is more likely to question established practices. The expert, now required to explain established practices, is also more likely to question them. However, in this pairing, an intimidated novice may passively "watch the master" and hesitate to participate meaningfully. Also, some experts may not have the patience needed to allow constructive novice participation.

**Novice–novice**

Novice–novice pairing can produce results significantly better than two novices working independently, although this practice is generally discouraged because it is harder for novices to develop good habits without a proper role model.

## Remote pair programming

**Remote pair programming**, also known as **virtual pair programming** or **distributed pair programming**, is pair programming in which the two programmers are in different locations, working via a collaborative real-time editor, shared desktop, or a remote pair programming IDE plugin. Remote pairing introduces difficulties not present in face-to-face pairing, such as extra delays for coordination, depending more on "heavyweight" task-tracking tools instead of "lightweight" ones like index cards, and loss of verbal communication resulting in confusion and conflicts over such things as who "has the keyboard".

Tool support could be provided by:

- Whole-screen sharing software
- Terminal multiplexers
- Specialized distributed editing tools
- Audio chat programs or VoIP software could be helpful when the screen sharing software does not provide two-way audio capability. Use of headsets keeps the programmers' hands free
- Cloud development environments
- Collaborative pair programming services
