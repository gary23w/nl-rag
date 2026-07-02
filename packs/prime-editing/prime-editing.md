---
title: "Prime editing"
source: https://en.wikipedia.org/wiki/Prime_editing
domain: prime-editing
license: CC-BY-SA-4.0
tags: prime editor, reverse transcriptase, pegrna, search and replace
fetched: 2026-07-02
---

# Prime editing

**Prime editing** is a 'search-and-replace' genome editing technology in molecular biology by which the genome of living organisms may be modified. The technology directly writes new genetic information into a targeted DNA site. The most basic prime editor uses a fusion protein, consisting of a catalytically-impaired programmable endonuclease linked to an engineered reverse transcriptase, and a prime editing guide RNA (pegRNA), capable of identifying the target site and providing the new genetic information to replace the target DNA nucleotides. It mediates targeted insertions, deletions, and base-to-base conversions without the need for double strand breaks (DSBs) or donor DNA templates.

The technology has received mainstream press attention due to its potential uses in medical genetics. It utilizes methodologies similar to precursor genome editing technologies, including CRISPR/Cas9 and Base editing.

Prime editing has been used on some animal models of genetic disease, in various plants, and in bacteria. The first human trials for happened in 2024, with both patients enlisted being effectively cured of chronic granulomatous disease.

## Components

### Cas9 prime editors

#### Major components

Prime editing involves three major components:

- **Prime editing guide RNA** **(pegRNA)**: capable of (i) identifying the target nucleotide sequence to be edited, and (ii) encoding new genetic information that replaces the targeted sequence. The pegRNA consists of an extended single guide RNA (sgRNA) containing a primer binding site (PBS) and a reverse transcriptase (RT) template sequence. During genome editing, the primer binding site allows the 3' end of the nicked DNA strand to hybridize to the pegRNA, while the RT template serves as a template for the synthesis of edited genetic information.
- **Cas9 nickase:** With the exclusion of certain variants, all Cas9 prime editors use a nickase. Normally, Cas9 is a nuclease, slicing DNA in half to make blunt-ended double-stranded breaks. The protein uses two domains to do this. The HNH domain cleaves the target strand, the strand of DNA bound to guide RNA, and the RuvC domain cleaves the non-target strand, the target strand's compliment. By swapping the protein's 840th amino acid from a histidine to an alanine, the HNH domain is prevented from cutting. This generates a H840A nickase which can only make a single-stranded break (a nick) in the non-target strand. Most prime editors use a H840A nickase, but inverse prime editors take an opposite approach, instead using a D10A nickase. Here, the 10th amino acid is changed from aspartic acid to alanine. This prevents RuvC from functioning but preserves the HNH domain.
- **Reverse transcriptase:** an enzyme that synthesizes DNA from a single-stranded RNA template.

#### Accessory components

Certain editors have various accessory components:

- **sgRNA:**
- **Small RNA protector protein (La):**
- **circRNA:**
- **MCP:**
- **Rep-X:**
- **Cys4:**
- **T2A:**

### Cas12 prime editors

#### Main components

Cas12 prime editing involves five major components:

- **crRNA:**
- **Cas12a nickase or nuclease:**
- **Reverse transcriptase:**
- **circRNA:**
- **MCP:**

#### Accessory components

- **additional crRNA:**

### OMEGA prime editors

## Editing mechanism

### Original (used by PE1 and 2)

Genomic editing takes place by transfecting cells with the pegRNA and the fusion protein. Transfection is often accomplished by introducing vectors into a cell. Once internalized, the fusion protein nicks the target DNA sequence, exposing a 3'-hydroxyl group that can be used to initiate (prime) the reverse transcription of the RT template portion of the pegRNA. This results in a branched intermediate that contains two DNA flaps: a 3' flap that contains the newly synthesized (edited) sequence, and a 5' flap that contains the dispensable, unedited DNA sequence. The 5' flap is then cleaved by structure-specific endonucleases or 5' exonucleases. This process allows 3' flap ligation, and creates a heteroduplex DNA composed of one edited strand and one unedited strand. The reannealed double stranded DNA contains nucleotide mismatches at the location where editing took place. In order to correct the mismatches, the cells exploit the intrinsic mismatch repair (MMR) mechanism, with two possible outcomes: (i) the information in the edited strand is copied into the complementary strand, permanently installing the edit; (ii) the original nucleotides are re-incorporated into the edited strand, excluding the edit.

### PE3 strategy

Despite its increased efficacy, the edit installed by PE2 might still be removed by mismatch repair of the edited strand. To counter this, the Prime Editor 3 strategy comes with an extra component borrowed from base editing. In addition to the editor itself, PE3 uses a standard Cas9 nickase to exploit DNA repair systems by targeting the opposite non-edited strand. Following the nick on the non-edited strand, DNA repair will use the edited strand as a template, consequentially improving the odds of success.

However, there are drawbacks to this system as the unaltered strand can be nicked prematurely and lead to additional undesired indels.

### Paired prime editing

HOPE strategy: use two complimentary guide RNA pairs to increase chances of edit inclusion (just like Rin and Len guys!)

### PE4 and 5 strategies

Prime editor 4 utilizes the same machinery as PE2, but also includes a plasmid that encodes for dominant negative MMR protein MLH1. Dominant negative MLH1 is able to essentially knock out endogenous MLH1 by inhibition, thereby reducing cellular MMR response and increasing prime editing efficiency.

Prime editor 5 utilizes the same machinery as PE3, but also includes a plasmid that encodes for dominant negative MLH1. Like PE4, this allows for a knockdown of endogenous MMR response, increasing the efficiency of prime editing.

### Twin prime editing

The "twin prime editing" (twinPE) mechanism reported in 2021 allows editing large sequences of DNA – sequences as large as genes – which addresses the method's key drawback. It uses a prime editor protein and two prime editing guide RNAs.

### PASTE

Drag and drop using an Integrase

### PASSIGE

Performs way better than PASTE

### Nucease prime editing

### PEDAR

### PETI

## pegRNA improvements and modifications

### Engineered pegRNA (epegRNA)

Prime editing efficiency can be increased with the use of engineered pegRNAs (epegRNAs). One common issue with traditional pegRNAs is degradation of the 3' end, leading to decreased PE efficiency. epegRNAs have a structured RNA motif added to their 3' end to prevent degradation.

### Xrn1 resistant pegRNA (xr-pegRNA)

Xr-pegRNA is similar to epegRNA in that it adds an additional RNA motif after the primer binding sequence. In this case, these are Xrn1-resistant RNAs (xrRNAs), a group of conserved knot-like structures found in flaviviruses. They impede viral RNA degradation and are highly resistant to unfolding. When testing xrRNAs from five different viruses (the Murray Valley encephalitis virus, West Nile virus, Dengue virus, Yellow fever virus, and Zika virus), researchers found that they improved the efficiency of both PE2 and PE3 strategies while producing around the same or less indels as traditional pegRNA. This finding was consistent across different genes and cell types. Though using a xrRNA-PE3 strategy generally improved efficiency, there were a few sites where xr-PE2 barely differed from xr-PE3. In terms of which xrRNA motif worked best, the exact answer varied by target. However, the Zika motif functioned generally well for both PE2 and PE3 strategies.

Compared to epegRNA, xr-pegRNA has a similar edit-to-indel ratio and improvement in efficiency. However, unlike the RNA pseudoknot from the Moloney murine leukemia virus (mpknot), xr-pegRNA doesn't need an RNA linker to ensure structural stability. This is similar to the evopreQ1 motif, though even that sometimes requires one. Because the linker isn't necessary, using xr-pegRNA would offer better predictability and could prove more convenient.

### Addition of an RNA G-quadruplex

### Split pegRNA with a MS2 stem-loop aptamer

### Engineered non-canonical pegRNAs (npegRNA)

## Protein modifications in animals

Prime editing was developed in the lab of David R. Liu at the Broad Institute and disclosed in Anzalone et al. (2019). Since then prime editing and the research that produced it have received widespread scientific acclaim, being called "revolutionary" and an important part of the future of editing. During the development of this technology, several modifications were done to the components, in order to increase its effectiveness.

### Prime editor 1 (PE1)

Prime editor 1 was a prototype designed to have the minimum components necessary. It consisted of a wild-type Moloney murine leukemia virus (MMLV) reverse transcriptase attached to Cas9 H840A nickase by a flexible protein linker. Originally, the linker was too short and the reverse transcriptase was unable to do its job. However, extending it to 8-15 bases led to detectable editing. During development, the linker was attached to either the C- or N-terminal of the Cas9 protein. Linkage the C terminal proved more efficient, so it was chosen as the final design. Detectable editing efficiencies were observed.

### Prime editor 2 (PE2)

After the success of PE1, researchers chose to modify its reverse transcriptase. This was done to improve DNA synthesis and thus the editor's overall efficiency. They started by searching the literature for previously described mutations. These were found to improve the enzyme's thermostability, processivity, DNA to RNA substrate affinity, or prevent interference by RNaseH. A variety of mutations were combined into nineteen different variants and then tested against each other in human cells.

Researchers began by focusing on thermal stability. They found that a reverse transcriptase combining D200N, L603W, and T330P mutations improved editing efficiency by an average of 6.8-fold for insertions and transversions at five different sites. Following this, the mutant transcriptase was further combined with additional mutations. Adding T306K and W313F improved editing efficiency by an additional 1.3 to 3-fold for insertions or transversions at the same five sites. The resulting prime editor was deemed PE2.

Prime Editor 2 had a substantially higher efficiency than its predecessor when making insertion, deletion, or substitution mutations. Additionally, it was compatible with a shorter primer binding site (PBS) sequence due to its enhanced substrate affinity.

### PE2*

better PE2 with enhanced nuclear localization sequences

### KKH SaCas9 prime editors (SaKKHPE2*)

### HyPE2

### PAM flexible prime editors

### CMP-PE-V1

### Split prime editors

### Nuclease prime editors

Nuclease Prime Editor uses Cas9 nuclease instead of Cas9(H840A) nickase. Unlike prime editor 3 (PE3) that requires dual-nick at both DNA strands to induce efficient prime editing, Nuclease Prime Editor requires only a single pegRNA since the single-gRNA already creates double-strand break instead of single-strand nick.

further research done

another study

upgraded version

### PEmax

PEmax was created to further enhance the improvements made in PE2. To do this, researchers tested twenty-one PE2 variants with different Cas9 mutations, reverse transcriptase codon usages, nuclear localization sequences (NLS), protein linker lengths, and protein linker compositions. Out of the twenty-one created, an editor with a human-optimized reverse transcriptase, a Cas9 with the nucelase enhancing R221K (221st arginine to lysine) and N394K (394th asparagine to lysine) mutations, a 34-aa linker with a bipartite SV40 NLS, and an additional c-Myc NLS at the protein's C-terminal emerged most successful.

Afterwards, the resulting protein (dubbed PEmax) was pitted against other improved prime editors. All were tested on HeLa cells and performed various modifications at seven genomic sites. Notable competitors included PE2*, which has additional NLS sequences, and CMP–PE–V1, which contains high-mobility peptides. PEmax outperformed both at 6/7 sites, with the time it lost to PE2* being within the margin of error.

While improvements vary by cell line and modification, PEmax can be combined with various strategies (PE2max, PE3max, PE4max, PE5max) as well as epegRNA to dramatically enhance editing efficiency. However, note that combining PEmax with PE3 or PE5 leads to a slight increase in indels. This is likely due to the editor's increased nicking ability.

### FnCas9 prime editors

At the time this development was published, most prime editor variants used a SpCas9 H840A nickase. One issue with this protein is that the Cas9 from *Streptococcus pyogenes* can only nick 3 to 4 bases upstream from the PAM, thus limiting the editor's potential. As a workaround, one group made a prime editor using a Cas9 ortholog from *Francisella novicida*. This protein has the same NGG PAM as SpCas9 but different cleavage properties.

On the target strand (the DNA where the guide RNA binds) FnCas9 makes a cut 3 base pairs upstream the PAM, just like SpCas9. However, on the non-target strand, this protein cleaves 6 to 8 bases upstream. By changing the 969th histidine to an alanine, FnCas9 can be converted into a H969A nickase and will only snip the non-target strand. The primer becomes smaller, but the reverse transcriptase template gains an expanded editing range.

Starting off, researchers fused the FnCas9 nickase with a MMLV reverse transcriptase (RT) from a standard PE2 prime editor. They then attempted to optimize it by testing different linker lengths for both the pegRNA (extra nucleotides between the RNA scaffold and reverse transcriptase template) and the protein (amino acids between the Cas9 and RT). It turned out that a protein with a 1x linker (of unknown size) and a normal pegRNA (no linkers at all) worked best. Next, the group used a PE3 strategy to insert two thymines (TT) into various genes. They did this to check how primer binding sequence (PBS) and reverse transcriptase template (RTT) lengths affected efficiency. In general, having a longer PBS made the editor more efficient. The RTT length had an effect, but there was no consistent pattern. Furthermore, the insertion efficiency significantly differed for each gene depending on where the extra PE3 guide RNA nicked.

Comparing the two Cas9s, the one from *Francisella novicida* had more variation in efficiency and was overall worse than the one from *Streptococcus pyogenes* (3.82-87.56% vs 29.34-95.18%) when using a PE3 strategy. That might've been due to FnCas9's weaker nicking ability, something found in another experiment. To compensate, the group created a new strategy deemed PE4. Details on this can be found in the Editing mechanism section.

#### Editor with a relaxed YG PAM

Using previous research, the same group engineered a FnCas9 prime editor with a relaxed PAM-recognition site. Mutating the 1369th glutamic acid to arginine (E1369R), 1449th glutamic acid to histidine (E1449H), and 1556th argenine to alanine (R1556A) generates a Cas9 that recognizes a YG PAM. This RHA-FnCas9 is capable of targeting sequences ending in TG or CG (something SpCas9 can't do) and further expands the editor's range of targets.

### IN-PE2

### Prime editor 6 (PE6)

Smaller than normal. There are multiple variants that can be used in different applications (a,b,c,d)

### Miniature CjCas9 prime editor (mini-PE)

### Cas12a prime editors

### Yeast-improved prime editor (PE_Y18)

### Prime editor 7 (PE7)

### Inverse prime editors (iPE and ciPE)

### Very precise prime editor (xPE and vPE)

## Protein modifications in plants

## Protein modifications in bacteria

### OMEGA-based prime editing

### PE-STAR

## Applications

### Cell cultures

### Animal models

Efficient prime editing in mouse brain,liver and heart with dual AAVs

zebrafish

### Agriculture

PE is among recently introduced technologies which allow the transfer of single-nucleotide polymorphisms (SNPs) from one individual crop plant to another. PE is precise enough to be used to recreate an arbitrary SNP in an arbitrary target, including deletions, insertions, and all 12 point mutations without also needing to perform a double-stranded break or carry a donating template.

Ultra-efficient tomato prime editor

rice

### Gene therapy

In 2024, PM359, a gene therapy developed by Prime Medicine, became the first prime editor to enter clinical trials for human use. Prime Medicine reported in December 2025 that two chronic granulomatous disease patients treated with PM359 had been "effectively cured" of the disease.

### Other

Prime editors may be used in gene drives. A prime editor may be incorporated into the *Cleaver* half of a *Cleave and Rescue* *ClvR* system. In this case it is not meant to perform a precise alteration but instead to merely disrupt.

## Methods of delivery

Base editors used for prime editing require delivery of both a protein and RNA molecule into living cells. Introducing exogenous gene editing technologies into living organisms is a significant challenge. One potential way to introduce a base editor into animals and plants is to package the base editor into a viral capsid. The target organism can then be transduced by the virus to synthesize the base editor *in vivo*. Common laboratory vectors of transduction such as lentivirus cause immune responses in humans, so proposed human therapies often centered around adeno-associated virus (AAV) because AAV infections are largely asymptomatic. Unfortunately, the effective packaging capacity of AAV vectors is small, approximately 4.4kb not including inverted terminal repeats. As a comparison, an SpCas9-reverse transcriptase fusion protein is 6.3kb, which does not even account for the lengthened guide RNA necessary for targeting and priming the site of interest. However, successful delivery in mice has been achieved by splitting the editor into two AAV vectors or by using an adenovirus, which has a larger packaging capacity.

## Comparison to base editors and traditional CRISPR/Cas9 genome editing

Although additional research is required to improve the efficiency of prime editing, the technology offers promising scientific improvements over other gene editing tools. The prime editing technology has the potential to correct the vast majority of pathogenic alleles that cause genetic diseases, as it can repair insertions, deletions, and nucleotide substitutions.

### Advantages

The prime editing tool offers advantages over traditional gene editing technologies. CRISPR/Cas9 edits rely on double-strand breaks and non-homologous end joining (NHEJ) or homology-directed repair (HDR) to fix DNA breaks, while the prime editing system employs single-strand breaks and DNA mismatch repair. This is an important feature of this technology given that DNA repair mechanisms such as NHEJ and HDR, generate unwanted, random insertions or deletions (indels). These are byproducts that complicate the retrieval of cells carrying the correct edit. Prime editors do not frequently create these indel byproducts, suggesting that prime editors can be more precise than earlier tools.

The prime editing system introduces single-stranded DNA breaks, as with base editors, instead of the double-stranded DNA breaks observed in other editing tools, such as CRISPR/Cas9 editing. Collectively, base editing and prime editing offer complementary strengths and weaknesses for making targeted transition mutations. Base editors offer higher editing efficiency and fewer indel byproducts if the desired edit is a transition point mutation and a PAM sequence exists roughly 15 bases from the target site. However, because the prime editing technology does not require a precisely positioned PAM sequence to target a nucleotide sequence, it offers more flexibility and editing precision. Remarkably, prime editors allow all types of substitutions, both transitions and transversions, to be installed into the target sequence. Cytosine base editing and adenine BE can already perform precise base transitions but base transversions cannot be achieved with these base editors. Prime editing performs transversions with high efficiency. PE can insert up to 44bp, delete up to 80, or combinations thereof.

Because the prime system involves three separate DNA binding events (between (i) the guide sequence and the target DNA, (ii) the primer binding site and the target DNA, and (iii) the 3' end of the nicked DNA strand and the pegRNA), it has been suggested to have fewer undesirable off-target effects than CRISPR/Cas9.

### Limitations

There is considerable interest in applying gene-editing methods to the treatment of diseases with a genetic component. However, there are multiple challenges associated with this approach. An effective treatment would require editing of a large number of target cells, which in turn would require an effective method of delivery and a great level of tissue specificity.

As of 2019, prime editing looks promising for relatively small genetic alterations, but more research needs to be conducted to evaluate whether the technology is efficient in making larger alterations, such as targeted insertions and deletions. Larger genetic alterations would require a longer RT template, which could hinder the efficient delivery of pegRNA to target cells. Furthermore, a pegRNA containing a long RT template could become vulnerable to damage caused by cellular enzymes. Prime editing in plants suffers from low efficiency ranging from zero to a few percent and needs significant improvement.

Some of these limitations have been mitigated by recent improvements to the prime editors, including motifs that protect pegRNAs from degradation. Further research is needed before prime editing could be used to correct pathogenic alleles in humans. Research has also shown that inhibition of certain MMR proteins, including MLH1 can improve prime editing efficiency.
