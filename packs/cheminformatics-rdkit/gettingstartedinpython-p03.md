---
title: "Getting Started with the RDKit in Python (part 3/3)"
source: https://www.rdkit.org/docs/GettingStartedInPython.html
domain: cheminformatics-rdkit
license: CC-BY-SA-4.0
tags: cheminformatics rdkit, molecular descriptor, smiles notation, chemical fingerprint
fetched: 2026-07-02
part: 3/3
---

## Chemical Features and Pharmacophores

### Chemical Features

Chemical features in the RDKit are defined using a SMARTS-based feature definition language (described in detail in the RDKit book). To identify chemical features in molecules, you first must build a feature factory:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import ChemicalFeatures
>>> from rdkit import RDConfig
>>> import os
>>> fdefName = os.path.join(RDConfig.RDDataDir,'BaseFeatures.fdef')
>>> factory = ChemicalFeatures.BuildFeatureFactory(fdefName)
```

and then use the factory to search for features:

```pycon
>>> m = Chem.MolFromSmiles('OCc1ccccc1CN')
>>> feats = factory.GetFeaturesForMol(m)
>>> len(feats)
8
```

The individual features carry information about their family (e.g. donor, acceptor, etc.), type (a more detailed description), and the atom(s) that is/are associated with the feature:

```pycon
>>> feats[0].GetFamily()
'Donor'
>>> feats[0].GetType()
'SingleAtomDonor'
>>> feats[0].GetAtomIds()
(0,)
>>> feats[4].GetFamily()
'Aromatic'
>>> feats[4].GetAtomIds()
(2, 3, 4, 5, 6, 7)
```

If the molecule has coordinates, then the features will also have reasonable locations:

```pycon
>>> from rdkit.Chem import AllChem
>>> AllChem.Compute2DCoords(m)
0
>>> feats[0].GetPos()
<rdkit.Geometry.rdGeometry.Point3D object at 0x...>
>>> list(feats[0].GetPos())
[-2.999..., -1.558..., 0.0]
```

### 2D Pharmacophore Fingerprints

Combining a set of chemical features with the 2D (topological) distances between them gives a 2D pharmacophore. When the distances are binned, unique integer ids can be assigned to each of these pharmacophores and they can be stored in a fingerprint. Details of the encoding are in the The RDKit Book.

Generating pharmacophore fingerprints requires chemical features generated via the usual RDKit feature-typing mechanism:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import ChemicalFeatures
>>> fdefName = 'data/MinimalFeatures.fdef'
>>> featFactory = ChemicalFeatures.BuildFeatureFactory(fdefName)
```

The fingerprints themselves are calculated using a signature (fingerprint) factory, which keeps track of all the parameters required to generate the pharmacophore:

```pycon
>>> from rdkit.Chem.Pharm2D.SigFactory import SigFactory
>>> sigFactory = SigFactory(featFactory,minPointCount=2,maxPointCount=3)
>>> sigFactory.SetBins([(0,2),(2,5),(5,8)])
>>> sigFactory.Init()
>>> sigFactory.GetSigSize()
885
```

The signature factory is now ready to be used to generate fingerprints, a task which is done using the `rdkit.Chem.Pharm2D.Generate` module:

```pycon
>>> from rdkit.Chem.Pharm2D import Generate
>>> mol = Chem.MolFromSmiles('OCC(=O)CCCN')
>>> fp = Generate.Gen2DFingerprint(mol,sigFactory)
>>> fp
<rdkit.DataStructs.cDataStructs.SparseBitVect object at 0x...>
>>> len(fp)
885
>>> fp.GetNumOnBits()
57
```

Details about the bits themselves, including the features that are involved and the binned distance matrix between the features, can be obtained from the signature factory:

```pycon
>>> list(fp.GetOnBits())[:5]
[1, 2, 6, 7, 8]
>>> sigFactory.GetBitDescription(1)
'Acceptor Acceptor |0 1|1 0|'
>>> sigFactory.GetBitDescription(2)
'Acceptor Acceptor |0 2|2 0|'
>>> sigFactory.GetBitDescription(8)
'Acceptor Donor |0 2|2 0|'
>>> list(fp.GetOnBits())[-5:]
[704, 706, 707, 708, 714]
>>> sigFactory.GetBitDescription(707)
'Donor Donor PosIonizable |0 1 2|1 0 1|2 1 0|'
>>> sigFactory.GetBitDescription(714)
'Donor Donor PosIonizable |0 2 2|2 0 0|2 0 0|'
```

For the sake of convenience (to save you from having to edit the fdef file every time) it is possible to disable particular feature types within the SigFactory:

```pycon
>>> sigFactory.skipFeats=['PosIonizable']
>>> sigFactory.Init()
>>> sigFactory.GetSigSize()
510
>>> fp2 = Generate.Gen2DFingerprint(mol,sigFactory)
>>> fp2.GetNumOnBits()
36
```

Another possible set of feature definitions for 2D pharmacophore fingerprints in the RDKit are those published by Gobbi and Poppinger. [10] The module `rdkit.Chem.Pharm2D.Gobbi_Pharm2D` has a pre-configured signature factory for these fingerprint types. Here’s an example of using it:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem.Pharm2D import Gobbi_Pharm2D,Generate
>>> m = Chem.MolFromSmiles('OCC=CC(=O)O')
>>> fp = Generate.Gen2DFingerprint(m,Gobbi_Pharm2D.factory)
>>> fp
<rdkit.DataStructs.cDataStructs.SparseBitVect object at 0x...>
>>> fp.GetNumOnBits()
8
>>> list(fp.GetOnBits())
[23, 30, 150, 154, 157, 185, 28878, 30184]
>>> Gobbi_Pharm2D.factory.GetBitDescription(157)
'HA HD |0 3|3 0|'
>>> Gobbi_Pharm2D.factory.GetBitDescription(30184)
'HA HD HD |0 3 0|3 0 3|0 3 0|'
```


## Molecular Fragments

The RDKit contains a collection of tools for fragmenting molecules and working with those fragments. Fragments are defined to be made up of a set of connected atoms that may have associated functional groups. This is more easily demonstrated than explained:

```pycon
>>> fName=os.path.join(RDConfig.RDDataDir,'FunctionalGroups.txt')
>>> from rdkit.Chem import FragmentCatalog
>>> fparams = FragmentCatalog.FragCatParams(1,6,fName)
>>> fparams.GetNumFuncGroups()
39
>>> fcat=FragmentCatalog.FragCatalog(fparams)
>>> fcgen=FragmentCatalog.FragCatGenerator()
>>> m = Chem.MolFromSmiles('OCC=CC(=O)O')
>>> fcgen.AddFragsFromMol(m,fcat)
3
>>> fcat.GetEntryDescription(0)
'C<-O>C'
>>> fcat.GetEntryDescription(1)
'C=C<-C(=O)O>'
>>> fcat.GetEntryDescription(2)
'C<-C(=O)O>=CC<-O>'
```

The fragments are stored as entries in a `rdkit.Chem.rdfragcatalog.FragCatalog`. Notice that the entry descriptions include pieces in angular brackets (e.g. between ‘<’ and ‘>’). These describe the functional groups attached to the fragment. For example, in the above example, the catalog entry 0 corresponds to an ethyl fragment with an alcohol attached to one of the carbons and entry 1 is an ethylene with a carboxylic acid on one carbon. Detailed information about the functional groups can be obtained by asking the fragment for the ids of the functional groups it contains and then looking those ids up in the `rdkit.Chem.rdfragcatalog.FragCatParams` object:

```pycon
>>> list(fcat.GetEntryFuncGroupIds(2))
[34, 1]
>>> fparams.GetFuncGroup(1)
<rdkit.Chem.rdchem.Mol object at 0x...>
>>> Chem.MolToSmarts(fparams.GetFuncGroup(1))
'*-C(=O)[O&D1]'
>>> Chem.MolToSmarts(fparams.GetFuncGroup(34))
'*-[O&D1]'
>>> fparams.GetFuncGroup(1).GetProp('_Name')
'-C(=O)O'
>>> fparams.GetFuncGroup(34).GetProp('_Name')
'-O'
```

The catalog is hierarchical: smaller fragments are combined to form larger ones. From a small fragment, one can find the larger fragments to which it contributes using the `rdkit.Chem.rdfragcatalog.FragCatalog.GetEntryDownIds()` method:

```pycon
>>> fcat=FragmentCatalog.FragCatalog(fparams)
>>> m = Chem.MolFromSmiles('OCC(NC1CC1)CCC')
>>> fcgen.AddFragsFromMol(m,fcat)
15
>>> fcat.GetEntryDescription(0)
'C<-O>C'
>>> fcat.GetEntryDescription(1)
'CN<-cPropyl>'
>>> list(fcat.GetEntryDownIds(0))
[3, 4]
>>> fcat.GetEntryDescription(3)
'C<-O>CC'
>>> fcat.GetEntryDescription(4)
'C<-O>CN<-cPropyl>'
```

The fragments from multiple molecules can be added to a catalog:

```pycon
>>> with Chem.SmilesMolSupplier('data/bzr.smi') as suppl:
...    ms = [x for x in suppl]
>>> fcat=FragmentCatalog.FragCatalog(fparams)
>>> for m in ms: nAdded=fcgen.AddFragsFromMol(m,fcat)
>>> fcat.GetNumEntries()
1169
>>> fcat.GetEntryDescription(0)
'Cc'
>>> fcat.GetEntryDescription(100)
'cc-nc(C)n'
```

The fragments in a catalog are unique, so adding a molecule a second time doesn’t add any new entries:

```pycon
>>> fcgen.AddFragsFromMol(ms[0],fcat)
0
>>> fcat.GetNumEntries()
1169
```

Once a `rdkit.Chem.rdfragcatalog.FragCatalog` has been generated, it can be used to fingerprint molecules:

```pycon
>>> fpgen = FragmentCatalog.FragFPGenerator()
>>> fp = fpgen.GetFPForMol(ms[8],fcat)
>>> fp
<rdkit.DataStructs.cDataStructs.ExplicitBitVect object at 0x...>
>>> fp.GetNumOnBits()
189
```

The rest of the machinery associated with fingerprints can now be applied to these fragment fingerprints. For example, it’s easy to find the fragments that two molecules have in common by taking the intersection of their fingerprints:

```pycon
>>> fp2 = fpgen.GetFPForMol(ms[7],fcat)
>>> andfp = fp&fp2
>>> obl = list(andfp.GetOnBits())
>>> fcat.GetEntryDescription(obl[-1])
'ccc(cc)NC<=O>'
>>> fcat.GetEntryDescription(obl[-5])
'c<-X>ccc(N)cc'
```

or we can find the fragments that distinguish one molecule from another:

```pycon
>>> combinedFp=fp&(fp^fp2) # can be more efficient than fp&(!fp2)
>>> obl = list(combinedFp.GetOnBits())
>>> fcat.GetEntryDescription(obl[-1])
'cccc(N)cc'
```

Or we can use the bit ranking functionality from the `rdkit.ML.InfoTheory.rdInfoTheory.InfoBitRanker` class to identify fragments that distinguish actives from inactives:

```pycon
>>> with Chem.SDMolSupplier('data/bzr.sdf') as suppl:
...    sdms = [x for x in suppl]
>>> fps = [fpgen.GetFPForMol(x,fcat) for x in sdms]
>>> from rdkit.ML.InfoTheory import InfoBitRanker
>>> ranker = InfoBitRanker(len(fps[0]),2)
>>> acts = [x.GetDoubleProp('ACTIVITY') for x in sdms]
>>> for i,fp in enumerate(fps):
...   act = int(acts[i]>7)
...   ranker.AccumulateVotes(fp,act)
...
>>> top5 = ranker.GetTopN(5)
>>> for id,gain,n0,n1 in top5:
...   print(int(id),'%.3f'%gain,int(n0),int(n1))
...
702 0.081 20 17
328 0.073 23 25
341 0.073 30 43
173 0.073 30 43
1034 0.069 5 53
```

The columns above are: bitId, infoGain, nInactive, nActive. Note that this approach isn’t particularly effective for this artificial example.


## R-Group Decomposition

Let’s look at how it works. We’ll read in a group of molecules (these were taken ChEMBL), define a core with labelled R groups, and then use the simplest call to do R-group decomposition: `rdkit.Chem.rdRGroupDecomposition.RGroupDecompose()`

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import rdRGroupDecomposition as rdRGD
>>> with Chem.SmilesMolSupplier('data/s1p_chembldoc89753.txt',delimiter=",",
...                              smilesColumn=9,nameColumn=10) as suppl:
...   ms = [x for x in suppl if x is not None]
>>> len(ms)
40
>>> core = Chem.MolFromSmarts('[*:1]c1nc([*:2])on1')
>>> res,unmatched = rdRGD.RGroupDecompose([core],ms,asSmiles=True)
>>> unmatched
[]
>>> len(res)
40
>>> res[:2]
[{'Core': 'n1oc([*:2])nc1[*:1]', 'R1': 'O=C(O)CCCC1NCCOc2c1cccc2[*:1]', 'R2': 'CC(C)Oc1ccc([*:2])cc1Cl'},
 {'Core': 'n1oc([*:2])nc1[*:1]', 'R1': 'O=C(O)CCC1NCCOc2c1cccc2[*:1]', 'R2': 'CC(C)Oc1ccc([*:2])cc1Cl'}]
```

The *unmatched* return value has the indices of the molecules that did not match a core; in this case there are none. The other result is a list with one dict for each molecule; each dict contains the core that matched the molecule (in this case there was only one) and the molecule’s R groups.

As an aside, if you are a Pandas user, it’s very easy to get the R-group decomposition results into a DataFrame:

```pycon
>>> import pandas as pd
>>> res,unmatched = rdRGD.RGroupDecompose([core],ms,asSmiles=True,asRows=False)
>>> df= pd.DataFrame(res)
>>> df.head()
                  Core                              R1                       R2
0  n1oc([*:2])nc1[*:1]   O=C(O)CCCC1NCCOc2c1cccc2[*:1]  CC(C)Oc1ccc([*:2])cc1Cl
1  n1oc([*:2])nc1[*:1]    O=C(O)CCC1NCCOc2c1cccc2[*:1]  CC(C)Oc1ccc([*:2])cc1Cl
2  n1oc([*:2])nc1[*:1]  O=C(O)CCC1COc2ccc([*:1])cc2CN1  CC(C)Oc1ccc([*:2])cc1Cl
3  n1oc([*:2])nc1[*:1]   O=C(O)CCCC1NCCOc2c1cccc2[*:1]  CC(C)Oc1ncc([*:2])cc1Cl
4  n1oc([*:2])nc1[*:1]   O=C(O)CCCC1NCCOc2c1cccc2[*:1]  CC(C)Oc1ncc([*:2])cc1Cl
```

It’s not necessary to label the attachment points on the core, if you leave them out the code will automatically assign labels:

```pycon
>>> core2 = Chem.MolFromSmarts('c1ncon1')
>>> res,unmatched = rdRGD.RGroupDecompose([core2],ms,asSmiles=True)
>>> res[:2]
[{'Core': 'n1oc([*:1])nc1[*:2]', 'R1': 'CC(C)Oc1ccc([*:1])cc1Cl', 'R2': 'O=C(O)CCCC1NCCOc2c1cccc2[*:2]'},
 {'Core': 'n1oc([*:1])nc1[*:2]', 'R1': 'CC(C)Oc1ccc([*:1])cc1Cl', 'R2': 'O=C(O)CCC1NCCOc2c1cccc2[*:2]'}]
```

R-group decomposition is actually pretty complex, so there’s a lot more there. Hopefully this is enough to get you started.


## Searching Synthon Spaces

A number of companies, notably Enamine and ChemSpace, provide very large libraries of compounds in synthon form. Enumerating and searching them is infeasible due to their enormous sizes, on the order of 10s of billions of compounds. They can, however, be searched efficiently in synthon form. Currently the RDKit can be used to query these libraries by substructure (returning those products that match a SMARTS string or MOL query) or fingerprint Tanimoto similarity (returning products which match a query molecule within a given Tanimoto similarity) using any of the available fingerprint generators.

### How It Works

The synthon space is provided in a format similar to:

```
SMILES      synton_id       synton# reaction_id
c1ccccc1C(=O)[1*]   1-1     0       amide-1
C1CCCCC1C(=O)[1*]   1-2     0       amide-1
Clc1ccccc1C(=O)[1*] 1-3     0       amide-1
CCCCC(=O)[1*]       1-4     0       amide-1
[1*]N1CCCC1         2-1     1       amide-1
[1*]NCCCCC          2-2     1       amide-1
[1*]NCC1CC1         2-3     1       amide-1
```

which describes a library of amides built from 2 synthons. There are 4 examples for the first synthon and 3 for the second, giving a total of 12 products. Each product is formed by taking a synthon from the first set and another from the second and combining them by removing the attachment atoms ([1*] in this case), and adding a bond between the atoms the attachment atoms were bonded to. Both Enamine and ChemSpace use transuranic elements (uranium, neptunium, plutonium and americium) as the attachment atoms. Libraries with up to 4 synthons per product are supported.

In order to perform the search, the query molecule is fragmented by cutting all combinations of bonds that give rise to a maximum number of fragments. The maximum is the largest number of synthon sets in any reaction in the space, and will most likely be between 2 and 4. There is not a maximum on the number of bonds used in the cutting, because 2 non-ring bonds will give rise to 3 fragments, but 4 ring bonds may also do so, 2 splitting one ring and the other 2 a different ring in the query. This produces a large number of fragment sets, where each set is produced by cutting one particular combination of bonds. Each fragment in the set is compared with synthons in one column of the synthons for each reaction thus identifying combinations of synthons that might match the query. These combinations are enumerated and a final comparison with the query performed to select the hit set. The algorithm is largely similar to that described by Liphardt and Sander.

### Database Preparation

The databases are normally supplied in text form, and can be used as such:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import rdSynthonSpaceSearch, rdFingerprintGenerator
>>> import os
>>> RDBASE = os.environ["RDBASE"]
>>> synthonspace = rdSynthonSpaceSearch.SynthonSpace()
>>> textFile = f"{RDBASE}/Code/GraphMol/SynthonSpaceSearch/data/amide_space.txt"
>>> synthonspace.ReadTextFile(textFile)
>>> print(f"Number of reactions : {synthonspace.GetNumReactions()}")
Number of reactions : 1
>>> print(f"Number of products : {synthonspace.GetNumProducts()}")
Number of products : 12
```

However, a large amount of pre-processing is required before the data are searchable which can be time consuming. For example, preparing the current REAL database (2024-09) of 70 billion compounds can take several hours. It is therefore strongly recommended that a binary database is created before use.

The fingerprints are written to the DB file, which means that the file must be searched using exactly the same type in order to get meaningful results. This will be checked at runtime. You may need to keep several versions of the database, labelled accordingly.

```pycon
>>> fpgen = rdFingerprintGenerator.GetRDKitFPGenerator(fpSize=2048)
>>> synthonspace.BuildSynthonFingerprints(fpgen)
>>> dbFile = "amide_library_rdkit.spc"
>>> synthonspace.WriteDBFile(dbFile)
```

There is also a convenience function for performing the conversion in one go:

```pycon
>>> fpgen = rdFingerprintGenerator.GetMorganGenerator(fpSize=2048)
>>> rdSynthonSpaceSearch.ConvertTextToDBFile(textFile, dbFile, fpgen)
```

although under the hood it does exactly the same steps.

The binary database is read using the appropriate function:

```pycon
>>> synthonspace.ReadDBFile(f"{RDBASE}/Code/GraphMol/SynthonSpaceSearch/data/idorsia_toy_space_a.spc")
```

### Memory Usage

The 2024-09 REAL database requires about 10GB of RAM, FreedomSpace 2024-09 about 3.5GB. They should both therefore be searchable on an average laptop.

### Substructure Searching

Any query molecule can be used for substructure searching. The full set of query features supported by the RDKit is allowed. However, queries that use recursive SMARTS or other more complicated features may be noticeably slower. Results are returned in a *rdSynthonSpaceSearch.SearchResults* object.

```pycon
>>> spc = rdSynthonSpaceSearch.SynthonSpace()
>>> spc.ReadDBFile(f"{RDBASE}/Code/GraphMol/SynthonSpaceSearch/data/idorsia_toy_space_a.spc")
>>> qmol = Chem.MolFromSmarts("s1cccc1C(=O)Cn1nn(c(-c)c1)")
>>> results = spc.SubstructureSearch(qmol)
>>> print(f"Number of hits : {len(results.GetHitMolecules())}")
Number of hits : 50
```

Substructure searches should take no more than a few seconds on a machine with average performance, although this will depend on the generality and complexity of the query and the number of hits returned.

The search can be given an optional parameters object that can control various aspects of the search:

```pycon
>>> params = rdSynthonSpaceSearch.SynthonSpaceSearchParams()
>>> params.maxHits = 10
>>> params.timeOut = 10
>>> results = spc.SubstructureSearch(qmol, params=params)
>>> print(f"Number of hits : {len(results.GetHitMolecules())}")
Number of hits : 10
```

The timeout is specified in seconds; if the given time is exceeded all results found thus far will be returned. The method *results.GetTimedOut()* will report whether or not that has occurred. The *maxHits* parameter defaults to 1000. If set to -1, all hits will be returned. It can happen that having looked at the first 1000 hits, you may wish to examine the following 1000 in the hit list. The parameter *hitStart* allows this.

As well as returning the first hits, the parameter *randomSample*, if set True, will return a random sampling of the possible hits.

### Similarity Searching

The synthon space can also be searched by fingerprint similarity. The fingerprint generator used to make the query fingerprints must be exactly the same as that used to create the DB file. The SynthonSpace can report the infoString of the fingerprint generator it was used with, which will help if there is a mismatch. At present there is no way of using the infoString directly to create a fingerprint generator, so it must be examined visually.

```pycon
>>> print(spc.GetSynthonFingerprintType())
Common arguments : countSimulation=0 fpSize=2048 bitsPerFeature=2 includeChirality=0 --- RDKitFPArguments minPath=1 maxPath=7 useHs=1 branchedPaths=1 useBondOrder=1 --- RDKitFPEnvGenerator --- RDKitFPAtomInvGenerator --- No bond invariants generator
```

The similarity metric is hard-coded to use the Tanimoto coefficient. The default similarity cutoff for the search is 0.5, which is a reasonable starting value for a Morgan fingerprint of radius 2. Note that in the similarity search, you will get the first *maxHits* hits that pass the threshold, not necessarily the best hits. The search attempts to bring the most similar matches towards the start of the hit list by ordering the synthons that match a fragment in descending order of similarity, but this does not always bring the most similar products to the fore.

Once the search has assembled a set of likely synthon combinations that might match the query by similarity, a two stage screen is used. The fingerprints of the synthons are added together and the Tanimoto similarity to the query fingerprint calculated. If this is above the threshold then the hit molecule is made, a fingerprint generated and that compared with the query fingerprint. If that similarity passes the threshold, the hit is accepted. The first, approximate, comparison may cause genuine hits to be missed, so there is a parameter *approxSimilarityAdjuster* that lowers the threshold for the first test. It defaults to 0.1. The higher the value the fewer hits will be missed, but at the expense of longer search times.

### Limiting Hits

The sizes of the hits can be limited by setting appropriate values to the SynthonSpaceSearchParams object. Maximum and minimum values can be set for the number of heavy atoms, the number of chiral atoms and the molecular weight.


## Non-Chemical Functionality

### Bit vectors

Bit vectors are containers for efficiently storing a set number of binary values, e.g. for fingerprints. The RDKit includes two types of fingerprints differing in how they store the values internally; the two types are easily interconverted but are best used for different purpose:

- SparseBitVects store only the list of bits set in the vector; they are well suited for storing very large, very sparsely occupied vectors like pharmacophore fingerprints. Some operations, such as retrieving the list of on bits, are quite fast. Others, such as negating the vector, are very, very slow.
- ExplicitBitVects keep track of both on and off bits. They are generally faster than SparseBitVects, but require more memory to store.

### Discrete value vectors

### 3D grids

### Points


## Getting Help

There is a reasonable amount of documentation available within from the RDKit’s docstrings. These are accessible using Python’s help command:

```pycon
>>> m = Chem.MolFromSmiles('Cc1ccccc1')
>>> m.GetNumAtoms()
7
>>> help(m.GetNumAtoms)
Help on method GetNumAtoms...

GetNumAtoms(...) method of rdkit.Chem.rdchem.Mol instance
    GetNumAtoms( (Mol)self [, (int)onlyHeavy=-1 [, (bool)onlyExplicit=True]]) -> int :
        Returns the number of atoms in the molecule.

          ARGUMENTS:
            - onlyExplicit: (optional) include only explicit atoms (atoms in the molecular graph)
                            defaults to 1.
          NOTE: the onlyHeavy argument is deprecated

        C++ signature :
            int GetNumAtoms(...)

>>> m.GetNumAtoms(onlyExplicit=False)
15
```

When working in an environment that does command completion or tooltips, one can see the available methods quite easily. Here’s a sample screenshot from within the Jupyter notebook:


## Advanced Topics/Warnings

### Editing Molecules

Some of the functionality provided allows molecules to be edited “in place”:

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1')
>>> m.GetAtomWithIdx(0).SetAtomicNum(7)
>>> Chem.SanitizeMol(m)
rdkit.Chem.rdmolops.SanitizeFlags.SANITIZE_NONE
>>> Chem.MolToSmiles(m)
'c1ccncc1'
```

Do not forget the sanitization step, without it one can end up with results that look ok (so long as you don’t think):

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1')
>>> m.GetAtomWithIdx(0).SetAtomicNum(8)
>>> Chem.MolToSmiles(m)
'c1ccocc1'
```

but that are, of course, complete nonsense, as sanitization will indicate:

```pycon
>>> Chem.SanitizeMol(m)
Traceback (most recent call last):
  File "/usr/lib/python3.6/doctest.py", line 1253, in __run
    compileflags, 1) in test.globs
  File "<doctest default[0]>", line 1, in <module>
    Chem.SanitizeMol(m)
rdkit.Chem.rdchem.KekulizeException: Can't kekulize mol.  Unkekulized atoms: 1 2 3 4 5
```

More complex transformations can be carried out using the `rdkit.Chem.rdchem.RWMol` class:

```pycon
>>> m = Chem.MolFromSmiles('CC(=O)C=CC=C')
>>> mw = Chem.RWMol(m)
>>> mw.ReplaceAtom(4,Chem.Atom(7))
>>> mw.AddAtom(Chem.Atom(6))
7
>>> mw.AddAtom(Chem.Atom(6))
8
>>> mw.AddBond(6,7,Chem.BondType.SINGLE)
7
>>> mw.AddBond(7,8,Chem.BondType.DOUBLE)
8
>>> mw.AddBond(8,3,Chem.BondType.SINGLE)
9
>>> mw.RemoveAtom(0)
>>> mw.GetNumAtoms()
8
```

The RWMol can be used just like an ROMol:

```pycon
>>> Chem.MolToSmiles(mw)
'O=CC1=NC=CC=C1'
>>> Chem.SanitizeMol(mw)
rdkit.Chem.rdmolops.SanitizeFlags.SANITIZE_NONE
>>> Chem.MolToSmiles(mw)
'O=Cc1ccccn1'
```

The RDKit also has functionality enabling batch edits of molecules which provides a more efficient way to remove multiple atoms or bonds at once.

```pycon
>>> m = Chem.MolFromSmiles('CC(=O)C=CC=C')
>>> mw = Chem.RWMol(m)
>>> mw.BeginBatchEdit()
>>> mw.RemoveAtom(3)
>>> mw.RemoveBond(1,2)  #<- these are the begin and end atoms of the bond
```

None of the changes actually happen until we “commit” them:

```pycon
>>> Chem.MolToSmiles(mw)
'C=CC=CC(C)=O'
>>> mw.CommitBatchEdit()
>>> Chem.MolToSmiles(mw)
'C=CC.CC.O'
```

You can make this more concise using a context manager, which takes care of the commit for you:

```pycon
>>> with Chem.RWMol(m) as mw:
...     mw.RemoveAtom(3)
...     mw.RemoveBond(1,2)
...
>>> Chem.MolToSmiles(mw)
'C=CC.CC.O'
```

It is even easier to generate nonsense using the RWMol than it is with standard molecules. If you need chemically reasonable results, be certain to sanitize the results.


## Miscellaneous Tips and Hints

### Chem vs AllChem

The majority of “basic” chemical functionality (e.g. reading/writing molecules, substructure searching, molecular cleanup, etc.) is in the `rdkit.Chem` module. More advanced, or less frequently used, functionality is in `rdkit.Chem.AllChem`. The distinction has been made to speed startup and lower import times; there’s no sense in loading the 2D->3D library and force field implementation if one is only interested in reading and writing a couple of molecules. If you find the Chem/AllChem thing annoying or confusing, you can use python’s “import … as …” syntax to remove the irritation:

```pycon
>>> from rdkit.Chem import AllChem as Chem
>>> m = Chem.MolFromSmiles('CCC')
```

### The SSSR Problem

As others have ranted about with more energy and eloquence than I intend to, the definition of a molecule’s smallest set of smallest rings is not unique. In some high symmetry molecules, a “true” SSSR will give results that are unappealing. For example, the SSSR for cubane only contains 5 rings, even though there are “obviously” 6. This problem can be fixed by implementing a *small* (instead of *smallest*) set of smallest rings algorithm that returns symmetric results. This is the approach that we took with the RDKit in `rdkit.Chem.GetSymmSSSR()`.

Because it is sometimes useful to know the “true” SSSR rings, there is a `rdkit.Chem.GetSSSR()` function which returns this potentially non-unique set of rings.


## List of Available Descriptors

| Descriptor/Descriptor Family | Notes | Language |
|---|---|---|
| Gasteiger/Marsili Partial Charges | *Tetrahedron* **36**:3219-28 (1980) | C++ |
| BalabanJ | *Chem. Phys. Lett.* **89**:399-404 (1982) | Python |
| BertzCT | *J. Am. Chem. Soc.* **103**:3599-601 (1981) | Python |
| Ipc | *J. Chem. Phys.* **67**:4517-33 (1977) | Python |
| HallKierAlpha | *Rev. Comput. Chem.* **2**:367-422 (1991) | C++ |
| Kappa1 - Kappa3 | *Rev. Comput. Chem.* **2**:367-422 (1991) | C++ |
| Phi | New in 2021.03 release *Quant. Struct.-Act. Rel.* **8**:221-224 (1989) | C++ |
| Chi0, Chi1 | *Rev. Comput. Chem.* **2**:367-422 (1991) | Python |
| Chi0n - Chi4n | *Rev. Comput. Chem.* **2**:367-422 (1991) | C++ |
| Chi0v - Chi4v | *Rev. Comput. Chem.* **2**:367-422 (1991) | C++ |
| MolLogP | Wildman and Crippen *JCICS* **39**:868-73 (1999) | C++ |
| MolMR | Wildman and Crippen *JCICS* **39**:868-73 (1999) | C++ |
| MolWt |   | C++ |
| ExactMolWt |   | C++ |
| HeavyAtomCount |   | C++ |
| HeavyAtomMolWt |   | C++ |
| NHOHCount |   | C++ |
| NOCount |   | C++ |
| NumHAcceptors |   | C++ |
| NumHDonors |   | C++ |
| NumHeteroatoms |   | C++ |
| NumRotatableBonds |   | C++ |
| NumValenceElectrons |   | C++ |
| NumAmideBonds |   | C++ |
| NumHeterocycles |   | C++ |
| Num{Aromatic,Saturated,Aliphatic}Rings |   | C++ |
| Num{Aromatic,Saturated,Aliphatic}{Hetero,Carbo}cycles |   | C++ |
| RingCount |   | C++ |
| FractionCSP3 |   | C++ |
| NumSpiroAtoms | Number of spiro atoms (atoms shared between rings that share exactly one atom) | C++ |
| NumBridgeheadAtoms | Number of bridgehead atoms (atoms shared between rings that share at least two bonds) | C++ |
| NumAtomStereoCenters |   | C++ |
| NumAtomUnspecifiedStereoCenters |   | C++ |
| TPSA | *J. Med. Chem.* **43**:3714-7, (2000) See the section in the RDKit book describing differences to the original publication. | C++ |
| LabuteASA | *J. Mol. Graph. Mod.* **18**:464-77 (2000) | C++ |
| PEOE_VSA1 - PEOE_VSA14 | MOE-type descriptors using partial charges and surface area contributions http://www.chemcomp.com/journal/vsadesc.htm | C++ |
| SMR_VSA1 - SMR_VSA10 | MOE-type descriptors using MR contributions and surface area contributions http://www.chemcomp.com/journal/vsadesc.htm | C++ |
| SlogP_VSA1 - SlogP_VSA12 | MOE-type descriptors using LogP contributions and surface area contributions http://www.chemcomp.com/journal/vsadesc.htm | C++ |
| EState_VSA1 - EState_VSA11 | MOE-type descriptors using EState indices and surface area contributions (developed at RD, not described in the CCG paper) | Python |
| VSA_EState1 - VSA_EState10 | MOE-type descriptors using EState indices and surface area contributions (developed at RD, not described in the CCG paper) | Python |
| MQNs | Nguyen et al. *ChemMedChem* **4**:1803-5 (2009) | C++ |
| Topliss fragments | implemented using a set of SMARTS definitions in $(RDBASE)/Data/FragmentDescriptors.csv | Python |
| Autocorr2D | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| BCUT2D | New in 2020.09 release. Pearlman and Smith in “3D-QSAR and Drug design: Recent Advances” (1997) | C++ |


## List of Available 3D Descriptors

These all require the molecule to have a 3D conformer.

| Descriptor/Descriptor Family | Notes | Language |
|---|---|---|
| Plane of best fit (PBF) | Nicholas C. Firth, Nathan Brown, and Julian Blagg, *JCIM* **52**:2516-25 | C++ |
| PMI1, PMI2, PMI3 | Principal moments of inertia | C++ |
| NPR1, NPR2 | Normalized principal moments ratios Sauer and Schwarz *JCIM* **43**:987-1003 (2003) | C++ |
| Radius of gyration | G. A. Arteca “Molecular Shape Descriptors” Reviews in Computational Chemistry vol 9 https://doi.org/10.1002/9780470125861.ch5 | C++ |
| Inertial shape factor | Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| Eccentricity | G. A. Arteca “Molecular Shape Descriptors” Reviews in Computational Chemistry vol 9 https://doi.org/10.1002/9780470125861.ch5 | C++ |
| Asphericity | A. Baumgaertner, “Shapes of flexible vesicles” J. Chem. Phys. 98:7496 (1993) https://doi.org/10.1063/1.464689 | C++ |
| Spherocity Index | Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| Autocorr3D | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| RDF | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| MORSE | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 | C++ |
| WHIM | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 **Note** insufficient information is available to exactly reproduce values from DRAGON for these descriptors. We believe that this is close. | C++ |
| GETAWAY | New in 2017.09 release. Todeschini and Consoni “Descriptors from Molecular Geometry” Handbook of Chemoinformatics https://doi.org/10.1002/9783527618279.ch37 **Note** insufficient information is available to exactly reproduce values from DRAGON for these descriptors. We believe that this is close. | C++ |
| DCLV | New in 2024.03 release. Eisenhaber et al. J. of Comp. Chem, Vol. 16, pp. 273-284, 1995. https://doi.org/10.1002/jcc.540160303 | C++ |


## List of Available Fingerprints

| Fingerprint Type | Notes | Language |
|---|---|---|
| RDKit | a Daylight-like fingerprint based on hashing molecular subgraphs | C++ |
| Atom Pairs | *JCICS* **25**:64-73 (1985) | C++ |
| Topological Torsions | *JCICS* **27**:82-5 (1987) | C++ |
| MACCS keys | Using the 166 public keys implemented as SMARTS | C++ |
| Morgan/Circular | Fingerprints based on the Morgan algorithm, similar to the ECFP/FCFP fingerprints *JCIM* **50**:742-54 (2010). | C++ |
| 2D Pharmacophore | Uses topological distances between pharmacophoric points. | C++ |
| Pattern | a topological fingerprint optimized for substructure screening | C++ |
| Extended Reduced Graphs | Derived from the ErG fingerprint published by Stiefl et al. in *JCIM* **46**:208–20 (2006). NOTE: these functions return an array of floats, not the usual fingerprint types | C++ |
| MHFP and SECFP | Derived from the ErG fingerprint published by Probst et al. in *J Cheminformatics* **10** (2018). NOTE: these functions return different types of values | C++ |


## Feature Definitions Used in the Morgan Fingerprints

These are adapted from the definitions in Gobbi, A. & Poppinger, D. “Genetic optimization of combinatorial libraries.” *Biotechnology and Bioengineering* **61**, 47-54 (1998).

| Feature | SMARTS |
|---|---|
| Donor | `[$([N;!H0;v3,v4&+1]),$([O,S;H1;+0]),n&H1&+0]` |
| Acceptor | `[$([O,S;H1;v2;!$(*-*=[O,N,P,S])]),$([O,S;H0;v2]),$([O,S;-]),$([N;v3;!$(N-*=[O,N,P,S])]),n&H0&+0,$([o,s;+0;!$([o,s]:n);!$([o,s]:c:n)])]` |
| Aromatic | `[a]` |
| Halogen | `[F,Cl,Br,I]` |
| Basic | `[#7;+,$([N;H2&+0][$([C,a]);!$([C,a](=O))]),$([N;H1&+0]([$([C,a]);!$([C,a](=O))])[$([C,a]);!$([C,a](=O))]),$([N;H0&+0]([C;!$(C(=O))])([C;!$(C(=O))])[C;!$(C(=O))])]` |
| Acidic | `[$([C,S](=[O,S,P])-[O;H1,-1])]` |


## Filtering Molecular Datasets

Several sets of rules exist for estimating the likelihood of a molecule exhibiting drug-like behaviour. It’s worth noting that these are rules of thumb, and that many examples of approved small molecule drugs exist that disobey these rules.

### Lipinski Rule of 5

Lipinski’s “Rule of 5” [19] was introduced to estimate the oral bioavailability of molecules. Poor absorption is likely if the molecule violates more than one of the following conditions:

- Molecular Weight <= 500 Da
- No. Hydrogen Bond Donors <= 5
- No. Hydrogen Bond Acceptors <= 10
- LogP <= 5

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem import Descriptors
>>> mol = Chem.MolFromSmiles('CC(=O)Nc1ccc(O)cc1')  # e.g. Paracetamol

# Ro5 descriptors
>>> MW = Descriptors.MolWt(mol)
>>> HBA = Descriptors.NOCount(mol)
>>> HBD = Descriptors.NHOHCount(mol)
>>> LogP = Descriptors.MolLogP(mol)
>>> conditions = [MW <= 500, HBA <= 10, HBD <= 5, LogP <= 5]
>>> pass_ro5 = conditions.count(True) >= 3
>>> print(pass_ro5)
True
```

### Filtering Unwanted Substructures

Pan Assay Interference Compounds (or PAINS) [20] are molecules that display non-specific binding, leading to unwanted side effects and false-positives in virtual screening. Common PAINS motifs include toxoflavin, isothiazolones, hydroxyphenyl hydrazones, curcumin, phenolsulfonamides, rhodanines, enones, quinones, and catechols.

The Brenk filter [21] removes molecules containing substructures with undesirable pharmacokinetics or toxicity. These include sulfates and phosphates that contribute to unfavourable pharmacokinetics, nitro groups which are mutagenic and 2-halopyridines and thiols which are both reactive.

The NIH filter [22], [23] defined a list of functional groups with undesirable properties. These are split into those with reactive functionalities (including Michael acceptors, aldehydes, epoxides, alkyl halides, metals, 2-halo pyridines, phosphorus nitrogen bonds, α-chloroketones and β-lactams) and medicinal chemistry exclusions (including oximes, crown ethers, hydrazines, flavanoids, polyphenols, primary halide sulfates and multiple nitro groups).

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams

>>> mol = Chem.MolFromSmiles('CC1=C(C=C(C=C1)N2C(=O)C(=C(N2)C)N=NC3=CC=CC(=C3O)C4=CC(=CC=C4)C(=O)O)C')  # e.g. Eltrombopag

# PAINS flag
>>> params_pains = FilterCatalogParams()
>>> params_pains.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_A)
True
>>> catalog_pains = FilterCatalog(params_pains)
>>> flag = catalog_pains.HasMatch(mol)  # Checks if there is a matching PAINS
>>> print("PAINs: ", flag)
PAINs:  True

# Brenk Flag
>>> params_unwanted = FilterCatalogParams()
>>> params_unwanted.AddCatalog(FilterCatalogParams.FilterCatalogs.BRENK)
True
>>> catalog_unwanted = FilterCatalog(params_unwanted)
>>> flag = catalog_unwanted.HasMatch(mol)  # Checks if there is a matching unwanted substructure
>>> print("Brenk: ", flag)
Brenk:  True

# NIH Flag
>>> params_nih = FilterCatalogParams()
>>> params_nih.AddCatalog(FilterCatalogParams.FilterCatalogs.NIH)
True
>>> catalog_nih = FilterCatalog(params_nih)
>>> flag = catalog_nih.HasMatch(mol)  # Checks if there is a matching NIH
>>> print("NIH: ", flag)
NIH:  True
```

All of the available filters can also be considered at once. Additional information such as the class and description of the unwanted substructures can be obtained using the FilterCatalogEntry object:

```pycon
>>> from rdkit import Chem
>>> from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams

>>> mol = Chem.MolFromSmiles('CC1=C(C=C(C=C1)N2C(=O)C(=C(N2)C)N=NC3=CC=CC(=C3O)C4=CC(=CC=C4)C(=O)O)C')  # e.g. Eltrombopag

# ALL Filters
>>> params_all = FilterCatalogParams()
>>> params_all.AddCatalog(FilterCatalogParams.FilterCatalogs.ALL)
True
>>> catalog_all = FilterCatalog(params_all)

>>> print([entry.GetProp('FilterSet') for entry in catalog_all.GetMatches(mol)])
['PAINS_A', 'Brenk', 'NIH', 'ChEMBL23_Dundee', 'ChEMBL23_BMS', 'ChEMBL23_MLSMR', 'ChEMBL23_Inpharmatica', 'ChEMBL23_LINT']
>>> print([entry.GetDescription() for entry in catalog_all.GetMatches(mol)])
['azo_A(324)', 'diazo_group', 'azo_aryl', 'diazo group', 'azo_aryl', 'Azo', 'Filter5_azo', 'acyclic N-,=N and not N bound to carbonyl or sulfone']
```

Footnotes


## License

This document is copyright (C) 2007-2021 by Greg Landrum

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, 543 Howard Street, 5th Floor, San Francisco, California, 94105, USA.

The intent of this license is similar to that of the RDKit itself. In simple words: “Do whatever you want with it, but please give us some credit.”
