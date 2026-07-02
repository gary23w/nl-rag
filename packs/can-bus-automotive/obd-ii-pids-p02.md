---
title: "OBD-II PIDs (part 2/2)"
source: https://en.wikipedia.org/wiki/OBD-II_PIDs
domain: can-bus-automotive
license: CC-BY-SA-4.0
tags: can bus, automotive networking, flexray protocol, obd diagnostics
fetched: 2026-07-02
part: 2/2
---

## CAN (11-bit) bus format

As defined in ISO 15765-4, emissions protocols (including OBD-II, EOBD, UDS, etc.) use the ISO-TP transport layer (ISO 15765-2). All CAN frames sent using ISO-TP use a data length of 8 bytes (and DLC of 8). It is recommended to pad the unused data bytes with 0xCC.

The PID query and response occurs on the vehicle's CAN bus. Standard OBD requests and responses use functional addresses. The diagnostic reader initiates a query using CAN ID 7DFh, which acts as a broadcast address, and accepts responses from any ID in the range 7E8h to 7EFh. ECUs that can respond to OBD queries listen both to the functional broadcast ID of 7DFh and one assigned ID in the range 7E0h to 7E7h. Their response has an ID of their assigned ID plus 8 e.g. 7E8h through 7EFh.

This approach allows up to eight ECUs, each independently responding to OBD queries. The diagnostic reader can use the ID in the ECU response frame to continue communication with a specific ECU. In particular, multi-frame communication requires a response to the specific ECU ID rather than to ID 7DFh.

CAN bus may also be used for communication beyond the standard OBD messages. Physical addressing uses particular CAN IDs for specific modules (e.g., 720h for the instrument cluster in Fords) with proprietary frame payloads.

### Query

The functional PID query is sent to the vehicle on the CAN bus at ID 7DFh, using 8 data bytes. The bytes are:

Byte

PID Type

0

1

2

3

4

5

6

7

SAE Standard

Number of

additional

data bytes:

2

Service

01 = show current data;

02 = freeze frame;

etc.

PID code

(e.g.: 05 = Engine coolant temperature)

not used

(

ISO 15765-2

suggests CCh)

Vehicle specific

Number of

additional

data bytes:

3

Custom service: (e.g.: 22 = enhanced data)

PID code

(e.g.: 4980h)

not used

(

ISO 15765-2

suggests CCh)

### Response

The vehicle responds to the PID query on the CAN bus with message IDs that depend on which module responded. Typically the engine or main ECU responds at ID 7E8h. Other modules, like the hybrid controller or battery controller in a Prius, respond at 07E9h, 07EAh, 07EBh, etc. These are 8h higher than the physical address the module responds to. Even though the number of bytes in the returned value is variable, the message uses 8 data bytes regardless (CAN bus protocol form Frameformat with 8 data bytes). The bytes are:

Byte

CAN Address

0

1

2

3

4

5

6

7

SAE Standard

7E8h,

7E9h,

7EAh,

etc.

Number of

additional

data bytes:

3 to 6

Custom service

Same as query, except that 40h is added to the service value. So:

41h = show current data;

42h = freeze frame;

etc.

PID code

(e.g.: 05 = Engine coolant temperature)

value of the specified parameter, byte 0

value, byte 1 (optional)

value, byte 2 (optional)

value, byte 3 (optional)

not used

(may be 00h or 55h)

Vehicle specific

7E8h, or 8h + physical ID of module.

Number of

additional

data bytes:

4to 7

Custom service: same as query, except that 40h is added to the service value.(e.g.: 62h = response to service 22h request)

PID code

(e.g.: 4980h)

value of the specified parameter, byte 0

value, byte 1 (optional)

value, byte 2 (optional)

value, byte 3 (optional)

Vehicle specific

7E8h, or 8h + physical ID of module.

Number of

additional

data bytes:

3

7Fh this a general response usually indicating the module doesn't recognize the request.

Custom service: (e.g.: 22h = enhanced diagnostic data by PID, 21h = enhanced data by offset)

31h

not used

(may be 00h)
