---
title: "Ackermann function (part 6/6)"
source: https://rosettacode.org/wiki/Ackermann_function
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/6
---

## XSLT

The following named template calculates the Ackermann function:

```mw
  <xsl:template name="ackermann">
    <xsl:param name="m"/>
    <xsl:param name="n"/>

    <xsl:choose>
      <xsl:when test="$m = 0">
        <xsl:value-of select="$n+1"/>
      </xsl:when>
      <xsl:when test="$n = 0">
        <xsl:call-template name="ackermann">
          <xsl:with-param name="m" select="$m - 1"/>
          <xsl:with-param name="n" select="'1'"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="p">
          <xsl:call-template name="ackermann">
            <xsl:with-param name="m" select="$m"/>
            <xsl:with-param name="n" select="$n - 1"/>
          </xsl:call-template>
        </xsl:variable>

        <xsl:call-template name="ackermann">
          <xsl:with-param name="m" select="$m - 1"/>
          <xsl:with-param name="n" select="$p"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
```

Here it is as part of a template

```mw
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:template match="arguments">
      <xsl:for-each select="args">
        <div>
          <xsl:value-of select="m"/>, <xsl:value-of select="n"/>:
          <xsl:call-template name="ackermann">
            <xsl:with-param name="m" select="m"/>
            <xsl:with-param name="n" select="n"/>
          </xsl:call-template>
        </div>
      </xsl:for-each>
  </xsl:template>

  <xsl:template name="ackermann">
    <xsl:param name="m"/>
    <xsl:param name="n"/>

    <xsl:choose>
      <xsl:when test="$m = 0">
        <xsl:value-of select="$n+1"/>
      </xsl:when>
      <xsl:when test="$n = 0">
        <xsl:call-template name="ackermann">
          <xsl:with-param name="m" select="$m - 1"/>
          <xsl:with-param name="n" select="'1'"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="p">
          <xsl:call-template name="ackermann">
            <xsl:with-param name="m" select="$m"/>
            <xsl:with-param name="n" select="$n - 1"/>
          </xsl:call-template>
        </xsl:variable>

        <xsl:call-template name="ackermann">
          <xsl:with-param name="m" select="$m - 1"/>
          <xsl:with-param name="n" select="$p"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
</xsl:stylesheet>
```

Which will transform this input

```mw
<?xml version="1.0" ?>
<?xml-stylesheet type="text/xsl" href="ackermann.xslt"?>
<arguments>
  <args>
    <m>0</m>
    <n>0</n>
  </args>
  <args>
    <m>0</m>
    <n>1</n>
  </args>
  <args>
    <m>0</m>
    <n>2</n>
  </args>
  <args>
    <m>0</m>
    <n>3</n>
  </args>
  <args>
    <m>0</m>
    <n>4</n>
  </args>
  <args>
    <m>0</m>
    <n>5</n>
  </args>
  <args>
    <m>0</m>
    <n>6</n>
  </args>
  <args>
    <m>0</m>
    <n>7</n>
  </args>
  <args>
    <m>0</m>
    <n>8</n>
  </args>
  <args>
    <m>1</m>
    <n>0</n>
  </args>
  <args>
    <m>1</m>
    <n>1</n>
  </args>
  <args>
    <m>1</m>
    <n>2</n>
  </args>
  <args>
    <m>1</m>
    <n>3</n>
  </args>
  <args>
    <m>1</m>
    <n>4</n>
  </args>
  <args>
    <m>1</m>
    <n>5</n>
  </args>
  <args>
    <m>1</m>
    <n>6</n>
  </args>
  <args>
    <m>1</m>
    <n>7</n>
  </args>
  <args>
    <m>1</m>
    <n>8</n>
  </args>
  <args>
    <m>2</m>
    <n>0</n>
  </args>
  <args>
    <m>2</m>
    <n>1</n>
  </args>
  <args>
    <m>2</m>
    <n>2</n>
  </args>
  <args>
    <m>2</m>
    <n>3</n>
  </args>
  <args>
    <m>2</m>
    <n>4</n>
  </args>
  <args>
    <m>2</m>
    <n>5</n>
  </args>
  <args>
    <m>2</m>
    <n>6</n>
  </args>
  <args>
    <m>2</m>
    <n>7</n>
  </args>
  <args>
    <m>2</m>
    <n>8</n>
  </args>
  <args>
    <m>3</m>
    <n>0</n>
  </args>
  <args>
    <m>3</m>
    <n>1</n>
  </args>
  <args>
    <m>3</m>
    <n>2</n>
  </args>
  <args>
    <m>3</m>
    <n>3</n>
  </args>
  <args>
    <m>3</m>
    <n>4</n>
  </args>
  <args>
    <m>3</m>
    <n>5</n>
  </args>
  <args>
    <m>3</m>
    <n>6</n>
  </args>
  <args>
    <m>3</m>
    <n>7</n>
  </args>
  <args>
    <m>3</m>
    <n>8</n>
  </args>
</arguments>
```

into this output

```
0, 0: 1
0, 1: 2
0, 2: 3
0, 3: 4
0, 4: 5
0, 5: 6
0, 6: 7
0, 7: 8
0, 8: 9
1, 0: 2
1, 1: 3
1, 2: 4
1, 3: 5
1, 4: 6
1, 5: 7
1, 6: 8
1, 7: 9
1, 8: 10
2, 0: 3
2, 1: 5
2, 2: 7
2, 3: 9
2, 4: 11
2, 5: 13
2, 6: 15
2, 7: 17
2, 8: 19
3, 0: 5
3, 1: 13
3, 2: 29
3, 3: 61
3, 4: 125
3, 5: 253
3, 6: 509
3, 7: 1021
3, 8: 2045
```


## Yabasic

```mw
sub ack(M,N)
    if M = 0 return N + 1
    if N = 0 return ack(M-1,1)
    return ack(M-1,ack(M, N-1))
end sub

print ack(3, 4)
```

What smart code can get. Fast as lightning!

Translation of

:

Phix

```mw
sub ack(m, n)
    if m=0 then
        return n+1
    elsif m=1 then
        return n+2
    elsif m=2 then
        return 2*n+3
    elsif m=3 then
        return 2^(n+3)-3
    elsif m>0 and n=0 then
        return ack(m-1,1)
    else
        return ack(m-1,ack(m,n-1))
    end if
end sub

sub Ackermann()
    local i, j
    for i=0 to 3
        for j=0 to 10
            print ack(i,j) using "#####";
        next
        print
    next
    print "ack(4,1) ";: print ack(4,1) using "#####"
end sub
 
Ackermann()
```


## YAMLScript

```mw
!ys-0

defn main(m=3, n=4):
  say: "A($m, $n) = $(ack(m n))"

defn ack(m n):
  cond:
    m == 0: n.++
    n == 0: m.--.ack(1)
    else:   m.--.ack(m.ack(n.--))
```

**Output:**

```
$ ys ackermann-function.ys
A(3, 4) = 125
```


## Yorick

```mw
func ack(m, n) {
    if(m == 0)
        return n + 1;
    else if(n == 0)
        return ack(m - 1, 1);
    else
        return ack(m - 1, ack(m, n - 1));
}
```

Example invocation:

```mw
for(m = 0; m <= 3; m++) {
    for(n = 0; n <= 6; n++)
        write, format="%d ", ack(m, n);
    write, "";
}
```

**Output:**

```
1 2 3 4 5 6 7  
2 3 4 5 6 7 8  
3 5 7 9 11 13 15  
5 13 29 61 125 253 509
```


## Z80 Assembly

This function does 16-bit math. Sjasmplus syntax, CP/M executable.

```mw
    OPT --syntax=abf : OUTPUT "ackerman.com"
    ORG $100
    jr demo_start

;--------------------------------------------------------------------------------------------------------------------
; entry: ackermann_fn
; input: bc = m, hl = n
; output: hl = A(m,n) (16bit only)
ackermann_fn.inc_n:
    inc hl
ackermann_fn:
    inc hl
    ld a,c
    or b
    ret z               ; m == 0 -> return n+1
    ; m > 0 case        ; bc = m, hl = n+1
    dec bc
    dec hl              ; m-1, n restored
    ld a,l
    or h
    jr z,.inc_n         ; n == 0 -> return A(m-1, 1)
    ; m > 0, n > 0      ; bc = m-1, hl = n
    push bc
    inc bc
    dec hl
    call ackermann_fn   ; n = A(m, n-1)
    pop bc
    jp ackermann_fn     ; return A(m-1,A(m, n-1))

;--------------------------------------------------------------------------------------------------------------------
; helper functions for demo printing 4x9 table
print_str:
    push bc
    push hl
    ld c,9
.call_cpm:
    call 5
    pop hl
    pop bc
    ret
print_hl:
    ld b,' '
    ld e,b
    call print_char
    ld de,-10000
    call extract_digit
    ld de,-1000
    call extract_digit
    ld de,-100
    call extract_digit
    ld de,-10
    call extract_digit
    ld a,l
print_digit:
    ld b,'0'
    add a,b
    ld e,a
print_char:
    push bc
    push hl
    ld c,2
    jr print_str.call_cpm
extract_digit:
    ld a,-1
.digit_loop:
    inc a
    add hl,de
    jr c,.digit_loop
    sbc hl,de
    or a
    jr nz,print_digit
    ld e,b
    jr print_char

;--------------------------------------------------------------------------------------------------------------------
demo_start:             ; do m: [0,4) cross n: [0,9) table
    ld bc,0
.loop_m:
    ld hl,0             ; bc = m, hl = n = 0
    ld de,txt_m_is
    call print_str
    ld a,c
    or '0'
    ld e,a
    call print_char
    ld e,':'
    call print_char
.loop_n:
    push bc
    push hl
    call ackermann_fn
    call print_hl
    pop hl
    pop bc
    inc hl
    ld a,l
    cp 9
    jr c,.loop_n
    ld de,crlf
    call print_str
    inc bc
    ld a,c
    cp 4
    jr c,.loop_m
    rst 0               ; return to CP/M

txt_m_is:   db  "m=$"
crlf:       db  10,13,'$'
```

**Output:**

```
m=0:     1     2     3     4     5     6     7     8     9
m=1:     2     3     4     5     6     7     8     9    10
m=2:     3     5     7     9    11    13    15    17    19
m=3:     5    13    29    61   125   253   509  1021  2045
```


## ZED

```mw
(a) m n
M ZERO
(=) m 0
(add1) n

(a) m n
N ZERO
(=) n 0
(a) (sub1) m 1

(a) m n
DEFAULT
#true
(a) (sub1) m (a) m (sub1) n

(add1) n
=========
#true
(003) "+" n 1

(sub1) n
=========
#true
(003) "-" n 1

(=) n1 n2
=========
#true
(003) "=" n1 n2
```


## Zen C

```mw
fn ackermann(m: int, n: int) -> int {
    if m == 0 {
        return n + 1;
    }
    if m > 0 && n == 0 {
        return ackermann(m - 1, 1);
    }
    return ackermann(m - 1, ackermann(m, n - 1));
}

fn main() {
    // Test the function for small values... 
    for let m = 0; m <= 3; m += 1 {
        for let n = 0; n <= 4; n += 1 {
            let a = ackermann(m, n);
            println "A({m}, {n}) = {a}";
        }
    }
}
```

**Output:**

```
A(0, 0) = 1
A(0, 1) = 2
A(0, 2) = 3
A(0, 3) = 4
A(0, 4) = 5
A(1, 0) = 2
A(1, 1) = 3
A(1, 2) = 4
A(1, 3) = 5
A(1, 4) = 6
A(2, 0) = 3
A(2, 1) = 5
A(2, 2) = 7
A(2, 3) = 9
A(2, 4) = 11
A(3, 0) = 5
A(3, 1) = 13
A(3, 2) = 29
A(3, 3) = 61
A(3, 4) = 125
```


## Zig

```mw
pub fn ack(m: u64, n: u64) u64 {
    if (m == 0) return n + 1;
    if (n == 0) return ack(m - 1, 1);
    return ack(m - 1, ack(m, n - 1));
}

pub fn main() !void {
    const stdout = @import("std").io.getStdOut().writer();

    var m: u8 = 0;
    while (m <= 3) : (m += 1) {
        var n: u8 = 0;
        while (n <= 8) : (n += 1)
            try stdout.print("{d:>8}", .{ack(m, n)});
        try stdout.print("\n", .{});
    }
}
```

**Output:**

```
       1       2       3       4       5       6       7       8       9
       2       3       4       5       6       7       8       9      10
       3       5       7       9      11      13      15      17      19
       5      13      29      61     125     253     509    1021    2045
```


## ZX Spectrum Basic

Translation of

:

BASIC256

```mw
10 DIM s(2000,3)
20 LET s(1,1)=3: REM M
30 LET s(1,2)=7: REM N
40 LET lev=1
50 GO SUB 100
60 PRINT "A(";s(1,1);",";s(1,2);") = ";s(1,3)
70 STOP 
100 IF s(lev,1)=0 THEN LET s(lev,3)=s(lev,2)+1: RETURN 
110 IF s(lev,2)=0 THEN LET lev=lev+1: LET s(lev,1)=s(lev-1,1)-1: LET s(lev,2)=1: GO SUB 100: LET s(lev-1,3)=s(lev,3): LET lev=lev-1: RETURN 
120 LET lev=lev+1
130 LET s(lev,1)=s(lev-1,1)
140 LET s(lev,2)=s(lev-1,2)-1
150 GO SUB 100
160 LET s(lev,1)=s(lev-1,1)-1
170 LET s(lev,2)=s(lev,3)
180 GO SUB 100
190 LET s(lev-1,3)=s(lev,3)
200 LET lev=lev-1
210 RETURN
```

**Output:**

```
A(3,7) = 1021
```

Retrieved from "

https://rosettacode.org/wiki/Ackermann_function?oldid=402677

"
