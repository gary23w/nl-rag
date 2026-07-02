---
title: "Spatial transcriptomics"
source: https://en.wikipedia.org/wiki/Spatial_transcriptomics
domain: spatial-transcriptomics
license: CC-BY-SA-4.0
tags: spatial gene expression, tissue section, in situ hybridization, spot capture
fetched: 2026-07-02
---

# Spatial transcriptomics

**Spatial transcriptomics,** or spatially resolved transcriptomics**,** is a method that captures positional context of transcriptional activity within intact tissue. The historical precursor to spatial transcriptomics is *in situ* hybridization, where the modernized omics terminology refers to the measurement of all the mRNA in a cell rather than select RNA targets. It comprises an important part of spatial biology.

Spatial transcriptomics includes methods that can be divided into two modalities, those based in next-generation sequencing for gene detection, and those based in imaging. Some common approaches to resolve spatial distribution of transcripts are microdissection techniques, fluorescent *in situ* hybridization methods, *in situ* sequencing, *in situ* capture protocols and *in silico* approaches.

## History

*in situ* hybridization was developed in the late 1960's by Joseph G. Gall and Mary-Lou Pardue and saw major developments in the 1980's with single molecule FISH (smFISH) and 2010's with RNAscope, seqFISH, MERFISH and osmFISH, seqFISH+, and DNA microscopy. Microdisecction techniques were first developed in the late 1990's (Laser Capture Microdissection) and combined with RNA-seq profiling in 2013 in Michael Eisen's lab using fruit fly embryos.

Spatial genomics as a technique, or now referred to as spatial transcriptomics, was initiated in 1990s by Michael Doyle (of Eolas), Maurice Pescitelli (of the University of Illinois at Chicago), Betsey Williams (of Harvard), and George Michaels (of George Mason University), as part of the Visible Embryo Project. Doyle and his co-investigators described a method called Spatial Analysis of Genomic Activity (SAGA).

This spatial indexing concept was expanded upon in 2016 by Jonas Frisén, Joakim Lundeberg, Patrik Ståhl and their colleagues in Stockholm, Sweden. In 2019, the first commercial platforms for spatial transcriptomics were launched with GeoMx Digital Spatial Profiler (DSP) by Nanostring Technologies and Visium by 10X Genomics. In 2019, at the Broad Institute, the labs of Fei Chen and Evan Macosko developed Slide-seq, which used barcoded oligos on beads.

## Applications

Defining the spatial distribution of mRNA molecules allows for the detection of cellular heterogeneity in tissues, tumours, and immune cells as well as determining the subcellular distribution of transcripts in various conditions. This information provides a unique opportunity to decipher both the cellular and subcellular architecture in both tissues and individual cells. These methodologies provide crucial insights in the fields of embryology, oncology, immunology, neuroscience, pathology, and histology. The functioning of the individual cells in multicellular organisms can only be completely explained in the context of identifying their exact location in the body. Spatial transcriptomics techniques sought to elucidate cells' properties this way. Below, we look into the methods that connect gene expression to the spatial organization of cells.

## Microdissection

### Laser capture microdissection

Laser capture microdissection enables capturing single cells without causing morphologic alterations. It exploits transparent ethylene vinyl acetate film apposed to the histological section and a low-power infrared laser beam. Once such beam is directed at the cells of interest, film directly above the targeted area temporarily melts so that its long-chain polymers cover and tightly capture the cells. Then, the section is removed and cells of interest remain embedded in the film. This method allows further RNA transcript profiling and cDNA library generation of the retrieved cells.

### RNA sequencing of individual cryosections

RNA sequencing of the selected regions in individual cryosections is another method that can produce location-based genome-wide expression data. This method is carried out without laser capture microdissection. It was first used to determine genome-wide spatial patterns of gene expression in cryo-sliced Drosophila embryos. Essentially, it implies simple preparation of the library from the selected regions of the sample. This method had difficulties in obtaining high-quality RNA-seq libraries from every section due to the material loss as a result of the small amount of total RNA in each slice. This problem was resolved by adding RNA of a distantly related Drosophila species to each tube after initial RNA extraction.

### GeoMx

The GeoMx Digital Spatial Profiler (DSP) (NanoString Technologies) is the first automated commercial instrument developed for spatial profiling of RNAs and proteins in archival formalin-fixed, paraffin-embedded (FFPE) tissue sections. FFPE is a common sample type in the field of pathology and histology due to its long term preservation of tissue structure. The GeoMx DSP technology centers around a user's ability to perform "microdissection" based on histological structures, functional compartments, and cell types. However, unlike LCM, gene expression profiling is performed in a nondestructive manner through light, due to a UV-photocleavable barcode engineered into the *in situ* hybridization probe. To do this, tissue sections on microscope slides are stained with fluorescent antibodies and nuclear dye to visualize the whole tissue section at single cell resolution on the DSP instrument. Selection of region of interests occurs through automated segmentation on flurorescent signal intensities or drawing tools, including geometric or free hand shapes. Each region of interest is precisely exposed to UV light and the barcodes are cleaved, collected, and used to identify RNAs or proteins present in the tissue. The defined regions of interest can vary in size, between ten and six hundred micrometers, allowing a wide variety of structures and cells in the histological sample. GeoMx DSP can spatially resolve and measure human or mouse whole transcriptomes, more than 1200 proteins, or both RNA and protein in multiomic same slide protocols.

### TIVA

Transcriptome in vivo analysis (TIVA) is a technique that enables capturing mRNA in live single cells in intact live tissue sections. It uses a photoactivatable tag. The TIVA tag has several functional groups and a trapped poly(U) oligonucleotide coupled to biotin. A disulfide-linked peptide, which is adjacent to the tag, allows it to penetrate the cell membrane. Once inside, laser photoactivation is used to unblock poly(U) oligonucleotide in the cells of interest, so that TIVA tag hybridizes to mRNAs within the cell. Then, streptavidin capture of the biotin group is used to extract poly(A)-tailed mRNA molecules bound to unblocked tags, after which these mRNAs are analyzed by RNA sequencing. This method is limited by low throughput, as only a few single cells can be processed at a time.

### tomo-seq

An advanced alternative for RNA Sequencing of Individual Cryosections described above, RNA tomography (tomo-seq) features better RNA quantification and spatial resolution. It is also based on tissue cryosectioning with further RNA sequencing of individual sections, yielding genome-wide expression data and preserving spatial information. In this protocol, usage of carrier RNA is omitted due to linear amplification of cDNA in individual histological sections. The identical sample is sectioned in different directions followed by 3D transcriptional construction using overlapping data. Overall, this method implies using identical samples for each section and thus cannot be applied for processing clinical material.

### LCM-seq

LCM-seq utilizes laser capture microdissection (LCM) coupled with Smart-Seq2 RNA sequencing and is applicable down to the single cell level and can even be used on partially degraded tissues. The workflow includes cryosectioning of tissues followed by laser capture microdissection, where cells are collected directly into lysis buffer and cDNA is generated without the need for RNA isolation, which both simplifies the experimental procedures as well as lowers technical noise. As the positional identity of each cell is recorded during the LCM procedure, the transcriptome of each cell after RNA sequencing of the corresponding cDNA library can be inferred to the position where it was isolated from. LCM-seq has been applied to multiple cell types to understand their intrinsic properties, including oculomotor neurons, facial motor neurons, hypoglossal motor neurons, spinal motor neurons, red nucleus neurons, interneurons, dopamine neurons, and chondrocytes.

### Geo-seq

Geo-seq is a method that utilizes both laser capture microdissection and single-cell RNA sequencing procedures to determine the spatial distribution of the transcriptome in tissue areas approximately ten cells in size. The workflow involves removal and cryosectioning of tissue followed by laser capture microdissection. The extracted tissue is then lysed, and the RNA is purified and reverse transcribed into a cDNA library. Library is sequenced, and the transcriptomic profile can be mapped to the original location of the extracted tissue. This technique allows the user to define regions of interest in a tissue, extract said tissue and map the transcriptome in a targeted approach.

### NICHE-seq

The NICHE-seq method uses photoactivatable fluorescent markers and two-photon laser scanning microscopy to provide spatial data to the transcriptome generated. The cells bound by the fluorescent marker are photoactivated, dissociated and sorted via fluorescence-activated cell sorting. This provides sorting specificity to only labeled, photoactivated cells. Following sorting, single-cell RNA sequencing generates the transcriptome of the visualized cells. This method can process thousands of cells within a defined niche at the cost of losing spatial data between cells in the niche.

### ProximID

ProximID is a methodology based on iterative micro digestion of extracted tissue to single cells. Initial mild digestion steps preserve small interacting structures that are recorded prior to continued digestion. The single cells are then separated from each structure and undergo sc-RNAseq and clustered using t-distributed stochastic neighbour embedding. The clustered cells can be mapped to physical interactions based on the interacting structures prior to the micro digestions. While the throughput of this technique is relatively low it provides information on physical interaction between cells to the dataset.

## Fluorescent *in situ* hybridization

### CosMx

The CosMx Spatial Molecular Imager (NanoString Technologies) is the first high-plex *in situ* analysis platform to provide spatial multiomics with formalin-fixed paraffin-embedded (FFPE) and fresh frozen (FF) tissue samples at cellular and subcellular resolution. It enables rapid quantification and visualization of up to the whole transcriptome and 64 validated protein analytes and is the flexible, spatial single-cell imaging platform for cell atlasing, tissue phenotyping, cell-cell interactions, cellular processes, and biomarker discovery.

### smFISH

One of the first techniques able to achieve spatially resolved RNA profiling of individual cells was single-molecule fluorescent *in situ* hybridization (smFISH). It implemented short (50 base pairs) oligonucleotide probes conjugated with 5 fluorophores which could bind to a specific transcript yielding bright spots in the sample. Detection of these spots provides quantitative information about expression of certain genes in the cell. However, usage of probes labeled with multiple fluorophores was challenged by self-quenching, altered hybridization characteristics, their synthesis and purification.

Later, this method was changed by substituting the above described probes with those of 20 bp length, coupled to only one fluorophore and complementary in tandem to an mRNA sequence of interest, meaning that those would collectively bind to the targeted mRNA. One such probe itself wouldn't produce a strong signal, but the cumulative fluorescence of the congregated probes would show a bright spot. Since single misbound probes are unlikely to co-localize, false-positive signals in this method are limited.

Thus, this *in situ* hybridization (ISH) technique spots spatial localization of RNA expression via direct imaging of individual RNA molecules in single cells.

### RNAscope

Another *in situ* hybridization technique termed RNAscope employs probes of the specific Z-shaped design to simultaneously amplify hybridization signals and suppress background noise. It allows for the visualization of single RNA in a variety of cellular types. Most steps of RNAScope are similar to the classic ISH protocol. The tissue sample is fixed onto slides and then treated with RNAscope reagents that permeate the cells. Z-probes are designed in a way that they are only effective when bound in pairs to the target sequence. This allows another element of this method (preamplifier) to connect to the top tails of Z-probes. Once affixed, preamplifier serves as a binding site for other elements: amplifiers which in turn bind to another type of probes: label probes. As a result, a bulky structure is formed on the target sequence. Most importantly, the preamplifier fails to bind to a singular Z-probe, thus, nonspecific binding wouldn't entail signal emission, thus, eliminating background noise mentioned in the beginning.

### seqFISH

Sequential fluorescence *in situ* hybridization (seqFISH) is another method that provides identification of mRNA directly in single cells with preservation of their spatial context. This method is carried out in multiple rounds; each of them includes fluorescent probe hybridization, imaging, and consecutive probe stripping. Various genes are assigned different colors in every round, generating a unique temporal barcode. Thus, seqFISH distinguishes mRNAs by a sequential color code, such as red-red-green. Nevertheless, this technique has its flaws featuring autofluorescent background and high costs due to the number of probes used in each round.

### MERFISH

Conventional FISH methods are limited by the small number of genes that can be simultaneously analyzed due to the small number of distinct color channels, so multiplexed error-robust FISH was designed to overcome this problem. Multiplexed Error-Robust FISH (MERFISH) greatly increases the number of RNA species that can be simultaneously imaged in single cells employing binary code gene labeling in multiple rounds of hybridization. This approach can measure 140 RNA species at a time using an encoding scheme that both detects and corrects errors. The core principle lies in identification of genes by combining signals from several consecutive hybridization rounds and assigning N-bit binary barcodes to genes of interest. The Code depends on specific probes and comprises "1" or "0" values and their combination is set differently for each gene. Errors are avoided by using six-bit or longer codes with any two of them differing by at least 3 bits. A specific probe is created for each RNA species. Each probe is a target-specific oligonucleotide that consists of 20-30 base pairs and complementary binds to mRNA sequence after permeating the cell. Then, multiple rounds of hybridization are conducted as follows: for each round, only a probe that includes "1" in the corresponding binary code position is added. At the end of each round, fluorescent microscopy is used to locate each probe. Expectedly, only those mRNAs which had "1" in the assigned position would be captured. Photos are then photobleached and a new subset is added. Thus, we retrieve combination of binary values which makes it possible to distinguish between numerous RNA species.

### smHCR

Single-molecule RNA detection at depth by hybridization chain reaction (smHCR) is an advanced seqFISH technique that can overcome typical complication of autofluorescent background in thick and opaque tissue samples. In this method, multiple readout probes are bound with the target region of mRNA. Target is detected by a set of short DNA probes which attach to it in defined subsequence. Each DNA probe carries an initiator for the same HCR amplifier. Then, fluorophore-labeled DNA HCR hairpins penetrate the sample and assemble into fluorescent amplification polymers attaching to initiating probes. In multiplexed studies, the same two-stage protocol described above is used: all probe sets are introduced simultaneously, just as all HCR amplifiers are; spectrally distinct fluorophores are used for further imaging.

### osmFISH

Cyclic-ouroboros smFISH (osmFISH) is an adaptation of smFISH which aims to overcome the challenge of optical crowding. In osmFISH, transcripts are visualized, and an image is acquired before the probe is stripped and a new transcript is visualized with a different fluorescent probe. After successive rounds the images are compiled to view the spatial distribution of the RNA. Due to transcripts being sequentially visualized it eliminates the issue of signals interfering with each other. This method allows the user to generate high resolution images of larger tissue sections than other related techniques.

### ExFISH

Expansion FISH (ExFISH) leverages expansion microscopy to allow for super-resolution imaging of RNA location, even in thick specimens such as brain tissue. It supports both single-molecule and multiplexed readouts.

### EASI-FISH

Expansion-Assisted Iterative Fluorescence *In Situ* Hybridization (EASI-FISH) optimizes and builds on ExFISH with improved detection accuracy and robust multi-round processing across samples thicker (300 μm) than what was previously possible. It also includes a turn-key computational analysis pipeline.

### seqFISH+

SeqFISH+ resolved optical issues related to spatial crowding by subsequent rounds of fluorescence. First, a primary probe anneals to targeted mRNA and then subsequent probes bind to flanking regions of the primary probe resulting in a unique barcode. Each readout probe is captured as an image and collapsed into a super resolved image. This method allows the user to target up to ten thousand genes at a time.

### DNA microscopy

DNA microscopy is a distinct imaging method for optics-free mapping of molecules' positions with simultaneous preservation of sequencing data carried out in several consecutive *in situ* reactions. First, cells are fixed and cDNA is synthesized. Randomized nucleotides then tag target cDNAs *in situ*, providing unique labels for each molecule. Tagged transcripts are amplified in the second *in situ* reaction, retrieved copies are concatenated, and new randomized nucleotides are added. Each consecutive concatenation event is labeled, yielding unique event identifiers. Algorithm then generates images of the original transcripts based on decoded molecular proximities from the obtained concatenated sequences, while target's single nucleotide information is being recorded as well.

## *in situ* sequencing

### ISS using padlock probes

The ISS padlock method is based on padlock probing, rolling-circle amplification (RCA), and sequencing by ligation chemistry. Within intact tissue sections, mRNA is reversely transcribed to cDNA, which is followed by mRNA degradation by RNase H. Then, there are two ways of how this method can be carried out. The first way, gap-targeted sequencing, involves padlock probe binding to cDNA with a gap between the ends of the probe which are targeted for sequencing by ligation. DNA polymerization then fills this gap and a DNA circle is created by DNA ligation. Another way, barcode-targeted sequencing, DNA circularization of a padlock probe with a barcode sequence is conducted by ligation only. In both versions of the method, the ends are ligated forming a circle of DNA. Target amplification is then performed by RCA, yielding micrometer-sized RCA products (RCPs). RCAs consist of repeats of the padlock probe sequence. These DNA molecules are then subjected to sequencing by ligation, decoding either a gap-filled sequence or an up to four-base-long barcode within the probe with adjacent ends, depending on the version. No-gap variant claims higher sensitivity, while gap-filled one implies reading out the actual RNA sequence of the transcript. Later, this method was improved by automatization on a microfluidic platform and substitution of sequencing by ligation with sequencing by hybridization technology.

### FISSEQ

Fluorescent *in situ* sequencing (FISSEQ), like ISS padlock, is a  method that uses reverse transcription, rolling-circle amplification, and sequencing by ligation techniques. It allows spatial transcriptome analysis in fixed cells. RNA is first reverse transcribed into cDNA with regular and modified amine-bases and tagged random hexamer RT primers. Amine-bases mediate the cross-linkage of cDNA to its cellular surrounding. Then cDNA is circulated by ligation and amplified by RCA. Single-stranded DNA nanoballs of 200–400 nm in diameter are obtained as a result. Thus, these nanoballs comprise numerous tandem repeats of the cDNA sequence. Then sequencing is performed via SOLiD sequencing by ligation. Positions of both product of reverse transcription and clonally amplified RCPs are maintained via cross-linkage to cellular matrix components mentioned previously, creating a 3D *in situ* RNA-seq library within the cell. Once bound with fluorescent probes featuring different colors, amplicons become highly fluorescent which allows visual detection of the signal; however, the image-processing algorithm relies on read alignment to reference sequences rather than signal intensity.

### Barista-seq

Barcode *in situ* targeted sequencing (Barista-seq) is an improvement on the gap padlock probe methodology boasting a fivefold increase in efficiency, an increased read length of fifteen bases and is compatible with illumina sequencing platforms. The method also uses padlock probes and rolling circle amplification, however this approach uses sequencing-by-synthesis and crosslinking unlike the gap padlock method. The crosslinking to the cellular matrix in the same procedure is the same as FISSEQ.

### STARmap

Spatially-resolved transcript amplicon readout mapping (STARmap) utilizes a padlock probe with an additional primer which allows for direct amplification of mRNA, forgoing the need for reverse transcription. Similar to other padlock probe based methods amplification occurs via rolling circle amplification. The DNA amplicons are chemically modified and embedded into a polymerized hydrogel within the cell. Captured RNA can then be sequenced *in situ* providing three dimensional locations of the mRNA within each cell.

## *in situ* capture

### Stereo-seq(STOmics)

STOmics is a pioneer in advancing spatially-resolved transcriptomic analysis through its proprietary SpaTial Enhanced REsolution Omics-Sequencing (Stereo-seq) technology. It combines *in situ* capture with DNB-seq, DNB sequencing is based on lithographically etched chips (patterned arrays) for *in situ* sequencing. Unlike other um-level *in situ* capture technologies, standard DNB chips have spots with approximately 220 nm diameter and a center-to-center distance of 500 nm, providing up to 20000 spots for tissue RNA capture per 10mm linear distance, or 4 × 108 spots per 1 cm2. Therefore, STOmics can show higher resolution and wider field of view than other *in situ* capture technologies.

### Spatial transcriptomics

The first widely-adopted method was described by Ståhl *et al.* in a landmark 2016 paper in Science, coining the term "spatial transcriptomics." This methodology relies on diffusion of mRNA from a fresh frozen tissue section for capture of the polyadenylated mRNAs via hybridization to oligo(dT) sequence attached to a glass slide. The glass slide is arrayed with "spots" that contain oligo(dT) sequence to capture mRNA transcripts, spatial barcode sequence to indicate the x and y position on the arrayed slide, amplification and sequencing handle to generate sequence libraries, and unique molecular identifier to quantitate transcript abundance. Frozen tissue samples are cut using cryotome, then fixed, stained, and carefully laid flat onto the microarray. Next, enzymatic permeabilization allows RNA molecules to diffuse to the microarray slide for hybridization of polyadenylated mRNA molecules to the oligo(dT) sequence tails. Reverse transcription is then carried out *in situ* for first-strand synthesis. As a result, spatially marked complementary DNA (cDNA) is synthesized, providing information about gene expression in the exact location of the tissue section. From the cDNA, libraries are generated for short-read sequencing. In summary, this spatial transcriptomics protocol combines paralleled sequencing and staining of the same sample. In the downstream analysis, bioinformatic tools allow overlay of the tissue image with the gene expression. The output is a map of the transcriptome captured gene expression within a tissue section. It is important to mention that the first generation of the arrayed slides comprised about 1,000 spots of the 100-μm diameter, limiting resolution to ~10-40 cells per spot.

This technology was the basis of a company founded in 2012 called Spatial Transcriptomics. In 2018, 10X Genomics acquired Spatial Transcriptomics as the foundation for the 10X Visium platform.

### Slide-seq

Slide-seq relies on the attachment of RNA binding, DNA-barcoded micro beads to a rubber coated glass coverslip. The microbeads are mapped to their spatial location via SOLiD sequencing. Tissue sections are transferred to this coverslip to capture extracted RNA. Captured RNA is amplified and sequenced. Transcript localization is determined by the barcode oligonucleotide sequence from the bead that captured it.

### APEX-seq

APEX-seq allows the for assessment of the spatial transcriptome in different regions of a cell. The method utilizes the APEX2 gene, expressed in live cells which are incubated with biotin-phenol and hydrogen peroxide. In these conditions the APEX2 enzymes catalyse the transfer of biotin groups to the RNA molecules and these can then be purified via streptavidin bead purification. The purified transcripts are then sequenced to determine which molecules were in close proximity to the biotin tagging enzyme.

### HDST

High-Definition Spatial Transcriptomics (HDST) begins with decoding the location of mRNA capture beads in wells on a glass slide. This is accomplished by sequential hybridization to the barcode oligonucleotide sequence of each bead. Once the location of each bead is decoded, a tissue sample can be placed on the slide and permeabilized. The captured transcripts are then sequenced. HDST uses smaller beads than Slide-seq and thus can resolve at a spatial resolution of two micrometers compared to ten micrometers of Slide-seq.

### 10X Genomics Visium

The 10X Genomics Visium assay is a newer and improved version of the Spatial Transcriptomics assay. It also utilizes spotted arrays of mRNA-capturing probes on the surface of glass slides but with increased spot number, minimized spot size and increased amount of capture probes per spot. Within each of the four capture areas of the Visium Spatial Gene Expression slides, there are approximately 5000 barcoded spots, which in turn contain millions of spatially barcoded capture oligonucleotides. Tissue mRNA is released upon permeabilization and binds to the barcoded oligos, enabling capture of gene expression information. Each barcoded spot is 55 μm in diameter, and the distance from the center of one spot to the center of another is approximately 100 μm. The spots are staggered to minimize the distance between them. On average, mRNA from anywhere between 1 and 10 cells are captured per spot which provides near single-cell resolution.

### Takara Bio SEEKER

The assay is similar in concept to the 10X Genomics Visium but has a higher density of spots. Contrary to the 10X Genomics Visium HD, which uses RNA probes that have to be pre-defined for species like human or mouse, SEEKER has a similar density and resolution, but will assay any fresh frozen tissue sample, using poly-A adaptation of all the mRNAs in the sample.

## *in silico* construction

### Reconstruction using ISH

*in silico* Spatial Reconstruction with ISH implies computational spatial reconstruction of cells' locations according to their expression profiles. Several similar methods of this principle exist. They co-analyze single-cell transcriptomics and available ISH-based gene expression atlases of the same cell type. Based on these data, cells are then assigned to their positions in the tissue. Obviously, this method is limited by the factor of availability of ISH references. Additionally, it becomes more complicated when assigning cells in complex tissues. This approach is not applicable for clinical samples due to the lack of paired references. Reported success rate for the exact allocation of cells in brain tissue was 81%.

### DistMap

Mapping the transcriptome using the Distmap algorithm requires high-throughput single cell sequencing and an existing *in situ* hybridization atlas for the tissue of interest. The Distmap algorithm generates a virtual 3D model of the tissue of interest using the transcriptomes of sequenced cells and said reference atlas. The transcriptomes can be clustered into cell types using t-distributed stochastic neighbour embedding and mapped to the 3D model using virtual *in situ* hybridization. Essentially, this algorithm takes data generated from single cells in a dissociated tissue and is able to map individual transcripts to where the cell type exists in the tissue using virtual *in situ* hybridization.
