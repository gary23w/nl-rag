---
title: "Deepfake (part 1/2)"
source: https://en.wikipedia.org/wiki/Deepfake
domain: voice-cloning-ml
license: CC-BY-SA-4.0
tags: voice cloning, speaker voice synthesis, speaker embedding adaptation, few shot voice mimicry, audio deepfake voice
fetched: 2026-07-02
part: 1/2
---

# Deepfake

**Deepfakes** (a portmanteau of 'deep learning' and 'fake') are images, videos, or audio that have been edited or generated using artificial intelligence, AI-based tools or audio-video editing software. They may depict real or fictional people and are considered a form of synthetic media, that is media that is usually created by artificial intelligence systems by combining various media elements into a new media artifact.

While the act of creating fake content is not new, deepfakes uniquely leverage machine learning and artificial intelligence techniques, including facial recognition algorithms and artificial neural networks such as variational autoencoders and generative adversarial networks (GANs). In turn, the field of image forensics has worked to develop techniques to detect manipulated images. Deepfakes have garnered widespread attention for their potential use in creating child sexual abuse material, celebrity pornographic videos, revenge porn, fake news, hoaxes, bullying, and financial fraud.

Academics have raised concerns about the potential for deepfakes to promote disinformation and hate speech, as well as interfere with elections. In response, the information technology industry and governments have proposed recommendations and methods to detect and mitigate their use. Academic research has also delved deeper into the factors driving deepfake engagement online as well as potential countermeasures to malicious application of deepfakes.

From traditional entertainment to gaming, deepfake technology has evolved to be increasingly convincing and available to the public, allowing for the disruption of the entertainment and media industries.


## History

Photo manipulation was developed in the 19th century and soon applied to motion pictures. Technology steadily improved during the 20th century, and more quickly with the advent of digital video.

Deepfake technology has been developed by researchers at academic institutions beginning in the 1990s, and later by amateurs in online communities. More recently, the methods have been adopted by industry.

The development of generative adversarial networks (GANs) in the mid-2010s represented a key technical turning point in the evolution of deepfakes. GANs allowed for the creation of highly realistic fake images and videos by training competing neural networks, achieving a much improved visual fidelity over previous methods of creating the content using rules or by using autoencoders, and formed the basis for modern deepfake methods.

### Academic research

Academic research related to deepfakes is split between the field of computer vision, a sub-field of computer science, which develops techniques for creating and identifying deepfakes, and humanities and social science approaches that study the social, ethical, aesthetic implications as well as journalistic and informational implications of deepfakes. As deepfakes have become more sophisticated and more common, with innovations provided by AI tools, significant research has gone into developing detection methods and defining the factors driving engagement with deepfakes on the internet. Deepfakes have been shown to appear on social media platforms and other parts of the internet for purposes including entertainment, education related to deepfakes, and misinformation intended to elicit strong reactions. There are gaps in research related to the propagation of deepfakes on social media. Negativity and emotional response are the primary driving factors for users sharing deepfakes.

In cinema studies, deepfakes illustrate how "the human face is emerging as a central object of ambivalence in the digital age". Video artists have used deepfakes to "playfully rewrite film history by retrofitting canonical cinema with new star performers". Film scholar Christopher Holliday analyses how altering the gender and race of performers in familiar movie scenes destabilizes gender classifications and categories. The concept of "queering" deepfakes is also discussed in Oliver M. Gingrich's discussion of media artworks that use deepfakes to reframe gender, including British artist Jake Elwes' *Zizi: Queering the Dataset*, an artwork that uses deepfakes of drag queens to intentionally play with gender. The aesthetic potentials of deepfakes are also beginning to be explored. Theatre historian John Fletcher notes that early demonstrations of deepfakes are presented as performances, and situates these in the context of theater, discussing "some of the more troubling paradigm shifts" that deepfakes represent as a performance genre.

While most English-language academic studies of deepfakes focus on the Western anxieties about disinformation and pornography, digital anthropologist Gabriele de Seta has analyzed the Chinese reception of deepfakes, which are known as *huanlian*, which translates to "changing faces". The Chinese term does not contain the "fake" of the English deepfake, and de Seta argues that this cultural context may explain why the Chinese response has centered on practical regulatory measures to "fraud risks, image rights, economic profit, and ethical imbalances".

### Computer science research on deepfakes

A landmark early project was the "Video Rewrite" program, published in 1997. The program modified existing video footage of a person speaking to depict that person mouthing the words from a different audio track. It was the first system to fully automate this kind of facial reanimation, and it did so using machine learning techniques to make connections between the sounds produced by a video's subject and the shape of the subject's face.

Contemporary academic projects have focused on creating more realistic videos and improving deepfake techniques. The "Synthesizing Obama" program, published in 2017, modifies video footage of former president Barack Obama to depict him mouthing the words contained in a separate audio track. The project lists as a main research contribution to its photorealistic technique for synthesizing mouth shapes from audio. The "Face2Face" program, published in 2016, modifies video footage of a person's face to depict them mimicking another person's facial expressions. The project highlights its primary research contribution as the development of the first method for re-enacting facial expressions in real time using a camera that does not capture depth, enabling the technique to work with common consumer cameras.

Researchers have also shown that deepfakes are expanding into other domains such as medical imagery. In this work, it was shown how an attacker can automatically inject or remove lung cancer in a patient's 3D CT scan. The result was so convincing that it fooled three radiologists and a state-of-the-art lung cancer detection AI. To demonstrate the threat, the authors successfully performed the attack on a hospital in a White hat penetration test.

A survey of deepfakes, published in May 2020, provides a timeline of how the creation and detection of deepfakes have advanced over the last few years. The survey identifies that researchers have been focusing on resolving the following challenges of deepfake creation:

- Generalization. High-quality deepfakes are often achieved by training on hours of footage of the target. This challenge is to minimize the amount of training data and the time to train the model required to produce quality images and to enable the execution of trained models on *new* identities (unseen during training).
- Paired Training. Training a supervised model can produce high-quality results, but requires data pairing. This is the process of finding examples of inputs and their desired outputs for the model to learn from. Data pairing is laborious and impractical when training on multiple identities and facial behaviors. Some solutions include self-supervised training (using frames from the same video), the use of unpaired networks such as Cycle-GAN, or the manipulation of network embeddings.
- Identity leakage. This is where the identity of the driver (i.e., the actor controlling the face in a reenactment) is partially transferred to the generated face. Some solutions proposed include attention mechanisms, few-shot learning, disentanglement, boundary conversions, and skip connections.
- Occlusions. When part of the face is obstructed with a hand, hair, glasses, or any other item then artifacts can occur. A common occlusion is a closed mouth which hides the inside of the mouth and the teeth. Some solutions include image segmentation during training and in-painting.
- Temporal coherence. In videos containing deepfakes, artifacts such as flickering and jitter can occur because the network has no context of the preceding frames. Some researchers provide this context or use novel temporal coherence losses to help improve realism. As the technology improves, the interference is diminishing.

Overall, deepfakes are expected to have several implications in media and society, media production, media representations, media audiences, gender, law, and regulation, and politics.

### Amateur development

The term *deepfake* originated in late 2017 from a Reddit user named "deepfakes". He, along with other members of Reddit's "r/deepfakes", shared deepfakes they created; many videos involved celebrities' faces swapped onto the bodies of actors in pornographic videos, while non-pornographic content included many videos with actor Nicolas Cage's face swapped into various movies.

After this first introduction, amateur development grew at a quick rate because of the presence of open-source software and tutorials on the Internet. The freely available tools like FakeApp, FaceSwap, and DeepFaceLab allowed users who did not have any formal education in computer science to assemble deepfake videos with consumer hardware. Online forums such as Reddit, GitHub and YouTube were important to the distribution of software, instructions, and sample content, and helped to spread and perfect amateur creation of deepfakes quicker.

Other online communities continue to share pornography on platforms that have not banned deepfake pornography.

### Commercial development

In January 2018, a proprietary desktop application called "FakeApp" was launched. This app allows users to easily create and share videos with their faces swapped with each other. As of 2019, "FakeApp" had been largely replaced by open-source alternatives such as "Faceswap", command line-based "DeepFaceLab", and web-based apps such as DeepfakesWeb.

Larger companies started to use deepfakes. Corporate training videos can be created using deepfaked avatars and their voices, for example Synthesia, which uses deepfake technology with avatars to create personalized videos. The mobile app Momo created the application Zao which allows users to superimpose their face on television and movie clips with a single picture. As of 2019 the Japanese AI company DataGrid made a full body deepfake that could create a person from scratch.

By 2020, audio deepfakes and AI software capable of cloning human voices based on a few seconds of speech exist. Tools for deepfake detection also emerge. A mobile deepfake app, Impressions, was launched in March 2020. It was the first app for the creation of celebrity deepfake videos from mobile phones.

### Resurrection

Deepfake technology's ability to fabricate messages and actions of others can extend to the deceased, such as in grief therapy that allows seeming communication with a deceased loved one. In October 2020, Kim Kardashian posted a video featuring a hologram of her late father, Robert Kardashian, created by the company Kaleida, which used a combination of performance, motion tracking, SFX, VFX and DeepFake technologies to create the illusion.

In 2020, a deepfake video of Joaquin Oliver, a victim of the Parkland shooting, was created as part of a gun safety campaign. Oliver's parents partnered with nonprofit Change the Ref and McCann Health to produce a video in which Oliver to encourage people to support gun safety legislation and politicians who back do so as well.

In 2022, a deepfake video of Elvis Presley was used on the program *America's Got Talent 17*.


## Techniques

Deepfakes rely on a type of neural network called an autoencoder. These consist of an encoder, which reduces an image to a lower dimensional latent space, and a decoder, which reconstructs the image from the latent representation. Deepfakes utilize this architecture by having a universal encoder which encodes a person in to the latent space. The latent representation contains key features about their facial features and body posture. This can then be decoded with a model trained specifically for the target. This means the target's detailed information will be superimposed on the underlying facial and body features of the original video, represented in the latent space.

A popular upgrade to this architecture attaches a generative adversarial network to the decoder. A GAN trains a generator, in this case the decoder, and a discriminator in an adversarial relationship. The first network, known as the generator, attempts to craft fabricated images, while the second network, the discriminator, distinguishes between real and fake images using a legitimate data set to guide its judgment. This causes the generator to create images that mimic reality extremely well as any defects would be caught by the discriminator. Both algorithms improve constantly in a zero sum game. This makes deepfakes difficult to combat as they are constantly evolving; any time a defect is determined, it can be corrected.


## Applications

### Acting

Digital clones of professional actors have appeared in films before, and progress in deepfake technology is expected to further the accessibility and effectiveness of such clones. The use of AI technology was a major issue in the 2023 SAG-AFTRA strike, as new techniques enabled the capability of generating and storing a digital likeness to use in place of actors.

Disney has improved their visual effects using high-resolution deepfake face swapping technology. Disney improved their technology through progressive training programmed to identify facial expressions, implementing a face-swapping feature, and iterating in order to stabilize and refine the output. This high-resolution deepfake technology saves significant operational and production costs. Disney's deepfake generation model can produce AI-generated media at a 1024 x 1024 resolution, as opposed to common models that produce media at a 256 x 256 resolution. The technology allows Disney to de-age characters or revive deceased actors. Similar technology was initially used by fans to unofficially insert faces into existing media, such as overlaying Harrison Ford's young face onto Han Solo's face in *Solo: A Star Wars Story*. Disney used deepfakes for the characters of Princess Leia in *Rogue One* and Luke Skywalker in both *The Mandalorian* and *The Book of Boba Fett.*

In the 2024 Indian Tamil science fiction action thriller *The Greatest of All Time*, the teenage version of Vijay's character Jeevan is portrayed by Ayaz Khan. Vijay's teenage face was then attained by AI deepfake. In May 2025, an AI-generated actress called Tilly Norwood was developed by the Dutch company Xicoia, a division of the existing production company Particle6 that was founded by actor and comedian Eline Van der Velden.

### Art

Deepfakes are also being used in education and media to create realistic videos and interactive content, which offer new ways to engage audiences.

In March 2018 the multidisciplinary artist Joseph Ayerle published the video artwork *Un'emozione per sempre 2.0* (English title: *The Italian Game*). The artist worked with Deepfake technology to create an *AI actor,* a synthetic version of 80s movie star Ornella Muti, traveling in time from 1978 to 2018. The Massachusetts Institute of Technology referred this artwork in the study "Collective Wisdom". The artist used Ornella Muti's time travel to explore generational reflections, while also investigating questions about the role of provocation in the world of art. For the technical realization Ayerle used scenes of photo model Kendall Jenner. The program replaced Jenner's face by an AI calculated face of Ornella Muti. As a result, the AI actor has the face of the Italian actor Ornella Muti and the body of Kendall Jenner.

Deepfakes have been widely used in satire or to parody celebrities and politicians. The 2020 webseries *Sassy Justice*, created by Trey Parker and Matt Stone, heavily features the use of deepfaked public figures to satirize current events and raise awareness of deepfake technology.

### Blackmail

Deepfakes can be used to generate blackmail materials that falsely incriminate a victim. A report by the American Congressional Research Service warned that deepfakes could be used to blackmail elected officials or those with access to classified information for espionage or influence purposes.

When or if fakes cannot reliably be distinguished from genuine evidence, victims who are blackmailed over digital evidence might claim that true artifacts are fakes, thereby seeking plausible deniability by relying on an argument of indistinguishability between fake and genuine evidence. The hoped-for effect is to void credibility of certain existing blackmail materials, which, if they were the sole evidence retained by a blackmailer and could not be distinguished by a jury from fake evidence under this argument, could in theory erode loyalty to blackmailers and limit their control over the blackmailed. This phenomenon has been termed "blackmail inflation", since in theory it "devalues" authentic blackmail material. It is possible to utilize commodity GPU hardware with a small software program to generate fake content intended to blackmail anyone for whom an adversary has ample training data. However, even carefully manipulated fakes may still be detected.

The existence of efficient techniques for fabricating false evidence certainly suggests that any combination of video, audio, photographic or other generable evidence alone as the basis for conviction of a crime is by now a perilous and tenuous standard owing to the possibility of maliciously fabricated evidence, raising the importance of multiple firsthand witnesses to a crime, especially for more serious allegations.

### Entertainment

On 8 June 2022, Daniel Emmet, a former AGT contestant, teamed up with the AI startup Metaphysic AI, to create a hyperrealistic deepfake to make it appear as Simon Cowell. Cowell, notoriously known for severely critiquing contestants, was on stage interpreting "You're The Inspiration" by Chicago. Emmet sang on stage as an image of Simon Cowell emerged on the screen behind him in flawless synchronicity.

On 30 August 2022, Metaphysic AI had 'deep-fake' Simon Cowell, Howie Mandel and Terry Crews singing opera on stage.

On 13 September 2022, Metaphysic AI performed with a synthetic version of Elvis Presley for the finals of *America's Got Talent*.

The MIT artificial intelligence project 15.ai has been used for content creation for multiple Internet fandoms, particularly on social media.

In 2023 the bands ABBA and Kiss partnered with Industrial Light & Magic and Pophouse Entertainment to develop deepfake avatars capable of performing virtual concerts.

### Fraud and scams

Fraudsters and scammers make use of deepfakes to trick people into fake investment schemes, financial fraud, cryptocurrencies, sending money, and following endorsements. The likenesses of celebrities and politicians have been used for large-scale scams, as well as those of private individuals, which are used in spearphishing attacks. According to the Better Business Bureau, deepfake scams are becoming more prevalent. These scams are responsible for an estimated $12 billion in fraud losses globally. According to a recent report these numbers are expected to reach $40 Billion over the next three years.

Fake endorsements have misused the identities of celebrities like Taylor Swift, Tom Hanks, Oprah Winfrey, and Elon Musk; news anchors like Gayle King and Sally Bundock; and politicians like Lee Hsien Loong and Jim Chalmers. Videos of them have appeared in online advertisements on YouTube, Facebook, and TikTok, who have policies against synthetic and manipulated media. Ads running these videos are seen by millions of people. A single Medicare fraud campaign had been viewed more than 195 million times across thousands of videos. Deepfakes have been used for: a fake giveaway of Le Creuset cookware for a "shipping fee" without receiving the products, except for hidden monthly charges; weight-loss gummies that charge significantly more than what was said; a fake iPhone giveaway; and fraudulent get-rich-quick, investment, and cryptocurrency schemes.

Audio deepfakes have been used as part of social engineering scams, fooling people into thinking they are receiving instructions from a trusted individual. In 2019, a U.K.-based energy firm's CEO was scammed over the phone when he was ordered to transfer €220,000 into a Hungarian bank account by an individual who reportedly used audio deepfake technology to impersonate the voice of the firm's parent company's chief executive. As of 2023, the combination advances in deepfake technology, which could clone an individual's voice from a recording of a few seconds to a minute, and new text generation tools, enabled automated impersonation scams, targeting victims using a convincing digital clone of a friend or relative.

### Politics

Deepfakes have been used to misrepresent well-known politicians in videos.

- In February 2018, in separate videos, the face of the Argentine President Mauricio Macri had been replaced by the face of Adolf Hitler, and Angela Merkel's face has been replaced with Donald Trump's.
- In April 2018, Jordan Peele collaborated with BuzzFeed to create a deepfake of Barack Obama with Peele's voice; it served as a public service announcement to increase awareness of deepfakes.
- In January 2019, Fox affiliate KCPQ aired a deepfake of Trump during his Oval Office address, mocking his appearance and skin color. The employee found responsible for the video was subsequently fired.
- In June 2019, the United States House Intelligence Committee held hearings on the potential malicious use of deepfakes to sway elections.
- In April 2020, the Belgian branch of Extinction Rebellion published a deepfake video of Belgian Prime Minister Sophie Wilmès on Facebook. The video promoted a possible link between deforestation and COVID-19. It had more than 100,000 views within 24 hours and received many comments. On the Facebook page where the video appeared, many users interpreted the deepfake video as genuine.
- During the 2020 US presidential campaign, many deepfakes surfaced purporting Joe Biden in cognitive decline—falling asleep during an interview, getting lost, and misspeaking—all bolstering rumors of his decline.
- During the 2020 Delhi Legislative Assembly election campaign, the Delhi Bharatiya Janata Party used similar technology to distribute a version of an English-language campaign advertisement by its leader, Manoj Tiwari, translated into Haryanvi to target Haryana voters. A voiceover was provided by an actor, and AI trained using video of Tiwari speeches was used to lip-sync the video to the new voiceover. A party staff member described it as a "positive" use of deepfake technology, which allowed them to "convincingly approach the target audience even if the candidate didn't speak the language of the voter."
- In 2020, Bruno Sartori produced deepfakes parodying politicians like Jair Bolsonaro and Donald Trump.
- In April 2021, politicians in a number of European countries were approached by pranksters Vovan and Lexus, who are accused by critics of working for the Russian state. They impersonated Leonid Volkov, a Russian opposition politician and chief of staff of the Russian opposition leader Alexei Navalny's campaign, allegedly through deepfake technology. However, the pair told *The Verge* that they did not use deepfakes, and just used a look-alike.
- In May 2023, a deepfake video of Vice President Kamala Harris supposedly slurring her words and speaking nonsensically about today, tomorrow and yesterday went viral on social media.
- In June 2023, in the United States, Ron DeSantis's presidential campaign used a deepfake to misrepresent Donald Trump.
- In November 2023, a deepfake video of the German Chancellor Olaf Scholz announcing a plan to ban the political activities of the AfD was uploaded to YouTube by the Zentrum für Politische Schönheit (Center of Political Beauty).
- In March 2024, during India's state assembly elections, deepfake technology was widely employed by political candidates to reach out to voters. Many politicians used AI-generated deepfakes created by startup The Indian Deepfaker, founded by Divyendra Singh Jadoun, to translate their speeches into multiple regional languages, allowing them to engage with diverse linguistic communities across the country. This surge in the use of deepfakes for political campaigns marked a significant shift in electioneering tactics in India.
- In June 2025, Javier Milei's government backed a smear campaign against journalist Mengolini, which was partly based on explicit deepfakes.
- In July 2025, Donald Trump posted a deepfake on his Truth Social account, depicting former president Barack Obama getting arrested at the White House and put in prison.

### Pornography

In 2017, Deepfake pornography prominently surfaced on the Internet, particularly on Reddit. As of 2019, many deepfakes on the internet feature pornography of female celebrities whose likeness is typically used without their consent. A report published in October 2019 by Dutch cybersecurity startup Deeptrace estimated that 96% of all deepfakes online were pornographic. As of 2018, a Daisy Ridley deepfake first captured attention, among others. As of October 2019, most of the deepfake subjects on the internet were British and American actors. However, around a quarter of the subjects are South Korean, the majority of which are K-pop stars.

In June 2019, a downloadable Windows and Linux application called DeepNude was released that used neural networks, specifically generative adversarial networks, to remove clothing from images of women. The app had both a paid and unpaid version, the paid version costing $50. On 27 June the creators removed the application and refunded consumers.

Female celebrities are often a main target when it comes to deepfake pornography. In 2023, deepfake porn videos appeared online of Emma Watson and Scarlett Johansson in a face swapping app. In 2024, deepfake porn images circulated online of Taylor Swift.

Academic studies have reported that women, LGBT people and people of color (particularly activists, politicians and those questioning power) are at higher risk of being targets of promulgation of deepfake pornography. Deepfake technology has become a tool for gender-based harassment and violence, proportionally targeting women and marginalized groups. There is an increasing ethical and equity concerns of intimidation and reputational harm intentions behind this specific media.

Deepfakes have begun to see use in popular social media platforms, notably through Zao, a Chinese deepfake app that allows users to substitute their own faces onto those of characters in scenes from films and television shows such as *Romeo + Juliet* and *Game of Thrones*. The app originally faced scrutiny over its invasive user data and privacy policy, after which the company put out a statement claiming it would revise the policy. In January 2020 Facebook announced that it was introducing new measures to counter this on its platforms.

The Congressional Research Service cited unspecified evidence as showing that foreign intelligence operatives used deepfakes to create social media accounts with the purposes of recruiting individuals with access to classified information.

In 2021, realistic deepfake videos of actor Tom Cruise were released on TikTok, which went viral and garnered more than tens of millions of views. The deepfake videos featured an "artificial intelligence-generated doppelganger" of Cruise doing various activities such as teeing off at the golf course, showing off a coin trick, and biting into a lollipop. The creator of the clips, Belgian VFX Artist Chris Umé, said he first got interested in deepfakes in 2018 and saw the "creative potential" of them.

### Sockpuppets

Deepfake photographs can be used to create sockpuppets, non-existent people, who are active both online and in traditional media. A deepfake photograph appears to have been generated together with a legend for an apparently non-existent person named Oliver Taylor, whose identity was described as a university student in the United Kingdom. The Oliver Taylor persona submitted opinion pieces in several newspapers and was active in online media attacking a British legal academic and his wife, as "terrorist sympathizers". The academic had drawn international attention in 2018 when he commenced a lawsuit in Israel against NSO, a surveillance company, on behalf of people in Mexico who alleged they were victims of NSO's phone hacking technology. *Reuters* could find only scant records for Oliver Taylor and "his" university had no records for him. Many experts agreed that the profile photo is a deepfake. Several newspapers have not retracted articles attributed to him or removed them from their websites. It is feared that such techniques are a new battleground in disinformation.


## Concerns and countermeasures

Though fake photos have long been plentiful, faking motion pictures has been more difficult, and the presence of deepfakes increases the difficulty of classifying videos as genuine or not. AI researcher Alex Champandard has said people should know how fast things can be corrupted with deepfake technology, and that the problem is not a technical one, but rather one to be solved by trust in information and journalism. Computer science associate professor Hao Li of the University of Southern California states that deepfakes created for malicious use, such as fake news, will be even more harmful if nothing is done to spread awareness of deepfake technology. Li predicted that genuine videos and deepfakes would become indistinguishable in as soon as six months, as of October 2019, due to rapid advancement in artificial intelligence and computer graphics. Former Google fraud czar Shuman Ghosemajumder has called deepfakes an area of "societal concern" and said that they will inevitably evolve to a point at which they can be generated automatically, and an individual could use that technology to produce millions of deepfake videos.

### Credibility of information

A primary pitfall is that humanity could fall into an age in which it can no longer be determined whether a medium's content corresponds to the truth. Deepfakes are one of a number of tools for disinformation attack, creating doubt, and undermining trust. They have a potential to interfere with democratic functions in societies, such as identifying collective agendas, debating issues, informing decisions, and solving problems through the exercise of political will. People may also start to dismiss real events as fake.

### Defamation

Deepfakes possess the ability to damage individual entities tremendously. This is because deepfakes are often targeted at one individual, and/or their relations to others in hopes to create a narrative powerful enough to influence public opinion or beliefs. This can be done through deepfake voice phishing, which manipulates audio to create fake phone calls or conversations. Another method of deepfake use is fabricated private remarks, which manipulate media to convey individuals voicing damaging comments. The quality of a negative video or audio does not need to be that high. As long as someone's likeness and actions are recognizable, a deepfake can hurt their reputation.

In September 2020, Microsoft made public that they were developing a Deepfake detection software tool.

### Detection

#### Audio

Detecting fake audio is a challenging task that requires careful analysis of the underlying signal to achieve reliable performance. Deep learning approaches have shown that feature design and masking-based augmentation contribute to improved detection. More recently, approaches that integrate trainable feature extractors with strong and diverse audio augmentation strategies have demonstrated improved performance by enabling the model to learn representations that more effectively capture manipulation artifacts.

Partial deepfake audio detection, in which only a limited portion of the signal is manipulated, has emerged as a significant challenge in the field. This setting introduces additional complexity beyond conventional detection tasks, as it requires not only identifying the presence of spoofing but also accurately localizing the manipulated regions. Moreover, the need to detect short and often subtle spoofed segments within predominantly genuine audio further increases the difficulty of the problem.

#### Video

Most of the academic research surrounding deepfakes focuses on the detection of deepfake videos. One approach to deepfake detection is to use algorithms to recognize patterns and pick up subtle inconsistencies that arise in deepfake videos. For example, researchers have developed automatic systems that examine videos for errors such as irregular blinking patterns of lighting. This approach has been criticized because deepfake detection is characterized by a "moving goal post" where the production of deepfakes continues to change and improve as algorithms to detect deepfakes improve. In order to assess the most effective algorithms for detecting deepfakes, a coalition of leading technology companies hosted the Deepfake Detection Challenge to accelerate the technology for identifying manipulated content. The winning model of the Deepfake Detection Challenge was 65% accurate on the holdout set of 4,000 videos. A team at Massachusetts Institute of Technology published a paper in December 2021 demonstrating that ordinary humans are 69–72% accurate at identifying a random sample of 50 of these videos.

Beyond automated detection, viewers can rely on context and perceptual cues to identify deep fake content. Studies have found that viewers can note inconsistencies with body language, facial features, lighting and audio to mouth movement. These are some ways to identify inauthentic content, but these are not always the most reliable ways to determine whether or not the content is real. Evidence suggests that in natural viewing conditions, viewers are not more likely to recognize deep fake videos over authentic videos. Using content warnings has shown mixed results, where the warnings did not improve the accuracy of detection and also resulted in some individuals incorrectly judging videos as deep fake.

Another team led by Wael AbdAlmageed with Visual Intelligence and Multimedia Analytics Laboratory (VIMAL) of the Information Sciences Institute at the University Of Southern California developed two generations of deepfake detectors based on convolutional neural networks. The first generation used recurrent neural networks to spot spatio-temporal inconsistencies to identify visual artifacts left by the deepfake generation process. The algorithm achieved 96% accuracy on FaceForensics++, the only large-scale deepfake benchmark available at that time. The second generation used end-to-end deep networks to differentiate between artifacts and high-level semantic facial information using two-branch networks. The first branch propagates color information while the other branch suppresses facial content and amplifies low-level frequencies using Laplacian of Gaussian (LoG).

Other techniques suggest that blockchain could be used to verify the source of the media. For instance, a video might have to be verified through the ledger before it is shown on social media platforms. With this technology, only videos from trusted sources would be approved, decreasing the spread of possibly harmful deepfake media.

Digitally signing of all video and imagery by cameras and video cameras, including smartphone cameras, was suggested to fight deepfakes. That allows tracing every photograph or video back to its original owner that can be used to pursue dissidents.

One easy way to uncover deepfake video calls consists in asking the caller to turn sideways.

### Deepfake detection and regulation

Legal experts are actively questioning whether current and emerging regulatory frameworks adequately balance the advancements in deepfake detection with the protection of individual rights. Relevant legislation being scrutinized includes the EU AI Act, the General Data Protection Regulation (GDPR), the Digital Services Act in the European Union, as well as the fragmented state and federal laws in the United States, the Online Safety Act 2023 in the United Kingdom, and China's Administrative Provisions on Deep Synthesis in Internet-Based Information Services (commonly known as the Deep Synthesis Provisions). Scholars are evaluating if these frameworks effectively address the complex interplay between technology, rights, and responsibilities in the context of deepfakes.

### Prevention

Henry Ajder who works for Deeptrace, a company that detects deepfakes, says there are several ways to protect against deepfakes in the workplace. Semantic passwords or secret questions can be used when holding important conversations. Voice authentication and other biometric security features should be up to date. Educate employees about deepfakes.

### Media literacy and deepfakes

Due to the capability of deepfakes to fool viewers and believably mimic a person, research has indicated that the concept of truth through observation cannot be fully relied on. Additionally, literacy of the technology among populations could be called into question due to the relatively new success of convincing deepfakes. When combined with increasing ease of access to the technology, this has led to the concern among some experts that some societies are not prepared to interact with deepfakes organically without potential consequences from sharing misinformation and disinformation. Media literacy has been considered as a potential counter to "prime" a viewer to identify a deepfake when they encounter one organically by encouraging critical thinking. While media literacy education can have conflicting results in the overall success in detecting deepfakes, research has indicated that critical thinking and a skeptical outlook toward a presented piece of media are effective at assisting an individual in determining a deepfake. Media literacy frameworks promote critical analysis of media and the motivations behind the presentation of the associated content and can reduce vulnerability of disinformation. Media literacy shows promise as a potential cognitive countermeasure when interacting with malicious deepfakes.

### Controversies

In March 2024, a video clip was released by Buckingham Palace announcing that Kate Middleton had cancer and was undergoing chemotherapy. The appearance of a ring worn by Middleton in the clip fueled rumors that the clip was a deepfake. Johnathan Perkins, UCLA's Director of Race and Equity, doubted Middleton had cancer, and further speculated that she could be in critical condition or dead.

### Politics

Researchers have studied the capabilities and effects of deepfakes when used in disinformation campaigns, including the potential for deepfakes to circumvent a person's skepticism and influence their views on an issue. Unlike crude misinformation, political propaganda via generative AI often co-opts cultural tropes, visual media, and satire to craft emotionally resonant messages that are difficult to fact-check without losing nuance. Due to the continued advancement in technology that improves deceptive capabilities of deepfakes, some scholars believe that deepfakes could pose a significant threat to democratic societies. Studies have investigated the effects of political deepfakes. In two separate studies focusing on Dutch participants, it was found that deepfakes have varying effects on an audience. As a tool of disinformation, deepfakes did not necessarily produce stronger reactions or shifts in viewpoints than traditional textual disinformation. However, deepfakes did produce a reassuring effect on individuals who held preconceived notions that aligned with the viewpoint promoted by the deepfake disinformation in the study. Additionally, deepfakes are effective when designed to target a specific demographic segment related to a particular issue. "Microtargeting" involves understanding nuanced political issues of a specific demographic to create a targeted deepfake. The targeted deepfake is then used to connect with and influence the viewpoint of that demographic. Targeted deepfakes were found to be notably effective by some researchers. Other researchers in the United Kingdom found that deepfake political disinformation does not have a guaranteed effect on populations beyond indications that it may sow distrust or uncertainty in a source that provides the deepfake. The implications of distrust in sources led those researchers to conclude that deepfakes may have outsized effect in a "low-trust" information environment where public institutions are not trusted by the public.

Across the world, there are key instances where deepfakes have been used to misrepresent well-known politicians and other public figures.

### Liar's dividend

The liar's dividend is a political and social phenomenon in which, when faced with incriminating or embarrassing authentic video or audio recordings of themselves, individuals will claim that the recordings are AI in order to dismiss the claims and gain sympathy.
