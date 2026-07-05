---
title: "archive.today"
source: https://en.wikipedia.org/wiki/Archive.today
domain: donát-bánki
license: CC-BY-SA-4.0
tags: donát bánki
fetched: 2026-07-05
---

# archive.today

**archive.today** (also known as **archive.is**, among other domains) is a web archiving website that saves snapshots on demand. It has support for JavaScript-heavy sites such as Google Maps and X. archive.today records two snapshots: one replicates the original webpage including any functional live links; the other is a screenshot of the page.

The website has come under scrutiny from many governments starting in the late 2010s, including bans in China and Russia and in 2025 U.S. Federal Bureau of Investigation (FBI) subpoenaed a domain registrar to identify the owner of archive.today's domain name.

## History

archive.today was founded in 2012 as a web archive. It allegedly registered its trademark in the Czech Republic in 2013. The site originally branded itself as archive.today, but changed the primary mirror to archive.is in May 2015. It began to deprecate the archive.is domain in favor of other mirrors in January 2019. According to the archive.today blog, the website had saved about 500 million pages by 2021, 700 terabytes in total size.

In July 2013, archive.today began supporting the API of the Memento Project at Los Alamos National Laboratory. Due to budget constraints at LANL, the Memento Project was disestablished in September 2025. Archive.today was one of the last major active users of the Memento protocol following the project's downsizing. The closure of the Memento infrastructure at LANL in September 2025 came amid a broader period of increased scrutiny for the service.

The Russian independent media outlet *Mediazona* uses the site to preserve social media profiles and posts of Russian servicemen killed in the Russo-Ukrainian war, as part of its Russia 200 project, a named database of confirmed Russian military casualties compiled jointly with the BBC Russian Service and a team of volunteers. Individual profile pages on 200.zona.media link to snapshots of social media posts by relatives, obituaries in local media, and other open-source evidence used to verify each death.

In early 2023, a team of researchers at the University of Amsterdam identified archive.today as the most-used open-access archiving service among fact-checking organisations, based on the European Digital Media Observatory's dataset on the Russo-Ukrainian war.

On 5 August 2023, Jani Patokallio published on his blog *Gyrovague* an investigation regarding archive.today's funding sources and the founder's identity.

On 30 October 2025, the US Federal Bureau of Investigation (FBI) subpoenaed archive.today's domain registrar, Tucows. The subpoena stated its purpose was to identify the owner(s) of the archive.today domain name, and that it was part of a criminal investigation conducted by the FBI, the nature of which was not disclosed. The Catalan daily *Ara* interpreted the action as part of a campaign to selectively criminalize anonymous digital archives reliant on micro-donations (such as Anna's Archive, eliminated by Google from its search results), even though industrial datasets used for training large language models (such as the Common Crawl, financed by OpenAI and Anthropic) also fail to compensate content creators and owners. News coverage of the subpoena mentioned Patokallio's report, where Patokallio has said there were "several indications" the founder was based in Russia.

In November 2025, the DNS provider AdGuard DNS reported that a French organization *Web Abuse Association Defense* (WAAD) had pressured it to block archive.today and its mirror domains. WAAD alleged that archive.today had refused to remove child sexual abuse material since 2023. When AdGuard contacted archive.today, the archive removed the material, stating that it had never received prior complaints about those URLs. AdGuard found WAAD suspicious as a recently registered association with minimal public presence, noting evidence of possible impersonation of a real French lawyer in similar WAAD complaints sent to other companies. AdGuard announced it would file a criminal complaint with French police.

### Attack on *Gyrovague* and Wikipedia's restrictions

On 8 January 2026, Patokallio's hosting provider Automattic notified him of a GDPR complaint from "Nora" alleging that the 2023 *Gyrovague* investigation "contains extensive personal data… presented in a narrative that is defamatory in tone and context." After Patokallio submitted a rebuttal, Automattic sided with him and left the post up.

On 14 January 2026, it emerged that archive.today had silently modified its CAPTCHA page to send repeated requests to *Gyrovague*, thereby causing visitors to unwittingly contribute to a DDOS attack against the blog. The archive.today blog simultaneously posted several public criticisms of Patokallio. Emails released by Patokallio show archive.today requesting the temporary removal of his report and later threatening him with AI pornography.

On 20 February 2026, the English Wikipedia banned all links to archive.today, citing the DDoS attack and evidence that archived content was tampered with: Discussion had discovered that instances of Nora's name were replaced with Patokallio's and that "Nora" was likely an appropriated identity—the name belonged to a real person, whose only connection to archive.today had been a prior content takedown request. The community's decision was made despite concerns over maintaining content verifiability—partly undermined by the discovery of the alterations— while removing and replacing the second-largest archiving service used across the Wikimedia Foundation's projects. The Wikimedia Foundation had stated its readiness to take action regardless of the community verdict. Patokallio expressed his satisfaction with the outcome.

This was not the first time Wikipedia had restricted links to archive.today. In 2013, the community blacklisted archive.is, citing concerns about botnets, linkspamming, and the opaque manner in which the site was operated. The decision was overturned in 2016 following a new request for comment, and archive.today was removed from the spam blacklist. At the time of the 2026 ban, the site was the second-largest archiving service used across all Wikimedia Foundation projects, with over 695,000 links spread across approximately 400,000 pages.

## Features

### Archiving

archive.today can capture individual pages in response to explicit user requests. Since its beginning, it has supported crawling pages with URLs containing the now-deprecated hash-bang fragment (#!). The website records only text and images, excluding XML, RTF, spreadsheet (xls or ods) and other non-static content. However, videos for certain sites, like Twitter, are saved. It keeps track of the history of snapshots saved, requesting confirmation before adding a new snapshot of an already saved page. Once a web page is archived, it cannot be deleted directly by any Internet user. Users can download archived pages as a ZIP file, except pages archived since 29 November 2019, when archive.today changed their browser engine from PhantomJS to Chromium (non-headless). archive.today does not obey robots.txt because it acts "as a direct agent of the human user."

Pages are captured at a browser width of 1,024 pixels. CSS is converted to inline CSS, removing responsive web design and selectors such as `:hover` and `:active`. Content generated using JavaScript during the crawling process appears in a frozen state. HTML class names are preserved inside the `old-class` attribute. When text is selected, a JavaScript applet generates a URL fragment seen in the browser's address bar that automatically highlights that portion of the text when visited again. Web pages can be duplicated from archive.today to web.archive.org as second-level backup, but archive.today does not save its snapshots in WARC format. The reverse—from web.archive.org to archive.today—is also possible, but the copy usually takes more time than a direct capture.

While saving a page, a list of URLs for individual page elements and their content sizes, HTTP statuses and MIME types is shown. This list can only be viewed during the crawling process. Removing advertisements, popups or expanding links from archived pages is possible by asking the owner to do it on his blog.

According to the site's FAQ, archive.today's storage layer runs on Apache Hadoop and Apache Accumulo, with all data stored on the Hadoop Distributed File System (HDFS). Textual content is replicated three times across servers in two data centers, both located in Europe, with at least one hosted by the French provider OVH; images are replicated twice. The site does not store snapshots in WARC format.

The scraping component has used a modified version of the Chromium browser since November 2019, replacing the previous PhantomJS-based engine.

The research toolbar enables advanced keywords operators, using `*` as the wildcard character. Paired quotation marks address the search to an exact sequence of keywords present in the title or in the body of the webpage, whereas the *insite* operator restricts it to a specific Internet domain. While saving a dynamic list, archive.today search box shows only a result that links the previous and the following section of the list (e.g. 20 links for page). The other web pages saved are filtered, and sometimes may be found by one of their occurrences. The search feature is backed by Google CustomSearch. If it delivers no results, archive.today attempts to utilize Yandex Search.

### Bypassing paywalls

archive.today is frequently used to bypass paywalls on news websites, similarly to the defunct service 12ft.

#### Legal and ethical debate

The practice of sharing archive.today links to circumvent paywalls has sparked legal and ethical debate in Europe. In the Netherlands, journalist Peter Aanzee publicly challenged a physician who shared an archive.ph link to one of his paywalled articles in *De Volkskrant*, arguing that distributing archived copies constituted copyright infringement. The discussion drew on European Court of Justice jurisprudence on hyperlinking, particularly the 2016 *GS Media v Sanoma* ruling, which established that linking to illegally published content can constitute a copyright violation if the linker knew or ought to have known of the illegality—a presumption that applies automatically to parties acting for profit.

The largest Dutch publisher, DPG Media, acknowledged that archive.today is "a thorn in the side of many publishers (and journalists)" but noted that enforcement is difficult because the site is operated anonymously, hosted across multiple servers that frequently change location, and resurfaces under new domains when one is taken down.

#### Comparison with Internet Archive

Commentators have contrasted archive.today with the Internet Archive's Wayback Machine. The same paywalled *Volkskrant* article shared via archive.ph was also found archived in the Wayback Machine, demonstrating that both services can be used to circumvent paywalls. Like the Wayback Machine, archive.today does not advertise paywall circumvention among its stated features; the ability to bypass paywalls is a byproduct of its core function of archiving web pages as they appear to visitors.

#### AI agents

A 2025 investigation by journalist Henk van Ess found that AI chatbots—including ChatGPT, Perplexity AI, Grok, and Claude—exploit web archives to bypass paywalls during live web searches. In one documented case, ChatGPT retrieved a full article from *The Economist* via archive.today and then generated a five-point economic analysis in the publication's characteristic style and terminology. Van Ess identified six distinct methods of paywall circumvention by AI systems, of which "archive exploitation"—finding archived copies on services such as archive.today and the Internet Archive—was the most direct. Unlike documented concerns about AI training unpaywalled content, this behaviour involves real-time retrieval through archived copies during individual queries, effectively extending paywall circumvention beyond human users to automated agents.

## Academic research

A 2018 study by researchers at University College London, University of Alabama at Birmingham, and Cyprus University of Technology, published at the AAAI International Conference on Web and Social Media (ICWSM), analysed 21 million URLs from archive.is's live feed and 356,000 archive.is URLs shared on Reddit, Twitter, Gab, and 4chan's /pol/ board over 14 months. The study found that news articles and social media posts were the most commonly archived content types, likely due to their "perceived ephemeral and/or controversial nature."

The researchers documented that archive.is URLs were extensively shared on "fringe" communities such as 4chan's /pol/ board and the Reddit subreddit r/The_Donald, both to preserve potentially contentious content and to deny ad revenue to news outlets perceived as ideologically opposed. Moderation bots on r/The_Donald automatically blocked direct links to certain news sites—for example, 46% of links to the *New York Daily News* were censored—and prompted users to post archive.is URLs instead. The authors estimated that *The Washington Post* lost approximately US$70,000 per year in ad revenue due to the practice of sharing archived copies rather than direct links on Reddit alone.

On Reddit, bots were responsible for posting 44% of archive.is links and 85% of Wayback Machine links across the studied subreddits, driven by moderators aiming to mitigate link rot.

A 2023 study by researchers at the University of Amsterdam, as part of the vera.ai project, examined 1,991 fact-checking articles from the European Digital Media Observatory's "War in Ukraine" dataset. Of 41,758 extracted links, 6,002 were archived pages. archive.today was the most-used link archiving service, at 44.1%, ahead of the Internet Archive/Wayback Machine (29.2%) and Perma.cc (26.6%). Fact-checkers primarily used these services to preserve ephemeral and platform-restricted content, such as Facebook posts that are difficult to capture due to anti-bot measures.

## Worldwide availability

### Australia and New Zealand

In March 2019, the site was blocked for six months by several internet providers in Australia and New Zealand in the aftermath of the Christchurch mosque shootings in an attempt to limit distribution of the footage of the attack.

### China

According to GreatFire.org, archive.today has been blocked in mainland China since March 2016, archive.li since September 2017, archive.fo since July 2018, as well as archive.ph since December 2019.

### Finland

On 21 July 2015, the archive.today blocked access to the service from all Finnish IP addresses, stating on Twitter that they did this in order to avoid escalating a dispute they allegedly had with the Finnish government.

Since the conflict with the Finnish blogger in early 2026, the website displays an unpassable captcha to visitors from Finland.

### Russia

In 2016, the Russian communications agency Roskomnadzor began blocking access to archive.is from Russia.

On 23 March 2026, archive.today and several mirror domains were blocked by Russian authorities.
