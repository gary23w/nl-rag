---
title: "Windows Management Instrumentation"
source: https://en.wikipedia.org/wiki/Windows_Management_Instrumentation
domain: powershell-deep
license: CC-BY-SA-4.0
tags: powershell language, windows management instrumentation, cmdlet command, command line interface, scripting language
fetched: 2026-07-02
---

# Windows Management Instrumentation

**Windows Management Instrumentation** (**WMI**) is a set of extensions to the Windows Driver Model that provides an operating system interface through which instrumented components provide information and notification. WMI is Microsoft's implementation of the Web-Based Enterprise Management (WBEM) and Common Information Model (CIM) standards from the Distributed Management Task Force (DMTF).

WMI allows scripting languages (such as VBScript or PowerShell) to manage Microsoft Windows personal computers and servers, both locally and remotely. WMI comes preinstalled in Windows 2000 and later. It is available as a download for Windows NT 4.0, Windows 95, and Windows 98.

Also included with Windows was **Windows Management Instrumentation Command-line** (**WMIC**), a CLI utility to interface with WMI. However, starting with Windows 10, version 21H1 and Windows Server 2022, WMIC is deprecated in favor of PowerShell.

## Purpose of WMI

The purpose of WMI is to define a proprietary set of environment-independent specifications that enable sharing management information between management apps. WMI prescribes enterprise management standards and related technologies for Windows that work with existing management standards, such as Desktop Management Interface (DMI) and Simple Network Management Protocol (SNMP). WMI complements these other standards by providing a uniform model for accessing management data from any source.

## Development process

Because WMI abstracts the manageable entities with Common Information Model (CIM) and a collection of providers, the development of a provider implies several steps. The major steps can be summarized as follows:

1. Create the manageable entity model
  1. Define a model
  2. Implement the model
2. Create the WMI provider
  1. Determine the provider type to implement
  2. Determine the hosting model of the provider
  3. Create the provider template with the ATL wizard
  4. Implement the code logic in the provider
  5. Register the provider with WMI and the system
3. Test the provider
4. Create consumer sample code.

## Providers

Since the release of the first WMI implementation during the Windows NT 4.0 SP4 era (as an out-of-band download), Microsoft has consistently added WMI providers to Windows:

- On Windows NT 4.0, the WMI package shipped with 15 providers.
- Windows 2000 shipped with 29 WMI providers.
- Windows Server 2003 came with approximately 80 WMI providers.
- Windows Vista includes 13 new WMI providers, hence ships with approximately 100 providers.
- Windows Server 2008 includes more providers for IIS 7, PowerShell and virtualization.
- Windows 10 adds 47 providers for the Mobile Device Management (MDM) service.

Many customers have interpreted the growth in numbers of providers as a sign that Microsoft envisions WMI as the ubiquitous management layer of Windows.

Beyond the scripting needs, most leading management solutions, such as Microsoft Operations Manager (MOM), System Center Configuration Manager (SCCM), Active Directory Services (ADS), HP OpenView (HPOV), and the various offerings of BMC Software and CA, Inc. are WMI-enabled, i.e., capable of consuming and providing WMI information. This enables administrators who lack WMI coding skills to benefit from WMI.

## Features

WMI offers many features out of the box. Here are the most important advantages:

- **Automation interfaces:** WMI comes with a set of automation interfaces ready to use. Beyond the WMI class design and the provider development, the Microsoft development and test teams are not required to create, validate or test a scripting model as it is already available from WMI.
- **.NET management interfaces:** The `System.Management` namespace makes WMI classes available to all .NET apps and scripts written in C# or PowerShell. Beyond the WMI class design and the provider development, the Microsoft development and test teams are not required to create, validate and test new assemblies to support a new namespace in .NET as this support is already available from WMI.
- **COM interfaces:** Unmanaged code in Microsoft Windows (e.g., apps written in C or C++ languages) can interact with the standard set of WMI interfaces for the Component Object Model (COM) to access WMI providers and their supported WMI classes. Developers of WMI providers can leverage the same COM interfaces in their projects to furnish said classes.
- **Remoting capabilities over DCOM and SOAP:** In addition to local management via COM, WMI supports remoting via Distributed COM (DCOM) and SOAP. The latter is available in Windows Server 2003 R2 and later, through the WS-Management initiative led by Microsoft, Intel, Sun Microsystems, and Dell. This initiative allows running any scripts remotely or to consume WMI data through interfaces that handle SOAP requests and responses. WS-Management can consume everything that a WMI provider generates, although embedded objects in WMI instances were not supported until Windows Vista. WS-Management later became an integral part of PowerShell. Unlike SOAP-based remoting, DCOM-based remoting requires a proxy DLL deployed on each client machine.
- **Support for queries:** WMI offers support for WQL queries. This means WMI can still filter the results of a provider that doesn't implement filtering or queries.
- **Event-handling capabilities:** WMI can notify a subscriber of events of interest. WMI uses the WQL to submit event queries and define the type of events to be returned. Anyone writing a WMI provider can have the benefit of this functionality at no cost for their customers. It will be up to consumers to decide how they desire to consume the management information exposed by the WMI provider.

To speed up the process of writing a WMI provider, the WMI team developed the *WMI ATL Wizard* to generate the code template implementing a provider. The code generated is based on the WMI class model initially designed by the developer. The WMI provider developer will be able to interface the pre-defined COM or DCOM interfaces for the WMI provider with its set of native APIs retrieving the management information to expose.

WMI is based on an industry standard called Common Information Model (CIM) defined by the Distributed Management Task Force (DMTF). The CIM class-based schema is defined by a consortium of manufacturers and software developers for the requirements of the industry. Any developer can write code that fits into this model. For instance, Intel develops WMI providers for its network adapters. HP leveraged existing WMI providers and developed custom WMI providers for its OpenView enterprise management solutions. IBM's Tivoli management suite consumes WMI. Starting with Windows XP SP2, Microsoft leverages WMI to get status information from antivirus software and firewalls.

## Service

On the Windows NT family of operating systems, WMI runs as a Windows service called `WinMgmt`. On the Windows 9x family, WMI runs in the context of the `WinMgmt.exe` executable file. On both Windows 9x and Windows NT families, `WinMgmt.exe` is available as a command-line utility for servicing the WMI repository.

## WMI tools

Microsoft provides the following WMI tools for developers and IT pros:

- **MOF compiler (`MOFComp.exe`):** The Managed Object Format (MOF) compiler parses a file containing MOF statements and adds the classes and objects defined in the file to the CIM repository. The MOF format is a specific syntax to define CIM class representation in an ASCII file. MOF's role for CIM is comparable to MIB's role for SNMP. `MOFComp.exe` is included in every WMI installation. Every definition existing in the CIM repository is initially defined in an MOF file. MOF files are located in `%SystemRoot%\System32\WBEM`. During the WMI setup, they are loaded in the CIM repository.
- **WMI Administrative Tools:** This suite of tool consists of WMI CIM Studio, WMI Object Browser, WMI Event Registration, and WMI Event Viewer. The most important tool for a WMI provider developer is WMI CIM Studio as it helps in the initial WMI class creation in the CIM repository. It uses a web interface to display information and relies on a collection of ActiveX components installed on the system when it runs for the first time. WMI CIM Studio can:
  - Connect to a chosen system and browse the CIM repository in any namespace available.
  - Search for classes by their name, by their descriptions or by property names.
  - Review the properties, methods, and associations related to a given class.
  - See the instances available for a given class of the examined system.
  - Perform Queries in the WQL language.
  - Generate an MOF file based on selected classes.
  - Compile an MOF file to load it in the CIM repository.
- `**WBEMTest.exe**` is a WMI tester tool delivered with WMI. This tool allows an administrator or a developer to perform most of the tasks from a graphical interface that WMI provides at the API level. Although available under all Windows NT-based operating systems, this tool is not officially supported by Microsoft. WBEMTest provides the ability to:
  - Enumerate, open, create, and delete classes.
  - Enumerate, open, create, and delete instances of classes.
  - Select a namespace.
  - Perform data and event queries.
  - Execute methods associated to classes or instances.
  - Execute every WMI operation asynchronously, synchronously or semi-asynchronously.

- **WMI command line tool (WMIC)** is a scripting and automation utility that allows information retrieval and system administration via WMI, using some simple keywords (aliases). WMIC.exe is available on all Windows versions since Windows XP. Starting with Windows 10, version 21H1 and Windows Server 2022, WMIC is deprecated in favor of PowerShell. In Windows 11, version 24H2, WMIC is not installed by default. A Linux port of WMIC, `wmi-client`, is written in Python and is based on Samba4.
- **WBEMDump.exe:** This command-line tool is a component of the Platform SDK and comes a corresponding Visual C++ project. The tool can show the CIM repository classes, instances, or both. It is possible to retrieve the same information WMIC retrieves. `WBEMDump.exe` requires more specific knowledge about WMI, as it doesn't abstract WMI as WMIC. It is also possible to execute methods exposed by classes or instances. Even if it is not a standard WMI tool delivered with the system installation, this tool can be quite useful for exploring the CIM repository and WMI features.
- **WMIDiag.vbs (discontinued)**: The WMI Diagnosis Tool is a VBScript for testing and validating WMI on Windows 2000 and later. This script was downloadable from Microsoft until August 2020. The download includes pretty thorough documentation and the tool supports numerous switches. When run, it will generate up to four text files which: list the steps taken (the LOG file), an overview of the results (REPORT file), a statistics file (in comma separated values format), and optionally a file listing of the providers registered on the machine (PROVIDERS, also in comma separated values format). The report file that is generated includes a list of the issues identified and potential ways to fix them.

## Wireless networking example

In the .NET Framework, the ManagementClass class represents a Common Information Model (CIM) management class. A WMI class can be a `Win32_LogicalDisk` in the case of a disk drive, or a `Win32_Process`, such as a running program like `Notepad.exe`.

This example shows how `MSNdis_80211_ServiceSetIdentifier` WMI class is used to find the SSID of the Wi-Fi network that the system is currently connected to in the language C#:

```mw
ManagementClass mc = new ManagementClass("root\\WMI", "MSNdis_80211_ServiceSetIdentifier", null);
ManagementObjectCollection moc = mc.GetInstances();

foreach (ManagementObject mo in moc)
{
    string wlanCard = (string)mo["InstanceName"];
    bool active;
    if (!bool.TryParse((string)mo["Active"], out active))
    {
       active = false;
    }
    byte[] ssid = (byte[])mo["Ndis80211SsId"];
}
```

The `MSNdis_80211_ServiceSetIdentifier` WMI class is only supported on Windows XP and Windows Server 2003.

## WMI driver extensions

The WMI extensions to WDM provide kernel-level instrumentation such as publishing information, configuring device settings, supplying event notification from device drivers, and allowing administrators to set data security through a WMI provider known as the *WDM provider*. The extensions are part of the WDM architecture; however, they have broad utility and can be used with other types of drivers as well (such as SCSI and NDIS).

The WMI Driver Extensions service monitors all drivers and event trace providers that are configured to publish WMI or event trace information. Instrumented hardware data is provided by way of drivers instrumented for WMI extensions for WDM. WMI extensions for WDM offer a set of Windows device driver interfaces for instrumenting data within the driver models native to Windows, so OEMs and IHVs can easily extend the instrumented data set and add value to a hardware/software solution. The WMI Driver Extensions, however, are not supported by Windows Vista and later operating systems.

## Other examples of using WMI

Performance Monitor and AIDA64 are examples to using WMI to get some operating system monitoring information.
