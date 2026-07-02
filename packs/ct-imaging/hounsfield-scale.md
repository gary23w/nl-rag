---
title: "Hounsfield scale"
source: https://en.wikipedia.org/wiki/Hounsfield_scale
domain: ct-imaging
license: CC-BY-SA-4.0
tags: computed tomography, ct scan, hounsfield unit, filtered back projection
fetched: 2026-07-02
---

# Hounsfield scale

The **Hounsfield scale** (/ˈhaʊnzfiːld/ *HOWNZ-feeld*), named after Sir Godfrey Hounsfield, is a quantitative scale for describing radiodensity. It is frequently used in CT scans, where its value is also termed **CT number**.

## Definition

The Hounsfield unit (HU) scale is a linear transformation of the original linear attenuation coefficient measurement into one in which the radiodensity of distilled water at standard pressure and temperature (STP) is defined as 0 Hounsfield units (HU), while the radiodensity of air at STP is defined as −1000 HU. In a voxel with average linear attenuation coefficient $\mu$ , the corresponding HU value is therefore given by:

$HU=1000\times {\frac {\mu -\mu _{\textrm {water}}}{\mu _{\textrm {water}}-\mu _{\textrm {air}}}}$

where $\mu _{\textrm {water}}$ and $\mu _{\textrm {air}}$ are respectively the linear attenuation coefficients of water and air.

Thus, a change of one Hounsfield unit (HU) represents a change of 0.1% of the attenuation coefficient of water since the attenuation coefficient of air is nearly zero.

Calibration tests of HU with reference to water and other materials may be done to ensure standardised response. This is particularly important for CT scans used in radiotherapy treatment planning, where HU is converted to electron density. Variation in the measured values of reference materials with known composition, and variation between and within slices may be used as part of test procedures.

### Rationale

The above standards were chosen originally to encode the radiodensity of organic tissues relative to water for 12-bit processing on clinical CT scanners. A 12-bit encoding corresponds to 4096 ( $2^{12}$ ) values, where the range (–1024 to 3071) encompasses HU values for air, soft tissue and bone.

## Values for different body tissues and material

HU-based differentiation of material applies to medical-grade dual-energy CT scans but not to cone beam computed tomography (CBCT) scans, as CBCT scans provide unreliable HU readings.

Values reported here are **approximations**. Different dynamics are reported from one study to another.

Exact HU dynamics can vary from one CT acquisition to another due to CT acquisition and reconstruction parameters (kV, filters, reconstruction algorithms, etc.). The use of contrast agents modifies HU as well in some body parts (mainly blood).

| Substance | HU |   |
|---|---|---|
| Air | −1000 |   |
| Fat | −120 to −90 |   |
| Soft tissue on contrast CT | +100 to +300 |   |
| Bone | Cancellous | +300 to +400 |
| Cortical | +500 to +1900 |   |
| Subdural hematoma | First hours | +75 to +100 |
| After 3 days | +65 to +85 |   |
| After 10–14 days | +35 to +40 |   |
| Other blood | Unclotted | +13 to +50 |
| Clotted | +50 to +75 |   |
| Pleural effusion | Transudate | +2 to +15 |
| Exudate | +4 to +33 |   |
| Other fluids | Chyle | −30 |
| Water | 0 |   |
| Urine | −5 to +15 |   |
| Bile | −5 to +15 |   |
| CSF | +15 |   |
| Abscess / Pus | 0 or +20, to +40 or +45 |   |
| Mucus | 0 - 130 ("high attenuating" at over 70 HU) |   |
| Parenchyma | Lung | −700 to −600 |
| Kidney | +20 to +45 |   |
| Liver | 60 ± 6 |   |
| Lymph nodes | +10 to +20 |   |
| Muscle | +35 to +55 |   |
| Thymus | +20 to +40 in children +20 to +120 in adolescents |   |
| White matter | +20 to +30 |   |
| Grey matter | +37 to +45 |   |
| Gallstone | Cholesterol stone | +30 to +100 |
| Bilirubin stone | +90 to +120 |   |
| Foreign body | Windowpane glass | +500 |
| Aluminum, tarmac, car window glass, bottle glass, and other rocks | +2,100 to +2,300 |   |
| Limestone | +2,800 |   |
| Copper | +14,000 |   |
| Silver | +17,000 |   |
| Steel | +20,000 |   |
| Gold, steel, and brass | +30,000 (upper measurable limit) |   |
| Earwax | <0 |   |

A practical application of this is in evaluation of tumors, where, for example, an adrenal tumor with a radiodensity of less than 10 HU is rather fatty in composition and almost certainly a benign adrenal adenoma.
