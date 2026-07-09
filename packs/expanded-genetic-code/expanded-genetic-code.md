---
title: "Expanded genetic code"
source: https://en.wikipedia.org/wiki/Expanded_genetic_code
domain: expanded-genetic-code
license: CC-BY-SA-4.0
tags: expanded genetic code
fetched: 2026-07-09
---

# Expanded genetic code

An **expanded genetic code** is an artificially modified genetic code in which one or more specific codons have been re-allocated to encode an amino acid that is not among the 22 common naturally-encoded proteinogenic amino acids.

The key prerequisites to expand the genetic code are:

- the non-standard amino acid to encode,
- an unused codon to adopt,
- a tRNA that recognizes this codon, and
- a tRNA synthetase that recognizes only that tRNA and only the non-standard amino acid.

Expanding the genetic code is an area of research of synthetic biology, an applied biological discipline whose goal is to engineer living systems for useful purposes. The genetic code expansion enriches the repertoire of useful tools available to science.

In May 2019, researchers, in a milestone effort, reported the creation of a new synthetic (possibly artificial) form of viable life, a variant of the bacteria *Escherichia coli*, by reducing the natural number of 64 codons in the bacterial genome to 61 codons (eliminating two out of the six codons coding for serine and one out of three stop codons) – of which 59 used to encode 20 amino acids.

## Introduction

It is noteworthy that the genetic code for all organisms is basically the same, so that all living beings use the same 'genetic language'. In general, the introduction of new functional unnatural amino acids into proteins of living cells breaks the universality of the genetic language, which ideally leads to alternative life forms. Proteins are produced thanks to the translational system molecules, which decode the RNA messages into a string of amino acids. The translation of genetic information contained in messenger RNA (mRNA) into a protein is catalysed by ribosomes. Transfer RNAs (tRNA) are used as keys to decode the mRNA into its encoded polypeptide. The tRNA recognizes a specific three nucleotide codon in the mRNA with a complementary sequence called the anticodon on one of its loops. Each three-nucleotide codon is translated into one of twenty naturally occurring amino acids. There is at least one tRNA for any codon, and sometimes multiple codons code for the same amino acid. Many tRNAs are compatible with several codons. An enzyme called an aminoacyl tRNA synthetase covalently attaches the amino acid to the appropriate tRNA. Most cells have a different synthetase for each amino acid (20 or more synthetases). On the other hand, some bacteria have fewer than 20 aminoacyl tRNA synthetases, and introduce the "missing" amino acid(s) by modification of a structurally related amino acid by an aminotransferase enzyme. A feature exploited in the expansion of the genetic code is the fact that the aminoacyl tRNA synthetase often does not recognize the anticodon, but another part of the tRNA, meaning that if the anticodon were to be mutated the encoding of that amino acid would change to a new codon. In the ribosome, the information in mRNA is translated into a specific amino acid when the mRNA codon matches with the complementary anticodon of a tRNA, and the attached amino acid is added onto a growing polypeptide chain. When it is released from the ribosome, the polypeptide chain folds into a functioning protein.

In order to incorporate a novel amino acid into the genetic code several changes are required. First, for successful translation of a novel amino acid, the codon to which the novel amino acid is assigned cannot already code for one of the 20 natural amino acids. Usually a nonsense codon (stop codon) or a four-base codon are used. Second, a novel pair of tRNA and aminoacyl tRNA synthetase are required, these are called the orthogonal set. The orthogonal set must not crosstalk with the endogenous tRNA and synthetase sets, while still being functionally compatible with the ribosome and other components of the translation apparatus. The active site of the synthetase is modified to accept only the novel amino acid. Most often, a library of mutant synthetases is screened for one which charges the tRNA with the desired amino acid. The synthetase is also modified to recognize only the orthogonal tRNA. The tRNA synthetase pair is often engineered in other bacteria or eukaryotic cells.

In this area of research, the 20 encoded proteinogenic amino acids are referred to as standard amino acids, or alternatively as natural or canonical amino acids, while the added amino acids are called non-standard amino acids (NSAAs), or unnatural amino acids (UAAs; term not used in papers dealing with natural non-proteinogenic amino acids, such as phosphoserine), or non-canonical amino acids.

## Non-standard amino acids

The first element of the system is the amino acid that is added to the genetic code of a certain strain of organism.

Over 71 different NSAAs have been added to different strains of *E. coli*, yeast or mammalian cells. Due to technical details (easier chemical synthesis of NSAAs, less crosstalk and easier evolution of the aminoacyl-tRNA synthase), the NSAAs are generally larger than standard amino acids and most often have a phenylalanine core but with a large variety of different substituents. These allow a large repertoire of new functions, such as labeling (see figure), as a fluorescent reporter (*e.g.* dansyl alanine) or to produce translational proteins in *E. coli* with Eukaryotic post-translational modifications (*e.g.* phosphoserine, phosphothreonine, and phosphotyrosine).

The founding work was performed by Rolf Furter, who used the yeast tRNAPhe/PheRS pair to incorporate p-fluorophenylalanine in *E. coli*.

Unnatural amino acids incorporated into proteins include heavy atom-containing amino acids to facilitate certain x-ray crystallographic studies; amino acids with novel steric/packing and electronic properties; photocrosslinking amino acids which can be used to probe protein-protein interactions in vitro or in vivo; keto, acetylene, azide, and boronate-containing amino acids which can be used to selectively introduce a large number of biophysical probes, tags, and novel chemical functional groups into proteins *in vitro* or *in vivo*; redox active amino acids to probe and modulate electron transfer; photocaged and photoisomerizable amino acids to photoregulate biological processes; metal binding amino acids for catalysis and metal ion sensing; amino acids that contain fluorescent or infra-red active side chains to probe protein structure and dynamics; α-hydroxy acids and D-amino acids as probes of backbone conformation and hydrogen bonding interactions; and sulfated amino acids and mimetics of phosphorylated amino acids as probes of post-translational modifications.

Availability of the non-standard amino acid requires that the organism either import it from the medium or biosynthesize it. In the first case, the unnatural amino acid is first synthesized chemically in its optically pure L-form. It is then added to the growth medium of the cell. A library of compounds is usually tested for use in incorporation of the new amino acid, but this is not always necessary, for example, various transport systems can handle unnatural amino acids with apolar side-chains. In the second case, a biosynthetic pathway needs to be engineered, for example, an *E. coli* strain that biosynthesizes a novel amino acid (p-aminophenylalanine) from basic carbon sources and includes it in its genetic code. Another example is the production of phosphoserine, a natural metabolite, which required alteration of its pathway flux to increase its production.

## Codon assignment

Another element of the system is a codon to allocate to the new amino acid.

A major problem for the genetic code expansion is that there are no free codons. The genetic code has a non-random layout that shows tell-tale signs of various phases of primordial evolution, however, it has since frozen into place and is near-universally conserved. Nevertheless, some codons are rarer than others. In fact, in *E. coli* (and all organisms) the codon usage is not equal, but presents several rare codons (see table), the rarest being the amber stop codon (UAG).

| Codon | Amino acid | Abundance (%) |
|---|---|---|
| UUU | Phe (F) | 1.9 |
| UUC | Phe (F) | 1.8 |
| UUA | Leu (L) | 1.0 |
| UUG | Leu (L) | 1.1 |
| CUU | Leu (L) | 1.0 |
| CUC | Leu (L) | 0.9 |
| CUA | Leu (L) | 0.3 |
| CUG | Leu (L) | 5.2 |
| AUU | Ile (I) | 2.7 |
| AUC | Ile (I) | 2.7 |
| AUA | Ile (I) | 0.4 |
| AUG | Met (M) | 2.6 |
| GUU | Val (V) | 2.0 |
| GUC | Val (V) | 1.4 |
| GUA | Val (V) | 1.2 |
| GUG | Val (V) | 2.4 |
| UCU | Ser (S) | 1.1 |
| UCC | Ser (S) | 1.0 |
| UCA | Ser (S) | 0.7 |
| UCG | Ser (S) | 0.8 |
| CCU | Pro (P) | 0.7 |
| CCC | Pro (P) | 0.4 |
| CCA | Pro (P) | 0.8 |
| CCG | Pro (P) | 2.4 |
| ACU | Thr (T) | 1.2 |
| ACC | Thr (T) | 2.4 |
| ACA | Thr (T) | 0.1 |
| ACG | Thr (T) | 1.3 |
| GCU | Ala (A) | 1.8 |
| GCC | Ala (A) | 2.3 |
| GCA | Ala (A) | 0.1 |
| GCG | Ala (A) | 3.2 |
| UAU | Tyr (Y) | 1.6 |
| UAC | Tyr (Y) | 1.4 |
| UAA | Stop | 0.2 |
| UAG | Stop | 0.03 |
| CAU | His (H) | 1.2 |
| CAC | His (H) | 1.1 |
| CAA | Gln (Q) | 1.3 |
| CAG | Gln (Q) | 2.9 |
| AAU | Asn (N) | 1.6 |
| AAC | Asn (N) | 2.6 |
| AAG | Lys (K) | 3.8 |
| AAA | Lys (K) | 1.2 |
| GAU | Asp (D) | 3.3 |
| GAC | Asp (D) | 2.3 |
| GAA | Glu (E) | 4.4 |
| GAG | Glu (E) | 1.9 |
| UGU | Cys (C) | 0.4 |
| UGC | Cys (C) | 0.6 |
| UGA | Stop | 0.1 |
| UGG | Trp (W) | 1.4 |
| CGU | Arg (R) | 2.4 |
| CGC | Arg (R) | 2.2 |
| CGA | Arg (R) | 0.3 |
| CGG | Arg (R) | 0.5 |
| AGU | Ser (S) | 0.7 |
| AGC | Ser (S) | 1.5 |
| AGA | Ser (S) | 0.2 |
| AGG | Ser (S) | 0.2 |
| GGU | Gly (G) | 2.8 |
| GGC | Gly (G) | 3.0 |
| GGC | Gly (G) | 0.7 |
| GGA | Gly (G) | 0.9 |

### Amber codon suppression

The possibility of reassigning codons was realized by Normanly *et al.* in 1990, when a viable mutant strain of *E. coli* read through the UAG ("amber") stop codon. This was possible thanks to the rarity of this codon and the fact that release factor 1 alone makes the amber codon terminate translation. Later, in the Schultz lab, the tRNATyr/tyrosyl-tRNA synthetase (TyrRS) from *Methanococcus jannaschii*, an archaebacterium, was used to introduce a tyrosine instead of STOP, the default value of the amber codon. This was possible because of the differences between the endogenous bacterial syntheses and the orthologous archaeal synthase, which do not recognize each other. Subsequently, the group evolved the orthologonal tRNA/synthase pair to utilize the non-standard amino acid *O*-methyltyrosine. This was followed by the larger naphthylalanine and the photocrosslinking benzoylphenylalanine, which proved the potential utility of the system.

The amber codon is the least used codon in *Escherichia coli*, but hijacking it results in a substantial loss of fitness. One study, in fact, found that there were at least 83 peptides majorly affected by the readthrough. Additionally, the labelling was incomplete. As a consequence, several strains have been made to reduce the fitness cost, including the removal of all amber codons from the genome. In most *E. coli* K-12 strains (viz. *Escherichia coli* (molecular biology) for strain pedigrees) there are 314 UAG stop codons. Consequently, a gargantuan amount of work has gone into the replacement of these. One approach pioneered by the group of Prof. George Church from Harvard, was dubbed MAGE in CAGE: this relied on a multiplex transformation and subsequent strain recombination to remove all UAG codons—the latter part presented a halting point in a first paper, but was overcome. This resulted in the *E. coli* strain C321.ΔA, which lacks all UAG codons and RF1. This allowed an experiment to be done with this strain to make it "addicted" to the amino acid biphenylalanine by evolving several key enzymes to require it structurally, therefore putting its expanded genetic code under positive selection.

### Rare sense codon reassignment

In addition to the amber codon, rare sense codons have also been considered for use. The AGG codon codes for arginine, but a strain has been successfully modified to make it code for 6-*N*-allyloxycarbonyl-lysine. Another candidate is the AUA codon, which is unusual in that its respective tRNA has to differentiate against AUG that codes for methionine (primordially, isoleucine, hence its location). In order to do this, the AUA tRNA has a special base, lysidine. The deletion of the synthase (*tilS*) was possible thanks to the replacement of the native tRNA with that of *Mycoplasma mobile* (no lysidine). The reduced fitness is a first step towards pressuring the strain to lose all instances of AUA, allowing it to be used for genetic code expansion.

*E. coli* strain Syn61 is a variant where all uses of TCG (Ser), TCA (Ser), TAG (STOP) codons are eliminated using a synthetic genome (see § Recoded synthetic genome below) containing 18,214 replacements. By removing the unneeded tRNA genes and RF1, strain Syn61Δ3 was produced. The three freed codons then become available for adding three special residues, as demonstrated in strain "Syn61Δ3(ev4)". A newer strain Syn57 frees up 7 codons (101,553 replacements) and is expected to allow more special residues to be added.

### Four base (quadruplet) codons

While triplet codons are the basis of the genetic code in nature, programmed +1 frameshift is a natural process that allows the use of a four-nucleotide sequence (quadruplet codon) to encode an amino acid. Recent developments in genetic code engineering also showed that quadruplet codon could be used to encode non-standard amino acids under experimental conditions. This allowed the simultaneous usage of two unnatural amino acids, *p*-azidophenylalanine (pAzF) and N6-[(2-propynyloxy)carbonyl]lysine (CAK), which cross-link with each other by Huisgen cycloaddition. Quadrupled decoding in wild-type, non-recoded strains is very inefficient. This stems from the fact that the interaction between engineered tRNAs with ternary complexes or other translation components is not as favorable and strong as with cell endogenous translation elements. This problem can be overcome by specifically engineering and evolving tRNA that can decode quadruplet codons in non-recoded strains. Up to 4 different quadruplet orthogonal tRNA/tRNA synthethase pairs can be generated in this manner. Quadruplet codon decoding approach has also been applied to the construction of an HIV-1 vaccine.

## tRNA/synthetase pair

Another key element is the tRNA/synthetase pair.

The orthologous set of synthetase and tRNA can be mutated and screened through directed evolution to charge the tRNA with a different, even novel, amino acid. Mutations to the plasmid containing the pair can be introduced by error-prone PCR or through degenerate primers for the synthetase's active site. Selection involves multiple rounds of a two-step process, where the plasmid is transferred into cells expressing chloramphenicol acetyl transferase with a premature amber codon. In the presence of toxic chloramphenicol and the non-natural amino acid, the surviving cells will have overridden the amber codon using the orthogonal tRNA aminoacylated with either the standard amino acids or the non-natural one. To remove the former, the plasmid is inserted into cells with a barnase gene (toxic) with a premature amber codon but without the non-natural amino acid, removing all the orthogonal syntheses that do not specifically recognize the non-natural amino acid. In addition to the recoding of the tRNA to a different codon, they can be mutated to recognize a four-base codon, allowing additional free coding options. The non-natural amino acid, as a result, introduces diverse physicochemical and biological properties in order to be used as a tool to explore protein structure and function or to create novel or enhanced protein for practical purposes.

### Orthogonal sets in model organisms

The orthogonal pairs of synthetase and tRNA that work for one organism may not work for another, as the synthetase may mis-aminoacylate endogenous tRNAs or the tRNA be mis-aminoacylated itself by an endogenous synthetase. As a result, the sets created to date differ between organisms.

| Pair | Source | *E. coli* | Yeast | Mammals | Notes and references |
|---|---|---|---|---|---|
| tRNATyr-TyrRS | *Methanococcus jannaschii* | Yes | No | No |   |
| tRNALys–LysRS | *Pyrococcus horikoshii* | Yes | No | No |   |
| tRNAGlu–GluRS | *Pyrococcus horikoshii* | Yes | No | No |   |
| tRNALeu–LeuRS | tRNA: mutant *Halobacterium* sp. RS: *Methanobacterium thermoautotrophicum* | Yes | No | No |   |
| tRNAAmber-PylRS | *Methanosarcina barkeri* and *Methanosarcina mazei* | Yes | Yes | Yes |   |
| tRNAAmber-3-iodotyrosyl-RS | RS: variant *Methanocaldococcus jannaschii* aaRS | Yes | No | No |   |
| tRNATyr/Amber-TyrRS | *Escherichia coli* | No | Yes | No | Reported in 2003, mentioned in 2014 LeuRS |
| tRNA*i*Met-GlnRS | tRNA: human RS: *Escherichia coli* | No | Yes | No | Switched to Amber codon. |
| tRNA*i*fMet-TyrRS | tRNA: *Escherichia coli* RS: *S. cerevisiae* | Yes | Yes | No | Switched to Amber codon. |
| tRNALeu/Amber-LeuRS | *Escherichia coli* | No | Yes | Yes | Reported in 2004 and mutated for 2-Aminooctanoic acid, *o*-methyl tyrosine, and *o*-nitrobenzyl cysteine. Evolved in yeast for 4,5-dimethoxy-2-nitrobenzyl serine, tested in mice and mammalian cells with photosensitive 4,5-dimethoxy-2-nitrobenzyl-cysteine. |
| tRNATyr-TyrRS | *Bacillus stearothermophilus* | No | No | Yes |   |
| tRNATrp-TrpRS | *Bacillus subtilis*, RS modified | No | No | Yes | New AA is 5-OH Trp. |

In 2017, a mouse engineered with an extended genetic code that can produce proteins with unnatural amino acids was reported.

## Orthogonal ribosomes

Similarly to orthogonal tRNAs and aminoacyl tRNA synthetases (aaRSs), orthogonal ribosomes have been engineered to work in parallel to the natural ribosomes. Orthogonal ribosomes ideally use different mRNA transcripts than their natural counterparts and ultimately should draw on a separate pool of tRNA as well. This should alleviate some of the loss of fitness which currently still arises from techniques such as Amber codon suppression. Additionally, orthogonal ribosomes can be mutated and optimized for particular tasks, like the recognition of quadruplet codons. Such an optimization is not possible, or highly disadvantageous for natural ribosomes.

### o-Ribosome

In 2005, three sets of ribosomes were published, which did not recognize natural mRNA, but instead translated a separate pool of orthogonal mRNA (o-mRNA). This was achieved by changing the recognition sequence of the mRNA, the Shine-Dalgarno sequence, and the corresponding recognition sequence in the 16S rRNA of ribosomes, the so-called Anti-Shine-Dalgarno-Sequence. This way the base pairing, which is usually lost if either sequence is mutated, stays available. However the mutations in the 16S rRNA were not limited to the obviously base-pairing nucleotides of the classical Anti-Shine-Dalgarno sequence.

### Ribo-X

In 2007, the group of Jason W. Chin presented an orthogonal ribosome, which was optimized for Amber codon suppression. The 16S rRNA was mutated in such a way that it bound the release factor RF1 less strongly than the natural ribosome does. This ribosome did not eliminate the problem of lowered cell fitness caused by suppressed stop codons in natural proteins. However through the improved specificity it raised the yields of correctly synthesized target protein significantly (from ~20% to >60% percent for one amber codon to be suppressed and from <1% to >20% for two amber codons).

### Ribo-Q

In 2010, the group of Jason W. Chin presented a further optimized version of the orthogonal ribosome. The Ribo-Q is a 16S rRNA optimized to recognize tRNAs, which have quadruplet anti-codons to recognize quadruplet codons, instead of the natural triplet codons. With this approach the number of possible codons rises from 64 to 256. Even accounting for a variety of stop codons, more than 200 different amino acids could potentially be encoded this way.

### Ribosome stapling

The orthogonal ribosomes described above all focus on optimizing the 16S rRNA. Thus far, this optimized 16S rRNA was combined with natural large-subunits to form orthogonal ribosomes. If the 23S rRNA, the main RNA-component of the large ribosomal subunit, is to be optimized as well, it had to be assured, that there was no crosstalk in the assembly of orthogonal and natural ribosomes (see figure B). To ensure that optimized 23S rRNA would only form into ribosomes with the optimized 16S rRNA, the two rRNAs were combined into one transcript. By inserting the sequence for the 23S rRNA into a loop-region of the 16S rRNA sequence, both subunits still adopt functioning folds. Since the two rRNAs are linked and thus in constant proximity, they preferably bind each other, not other free floating ribosomal subunits.

### Engineered peptidyl transferase center

In 2014, it was shown that by altering the peptidyl transferase center of the 23S rRNA, ribosomes could be created which draw on orthogonal pools of tRNA. The 3' end of tRNAs is universally conserved to be CCA. The two cytidines base pair with two guanines the 23S rRNA to bind the tRNA to the ribosome. This interaction is required for translational fidelity. However, by co-mutating the binding nucleotides in such a way, that they can still base pair, the translational fidelity can be conserved. The 3'-end of the tRNA is mutated from CCA to CGA, while two cytidine nucleotides in the ribosomes A- and P-sites are mutated to guanidine. This leads to ribosomes which do not accept naturally occurring tRNAs as substrates and to tRNAs, which cannot be used as substrate by natural ribosomes. To use such tRNAs effectively, they would have to be aminoacylated by specific, orthogonal aaRSs. Most naturally occurring aaRSs recognize the 3'-end of their corresponding tRNA. aaRSs for these 3'-mutated tRNAs are not available yet. Thus far, this system has only been shown to work in an in-vitro translation setting where the aminoacylation of the orthogonal tRNA was achieved using so called "flexizymes". Pioneered by the laboratory of Hiroaki Suga at the University of Tokyo, flexizymes are ribozymes with tRNA-amino-aclylation activity.

## Applications

With an expanded genetic code, the unnatural amino acid can be genetically directed to any chosen site in the protein of interest. The high efficiency and fidelity of this process allows a better control of the placement of the modification compared to modifying the protein post-translationally, which, in general, will target all amino acids of the same type, such as the thiol group of cysteine and the amino group of lysine. Also, an expanded genetic code allows modifications to be carried out *in vivo*. The ability to site-specifically direct lab-synthesized chemical moieties into proteins allows many types of studies that would otherwise be extremely difficult, such as:

- Probing protein structure and function: By using amino acids with slightly different size such as *O*-methyltyrosine or dansyl alanine instead of tyrosine, and by inserting genetically coded reporter moieties (color-changing and/or spin-active) into selected protein sites, chemical information about the protein's structure and function can be measured.
- Probing the role of post-translational modifications in protein structure and function: By using amino acids that mimic post-translational modifications such as phosphoserine, biologically active protein can be obtained, and the site-specific nature of the amino acid incorporation can lead to information on how the position, density, and distribution of protein phosphorylation effect protein function.
- Identifying and regulating protein activity: By using photocaged aminoacids, protein function can be "switched" on or off by illuminating the organism.
- Changing the mode of action of a protein: One can start with the gene for a protein that binds a certain sequence of DNA and, by inserting a chemically active amino acid into the binding site, convert it to a protein that cuts the DNA rather than binding it.
- Improving immunogenicity and overcoming self-tolerance: By replacing strategically chosen tyrosines with *p*-nitro phenylalanine, a tolerated self-protein can be made immunogenic.
- Selective destruction of selected cellular components: using an expanded genetic code, unnatural, destructive chemical moieties (sometimes called "chemical warheads") can be incorporated into proteins that target specific cellular components.
- Producing better protein: the evolution of T7 bacteriophages on a non-evolving *E. coli* strain that encoded 3-iodotyrosine on the amber codon, resulted in a population fitter than wild-type thanks to the presence of iodotyrosine in its proteome
- Probing protein localization and protein-protein interaction in bacteria.

## Future

The expansion of the genetic code is still in its infancy. Current methodology uses only one non-standard amino acid at the time, whereas ideally multiple could be used. In fact, the group of Jason Chin has recently broken the record for a genetically recoded *E. coli* strain that can simultaneously incorporate up to 4 unnatural amino acids. Moreover, there has been development in software that allows combination of orthogonal ribosomes and unnatural tRNA/RS pairs in order to improve protein yield and fidelity.

### Recoded synthetic genome

One way to achieve the encoding of multiple unnatural amino acids is by synthesising a rewritten genome. In 2010, at the cost of $40 million an organism, *Mycoplasma laboratorium*, was constructed that was controlled by a synthetic, but not recoded, genome. The first genetically recoded organism was created by a collaboration between George Church's and Farren Isaacs' labs, when the wild type *E. coli* MG1655 was recoded in such a way that all 321 known UAG stop codons were substituted with synonymous UAA codons and release factor 1 was knocked out in order to eliminate the interaction with the exogenous stop codon and improve unnatural protein synthesis. In 2019, *Escherichia coli* Syn61 was created, with a 4 megabase recoded genome consisting of only 61 codons instead of the natural 64. In addition to the elimination of the usage of rare codons, the specificity of the system needs to be increased as many tRNA recognise several codons

### Expanded genetic alphabet

Another approach is to expand the number of nucleobases to increase the coding capacity.

An unnatural base pair (UBP) is a designed subunit (or nucleobase) of DNA which is created in a laboratory and does not occur in nature. A demonstration of UBPs were achieved *in vitro* by Ichiro Hirao's group at RIKEN institute in Japan. In 2002, they developed an unnatural base pair between 2-amino-8-(2-thienyl)purine (s) and pyridine-2-one (y) that functions *in vitro* in transcription and translation for the site-specific incorporation of non-standard amino acids into proteins. In 2006, they created 7-(2-thienyl)imidazo[4,5-b]pyridine (Ds) and pyrrole-2-carbaldehyde (Pa) as a third base pair for replication and transcription. Afterward, Ds and 4-[3-(6-aminohexanamido)-1-propynyl]-2-nitropyrrole (Px) was discovered as a high fidelity pair in PCR amplification. In 2013, they applied the Ds-Px pair to DNA aptamer generation by *in vitro* selection (SELEX) and demonstrated the genetic alphabet expansion significantly augment DNA aptamer affinities to target proteins.

In 2012, a group of American scientists led by Floyd Romesberg, a chemical biologist at the Scripps Research Institute in San Diego, California, published that his team designed an unnatural base pair (UBP). The two new artificial nucleotides or *Unnatural Base Pair* (UBP) were named "d5SICS" and "dNaM." More technically, these artificial nucleotides bearing hydrophobic nucleobases, feature two fused aromatic rings that form a (d5SICS–dNaM) complex or base pair in DNA. In 2014 the same team from the Scripps Research Institute reported that they synthesized a stretch of circular DNA known as a plasmid containing natural T-A and C-G base pairs along with the best-performing UBP Romesberg's laboratory had designed, and inserted it into cells of the common bacterium *E. coli* that successfully replicated the unnatural base pairs through multiple generations. This is the first known example of a living organism passing along an expanded genetic code to subsequent generations. This was in part achieved by the addition of a supportive algal gene that expresses a nucleotide triphosphate transporter which efficiently imports the triphosphates of both d5SICSTP and dNaMTP into *E. coli* bacteria. Then, the natural bacterial replication pathways use them to accurately replicate the plasmid containing d5SICS–dNaM.

The successful incorporation of a third base pair into a living micro-organism is a significant breakthrough toward the goal of greatly expanding the number of amino acids which can be encoded by DNA, thereby expanding the potential for living organisms to produce novel proteins. The artificial strings of DNA do not encode for anything yet, but scientists speculate they could be designed to manufacture new proteins which could have industrial or pharmaceutical uses.

In May 2014, researchers announced that they had successfully introduced two new artificial nucleotides into bacterial DNA, and by including individual artificial nucleotides in the culture media, were able to induce amplification of the plasmids containing the artificial nucleotides by a factor of 2 × 107 (24 doublings); they did not create mRNA or proteins able to use the artificial nucleotides.

### Selective pressure incorporation (SPI) method for production of alloproteins

There have been many studies that have produced protein with non-standard amino acids, but they do not alter the genetic code. These protein, called alloprotein, are made by incubating cells with an unnatural amino acid in the absence of a similar coded amino acid in order for the former to be incorporated into protein in place of the latter, for example L-2-aminohexanoic acid (Ahx) for methionine (Met).

These studies rely on the natural promiscuous activity of the aminoacyl tRNA synthetase to add to its target tRNA an unnatural amino acid (i.e. analog) similar to the natural substrate, for example methionyl-tRNA synthase's mistaking isoleucine for methionine. In protein crystallography, for example, the addition of selenomethionine to the media of a culture of a methionine-auxotrophic strain results in proteins containing selenomethionine as opposed to methionine (*viz.* Multi-wavelength anomalous dispersion for reason). Another example is that L-photo-leucine and photomethionine are added instead of leucine and methionine to cross-label protein. Similarly, some tellurium-tolerant fungi can incorporate tellurocysteine and telluromethionine into their protein instead of cysteine and methionine. The objective of expanding the genetic code is more radical as it does not replace an amino acid, but it adds one or more to the code. On the other hand, proteome-wide replacements are most efficiently performed by global amino acid substitutions. For example, global proteome-wide substitutions of natural amino acids with fluorinated analogs have been attempted in *E. coli* and *B. subtilis*. A complete tryptophan substitution with thienopyrrole-alanine in response to 20899 UGG codons in *E. coli* was reported in 2015 by Budisa and Söll. Moreover, many biological phenomena, such as protein folding and stability, are based on synergistic effects at many positions in the protein sequence.

In this context, the SPI method generates recombinant protein variants or alloproteins directly by substitution of natural amino acids with unnatural counterparts. An amino acid auxotrophic expression host is supplemented with an amino acid analog during target protein expression. This approach avoids the pitfalls of suppression-based methods and it is superior to it in terms of efficiency, reproducibility and an extremely simple experimental setup. Numerous studies demonstrated how global substitution of canonical amino acids with various isosteric analogs caused minimal structural perturbations but dramatic changes in thermodynamic, folding, aggregation spectral properties and enzymatic activity.

### *in vitro* synthesis

The genetic code expansion described above is *in vivo*. An alternative is the change of coding *in vitro* translation experiments. This requires the depletion of all tRNAs and the selective reintroduction of certain aminoacylated-tRNAs, some chemically aminoacylated.

### Chemical synthesis

There are several techniques to produce peptides chemically, generally it is by solid-phase protection chemistry. This means that any (protected) amino acid can be added into the nascent sequence.

In November 2017, a team from the Scripps Research Institute reported having constructed a semi-synthetic *E. coli* bacteria genome using six different nucleotides (versus four found in nature). The two extra 'letters' form a third, unnatural base pair. The resulting organisms were able to thrive and synthesize proteins using "unnatural amino acids". The unnatural base pair used is dNaM–dTPT3. This unnatural base pair has been demonstrated previously, but this is the first report of transcription and translation of proteins using an unnatural base pair.
