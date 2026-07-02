---
title: "Computerized physician order entry"
source: https://en.wikipedia.org/wiki/Computerized_physician_order_entry
domain: clinical-decision-support
license: CC-BY-SA-4.0
tags: clinical decision support, diagnostic decision, medical expert system, clinical guideline
fetched: 2026-07-02
---

# Computerized physician order entry

**Computerized physician order entry** (**CPOE**), sometimes referred to as **computerized provider order entry** or **computerized provider order management** (**CPOM**), is a process of electronic entry of medical practitioner instructions for the treatment of patients (particularly hospitalized patients) under his or her care.

The entered orders are communicated over a computer network to the medical staff or to the departments (pharmacy, laboratory, or radiology) responsible for fulfilling the order. CPOE reduces the time it takes to distribute and complete orders, while increasing efficiency by reducing transcription errors including preventing duplicate order entry, while simplifying inventory management and billing.

CPOE is a form of patient management software.

## Required data

In a graphical representation of an order sequence, specific data should be presented to CPOE system staff in cleartext, including:

- identity of the patient
- role of required member of staff
- resources, materials and medication applied
- procedures to be performed
- operational sequence to be obeyed
- feedback to be noted
- case specific documentation to build

Some textual data can be reduced to simple graphics.

CPOE systems use terminology familiar to medical and nursing staff, but there are different terms used to classify and concatenate orders. The following items are examples of additional terminology that a CPOE system programmer might need to know:

### Filler

The application responding to, *i.e.*, performing, a request for services (orders) or producing an observation. The filler can also originate requests for services (new orders), add additional services to existing orders, replace existing orders, put an order on hold, discontinue an order, release a held order, or cancel existing orders.

### Order

A request for a service from one application to a second application. In some cases an application is allowed to place orders with itself.

### Order detail segment

One of several segments that can carry order information. Future ancillary specific segments may be defined in subsequent releases of the Standard if they become necessary.

### Placer

The application or individual originating a request for services (order).

### Placer order group

A list of associated orders coming from a single location regarding a single patient.

### Order Set

A grouping of orders used to standardize and expedite the ordering process for a common clinical scenario. (Typically, these orders are started, modified, and stopped by a licensed physician.)

### Protocol

A grouping of orders used to standardize and automate a clinical process on behalf of a physician. (Typically, these orders are started, modified, and stopped by a nurse, pharmacist, or other licensed health professional.)

## Features of CPOE systems

Common features of CPOE systems include the following:

**Ordering**

Physician orders can be standardized across the organization, and may be individualized for each prescriber or specialty through the use of order sets for common clinical scenarios.

Orders are communicated electronically to all departments and caregivers involved in carrying them out, which can improve response time and reduce conflicts with existing orders.

**Patient-centered decision support**

The ordering process is typically integrated with

clinical decision support systems

(CDSS) that can display the patient's medical history, current results, and evidence-based

clinical guidelines

to support treatment decisions.

Some implementations use a

medical logic module

and/or

Arden syntax

to integrate decision logic with the order-entry interface.

**Patient safety features**

CPOE systems can provide allergy alerts, drug–drug, drug–food and drug–disease interaction checks, safe-dose-range checking, and review of orders for conflicts with other tests or treatments.

**Intuitive Human interface**

The order-entry workflow is generally designed to resemble familiar paper-based ordering forms, with the aim of making the system usable by new or infrequent users.

**Regulatory compliance and security**

Access is authenticated and a permanent audit record of orders is created, supported by

electronic signature

.

**Portability**

Orders can be entered and managed at the point of care from a range of locations and devices, including workstations, laptops and

tablet computers

.

**Management**

Statistical reports allow managers to analyze census, staffing and inventory utilization, and to perform

root cause analysis

for patient-safety events.

**Billing**

Orders can be linked to diagnosis codes (such as

ICD-9-CM

or

ICD-10-CM

) at the time of entry to support charge capture.

## Patient safety benefits

Physicians have traditionally hand-written or verbally communicated orders for patient care, which are then transcribed by various individuals (such as unit clerks, nurses, and ancillary staff) before being carried out. Handwritten reports or notes, manual order entry, non-standard abbreviations and poor legibility can lead to errors and injuries to patients. A follow-up report from the Institute of Medicine (IOM) in 2001 advised use of electronic medication ordering, with computer- and internet-based information systems to support clinical decisions. Prescribing errors are the largest identified source of preventable hospital medical error, and a 2006 report by the IOM estimated that a hospitalized patient is exposed to a medication error each day of his or her stay.

Studies have estimated that CPOE implementation at all nonrural hospitals in the United States could prevent over 500,000 serious medication errors each year. Other studies of CPOE have yielded evidence suggesting that the medication error rate can be reduced by approximately 80%, and that errors with potential for serious harm or death can be reduced by 55%. Subsequent research has also reported mortality benefits.

A 2005 report from the Centers for Medicare & Medicaid Services and the Centers for Disease Control and Prevention found that only 41 percent of prophylactic antibacterials were correctly stopped within 24 hours of completed surgery. In a subsequent eight-month evaluation, an intervention hospital that implemented a CPOE workflow designed to discontinue prophylactic antibacterials saw timely discontinuation rise from 38.8 percent of surgeries to 55.7 percent.

CPOE and e-prescribing systems can also provide automatic dose-range alerts and drug-interaction checking. Specialists in pharmacy informatics work with medical and nursing staff to apply these capabilities to medication use within the hospital.

## Advantages

Compared with paper-based ordering, CPOE produces legible, complete and standardized orders, eliminates several manual transcription steps, and routes orders electronically to the pharmacy, laboratory, radiology, and other ancillary departments responsible for carrying them out. An efficiency study published as part of the Agency for Healthcare Research and Quality's *Advances in Patient Safety* series reported that CPOE reduced or eliminated the need to locate paper charts, the incidence of orders being overlooked by nursing or clerical staff, requests for order clarification arising from illegibility or poor fax quality, and the need to manually re-enter data into downstream departmental systems.

The use of standardized order sets allows institutions to encode evidence-based clinical pathways and present the appropriate orders to clinicians at the point of entry, reducing variation in care for common conditions and shortening the time required to enter routine admission, transfer or discharge orders. Because each order is captured in structured electronic form, the same data can simultaneously support clinical documentation, inventory tracking and billing without separate manual re-entry.

Realizing these advantages depends on adequate training, on careful design of the order-entry workflow, and on sustained organizational commitment to maintaining order sets and decision-support content after the initial deployment.

## Risks

CPOE can introduce new types of errors not present in paper-based ordering. A 2005 observational study at one academic hospital identified 22 categories of medication-error risk associated with a widely used CPOE system, including inflexible ordering formats, fragmented displays that obscured the patient's full medication list, and default selections that could result in dosing errors. Automation can also create a false sense of security, in which clinicians assume that orders accepted by the system have been verified for clinical appropriateness.

A 2005 study at the Children's Hospital of Pittsburgh reported an unexpected increase in mortality in the pediatric intensive care unit following the introduction of a commercially sold CPOE system; the authors attributed the increase primarily to workflow changes during the admission of critically ill patients, including delays in initiating treatment and reduced bedside presence of clinicians. In other settings, shortcut or default selections in the order interface can override non-standard medication regimens — for example for elderly or underweight patients — resulting in toxic doses.

Frequent alerts and warnings during order entry can interrupt workflow, leading to messages being ignored or overridden through alert fatigue. CPOE and automated drug dispensing were identified as a cause of error by 84% of over 500 health care facilities participating in a surveillance system operated by the United States Pharmacopoeia. Introducing CPOE into a complex medical environment requires ongoing design changes to accommodate unique patients and care settings, close monitoring of automatic overrides, and continuing training of all users.

## Implementation

CPOE systems can take years to install and configure. Despite ample evidence of the potential to reduce medication errors, adoption of this technology by doctors and hospitals in the United States has been slowed by resistance to changes in physician's practice patterns, costs and training time involved, and concern with interoperability and compliance with future national standards. According to a study by RAND Health, the US healthcare system could save more than 81 billion dollars annually, reduce adverse medical events and improve the quality of care if it were to widely adopt CPOE and other health information technology. As more hospitals become aware of the financial benefits of CPOE, and more physicians with a familiarity with computers enter practice, increased use of CPOE is predicted. Several high-profile failures of CPOE implementation have occurred, so a major effort must be focused on change management, including restructuring workflows, dealing with physicians' resistance to change, and creating a collaborative environment.

An early success with CPOE by the United States Department of Veterans Affairs (VA) is the Veterans Health Information Systems and Technology Architecture or VistA. A graphical user interface known as the Computerized Patient Record System (CPRS) allows health care providers to review and update a patient's record at any computer in the VA's over 1,000 healthcare facilities. CPRS includes the ability to place orders by CPOE, including medications, special procedures, x-rays, patient care nursing orders, diets and laboratory tests.

The world's first successful implementation of a CPOE system was at El Camino Hospital in Mountain View, California in the early 1970s. The Medical Information System (MIS) was originally developed by a software and hardware team at Lockheed in Sunnyvale, California, which became the TMIS group at Technicon Instruments Corporation. The MIS system used a light pen to allow physicians and nurses to quickly point and click items to be ordered.

As of 2005, one of the largest projects for a national EHR is by the National Health Service (NHS) in the United Kingdom. The goal of the NHS is to have 60,000,000 patients with a centralized electronic health record by 2010. The plan involves a gradual roll-out commencing May 2006, providing general practices in England access to the National Programme for IT (NPfIT). The NHS component, known as the "Connecting for Health Programme", includes office-based CPOE for medication prescribing and test ordering and retrieval, although some concerns have been raised about patient safety features.

In 2008, the Massachusetts Technology Collaborative and the New England Healthcare Institute (NEHI) published research showing that 1 in 10 patients admitted to a Massachusetts community hospital suffered a preventable medication error. The study argued that Massachusetts hospitals could prevent 55,000 adverse drug events per year and save $170 million annually if they fully implemented CPOE. The findings prompted the Commonwealth of Massachusetts to enact legislation requiring all hospitals to implement CPOE by 2012 as a condition of licensure.

In addition, the study also concludes that it would cost approximately $2.1 million to implement a CPOE system, and a cost of $435,000 to maintain it in the state of Massachusetts while it saves annually about $2.7 million per hospital. The hospitals will still see payback within 26 months through reducing hospitalizations generated by error. Despite the advantages and cost savings, the CPOE is still not well adapted by many hospitals in the US.

The Leapfrog's 2008 survey showed that most hospitals are still not complying with having a fully implemented, effective CPOE system. The CPOE requirement became more challenging to meet in 2008 because the Leapfrog introduced a new requirement: Hospitals must test their CPOE systems with Leapfrog's CPOE Evaluation Tool. So the number of hospitals in the survey considered to be fully meeting the standard dropped to 7% in 2008 from 11% the previous year. Though the adoption rate seems very low in 2008, it is still an improvement from 2002 when only 2% of hospitals met this Leapfrog standard.
