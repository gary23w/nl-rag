---
title: "Nanopore sequencing"
source: https://en.wikipedia.org/wiki/Nanopore_sequencing
domain: next-gen-sequencing
license: CC-BY-SA-4.0
tags: next generation sequencing, massively parallel sequencing, sequencing by synthesis, nanopore sequencing
fetched: 2026-07-02
---

# Nanopore sequencing

**Nanopore sequencing** is a third generation approach used in the sequencing of biopolymers — specifically, polynucleotides in the form of DNA or RNA.

Nanopore sequencing allows a single molecule of DNA or RNA be sequenced without PCR amplification or chemical labeling. Nanopore sequencing has the potential to offer relatively low-cost genotyping, high mobility for testing, and rapid processing of samples, including the ability to display real-time results. It has been proposed for rapid identification of viral pathogens, monitoring ebola, environmental monitoring, food safety monitoring, human genome sequencing, plant genome sequencing, monitoring of antibiotic resistance, haplotyping and other applications.

## Development

Nanopore sequencing took 25 years to materialize. David Deamer was one of the first to push the idea. In 1989 he sketched out a plan to push single-strands of DNA through a protein nanopore embedded into a thin membrane as part his work to synthesize RNA. Realizing that the approach might allow DNA sequencing, Deamer and his team spent a decade refining the concept. In 1999 they published the first paper using the term 'nanopore sequencing' and two years later produced an image capturing a DNA hairpin passing through a nanopore in real time.

Another foundation for nanopore sequencing was the work of Hagan Bayley's team, who from the 1990s independently developed stochastic sensing, a technique that measures the change in an ionic current passing through a nanopore to determine the concentration and identity of a substance. By 2005 Bayley had made progress with the DNA sequencing method. He co-founded Oxford Nanopore to push the technology. In 2014 the company released its first portable nanopore sequencing device. This made it possible for DNA sequencing to be carried out almost anywhere, even with limited resources. A quarter of the world's SARS-CoV-2 viral genomes were sequenced with nanopore devices. The technology offers an important tool for combating antimicrobial resistance.

## Principles

The biological or solid-state membrane, where the nanopore is found, is surrounded by an electrolyte solution. The membrane splits the solution into two chambers. Applying a bias voltage across the membrane induces an electric field that drives charged particles, in this case the ions, into motion. This effect is known as electrophoresis. For high enough concentrations, the electrolyte solution is well distributed and the voltage drop concentrates near and inside the nanopore. This means charged particles in the solution feel a force only from the electric field when they are near the pore region. This region is typically referred to as the capture region. Inside the capture region, ions have a directed motion that can be recorded as a steady ionic current by placing electrodes near the membrane. A nano-sized polymer such as DNA or protein placed in one of the chambers has a net charge that feels a force from the electric field in the capture region. The molecule approaches this capture region aided by Brownian motion. Any attraction it might have to the surface of the membrane. Once inside the nanopore, the molecule translocates via a combination of electro-phoretic, electro-osmotic and sometimes thermo-phoretic forces. Inside the pore the molecule occupies a volume that partially restricts the ion flow, observed as an ionic current drop. Based on various factors such as geometry, size and chemical composition, the change in magnitude of the ionic current and the duration of the translocation vary. Different molecules can then be sensed and potentially identified based on this current modulation.

### Base identification

The magnitude of the electric current density across a nanopore surface depends on the nanopore's dimensions and the composition of DNA or RNA that is occupying the nanopore. Sequencing was made possible because passing through the channel of the nanopore, the samples cause characteristic changes in the density of the electric current. The total charge flowing through a nanopore channel is equal to the surface integral of electric current density flux across the nanopore unit normal surfaces.

## Types

### Biological

Biological nanopore sequencing relies on the use of transmembrane proteins, called protein nanopores, in particular, formed by protein toxins, that are embedded in lipid membranes so as to create size dependent porous surfaces - with nanometer scale "holes" distributed across the membranes. Sufficiently low translocation velocity can be attained through the incorporation of various proteins that facilitate the movement of DNA or RNA through the pores of the lipid membranes.

#### Alpha hemolysin

Alpha hemolysin (αHL), a nanopore from bacteria that causes lysis of red blood cells, has been studied for over 15 years. To this point, studies have shown that all four bases can be identified using ionic current measured across the αHL pore. The structure of αHL is advantageous to identify specific bases moving through the pore. The αHL pore is ~10 nm long, with two distinct 5 nm sections. The upper section consists of a larger, vestibule-like structure and the lower section consists of three possible recognition sites (R1, R2, R3), and is able to discriminate between each base.

Sequencing using αHL has been developed through basic study and structural mutations, moving towards the sequencing of very long reads. Protein mutation of αHL has improved the detection abilities of the pore. The next proposed step is to bind an exonuclease onto the αHL pore. The enzyme would periodically cleave single bases, enabling the pore to identify successive bases. Coupling an exonuclease to the biological pore would slow the translocation of the DNA through the pore, and increase the accuracy of data acquisition.

Notably, theorists have shown that sequencing via exonuclease enzymes as described here is not feasible. This is mainly due to diffusion related effects imposing a limit on the capture probability of each nucleotide as it is cleaved. This results in a significant probability that a nucleotide is either not captured before it diffuses into the bulk or captured out of order, and therefore is not properly sequenced by the nanopore, leading to insertion and deletion errors. Therefore, major changes are needed to this method before it can be considered a viable strategy.

A recent study has pointed to the ability of αHL to detect nucleotides at two separate sites in the lower half of the pore. The R1 and R2 sites enable each base to be monitored twice as it moves through the pore, creating 16 different measurable ionic current values instead of 4. This method improves upon the single read through the nanopore by doubling the sites that the sequence is read per nanopore.

#### MspA

Mycobacterium smegmatis porin A (MspA) is the second biological nanopore currently being investigated for DNA sequencing. The MspA pore has been identified as a potential improvement over αHL due to a more favorable structure. The pore is described as a goblet with a thick rim and a diameter of 1.2 nm at the bottom of the pore. A natural MspA, while favorable for DNA sequencing because of shape and diameter, has a negative core that prohibited single stranded DNA(ssDNA) translocation. The natural nanopore was modified to improve translocation by replacing three negatively charged aspartic acids with neutral asparagines.

The electric current detection of nucleotides across the membrane has been shown to be tenfold more specific than αHL for identifying bases. Utilizing this improved specificity, a group at the University of Washington has proposed using double stranded DNA (dsDNA) between each single stranded molecule to hold the base in the reading section of the pore. The dsDNA would halt the base in the correct section of the pore and enable identification of the nucleotide. A 2011 grant was awarded to a collaboration from UC Santa Cruz, the University of Washington, and Northeastern University to improve the base recognition of MspA using phi29 polymerase in conjunction with the pore. MspA with electric current detection can also be used to sequence peptides.

#### CsgG

The CsgG nanopore is a 36-stranded β-barrel protein from *Escherichia coli*. The CsgG pore has a nine-fold circular symmetry and a single, well-defined constriction that is approximately 1 nm wide.

A significant development in its use for sequencing is the creation of a dual-constriction pore by combining CsgG with its partner protein, CsgF. The N-terminal region of CsgF binds inside the CsgG barrel, creating a second constriction that is roughly 1.5 nm wide and separated from the original CsgG constriction by about 2.5 nm. This dual-constriction structure is a major advantage because both constrictions contribute to the electrical signal modulation as a single strand of DNA moves through the pore.

This dual-reading capability significantly improves sequencing accuracy, particularly for homopolymer regions (stretches of identical bases), which are a known source of errors in nanopore sequencing. DNA sequencing using this dual-constriction CsgG:CsgF pore has been shown to improve single-read accuracy by 25-70% in homopolymers up to 9 nucleotides long. The addition of the second constriction increases the signal complexity, leading to higher accuracy in calling the length of homopolymers compared to a single-constriction CsgG pore.

### Solid state

Solid state nanopore sequencing approaches, unlike biological nanopore sequencing, do not incorporate proteins into their systems. Instead, solid state nanopore technology uses various metal or metal alloy substrates with nanometer sized pores that allow DNA or RNA to pass through. These substrates most often serve integral roles in the sequence recognition of nucleic acids as they translocate through the channels along the substrates.

#### Tunneling current

Measurement of electron tunneling through bases as ssDNA translocates through the nanopore is an improved solid state nanopore sequencing method. Most research has focused on proving bases could be determined using electron tunneling. These studies were conducted using a scanning probe microscope as the sensing electrode, and have proved that bases can be identified by specific tunneling currents. After the proof of principle research, a functional system must be created to couple the solid state pore and sensing devices.

Researchers at the Harvard Nanopore group have engineered solid state pores with single walled carbon nanotubes across the diameter of the pore. Arrays of pores are created and chemical vapor deposition is used to create nanotubes that grow across the array. Once a nanotube has grown across a pore, the diameter of the pore is adjusted to the desired size. Successful creation of a nanotube coupled with a pore is an important step towards identifying bases as the ssDNA translocates through the solid state pore.

Another method is the use of nanoelectrodes on either side of a pore. The electrodes are specifically created to enable a solid state nanopore's formation between the two electrodes. This technology could be used to not only sense the bases but to help control base translocation speed and orientation.

Another technique to support ionic current based sensing is called Nanopore electrometry, which has been also recently proposed theoretically. This is where the modulations in electric field is utilised instead of the modulations in ionic current for nanopore sensing.

#### Fluorescence

An effective technique to determine a DNA sequence has been developed using solid state nanopores and fluorescence. This fluorescence sequencing method converts each base into a characteristic representation of multiple nucleotides which bind to a fluorescent probe strand-forming dsDNA. With the two color system proposed, each base is identified by two separate fluorescences, and will therefore be converted into two specific sequences. Probes consist of a fluorophore and quencher at the start and end of each sequence, respectively. Each fluorophore will be extinguished by the quencher at the end of the preceding sequence. When the dsDNA is translocating through a solid state nanopore, the probe strand will be stripped off, and the upstream fluorophore will fluoresce.

This sequencing method has a capacity of 50-250 bases per second per pore, and a four color fluorophore system (each base could be converted to one sequence instead of two), will sequence over 500 bases per second. Advantages of this method are based on the clear sequencing readout—using a camera instead of noisy current methods. However, the method does require sample preparation to convert each base into an expanded binary code before sequencing. Instead of one base being identified as it translocates through the pore, ~12 bases are required to find the sequence of one base.

## Purposes

Nanopore devices can be used for eDNA analysis in environmental monitoring and crop epidemiology. These can be miniaturised more than earlier technologies and so have been made into portable devices, especially the MinION. The MinION is especially known for the studies of crop viruses by Boykin et al 2018 & Shaffer 2019 and studies of species prevalence by Menegon et al 2017 and Pomerantz et al 2018. Owing to its high portability, low cost and easiness to use for rapid sequencing applications, it also raised ethical, legal and social concerns along with other next generation sequencing technologies. SARS-CoV-2 variants in Prague wastewater were detected by nanopore-based sequencing. Sequencing of sub-sewershed samples benefits epidemiological early warning systems.

## Comparison between types

|   | Biological | Solid State |
|---|---|---|
| Low Translocation Velocity | ✓ |   |
| Dimensional Reproducibility | ✓ |   |
| Stress Tolerance |   | ✓ |
| Longevity |   | ✓ |
| Ease of Fabrication |   | ✓ |

### Major constraints

1. Low Translocation Velocity:  The speed at which a sample passes through a unit's pore slow enough to be measured
2. Dimensional Reproducibility:  The likelihood of a unit's pore to be made the proper size
3. Stress Tolerance:  The sensitivity of a unit to internal environmental conditions
4. Longevity: The length of time that a unit is expected to remain functioning
5. Ease of Fabrication: The ability to produce a unit- usually in regards to mass-production

### Biological: advantages and disadvantages

Biological nanopore sequencing systems have several fundamental characteristics that make them advantageous as compared with solid state systems- with each advantageous characteristic of this design approach stemming from the incorporation of proteins into their technology. Uniform pore structure, the precise control of sample translocation through pore channels, and even the detection of individual nucleotides in samples can be facilitated by unique proteins from a variety of organism types.

The use of proteins in biological nanopore sequencing systems, despite the various benefits, also brings with it some negative characteristics. The sensitivity of the proteins in these systems to local environmental stress has a large impact on the longevity of the units, overall. One example is that a motor protein may only unzip samples with sufficient speed at a certain pH range while not operating fast enough outside of the range- this constraint impacts the functionality of the whole sequencing unit. Another example is that a transmembrane porin may only operate reliably for a certain number of runs before it breaks down. Both of these examples would have to be controlled for in the design of any viable biological nanopore system- something that may be difficult to achieve while keeping the costs of such a technology as low and as competitive, to other systems, as possible.

## Adaptive Sampling

Adaptive sampling can be applied to nanopore sequencing to target or enrich a single gene, reducing the inefficiency and cost associated with whole-genome sequencing. Functionally, adaptive nanopore sequencing proceeds by the same mechanism as nanopore sequencing, where a single stranded polynucleotide (DNA or RNA) passes through a pore in a sequencing membrane, and characteristic changes in current can be used to identify each base. In adaptive sampling, the electrical signal is used in real-time to decode the genome, and a decision is made whether to continue sequencing. If the sequence is not of interest, the membrane potential is reversed and the strand is rejected. Computational processing of the live read must outpace nanopore sequencing, which proceeds at a rate of ~450 nt/s, to provide ample time for decision making.

The two primary modes of adaptive sampling are enrichment and depletion. In enrichment mode, regions of interest (ROIs) are supplied. Each strand is sequenced for a “read-until” decision phase. Then, if the ROI has not been identified within the sequence, the strand is rejected. In depletion mode, however, targets that are not of interest are selected, and a hit leads to rejection. This reduces the cost and effort of sequencing contaminants and opens opportunities for improved microbiome metagenome analysis. Because nanopore sequencing devices can selectively eject DNA strands in real time, they enable fully computational approaches to targeted sequencing.

### Computational Methods

The success rate of the adaptive nanopore sequencing relies on how instantaneously the computer algorithm can perform. Oxford Nanopore Technologies provides commercially available nanopore sequencing technology. They also produce algorithms for adaptive sequencing, like Guppy and MinKNOW. Tools such as ReadBouncer enhance the scalability and accuracy of adaptive sampling by quickly determining the nucleotide strand being read. Further tools, such as AI deep learning or NanoDeep (a Convolutional Neural Network), improve the identification of complex and complicated sequences. By using AI to process the electrical signals, these computational methods are capable of sampling multiple ~4000 nucleotide "read-until" steps within milliseconds. Given these computational advancements, adaptive sampling is capable of outpacing the ~ 450 nt/s procession of the oligonucleotide strand through the pore .

### Limitations

While strictly computational targeted sequencing is promising, this results in the need for fast identification of on-target reads. Additionally, many mapping methods require computationally intensive base calling (the mapping of electrical signal to nucleotide bases). This has resulted in various steps taken such as the open-source mapper UNCALLED which can quickly match nanopore current signals to a reference sequence. Even though adaptive nanopore sequencing is made more practical by the design of these types of tools, more research is needed to identify false positives / negatives or issues of signal variability .

Variability in sample composition and sequencing conditions can increase signal noise, and the system software may misinterpret the sequence. Furthermore, the system has to analyze the signals, make a prediction, and then reach a decision, all in a short time. Even though the method relies on an advanced computation algorithm, signal variability and sequencing errors can still limit the overall accuracy of the results .

### Applications

Adaptive nanopore sequencing can be used to enrich target sequences and cut down on unnecessary sequencing time in long reads. When coupled with adaptive sampling, nanopore sequencing has shown to be a reliable and fast long-read sequencing technique, specifically useful in genetic diagnoses of Mendelian diseases. Because adaptive sequencing enables target enrichment without library preparation steps it has been utilized effectively in a proof-of-concept study investigating structural variants in tumor suppressor genes. While breast cancer is not a Mendelian disease, some types are driven by mutations of the BRCA1/2 genes following similar hereditary inheritance. Adaptive sequencing has produced enrichment of the BRCA1 gene allowing for reduced steps in the sequencing process. In “conventional” methods of enrichment, DNA processing steps such as amplification by PCR are required. However, avoiding this process altogether reduces cost and improves efficiency. Overall, this has shown that analyzing pathogenic activity via adaptive nanopore sequencing is a possible method for various tumor suppressor genes. .

## Challenges

One challenge for the 'strand sequencing' method was in refining the method to improve its resolution to be able to detect single bases. In the early papers methods, a nucleotide needed to be repeated in a sequence about 100 times successively in order to produce a measurable characteristic change. This low resolution is because the DNA strand moves rapidly at the rate of 1 to 5μs per base through the nanopore. This makes recording difficult and prone to background noise, failing in obtaining single-nucleotide resolution. As of 2006, the problem has been tackled by either improving the recording technology or by controlling the speed of DNA strand by various protein engineering strategies and Oxford Nanopore employs a 'kmer approach', analyzing more than one base at any one time so that stretches of DNA are subject to repeat interrogation as the strand moves through the nanopore one base at a time. Various techniques including algorithmic have been used to improve the performance of the MinION technology since it was first made available to users. More recently effects of single bases due to secondary structure or released mononucleotides have been shown.

In 2010 Hagan Bayley proposed that creating two recognition sites within an alpha-hemolysin pore may confer advantages in base recognition.

As of 2009, one challenge for the 'exonuclease approach', where a processive enzyme feeds individual bases, in the correct order, into the nanopore, has been to integrate the exonuclease and the nanopore detection systems. In particular, the problem is that when an exonuclease hydrolyzes the phosphodiester bonds between nucleotides in DNA, the subsequently released nucleotide is not necessarily guaranteed to directly move into, say, a nearby alpha-hemolysin nanopore. In 2009, one idea has been to attach the exonuclease to the nanopore, perhaps through biotinylation to the beta barrel hemolysin.

The central pore of the protein may be lined with charged residues arranged so that the positive and negative charges appear on opposite sides of the pore. However, this mechanism is primarily discriminatory and does not constitute a mechanism to guide nucleotides down some particular path.
