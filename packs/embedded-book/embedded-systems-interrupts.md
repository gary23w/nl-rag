---
title: "Embedded Systems/Interrupts"
source: https://en.wikibooks.org/wiki/Embedded_Systems/Interrupts
domain: embedded-book
license: CC-BY-SA-4.0 (Wikibooks Embedded Systems)
tags: embedded programming, interrupt service routine, embedded c
fetched: 2026-07-02
---

# Embedded Systems/Interrupts

<

Embedded Systems

## Interrupt

Sometimes things will happen in a system when the processor is simply not ready. In fact, sometimes things change that require immediate attention. Can you imagine, sitting at your PC, that you were to hit buttons on the keyboard, and nothing happens on your computer? Maybe the processor was busy, and it just didn't check to see if you were hitting any buttons at that time. The solution to this problem is something called an "Interrupt." Interrupts are events that cause the microprocessor to stop what it is doing, and handle a high-priority task first. After the interrupt is handled, the microprocessor goes back to whatever it was doing before. In this way, we can be assured that high-priority inputs are never ignored.

## Hardware and Software

There are two types of interrupts: Hardware and Software. Software interrupts are called from software, using a specified command. Hardware interrupts are triggered by peripheral devices outside the micro-controller. For instance, your embedded system may contain a timer that sends a pulse to the controller every second. Your micro-controller would wait until this pulse is received, and when the pulse comes, an interrupt would be triggered that would handle the signal.

## Interrupt Service Routines

Interrupt Service Routines (ISR) are the portions of the program code that handle the interrupt requests. When an Interrupt is triggered (either a hardware or software interrupt), the processor breaks away from the current task, moves the instruction pointer to the ISR, and then continues operation. When the ISR has completed, the processor returns execution to the previous location.

Many embedded systems are called **interrupt driven systems**, because most of the processing occurs in ISRs, and the embedded system spends most of its time in a low-power mode.

Some people split an ISR into two parts: top-half (fast interrupt handler, First-Level Interrupt Handler (FLIH)) and bottom-half (slow interrupt handler, Second-Level Interrupt Handlers (SLIH)). Top-half is a faster part of ISR which should quickly store minimal information about interrupt and schedule slower bottom-half at a later time.

We discuss two-level interrupt handling and other ways of writing interrupt handlers in interrupt architecture.

## Interrupt Vector Table

The "Interrupt Vector Table" is a list of every interrupt service routine. It is located at a fixed location in program memory. (Some processors expect the interrupt vector table to be a series of "call" instructions, each one followed by the address of the ISR. Other processors expect the interrupt vector table to hold just the ISR addresses alone.)

You must make sure that every entry in the interrupt vector table is filled with the address of some actual ISR, even if it means making most of them point to the "do nothing and return from interrupt" ISR.

## Interrupt flags

The PIC18 and PIC16 series of processors have a single interrupt handler, a single global interrupt enable bit, and a whole array of bits in the interrupt hardware. Each possible source of interrupts has a pair of bits in the interrupt hardware—a "flag" bit that is set whenever some piece of hardware wants attention, as if it's waving a flag trying to attract attention, and an "enable" bit that controls whether the processor will ignore that flag, or stop everything and run the interrupt handler. (Confusingly, some people refer to both bits as "flags"—in this section, we refer to the "request attention" bits as flag bits, and the "ignore or not" bits as enable bits).

When an interrupt occurs on an 8-bit PICmicro (PIC18 or PIC16), the hardware clears the global interrupt enable bit, then starts running the one and only interrupt handler. The interrupt handler software must somehow check all the things that could have possibly caused the interrupt—typically by checking each interrupt flag one by one—and handle each one (if necessary).

The 680x0 and x86 and dsPIC and PIC24 and many other processors have many interrupt vectors. When some piece of hardware requests attention on such a processor, the hardware vectors to and runs the specific interrupt handler for that particular bit of hardware.

## Writing interrupt routines

Many people write interrupt routines in C. A programmer who uses `gcc` declares an interrupt handler very similar to declaring a normal function, something like this:

```mw
void __attribute__ ((interrupt)) universal_handler ();
```

Alas, there is no standard way to write interrupt handlers in portable C. Every C compiler seems to use its own keywords incompatible with the keywords for any other C compiler. Even with gcc, the favored interrupt declaration varies from one processor to another.

Other programmers use C compilers that do not support writing interrupt handlers directly in C. They are forced to write the interrupt handler in assembly language, doing by hand the things the compiler does for the previous group of people:

An interrupt routine typically begins with a bunch of boilerplate code that pushes the status register and other stuff to the stack, and ends with another bunch of boilerplate code to restore all that stuff so whatever code was interrupted can continue from exactly where it left off. That boilerplate code is very different from one processor family to another—and has some key differences from the normal calling convention prologue and epilogue.

The compiler (or an assembly language programmer) writes in the interrupt vector table a pointer to that interrupt handler.

One extremely common problem is trying to do "too much" in an interrupt routine. Alas, often the symptoms only occur when two different interrupt routines are triggered more-or-less simultaneously, leading to difficult-to-debug intermittent errors and a lot of finger-pointing. Unfortunately, the person who wrote one interrupt routine points out that his routine works fine when run alone, and the person who wrote the other interrupt routine points out that his routine works fine when run alone, and all too often they each blame the other person for the problems that occur when both interrupts occur. One common symptom of an interrupt routine (possibly the UART interrupt handler, but often some other seemingly unrelated interrupt routine) taking "too long" is losing some, but not all of the characters in a stream of characters coming in over the UART.

Because it is difficult to calculate how much time an interrupt handler will take, it is common to directly measure how long interrupt handlers actually take. One popular debugging technique is to write interrupt handlers such that the interrupt handler sets a test pin high at the beginning of every interrupt routine, and the interrupt handler clears the test pin low at the end of every interrupt routine. An o'scope attached to that pin shows the actual execution time of that interrupt handler.
