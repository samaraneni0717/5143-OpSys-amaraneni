# Chapter 2 Review Questions
Name: Sai Chowdary Amaraneni
Course: 5143 Operating Systems
Date: 02 Feb 2016 

## 1.What are three objectives of an OS design?

. Convenience: An OS makes a computer more convenient to use.
• Efficiency: An OS allows the computer system resources to be used in an efficient
manner.
• Ability to evolve: An OS should be constructed in such a way as to permit the
effective development, testing, and introduction of new system functions without
interfering with service.


## 2. What is the kernel of an OS?
 The kernel is a computer program that manages input/output requests from software,
 and translates them into data processing instructions for the central processing unit 

 
##  3.What is multiprogramming?
 
 the running of two or more programs or sequences of instructions simultaneously 
by a computer with more than one central processor.


## 4. What is a process?

 A program in execution
 
## 5. How is the execution context of a process used by the OS?

•	By holding the process elements
•	Processes are created and managed by the operating system
•	It allows support for multiple processes

## 6.List and briefly explain five storage management responsibilities of a typical OS 

. Process isolation: The OS must prevent independent processes from interfering with each
other¡¯s memory, both data and instructions.
. Automatic allocation and management: Programs should be dynamically allo cated across
the memory hierarchy as required. Allocation should be transparent to the programmer. Thus,
the programmer is relieved of concerns relating to memory limitations, and the OS can achieve
efficiency by assigning memory to jobs only as needed.
. Support of modular programming: Programmers should be able to define program modules,
and to create, destroy, and alter the size of modules dynamically.
. Protection and access control: Sharing of memory, at any level of the memory hierarchy,
creates the potential for one program to address the memory space of another. This is desirable
when sharing is needed by particular applications. At other times, it threatens the integrity of
programs and even of the OS itself. The OS must allow portions of memory to be accessible in
various ways by various users.
. Long-term storage: Many application programs require means for storing information for
extended periods of time, after the computer has been powered down.
operating systems meet these requirements with virtual memory and file system facilities.
. The file system implements a long-term store, with information stored in named objects, called
files.


## 7.Explain the distinction between a real address and a virtual address.

Physical addresses refer to hardware addresses of physical memory. It has got frames.
Virtual addresses refer to the virtual store viewed by the process. It has got pages.


## 8.Describe the round-robin scheduling technique

different program process take turns using the resources of the computer is to limit each process 
to a certain short time period, then suspending that process to give another process a turn (or "time-slice"). 
This is often described as round-robin process scheduling.


## 9. Explain the difference between a monolithic kernel and a microkernel.

Monolithic kernel is a single large processes running entirely in a single address space. 
It is a single static binary file. All kernel services exist and execute in kernel address space. 
The kernel can invoke functions directly. The examples of monolithic kernel based OSs are Linux, Unix.
In Microkernels, the kernel is broken down into separate processes, known as servers. 
Some of the servers run in kernel space and some run in user-space. All servers are kept separate and 
run in different address spaces.The communication in microkernels is done via message passing. 
The servers communicate through IPC (Interprocess Communication). Servers invoke "services" from 
each other by sending messages. The separation has advantage that if one server fails other server 
can still work efficiently. The example of microkernel based OS are Mac OS X and Windows NT.


## 10. What is multithreading?

A technique by which a single set of code can be used by several processors at different stages of execution.
is the ability of a program or an operating system process to manage its use by more than one user at a time
and to even manage multiple requests by the same user without having to have multiple copies of the programming running in the computer

## 11.List the key design issues for an SMP operating system

Simultaneous concurrent process or threads ,Scheduling , Synchronization , Memory management, Reliability and fault tolerance
