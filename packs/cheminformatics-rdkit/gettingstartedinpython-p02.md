---
title: "Getting Started with the RDKit in Python (part 2/3)"
source: https://www.rdkit.org/docs/GettingStartedInPython.html
domain: cheminformatics-rdkit
license: CC-BY-SA-4.0
tags: cheminformatics rdkit, molecular descriptor, smiles notation, chemical fingerprint
fetched: 2026-07-02
part: 2/3
---

## Maximum Common Substructure

There are 2 methods for finding maximum common substructures. The first, FindMCS, finds a single fragment maximum common substructure (MCS) of two or more molecules: The second, RascalMCES, finds the maximum common edge substructure (MCES) between two molecules and can return a multi-fragment MCES. The difference is demonstrated with the following pair of molecules:

| (_images/mcs_example_1.png) |
|---|
| (_images/mcs_example_2.png) |

FMCS gives this maximum common substructure:

| (_images/mcs_example_3.png) |
|---|
| (_images/mcs_example_4.png) |

Whereas RascalMCES gives:

| (_images/mcs_example_5.png) |
|---|
| (_images/mcs_example_6.png) |

### FindMCS

FindMCS operates on 2 or more molecules:

```pycon
>>> from rdkit.Chem import rdFMCS
>>> mol1 = Chem.MolFromSmiles("O=C(NCc1cc(OC)c(O)cc1)CCCC/C=C/C(C)C")
>>> mol2 = Chem.MolFromSmiles("CC(C)CCCCCC(=O)NCC1=CC(=C(C=C1)O)OC")
>>> mol3 = Chem.MolFromSmiles("c1(C=O)cc(OC)c(O)cc1")
>>> mols = [mol1,mol2,mol3]
>>> res=rdFMCS.FindMCS(mols)
>>> res
<rdkit.Chem.rdFMCS.MCSResult object at 0x...>
>>> res.numAtoms
10
>>> res.numBonds
10
>>> res.smartsString
'[#6]1(-[#6]):[#6]:[#6](-[#8]-[#6]):[#6](:[#6]:[#6]:1)-[#8]'
>>> res.canceled
False
```

It returns an MCSResult instance with information about the number of atoms and bonds in the MCS, the SMARTS string which matches the identified MCS, and a flag saying if the algorithm timed out. If no MCS is found then the number of atoms and bonds is set to 0 and the SMARTS to `''`.

By default, two atoms match if they are the same element and two bonds match if they have the same bond type. Specify `atomCompare` and `bondCompare` to use different comparison functions, as in:

```pycon
>>> mols = (Chem.MolFromSmiles('NCC'),Chem.MolFromSmiles('OC=C'))
>>> rdFMCS.FindMCS(mols).smartsString
'[#6]'
>>> rdFMCS.FindMCS(mols, atomCompare=rdFMCS.AtomCompare.CompareAny).smartsString
'[#7,#8]-[#6]'
>>> rdFMCS.FindMCS(mols, bondCompare=rdFMCS.BondCompare.CompareAny).smartsString
'[#6]-,=[#6]'
```

The options for the atomCompare argument are: CompareAny says that any atom matches any other atom, CompareElements compares by element type, and CompareIsotopes matches based on the isotope label. Isotope labels can be used to implement user-defined atom types. A bondCompare of CompareAny says that any bond matches any other bond, CompareOrderExact says bonds are equivalent if and only if they have the same bond type, and CompareOrder allows single and aromatic bonds to match each other, but requires an exact order match otherwise:

```pycon
>>> mols = (Chem.MolFromSmiles('c1ccccc1'),Chem.MolFromSmiles('C1CCCC=C1'))
>>> rdFMCS.FindMCS(mols,bondCompare=rdFMCS.BondCompare.CompareAny).smartsString
'[#6]1:,-[#6]:,-[#6]:,-[#6]:,-[#6]:,=[#6]:,-1'
>>> rdFMCS.FindMCS(mols,bondCompare=rdFMCS.BondCompare.CompareOrderExact).smartsString
'[#6]'
>>> rdFMCS.FindMCS(mols,bondCompare=rdFMCS.BondCompare.CompareOrder).smartsString
'[#6](:,-[#6]:,-[#6]:,-[#6]):,-[#6]:,-[#6]'
```

A substructure has both atoms and bonds. By default, the algorithm attempts to maximize the number of bonds found. You can change this by setting the `maximizeBonds` argument to False. Maximizing the number of bonds tends to maximize the number of rings, although two small rings may have fewer bonds than one large ring.

You might not want a 3-valent nitrogen to match one which is 5-valent. The default `matchValences` value of False ignores valence information. When True, the atomCompare setting is modified to also require that the two atoms have the same valency.

```pycon
>>> mols = (Chem.MolFromSmiles('NC1OC1'),Chem.MolFromSmiles('C1OC1[N+](=O)[O-]'))
>>> rdFMCS.FindMCS(mols).numAtoms
4
>>> rdFMCS.FindMCS(mols, matchValences=True).numBonds
3
```

It can be strange to see a linear carbon chain match a carbon ring, which is what the `ringMatchesRingOnly` default of False does. If you set it to True then ring bonds will only match ring bonds.

```pycon
>>> mols = [Chem.MolFromSmiles("C1CCC1CCC"), Chem.MolFromSmiles("C1CCCCCC1")]
>>> rdFMCS.FindMCS(mols).smartsString
'[#6](-[#6]-[#6])-[#6]-[#6]-[#6]-[#6]'
>>> rdFMCS.FindMCS(mols, ringMatchesRingOnly=True).smartsString
'[#6&R](-&@[#6&R]-&@[#6&R])-&@[#6&R]'
```

Notice that the SMARTS returned now include ring queries on the atoms and bonds.

You can further restrict things and require that partial rings (as in this case) are not allowed. That is, if an atom is part of the MCS and the atom is in a ring of the entire molecule then that atom is also in a ring of the MCS. Setting `completeRingsOnly` to True toggles this requirement.

```pycon
>>> mols = [Chem.MolFromSmiles("CCC1CC2C1CN2"), Chem.MolFromSmiles("C1CC2C1CC2")]
>>> rdFMCS.FindMCS(mols).smartsString
'[#6]1-[#6]-[#6](-[#6]-1-[#6])-[#6]'
>>> rdFMCS.FindMCS(mols, ringMatchesRingOnly=True).smartsString
'[#6]1-&@[#6]-&@[#6](-&@[#6]-&@1)-&@[#6&R]'
>>> rdFMCS.FindMCS(mols, completeRingsOnly=True).smartsString
'[#6]1-&@[#6]-&@[#6]-&@[#6]-&@1'
```

Of course the two options can be combined with each other:

```pycon
>>> ms = [Chem.MolFromSmiles(x) for x in ('CC1CCC1','CCC1CC1',)]
>>> rdFMCS.FindMCS(ms,ringMatchesRingOnly=True).smartsString
'[#6&!R]-&!@[#6&R](-&@[#6&R])-&@[#6&R]'
>>> rdFMCS.FindMCS(ms,completeRingsOnly=True).smartsString
'[#6]-&!@[#6]'
>>> rdFMCS.FindMCS(ms,ringMatchesRingOnly=True,completeRingsOnly=True).smartsString
'[#6&!R]-&!@[#6&R]'
```

The MCS algorithm will exhaustively search for a maximum common substructure. Typically this takes a fraction of a second, but for some comparisons this can take minutes or longer. Use the `timeout` parameter to stop the search after the given number of seconds (wall-clock seconds, not CPU seconds) and return the best match found in that time. If timeout is reached then the `canceled` property of the MCSResult will be True instead of False.

```pycon
>>> mols = [Chem.MolFromSmiles("Nc1ccccc1"*10), Chem.MolFromSmiles("Nc1ccccccccc1"*10)]
>>> rdFMCS.FindMCS(mols, timeout=1).canceled
True
```

(The MCS after 50 seconds contained 511 atoms.)

### RascalMCES

RascalMCES can only work on 2 molecules at a time:

```pycon
>>> from rdkit.Chem import rdRascalMCES
>>> mol1 = Chem.MolFromSmiles("CN(C)c1ccc(CC(=O)NCCCCCCCCCCNC23CC4CC(C2)CC(C3)C4)cc1 CHEMBL153934")
>>> mol2 = Chem.MolFromSmiles("CN(C)c1ccc(CC(=O)NCCCCCCCNC23CC4CC(C2)CC(C3)C4)cc1 CHEMBL152361")
>>> res = rdRascalMCES.FindMCES(mol1, mol2)
>>> res[0].smartsString
'CN(-C)-c1:c:c:c(-CC(=O)-NCCCCCCC):c:c:1.NC12CC3CC(-C1)-CC(-C2)-C3'
>>> len(res[0].bondMatches())
33
```

It returns a list of RascalResult objects. Each RascalResult contains the 2 molecules that the result pertains to, the SMARTS string of the MCES, the lists of atoms and bonds in the two molecules that match, the Johnson similarity between the 2 molecules, the number of fragments in the MCES, the number of atoms in the largest fragment and whether the run timed out or not. There is also the method largestFragmentOnly(), which cuts the MCES down to the largest single fragment. This is a non-reversible change, so if you want both results, take a copy first.

By default, the MCES algorithm returns the first result it finds of maximum size. Because of symmetry, there may be other equivalent solutions with the same number of atoms and bonds, but with different equivalent bonds matched to each other. If you want to see all MCESs of maximum size, you can use the option allBestMCESs = True. This will increase the run time, partly because more branches in the search tree must be examined, but mostly because sorting the multiple results is quite time-consuming. The results are returned in a consistent order sorted by number of bond matches, then number of fragments (fewer first), then largest fragment size and so on. Some of these aren’t trivial to compute. The adamantane example above is particularly extreme because not only is there extensive symmetry about the adamantane end and 2-fold symmetry at the phenyl end but also several points of breaking the matching alkyl chain all of which give rise to valid MCESs of the same size. In this case, sorting into a consistent order takes significantly longer than determining the MCESs in the first place.

The MCES differs from a conventional MCS in that it is the maximum common substructure based on bonds rather than atoms. Often the result is the same, but not always.

The Johnson similarity is akin to a Tanimoto similarity, but expressed in terms of the atoms and bonds in the MCES. It is the square of the sum of the number of atoms and bonds in the MCES divided by the product of the sums of the numbers of atoms and bonds in the 2 input molecules. It has values between 0.0 (no MCES between the molecules) and 1.0 (the molecules are identical). A key source of efficiency in the RASCAL algorithm is a fast and correct prediction of a maximum value for the Johnson similarity between 2 molecules and hence the maximum size of the MCES. The first step in the algorithm is then a screening, whereby the full MCES determination is not performed if the predicted similarity is less than some desired threshold. The final similarity between the 2 molecules may be less than the threshold, but it will never be higher than the predicted upper bound. RASCAL stems from RApid Similarity CALulation.

The default settings for RascalMCES are good for general use, but they may be altered by passing an optional RascalOptions object:

```pycon
>>> mol1 = Chem.MolFromSmiles('Oc1cccc2C(=O)C=CC(=O)c12')
>>> mol2 = Chem.MolFromSmiles('O1C(=O)C=Cc2cc(OC)c(O)cc12')
>>> results = rdRascalMCES.FindMCES(mol1, mol2)
>>> len(results)
0
>>> opts = rdRascalMCES.RascalOptions()
>>> opts.similarityThreshold = 0.5
>>> results = rdRascalMCES.FindMCES(mol1, mol2, opts)
>>> len(results)
1
>>> f'{results[0].similarity:.2f}'
'0.37'
>>> results[0].smartsString
'Oc1:c:c:c:c:c:1.[#6]=O'
>>> opts.minFragSize = 3
>>> results = rdRascalMCES.FindMCES(mol1, mol2, opts)
>>> len(results)
1
>>> f'{results[0].similarity:.2f}'
'0.25'
>>> results[0].smartsString
'Oc1:c:c:c:c:c:1'
```

In this case, the upper bound on the similarity score is below the default threshold of 0.7, so no results are returned. Setting the threshold to 0.5 produces the second result although, as can be seen, the final similarity is substantially below the threshold. This example also shows a disadvantage of the MCES method, which is that it can produce small fragments in the MCES which are rarely helpful. The option minFragSize can be used to over-ride the default value of -1, which means no minimum size.

Like FindMCS, there is a ringMatchesRingOnly option, and also there’s completeAromaticRings, which is True by default, and means that MCESs won’t be returned with partial aromatic rings matching:

```pycon
>>> mol1 = Chem.MolFromSmiles('C1CCCC1c1ccncc1')
>>> mol2 = Chem.MolFromSmiles('C1CCCC1c1ccccc1')
>>> results = rdRascalMCES.FindMCES(mol1, mol2, opts)
>>> f'{results[0].similarity:.2f}'
'0.27'
>>> results[0].smartsString
'C1CCCC1-c'
>>> opts.completeAromaticRings = False
>>> results = rdRascalMCES.FindMCES(mol1, mol2, opts)
>>> f'{results[0].similarity:.2f}'
'0.76'
>>> results[0].smartsString
'C1CCCC1-c(:c:c):c:c'
```

This result may look a bit odd, with a single aromatic carbon in the first SMARTS string. This is a consequence of the fact that the MCES works on matching bonds. A better, atom-centric, representation might be C1CCC[$(C-c)]1. When the completeAromaticRings option is set to False, a larger MCES is found, with just the pyridine nitrogen atom not matching the corresponding phenyl carbon atom.

There are 2 ways of getting an MCES that is just a single fragment. The first is to use the option *opts.singleLargestFrag = True*. The second is to use the method *opts.allBestMCESs*, find the result with the largest single fragment and use its *largestFragmentOnly*. The two methods are equivalent - the first option does this internally.

The result of the singleLargestFrag option may not be the largest single possible fragment in common between the two molecules. For example, consider the 2 molecules

There are 8 multi-fragment MCESs, all with 12 bonds, of which one of the ones with the largest single fragment is

The single largest fragment is thus the 3-propylpiperidine. However, if you use rdFMCS with the same pair of molecules, you get

Which has a 10 atom, 9 bond fragment which cannot be part of a fragmented MCES of 12 bonds, so doesn’t appear in the Rascal results set. If you are sure you will only ever be interested in the single largest fragment in common, you should use rdFMCS.

### Clustering with Rascal

There are 2 clustering methods available using the Johnson metric. The first, RascalCluster, is a fuzzy method described in ‘A Line Graph Algorithm for Clustering Chemical Structures Based on Common Substructural Cores’, JW Raymond, PW Willett (https://match.pmf.kg.ac.rs/electronic_versions/Match48/match48_197-207.pdf also available at https://eprints.whiterose.ac.uk/77598/). The second, RascalButinaCluster, uses the Butina sphere-exclusion algorithm (Butina JCICS 39 747-750 (1999)). Because of the time-consuming nature of the MCES determination, these clustering methods can be slow to run, so are best used on small sets (no more than a few hundred molecules) of small molecules.


## Fingerprinting and Molecular Similarity

The RDKit has a variety of built-in functionality for generating molecular fingerprints and using them to calculate molecular similarity.

The most straightforward and consistent way to get fingerprints is to create a FingeprintGenerator object for your fingerprint type of interest and then use that to calculate fingerprints. Fingerprint generators provide a consistent interface to all the supported fingerprinting methods and allow easy generation of fingerprints as:

- bit vectors : `fpgen.GetFingerprint`
- sparse (unfolded) bit vectors : `fpgen.GetSparseFingerprint`
- count vectors : `fpgen.GetCountFingerprint`
- sparse (unfolded) count vectors : `fpgen.GetSparseCountFingerprint`

Note that there are older, legacy methods of generating fingerprints with the RDKit which are still supported, but these will not be covered here.

### RDKit (Topological) Fingerprints

```pycon
>>> from rdkit import DataStructs
>>> ms = [Chem.MolFromSmiles('CCOC'), Chem.MolFromSmiles('CCO'),
... Chem.MolFromSmiles('COC')]
>>> fpgen = AllChem.GetRDKitFPGenerator()
>>> fps = [fpgen.GetFingerprint(x) for x in ms]
>>> DataStructs.TanimotoSimilarity(fps[0],fps[1])
0.6...
>>> DataStructs.TanimotoSimilarity(fps[0],fps[2])
0.4...
>>> DataStructs.TanimotoSimilarity(fps[1],fps[2])
0.25
```

The examples above used Tanimoto similarity, but one can use different similarity metrics:

```pycon
>>> DataStructs.DiceSimilarity(fps[0],fps[1])
0.75
```

Available similarity metrics include Tanimoto, Dice, Cosine, Sokal, Russel, Kulczynski, McConnaughey, and Tversky.

More details about the algorithm used for the RDKit fingerprint can be found in the “RDKit Book”.

The default set of parameters used by the fingerprinter is:

- minimum path size: 1 bond
- maximum path size: 7 bonds
- fingerprint size: 2048 bits
- number of bits set per hash: 2

You can control these when calling `AllChem.GetRDKitFPGenerator()`:

```pycon
>>> fpgen = AllChem.GetRDKitFPGenerator(maxPath=2,fpSize=1024)
>>> fps = [fpgen.GetFingerprint(x) for x in ms]
>>> DataStructs.TanimotoSimilarity(fps[0],fps[2])
0.5
```

### Atom Pairs and Topological Torsions

Atom-pair descriptors [3] are available in several different forms. The standard form is as fingerprint including counts for each bit instead of just zeros and ones:

```pycon
>>> ms = [Chem.MolFromSmiles('C1CCC1OCC'),Chem.MolFromSmiles('CC(C)OCC'),Chem.MolFromSmiles('CCOCC')]
>>> fpgen = AllChem.GetAtomPairGenerator()
>>> pairFps = [fpgen.GetSparseCountFingerprint(x) for x in ms]
```

Because the space of bits that can be included in atom-pair fingerprints is huge, they are stored in a sparse manner. We can get the list of bits and their counts for each fingerprint as a dictionary:

```pycon
>>> pairFps[-1].GetNonzeroElements()
{541732: 1, 558113: 2, 558115: 2, 558146: 1, 1606690: 2, 1606721: 2}
```

Unlike most other fingerprint types, descriptions of the bits are directly available:

```pycon
>>> from rdkit.Chem.AtomPairs import Pairs
>>> Pairs.ExplainPairScore(558115)
(('C', 1, 0), 3, ('C', 2, 0))
```

The above means: C with 1 neighbor and 0 pi electrons which is 3 bonds from a C with 2 neighbors and 0 pi electrons

The usual metric for similarity between atom-pair fingerprints is Dice similarity:

```pycon
>>> from rdkit import DataStructs
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[1])
0.333...
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[2])
0.258...
>>> DataStructs.DiceSimilarity(pairFps[1],pairFps[2])
0.56
```

It’s also possible to get atom-pair descriptors encoded as a standard bit vector fingerprint.

```pycon
>>> pairFps = [fpgen.GetFingerprint(x) for x in ms]
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[1])
0.352...
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[2])
0.266...
>>> DataStructs.DiceSimilarity(pairFps[1],pairFps[2])
0.583...
```

By default the atom pair bit vector fingerprints use a scheme which simulates counts in the bit vectors (described in detail in the “RDKit Book”), but this can be disabled:

```pycon
>>> fpgen = AllChem.GetAtomPairGenerator(countSimulation=False)
>>> pairFps = [fpgen.GetFingerprint(x) for x in ms]
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[1])
0.5
>>> DataStructs.DiceSimilarity(pairFps[0],pairFps[2])
0.4
>>> DataStructs.DiceSimilarity(pairFps[1],pairFps[2])
0.625
```

Topological torsion descriptors [4] are calculated in essentially the same way:

```pycon
>>> fpgen = AllChem.GetTopologicalTorsionGenerator()
>>> tts = [fpgen.GetSparseCountFingerprint(x) for x in ms]
>>> DataStructs.DiceSimilarity(tts[0],tts[1])
0.166...
```

Topological torsion fingerprints, like atom-pair fingerprints, use a count simulation scheme by default when generating bit vector fingerprints

### Morgan Fingerprints (Circular Fingerprints)

This family of fingerprints, better known as circular fingerprints [5], is built by applying the Morgan algorithm to a set of user-supplied atom invariants. When generating Morgan fingerprints, the radius of the fingerprint can also be provided (the default is 3):

```pycon
>>> from rdkit.Chem import AllChem
>>> fpgen = AllChem.GetMorganGenerator(radius=2)
>>> m1 = Chem.MolFromSmiles('Cc1ccccc1')
>>> fp1 = fpgen.GetSparseCountFingerprint(m1)
>>> fp1
<rdkit.DataStructs.cDataStructs.ULongSparseIntVect object at 0x...>
>>> m2 = Chem.MolFromSmiles('Cc1ncccc1')
>>> fp2 = fpgen.GetSparseCountFingerprint(m2)
>>> DataStructs.DiceSimilarity(fp1,fp2)
0.55...
```

Morgan fingerprints, like atom pairs and topological torsions, are often used as counts, but it’s also possible to calculate them as bit vectors, the default fingerprint size is 2048 bits:

```pycon
>>> fp1 = fpgen.GetFingerprint(m1)
>>> fp1
<rdkit.DataStructs.cDataStructs.ExplicitBitVect object at 0x...>
>>> len(fp1)
2048
>>> fp2 = fpgen.GetFingerprint(m2)
>>> DataStructs.DiceSimilarity(fp1,fp2)
0.51...
```

The default atom invariants use connectivity information similar to those used for the well known ECFP family of fingerprints. Feature-based invariants, similar to those used for the FCFP fingerprints, can also be used by creating the fingerprint generator with an appropriate atom invariant generator. The feature definitions used are defined in the section Feature Definitions Used in the Morgan Fingerprints. At times this can lead to quite different similarity scores:

```pycon
>>> m1 = Chem.MolFromSmiles('c1ccccn1')
>>> m2 = Chem.MolFromSmiles('c1ccco1')
>>> fpgen = AllChem.GetMorganGenerator(radius=2)
>>> fp1 = fpgen.GetSparseCountFingerprint(m1)
>>> fp2 = fpgen.GetSparseCountFingerprint(m2)
>>> invgen = AllChem.GetMorganFeatureAtomInvGen()
>>> ffpgen = AllChem.GetMorganGenerator(radius=2, atomInvariantsGenerator=invgen)
>>> ffp1 = ffpgen.GetSparseCountFingerprint(m1)
>>> ffp2 = ffpgen.GetSparseCountFingerprint(m2)
>>> DataStructs.DiceSimilarity(fp1,fp2)
0.36...
>>> DataStructs.DiceSimilarity(ffp1,ffp2)
0.90...
```

When comparing the ECFP/FCFP fingerprints and the Morgan fingerprints generated by the RDKit, remember that the 4 in ECFP4 corresponds to the diameter of the atom environments considered, while the Morgan fingerprints take a radius parameter. So the examples above, with radius=2, are roughly equivalent to ECFP4 and FCFP4.

The user can also provide their own atom invariants using the optional `customAtomInvariants` argument to the `GetFingerprint()` call. Here’s a simple example that uses a constant for the invariant; the resulting fingerprints compare the topology of molecules:

```pycon
>>> m1 = Chem.MolFromSmiles('Cc1ccccc1')
>>> m2 = Chem.MolFromSmiles('Cc1ncncn1')
>>> fpgen = AllChem.GetMorganGenerator(radius=2)
>>> fp1 = fpgen.GetFingerprint(m1,customAtomInvariants=[1]*m1.GetNumAtoms())
>>> fp2 = fpgen.GetFingerprint(m2,customAtomInvariants=[1]*m2.GetNumAtoms())
>>> fp1==fp2
True
```

Note that bond order is by default still considered:

```pycon
>>> m3 = Chem.MolFromSmiles('CC1CCCCC1')
>>> fp3 = fpgen.GetFingerprint(m3,customAtomInvariants=[1]*m3.GetNumAtoms())
>>> fp1==fp3
False
```

But this can also be turned off:

```pycon
>>> fpgen = AllChem.GetMorganGenerator(radius=2,useBondTypes=False)
>>> fp1 = fpgen.GetFingerprint(m1,customAtomInvariants=[1]*m1.GetNumAtoms())
>>> fp3 = fpgen.GetFingerprint(m3,customAtomInvariants=[1]*m3.GetNumAtoms())
>>> fp1==fp3
True
```

### MACCS Keys

There is a SMARTS-based implementation of the 166 public MACCS keys. This is not currently supported by the RDKit’s fingerprint generators, so you have to use a different interface.

```pycon
>>> from rdkit.Chem import MACCSkeys
>>> ms = [Chem.MolFromSmiles('CCOC'), Chem.MolFromSmiles('CCO'),
... Chem.MolFromSmiles('COC')]
>>> fps = [MACCSkeys.GenMACCSKeys(x) for x in ms]
>>> DataStructs.TanimotoSimilarity(fps[0],fps[1])
0.5
>>> DataStructs.TanimotoSimilarity(fps[0],fps[2])
0.538...
>>> DataStructs.TanimotoSimilarity(fps[1],fps[2])
0.214...
```

The MACCS keys were critically evaluated and compared to other MACCS implementations in Q3 2008. In cases where the public keys are fully defined, things looked pretty good.

### Explaining bits from fingerprints

The fingerprint generators can collect information about the atoms/bonds involved in setting bits when a fingerprint is generated. This information is quite useful for understanding which parts of a molecule were involved in each bit.

Each fingerprinting method provides different information, but this is all accessed using the additionalOutput argument to the fingerprinting functions.

#### Morgan Fingerprints

Information is available about the atoms that contribute to particular bits in the Morgan fingerprint via the bit info map. This is a dictionary with one entry per bit set in the fingerprint, the keys are the bit ids, the values are lists of (atom index, radius) tuples.

```pycon
>>> m = Chem.MolFromSmiles('c1cccnc1C')
>>> fpgen = AllChem.GetMorganGenerator(radius=2)
>>> ao = AllChem.AdditionalOutput()
>>> ao.CollectBitInfoMap()
>>> fp = fpgen.GetSparseCountFingerprint(m,additionalOutput=ao)
>>> len(fp.GetNonzeroElements())
16
>>> info = ao.GetBitInfoMap()
>>> len(info)
16
>>> info[98513984]
((1, 1), (2, 1))
>>> info[4048591891]
((5, 2),)
```

Interpreting the above: bit 98513984 is set twice: once by atom 1 and once by atom 2, each at radius 1. Bit 4048591891 is set once by atom 5 at radius 2.

Focusing on bit 4048591891, we can extract the submolecule consisting of all atoms within a radius of 2 of atom 5:

```pycon
>>> env = Chem.FindAtomEnvironmentOfRadiusN(m,2,5)
>>> amap={}
>>> submol=Chem.PathToSubmol(m,env,atomMap=amap)
>>> submol.GetNumAtoms()
6
>>> amap
{0: 0, 1: 1, 3: 2, 4: 3, 5: 4, 6: 5}
```

And then “explain” the bit by generating SMILES for that submolecule:

```pycon
>>> Chem.MolToSmiles(submol)
'ccc(C)nc'
```

This is more useful when the SMILES is rooted at the central atom:

```pycon
>>> Chem.MolToSmiles(submol,rootedAtAtom=amap[5],canonical=False)
'c(cc)(nc)C'
```

An alternate (and faster, particularly for large numbers of molecules) approach to do the same thing, using the function `rdkit.Chem.MolFragmentToSmiles()` :

```pycon
>>> atoms=set()
>>> for bidx in env:
...     atoms.add(m.GetBondWithIdx(bidx).GetBeginAtomIdx())
...     atoms.add(m.GetBondWithIdx(bidx).GetEndAtomIdx())
...
>>> Chem.MolFragmentToSmiles(m,atomsToUse=list(atoms),bondsToUse=env,rootedAtAtom=5)
'c(C)(cc)nc'
```

#### RDKit Fingerprints

Information is available about the bond paths that contribute to particular bits in the RDKit fingerprint via the bit info map. This is a dictionary with one entry per bit set in the fingerprint, the keys are the bit ids, the values are tuples of tuples containing bond indices.

```pycon
>>> m = Chem.MolFromSmiles('CCO')
>>> fpgen = AllChem.GetRDKitFPGenerator()
>>> ao = AllChem.AdditionalOutput()
>>> ao.CollectBitPaths()
>>> fp = fpgen.GetSparseCountFingerprint(m,additionalOutput=ao)
>>> len(fp.GetNonzeroElements())
6
>>> paths = ao.GetBitPaths()
>>> len(paths)
6
>>> paths[54413874]
((1,),)
>>> paths[1135572127]
((0, 1),)
>>> paths[1524090560]
((0, 1),)
```

Those last two examples, which each correspond to the path containing bonds 0 and 1, demonstrate that by default each path sets two bits in the RDKit fingerprint. We can, of course, create a fingerprint generator which does not do this:

```pycon
>>> fpgen = AllChem.GetRDKitFPGenerator(numBitsPerFeature=1)
>>> ao = AllChem.AdditionalOutput()
>>> ao.CollectBitPaths()
>>> fp = fpgen.GetSparseCountFingerprint(m,additionalOutput=ao)
>>> len(fp.GetNonzeroElements())
3
>>> ao.GetBitPaths()
{1524090560: ((0, 1),), 4274652475: ((1,),), 4275705116: ((0,),)}
```

Here we can also use the bond path information to create submolecules:

```pycon
>>> envs = ao.GetBitPaths()[4274652475]
>>> envs
((1,),)
>>> env = envs[0]
>>> atoms=set()
>>> for bidx in env:
...     atoms.add(m.GetBondWithIdx(bidx).GetBeginAtomIdx())
...     atoms.add(m.GetBondWithIdx(bidx).GetEndAtomIdx())
...
>>> Chem.MolFragmentToSmiles(m,atomsToUse=list(atoms),bondsToUse=env)
'CO'
```

### Generating images of fingerprint bits

For the Morgan and RDKit fingerprint types, it’s possible to generate images of the atom environment that defines the bit using the functions `rdkit.Chem.Draw.DrawMorganBit()` and `rdkit.Chem.Draw.DrawRDKitBit()`

```pycon
>>> from rdkit.Chem import Draw
>>> mol = Chem.MolFromSmiles('c1ccccc1CC1CC1')
>>> fpgen = AllChem.GetMorganGenerator(radius=2)
>>> ao = AllChem.AdditionalOutput()
>>> ao.CollectBitInfoMap()
>>> fp = fpgen.GetFingerprint(mol,additionalOutput=ao)
>>> bi = ao.GetBitInfoMap()
>>> bi[872]
((6, 2),)
>>> mfp2_svg = Draw.DrawMorganBit(mol, 872, bi, useSVG=True)
>>> fpgen = AllChem.GetRDKitFPGenerator()
>>> ao = AllChem.AdditionalOutput()
>>> ao.CollectBitPaths()
>>> fp = fpgen.GetFingerprint(mol,additionalOutput=ao)
>>> rdkbi = ao.GetBitPaths()
>>> rdkbi[1553]
((0, 1, 9, 5, 4), (2, 3, 4, 9, 5))
>>> rdk_svg = Draw.DrawRDKitBit(mol, 1553, rdkbi, useSVG=True)
```

Producing these images:

| (_images/mfp2_bit872.svg) | (_images/rdk_bit1553.svg) |
|---|---|
| Morgan bit | RDKit bit |

The default highlight colors for the Morgan bits indicate:

> - blue: the central atom in the environment
> - yellow: aromatic atoms
> - gray: aliphatic ring atoms

The default highlight colors for the RDKit bits indicate:

> - yellow: aromatic atoms

Note that in cases where the same bit is set by multiple atoms in the molecule (as for bit 1553 for the RDKit fingerprint in the example above), the drawing functions will display the first example. You can change this by specifying which example to show:

```pycon
>>> rdk_svg = Draw.DrawRDKitBit(mol, 1553, rdkbi, whichExample=1, useSVG=True)
```

Producing this image:

| (_images/rdk_bit1553_2.svg) |
|---|
| RDKit bit |

### Picking Diverse Molecules Using Fingerprints

A common task is to pick a small subset of diverse molecules from a larger set. The RDKit provides a number of approaches for doing this in the `rdkit.SimDivFilters` module. The most efficient of these uses the MaxMin algorithm. [6] Here’s an example:

Start by reading in a set of molecules and generating Morgan fingerprints:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import rdFingerprintGenerator
>>> fpgen = rdFingerprintGenerator.GetMorganGenerator(radius=3)
>>> from rdkit import DataStructs
>>> from rdkit.SimDivFilters.rdSimDivPickers import MaxMinPicker
>>> with Chem.SDMolSupplier('data/actives_5ht3.sdf') as suppl:
...   ms = [x for x in suppl if x is not None]
>>> fps = [fpgen.GetFingerprint(x) for x in ms]
>>> nfps = len(fps)
```

Now create a picker and grab a set of 10 diverse molecules:

```pycon
>>> picker = MaxMinPicker()
>>> pickIndices = picker.LazyBitVectorPick(fps,nfps,10,seed=23)
>>> list(pickIndices)
[93, 137, 135, 109, 18, 150, 142, 12, 6, 160]
```

Note that the picker just returns indices of the fingerprints; we can get the molecules themselves as follows:

```pycon
>>> picks = [ms[x] for x in pickIndices]
```

If we aren’t working with bit vector fingerprints, we can also do a diversity pick by providing our own distance matrix to the algorithm. This is less efficient than the above approach, but still works quite quickly:

```pycon
>>> fps = [fpgen.GetSparseCountFingerprint(x) for x in ms]
>>> def distij(i,j,fps=fps):
...   return 1-DataStructs.DiceSimilarity(fps[i],fps[j])
>>> picker = MaxMinPicker()
>>> pickIndices = picker.LazyPick(distij,nfps,10,seed=23)
>>> list(pickIndices)
[93, 109, 154, 6, 95, 135, 151, 61, 137, 139]
```

### Generating Similarity Maps Using Fingerprints

Similarity maps are a way to visualize the atomic contributions to the similarity between a molecule and a reference molecule. The methodology is described in Ref. [17] . They are in the `rdkit.Chem.Draw.SimilarityMaps` module :

Start by creating two molecules:

```pycon
>>> from rdkit import Chem
>>> mol = Chem.MolFromSmiles('COc1cccc2cc(C(=O)NCCCCN3CCN(c4cccc5nccnc54)CC3)oc21')
>>> refmol = Chem.MolFromSmiles('CCCN(CCCCN1CCN(c2ccccc2OC)CC1)Cc1ccc2ccccc2c1')
```

The SimilarityMaps module supports three kind of fingerprints: atom pairs, topological torsions and Morgan fingerprints.

```
>>> from rdkit.Chem import Draw
>>> from rdkit.Chem.Draw import SimilarityMaps
>>> fp = SimilarityMaps.GetAPFingerprint(mol, fpType='normal')
>>> fp = SimilarityMaps.GetTTFingerprint(mol, fpType='normal')
>>> fp = SimilarityMaps.GetMorganFingerprint(mol, fpType='bv')
```

The types of atom pairs and torsions are normal (default), hashed and bit vector (bv). The types of the Morgan fingerprint are bit vector (bv, default) and count vector (count).

The function generating a similarity map for two fingerprints requires the specification of the fingerprint function and optionally the similarity metric. The default for the latter is the Dice similarity. Using all the default arguments of the Morgan fingerprint function, the similarity map can be generated like this:

```
>>> d2d = Draw.MolDraw2DCairo(400, 400)
>>> _, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, mol, SimilarityMaps.GetMorganFingerprint, d2d)
```

Producing this image:

For a different type of Morgan (e.g. count) and radius = 1 instead of 2, as well as a different similarity metric (e.g. Tanimoto), the call becomes:

```
>>> from rdkit import DataStructs
>>> _, maxweight = SimilarityMaps.GetSimilarityMapForFingerprint(refmol, mol, lambda m,idx: SimilarityMaps.GetMorganFingerprint(m, atomId=idx, radius=1, fpType='count'), d2d, metric=DataStructs.TanimotoSimilarity)
```

Producing this image:

The convenience function GetSimilarityMapForFingerprint involves the normalisation of the atomic weights such that the maximum absolute weight is 1. Therefore, the function outputs the maximum weight that was found when creating the map.

```
>>> print(maxweight)
0.05747...
```

If one does not want the normalisation step, the map can be created like:

```
>>> weights = SimilarityMaps.GetAtomicWeightsForFingerprint(refmol, mol, SimilarityMaps.GetMorganFingerprint)
>>> print(["%.2f " % w for w in weights])
['0.05 ', ...
>>> _ = SimilarityMaps.GetSimilarityMapFromWeights(mol, weights, d2d)
```

Producing this image:


## Descriptor Calculation

A variety of descriptors are available within the RDKit. The complete list is provided in List of Available Descriptors.

Most of the descriptors are straightforward to use from Python via the centralized `rdkit.Chem.Descriptors` module :

```pycon
>>> from rdkit.Chem import Descriptors
>>> m = Chem.MolFromSmiles('c1ccccc1C(=O)O')
>>> Descriptors.TPSA(m)
37.3
>>> Descriptors.MolLogP(m)
1.3848
```

### Calculating All Descriptors

The `rdkit.Chem.Descriptors` module provides a convenience function, `CalcMolDescriptors()`, to calculate all available descriptors for a molecule. `CalcMolDescriptors()` returns a dictionary with descriptor names as the keys and descriptor values as the values:

```pycon
>>> vals = Descriptors.CalcMolDescriptors(m)
>>> vals['TPSA']
37.3
>>> vals['NumHDonors']
1
```

`CalcMolDescriptors()` makes it easy to generate descriptors for a set of molecules and get the values into a pandas DataFrame:

> ```
> >>> descrs = [Descriptors.CalcMolDescriptors(mol) for mol in mols]
> >>> df = pandas.DataFrame(descrs)
> >>> df.head()
> >>> df.head(3)
>   MaxEStateIndex  MinEStateIndex  MaxAbsEStateIndex  ...  fr_thiophene  fr_unbrch_alkane  fr_urea
> 0        8.361111       -0.115741           8.361111  ...             0                 0        0
> 1        8.361111       -0.115741           8.361111  ...             0                 0        0
> 2        8.334769        0.329861           8.334769  ...             0                 0        0
> ```
> 
> [3 rows x 208 columns]

### Calculating Partial Charges

Partial charges are handled a bit differently:

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1C(=O)O')
>>> AllChem.ComputeGasteigerCharges(m)
>>> m.GetAtomWithIdx(0).GetDoubleProp('_GasteigerCharge')
-0.047...
```

### Visualization of Descriptors

Similarity maps can be used to visualize descriptors that can be divided into atomic contributions.

The Gasteiger partial charges can be visualized as (using a different color scheme):

```pycon
>>> from rdkit.Chem import Draw
>>> from rdkit.Chem.Draw import SimilarityMaps
>>> mol = Chem.MolFromSmiles('COc1cccc2cc(C(=O)NCCCCN3CCN(c4cccc5nccnc54)CC3)oc21')
>>> AllChem.ComputeGasteigerCharges(mol)
>>> contribs = [mol.GetAtomWithIdx(i).GetDoubleProp('_GasteigerCharge') for i in range(mol.GetNumAtoms())]
>>> d2d = Draw.MolDraw2DCairo(400, 400)
>>> _ = SimilarityMaps.GetSimilarityMapFromWeights(mol, contribs, d2d, colorMap='jet', contourLines=10)
```

Producing this image:

Or for the Crippen contributions to logP:

```pycon
>>> from rdkit.Chem import rdMolDescriptors
>>> contribs = rdMolDescriptors._CalcCrippenContribs(mol)
>>> _ = SimilarityMaps.GetSimilarityMapFromWeights(mol,[x for x,y in contribs], d2d, colorMap='jet', contourLines=10)
```

Producing this image:


## Chemical Reactions

The RDKit also supports applying chemical reactions to sets of molecules. One way of constructing chemical reactions is to use a SMARTS-based language similar to Daylight’s Reaction SMILES [11]:

```pycon
>>> rxn = AllChem.ReactionFromSmarts('[C:1](=[O:2])-[OD1].[N!H0:3]>>[C:1](=[O:2])[N:3]')
>>> rxn
<rdkit.Chem.rdChemReactions.ChemicalReaction object at 0x...>
>>> rxn.GetNumProductTemplates()
1
>>> ps = rxn.RunReactants((Chem.MolFromSmiles('CC(=O)O'),Chem.MolFromSmiles('NC')))
>>> len(ps) # one entry for each possible set of products
1
>>> len(ps[0]) # each entry contains one molecule for each product
1
>>> Chem.MolToSmiles(ps[0][0])
'CNC(C)=O'
>>> ps = rxn.RunReactants((Chem.MolFromSmiles('C(COC(=O)O)C(=O)O'),Chem.MolFromSmiles('NC')))
>>> len(ps)
2
>>> Chem.MolToSmiles(ps[0][0])
'CNC(=O)OCCC(=O)O'
>>> Chem.MolToSmiles(ps[1][0])
'CNC(=O)CCOC(=O)O'
```

Reactions can also be built from MDL rxn files:

```pycon
>>> rxn = AllChem.ReactionFromRxnFile('data/AmideBond.rxn')
>>> rxn.GetNumReactantTemplates()
2
>>> rxn.GetNumProductTemplates()
1
>>> ps = rxn.RunReactants((Chem.MolFromSmiles('CC(=O)O'), Chem.MolFromSmiles('NC')))
>>> len(ps)
1
>>> Chem.MolToSmiles(ps[0][0])
'CNC(C)=O'
```

It is, of course, possible to do reactions more complex than amide bond formation:

```pycon
>>> rxn = AllChem.ReactionFromSmarts('[C:1]=[C:2].[C:3]=[*:4][*:5]=[C:6]>>[C:1]1[C:2][C:3][*:4]=[*:5][C:6]1')
>>> ps = rxn.RunReactants((Chem.MolFromSmiles('OC=C'), Chem.MolFromSmiles('C=CC(N)=C')))
>>> Chem.MolToSmiles(ps[0][0])
'NC1=CCCC(O)C1'
```

Note in this case that there are multiple mappings of the reactants onto the templates, so we have multiple product sets:

```pycon
>>> len(ps)
4
```

You can use canonical smiles and a python dictionary to get the unique products:

```pycon
>>> uniqps = {}
>>> for p in ps:
...   smi = Chem.MolToSmiles(p[0])
...   uniqps[smi] = p[0]
...
>>> sorted(uniqps.keys())
['NC1=CCC(O)CC1', 'NC1=CCCC(O)C1']
```

Note that the molecules that are produced by the chemical reaction processing code are not sanitized, as this artificial reaction demonstrates:

```pycon
>>> rxn = AllChem.ReactionFromSmarts('[C:1]=[C:2][C:3]=[C:4].[C:5]=[C:6]>>[C:1]1=[C:2][C:3]=[C:4][C:5]=[C:6]1')
>>> ps = rxn.RunReactants((Chem.MolFromSmiles('C=CC=C'), Chem.MolFromSmiles('C=C')))
>>> Chem.MolToSmiles(ps[0][0])
'C1=CC=CC=C1'
>>> p0 = ps[0][0]
>>> Chem.SanitizeMol(p0)
rdkit.Chem.rdmolops.SanitizeFlags.SANITIZE_NONE
>>> Chem.MolToSmiles(p0)
'c1ccccc1'
```

### Drawing Chemical Reactions

The RDKit’s MolDraw2D-based rendering can also handle chemical reactions.

```pycon
>>> from rdkit.Chem import Draw
>>> rxn = AllChem.ReactionFromSmarts('[cH:5]1[cH:6][c:7]2[cH:8][n:9][cH:10][cH:11][c:12]2[c:3]([cH:4]1)[C:2](=[O:1])O.[N-:13]=[N+:14]=[N-:15]>C(Cl)Cl.C(=O)(C(=O)Cl)Cl>[cH:5]1[cH:6][c:7]2[cH:8][n:9][cH:10][cH:11][c:12]2[c:3]([cH:4]1)[C:2](=[O:1])[N:13]=[N+:14]=[N-:15]',useSmiles=True)
>>> d2d = Draw.MolDraw2DCairo(800,300)
>>> d2d.DrawReaction(rxn)
>>> png = d2d.GetDrawingText()
>>> open('./images/reaction1.o.png','wb+').write(png)
```

the result looks like this:

There’s another drawing mode which leaves out the atom map information but which highlights which of the reactants atoms in the products come from:

```pycon
>>> d2d = Draw.MolDraw2DCairo(800,300)
>>> d2d.DrawReaction(rxn,highlightByReactant=True)
>>> png = d2d.GetDrawingText()
>>> open('./images/reaction1_highlight.o.png','wb+').write(png)
```

As of the 2020.09 release, PNG images of reactions include metadata allowing the reaction to be reconstructed:

```pycon
>>> newRxn = AllChem.ReactionFromPNGString(png)
>>> AllChem.ReactionToSmarts(newRxn)
'[#6:5]1:[#6:6]:[#6:7]2:[#6:8]:[#7:9]:[#6:10]:[#6:11]:[#6:12]:2:[#6:3](:[#6:4]:1)-[#6:2](=[#8:1])-[#8].[#7-:13]=[#7+:14]=[#7-:15]>[#6](-[#17])-[#17].[#6](=[#8])(-[#6](=[#8])-[#17])-[#17]>[#6:5]1:[#6:6]:[#6:7]2:[#6:8]:[#7:9]:[#6:10]:[#6:11]:[#6:12]:2:[#6:3](:[#6:4]:1)-[#6:2](=[#8:1])-[#7:13]=[#7+:14]=[#7-:15]'
```

### Advanced Reaction Functionality

#### Protecting Atoms

Sometimes, particularly when working with rxn files, it is difficult to express a reaction exactly enough to not end up with extraneous products. The RDKit provides a method of “protecting” atoms to disallow them from taking part in reactions.

This can be demonstrated re-using the amide-bond formation reaction used above. The query for amines isn’t specific enough, so it matches any nitrogen that has at least one H attached. So if we apply the reaction to a molecule that already has an amide bond, the amide N is also treated as a reaction site:

```pycon
>>> rxn = AllChem.ReactionFromRxnFile('data/AmideBond.rxn')
>>> acid = Chem.MolFromSmiles('CC(=O)O')
>>> base = Chem.MolFromSmiles('CC(=O)NCCN')
>>> ps = rxn.RunReactants((acid,base))
>>> len(ps)
2
>>> Chem.MolToSmiles(ps[0][0])
'CC(=O)N(CCN)C(C)=O'
>>> Chem.MolToSmiles(ps[1][0])
'CC(=O)NCCNC(C)=O'
```

The first product corresponds to the reaction at the amide N.

We can prevent this from happening by protecting all amide Ns. Here we do it with a substructure query that matches amides and thioamides and then set the “_protected” property on matching atoms:

```pycon
>>> amidep = Chem.MolFromSmarts('[N;$(NC=[O,S])]')
>>> for match in base.GetSubstructMatches(amidep):
...     base.GetAtomWithIdx(match[0]).SetProp('_protected','1')
```

Now the reaction only generates a single product:

```pycon
>>> ps = rxn.RunReactants((acid,base))
>>> len(ps)
1
>>> Chem.MolToSmiles(ps[0][0])
'CC(=O)NCCNC(C)=O'
```

### Recap Implementation

Associated with the chemical reaction functionality is an implementation of the Recap algorithm. [8] Recap uses a set of chemical transformations mimicking common reactions carried out in the lab in order to decompose a molecule into a series of reasonable fragments.

The RDKit `rdkit.Chem.Recap` implementation keeps track of the hierarchy of transformations that were applied:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import Recap
>>> m = Chem.MolFromSmiles('c1ccccc1OCCOC(=O)CC')
>>> hierarch = Recap.RecapDecompose(m)
>>> type(hierarch)
<class 'rdkit.Chem.Recap.RecapHierarchyNode'>
```

The hierarchy is rooted at the original molecule:

```pycon
>>> hierarch.smiles
'CCC(=O)OCCOc1ccccc1'
```

and each node tracks its children using a dictionary keyed by SMILES:

```pycon
>>> ks=hierarch.children.keys()
>>> sorted(ks)
['*C(=O)CC', '*CCOC(=O)CC', '*CCOc1ccccc1', '*OCCOc1ccccc1', '*c1ccccc1']
```

The nodes at the bottom of the hierarchy (the leaf nodes) are easily accessible, also as a dictionary keyed by SMILES:

```pycon
>>> ks=hierarch.GetLeaves().keys()
>>> ks=sorted(ks)
>>> ks
['*C(=O)CC', '*CCO*', '*CCOc1ccccc1', '*c1ccccc1']
```

Notice that dummy atoms are used to mark points where the molecule was fragmented.

The nodes themselves have associated molecules:

```pycon
>>> leaf = hierarch.GetLeaves()[ks[0]]
>>> Chem.MolToSmiles(leaf.mol)
'*C(=O)CC'
```

### BRICS Implementation

The RDKit also provides an implementation of the BRICS algorithm. [9] BRICS provides another method for fragmenting molecules along synthetically accessible bonds:

```pycon
>>> from rdkit.Chem import BRICS
>>> with Chem.SDMolSupplier('data/cdk2.sdf') as cdk2mols:
...   m1 = cdk2mols[0]
...   m2 = cdk2mols[20]
>>> sorted(BRICS.BRICSDecompose(m1))
['[14*]c1nc(N)nc2[nH]cnc12', '[3*]O[3*]', '[4*]CC(=O)C(C)C']
>>> sorted(BRICS.BRICSDecompose(m2))
['[1*]C(=O)NN(C)C', '[14*]c1[nH]nc2c1C(=O)c1c([16*])cccc1-2', '[16*]c1ccc([16*])cc1', '[3*]OC', '[5*]N[5*]']
```

Notice that RDKit BRICS implementation returns the unique fragments generated from a molecule and that the dummy atoms are tagged to indicate which type of reaction applies.

It’s quite easy to generate the list of all fragments for a group of molecules:

```pycon
>>> allfrags=set()
>>> with Chem.SDMolSupplier('data/cdk2.sdf') as cdk2mols:
...   for m in cdk2mols:
...      if m is None:
...        continue
...      pieces = BRICS.BRICSDecompose(m)
...      allfrags.update(pieces)
>>> len(allfrags)
90
>>> sorted(allfrags)[:5]
['NS(=O)(=O)c1ccc(N/N=C2\\C(=O)Nc3ccc(Br)cc32)cc1', '[1*]C(=O)C(C)C', '[1*]C(=O)NN(C)C', '[1*]C(=O)NN1CC[NH+](C)CC1', '[1*]C(C)=O']
```

The BRICS module also provides an option to apply the BRICS rules to a set of fragments to create new molecules:

```pycon
>>> import random
>>> random.seed(127)
>>> fragms = [Chem.MolFromSmiles(x) for x in sorted(allfrags)]
>>> random.seed(0xf00d)
>>> ms = BRICS.BRICSBuild(fragms)
```

The result is a generator object:

```pycon
>>> ms
<generator object BRICSBuild at 0x...>
```

That returns molecules on request:

```pycon
>>> prods = [next(ms) for x in range(10)]
>>> prods[0]
<rdkit.Chem.rdchem.Mol object at 0x...>
```

The molecules have not been sanitized, so it’s a good idea to at least update the valences before continuing:

```pycon
>>> for prod in prods:
...     prod.UpdatePropertyCache(strict=False)
...
>>> Chem.MolToSmiles(prods[0],True)
'[H]/N=C(\\N)NC(=O)C(C)C'
>>> Chem.MolToSmiles(prods[1],True)
'CC(C)C(=O)N/C=C1\\C(=O)Nc2ccc3ncsc3c21'
>>> Chem.MolToSmiles(prods[2],True)
'CC(C)C(=O)N/C=C1\\C(=O)Nc2ccccc21'
>>> Chem.MolToSmiles(prods[3],True)
'CNC(=O)C(C)C'
```

By default those results come back in a random order (technically the example above will always return the same results since we seeded Python’s random number generator just before calling BRICSBuild()). If you want the results to be returned in a consistent order use the scrambleReagents argument:

```
>>> ms = BRICS.BRICSBuild(fragms, scrambleReagents=False)
>>> prods = [next(ms) for x in range(10)]
>>> for prod in prods:
...     prod.UpdatePropertyCache(strict=False)
...
>>> Chem.MolToSmiles(prods[0],True)
'COC(=O)C(C)C'
>>> Chem.MolToSmiles(prods[1],True)
'CNC(=O)C(C)C'
>>> Chem.MolToSmiles(prods[2],True)
'CC(C)C(=O)NC(=N)N'
```

### Other fragmentation approaches

In addition to the methods described above, the RDKit provide a very flexible generic function for fragmenting molecules along user-specified bonds.

Here’s a quick demonstration of using that to break all bonds between atoms in rings and atoms not in rings. We start by finding all the atom pairs:

```pycon
>>> m = Chem.MolFromSmiles('CC1CC(O)C1CCC1CC1')
>>> bis = m.GetSubstructMatches(Chem.MolFromSmarts('[!R][R]'))
>>> bis
((0, 1), (4, 3), (6, 5), (7, 8))
```

then we get the corresponding bond indices:

```pycon
>>> bs = [m.GetBondBetweenAtoms(x,y).GetIdx() for x,y in bis]
>>> bs
[0, 3, 5, 7]
```

then we use those bond indices as input to the fragmentation function:

```pycon
>>> nm = Chem.FragmentOnBonds(m,bs)
```

the output is a molecule that has dummy atoms marking the places where bonds were broken:

```pycon
>>> Chem.MolToSmiles(nm,True)
'*C1CC([4*])C1[6*].[1*]C.[3*]O.[5*]CC[8*].[7*]C1CC1'
```

By default the attachment points are labelled (using isotopes) with the index of the atom that was removed. We can also provide our own set of atom labels in the form of pairs of unsigned integers. The first value in each pair is used as the label for the dummy that replaces the bond’s begin atom, the second value in each pair is for the dummy that replaces the bond’s end atom. Here’s an example, repeating the analysis above and marking the positions where the non-ring atoms were with the label 10 and marking the positions where the ring atoms were with label 1:

```pycon
>>> bis = m.GetSubstructMatches(Chem.MolFromSmarts('[!R][R]'))
>>> bs = []
>>> labels=[]
>>> for bi in bis:
...    b = m.GetBondBetweenAtoms(bi[0],bi[1])
...    if b.GetBeginAtomIdx()==bi[0]:
...        labels.append((10,1))
...    else:
...        labels.append((1,10))
...    bs.append(b.GetIdx())
>>> nm = Chem.FragmentOnBonds(m,bs,dummyLabels=labels)
>>> Chem.MolToSmiles(nm,True)
'[1*]C.[1*]CC[1*].[1*]O.[10*]C1CC([10*])C1[10*].[10*]C1CC1'
```
