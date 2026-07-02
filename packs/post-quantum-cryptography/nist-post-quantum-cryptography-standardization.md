---
title: "NIST Post-Quantum Cryptography Standardization"
source: https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization
domain: post-quantum-cryptography
license: CC-BY-SA-4.0
tags: post quantum cryptography, quantum resistant algorithm, shor algorithm threat, nist pqc standardization, quantum safe encryption
fetched: 2026-07-02
---

# NIST Post-Quantum Cryptography Standardization

**Post-Quantum Cryptography Standardization** is a program and competition by NIST to update their standards to include post-quantum cryptography. It was announced at PQCrypto 2016. Twenty-three signature schemes and fifty-nine encryption/KEM schemes were submitted by the initial submission deadline at the end of 2017 of which sixty-nine total were deemed complete and proper and participated in the first round. Seven of these, of which three are signature schemes, advanced to the third round, which was announced in July 2020.

On August 13, 2024, NIST released final versions of the first three Post Quantum Crypto Standards: FIPS 203, FIPS 204, and FIPS 205.

## Background

Academic research on the potential impact of quantum computing dates back to at least 2001. A NIST published report from April 2016 cites experts that acknowledge the possibility of quantum technology to render the commonly used RSA algorithm insecure by 2030. As a result, a need to standardize quantum-secure cryptographic primitives was pursued. Since most symmetric primitives are relatively easy to modify in a way that makes them quantum resistant, efforts have focused on public-key cryptography, namely digital signatures and key encapsulation mechanisms. In December 2016 NIST initiated a standardization process by announcing a call for proposals.

## Round one

Under consideration were: (strikethrough means it had been withdrawn)

| Type | PKE/KEM | Signature | Signature & PKE/KEM |
|---|---|---|---|
| Lattice | Compact LWE CRYSTALS-Kyber Ding Key Exchange EMBLEM and R.EMBLEM FrodoKEM HILA5 (withdrawn and merged into Round5) KCL (pka OKCN/AKCN/CNKE) KINDI LAC LIMA Lizard LOTUS NewHope NTRUEncrypt NTRU-HRSS-KEM NTRU Prime Odd Manhattan Round2 (withdrawn and merged into Round5) Round5 (merger of Round2 and Hila5, announced 4 August 2018) SABER Three Bears Titanium | CRYSTALS-Dilithium DRS FALCON pqNTRUSign qTESLA |   |
| Code-based | BIG QUAKE BIKE Classic McEliece + NTS-KEM DAGS Edon-K HQC LAKE (withdrawn and merged into ROLLO) LEDAkem LEDApkc Lepton LOCKER (withdrawn and merged into ROLLO) McNie NTS-KEM ROLLO (merger of Ouroboros-R, LAKE and LOCKER) Ouroboros-R (withdrawn and merged into ROLLO) QC-MDPC KEM Ramstake RLCE-KEM RQC | pqsigRM RaCoSS RankSign |   |
| Hash-based |   | Gravity-SPHINCS SPHINCS+ |   |
| Multivariate | CFPKM Giophantus | DualModeMS GeMSS Gui HiMQ-3 LUOV MQDSS Rainbow | SRTPI DME |
| Braid group |   | WalnutDSA |   |
| Supersingular elliptic curve isogeny | SIKE |   |   |
| Satirical submission |   |   | pqRSA |
| Other | Guess Again HK17 Mersenne-756839 RVB | Picnic |   |

### Round one submissions published attacks

- Guess Again by Lorenz Panny
- RVB by Lorenz Panny
- RaCoSS by Daniel J. Bernstein, Andreas Hülsing, Tanja Lange and Lorenz Panny
- HK17 by Daniel J. Bernstein and Tanja Lange
- SRTPI by Bo-Yin Yang
- WalnutDSA
  - by Ward Beullens and Simon R. Blackburn
  - by Matvei Kotov, Anton Menshov and Alexander Ushakov
- DRS by Yang Yu and Léo Ducas
- DAGS by Elise Barelli and Alain Couvreur
- Edon-K by Matthieu Lequesne and Jean-Pierre Tillich
- RLCE by Alain Couvreur, Matthieu Lequesne, and Jean-Pierre Tillich
- Hila5 by Daniel J. Bernstein, Leon Groot Bruinderink, Tanja Lange and Lorenz Panny
- Giophantus by Ward Beullens, Wouter Castryck and Frederik Vercauteren
- RankSign by Thomas Debris-Alazard and Jean-Pierre Tillich
- McNie by Philippe Gaborit; Terry Shue Chien Lau and Chik How Tan

## Round two

Candidates moving on to the second round were announced on January 30, 2019. They are:

| Type | PKE/KEM | Signature |
|---|---|---|
| Lattice | CRYSTALS-Kyber FrodoKEM LAC NewHope NTRU (merger of NTRUEncrypt and NTRU-HRSS-KEM) NTRU Prime Round5 (merger of Round2 and Hila5, announced 4 August 2018) SABER Three Bears | CRYSTALS-Dilithium FALCON qTESLA |
| Code-based | BIKE Classic McEliece HQC LEDAcrypt (merger of LEDAkem and LEDApkc) NTS-KEM ROLLO (merger of Ouroboros-R, LAKE and LOCKER) RQC |   |
| Hash-based |   | SPHINCS+ |
| Multivariate |   | GeMSS LUOV MQDSS Rainbow |
| Supersingular elliptic curve isogeny | SIKE |   |
| Zero-knowledge proofs |   | Picnic |

## Round three

On July 22, 2020, NIST announced seven finalists ("first track"), as well as eight alternate algorithms ("second track"). The first track contains the algorithms which appear to have the most promise, and will be considered for standardization at the end of the third round. Algorithms in the second track could still become part of the standard, after the third round ends. NIST expects some of the alternate candidates to be considered in a fourth round. NIST also suggests it may re-open the signature category for new schemes proposals in the future.

On June 7–9, 2021, NIST conducted the third PQC standardization conference, virtually. The conference included candidates' updates and discussions on implementations, on performances, and on security issues of the candidates. A small amount of focus was spent on intellectual property concerns.

### Finalists

| Type | PKE/KEM | Signature |
|---|---|---|
| Lattice | CRYSTALS-Kyber NTRU SABER | CRYSTALS-Dilithium FALCON |
| Code-based | Classic McEliece |   |
| Multivariate |   | Rainbow |

### Alternate candidates

| Type | PKE/KEM | Signature |
|---|---|---|
| Lattice | FrodoKEM NTRU Prime |   |
| Code-based | BIKE HQC |   |
| Hash-based |   | SPHINCS+ |
| Multivariate |   | GeMSS |
| Supersingular elliptic curve isogeny | SIKE |   |
| Zero-knowledge proofs |   | Picnic |

### Intellectual property concerns

After NIST's announcement regarding the finalists and the alternate candidates, various intellectual property concerns were voiced, notably surrounding lattice-based schemes such as Kyber and NewHope. NIST holds signed statements from submitting groups clearing any legal claims, but there is still a concern that third parties could raise claims. NIST claims that they will take such considerations into account while picking the winning algorithms.

### Round three submissions published attacks

- Rainbow: by Ward Beullens on a classical computer

### Adaptations

During this round, some candidates have shown to be vulnerable to some attack vectors. It forces these candidates to adapt accordingly:

**CRYSTAL-Kyber and SABER**

may change the nested hashes used in their proposals in order for their security claims to hold.

**FALCON**

side channel attack using electromagnetic measurements to extract the secret signing keys. A masking may be added in order to resist the attack. This adaptation affects performance and should be considered whilst standardizing.

### Selected Algorithms 2022

On July 5, 2022, NIST announced the first group of winners from its six-year competition.

| Type | PKE/KEM | Signature |
|---|---|---|
| Lattice | CRYSTALS-Kyber | CRYSTALS-Dilithium FALCON |
| Hash-based |   | SPHINCS+ |

## Round four

On July 5, 2022, NIST announced four candidates for PQC Standardization Round 4.

| Type | PKE/KEM |
|---|---|
| Code-based | BIKE Classic McEliece HQC |
| Supersingular elliptic curve isogeny | SIKE (Broken August 5, 2022) |

### Round four submissions published attacks

- SIKE: by Wouter Castryck and Thomas Decru on a classical computer

### Selected Algorithm 2025

On March 11, 2025, NIST announced the selection of a backup algorithm for KEM.

| Type | PKE/KEM |
|---|---|
| Code-based | HQC |

## First release

On August 13, 2024, NIST released final versions of its first three Post Quantum Crypto Standards. According to the release announcement:

> While there have been no substantive changes made to the standards since the draft versions, NIST has changed the algorithms’ names to specify the versions that appear in the three finalized standards, which are:
> 
> - Federal Information Processing Standard (FIPS) 203, intended as the primary standard for general encryption. Among its advantages are comparatively small encryption keys that two parties can exchange easily, as well as its speed of operation. The standard is based on the CRYSTALS-Kyber algorithm, which has been renamed ML-KEM, short for Module-Lattice-Based Key-Encapsulation Mechanism.
> - FIPS 204, intended as the primary standard for protecting digital signatures. The standard uses the CRYSTALS-Dilithium algorithm, which has been renamed ML-DSA, short for Module-Lattice-Based Digital Signature Algorithm.
> - FIPS 205, also designed for digital signatures. The standard employs the SPHINCS+ algorithm, which has been renamed SLH-DSA, short for Stateless Hash-Based Digital Signature Algorithm. The standard is based on a different math approach than ML-DSA, and it is intended as a backup method in case ML-DSA proves vulnerable.
> - Similarly, when the draft FIPS 206 standard built around FALCON is released, the algorithm will be dubbed FN-DSA, short for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm.

On March 11, 2025 NIST released Hamming Quasi-Cyclic (HQC) as the fifth algorithm for post-quantum asymmetric encryption as used for key encapsulation / exchange. The new algorithm is as a backup for ML-KEM, the main algorithm for general encryption. HQC is a code-based scheme using different math than ML-KEM, thus mitigating possible weaknesses should any be found in the lattice-based ML-KEM. The draft standard incorporating the HQC algorithm is expected in early 2026 with the final in 2027.

## Additional Digital Signature Schemes

### Round One

NIST received 50 submissions and deemed 40 to be complete and proper according to the submission requirements. Under consideration are: (strikethrough means it has been withdrawn)

| Type | Signature |
|---|---|
| Lattice | EagleSign EHTv3 and EHTv4 HAETAE HAWK HuFu Raccoon SQUIRRELS |
| Code-based | CROSS Enhanced pqsigRM FuLeeca LESS MEDS Wave |
| MPC-in-the-Head | MIRA MiRitH MQOM PERK RYDE SDitH |
| Multivariate | 3WISE ("the submitter agrees that the scheme is insecure, but prefers to not withdraw in the hope that studying the scheme will advance cryptanalysis") Biscuit DME-Sign ("Our first impression is that the attack works and we are checking the details of the attack .We are implementing a variant of the DME that may resist the attack but we have to verify it.") HPPC MAYO PROV QR-UOV SNOVA TUOV UOV VOX |
| Supersingular elliptic curve isogeny | SQIsign |
| Symmetric-based | AIMer Ascon-Sign FAEST SPHINCS-alpha |
| Other | ALTEQ eMLE-Sig 2.0 KAZ-SIGN Preon Xifrat1-Sign.I |

### Round one submissions published attacks

- 3WISE by Daniel Smith-Tone
- EagleSign by Mehdi Tibouchi
- KAZ-SIGN by Daniel J. Bernstein; Scott Fluhrer
- Xifrat1-Sign.I by Lorenz Panny
- eMLE-Sig 2.0 by Mehdi Tibouchi (implementation by Lorenz Panny)
- HPPC by Ward Beullens; Pierre Briaud, Maxime Bros, and Ray Perlner
- ALTEQ by Markku-Juhani O. Saarinen (implementation only?)
- Biscuit by Charles Bouillaguet
- MEDS by Markku-Juhani O. Saarinen and Ward Beullens (implementation only)
- FuLeeca by Felicitas Hörmann and Wessel van Woerden
- LESS by the LESS team (implementation only)
- DME-Sign by Markku-Juhani O. Saarinen (implementation only?); Pierre Briaud, Maxime Bros, Ray Perlner, and Daniel Smith-Tone
- EHTv3 by Eamonn Postlethwaite and Wessel van Woerden; Keegan Ryan and Adam Suhl
- Enhanced pqsigRM by Thomas Debris-Alazard, Pierre Loisel and Valentin Vasseur; Pierre Briaud, Maxime Bros, Ray Perlner and Daniel Smith-Tone
- HAETAE by Markku-Juhani O. Saarinen (implementation only?)
- HuFu by Markku-Juhani O. Saarinen
- SDitH by Kevin Carrier and Jean-Pierre Tillich; Kevin Carrier, Valérian Hatey, and Jean-Pierre Tillich
- VOX by Hiroki Furue and Yasuhiko Ikematsu
- AIMer by Fukang Liu, Mohammad Mahzoun, Morten Øygarden, Willi Meier
- SNOVA by Yasuhiko Ikematsu and Rika Akiyama
- PROV by Ludovic Perret, and River Moreira Ferreira (implementation only)

### Round Two

NIST deemed 14 submissions to pass to the second round.

| Type | Signature | Technique(s) Used | Hard Problem |
|---|---|---|---|
| Lattice | HAWK | Hash-and-sign | lattice problems |
| Code-based | CROSS | Fiat–Shamir heuristic | Syndrome Decoding Problem |
| LESS | Fiat–Shamir heuristic | Linear Equivalence Problem |   |
| MPC-in-the-Head | Mirath (merge of MIRA and MiRitH) | "in the head", Fiat–Shamir heuristic | MinRank (matrix-based) |
| MQOM | "in the head", Fiat–Shamir heuristic | Multivariable Quadratic Problem |   |
| PERK | "in the head", Fiat–Shamir heuristic | Permuted Kernel Problem (matrix-based) |   |
| RYDE | "in the head", Fiat–Shamir heuristic | Rank Syndrome Decoding Problem (code-based) |   |
| SDitH | "in the head", Fiat–Shamir heuristic | Syndrome Decoding Problem (code-based) |   |
| Multivariate | MAYO | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |
| QR-UOV | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| SNOVA | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| UOV | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| Supersingular elliptic curve isogeny | SQIsign | Fiat–Shamir heuristic | Endomorphism Ring Problem |
| Symmetric-based | FAEST | "in the head", Fiat–Shamir heuristic | breaking AES |

### Round Three

Nine candidates advanced from Round Two to Round Three:

| Type | Signature | Technique(s) Used | Hard Problem |
|---|---|---|---|
| Lattice | HAWK | Hash-and-sign | lattice problems |
| MPC-in-the-Head | MQOM | "in the head", Fiat–Shamir heuristic | Multivariable Quadratic Problem |
| SDitH | "in the head", Fiat–Shamir heuristic | Syndrome Decoding Problem (code-based) |   |
| FAEST | "in the head", Fiat–Shamir heuristic | breaking AES |   |
| Multivariate | MAYO | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |
| QR-UOV | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| SNOVA | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| UOV | Unbalanced Oil and Vinegar | Multivariable Quadratic Problem |   |
| Supersingular elliptic curve isogeny | SQIsign | Fiat–Shamir heuristic | Endomorphism Ring Problem |

NIST has indicated that at least the multivariate candidates will probably require a further round of evaluation.
