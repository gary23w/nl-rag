---
title: "Fungal DNA barcoding"
source: https://en.wikipedia.org/wiki/Fungal_DNA_barcoding
domain: fungal-dna-barcoding
license: CC-BY-SA-4.0
tags: fungal dna barcoding
fetched: 2026-07-08
---

# Fungal DNA barcoding

**Fungal DNA barcoding** is the process of identifying species of the biological kingdom Fungi through the amplification and sequencing of specific DNA sequences and their comparison with sequences deposited in a DNA barcode database such as the ISHAM reference database, or the Barcode of Life Data System (BOLD). In this attempt, DNA barcoding relies on universal genes that are ideally present in all fungi with the same degree of sequence variation. The interspecific variation, i.e., the variation between species, in the chosen DNA barcode gene should exceed the intraspecific (within-species) variation.

A fundamental problem in fungal systematics is the existence of teleomorphic and anamorphic stages in their life cycles. These morphs usually differ drastically in their phenotypic appearance, preventing a straightforward association of the asexual anamorph with the sexual teleomorph. Moreover, fungal species can comprise multiple strains that can vary in their morphology or in traits such as carbon- and nitrogen utilisation, which has often led to their description as different species, eventually producing long lists of synonyms. Fungal DNA barcoding can help to identify and associate anamorphic and teleomorphic stages of fungi, and through that to reduce the confusing multitude of fungus names. For this reason, mycologists were among the first to spearhead the investigation of species discrimination by means of DNA sequences, at least 10 years earlier than the DNA barcoding proposal for animals by Paul D. N. Hebert and colleagues in 2003, who popularised the term "DNA barcoding".

The success of identification of fungi by means of DNA barcode sequences stands and falls with the quantitative (completeness) and qualitative (level of identification) aspect of the reference database. Without a database covering a broad taxonomic range of fungi, many identification queries will not result in a satisfyingly close match. Likewise, without a substantial curatorial effort to maintain the records at a high taxonomic level of identification, queries – even when they might have a close or exact match in the reference database – will not be informative if the closest match is only identified to phylum or class level.

Another crucial prerequisite for DNA barcoding is the ability to unambiguously trace the provenance of DNA barcode data back to the originally sampled specimen, the so-called voucher specimen. This is common practice in biology along with the description of new taxa, where the voucher specimens, on which the taxonomic description is based, become the type specimens. When the identity of a certain taxon (or a genetic sequence in the case of DNA barcoding) is in doubt, the original specimen can be re-examined to review and ideally solve the issue. Voucher specimens should be clearly labelled as such, including a permanent voucher identifier that unambiguously connects the specimen with the DNA barcode data derived from it. Furthermore, these voucher specimens should be deposited in publicly accessible repositories like scientific collections or herbaria to preserve them for future reference and to facilitate research involving the deposited specimens.

## Barcode DNA markers

### Internal Transcribed Spacer (ITS) – the primary fungal barcode

In fungi, the Internal transcribed spacer (*ITS*) is a roughly 600 base pairs long region in the ribosomal tandem repeat gene cluster of the nuclear genome. The region is flanked by the DNA sequences for the ribosomal small subunit (SSU) or 18S subunit at the 5' end, and by the large subunit (LSU) or 28S subunit at the 3' end. The Internal Transcribed Spacer itself consists of two parts, *ITS1* and *ITS2*, which are separated from each other by the 5.8S subunit nested between them. Like the flanking 18S and 28S subunits, the 5.8S subunit contains a highly conserved DNA sequence, as they code for structural parts of the ribosome, which is a key component in intracellular protein synthesis.

Due to several advantages of *ITS* (see below) and a comprehensive amount of sequence data accumulated in the 1990s and early 2000s, Begerow et al. (2010) and Schoch et al. (2012) proposed the *ITS* region as primary DNA barcode region for the genetic identification of fungi.

UNITE is an open *ITS* barcoding database for fungi and all other eukaryotes.

#### Primers

The conserved flanking regions of 18S and 28S serve as anchor points for the primers used for PCR amplification of the *ITS* region. Moreover, the conserved nested 5.8S region allows for the construction of "internal" primers, i.e., primers attaching to complementary sequences within the ITS region. White et al. (1990) proposed such internal primers, named ITS2 and ITS3, along with the flanking primers ITS1 and ITS4 in the 18S and the 28S subunit, respectively. Due to their almost universal applicability to ITS sequencing in fungi, these primers are still in wide use today. Optimised primers specifically for ITS sequencing in Dikarya (comprising Basidiomycota and Ascomycota) have been proposed by Toju et al. (2012).

For the majority of fungi, the ITS primers proposed by White et al. (1990) have become the standard primers used for PCR amplification (with the most common pairing being ITS1 + ITS4). These primers are as follows:

| Forward primers: *ITS1*: 5'-TCCGTAGGTGAACCTGCGG-3' *ITS2*: 5'-GCTGCGTTCTTCCATCGATGC-3' *ITS5*: 5'-GGAAGTAAAAGTCGTAACAAG G-3' | Reverse primers: *ITS3*: 5'-GCATCGATGAAGAACGCAGC-3' *ITS4*: 5'-TCCTCCGCTTATTGATATGC-3' |
|---|---|

#### Advantages and shortcomings

A major advantage of using the ITS region as molecular marker and fungal DNA barcode is that the entire ribosomal gene cluster is arranged in tandem repeats, i.e., in multiple copies. This allows for its PCR amplification and Sanger sequencing even from small material samples (given the DNA is not fragmented due to age or other degenerative influences). Hence, a high PCR success rate is usually observed when amplifying *ITS*. However, this success rate varies greatly among fungal groups, from 65% in non-Dikarya (including the now paraphyletic Mucoromycotina, the Chytridiomycota and the Blastocladiomycota) to 100% in Saccharomycotina and Basidiomycota (with the exception of very low success in Pucciniomycotina). Furthermore, the choice of primers for *ITS* amplification can introduce biases towards certain taxonomic fungus groups. For example, the "universal" *ITS* primers fail to amplify about 10% of the tested fungal specimens.

The tandem repeats of the ribosomal gene cluster cause the problem of significant intragenomic sequence heterogeneity observed among *ITS* copies of several fungal groups. In Sanger sequencing, this will cause *ITS* sequence reads of different lengths to superpose each other, potentially rendering the resulting chromatograph unreadable. Furthermore, because of the non-coding nature of the *ITS* region that can lead to a substantial amount of indels, it is impossible to consistently align *ITS* sequences from highly divergent species for further bigger-scale phylogenetic analyses. The degree of intragenomic sequence heterogeneity can be investigated in more detail through molecular cloning of the initially PCR-amplified ITS sequences, followed by sequencing of the clones. This procedure of initial PCR amplification, followed by cloning of the amplicons and finally sequencing of the cloned PCR products is the most common approach of obtaining *ITS* sequences for DNA metabarcoding of environmental samples, in which a multitude of different fungal species can be present simultaneously. However, this approach of sequencing after cloning was rarely done for the *ITS* sequences that make up the reference libraries used for DNA barcode-aided identification, thus potentially giving an underestimate of the existing *ITS* sequence variation in many samples.

The weighted arithmetic mean of the intraspecific (within-species) *ITS* variability among fungi is 2.51%. This variability, however, can range from 0% for example in *Serpula lacrymans* (n=93 samples) over 0.19% in *Tuber melanosporum* (n=179) up to 15.72% in *Rhizoctonia solani* (n=608), or even 24.75% in *Pisolithus tinctorius* (n=113). In cases of high intraspecific *ITS* variability, the application of a threshold of 3% sequence variability – a canonical upper value for intraspecific variation – will therefore lead to a higher estimate of operational taxonomic units (OTUs), i.e., putative species, than there actually are in a sample. In the case of medically relevant fungal species, a more strict threshold of 2.5% *ITS* variability allows only around 75% of all species to be accurately identified to the species level.

On the other hand, morphologically well-defined, but evolutionarily young species complexes or sibling species may only differ (if at all) in a few nucleotides of the *ITS* sequences. Solely relying on *ITS* barcode data for the identification of such species pairs or complexes may thus obscure the actual diversity and might lead to misidentification if not accompanied by the investigation of morphological and ecological features and/or comparison of additional diagnostic genetic markers. For some taxa, *ITS* (or its *ITS2* part) is not variable enough as fungal DNA barcode, as for example has been shown in *Aspergillus*, *Cladosporium*, *Fusarium* and *Penicillium*. Efforts to define a universally applicable threshold value of *ITS* variability that demarcates intraspecific from interspecific (between-species) variability thus remain futile.

Nonetheless, the probability of correct species identification with the *ITS* region is high in the Dikarya, and especially so in Basidiomycota, where even the *ITS1* part is often sufficient to identify the species. However, its discrimination power is partly superseded by that of the DNA-directed RNA polymerase II subunit *RPB1* (see also below).

Due to the shortcomings of ITS-based primary fungal DNA barcoding, the necessity of establishing a second DNA barcode marker was expressed. Several attempts were made to establish other genetic markers that could serve as additional DNA barcodes, similar to the situation in plants, where the plastidial genes *rbcL*, *matK* and *trnH-psbA*, as well as the nuclear *ITS* are often used in combination for DNA barcoding.

### Translational elongation factor 1α (TEF1α) – the secondary fungal barcode

The translational elongation factor 1α is part of the eukaryotic elongation factor 1 complex, whose main function is to facilitate the elongation of the amino acid chain of a polypeptide during the translation process of gene expression.

Stielow et al. (2015) investigated the *TEF1α* gene, among a number of others, as potential genetic marker for fungal DNA barcoding. The *TEF1α* gene coding for the translational elongation factor 1α is generally considered to have a slow mutation rate, and it is therefore generally better suited for investigating older splits deeper in the phylogenetic history of an organism group. Despite this, the authors conclude that *TEF1α* is the most promising candidate for an additional DNA barcode marker in fungi as it also features sequence regions of higher mutation rates. Following this, a quality-controlled reference database was established and merged with the previously existing ISHAM-ITS database for fungal ITS DNA barcodes to form the ISHAM database.

*TEF1α* has been successfully used to identify a new species of *Cantharellus* from Texas and distinguish it from a morphologically similar species. In the genera *Ochroconis* and *Verruconis* (Sympoventuriaceae, Venturiales), however, the marker does not allow distinction of all species. *TEF1α* has also been used in phylogenetic analyses at the genus level, e.g. in the case of *Cantharellus* and the entomopathogenic *Beauveria*, and for the phylogenetics of early-diverging fungal lineages.

#### Primers

*TEF1α* primers used in the broad-scale screening of the performance of DNA barcode gene candidates of Stielow et al. (2015) were the forward primer *EF1-983F* with the sequence 5'-GCYCCYGGHCAYCGTGAYTTYAT-3', and the reverse primer *EF1-1567R* with the sequence 5'-ACHGTRCCRATACCACCRATCTT-3'. In addition, a number of new primers was developed, with the primer pair in bold resulting in a high average amplification success of 88%:

| Forward primers: ***EF1-1018F***: 5'-GAYTTCATCAAGAACATGAT-3' *EF1-1002F*: 5'-TTCATCAAGAACATGAT-3' *Al33_alternative_f*: 5'-GARTTYGARGCYGGTATCTC-3' *EF1_alternative_3f*: 5'-TTYGARGCYGGTATCTC-3' | Reverse primers: ***EF1-1620R***: 5'-GACGTTGAADCCRACRTTGTC-3' *EF1-1688R*: 5'-GCTATCATCACAATGGACGTTCTTGGAG-3' *EF1_alternative_3r*: 5'-GAVACRTTCTTGACGTTGAA-3' |
|---|---|

Primers used for the investigation of Rhizophydiales and especially *Batrachochytrium dendrobatidis*, a pathogen of amphibia, are the forward primer *tef1F* with the nucleotide sequence 5'-TACAARTGYGGTGGTATYGACA-3', and the reverse primer *tef1R* with the sequence 5'-ACNGACTTGACYTCAGTRGT-3'. These primers also successfully amplified the majority of *Cantharellus* species investigated by Buyck et al. (2014), with the exception of a few species for which more specific primers were developed: the forward primer *tef-1Fcanth* with the sequence 5'-AGCATGGGTDCTYGACAAG-3', and the reverse primer *tef-1Rcanth* with the sequence 5'-CCAATYTTRTAYACATCYTGGAG-3'.

### D1/D2 domain of the LSU ribosomal RNA

The D1/D2 domain is part of the nuclear large subunit (28S) ribosomal RNA, and it is therefore located in the same ribosomal tandem repeat gene cluster as the Internal Transcribed Spacer (*ITS*). But unlike the non-coding ITS sequences, the D1/D2 domain contains coding sequence. With about 600 base pairs it is about the same nucleotide sequence length as *ITS*, which makes amplification and sequencing rather straightforward, an advantage that has led to the accumulation of an extensive amount of *D1/D2* sequence data especially for yeasts.

Regarding the molecular identification of basidiomycetous yeasts, *D1/D2* (or *ITS*) can be used alone. However, Fell et al. (2000) and Scorzetti et al. (2002) recommend the combined analysis of the *D1/D2* and *ITS* regions, a practice that later became the standard required information for describing new taxa of asco- and basidiomycetous yeasts. When attempting to identify early diverging fungal lineages, the study of Schoch et al. (2012), comparing the identification performance of different genetic markers, showed that the large subunit (as well as the small subunit) of the ribosomal RNA performs better than *ITS* or *RPB1*.

#### Primers

For basidiomycetous yeasts, the forward primer *F63* with the sequence 5'-GCATATCAATAAGCGGAGGAAAAG-3', and the reverse primer *LR3* with the sequence 5'-GGTCCGTGTTTCAAGACGG-3' have been successfully used for PCR amplification of the D1/D23 domain. The D1/D2 domain of ascomycetous yeasts like *Candida* can be amplified with the forward primer *NL-1* (same as *F63*) and the reverse primer *NL-4* (same as *LR3*).

### RNA polymerase II subunit RPB1

The RNA polymerase II subunit *RPB1* is the largest subunit of the RNA polymerase II. In *Saccharomyces cerevisiae*, it is encoded by the *RPO21* gene. PCR amplification success of *RPB1* is very taxon-dependent, ranging from 70 to 80% in Ascomycota to 14% in early diverging fungal lineages. Apart from the early diverging lineages, *RPB1* has a high rate of species identification in all fungal groups. In the species-rich Pezizomycotina it even outperforms ITS.

In a study comparing the identification performance of four genes, *RPB1* was among the most effective genes when combining two genes in the analysis: combined analysis with either *ITS* or with the large subunit ribosomal RNA yielded the highest identification success.

Other studies also used RPB2, the second-largest subunit of the RNA polymerase II, e.g. for studying the phylogenetic relationships among species of the genus *Cantharellus* or for a phylogenetic study shedding light on the relationships among early-diverging lineages in the fungal kingdom.

#### Primers

Primers successfully amplifying RPB1 especially in Ascomycota are the forward primer *RPB1-Af* with the sequence 5'-GARTGYCCDGGDCAYTTYGG-3', and the reverse primer *RPB1-Ac-RPB1-Cr* with the sequence 5'-CCNGCDATNTCRTTRTCCATRTA-3'.

### Intergenic Spacer (IGS) of ribosomal RNA genes

The Intergenic Spacer (*IGS*) is the region of non-coding DNA between individual tandem repeats of the ribosomal gene cluster in the nuclear genome, as opposed to the Internal Transcribed Spacer (ITS) that is situated within these tandem repeats.

*IGS* has been successfully used for the differentiation of strains of *Xanthophyllomyces dendrorhous* as well as for species distinction in the psychrophilic genus *Mrakia* (Cystofilobasidiales). Due to these results, *IGS* has been recommended as a genetic marker for additional differentiation (along with D1/D2 and *ITS*) of closely related species and even strains within one species in basidiomycete yeasts.

The recent discovery of additional non-coding RNA genes in the IGS region of some basidiomycetes cautions against uncritical use of *IGS* sequences for DNA barcoding and phylogenetic purposes.

### Other genetic markers

The **cytochrome c oxidase subunit I (*COI*)** gene outperforms *ITS* in DNA barcoding of *Penicillium* (Ascomycota) species, with species-specific barcodes for 66% of the investigated species versus 25% in the case of *ITS*. Furthermore, a part of the β-Tubulin A (*BenA*) gene exhibits a higher taxonomic resolution in distinguishing *Penicillium* species as compared to *COI* and *ITS*. In the closely related *Aspergillus niger* complex, however, *COI* is not variable enough for species discrimination. In *Fusarium*, *COI* exhibits paralogues in many cases, and homologous copies are not variable enough to distinguish species.

*COI* also performs poorly in the identification of basidiomycote rusts of the order Pucciniales due to the presence of introns. Even when the obstacle of introns is overcome, *ITS* and the LSU rRNA (28S) outperform *COI* as DNA barcode marker. In the subdivision Agaricomycotina, PCR amplification success was poor for *COI*, even with multiple primer combinations. Successfully sequenced *COI* samples also included introns and possible paralogous copies, as reported for *Fusarium*. *Agaricus bisporus* was found to contain up to 19 introns, making the *COI* gene of this species the longest recorded, with 29,902 nucleotides. Apart from the substantial troubles of sequencing *COI*, *COI* and *ITS* generally perform equally well in distinguishing basidiomycete mushrooms.

**Topoisomerase I (*TOP1*)** was investigated as additional DNA barcode candidate by Lewis et al. (2011) based on proteome data, with the developed universal primer pair being subsequently tested on actual samples by Stielow et al. (2015). The forward primer *TOP1_501-F* with the sequence 5'-TGTAAAACGACGGCCAGT-ACGAT-ACTGCCAAGGTTTTCCGTACHTACAACGC-3' (where the first section marks the universal M13 forward primer tail, the second part consisting of ACGAT a spacer, and the third part the actual primer) and reverse the primer *TOP1_501-R* with 5'-CAGGAAACAGCTATGA-CCCAGTCCTCGTCAACWGACTTRATRGCCCA-3' (the first section marking the universal M13 reverse primer tail, the second part the actual TOP1 reverse primer) amplify a fragment of approximately 800 base pairs.

*TOP1* was found to be a promising DNA barcode candidate marker for ascomycetes, where it can distinguish species in *Fusarium* and *Penicillium* – genera, in which the primary *ITS* barcode performs poorly. However, poor amplification success with the *TOP1* universal primers is observed in early-diverging fungal lineages and basidiomycetes except Pucciniomycotina (where *ITS* PCR success is poor).

Like *TOP1*, the **Phosphoglycerate kinase (*PGK*)** was among the genetic markers investigated by Lewis et al. (2011) and Stielow et al. (2015) as potential additional fungal DNA barcodes. A number of universal primers was developed, with the PGK533 primer pair, amplifying a circa 1,000 base pair fragment, being the most successful in most fungi except Basidiomycetes. Like *TOP1*, *PGK* is superior to *ITS* in species differentiation in ascomycete genera like *Penicillium* and *Fusarium*, and both *PGK* and *TOP1* perform as good as *TEF1α* in distinguishing closely related species in these genera.

## Applications

### Food safety

A citizen science project investigated the consensus between the labelling of dried, commercially sold mushrooms and the DNA barcoding results from these mushrooms. All samples were found to be correctly labelled. However, an obstacle was the unreliability of ITS reference databases in terms of the level of identification, as the two databases (GenBank and UNITE) used for ITS sequence comparison gave different identification results in some of the samples.

Correct labelling of mushrooms intended for consumption was also investigated by Raja et al. (2016), who used the *ITS* region for DNA barcoding from dried mushrooms, mycelium powders, and dietary supplement capsules. In only 30% of the 33 samples did the product label correctly state the binomial fungus name. In another 30%, the genus name was correct, but the species epithet did not match, and in 15% of the cases not even the genus name of the binomial name given on the product label matched the result of the obtained *ITS* barcode. For the remaining 25% of the samples, no *ITS* sequence could be obtained.

Xiang et al. (2013) showed that using *ITS* sequences, the commercially highly valuable the caterpillar fungus *Ophiocordyceps sinensis* and its counterfeit versions (*O. nutans*, *O. robertsii*, *Cordyceps cicadae*, *C. gunnii*, *C. militaris*, and the plant *Ligularia hodgsonii*) can be reliably identified to the species level.

### Pathogenic fungi

A study by Vi Hoang et al. (2019) focused on the identification accuracy of pathogenic fungi using both the primary (*ITS*) and secondary (*TEF1α*) barcode markers. Their results show that in *Diutina* (a segregate of *Candida*) and *Pichia*, species identification is straightforward with either the *ITS* or the *TEF1α* as well as with a combination of both. In the *Lodderomyces* assemblage, which contains three of the five most common pathogenic *Candida* species (*C. albicans*, *C. dubliniensis*, and *C. parapsilosis*), *ITS* failed to distinguish *Candida orthopsilosis* and *C. parapsilosis*, which are part of the *Candida parapsilosis* complex of closely related species. *TEF1α*, on the other hand, allowed identification of all investigated species of the *Lodderomyces* clade. Similar results were obtained for *Scedosporium* species, which are attributed to a wide range of localised to invasive diseases: *ITS* could not distinguish between *S. apiospermum* and *S. boydii*, whereas with *TEF1α* all investigated species of this genus could be accurately identified. This study therefore underlines the usefulness of applying more than one DNA barcoding marker for fungal species identification.

### Conservation of cultural heritage

Fungal DNA barcoding has been successfully applied to the investigation of foxing phenomena, a major concern in the conservation of paper documents. Sequeira et al. (2019) sequenced *ITS* from foxing stains and found *Chaetomium globosum*, *Ch. murorum*, *Ch. nigricolor*, *Chaetomium* sp., *Eurotium rubrum*, *Myxotrichum deflexum*, *Penicillium chrysogenum*, *P. citrinum*, *P. commune*, *Penicillium* sp. and *Stachybotrys chartarum* to inhabit the investigated paper stains.

Another study investigated fungi that act as biodeteriorating agents in the Old Cathedral of Coimbra, part of the University of Coimbra, a UNESCO World Heritage Site. Sequencing the *ITS* barcode of ten samples with classical Sanger as well as with Illumina next-generation sequencing techniques, they identified 49 fungal species. *Aspergillus versicolor*, *Cladosporium cladosporioides*, *C. sphaerospermum*, *C. tenuissimum*, *Epicoccum nigrum*, *Parengyodontium album*, *Penicillium brevicompactum*, *P. crustosum*, *P. glabrum*, *Talaromyces amestolkiae* and *T. stollii* were the most common species isolated from the samples.

Another study concerning objects of cultural heritage investigated the fungal diversity on a canvas painting by Paula Rego using the *ITS2* subregion of the *ITS* marker. Altogether, 387 OTUs (putative species) in 117 genera of 13 different classes of fungi were observed.
