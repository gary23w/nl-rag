---
title: "Group Policy"
source: https://en.wikipedia.org/wiki/Group_Policy
domain: windows-registry
license: CC-BY-SA-4.0
tags: windows registry, registry editor, registry hive, group policy
fetched: 2026-07-02
---

# Group Policy

**Group Policy** is a feature of the Microsoft Windows NT family of operating systems (including Windows 8.1, Windows 10, Windows 11) that controls the working environment of user accounts and computer accounts. Group Policy provides centralized management and configuration of operating systems, applications, and users' settings in an Active Directory environment. A set of Group Policy configurations is called a **Group Policy Object** (**GPO**). A version of Group Policy called **Local Group Policy** (LGPO or LocalGPO) allows Group Policy Object management without Active Directory on standalone computers.

Active Directory servers disseminate group policies by listing them in their LDAP directory under objects of class `groupPolicyContainer`. These refer to fileserver paths (attribute `gPCFileSysPath`) that store the actual group policy objects, typically in an SMB share \\*domain.com*\SYSVOL shared by the Active Directory server. If a group policy has registry settings, the associated file share will have a file `registry.pol` with the registry settings that the client needs to apply.

The Policy Editor (`gpedit.msc`) is not provided on Home (& Starter) editions of Windows.

## Operation

Group Policies, in part, control what users can and cannot do on a computer system. For example, a Group Policy can be used to enforce a password complexity policy that prevents users from choosing an overly simple password. Other examples include: allowing or preventing unidentified users from remote computers to connect to a network share, or to block/restrict access to certain folders. A set of such configurations is called a Group Policy Object (GPO).

As part of Microsoft's *IntelliMirror* technologies, Group Policy aims to reduce the cost of supporting users. IntelliMirror technologies relate to the management of disconnected machines or roaming users and include *roaming user profiles*, *folder redirection*, and *offline files*.

### Enforcement

To accomplish the goal of central management of a group of computers, machines should receive and enforce GPOs. A GPO that resides on a single machine only applies to that computer. To apply a GPO to a group of computers, Group Policy relies on Active Directory (or on third-party products like ZENworks Desktop Management) for distribution. Active Directory can distribute GPOs to computers which belong to a Windows domain.

By default, Microsoft Windows refreshes its policy settings every 90 minutes with a random 30 minutes offset. On domain controllers, Microsoft Windows does so every five minutes. During the refresh, it discovers, fetches and applies all GPOs that apply to the machine and to logged-on users. Some settings - such as those for automated software installation, drive mappings, startup scripts or logon scripts - only apply during startup or user logon. Since Windows XP, users can manually initiate a refresh of the group policy by using the `gpupdate` command from a command prompt.

Group Policy Objects are processed in the following order (from top to bottom):

1. **Local** - Any settings in the computer's local policy. Prior to Windows Vista, there was only one local group policy stored per computer. Windows Vista and later Windows versions allow individual group policies per user accounts.
2. **Site** - Any Group Policies associated with the *Active Directory site* in which the computer resides. (An Active Directory site is a logical grouping of computers, intended to facilitate management of those computers based on their physical proximity.) If multiple policies are linked to a site, they are processed in the order set by the administrator.
3. **Domain** - Any Group Policies associated with the Windows domain in which the computer resides. If multiple policies are linked to a domain, they are processed in the order set by the administrator.
4. **Organizational Unit** - Group policies assigned to the *Active Directory organizational unit (OU)* in which the computer or user are placed. (OUs are logical units that help organizing and managing a group of users, computers or other Active Directory objects.) If multiple policies are linked to an OU, they are processed in the order set by the administrator.

The resulting Group Policy settings applied to a given computer or user are known as the Resultant Set of Policy (RSoP). RSoP information may be displayed for both computers and users using the `gpresult` command.

### Inheritance

A policy setting inside a hierarchical structure is ordinarily passed from parent to children, and from children to grandchildren, and so forth. This is termed *inheritance*. It can be blocked or enforced to control what policies are applied at each level. If a higher level administrator (enterprise administrator) creates a policy that has inheritance blocked by a lower level administrator (domain administrator), this policy will still be processed.

Where a Group Policy Preference Settings is configured and there is also an equivalent Group Policy Setting configured, then the value of the Group Policy Setting will take precedence.

### Filtering

*WMI filtering* is the process of customizing the scope of the GPO by choosing a (WMI) filter to apply. These filters allow administrators to apply the GPO only to, for example, computers of specific models, RAM, installed software, or anything available via WMI queries.

## History

The *System Policy Editor* was first introduced in Windows NT 4.0 Server. Later, Windows 2000 Professional and Windows 2000 Server introduced *Group Policy Editor* based on Microsoft Management Console.

## Local Group Policy

*Local Group Policy (LGP, or LocalGPO)* is a more basic version of Group Policy for standalone and non-domain computers, that has existed at least since Windows XP, and can be applied to domain computers. Prior to Windows Vista, LGP could enforce a Group Policy Object for a single local computer, but could not make policies for individual users or groups. From Windows Vista onward, LGP allow Local Group Policy management for individual users and groups as well, and also allows backup, importing and exporting of policies between standalone machines via "GPO Packs" – group policy containers which include the files needed to import the policy to the destination machine.

## Group Policy preferences

Group Policy Preferences are a way for the administrator to set policies that are not mandatory, but optional for the user or computer. There is a set of group policy setting extensions that were previously known as PolicyMaker. Microsoft bought PolicyMaker and then integrated them with Windows Server 2008. Microsoft has since released a migration tool that allows users to migrate PolicyMaker items to Group Policy Preferences.

Group Policy Preferences adds a number of new configuration items. These items also have a number of additional targeting options that can be used to granularly control the application of these setting items.

Group Policy Preferences are compatible with x86 and x64 versions of Windows XP, Windows Server 2003, and Windows Vista with the addition of the Client Side Extensions (also known as CSE).

Client Side Extensions are now included in Windows Server 2008, Windows 7, and Windows Server 2008 R2.

## Group Policy Management Console

Originally, Group Policies were modified using the Group Policy Edit tool that was integrated with Active Directory Users and Computers Microsoft Management Console (MMC) snap-in, but it was later split into a separate MMC snap-in called the Group Policy Management Console (GPMC). The GPMC is now a user component in Windows Server 2008 and Windows Server 2008 R2 and is provided as a download as part of the Remote Server Administration Tools for Windows Vista and Windows 7.

## Advanced Group Policy Management

Microsoft has also released a tool to make changes to Group Policy called Advanced Group Policy Management (a.k.a. AGPM). This tool is available for any organization that has licensed the Microsoft Desktop Optimization Pack (a.k.a. MDOP). This advanced tool allows administrators to have a check in/out process for modification Group Policy Objects, track changes to Group Policy Objects, and implement approval workflows for changes to Group Policy Objects.

AGPM consists of two parts - server and client. The server is a Windows Service that stores its Group Policy Objects in an archive located on the same computer or a network share. The client is a snap-in to the Group Policy Management Console, and connects to the AGPM server. Configuration of the client is performed via Group Policy.

## Administrative Templates

Administrative Templates are a feature of Group Policy, a Microsoft technology for centralized management of machines and users in an Active Directory environment.

Administrative Templates facilitate the management of registry-based policy. An ADM file is used to describe both the user interface presented to the Group Policy administrator and the registry keys that should be updated on the target machines. An ADM file is a text file with a specific syntax which describes both the interface and the registry values which will be changed if the policy is enabled or disabled.

ADM files are consumed by the Group Policy Object Editor (GPEdit). Windows XP Service Pack 2 shipped with five ADM files (system.adm, inetres.adm, wmplayer.adm, conf.adm and wuau.adm). These are merged into a unified "namespace" in GPEdit and presented to the administrator under the Administrative Templates node (for both machine and user policy).

### Syntax

A simple ADM example follows:

```
 CLASS MACHINE
 CATEGORY "Wikipedia Apps"
 	POLICY "Wikipedia"
 		KEYNAME "Software\WikiSoft\Preferences"
 		EXPLAIN "Configures WikiSoft Preferences"
 		VALUENAME "SharingEnabled"
 	        VALUEON "Yes"
 		VALUEOFF "No"
 	END POLICY
 END CATEGORY
```

A valid ADM file must have the following keywords:

- Class - either MACHINE or USER
- Category - Defines organizational structure of ADM and where it will be displayed in the GPEdit window.
- Policy - Groups definitions into one node and configuration screen of the GPEdit tree

Optional keywords used include:

- Keyname - used to define what registry key will be affected

View Filtering must be turned off in order to see custom preference settings (such as this example) in the Group Policy Editor.

### ADM files across different platforms

ADM files shipped with Microsoft operating systems include descriptions of policy settings for not just that platform but for all other platforms on which Group Policy is supported. For example, the Windows XP Service Pack 2 ADM files described policy settings not just for this platform but also for Windows 2000 and Windows Server 2003. This approach allows management of machines that are running an operating system other than that on which GPEdit is used.

### Managing ADM files

By default, ADM files are stored in each GPO, within Sysvol on domain controllers. This creates a simple and effective model for replicating ADM files across domain controllers (which is handled by the File Replication Service). However, in some instances this can cause operational issues. To this end, various policy settings are available to manage the manner in which ADM files are read and stored. These are described in Microsoft's KB article 816662.

### ADMX files

Starting with Windows Vista, ADM files have mostly been replaced with ADMX files (and their associated language-specific ADML files). The ADMX file is structured in standard XML format, whereas the ADM files used a proprietary format.

## Security

Group Policy settings are enforced voluntarily by the targeted applications. In many cases, this merely consists of disabling the user interface for a particular function.

Alternatively, a malevolent user can modify or interfere with the application so that it cannot successfully read its Group Policy settings, thus enforcing potentially lower security defaults or even returning arbitrary values.

## Later enhancements to Group Policy

Group Policy was enhanced following its initial release in Windows 2000. For example, Windows XP has introduced a new feature called Group Policy Update which replaced the `secedit` command. This feature allows an administrator to force a group policy update on all computers with accounts in a particular Organizational Unit. This overrides the default scheduled task on the computer which runs the `gpupdate` command within 90 minutes, adjusted by a random offset to avoid overloading the domain controller.

Group Policy Infrastructure Status was introduced, which can report when any Group Policy Objects are not replicated correctly amongst domain controllers.

Group Policy Results Report also has a new feature that times the execution of individual components when doing a Group Policy Update.
