---
title: "Getting Started with the RDKit in Python (part 1/3)"
source: https://www.rdkit.org/docs/GettingStartedInPython.html
domain: cheminformatics-rdkit
license: CC-BY-SA-4.0
tags: cheminformatics rdkit, molecular descriptor, smiles notation, chemical fingerprint
fetched: 2026-07-02
part: 1/3
---

# Getting Started with the RDKit in Python


## Important note

Beginning with the 2019.03 release, the RDKit is no longer supporting Python 2. If you need to continue using Python 2, please stick with a release from the 2018.09 release cycle.


## What is this?

This document is intended to provide an overview of how one can use the RDKit functionality from Python. It’s not comprehensive and it’s not a manual.

If you find mistakes, or have suggestions for improvements, please either fix them yourselves in the source document (the .rst file) or send them to the mailing list: rdkit-devel@lists.sourceforge.net In particular, if you find yourself spending time working out how to do something that doesn’t appear to be documented please contribute by writing it up for this document. Contributing to the documentation is a great service both to the RDKit community and to your future self.


## Reading, Drawing, and Writing Molecules

### Reading single molecules

The majority of the basic molecular functionality is found in module `rdkit.Chem`:

```pycon
>>> from rdkit import Chem
```

Individual molecules can be constructed using a variety of approaches:

```pycon
>>> m = Chem.MolFromSmiles('Cc1ccccc1')
>>> m = Chem.MolFromMolFile('data/input.mol')
>>> stringWithMolData=open('data/input.mol','r').read()
>>> m = Chem.MolFromMolBlock(stringWithMolData)
```

All of these functions return a `rdkit.Chem.rdchem.Mol` object on success:

```pycon
>>> m
<rdkit.Chem.rdchem.Mol object at 0x...>
```

or None on failure:

```pycon
>>> m_invalid = Chem.MolFromMolFile('data/invalid.mol')
>>> m_invalid is None
True
```

An `rdkit.Chem.rdchem.Mol` object can be displayed graphically using `rdkit.Chem.Draw.MolToImage()`:

```pycon
>>> from rdkit.Chem import Draw
>>> img = Draw.MolToImage(m)
```

An attempt is made to provide sensible error messages:

```pycon
>>> m1 = Chem.MolFromSmiles('CO(C)C')
```

displays a message like: `[12:18:01] Explicit valence for atom # 1 O greater than permitted` and

```pycon
>>> m2 = Chem.MolFromSmiles('c1cc1')
```

displays something like: `[12:20:41] Can't kekulize mol`. In each case the value `None` is returned:

```pycon
>>> m1 is None
True
>>> m2 is None
True
```

### Reading sets of molecules

Groups of molecules are read using a Supplier (for example, an `rdkit.Chem.rdmolfiles.SDMolSupplier` or a `rdkit.Chem.rdmolfiles.SmilesMolSupplier`):

```pycon
>>> suppl = Chem.SDMolSupplier('data/5ht3ligs.sdf')
>>> for mol in suppl:
...   print(mol.GetNumAtoms())
...
20
24
24
26
```

You can easily produce lists of molecules from a Supplier:

```pycon
>>> mols = [x for x in suppl]
>>> len(mols)
4
```

or just treat the Supplier itself as a random-access object:

```pycon
>>> suppl[0].GetNumAtoms()
20
```

Two good practices when working with Suppliers are to use a context manager and to test each molecule to see if it was correctly read before working with it:

```pycon
>>> with Chem.SDMolSupplier('data/5ht3ligs.sdf') as suppl:
...   for mol in suppl:
...     if mol is None: continue
...     print(mol.GetNumAtoms())
...
20
24
24
26
```

An alternate type of Supplier, the `rdkit.Chem.rdmolfiles.ForwardSDMolSupplier` can be used to read from file-like objects:

```pycon
>>> inf = open('data/5ht3ligs.sdf','rb')
>>> with Chem.ForwardSDMolSupplier(inf) as fsuppl:
...   for mol in fsuppl:
...     if mol is None: continue
...     print(mol.GetNumAtoms())
...
20
24
24
26
```

This means that they can be used to read from compressed files:

```pycon
>>> import gzip
>>> inf = gzip.open('data/actives_5ht3.sdf.gz')
>>> with Chem.ForwardSDMolSupplier(inf) as gzsuppl:
...    ms = [x for x in gzsuppl if x is not None]
>>> len(ms)
180
```

Note that ForwardSDMolSuppliers cannot be used as random-access objects:

```pycon
>>> inf = open('data/5ht3ligs.sdf','rb')
>>> with Chem.ForwardSDMolSupplier(inf) as fsuppl:
...   fsuppl[0]
Traceback (most recent call last):
  ...
TypeError: 'ForwardSDMolSupplier' object does not support indexing
```

For reading Smiles or SDF files with large number of records concurrently, MultithreadedMolSuppliers can be used like this:

```pycon
>>> i = 0
>>> with Chem.MultithreadedSDMolSupplier('data/5ht3ligs.sdf') as sdSupl:
...   for mol in sdSupl:
...     if mol is not None:
...       i += 1
...
>>> print(i)
4
```

By default a single reader thread is used to extract records from the file and a single writer thread is used to process them. Note that due to multithreading the output may not be in the expected order. Furthermore, the MultithreadedSmilesMolSupplier and the MultithreadedSDMolSupplier cannot be used as random-access objects.

### Writing molecules

Single molecules can be converted to text using several functions present in the `rdkit.Chem` module.

For example, for SMILES:

```pycon
>>> m = Chem.MolFromMolFile('data/chiral.mol')
>>> Chem.MolToSmiles(m)
'C[C@H](O)c1ccccc1'
>>> Chem.MolToSmiles(m,isomericSmiles=False)
'CC(O)c1ccccc1'
```

Note that the SMILES provided is canonical, so the output should be the same no matter how a particular molecule is input:

```pycon
>>> Chem.MolToSmiles(Chem.MolFromSmiles('C1=CC=CN=C1'))
'c1ccncc1'
>>> Chem.MolToSmiles(Chem.MolFromSmiles('c1cccnc1'))
'c1ccncc1'
>>> Chem.MolToSmiles(Chem.MolFromSmiles('n1ccccc1'))
'c1ccncc1'
```

If you’d like to have the Kekule form of the SMILES, first Kekulize the molecule, then use the “kekuleSmiles” option:

```pycon
>>> Chem.Kekulize(m)
>>> Chem.MolToSmiles(m,kekuleSmiles=True)
'C[C@H](O)C1=CC=CC=C1'
```

Note: as of this writing (Aug 2008), the smiles provided when one requests kekuleSmiles are not canonical. The limitation is not in the SMILES generation, but in the kekulization itself.

MDL Mol blocks are also available:

```pycon
>>> m2 = Chem.MolFromSmiles('C1CCC1')
>>> print(Chem.MolToMolBlock(m2))

     RDKit          2D

  4  4  0  0  0  0  0  0  0  0999 V2000
    1.0607    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0000   -1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0607    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  1  0
  3  4  1  0
  4  1  1  0
M  END
```

To include names in the mol blocks, set the molecule’s “_Name” property:

```pycon
>>> m2.SetProp("_Name","cyclobutane")
>>> print(Chem.MolToMolBlock(m2))
cyclobutane
     RDKit          2D

  4  4  0  0  0  0  0  0  0  0999 V2000
    1.0607    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0000   -1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0607    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  1  0
  3  4  1  0
  4  1  1  0
M  END
```

In order for atom or bond stereochemistry to be recognised correctly by most software, it’s essential that the mol block have atomic coordinates. It’s also convenient for many reasons, such as drawing the molecules. Generating a mol block for a molecule that does not have coordinates will, by default, automatically cause coordinates to be generated. These are not, however, stored with the molecule. Coordinates can be generated and stored with the molecule using functionality in the `rdkit.Chem.AllChem` module (see the Chem vs AllChem section for more information).

You can either include 2D coordinates (i.e. a depiction):

```pycon
>>> from rdkit.Chem import AllChem
>>> AllChem.Compute2DCoords(m2)
0
>>> print(Chem.MolToMolBlock(m2))
cyclobutane
     RDKit          2D

  4  4  0  0  0  0  0  0  0  0999 V2000
    1.0607   -0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.0000   -1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0607    0.0000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.0000    1.0607    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  1  0
  3  4  1  0
  4  1  1  0
M  END
```

Or you can add 3D coordinates by embedding the molecule (this uses the ETKDG method, which is described in more detail below). Note that we add Hs to the molecule before generating the conformer. This is essential to get good structures:

```pycon
>>> m3 = Chem.AddHs(m2)
>>> params = AllChem.ETKDGv3()
>>> params.randomSeed = 0xf00d # optional random seed for reproducibility
>>> AllChem.EmbedMolecule(m3, params)
0
>>> print(Chem.MolToMolBlock(m3))
cyclobutane
     RDKit          3D

 12 12  0  0  0  0  0  0  0  0999 V2000
    1.0257    0.2442   -0.0991 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2041    0.9236    0.4320 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0443   -0.2424   -0.0253 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2102   -0.9939   -0.3417 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.4192    0.7683   -0.9787 H   0  0  0  0  0  0  0  0  0  0  0  0
    1.8181    0.1486    0.6820 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.1697    1.0826    1.5236 H   0  0  0  0  0  0  0  0  0  0  0  0
   -0.5360    1.8377   -0.1050 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6809   -0.0600   -0.8987 H   0  0  0  0  0  0  0  0  0  0  0  0
   -1.6510   -0.6193    0.8225 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.4659   -1.7768    0.3858 H   0  0  0  0  0  0  0  0  0  0  0  0
    0.3467   -1.3126   -1.3975 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  1  0
  3  4  1  0
  4  1  1  0
  1  5  1  0
  1  6  1  0
  2  7  1  0
  2  8  1  0
  3  9  1  0
  3 10  1  0
  4 11  1  0
  4 12  1  0
M  END
```

If we don’t want the Hs in our later analysis, they are easy to remove:

```pycon
>>> m3 = Chem.RemoveHs(m3)
>>> print(Chem.MolToMolBlock(m3))
cyclobutane
      RDKit          3D

  4  4  0  0  0  0  0  0  0  0999 V2000
    1.0257    0.2442   -0.0991 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2041    0.9236    0.4320 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.0443   -0.2424   -0.0253 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2102   -0.9939   -0.3417 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0
  2  3  1  0
  3  4  1  0
  4  1  1  0
M  END
```

If you’d like to write the molecule to a file, use Python file objects:

```pycon
>>> print(Chem.MolToMolBlock(m2),file=open('data/foo.mol','w+'))
>>>
```

### Writing sets of molecules

Multiple molecules can be written to a file using an `rdkit.Chem.rdmolfiles.SDWriter` object:

```pycon
>>> with Chem.SDWriter('data/foo.sdf') as w:
...   for m in mols:
...     w.write(m)
>>>
```

An SDWriter can also be initialized using a file-like object:

```pycon
>>> from io import StringIO
>>> sio = StringIO()
>>> with Chem.SDWriter(sio) as w:
...   for m in mols:
...     w.write(m)
>>> print(sio.getvalue())
mol-295
     RDKit          3D

 20 22  0  0  1  0  0  0  0  0999 V2000
    2.3200    0.0800   -0.1000 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.8400   -1.2200    0.1200 C   0  0  0  0  0  0  0  0  0  0  0  0
...
  1  3  1  0
  1  4  1  0
  2  5  1  0
M  END
$$$$
```

Other available Writers include the `rdkit.Chem.rdmolfiles.SmilesWriter` and the `rdkit.Chem.rdmolfiles.TDTWriter`.


## Working with Molecules

### Looping over Atoms and Bonds

Once you have a molecule, it’s easy to loop over its atoms and bonds:

```pycon
>>> m = Chem.MolFromSmiles('C1OC1')
>>> for atom in m.GetAtoms():
...   print(atom.GetAtomicNum())
...
6
8
6
>>> print(m.GetBonds()[0].GetBondType())
SINGLE
```

You can also request individual bonds or atoms:

```pycon
>>> m.GetAtomWithIdx(0).GetSymbol()
'C'
>>> m.GetAtomWithIdx(0).GetExplicitValence()
2
>>> m.GetBondWithIdx(0).GetBeginAtomIdx()
0
>>> m.GetBondWithIdx(0).GetEndAtomIdx()
1
>>> m.GetBondBetweenAtoms(0,1).GetBondType()
rdkit.Chem.rdchem.BondType.SINGLE
```

Atoms keep track of their neighbors:

```pycon
>>> atom = m.GetAtomWithIdx(0)
>>> [x.GetAtomicNum() for x in atom.GetNeighbors()]
[8, 6]
>>> len(atom.GetNeighbors()[-1].GetBonds())
2
```

### Ring Information

Atoms and bonds both carry information about the molecule’s rings:

```pycon
>>> m = Chem.MolFromSmiles('OC1C2C1CC2')
>>> m.GetAtomWithIdx(0).IsInRing()
False
>>> m.GetAtomWithIdx(1).IsInRing()
True
>>> m.GetAtomWithIdx(2).IsInRingSize(3)
True
>>> m.GetAtomWithIdx(2).IsInRingSize(4)
True
>>> m.GetAtomWithIdx(2).IsInRingSize(5)
False
>>> m.GetBondWithIdx(1).IsInRingSize(3)
True
>>> m.GetBondWithIdx(1).IsInRing()
True
```

But note that the information is only about the smallest rings:

```pycon
>>> m.GetAtomWithIdx(1).IsInRingSize(5)
False
```

More detail about the smallest set of smallest rings (SSSR) is available:

```pycon
>>> ssr = Chem.GetSymmSSSR(m)
>>> len(ssr)
2
>>> list(ssr[0])
[1, 2, 3]
>>> list(ssr[1])
[4, 5, 2, 3]
```

As the name indicates, this is a symmetrized SSSR; if you are interested in the number of “true” SSSR, use the GetSSSR function (note that in this case there’s no difference).

```pycon
>>> len(Chem.GetSSSR(m))
2
```

The distinction between symmetrized and non-symmetrized SSSR is discussed in more detail below in the section The SSSR Problem.

For more efficient queries about a molecule’s ring systems (avoiding repeated calls to Mol.GetAtomWithIdx), use the `rdkit.Chem.rdchem.RingInfo` class:

```pycon
>>> m = Chem.MolFromSmiles('OC1C2C1CC2')
>>> ri = m.GetRingInfo()
>>> ri.NumAtomRings(0)
0
>>> ri.NumAtomRings(1)
1
>>> ri.NumAtomRings(2)
2
>>> ri.IsAtomInRingOfSize(1,3)
True
>>> ri.IsBondInRingOfSize(1,3)
True
```

### Modifying molecules

Normally molecules are stored in the RDKit with the hydrogen atoms implicit (e.g. not explicitly present in the molecular graph. When it is useful to have the hydrogens explicitly present, for example when generating or optimizing the 3D geometry, the :py:func:rdkit.Chem.rdmolops.AddHs function can be used:

```pycon
>>> m=Chem.MolFromSmiles('CCO')
>>> m.GetNumAtoms()
3
>>> m2 = Chem.AddHs(m)
>>> m2.GetNumAtoms()
9
```

The Hs can be removed again using the `rdkit.Chem.rdmolops.RemoveHs()` function:

```pycon
>>> m3 = Chem.RemoveHs(m2)
>>> m3.GetNumAtoms()
3
```

RDKit molecules are usually stored with the bonds in aromatic rings having aromatic bond types. This can be changed with the `rdkit.Chem.rdmolops.Kekulize()` function:

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1')
>>> m.GetBondWithIdx(0).GetBondType()
rdkit.Chem.rdchem.BondType.AROMATIC
>>> Chem.Kekulize(m)
>>> m.GetBondWithIdx(0).GetBondType()
rdkit.Chem.rdchem.BondType.SINGLE
>>> m.GetBondWithIdx(1).GetBondType()
rdkit.Chem.rdchem.BondType.DOUBLE
```

By default, the bonds are still marked as being aromatic:

```pycon
>>> m.GetBondWithIdx(1).GetIsAromatic()
True
```

because the flags in the original molecule are not cleared (clearAromaticFlags defaults to False). You can explicitly force or decline a clearing of the flags:

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1')
>>> m.GetBondWithIdx(0).GetIsAromatic()
True
>>> m1 = Chem.MolFromSmiles('c1ccccc1')
>>> Chem.Kekulize(m1, clearAromaticFlags=True)
>>> m1.GetBondWithIdx(0).GetIsAromatic()
False
```

Bonds can be restored to the aromatic bond type using the `rdkit.Chem.rdmolops.SanitizeMol()` function:

```pycon
>>> Chem.SanitizeMol(m)
rdkit.Chem.rdmolops.SanitizeFlags.SANITIZE_NONE
>>> m.GetBondWithIdx(0).GetBondType()
rdkit.Chem.rdchem.BondType.AROMATIC
```

The value returned by *SanitizeMol()* indicates that no problems were encountered.

### Working with 2D molecules: Generating Depictions

The RDKit has a library for generating depictions (sets of 2D) coordinates for molecules. This library, which is part of the AllChem module, is accessed using the `rdkit.Chem.rdDepictor.Compute2DCoords()` function:

```pycon
>>> m = Chem.MolFromSmiles('c1nccc2n1ccc2')
>>> AllChem.Compute2DCoords(m)
0
```

The 2D conformer is constructed in a canonical orientation and is built to minimize intramolecular clashes, i.e. to maximize the clarity of the drawing.

If you have a set of molecules that share a common template and you’d like to align them to that template, you can do so as follows:

```pycon
>>> template = Chem.MolFromSmiles('c1nccc2n1ccc2')
>>> AllChem.Compute2DCoords(template)
0
>>> ms = [Chem.MolFromSmiles(smi) for smi in ('OCCc1ccn2cnccc12','C1CC1Oc1cc2ccncn2c1','CNC(=O)c1nccc2cccn12')]
>>> for m in ms:
...     _ = AllChem.GenerateDepictionMatching2DStructure(m,template)
```

Running this process for the molecules above gives:

| (picture_1) | (picture_0) | (picture_3) |
|---|---|---|

Another option for Compute2DCoords allows you to generate 2D depictions for molecules that closely mimic 3D conformers. This is available using the function `rdkit.Chem.AllChem.GenerateDepictionMatching3DStructure()`.

Here is an illustration of the results using the ligand from PDB structure 1XP0:

| (picture_2) | (picture_4) |
|---|---|

More fine-grained control can be obtained using the core function `rdkit.Chem.rdDepictor.Compute2DCoordsMimicDistmat()`, but that is beyond the scope of this document. See the implementation of GenerateDepictionMatching3DStructure in AllChem.py for an example of how it is used.

### Working with 3D Molecules

The RDKit can generate conformers for molecules using two different methods. The original method used distance geometry. [1] The algorithm followed is:

1. The molecule’s distance bounds matrix is calculated based on the connection table and a set of rules.
2. The bounds matrix is smoothed using a triangle-bounds smoothing algorithm.
3. A random distance matrix that satisfies the bounds matrix is generated.
4. This distance matrix is embedded in 3D dimensions (producing coordinates for each atom).
5. The resulting coordinates are cleaned up somewhat using a crude force field and the bounds matrix.

Note that the conformers that result from this procedure tend to be fairly ugly. They should be cleaned up using a force field. This can be done within the RDKit using its implementation of the Universal Force Field (UFF). [2]

More recently, there is an implementation of the ETKDG method of Riniker and Landrum [18] which uses torsion angle preferences from the Cambridge Structural Database (CSD) to correct the conformers after distance geometry has been used to generate them. With this method, there should be no need to use a minimisation step to clean up the structures.

More detailed information about the conformer generator and the parameters controlling it can be found in the “RDKit Book”.

Since the 2018.09 release of the RDKit, ETKDG is the default conformer generation method. Since the 2024.03 release ETKDGv3 is the default.

The full process of embedding a molecule is easier than all the above verbiage makes it sound:

```pycon
>>> m2=Chem.AddHs(m)
>>> AllChem.EmbedMolecule(m2)
0
```

The RDKit also has an implementation of the MMFF94 force field available. [12], [13], [14], [15], [16] Please note that the MMFF atom typing code uses its own aromaticity model, so the aromaticity flags of the molecule will be modified after calling MMFF-related methods.

Here’s an example of using MMFF94 to minimize an RDKit-generated conformer: .. doctest:

```
>>> m = Chem.MolFromSmiles('C1CCC1OC')
>>> m2=Chem.AddHs(m)
>>> AllChem.EmbedMolecule(m2)
0
>>> AllChem.MMFFOptimizeMolecule(m2)
0
```

Note the calls to *Chem.AddHs()* in the examples above. By default RDKit molecules do not have H atoms explicitly present in the graph, but they are important for getting realistic geometries, so they generally should be added. They can always be removed afterwards if necessary with a call to *Chem.RemoveHs()*.

With the RDKit, multiple conformers can also be generated using the different embedding methods. In both cases this is simply a matter of running the distance geometry calculation multiple times from different random start points. The option *numConfs* allows the user to set the number of conformers that should be generated. Otherwise the procedures are as before. The conformers so generated can be aligned to each other and the RMS values calculated.

```pycon
>>> m = Chem.MolFromSmiles('C1CCC1OC')
>>> m2=Chem.AddHs(m)
>>> # run ETKDG 10 times
>>> cids = AllChem.EmbedMultipleConfs(m2, numConfs=10)
>>> print(len(cids))
10
>>> rmslist = []
>>> AllChem.AlignMolConformers(m2, RMSlist=rmslist)
>>> print(len(rmslist))
9
```

rmslist contains the RMS values between the first conformer and all others. The RMS between two specific conformers (e.g. 1 and 9) can also be calculated. The flag prealigned lets the user specify if the conformers are already aligned (by default, the function aligns them).

```pycon
>>> rms = AllChem.GetConformerRMS(m2, 1, 9, prealigned=True)
```

If you are interested in running MMFF94 on a molecule’s conformers (note that this is often not necessary when using ETKDG), there’s a convenience function available:

```pycon
>>> res = AllChem.MMFFOptimizeMoleculeConfs(m2)
```

The result is a list a containing 2-tuples: *(not_converged, energy)* for each conformer. If *not_converged* is 0, the minimization for that conformer converged.

By default *AllChem.EmbedMultipleConfs* and *AllChem.MMFFOptimizeMoleculeConfs()* run single threaded, but you can cause them to use multiple threads simultaneously for these embarassingly parallel tasks via the *numThreads* argument:

```pycon
>>> params = AllChem.ETKDGv3()
>>> params.numThreads = 0
>>> cids = AllChem.EmbedMultipleConfs(m2, 10, params)
>>> res = AllChem.MMFFOptimizeMoleculeConfs(m2, numThreads=0)
```

Setting *numThreads* to zero causes the software to use the maximum number of threads allowed on your computer.

*Disclaimer/Warning*: Conformer generation is a difficult and subtle task. The plain distance-geometry 2D->3D conversion provided with the RDKit is not intended to be a replacement for a “real” conformer analysis tool; it merely provides quick 3D structures for cases when they are required. We believe, however, that the newer ETKDG method [18] is suitable for most purposes.

### Preserving Molecules

Molecules can be converted to and from text using Python’s pickling machinery:

```pycon
>>> m = Chem.MolFromSmiles('c1ccncc1')
>>> import pickle
>>> pkl = pickle.dumps(m)
>>> m2=pickle.loads(pkl)
>>> Chem.MolToSmiles(m2)
'c1ccncc1'
```

The RDKit pickle format is fairly compact and it is much, much faster to build a molecule from a pickle than from a Mol file or SMILES string, so storing molecules you will be working with repeatedly as pickles can be a good idea.

The raw binary data that is encapsulated in a pickle can also be directly obtained from a molecule:

```pycon
>>> binStr = m.ToBinary()
```

This can be used to reconstruct molecules using the Chem.Mol constructor:

```pycon
>>> m2 = Chem.Mol(binStr)
>>> Chem.MolToSmiles(m2)
'c1ccncc1'
>>> len(binStr)
130
```

Note that this is smaller than the pickle:

```pycon
>>> len(binStr) < len(pkl)
True
```

The small overhead associated with python’s pickling machinery normally doesn’t end up making much of a difference for collections of larger molecules (the extra data associated with the pickle is independent of the size of the molecule, while the binary string increases in length as the molecule gets larger).

*Tip*: The performance difference associated with storing molecules in a pickled form on disk instead of constantly reparsing an SD file or SMILES table is difficult to overstate. In a test I just ran on my laptop, loading a set of 699 drug-like molecules from an SD file took 10.8 seconds; loading the same molecules from a pickle file took 0.7 seconds. The pickle file is also smaller – 1/3 the size of the SD file – but this difference is not always so dramatic (it’s a particularly fat SD file).

### Drawing Molecules

The RDKit has some built-in functionality for creating images from molecules found in the `rdkit.Chem.Draw` package:

```pycon
>>> with Chem.SDMolSupplier('data/cdk2.sdf') as suppl:
...   ms = [x for x in suppl if x is not None]
>>> for m in ms: tmp=AllChem.Compute2DCoords(m)
>>> from rdkit.Chem import Draw
>>> Draw.MolToFile(ms[0],'images/cdk2_mol1.o.png')
>>> Draw.MolToFile(ms[1],'images/cdk2_mol2.o.png')
```

Producing these images:

| (_images/cdk2_mol1.png) | (_images/cdk2_mol2.png) |
|---|---|

It’s also possible to produce an image grid out of a set of molecules:

```pycon
>>> img=Draw.MolsToGridImage(ms[:8],molsPerRow=4,subImgSize=(200,200),legends=[x.GetProp("_Name") for x in ms[:8]])
```

This returns a PIL image, which can then be saved to a file:

```pycon
>>> img.save('images/cdk2_molgrid.o.png')
```

The result looks like this:

These would of course look better if the common core were aligned. This is easy enough to do:

```pycon
>>> p = Chem.MolFromSmiles('[nH]1cnc2cncnc21')
>>> subms = [x for x in ms if x.HasSubstructMatch(p)]
>>> len(subms)
14
>>> AllChem.Compute2DCoords(p)
0
>>> for m in subms:
...   _ = AllChem.GenerateDepictionMatching2DStructure(m,p)
>>> img=Draw.MolsToGridImage(subms,molsPerRow=4,subImgSize=(200,200),legends=[x.GetProp("_Name") for x in subms])
>>> img.save('images/cdk2_molgrid.aligned.o.png')
```

The result looks like this:

Atoms in a molecule can be highlighted by drawing a coloured solid or open circle around them, and bonds likewise can have a coloured outline applied. An obvious use is to show atoms and bonds that have matched a substructure query

```pycon
>>> from rdkit.Chem.Draw import rdMolDraw2D
>>> smi = 'c1cc(F)ccc1Cl'
>>> mol = Chem.MolFromSmiles(smi)
>>> patt = Chem.MolFromSmarts('ClccccF')
>>> hit_ats = list(mol.GetSubstructMatch(patt))
>>> hit_bonds = []
>>> for bond in patt.GetBonds():
...    aid1 = hit_ats[bond.GetBeginAtomIdx()]
...    aid2 = hit_ats[bond.GetEndAtomIdx()]
...    hit_bonds.append(mol.GetBondBetweenAtoms(aid1,aid2).GetIdx())
>>> d = rdMolDraw2D.MolDraw2DSVG(500, 500) # or MolDraw2DCairo to get PNGs
>>> rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=hit_ats,
...                                    highlightBonds=hit_bonds)
```

will produce:

It is possible to specify the colours for individual atoms and bonds:

```pycon
>>> colours = [(0.8,0.0,0.8),(0.8,0.8,0),(0,0.8,0.8),(0,0,0.8)]
>>> atom_cols = {}
>>> for i, at in enumerate(hit_ats):
...     atom_cols[at] = colours[i%4]
>>> bond_cols = {}
>>> for i, bd in enumerate(hit_bonds):
...     bond_cols[bd] = colours[3 - i%4]
>>>
>>> d = rdMolDraw2D.MolDraw2DCairo(500, 500)
>>> rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=hit_ats,
...                                    highlightAtomColors=atom_cols,
...                                    highlightBonds=hit_bonds,
...                                    highlightBondColors=bond_cols)
```

to give:

Atoms and bonds can also be highlighted with multiple colours if they fall into multiple sets, for example if they are matched by more than 1 substructure pattern. This is too complicated to show in this simple introduction, but there is an example in data/test_multi_colours.py, which produces the somewhat garish

As of version 2020.03, it is possible to add arbitrary small strings to annotate atoms and bonds in the drawing. The strings are added as properties `atomNote` and `bondNote` and they will be placed automatically close to the atom or bond in question in a manner intended to minimise their clash with the rest of the drawing. For convenience, here are 3 flags in `MolDraw2DOptions` that will add stereo information (R/S to atoms, E/Z to bonds) and atom and bond sequence numbers.

```pycon
>>> mol = Chem.MolFromSmiles(r'Cl[C@H](F)NC\C=C\C')
>>> d = rdMolDraw2D.MolDraw2DCairo(250, 200) # or MolDraw2DSVG to get SVGs
>>> mol.GetAtomWithIdx(2).SetProp('atomNote', 'foo')
>>> mol.GetBondWithIdx(0).SetProp('bondNote', 'bar')
>>> d.drawOptions().addStereoAnnotation = True
>>> d.drawOptions().addAtomIndices = True
>>> d.DrawMolecule(mol)
>>> d.FinishDrawing()
>>> d.WriteDrawingText('atom_annotation_1.png')
```

will produce

If atoms have an `atomLabel` property set, this will be used when drawing them:

```pycon
>>> smi = 'c1nc(*)ccc1* |$;;;R1;;;;R2$|'
>>> mol = Chem.MolFromSmiles(smi)
>>> mol.GetAtomWithIdx(3).GetProp("atomLabel")
'R1'
>>> mol.GetAtomWithIdx(7).GetProp("atomLabel")
'R2'
>>> d = rdMolDraw2D.MolDraw2DCairo(250, 250)
>>> rdMolDraw2D.PrepareAndDrawMolecule(d,mol)
>>> d.WriteDrawingText("./images/atom_labels_1.png")
```

gives:

Since the `atomLabel` property is also used for other things (for example in CXSMILES as demonstrated), if you want to provide your own atom labels, it’s better to use the `_displayLabel` property:

```
>>> smi = 'c1nc(*)ccc1* |$;;;R1;;;;R2$|'
>>> mol = Chem.MolFromSmiles(smi)
>>> mol.GetAtomWithIdx(3).SetProp("_displayLabel","R<sub>1</sub>")
>>> mol.GetAtomWithIdx(7).SetProp("_displayLabel","R<sub>2</sub>")
>>> d = rdMolDraw2D.MolDraw2DCairo(250, 250)
>>> rdMolDraw2D.PrepareAndDrawMolecule(d,mol)
>>> d.WriteDrawingText("./images/atom_labels_2.png")
```

this gives:

Note that you can use `<sup>` and `<sub>` in these labels to provide super- and subscripts.

Finally, if you have atom labels which should be displayed differently when the bond comes into them from the right (the West), you can also set the `_displayLabelW` property:

```pycon
>>> smi = 'c1nc(*)ccc1* |$;;;R1;;;;R2$|'
>>> mol = Chem.MolFromSmiles(smi)
>>> mol.GetAtomWithIdx(3).SetProp("_displayLabel","CO<sub>2</sub>H")
>>> mol.GetAtomWithIdx(3).SetProp("_displayLabelW","HO<sub>2</sub>C")
>>> mol.GetAtomWithIdx(7).SetProp("_displayLabel","CO<sub>2</sub><sup>-</sup>")
>>> mol.GetAtomWithIdx(7).SetProp("_displayLabelW","<sup>-</sup>OOC")
>>> d = rdMolDraw2D.MolDraw2DCairo(250, 250)
>>> rdMolDraw2D.PrepareAndDrawMolecule(d,mol)
>>> d.WriteDrawingText("./images/atom_labels_3.png")
```

this gives:


## Substructure Searching

Substructure matching can be done using query molecules built from SMARTS:

```pycon
>>> m = Chem.MolFromSmiles('c1ccccc1O')
>>> patt = Chem.MolFromSmarts('ccO')
>>> m.HasSubstructMatch(patt)
True
>>> m.GetSubstructMatch(patt)
(0, 5, 6)
```

Those are the atom indices in `m`, ordered as `patt`’s atoms. To get all of the matches:

```pycon
>>> m.GetSubstructMatches(patt)
((0, 5, 6), (4, 5, 6))
```

This can be used to easily filter lists of molecules:

```pycon
>>> patt = Chem.MolFromSmarts('c[NH1]')
>>> matches = []
>>> with Chem.SDMolSupplier('data/actives_5ht3.sdf') as suppl:
...   for mol in suppl:
...     if mol.HasSubstructMatch(patt):
...       matches.append(mol)
>>> len(matches)
22
```

We can write the same thing more compactly using Python’s list comprehension syntax:

```pycon
>>> with Chem.SDMolSupplier('data/actives_5ht3.sdf') as suppl:
...   matches = [x for x in suppl if x.HasSubstructMatch(patt)]
>>> len(matches)
22
```

Substructure matching can also be done using molecules built from SMILES instead of SMARTS:

```pycon
>>> m = Chem.MolFromSmiles('C1=CC=CC=C1OC')
>>> m.HasSubstructMatch(Chem.MolFromSmarts('CO'))
True
>>> m.HasSubstructMatch(Chem.MolFromSmiles('CO'))
True
```

But don’t forget that the semantics of the two languages are not exactly equivalent:

```pycon
>>> m.HasSubstructMatch(Chem.MolFromSmiles('COC'))
True
>>> m.HasSubstructMatch(Chem.MolFromSmarts('COC'))
False
>>> m.HasSubstructMatch(Chem.MolFromSmarts('COc')) #<- need an aromatic C
True
```

### Stereochemistry in substructure matches

By default information about stereochemistry is not used in substructure searches:

```pycon
>>> m = Chem.MolFromSmiles('CC[C@H](F)Cl')
>>> m.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl'))
True
>>> m.HasSubstructMatch(Chem.MolFromSmiles('C[C@@H](F)Cl'))
True
>>> m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl'))
True
```

But this can be changed via the *useChirality* argument:

```pycon
>>> m.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl'),useChirality=True)
True
>>> m.HasSubstructMatch(Chem.MolFromSmiles('C[C@@H](F)Cl'),useChirality=True)
False
>>> m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl'),useChirality=True)
True
```

Notice that when *useChirality* is set a non-chiral query **does** match a chiral molecule. The same is not true for a chiral query and a non-chiral molecule:

```pycon
>>> m.HasSubstructMatch(Chem.MolFromSmiles('CC(F)Cl'))
True
>>> m2 = Chem.MolFromSmiles('CCC(F)Cl')
>>> m2.HasSubstructMatch(Chem.MolFromSmiles('C[C@H](F)Cl'),useChirality=True)
False
```

### Atom Map Indices in SMARTS

It is possible to attach indices to the atoms in the SMARTS pattern. This is most often done in reaction SMARTS (see Chemical Reactions), but is more general than that. For example, in the SMARTS patterns for torsion angle analysis published by Guba *et al.* (`DOI: acs.jcim.5b00522`) indices are used to define the four atoms of the torsion of interest. This allows additional atoms to be used to define the environment of the four torsion atoms, as in `[cH0:1][c:2]([cH0])!@[CX3!r:3]=[NX2!r:4]` for an aromatic C=N torsion. We might wonder in passing why they didn’t use recursive SMARTS for this, which would have made life easier, but it is what it is. The atom lists from `GetSubstructureMatches` are guaranteed to be in order of the SMARTS, but in this case we’ll get five atoms so we need a way of picking out, in the correct order, the four of interest. When the SMARTS is parsed, the relevant atoms are assigned an atom map number property that we can easily extract:

```pycon
>>> qmol = Chem.MolFromSmarts( '[cH0:1][c:2]([cH0])!@[CX3!r:3]=[NX2!r:4]' )
>>> ind_map = {}
>>> for atom in qmol.GetAtoms() :
...     map_num = atom.GetAtomMapNum()
...     if map_num:
...         ind_map[map_num-1] = atom.GetIdx()
>>> ind_map
{0: 0, 1: 1, 2: 3, 3: 4}
>>> map_list = [ind_map[x] for x in sorted(ind_map)]
>>> map_list
[0, 1, 3, 4]
```

Then, when using the query on a molecule you can get the indices of the four matching atoms like this:

```pycon
>>> mol = Chem.MolFromSmiles('Cc1cccc(C)c1C(C)=NC')
>>> for match in mol.GetSubstructMatches( qmol ) :
...     mas = [match[x] for x in map_list]
...     print(mas)
[1, 7, 8, 10]
```

### Advanced substructure matching

Starting with the 2020.03 release, the RDKit allows you to provide an optional function that is used to check whether or not a possible substructure match should be accepted. This function is called with the molecule to be matched and the indices of the matching atoms.

Here’s an example of how you can use the functionality to do “Markush-like” matching, requiring that all atoms in a sidechain are either carbon (type “all_carbon”) or aren’t aromatic (type “alkyl”). We start by defining the class that we’ll use to test the sidechains:

```python
from rdkit import Chem

class SidechainChecker(object):
  matchers = {
    'alkyl': lambda at: not at.GetIsAromatic(),
    'all_carbon': lambda at: at.GetAtomicNum() == 6
  }

  def __init__(self, query, pName="queryType"):
    # identify the atoms that have the properties we care about
    self._atsToExamine = [(x.GetIdx(), x.GetProp(pName)) for x in query.GetAtoms()
                          if x.HasProp(pName)]
    self._pName = pName

  def __call__(self, mol, vect):
    seen = [0] * mol.GetNumAtoms()
    for idx in vect:
      seen[idx] = 1
    # loop over the atoms we care about:
    for idx, qtyp in self._atsToExamine:
      midx = vect[idx]
      stack = [midx]
      atom = mol.GetAtomWithIdx(midx)
      # now do a breadth-first search from that atom, checking
      # all of its neighbors that aren't in the substructure
      # query:
      stack = [atom]
      while stack:
        atom = stack.pop(0)
        if not self.matchers[qtyp](atom):
          return False
        seen[atom.GetIdx()] = 1
        for nbr in atom.GetNeighbors():
          if not seen[nbr.GetIdx()]:
            stack.append(nbr)
    return True
```

Here’s the molecule we’ll use:

And the default behavior:

```pycon
>>> m = Chem.MolFromSmiles('C2NCC2CC1C(CCCC)C(OCCCC)C1c2ccccc2')
>>> p = Chem.MolFromSmarts('C1CCC1*')
>>> p.GetAtomWithIdx(4).SetProp("queryType", "all_carbon")
>>> m.GetSubstructMatches(p)
((5, 6, 11, 17, 18), (5, 17, 11, 6, 7), (6, 5, 17, 11, 12), (6, 11, 17, 5, 4))
```

Now let’s add the final check to filter the results:

```pycon
>>> params = Chem.SubstructMatchParameters()
>>> checker = SidechainChecker(p)
>>> params.setExtraFinalCheck(checker)
>>> m.GetSubstructMatches(p,params)
((5, 6, 11, 17, 18), (5, 17, 11, 6, 7))
```

Repeat that using the ‘alkyl’ query:

```pycon
>>> p.GetAtomWithIdx(4).SetProp("queryType", "alkyl")
>>> checker = SidechainChecker(p)
>>> params.setExtraFinalCheck(checker)
>>> m.GetSubstructMatches(p,params)
((5, 17, 11, 6, 7), (6, 5, 17, 11, 12), (6, 11, 17, 5, 4))
```


## Chemical Transformations

The RDKit contains a number of functions for modifying molecules. Note that these transformation functions are intended to provide an easy way to make simple modifications to molecules. For more complex transformations, use the Chemical Reactions functionality.

### Substructure-based transformations

There’s a variety of functionality for using the RDKit’s substructure-matching machinery for doing quick molecular transformations. These transformations include deleting substructures:

```pycon
>>> m = Chem.MolFromSmiles('CC(=O)O')
>>> patt = Chem.MolFromSmarts('C(=O)[OH]')
>>> rm = AllChem.DeleteSubstructs(m,patt)
>>> Chem.MolToSmiles(rm)
'C'
```

replacing substructures:

```pycon
>>> repl = Chem.MolFromSmiles('OC')
>>> patt = Chem.MolFromSmarts('[$(NC(=O))]')
>>> m = Chem.MolFromSmiles('CC(=O)N')
>>> rms = AllChem.ReplaceSubstructs(m,patt,repl)
>>> rms
(<rdkit.Chem.rdchem.Mol object at 0x...>,)
>>> Chem.MolToSmiles(rms[0])
'COC(C)=O'
```

as well as simple SAR-table transformations like removing side chains:

```pycon
>>> m1 = Chem.MolFromSmiles('BrCCc1cncnc1C(=O)O')
>>> core = Chem.MolFromSmiles('c1cncnc1')
>>> tmp = Chem.ReplaceSidechains(m1,core)
>>> Chem.MolToSmiles(tmp)
'[1*]c1cncnc1[2*]'
```

and removing cores:

```pycon
>>> tmp = Chem.ReplaceCore(m1,core)
>>> Chem.MolToSmiles(tmp)
'[1*]CCBr.[2*]C(=O)O'
```

By default the sidechains are labeled based on the order they are found. They can also be labeled according by the number of that core-atom they’re attached to:

```pycon
>>> m1 = Chem.MolFromSmiles('c1c(CCO)ncnc1C(=O)O')
>>> tmp=Chem.ReplaceCore(m1,core,labelByIndex=True)
>>> Chem.MolToSmiles(tmp)
'[1*]CCO.[5*]C(=O)O'
```

`rdkit.Chem.rdmolops.ReplaceCore()` returns the sidechains in a single molecule. This can be split into separate molecules using `rdkit.Chem.rdmolops.GetMolFrags()` :

```pycon
>>> rs = Chem.GetMolFrags(tmp,asMols=True)
>>> len(rs)
2
>>> Chem.MolToSmiles(rs[0])
'[1*]CCO'
>>> Chem.MolToSmiles(rs[1])
'[5*]C(=O)O'
```

### Murcko Decomposition

The RDKit provides standard Murcko-type decomposition [7] of molecules into scaffolds:

```pycon
>>> from rdkit.Chem.Scaffolds import MurckoScaffold
>>> with Chem.SDMolSupplier('data/cdk2.sdf') as cdk2mols:
...   m1 = cdk2mols[0]
>>> core = MurckoScaffold.GetScaffoldForMol(m1)
>>> Chem.MolToSmiles(core)
'c1ncc2nc[nH]c2n1'
```

or into a generic framework:

```pycon
>>> fw = MurckoScaffold.MakeScaffoldGeneric(core)
>>> Chem.MolToSmiles(fw)
'C1CCC2CCCC2C1'
```
