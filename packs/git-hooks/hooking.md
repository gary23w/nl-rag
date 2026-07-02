---
title: "Hooking"
source: https://en.wikipedia.org/wiki/Hooking
domain: git-hooks
license: CC-BY-SA-4.0
tags: git hooks, git commit hooks, version control hooks, pre-commit hook scripts
fetched: 2026-07-02
---

# Hooking

In computer programming, **hooking** is a range of techniques used to alter or augment the behaviour of an operating system, of applications, or of other software components by intercepting function calls or messages or events passed between software components. Code that handles such intercepted function calls, events or messages is called a **hook**.

Hook methods are of particular importance in the template method pattern where common code in an abstract class can be augmented by custom code in a subclass. In this case each hook method is defined in the abstract class with an empty implementation which then allows a different implementation to be supplied in each concrete subclass.

Hooking is used for many purposes, including debugging and extending functionality. Examples might include intercepting keyboard or mouse event messages before they reach an application, or intercepting operating system calls in order to monitor behavior or modify the function of an application or other component. It is also widely used in benchmarking programs, for example frame rate measuring in 3D games, where the output and input is done through hooking.

Hooking can also be used by malicious code. For example, rootkits, pieces of software that try to make themselves invisible by faking the output of API calls that would otherwise reveal their existence, often use hooking techniques.

## Methods

Typically hooks are inserted while software is already running, but hooking is a tactic that can also be employed prior to the application being started. Both these techniques are described in greater detail below.

### Source modification

Hooking can be achieved by modifying the source of the executable or library before an application is running, through techniques of reverse engineering. This is typically used to intercept function calls to either monitor or replace them entirely.

For example, by using a disassembler, the entry point of a function within a module can be found. It can then be altered to instead dynamically load some other library module and then have it execute desired methods within that loaded library. If applicable, another related approach by which hooking can be achieved is by altering the import table of an executable. This table can be modified to load any additional library modules as well as changing what external code is invoked when a function is called by the application.

An alternative method for achieving function hooking is by intercepting function calls through a wrapper library. A wrapper is a version of a library that an application loads, with all the same functionality of the original library that it will replace. That is, all the functions that are accessible are essentially the same between the original and the replacement. This wrapper library can be designed to call any of the functionality from the original library, or replace it with an entirely new set of logic.

### Symbol wrapping

The GNU Linker supports the `--wrap=foo` CLI option. When used, the linker replaces all calls to `foo` with calls to `__wrap_foo`. The original definition of `foo` can now be referenced with the symbol `__real_foo`. Since this method does not use the dynamic linker, this method can only be used when a program's source code is available and the linking step of the build can be modified.

### Runtime modification

Operating systems and software may provide the means to easily insert event hooks at runtime. It is available provided that the process inserting the hook is granted enough permission to do so. Microsoft Windows for example, allows users to insert hooks that can be used to process or modify system events and application events for dialogs, scrollbars, and menus as well as other items. It also allows a hook to insert, remove, process or modify keyboard and mouse events. Linux provides another example where hooks can be used in a similar manner to process network events within the kernel through NetFilter.

When such functionality is not provided, a special form of hooking employs intercepting the library function calls made by a process. Function hooking is implemented by changing the very first few code instructions of the target function to jump to an injected code. Alternatively on systems using the shared library concept, the interrupt vector table or the import descriptor table can be modified in memory. Essentially these tactics employ the same ideas as those of source modification, but instead altering instructions and structures located in the memory of a process once it is already running.

## Sample code

### Virtual method table hooking

Whenever a class defines/inherits a virtual function (or method), compilers add a hidden member variable to the class which points to a virtual method table (VMT or Vtable). Most compilers place the hidden VMT pointer at the first 4 bytes of every instance of the class. A VMT is basically an array of pointers to all the virtual functions that instances of the class may call. At runtime these pointers are set to point to the right functions, because at compile time, it is not yet known if the base function is to be called or if an overridden version of the function from a derived class is to be called (thereby allowing for polymorphism). Therefore, virtual functions can be hooked by replacing the pointers to them within any VMT that they appear. The code below shows an example of a typical VMT hook in Microsoft Windows, written in C++.

```mw
#include <iostream>
#include "windows.h"
 
using namespace std;
 
class VirtualClass
{
public:
 
    int number;
 
    virtual void VirtualFn1() //This is the virtual function that will be hooked.
    {
        cout << "VirtualFn1 called " << number++ << "\n\n";
    }
};
 
 
 
 
using VirtualFn1_t = void(__thiscall*)(void* thisptr); 
VirtualFn1_t orig_VirtualFn1;

void __fastcall hkVirtualFn1(void* thisptr, int edx) //This is our hook function which we will cause the program to call instead of the original VirtualFn1 function after hooking is done.
{
    cout << "Hook function called" << "\n";
 
    orig_VirtualFn1(thisptr); //Call the original function.
}
 
 
 
 
int main()
{
    VirtualClass* myClass = new VirtualClass(); //Create a pointer to a dynamically allocated instance of VirtualClass.
 
    void** vTablePtr = *reinterpret_cast<void***>(myClass); //Find the address that points to the base of VirtualClass' VMT (which then points to VirtualFn1) and store it in vTablePtr.
 
    DWORD oldProtection;
    VirtualProtect(vTablePtr, 4, PAGE_EXECUTE_READWRITE, &oldProtection); //Removes page protection at the start of the VMT so we can overwrite its first pointer.
 
    orig_VirtualFn1 = reinterpret_cast<VirtualFn1_t>(*vTablePtr); //Stores the pointer to VirtualFn1 from the VMT in a global variable so that it can be accessed again later after its entry in the VMT has been 
                                                                  //overwritten with our hook function.
 
    *vTablePtr = &hkVirtualFn1; //Overwrite the pointer to VirtualFn1 within the virtual table to a pointer to our hook function (hkVirtualFn1).
 
    VirtualProtect(vTablePtr, 4, oldProtection, 0); //Restore old page protection.
 
    myClass->VirtualFn1(); //Call the virtual function from our class instance. Because it is now hooked, this will actually call our hook function (hkVirtualFn1).
    myClass->VirtualFn1();
    myClass->VirtualFn1();
 
    delete myClass;
 
    return 0;
}
```

All virtual functions must be class member functions, and all (non-static) class member functions are called with the __thiscall calling convention (unless the member function takes a variable number of arguments, in which case it is called with __cdecl). The __thiscall calling convention passes a pointer to the calling class instance (commonly referred to as a "this" pointer) via the ECX register (on the x86 architecture). Therefore, in order for a hook function to properly intercept the "this" pointer that is passed and take it as an argument, it must look into the ECX register. In the above example, this is done by setting the hook function (hkVirtualFn1) to use the __fastcall calling convention, which causes the hook function to look into the ECX register for one of its arguments.

Also note that, in the above example, the hook function (hkVirtualFn1) is not a member function itself so it cannot use the __thiscall calling convention. __fastcall has to be used instead because it is the only other calling convention that looks into the ECX register for an argument.

### C# keyboard event hook

The following example will hook into keyboard events in Microsoft Windows using the Microsoft .NET Framework.

```mw
using System.Runtime.InteropServices;

namespace Hooks;

public class KeyHook
{
    /* Member variables */
    protected static int Hook;
    protected static LowLevelKeyboardDelegate Delegate;
    protected static readonly object Lock = new object();
    protected static bool IsRegistered = false;

    /* DLL imports */
    [DllImport("user32")]
    private static extern int SetWindowsHookEx(int idHook, LowLevelKeyboardDelegate lpfn,
        int hmod, int dwThreadId);

    [DllImport("user32")]
    private static extern int CallNextHookEx(int hHook, int nCode, int wParam, KBDLLHOOKSTRUCT lParam);

    [DllImport("user32")]
    private static extern int UnhookWindowsHookEx(int hHook);

    /* Types & constants */
    protected delegate int LowLevelKeyboardDelegate(int nCode, int wParam, ref KBDLLHOOKSTRUCT lParam);
    private const int HC_ACTION = 0;
    private const int WM_KEYDOWN = 0x0100;
    private const int WM_KEYUP = 0x0101;
    private const int WH_KEYBOARD_LL = 13;

    [StructLayout(LayoutKind.Sequential)]
    public struct KBDLLHOOKSTRUCT
    {
        public int vkCode;
        public int scanCode;
        public int flags;
        public int time;
        public int dwExtraInfo;
    }

    /* Methods */
    static private int LowLevelKeyboardHandler(int nCode, int wParam, ref KBDLLHOOKSTRUCT lParam)
    {
        if (nCode == HC_ACTION)
        {
            if (wParam == WM_KEYDOWN)
                System.Console.Out.WriteLine("Key Down: " + lParam.vkCode);
            else if (wParam == WM_KEYUP)
                System.Console.Out.WriteLine("Key Up: " + lParam.vkCode);
        }
        return CallNextHookEx(Hook, nCode, wParam, lParam);
    }

    public static bool RegisterHook()
    {
        lock (Lock)
        {
            if (IsRegistered)
                return true;
            Delegate = LowLevelKeyboardHandler;
            Hook = SetWindowsHookEx(
                WH_KEYBOARD_LL, Delegate,
                Marshal.GetHINSTANCE(
                    System.Reflection.Assembly.GetExecutingAssembly().GetModules()[0]
                ).ToInt32(), 0
            );

            if (Hook != 0)
                return IsRegistered = true;
            Delegate = null;
            return false;
        }
    }

    public static bool UnregisterHook()
    {
        lock (Lock)
        {
            return IsRegistered = (UnhookWindowsHookEx(Hook) != 0);
        }
    }
}
```

### API/function hooking/interception using JMP instruction aka splicing

The following source code is an example of an API/function hooking method which hooks by overwriting the first six bytes of a destination function with a JMP instruction to a new function. The code is compiled into a DLL file then loaded into the target process using any method of DLL injection. Using a backup of the original function one might then restore the first six bytes again so the call will not be interrupted. In this example the win32 API function MessageBoxW is hooked.

```mw
/*
 This idea is based on chrom-lib approach, Distributed under GNU LGPL License.
 Source chrom-lib: https://github.com/linuxexp/chrom-lib
 Copyright (C) 2011  Raja Jamwal
*/
#include <windows.h>  
#define SIZE 6

 typedef int (WINAPI *pMessageBoxW)(HWND, LPCWSTR, LPCWSTR, UINT);  // Messagebox prototype
 int WINAPI MyMessageBoxW(HWND, LPCWSTR, LPCWSTR, UINT);            // Our detour

 void BeginRedirect(LPVOID);                                        
 pMessageBoxW pOrigMBAddress = NULL;                                // address of original
 BYTE oldBytes[SIZE] = {0};                                         // backup
 BYTE JMP[SIZE] = {0};                                              // 6 byte JMP instruction
 DWORD oldProtect, myProtect = PAGE_EXECUTE_READWRITE;

 INT APIENTRY DllMain(HMODULE hDLL, DWORD Reason, LPVOID Reserved)  
 {  
   switch (Reason)  
   {  
   case DLL_PROCESS_ATTACH:                                        // if attached
     pOrigMBAddress = (pMessageBoxW)                      
       GetProcAddress(GetModuleHandleA("user32.dll"),              // get address of original 
               "MessageBoxW");  
     if (pOrigMBAddress != NULL)  
       BeginRedirect(MyMessageBoxW);                               // start detouring
     break;

   case DLL_PROCESS_DETACH:  
     VirtualProtect((LPVOID)pOrigMBAddress, SIZE, myProtect, &oldProtect);   // assign read write protection
     memcpy(pOrigMBAddress, oldBytes, SIZE);                                 // restore backup
     VirtualProtect((LPVOID)pOrigMBAddress, SIZE, oldProtect, &myProtect);   // reset protection

   case DLL_THREAD_ATTACH:  
   case DLL_THREAD_DETACH:  
     break;  
   }  
   return TRUE;  
 }

 void BeginRedirect(LPVOID newFunction)  
 {  
   BYTE tempJMP[SIZE] = {0xE9, 0x90, 0x90, 0x90, 0x90, 0xC3};              // 0xE9 = JMP 0x90 = NOP 0xC3 = RET
   memcpy(JMP, tempJMP, SIZE);                                             // store jmp instruction to JMP
   DWORD JMPSize = ((DWORD)newFunction - (DWORD)pOrigMBAddress - 5);       // calculate jump distance
   VirtualProtect((LPVOID)pOrigMBAddress, SIZE,                            // assign read write protection
           PAGE_EXECUTE_READWRITE, &oldProtect);  
   memcpy(oldBytes, pOrigMBAddress, SIZE);                                 // make backup
   memcpy(&JMP[1], &JMPSize, 4);                                           // fill the nop's with the jump distance (JMP,distance(4bytes),RET)
   memcpy(pOrigMBAddress, JMP, SIZE);                                      // set jump instruction at the beginning of the original function
   VirtualProtect((LPVOID)pOrigMBAddress, SIZE, oldProtect, &myProtect);   // reset protection
 }

 int WINAPI MyMessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uiType)  
 {  
   VirtualProtect((LPVOID)pOrigMBAddress, SIZE, myProtect, &oldProtect);   // assign read write protection
   memcpy(pOrigMBAddress, oldBytes, SIZE);                                 // restore backup
   int retValue = MessageBoxW(hWnd, lpText, lpCaption, uiType);            // get return value of original function
   memcpy(pOrigMBAddress, JMP, SIZE);                                      // set the jump instruction again
   VirtualProtect((LPVOID)pOrigMBAddress, SIZE, oldProtect, &myProtect);   // reset protection
   return retValue;                                                        // return original return value
 }
```

### Netfilter hook

This example shows how to use hooking to alter network traffic in the Linux kernel using Netfilter.

```mw
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/skbuff.h>

#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/in.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>

/* Port we want to drop packets on */
static const uint16_t port = 25;

/* This is the hook function itself */
static unsigned int hook_func(unsigned int hooknum,
                       struct sk_buff **pskb,
                       const struct net_device *in,
                       const struct net_device *out,
                       int (*okfn)(struct sk_buff *))
{
        struct iphdr *iph = ip_hdr(*pskb);
        struct tcphdr *tcph, tcpbuf;

        if (iph->protocol != IPPROTO_TCP)
                return NF_ACCEPT;

        tcph = skb_header_pointer(*pskb, ip_hdrlen(*pskb), sizeof(*tcph), &tcpbuf);
        if (tcph == NULL)
                return NF_ACCEPT;

        return (tcph->dest == port) ? NF_DROP : NF_ACCEPT;
}

/* Used to register our hook function */
static struct nf_hook_ops nfho = {
        .hook     = hook_func,
        .hooknum  = NF_IP_PRE_ROUTING,
        .pf       = NFPROTO_IPV4,
        .priority = NF_IP_PRI_FIRST,
};

static __init int my_init(void)
{
        return nf_register_hook(&nfho);
}

static __exit void my_exit(void)
{
    nf_unregister_hook(&nfho);
}

module_init(my_init);
module_exit(my_exit);
```

### Internal IAT hooking

The following code demonstrates how to hook functions that are imported from another module. This can be used to hook functions in a different process from the calling process. For this the code must be compiled into a DLL file then loaded into the target process using any method of DLL injection. The advantage of this method is that it is less detectable by antivirus software and/or anti-cheat software, one might make this into an external hook that doesn't make use of any malicious calls. The Portable Executable header contains the Import Address Table (IAT), which can be manipulated as shown in the source below. The source below runs under Microsoft Windows.

```mw
#include <windows.h>

typedef int(__stdcall *pMessageBoxA) (HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType); //This is the 'type' of the MessageBoxA call.
pMessageBoxA RealMessageBoxA; //This will store a pointer to the original function.

void DetourIATptr(const char* function, void* newfunction, HMODULE module);

int __stdcall NewMessageBoxA(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType) { //Our fake function
    printf("The String Sent to MessageBoxA Was : %s\n", lpText);
    return RealMessageBoxA(hWnd, lpText, lpCaption, uType); //Call the real function
}

int main(int argc, CHAR *argv[]) {
   DetourIATptr("MessageBoxA",(void*)NewMessageBoxA,0); //Hook the function
   MessageBoxA(NULL, "Just A MessageBox", "Just A MessageBox", 0); //Call the function -- this will invoke our fake hook.
   return 0;
}

void **IATfind(const char *function, HMODULE module) { //Find the IAT (Import Address Table) entry specific to the given function.
	int ip = 0;
	if (module == 0)
		module = GetModuleHandle(0);
	PIMAGE_DOS_HEADER pImgDosHeaders = (PIMAGE_DOS_HEADER)module;
	PIMAGE_NT_HEADERS pImgNTHeaders = (PIMAGE_NT_HEADERS)((LPBYTE)pImgDosHeaders + pImgDosHeaders->e_lfanew);
	PIMAGE_IMPORT_DESCRIPTOR pImgImportDesc = (PIMAGE_IMPORT_DESCRIPTOR)((LPBYTE)pImgDosHeaders + pImgNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress);

	if (pImgDosHeaders->e_magic != IMAGE_DOS_SIGNATURE)
		printf("libPE Error : e_magic is no valid DOS signature\n");

	for (IMAGE_IMPORT_DESCRIPTOR *iid = pImgImportDesc; iid->Name != NULL; iid++) {
		for (int funcIdx = 0; *(funcIdx + (LPVOID*)(iid->FirstThunk + (SIZE_T)module)) != NULL; funcIdx++) {
			char *modFuncName = (char*)(*(funcIdx + (SIZE_T*)(iid->OriginalFirstThunk + (SIZE_T)module)) + (SIZE_T)module + 2);
			const uintptr_t nModFuncName = (uintptr_t)modFuncName;
			bool isString = !(nModFuncName & (sizeof(nModFuncName) == 4 ? 0x80000000 : 0x8000000000000000));
			if (isString) {
				if (!_stricmp(function, modFuncName))
					return funcIdx + (LPVOID*)(iid->FirstThunk + (SIZE_T)module);
			}
		}
	}
	return 0;
}

void DetourIATptr(const char *function, void *newfunction, HMODULE module) {
	void **funcptr = IATfind(function, module);
	if (*funcptr == newfunction)
		 return;

	DWORD oldrights, newrights = PAGE_READWRITE;
	//Update the protection to READWRITE
	VirtualProtect(funcptr, sizeof(LPVOID), newrights, &oldrights);

	RealMessageBoxA = (pMessageBoxA)*funcptr; //Some compilers require the cast (like "MinGW"), not sure about MSVC though
	*funcptr = newfunction;

	//Restore the old memory protection flags.
	VirtualProtect(funcptr, sizeof(LPVOID), oldrights, &newrights);
}
```
