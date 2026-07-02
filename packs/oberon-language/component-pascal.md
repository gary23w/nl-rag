---
title: "Component Pascal"
source: https://en.wikipedia.org/wiki/Component_Pascal
domain: oberon-language
license: CC-BY-SA-4.0
tags: oberon language, niklaus wirth, oberon operating system, component pascal, active oberon
fetched: 2026-07-02
---

# Component Pascal

**Component Pascal** is a programming language in the tradition of Niklaus Wirth's Pascal, Modula-2, Oberon and Oberon-2. It bears the name of the language Pascal and preserves its heritage, but is incompatible with Pascal. Instead, it is a minor variant and refinement of Oberon-2 with a more expressive type system and built-in string support. Component Pascal was originally named Oberon/L, and was designed and supported by a small ETH Zürich spin-off company named Oberon microsystems. They developed an integrated development environment (IDE) named BlackBox Component Builder. Since 2014, development and support has been taken over by a small group of volunteers. The first version of the IDE was released in 1994, as *Oberon/F*. At the time, it presented a novel approach to graphical user interface (GUI) construction based on editable forms, where fields and command buttons are linked to exported variables and executable procedures. This approach bears some similarity to the code-behind way used in Microsoft's .NET 3.0 to access code in Extensible Application Markup Language (XAML), which was released in 2008.

An open-source software implementation of Component Pascal exists for the .NET and Java virtual machine (JVM) platforms, from the Gardens Point team around John Gough at Queensland University of Technology in Australia.

On 23 June 2004 Oberon microsystems announced that the BlackBox Component Builder was made available as a free download and that an open-source version was planned. The beta open-source version was initially released in December 2004 and updated to a final v1.5 release in December 2005. It includes the complete source code of the IDE, compiler, debugger, source analyser, profiler, and interfacing libraries, and can also be downloaded from their website. Several release candidates for v1.6 appeared in the years 2009–2011, the latest one (1.6rc6) appeared on Oberon microsystems web pages in 2011. At the end of 2013, Oberon microsystems released the final release 1.6. It is probably the last release bundled by them. A small community took over the ongoing development.

BlackBox Component Pascal uses the extensions .odc (***O**beron **d**o**c**ument)*for document files, such as source files, and .osf *(**O**beron **s**ymbol **f**ile*) for symbol files while Gardens Point Component Pascal uses .cp for source and .cps for symbol files. BlackBox Component Pascal has its own executable and loadable object format .ocf (***O**beron **c**ode **f**ile*); it includes a runtime linking loader for this format. The document format (.odc) is a rich text binary format, which allows formatting, supports conditional folding, and allows active content to be embedded in the source text. It also handles user interface elements in editable forms. This is in the tradition of the Oberon Text format.

## Syntax

The full syntax for CP, as given by the Language Report, is shown below. In the extended Backus–Naur form, only 34 grammatical productions are needed, one more than for Oberon-2, although it is a more advanced language.

```mw
Module = MODULE ident ";" 
           [ImportList] DeclSeq 
           [BEGIN StatementSeq] 
           [CLOSE StatementSeq] 
         END ident ".".

ImportList = IMPORT [ident ":="] ident {"," [ident ":="] ident} ";".

DeclSeq = { CONST {ConstDecl ";" } 
          | TYPE {TypeDecl ";"} 
          | VAR {VarDecl ";"}} 
          { ProcDecl ";" | ForwardDecl ";"}.

ConstDecl = IdentDef "=" ConstExpr.

TypeDecl = IdentDef "=" Type.

VarDecl = IdentList ":" Type.

ProcDecl = PROCEDURE [Receiver] IdentDef [FormalPars] MethAttributes 
           [";" DeclSeq [BEGIN StatementSeq] 
           END ident].

MethAttributes = ["," NEW] ["," (ABSTRACT | EMPTY | EXTENSIBLE)].

ForwardDecl = PROCEDURE "^" [Receiver] IdentDef [FormalPars] MethAttributes.

FormalPars = "(" [FPSection {";" FPSection}] ")" [":" Type].

FPSection = [VAR | IN | OUT] ident {"," ident} ":" Type.

Receiver = "(" [VAR | IN] ident ":" ident ")".

Type = Qualident
    | ARRAY [ConstExpr {"," ConstExpr}] OF Type
    | [ABSTRACT | EXTENSIBLE | LIMITED] RECORD ["("Qualident")"] FieldList {";" FieldList} END
    | POINTER TO Type
    | PROCEDURE [FormalPars].

FieldList = [IdentList ":" Type].

StatementSeq = Statement {";" Statement}.

Statement = [ Designator ":=" Expr
    | Designator ["(" [ExprList] ")"]
    | IF Expr THEN StatementSeq
        {ELSIF Expr THEN StatementSeq}
        [ELSE StatementSeq] 
      END
    | CASE Expr OF 
        Case {"|" Case}
        [ELSE StatementSeq] 
      END
    | WHILE Expr DO StatementSeq END
    | REPEAT StatementSeq UNTIL Expr
    | FOR ident ":=" Expr TO Expr [BY ConstExpr] DO StatementSeq END
    | LOOP StatementSeq END
    | WITH [ Guard DO StatementSeq ] 
       {"|" [ Guard DO StatementSeq ] } 
       [ELSE StatementSeq] 
      END
    | EXIT
    | RETURN [Expr]
    ].

Case = [CaseLabels {"," CaseLabels} ":" StatementSeq].

CaseLabels = ConstExpr [".." ConstExpr].

Guard = Qualident ":" Qualident.

ConstExpr = Expr.

Expr = SimpleExpr [Relation SimpleExpr].

SimpleExpr = ["+" | "-"] Term {AddOp Term}.

Term = Factor {MulOp Factor}.

Factor = Designator | number | character | string | NIL | Set | "(" Expr ")" | " ~ " Factor.

Set = "{" [Element {"," Element}] "}".

Element = Expr [".." Expr].

Relation = "=" | "#" | "<" | "<=" | ">" | ">=" | IN | IS.

AddOp = "+" | "-" | OR.

MulOp = "*" | "/" | DIV | MOD | "&".

Designator = Qualident {"." ident 
             | "[" ExprList "]" 
             | "^" 
             | "(" Qualident ")" 
             | "(" [ExprList] ")"} [ "$" ].

ExprList = Expr {"," Expr}.

IdentList = IdentDef {"," IdentDef}.

Qualident = [ident "."] ident.

IdentDef = ident ["*" | "-"].
```
