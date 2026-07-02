---
title: "Metabolic network modelling"
source: https://en.wikipedia.org/wiki/Metabolic_network_modelling
domain: systems-biology
license: CC-BY-SA-4.0
tags: systems biology, flux balance analysis, gene regulatory network, metabolic network modelling
fetched: 2026-07-02
---

# Metabolic network modelling

**Metabolic network modelling**, also known as **metabolic network reconstruction** or **metabolic pathway analysis**, allows for an in-depth insight into the molecular mechanisms of a particular organism. In particular, these models correlate the genome with molecular physiology. A reconstruction breaks down metabolic pathways (such as glycolysis and the citric acid cycle) into their respective reactions and enzymes, and analyzes them within the perspective of the entire network. In simplified terms, a reconstruction collects all of the relevant metabolic information of an organism and compiles it in a mathematical model. Validation and analysis of reconstructions can allow identification of key features of metabolism such as growth yield, resource distribution, network robustness, and gene essentiality. This knowledge can then be applied to create novel biotechnology.

In general, the process to build a reconstruction is as follows:

1. Draft a reconstruction
2. Refine the model
3. Convert model into a mathematical/computational representation
4. Evaluate and debug model through experimentation

The related method of flux balance analysis seeks to mathematically simulate metabolism in genome-scale reconstructions of metabolic networks.

## Genome-scale metabolic reconstruction

A metabolic reconstruction provides a highly mathematical, structured platform on which to understand the systems biology of metabolic pathways within an organism. The integration of biochemical metabolic pathways with rapidly available, annotated genome sequences has developed what are called genome-scale metabolic models. Simply put, these models correlate metabolic genes with metabolic pathways. In general, the more information about physiology, biochemistry and genetics is available for the target organism, the better the predictive capacity of the reconstructed models. Mechanically speaking, the process of reconstructing prokaryotic and eukaryotic metabolic networks is essentially the same. Having said this, eukaryote reconstructions are typically more challenging because of the size of genomes, coverage of knowledge, and the multitude of cellular compartments. The first genome-scale metabolic model was generated in 1995 for *Haemophilus influenzae*. The first multicellular organism, *C. elegans*, was reconstructed in 1998. Since then, many reconstructions have been formed. For a list of reconstructions that have been converted into a model and experimentally validated, see http://sbrg.ucsd.edu/InSilicoOrganisms/OtherOrganisms.

| Organism | Genes in Genome | Genes in Model | Reactions | Metabolites | Date of reconstruction | Reference |
|---|---|---|---|---|---|---|
| *Haemophilus influenzae* | 1,775 | 296 | 488 | 343 | June 1999 |   |
| *Escherichia coli* | 4,405 | 660 | 627 | 438 | May 2000 |   |
| *Saccharomyces cerevisiae* | 6,183 | 708 | 1,175 | 584 | February 2003 |   |
| *Mus musculus* | 28,287 | 473 | 1220 | 872 | January 2005 |   |
| *Homo sapiens* | 21,090 | 3,623 | 3,673 | -- | January 2007 |   |
| *Mycobacterium tuberculosis* | 4,402 | 661 | 939 | 828 | June 2007 |   |
| *Bacillus subtilis* | 4,114 | 844 | 1,020 | 988 | September 2007 |   |
| *Synechocystis sp. PCC6803* | 3,221 | 633 | 831 | 704 | October 2008 |   |
| *Salmonella typhimurium* | 4,489 | 1,083 | 1,087 | 774 | April 2009 |   |
| *Arabidopsis thaliana* | 27,379 | 1,419 | 1,567 | 1,748 | February 2010 |   |

## Drafting a reconstruction

### Resources

Because the timescale for the development of reconstructions is so recent, most reconstructions have been built manually. However, now, there are quite a few resources that allow for the semi-automatic assembly of these reconstructions that are utilized due to the time and effort necessary for a reconstruction. An initial fast reconstruction can be developed automatically using resources like PathoLogic or ERGO in combination with encyclopedias like MetaCyc, and then manually updated by using resources like PathwayTools. These semi-automatic methods allow for a fast draft to be created while allowing the fine tune adjustments required once new experimental data is found. It is only in this manner that the field of metabolic reconstructions will keep up with the ever-increasing numbers of annotated genomes.

#### Databases

- **Kyoto Encyclopedia of Genes and Genomes (KEGG)**: a bioinformatics database containing information on genes, proteins, reactions, and pathways. The 'KEGG Organisms' section, which is divided into eukaryotes and prokaryotes, encompasses many organisms for which gene and DNA information can be searched by typing in the enzyme of choice.
- **BioCyc, EcoCyc, and MetaCyc**: BioCyc Is a collection of 3,000 pathway/genome databases (as of Oct 2013), with each database dedicated to one organism. For example, EcoCyc is a highly detailed bioinformatics database on the genome and metabolic reconstruction of *Escherichia coli*, including thorough descriptions of *E. coli* signaling pathways and regulatory network. The EcoCyc database can serve as a paradigm and model for any reconstruction. Additionally, MetaCyc, an encyclopedia of experimentally defined metabolic pathways and enzymes, contains 2,100 metabolic pathways and 11,400 metabolic reactions (Oct 2013).
- **ENZYME**: An enzyme nomenclature database (part of the ExPASy proteonomics server of the Swiss Institute of Bioinformatics). After searching for a particular enzyme on the database, this resource gives you the reaction that is catalyzed. ENZYME has direct links to other gene/enzyme/literature databases such as KEGG, BRENDA, and PUBMED.
- **BRENDA**: A comprehensive enzyme database that allows for an enzyme to be searched by name, EC number, or organism.
- **BiGG**: A knowledge base of biochemically, genetically, and genomically structured genome-scale metabolic network reconstructions.
- **metaTIGER**: Is a collection of metabolic profiles and phylogenomic information on a taxonomically diverse range of eukaryotes which provides novel facilities for viewing and comparing the metabolic profiles between organisms.

| Database | Scope |   |   |   |   |
|---|---|---|---|---|---|
|   | Enzymes | Genes | Reactions | Pathways | Metabolites |
| KEGG | X | X | X | X | X |
| BioCyc | X | X | X | X | X |
| MetaCyc | X |   | X | X | X |
| ENZYME | X |   | X |   | X |
| BRENDA | X |   | X |   | X |
| BiGG |   | X |   | X | X |

#### Tools for metabolic modeling

- **Pathway Tools**: A bioinformatics software package that assists in the construction of pathway/genome databases such as EcoCyc. Developed by Peter Karp and associates at the SRI International Bioinformatics Research Group, Pathway Tools has several components. Its PathoLogic module takes an annotated genome for an organism and infers probable metabolic reactions and pathways to produce a new pathway/genome database. Its MetaFlux component can generate a quantitative metabolic model from that pathway/genome database using flux-balance analysis. Its Navigator component provides extensive query and visualization tools, such as visualization of metabolites, pathways, and the complete metabolic network.
- **ERGO**: A subscription-based service developed by Integrated Genomics. It integrates data from every level including genomic, biochemical data, literature, and high-throughput analysis into a comprehensive user friendly network of metabolic and nonmetabolic pathways.
- **KEGGtranslator**: an easy-to-use stand-alone application that can visualize and convert KEGG files (KGML formatted XML-files) into multiple output formats. Unlike other translators, KEGGtranslator supports a plethora of output formats, is able to augment the information in translated documents (e.g., MIRIAM annotations) beyond the scope of the KGML document, and amends missing components to fragmentary reactions within the pathway to allow simulations on those. KEGGtranslator converts these files to SBML, BioPAX, SIF, SBGN, SBML with qualitative modeling extension, GML, GraphML, JPG, GIF, LaTeX, etc.
- **ModelSEED**: An online resource for the analysis, comparison, reconstruction, and curation of genome-scale metabolic models. Users can submit genome sequences to the RAST annotation system, and the resulting annotation can be automatically piped into the ModelSEED to produce a draft metabolic model. The ModelSEED automatically constructs a network of metabolic reactions, gene-protein-reaction associations for each reaction, and a biomass composition reaction for each genome to produce a model of microbial metabolism that can be simulated using Flux Balance Analysis.
- **MetaMerge**: algorithm for semi-automatically reconciling a pair of existing metabolic network reconstructions into a single metabolic network model.
- **CoReCo**: algorithm for automatic reconstruction of metabolic models of related species. The first version of the software used KEGG as reaction database to link with the EC number predictions from CoReCo. Its automatic gap filling using atom map of all the reactions produce functional models ready for simulation.

#### Tools for literature

- **PUBMED**: This is an online library developed by the National Center for Biotechnology Information, which contains a massive collection of medical journals. Using the link provided by ENZYME, the search can be directed towards the organism of interest, thus recovering literature on the enzyme and its use inside of the organism.

### Methodology to draft a reconstruction

A reconstruction is built by compiling data from the resources above. Database tools such as KEGG and BioCyc can be used in conjunction with each other to find all the metabolic genes in the organism of interest. These genes will be compared to closely related organisms that have already developed reconstructions to find homologous genes and reactions. These homologous genes and reactions are carried over from the known reconstructions to form the draft reconstruction of the organism of interest. Tools such as ERGO, Pathway Tools and Model SEED can compile data into pathways to form a network of metabolic and non-metabolic pathways. These networks are then verified and refined before being made into a mathematical simulation.

The predictive aspect of a metabolic reconstruction hinges on the ability to predict the biochemical reaction catalyzed by a protein using that protein's amino acid sequence as an input, and to infer the structure of a metabolic network based on the predicted set of reactions. A network of enzymes and metabolites is drafted to relate sequences and function. When an uncharacterized protein is found in the genome, its amino acid sequence is first compared to those of previously characterized proteins to search for homology. When a homologous protein is found, the proteins are considered to have a common ancestor and their functions are inferred as being similar. However, the quality of a reconstruction model is dependent on its ability to accurately infer phenotype directly from sequence, so this rough estimation of protein function will not be sufficient. A number of algorithms and bioinformatics resources have been developed for refinement of sequence homology-based assignments of protein functions:

- **InParanoid**: Identifies eukaryotic orthologs by looking only at in-paralogs.
- **CDD**: Resource for the annotation of functional units in proteins. Its collection of domain models utilizes 3D structure to provide insights into sequence/structure/function relationships.
- **InterPro**: Provides functional analysis of proteins by classifying them into families and predicting domains and important sites.
- **STRING**: Database of known and predicted protein interactions.

Once proteins have been established, more information about the enzyme structure, reactions catalyzed, substrates and products, mechanisms, and more can be acquired from databases such as KEGG, MetaCyc and NC-IUBMB. Accurate metabolic reconstructions require additional information about the reversibility and preferred physiological direction of an enzyme-catalyzed reaction which can come from databases such as BRENDA or MetaCyc database.

## Model refinement

An initial metabolic reconstruction of a genome is typically far from perfect due to the high variability and diversity of microorganisms. Often, metabolic pathway databases such as KEGG and MetaCyc will have "holes", meaning that there is a conversion from a substrate to a product (i.e., an enzymatic activity) for which there is no known protein in the genome that encodes the enzyme that facilitates the catalysis. What can also happen in semi-automatically drafted reconstructions is that some pathways are falsely predicted and don't actually occur in the predicted manner. Because of this, a systematic verification is made in order to make sure no inconsistencies are present and that all the entries listed are correct and accurate. Furthermore, previous literature can be researched in order to support any information obtained from one of the many metabolic reaction and genome databases. This provides an added level of assurance for the reconstruction that the enzyme and the reaction it catalyzes do actually occur in the organism.

Enzyme promiscuity and spontaneous chemical reactions can damage metabolites. This metabolite damage, and its repair or pre-emption, create energy costs that need to be incorporated into models. It is likely that many genes of unknown function encode proteins that repair or pre-empt metabolite damage, but most genome-scale metabolic reconstructions only include a fraction of all genes.

Any new reaction not present in the databases needs to be added to the reconstruction. This is an iterative process that cycles between the experimental phase and the coding phase. As new information is found about the target organism, the model will be adjusted to predict the metabolic and phenotypical output of the cell. The presence or absence of certain reactions of the metabolism will affect the amount of reactants/products that are present for other reactions within the particular pathway. This is because products in one reaction go on to become the reactants for another reaction, i.e. products of one reaction can combine with other proteins or compounds to form new proteins/compounds in the presence of different enzymes or catalysts.

Francke *et al.* provide an excellent example as to why the verification step of the project needs to be performed in significant detail. During a metabolic network reconstruction of *Lactobacillus plantarum*, the model showed that succinyl-CoA was one of the reactants for a reaction that was a part of the biosynthesis of methionine. However, an understanding of the physiology of the organism would have revealed that due to an incomplete tricarboxylic acid pathway, *Lactobacillus plantarum* does not actually produce succinyl-CoA, and the correct reactant for that part of the reaction was acetyl-CoA.

Therefore, systematic verification of the initial reconstruction will bring to light several inconsistencies that can adversely affect the final interpretation of the reconstruction, which is to accurately comprehend the molecular mechanisms of the organism. Furthermore, the simulation step also ensures that all the reactions present in the reconstruction are properly balanced. To sum up, a reconstruction that is fully accurate can lead to greater insight about understanding the functioning of the organism of interest.

## Metabolic stoichiometric analysis

A metabolic network can be broken down into a stoichiometric matrix where the rows represent the compounds of the reactions, while the columns of the matrix correspond to the reactions themselves. Stoichiometry is a quantitative relationship between substrates of a chemical reaction. In order to deduce what the metabolic network suggests, recent research has centered on a few approaches, such as extreme pathways, elementary mode analysis, flux balance analysis, and a number of other constraint-based modeling methods.

### Extreme pathways

Price, Reed, and Papin, from the Palsson lab, use a method of singular value decomposition (SVD) of extreme pathways in order to understand regulation of a human red blood cell metabolism. Extreme pathways are convex basis vectors that consist of steady state functions of a metabolic network. For any particular metabolic network, there is always a unique set of extreme pathways available. Furthermore, Price, Reed, and Papin, define a constraint-based approach, where through the help of constraints like mass balance and maximum reaction rates, it is possible to develop a 'solution space' where all the feasible options fall within. Then, using a kinetic model approach, a single solution that falls within the extreme pathway solution space can be determined. Therefore, in their study, Price, Reed, and Papin, use both constraint and kinetic approaches to understand the human red blood cell metabolism. In conclusion, using extreme pathways, the regulatory mechanisms of a metabolic network can be studied in further detail.

### Elementary mode analysis

Elementary mode analysis closely matches the approach used by extreme pathways. Similar to extreme pathways, there is always a unique set of elementary modes available for a particular metabolic network. These are the smallest sub-networks that allow a metabolic reconstruction network to function in steady state. According to Stelling (2002), elementary modes can be used to understand cellular objectives for the overall metabolic network. Furthermore, elementary mode analysis takes into account stoichiometrics and thermodynamics when evaluating whether a particular metabolic route or network is feasible and likely for a set of proteins/enzymes.

### Minimal metabolic behaviors (MMBs)

In 2009, Larhlimi and Bockmayr presented a new approach called "minimal metabolic behaviors" for the analysis of metabolic networks. Like elementary modes or extreme pathways, these are uniquely determined by the network, and yield a complete description of the flux cone. However, the new description is much more compact. In contrast with elementary modes and extreme pathways, which use an inner description based on generating vectors of the flux cone, MMBs are using an outer description of the flux cone. This approach is based on sets of non-negativity constraints. These can be identified with irreversible reactions, and thus have a direct biochemical interpretation. One can characterize a metabolic network by MMBs and the reversible metabolic space.

### Flux balance analysis

A different technique to simulate the metabolic network is to perform flux balance analysis. This method uses linear programming, but in contrast to elementary mode analysis and extreme pathways, only a single solution results in the end. Linear programming is usually used to obtain the maximum potential of the objective function that you are looking at, and therefore, when using flux balance analysis, a single solution is found to the optimization problem. In a flux balance analysis approach, exchange fluxes are assigned to those metabolites that enter or leave the particular network only. Those metabolites that are consumed within the network are not assigned any exchange flux value. Also, the exchange fluxes along with the enzymes can have constraints ranging from a negative to positive value (ex: -10 to 10).

Furthermore, this particular approach can accurately define if the reaction stoichiometry is in line with predictions by providing fluxes for the balanced reactions. Also, flux balance analysis can highlight the most effective and efficient pathway through the network in order to achieve a particular objective function. In addition, gene knockout studies can be performed using flux balance analysis. The enzyme that correlates to the gene that needs to be removed is given a constraint value of 0. Then, the reaction that the particular enzyme catalyzes is completely removed from the analysis.

### Dynamic simulation and parameter estimation

In order to perform a dynamic simulation with such a network it is necessary to construct an ordinary differential equation system that describes the rates of change in each metabolite's concentration or amount. To this end, a rate law, i.e., a kinetic equation that determines the rate of reaction based on the concentrations of all reactants is required for each reaction. Software packages that include numerical integrators, such as COPASI or SBMLsimulator, are then able to simulate the system dynamics given an initial condition. Often these rate laws contain kinetic parameters with uncertain values. In many cases it is desired to estimate these parameter values with respect to given time-series data of metabolite concentrations. The system is then supposed to reproduce the given data. For this purpose the distance between the given data set and the result of the simulation, i.e., the numerically or in few cases analytically obtained solution of the differential equation system is computed. The values of the parameters are then estimated to minimize this distance. One step further, it may be desired to estimate the mathematical structure of the differential equation system because the real rate laws are not known for the reactions within the system under study. To this end, the program SBMLsqueezer allows automatic creation of appropriate rate laws for all reactions with the network.

### Synthetic accessibility

Synthetic accessibility is a simple approach to network simulation whose goal is to predict which metabolic gene knockouts are lethal. The synthetic accessibility approach uses the topology of the metabolic network to calculate the sum of the minimum number of steps needed to traverse the metabolic network graph from the inputs, those metabolites available to the organism from the environment, to the outputs, metabolites needed by the organism to survive. To simulate a gene knockout, the reactions enabled by the gene are removed from the network and the synthetic accessibility metric is recalculated. An increase in the total number of steps is predicted to cause lethality. Wunderlich and Mirny showed this simple, parameter-free approach predicted knockout lethality in *E. coli* and *S. cerevisiae* as well as elementary mode analysis and flux balance analysis in a variety of media.

## Applications of a reconstruction

- Several inconsistencies exist between gene, enzyme, reaction databases, and published literature sources regarding the metabolic information of an organism. A reconstruction is a systematic verification and compilation of data from various sources that takes into account all of the discrepancies.
- The combination of relevant metabolic and genomic information of an organism.
- Metabolic comparisons can be performed between various organisms of the same species as well as between different organisms.
- Analysis of synthetic lethality
- Predict adaptive evolution outcomes
- Use in metabolic engineering for high value outputs

Reconstructions and their corresponding models allow the formulation of hypotheses about the presence of certain enzymatic activities and the production of metabolites that can be experimentally tested, complementing the primarily discovery-based approach of traditional microbial biochemistry with hypothesis-driven research. The results these experiments can uncover novel pathways and metabolic activities and decipher between discrepancies in previous experimental data. Information about the chemical reactions of metabolism and the genetic background of various metabolic properties (sequence to structure to function) can be utilized by genetic engineers to modify organisms to produce high value outputs whether those products be medically relevant like pharmaceuticals; high value chemical intermediates such as terpenoids and isoprenoids; or biotechnological outputs like biofuels, or polyhydroxybutyrates also known as bioplastics.

Metabolic network reconstructions and models are used to understand how an organism or parasite functions inside of the host cell. For example, if the parasite serves to compromise the immune system by lysing macrophages, then the goal of metabolic reconstruction/simulation would be to determine the metabolites that are essential to the organism's proliferation inside of macrophages. If the proliferation cycle is inhibited, then the parasite would not continue to evade the host's immune system. A reconstruction model serves as a first step to deciphering the complicated mechanisms surrounding disease. These models can also look at the minimal genes necessary for a cell to maintain virulence. The next step would be to use the predictions and postulates generated from a reconstruction model and apply it to discover novel biological functions such as drug-engineering and drug delivery techniques.
