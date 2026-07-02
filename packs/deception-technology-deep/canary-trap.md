---
title: "Canary trap"
source: https://en.wikipedia.org/wiki/Canary_trap
domain: deception-technology-deep
license: CC-BY-SA-4.0
tags: deception technology, honeypot deployment, honeytoken tripwire, canary token alerting, network tarpit
fetched: 2026-07-02
---

# Canary trap

A **canary trap** is a method for exposing an information leak by giving different versions of a sensitive document to each of several suspects and seeing which version gets leaked. It could be one false statement, to see whether sensitive information gets out to other people as well. Special attention is paid to the quality of the prose of the unique language, in the hopes that the suspect will repeat it verbatim in the leak, thereby identifying the version of the document.

The term was coined by Tom Clancy in his 1987 novel *Patriot Games*, although Clancy did not invent the technique. The actual method (usually referred to as a **barium meal test** in espionage circles) has been used by intelligence agencies for many years. The fictional character Jack Ryan describes the technique he devised for identifying the sources of leaked classified documents:

> Each summary paragraph has six different versions, and the mixture of those paragraphs is unique to each numbered copy of the paper. There are over a thousand possible permutations, but only ninety-six numbered copies of the actual document. The reason the summary paragraphs are so lurid is to entice a reporter to quote them verbatim in the public media. If he quotes something from two or three of those paragraphs, we know which copy he saw and, therefore, who leaked it.

A refinement of this technique uses a thesaurus program to shuffle through synonyms, thus making every copy of the document unique.

## Barium meal test

According to the book *Spycatcher* by Peter Wright (published in 1987), the technique is standard practice that has been used by MI5 (and other intelligence agencies) for many years, under the name "barium meal test", named after the medical procedure.

A barium meal test is flexible and may take many different forms. The basic premise is to reveal a supposed secret to a suspected enemy (but nobody else) then monitor whether there is evidence of the fake information being utilized by the other side. For example, a suspected double agent could be offered some tempting "bait": e.g., be told that important information was stored at a dead drop site. The fake dead drop site could then be periodically checked for signs of disturbance. If the site showed signs of being disturbed (for instance, in order to copy microfilm stored there), then this would confirm that the suspected enemy really was an enemy, i.e., a double agent.

## Embedding information

The technique of embedding significant information in a hidden form in a medium has been used in many ways, which are usually classified according to intent:

- Watermarks are used to show that items are authentic and not forged.
- Steganography is used to hide a secret message in an apparently innocuous message, in order to escape detection.
- A canary trap hides information in a document that uniquely identifies it, so that copies of it can be traced.
- Screener versions of DVDs are often marked in some way so as to allow the tracking of unauthorised releases to their source.
- As with the *Star Trek* incident, major films or television productions frequently give out scripts to the cast and crew in which one or two lines are different in each individual version. Thus if the entire script is copied and leaked to the public, the producers can track down the specific person who leaked the script. In practice this does not prevent generalized information about the script from being leaked, but it does discourage leaking verbatim copies of the script itself.
- Trap streets on maps, or intentionally fictitious streets, are sometimes included to track copyright violations by those who might republish copyrighted maps illegally.
- Spurious words are sometimes included in dictionaries so as to detect other publishers copying from them. The *Oxford English Dictionary* contains an appendix of such words with which edition of which dictionary first used them and which first duplicated them.
- Zero-width spaces are Unicode characters that are not visually rendered. An arbitrary number of these characters can be inserted between the letters of a word. Though they are not visible, they will typically persist even as that word is copied and pasted and transmitted multiple times. This can be used to create persistent, invisible fingerprints in digital text.
- Mailing lists for purchase are typically seeded with a small number of postal or email addresses that route back to the seller of the list. This is used to detect reuse of the list (typically sold on a per-mailing basis) or resale of the list (usually prohibited).
- Email aliases can be used when creating accounts to provide an email address specific to that entity so that if the address starts getting spam or is found in a data breach, it can be traced back to the source. Like with the Star Trek incident, there isn't much that can be done about it post-hoc other than to know the source of the leak. The address is already being spammed, but in some cases, it might be important to know the source in case of a lawsuit for selling data or to fix the security weaknesses that led to a hack.
- Karaoke tracks sometimes include altered lyrics to demonstrate plagiarism between karaoke track-making companies.

## Known canary trap cases

Following the troubled production of *Star Trek: The Motion Picture* in the late 1970s, Paramount Pictures effectively replaced Gene Roddenberry as producer of further movies in the franchise with Harve Bennett. Roddenberry was retained as an "executive consultant", due to the high regard the series' fans held him in; while he had little real authority he was still kept involved in the creative process. The fans often complained about particular plot developments proposed for the films, such as the death of Spock in *Star Trek II*, that Roddenberry had opposed. So, before any drafts of the screenplay for *Star Trek III: The Search for Spock* were circulated, Bennett arranged for each individual copy to have subtle clues distinguishing it from the others. Shortly after Roddenberry opposed the destruction of the *Enterprise* at the climax of that film, fans began to complain to Paramount and Bennett. He found that a leaked copy of the script was the one given to Roddenberry, but was unable to do anything about it.

After a series of leaks at Tesla Motors in 2008, CEO Elon Musk reportedly sent slightly different versions of an e-mail to each employee in an attempt to reveal potential leakers. The e-mail was disguised as a request to employees to sign a new non-disclosure agreement. The plan was undermined when the company's general counsel forwarded his own unique version of the e-mail with the attached agreement. As a result, Musk's scheme was realized by employees who now had a safe copy to leak.

In October 2019, British celebrity Coleen Rooney used a barium meal test to identify who was leaking information from her private Instagram stories to tabloid newspaper *The Sun* by posting fake stories which were blocked to all but one account. When these details appeared in the press, she publicly identified the leaks as coming from the account of Rebekah Vardy, wife of soccer player Jamie Vardy. The subsequent libel trial became known as the Wagatha Christie case.

In December 2020, Andrew Lewer, a Member of Parliament and parliamentary private secretary in the UK government, was fired from his latter post after a canary trap in the form of a letter reminding staff not to leak was published on the website *Guido Fawkes*.

In 2023, Apple Inc. fired a staffer for leaking information regarding upcoming software releases; emails regarding the release date were sent to various employees containing dates for different releases in unique combinations to identify the source of the leaked information.

In 2025, it was reported that a candidate for a senior position within Britain's external intelligence agency, MI6, was able to infer a leak within the United Kingdom Security Vetting agency using the barium meal technique.

In 2026, an Albertan separatist group gained illegitimate access to the Alberta electoral database. Using a canary trap, it was found that the Republican Party of Alberta had leaked the data to the group.

## In popular culture

- The canary trap was used in several of Tom Clancy's novels. Chronologically it first appears in *Without Remorse*, when a CIA official alters a report given to a senator, revealing an internal leak who was giving information to the KGB. Different versions of the report were given to other suspected leakers.
- Barium meals are also administered in Robert Littel's book *The Company*, and later in the TV miniseries with same name.
- The technique (not named) was used in the 1970s BBC television serial *1990*. The same unnamed technique also appeared in Irving Wallace's book *The Word* (1972), and in the 1985 spy novel *London Match* by Len Deighton.
- A variation of the canary trap was used in the film *Miami Vice*, with various rendezvous dates leaked to different groups.
- In the third-season finale of *The Mentalist*, the characters use a canary trap (giving different hotel room numbers to different suspects) to uncover a mole within their agency. A similar ruse is used in the TV series *Ashes to Ashes*.
- In *A Clash of Kings*, the second book in the *A Song of Ice and Fire* series, Tyrion Lannister uses the trap to find out which member of the King's small council is reporting to his sister, the Queen Regent Cersei Lannister. To the Grand Maester Pycelle, he tells of a plot to marry his niece, Princess Myrcella, to Prince Trystane of the powerful House Martell, from Dorne. To Littlefinger, he claims he will instead send Myrcella to be raised by Lysa Arryn and married to her son Robert. To Varys, he says his plan is to send his nephew Tommen to the Martells. When Cersei confronts him, and knows only of the plan to send Myrcella to Dorne, Tyrion knows Pycelle to be the leak.
  - This plotline is also depicted in "What Is Dead May Never Die", during the second season of *Game of Thrones*, the television adaptation of the books.
- When distributing the film *Broken* to friends, Trent Reznor of Nine Inch Nails claims that he watermarked the tapes with dropouts at certain points so that he could identify if a leak would surface.
- In the film *The Heat*, a canary trap is employed by a drug ring to determine the loyalty of a returning member who is Detective Mullins' brother.
- In *Han Solo at Stars' End*, the first book in *The Han Solo Adventures*, the title character uses a canary trap to find a traitor and murderer among his passengers. He tells each that their target is a different planet, all false, knowing that the traitor would have learned the real destination when they killed the group's leader.
- Episode 25 of *Kamen Rider Build* has the main characters trying to determine the identity of the Namba Children agent through Barium meal test. While the identity of the leaker was revealed, several episodes later established that a bug was implanted into one of the protagonists' devices by another member of the Namba Children.
