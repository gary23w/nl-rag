---
title: "Sorting algorithms/Quicksort (part 3/8)"
source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 3/8
---

## AWK

```mw
# the following qsort implementation extracted from:
#
#       ftp://ftp.armory.com/pub/lib/awk/qsort
#
# Copyleft GPLv2 John DuBois
#
# @(#) qsort 1.2.1 2005-10-21
# 1990 john h. dubois iii (john@armory.com)
#
# qsortArbIndByValue(): Sort an array according to the values of its elements.
#
# Input variables:
#
# Arr[] is an array of values with arbitrary (associative) indices.
#
# Output variables:
#
# k[] is returned with numeric indices 1..n.  The values assigned to these
# indices are the indices of Arr[], ordered so that if Arr[] is stepped
# through in the order Arr[k[1]] .. Arr[k[n]], it will be stepped through in
# order of the values of its elements.
#
# Return value: The number of elements in the arrays (n).
#
# NOTES:
#
# Full example for accessing results:
#
#       foolist["second"] = 2;
#       foolist["zero"] = 0;
#       foolist["third"] = 3;
#       foolist["first"] = 1;
#
#       outlist[1] = 0;
#       n = qsortArbIndByValue(foolist, outlist)
#
#       for (i = 1; i <= n; i++) {
#               printf("item at %s has value %d\n", outlist[i], foolist[outlist[i]]);
#       }
#      delete outlist; 
#
function qsortArbIndByValue(Arr, k,
                            ArrInd, ElNum)
{
        ElNum = 0;
        for (ArrInd in Arr) {
                k[++ElNum] = ArrInd;
        }
        qsortSegment(Arr, k, 1, ElNum);
        return ElNum;
}
#
# qsortSegment(): Sort a segment of an array.
#
# Input variables:
#
# Arr[] contains data with arbitrary indices.
#
# k[] has indices 1..nelem, with the indices of Arr[] as values.
#
# Output variables:
#
# k[] is modified by this function.  The elements of Arr[] that are pointed to
# by k[start..end] are sorted, with the values of elements of k[] swapped
# so that when this function returns, Arr[k[start..end]] will be in order.
#
# Return value: None.
#
function qsortSegment(Arr, k, start, end,
                      left, right, sepval, tmp, tmpe, tmps)
{
        if ((end - start) < 1) {        # 0 or 1 elements
                return;
        }
        # handle two-element case explicitly for a tiny speedup
        if ((end - start) == 1) {
                if (Arr[tmps = k[start]] > Arr[tmpe = k[end]]) {
                        k[start] = tmpe;
                        k[end] = tmps;
                }
                return;
        }
        # Make sure comparisons act on these as numbers
        left = start + 0;
        right = end + 0;
        sepval = Arr[k[int((left + right) / 2)]];
        # Make every element <= sepval be to the left of every element > sepval
        while (left < right) {
                while (Arr[k[left]] < sepval) {
                        left++;
                }
                while (Arr[k[right]] > sepval) {
                        right--;
                }
                if (left < right) {
                        tmp = k[left];
                        k[left++] = k[right];
                        k[right--] = tmp;
                }
        }
        if (left == right)
                if (Arr[k[left]] < sepval) {
                        left++;
                } else {
                        right--;
                }
        if (start < right) {
                qsortSegment(Arr, k, start, right);
        }
        if (left < end) {
                qsortSegment(Arr, k, left, end);
        }
}
```


## BASIC

### ANSI BASIC

Works with

:

Decimal BASIC

```mw
100 REM Sorting algorithms/Quicksort
110 DECLARE EXTERNAL SUB QuickSort
120 DIM Arr(0 TO 19)
130 LET A = LBOUND(Arr)
140 LET B = UBOUND(Arr)
150 RANDOMIZE
160 FOR I = A TO B
170    LET Arr(I) = ROUND(INT(RND * 99))
180 NEXT I
190 PRINT "Unsorted:"
200 FOR I = A TO B
210    PRINT USING "## ": Arr(I);
220 NEXT I
230 PRINT
240 PRINT "Sorted:"
250 CALL QuickSort(Arr, A, B)
260 FOR I = A TO B
270    PRINT USING "## ": Arr(I);
280 NEXT I
290 PRINT
300 END
310 REM **
320 EXTERNAL SUB QuickSort (Arr(), L, R)
330 LET LIndex = L
340 LET RIndex = R
350 IF R > L THEN
360    LET Pivot = INT((L + R) / 2)
370    DO WHILE (LIndex <= Pivot) AND (RIndex >= Pivot)
380       DO WHILE (Arr(LIndex) < Arr(Pivot)) AND (LIndex <= Pivot)
390          LET LIndex = LIndex + 1
400       LOOP
410       DO WHILE (Arr(RIndex) > Arr(Pivot)) AND (RIndex >= Pivot)
420          LET RIndex = RIndex - 1
430       LOOP
440       LET Temp = Arr(LIndex)
450       LET Arr(LIndex) = Arr(RIndex)
460       LET Arr(RIndex) = Temp
470       LET LIndex = LIndex + 1
480       LET RIndex = RIndex - 1
490       IF (LIndex - 1) = Pivot THEN
500          LET RIndex = RIndex + 1
510          LET Pivot = RIndex
520       ELSEIF (RIndex + 1) = Pivot THEN
530          LET LIndex = LIndex - 1
540          LET Pivot = LIndex
550       END IF
560    LOOP
570    CALL QuickSort (Arr, L, Pivot - 1)
580    CALL QuickSort (Arr, Pivot + 1, R)
590 END IF
600 END SUB
```

**Output:**

(example)

```
Unsorted:
17 79 23 91 28 91 29 58 47 59  8 35 93 23 34 28 35 31  7 25 
Sorted:
 7  8 17 23 23 25 28 28 29 31 34 35 35 47 58 59 79 91 91 93 
```

### BBC BASIC

```mw
      DIM test(9)
      test() = 4, 65, 2, -31, 0, 99, 2, 83, 782, 1
      PROCquicksort(test(), 0, 10)
      FOR i% = 0 TO 9
        PRINT test(i%) ;
      NEXT
      PRINT
      END
      
      DEF PROCquicksort(a(), s%, n%)
      LOCAL l%, p, r%, t%
      IF n% < 2 THEN ENDPROC
      t% = s% + n% - 1
      l% = s%
      r% = t%
      p = a((l% + r%) DIV 2)
      REPEAT
        WHILE a(l%) < p l% += 1 : ENDWHILE
        WHILE a(r%) > p r% -= 1 : ENDWHILE
        IF l% <= r% THEN
          SWAP a(l%), a(r%)
          l% += 1
          r% -= 1
        ENDIF
      UNTIL l% > r%
      IF s% < r% PROCquicksort(a(), s%, r% - s% + 1)
      IF l% < t% PROCquicksort(a(), l%, t% - l% + 1 )
      ENDPROC
```

**Output:**

```
       -31         0         1         2         2         4        65        83        99       782
```

### Chipmunk Basic

Works with

:

Chipmunk Basic

version 3.6.4

Translation of

:

Yabasic

```mw
100 dim array(15)
110 a = 0
120 b = ubound(array)
130 randomize timer
140 for i = a to b
150   array(i) = rnd(1)*1000
160 next i
170 print "unsort ";
180 for i = a to b
190 print using "####";array(i);
200 if i = b then print ""; else print ", ";
210 next i
220 quicksort(array(),a,b)
230 print : print "  sort ";
240 for i = a to b
250   print using "####";array(i);
260   if i = b then print ""; else print ", ";
270 next i
280 print
290 end
300 sub quicksort(array(),l,r)
310   size = r-l+1
320   if size < 2 then return
330   i = l
340   j = r
350   pivot = array(l+int(size/2))
360   rem repeat
370     while array(i) < pivot
380       i = i+1
390     wend
400     while pivot < array(j)
410       j = j-1
420     wend
430     if i <= j then temp = array(i) : array(i) = array(j) : array(j) = temp : i = i+1 : j = j-1
440   if i <= j then goto 360
450   if l < j then quicksort(array(),l,j)
460   if i < r then quicksort(array(),i,r)
470 end sub
```

### Craft Basic

```mw
define size = 10, point = 0, top = 0
define high = 0, low = 0, pivot = 0

dim list[size]
dim stack[size]

gosub fill
gosub sort
gosub show

end

sub fill

   for i = 0 to size - 1

      let list[i] = int(rnd * 100)

   next i

return

sub sort

   let low = 0
   let high = size - 1
   let top = -1

   let top = top + 1
   let stack[top] = low
   let top = top + 1
   let stack[top] = high
 
   do

      if top < 0 then

         break

      endif

      let high = stack[top]
      let top = top - 1
      let low = stack[top]
      let top = top - 1

      let i = low - 1
      
      for j = low to high - 1

         if list[j] <= list[high] then

            let i = i + 1
            let t = list[i]
            let list[i] = list[j]
            let list[j] = t

         endif

      next j

      let point = i + 1
      let t = list[point]
      let list[point] = list[high]
      let list[high] = t
      let pivot = i + 1

      if pivot - 1 > low then

         let top = top + 1
         let stack[top] = low
         let top = top + 1
         let stack[top] = pivot - 1

      endif
  
      if pivot + 1 < high then

         let top = top + 1
         let stack[top] = pivot + 1
         let top = top + 1
         let stack[top] = high

      endif

      wait

   loop top >= 0

return

sub show

   for i = 0 to size - 1

      print i, ": ", list[i]

   next i

return
```

### FreeBASIC

```mw
' version 23-10-2016
' compile with: fbc -s console

' sort from lower bound to the highter bound
' array's can have subscript range from -2147483648 to +2147483647

Sub quicksort(qs() As Long, l As Long, r As Long)

    Dim As ULong size = r - l +1
    If size < 2 Then Exit Sub

    Dim As Long i = l, j = r
    Dim As Long pivot = qs(l + size \ 2)

    Do
        While qs(i) < pivot
            i += 1
        Wend
        While pivot < qs(j)
            j -= 1
        Wend
        If i <= j Then
            Swap qs(i), qs(j)
            i += 1
            j -= 1
        End If
    Loop Until i > j

    If l < j Then quicksort(qs(), l, j)
    If i < r Then quicksort(qs(), i, r)

End Sub

' ------=< MAIN >=------

Dim As Long i, array(-7 To 7)
Dim As Long a = LBound(array), b = UBound(array)

Randomize Timer
For i = a To b : array(i) = i  : Next
For i = a To b ' little shuffle
    Swap array(i), array(Int(Rnd * (b - a +1)) + a)
Next

Print "unsorted ";
For i = a To b : Print Using "####"; array(i); : Next : Print

quicksort(array(), LBound(array), UBound(array))

Print "  sorted ";
For i = a To b : Print Using "####"; array(i); : Next : Print

' empty keyboard buffer
While Inkey <> "" : Wend
Print : Print "hit any key to end program"
Sleep
End
```

**Output:**

```
unsorted   -5  -6  -1   0   2  -4  -7   6  -2  -3   4   7   5   1   3
  sorted   -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7
```

### FutureBasic

```mw
include "NSLog.incl"

local fn Quicksort( qs as CFMutableArrayRef, l as NSInteger, r as NSInteger )
  UInt64 size = r - l + 1
  
  if size < 2 then exit fn
  
  NSinteger i = l, j = r
  NSinteger pivot = fn NumberIntegerValue( qs[l+size / 2] )
  
  do
    while fn NumberIntegerValue( qs[i] ) < pivot
      i++
    wend
    while pivot < fn NumberIntegerValue( qs[j] )
      j--
    wend
    if ( i <= j )
      MutableArrayExchangeObjects( qs, i, j )
      i++
      j--
    end if
  until i > j
  
  if l < j then fn Quicksort( qs, l, j )
  if i < r then fn Quicksort( qs, i, r )
end fn

CFMutableArrayRef qs
CFArrayRef        unsorted
NSUInteger        i, amount

qs = fn MutableArrayWithCapacity(0)

for i = 0 to 25
  if i mod 2 == 0 then amount = 100 else amount = 10000
  MutableArrayInsertObjectAtIndex( qs, fn NumberWithInteger( rnd(amount) ), i )
next

unsorted = fn ArrayWithArray( qs )

fn QuickSort( qs, 0, len(qs) - 1  )

NSLog( @"\n-----------------\nUnsorted : Sorted\n-----------------" )
for i = 0 to 25
  NSLog( @"%8ld : %-8ld", fn NumberIntegerValue( unsorted[i] ), fn NumberIntegerValue( qs[i] ) )
next

randomize

HandleEvents
```

**Output:**

```
-----------------
Unsorted : Sorted
-----------------
      97 : 5       
    6168 : 30      
      61 : 34      
    8847 : 40      
      55 : 46      
    2570 : 49      
      40 : 55      
    4676 : 61      
      94 : 62      
     693 : 67      
      62 : 79      
    3419 : 94      
      30 : 97      
     936 : 693     
       5 : 733     
    9910 : 936     
      67 : 1395    
    8460 : 1796    
      79 : 2570    
    9352 : 3419    
      49 : 4676    
    1395 : 6168    
      34 : 8460    
     733 : 8847    
      46 : 9352    
    1796 : 9910    
```

### IS-BASIC

```mw
100 PROGRAM "QuickSrt.bas"
110 RANDOMIZE
120 NUMERIC A(5 TO 19)
130 CALL INIT(A)
140 CALL WRITE(A)
150 CALL QSORT(LBOUND(A),UBOUND(A))
160 CALL WRITE(A)
170 DEF INIT(REF A)
180   FOR I=LBOUND(A) TO UBOUND(A)
190     LET A(I)=RND(98)+1
200   NEXT
210 END DEF
220 DEF WRITE(REF A)
230   FOR I=LBOUND(A) TO UBOUND(A)
240     PRINT A(I);
250   NEXT
260   PRINT
270 END DEF
280 DEF QSORT(AH,FH)
290   NUMERIC E
300   LET E=AH:LET U=FH:LET K=A(E)
310   DO UNTIL E=U
320     DO UNTIL E=U OR A(U)<K
330       LET U=U-1
340     LOOP
350     IF E<U THEN
360       LET A(E)=A(U):LET E=E+1
370       DO UNTIL E=U OR A(E)>K
380         LET E=E+1
390       LOOP
400       IF E<U THEN LET A(U)=A(E):LET U=U-1
410     END IF
420   LOOP
430   LET A(E)=K
440   IF AH<E-1 THEN CALL QSORT(AH,E-1)
450   IF E+1<FH THEN CALL QSORT(E+1,FH)
460 END DEF
```

### PureBasic

```mw
Procedure qSort(Array a(1), firstIndex, lastIndex)
  Protected  low, high, pivotValue

  low = firstIndex
  high = lastIndex
  pivotValue = a((firstIndex + lastIndex) / 2)
  
  Repeat
    
    While a(low) < pivotValue
      low + 1
    Wend
    
    While a(high) > pivotValue
      high - 1
    Wend
    
    If low <= high
      Swap a(low), a(high)
      low + 1
      high - 1
    EndIf
    
  Until low > high
  
  If firstIndex < high
    qSort(a(), firstIndex, high)
  EndIf
  
  If low < lastIndex
    qSort(a(), low, lastIndex)
  EndIf
EndProcedure

Procedure quickSort(Array a(1))
  qSort(a(),0,ArraySize(a()))
EndProcedure
```

### QB64

```mw
' Written by Sanmayce, 2021-Oct-29
' The indexes are signed, but the elements are unsigned.
_Define A-Z As _INTEGER64
Sub Quicksort_QB64 (QWORDS~&&())
    Left = LBound(QWORDS~&&)
    Right = UBound(QWORDS~&&)
    LeftMargin = Left
    ReDim Stack&&(Left To Right)
    StackPtr = 0
    StackPtr = StackPtr + 1
    Stack&&(StackPtr + LeftMargin) = Left
    StackPtr = StackPtr + 1
    Stack&&(StackPtr + LeftMargin) = Right
    Do 'Until StackPtr = 0
        Right = Stack&&(StackPtr + LeftMargin)
        StackPtr = StackPtr - 1
        Left = Stack&&(StackPtr + LeftMargin)
        StackPtr = StackPtr - 1
        Do 'Until Left >= Right
            Pivot~&& = QWORDS~&&((Left + Right) \ 2)
            Indx = Left
            Jndx = Right
            Do
                Do While (QWORDS~&&(Indx) < Pivot~&&)
                    Indx = Indx + 1
                Loop
                Do While (QWORDS~&&(Jndx) > Pivot~&&)
                    Jndx = Jndx - 1
                Loop
                If Indx <= Jndx Then
                    If Indx < Jndx Then Swap QWORDS~&&(Indx), QWORDS~&&(Jndx)
                    Indx = Indx + 1
                    Jndx = Jndx - 1
                End If
            Loop While Indx <= Jndx
            If Indx < Right Then
                StackPtr = StackPtr + 1
                Stack&&(StackPtr + LeftMargin) = Indx
                StackPtr = StackPtr + 1
                Stack&&(StackPtr + LeftMargin) = Right
            End If
            Right = Jndx
        Loop Until Left >= Right
    Loop Until StackPtr = 0
End Sub
```

### QuickBASIC

Works with

:

FreeBASIC

Works with

:

PowerBASIC for DOS

Works with

:

QB64

Works with

:

QBasic

This is specifically for `INTEGER`s, but can be modified for any data type by changing `arr()`'s type.

```mw
DECLARE SUB quicksort (arr() AS INTEGER, leftN AS INTEGER, rightN AS INTEGER)

DIM q(99) AS INTEGER
DIM n AS INTEGER

RANDOMIZE TIMER

FOR n = 0 TO 99
    q(n) = INT(RND * 9999)
NEXT

OPEN "output.txt" FOR OUTPUT AS 1
    FOR n = 0 TO 99
        PRINT #1, q(n),
    NEXT
    PRINT #1,
    quicksort q(), 0, 99
    FOR n = 0 TO 99
        PRINT #1, q(n),
    NEXT
CLOSE

SUB quicksort (arr() AS INTEGER, leftN AS INTEGER, rightN AS INTEGER)
    DIM pivot AS INTEGER, leftNIdx AS INTEGER, rightNIdx AS INTEGER
    leftNIdx = leftN
    rightNIdx = rightN
    IF (rightN - leftN) > 0 THEN
        pivot = (leftN + rightN) / 2
        WHILE (leftNIdx <= pivot) AND (rightNIdx >= pivot)
            WHILE (arr(leftNIdx) < arr(pivot)) AND (leftNIdx <= pivot)
                leftNIdx = leftNIdx + 1
            WEND
            WHILE (arr(rightNIdx) > arr(pivot)) AND (rightNIdx >= pivot)
                rightNIdx = rightNIdx - 1
            WEND
            SWAP arr(leftNIdx), arr(rightNIdx)
            leftNIdx = leftNIdx + 1
            rightNIdx = rightNIdx - 1
            IF (leftNIdx - 1) = pivot THEN
                rightNIdx = rightNIdx + 1
                pivot = rightNIdx
            ELSEIF (rightNIdx + 1) = pivot THEN
                leftNIdx = leftNIdx - 1
                pivot = leftNIdx
            END IF
        WEND
        quicksort arr(), leftN, pivot - 1
        quicksort arr(), pivot + 1, rightN
    END IF
END SUB
```

### Run BASIC

```mw
' -------------------------------
' quick sort
' -------------------------------
size = 50
dim s(size)       ' array to sort
for i = 1 to size    ' fill it with some random numbers
 s(i) = rnd(0) * 100
next i

lft  = 1
rht  = size

[qSort]
  lftHold = lft
  rhtHold = rht
  pivot   = s(lft)
  while lft < rht
    while (s(rht) >= pivot) and (lft < rht) : rht = rht - 1 :wend
    if lft <> rht then
      s(lft) = s(rht)
      lft    = lft + 1
    end if
    while (s(lft) <= pivot) and (lft < rht) : lft = lft + 1 :wend
    if lft <> rht then
      s(rht) = s(lft)
      rht    = rht - 1
    end if
  wend

  s(lft) = pivot
  pivot  = lft
  lft    = lftHold
  rht    = rhtHold
  if lft < pivot then
    rht = pivot - 1
    goto [qSort]
  end if 
 if rht > pivot then
    lft = pivot + 1
    goto [qSort]
 end if

for i = 1 to size
 print i;"-->";s(i)
next i
```

### True BASIC

```mw
SUB quicksort (arr(), l, r)
    LET lidx = round(l)
    LET ridx = round(r)
    IF (r-l) > 0 THEN
       LET pivot = round((l+r)/2)
       DO WHILE (lidx <= pivot) AND (ridx >= pivot)
          DO WHILE (arr(lidx) < arr(pivot)) AND (lidx <= pivot)
             LET lidx = lidx+1
          LOOP
          DO WHILE (arr(ridx) > arr(pivot)) AND (ridx >= pivot)
             LET ridx = ridx-1
          LOOP
          LET temp = arr(lidx)
          LET arr(lidx) = arr(ridx)
          LET arr(ridx) = temp
          LET lidx = lidx+1
          LET ridx = ridx-1
          IF (lidx-1) = pivot THEN
             LET ridx = ridx+1
             LET pivot = ridx
          ELSEIF (ridx+1) = pivot THEN
             LET lidx = lidx-1
             LET pivot = lidx
          END IF
       LOOP
       CALL quicksort (arr(), l, pivot-1)
       CALL quicksort (arr(), pivot+1, r)
    END IF
END SUB

DIM arr(15)
LET a = round(LBOUND(arr))
LET b = round(UBOUND(arr))

RANDOMIZE
FOR n = a TO b
    LET arr(n) = round(INT(RND*99))
NEXT n

PRINT "unsort ";
FOR n = a TO b
    PRINT arr(n); " ";
NEXT n

PRINT
PRINT "  sort ";
CALL quicksort (arr(), a, b)
FOR n = a TO b
    PRINT arr(n); " ";
NEXT n
END
```

### uBasic/4tH

```mw
PRINT "Quick sort:"
  n = FUNC (_InitArray)
  PROC _ShowArray (n)
  PROC _Quicksort (n)
  PROC _ShowArray (n)
PRINT
 
END

_InnerQuick PARAM(2)
  LOCAL(4)

  IF b@ < 2 THEN RETURN
  f@ = a@ + b@ - 1
  c@ = a@
  e@ = f@
  d@ = @((c@ + e@) / 2)

  DO
    DO WHILE @(c@) < d@
      c@ = c@ + 1
    LOOP

    DO WHILE @(e@) > d@
      e@ = e@ - 1
    LOOP

    IF c@ - 1 < e@ THEN
      PROC _Swap (c@, e@)
      c@ = c@ + 1
      e@ = e@ - 1
    ENDIF

    UNTIL c@ > e@
  LOOP

  IF a@ < e@ THEN PROC _InnerQuick (a@, e@ - a@ + 1)
  IF c@ < f@ THEN PROC _InnerQuick (c@, f@ - c@ + 1)
RETURN

_Quicksort PARAM(1)                   ' Quick sort
  PROC _InnerQuick (0, a@)
RETURN
 
 
_Swap PARAM(2)                         ' Swap two array elements
  PUSH @(a@)
  @(a@) = @(b@)
  @(b@) = POP()
RETURN
 
 
_InitArray                             ' Init example array
  PUSH 4, 65, 2, -31, 0, 99, 2, 83, 782, 1
 
  FOR i = 0 TO 9
    @(i) = POP()
  NEXT
 
RETURN (i)
 
 
_ShowArray PARAM (1)                   ' Show array subroutine
  FOR i = 0 TO a@-1
    PRINT @(i),
  NEXT
 
  PRINT
RETURN
```

### VBA

This is the "simple" quicksort, using temporary arrays.

```mw
Public Sub Quick(a() As Variant, last As Integer)
' quicksort a Variant array (1-based, numbers or strings)
Dim aLess() As Variant
Dim aEq() As Variant
Dim aGreater() As Variant
Dim pivot As Variant
Dim naLess As Integer
Dim naEq As Integer
Dim naGreater As Integer

If last > 1 Then
    'choose pivot in the middle of the array
    pivot = a(Int((last + 1) / 2))
    'construct arrays
    naLess = 0
    naEq = 0
    naGreater = 0
    For Each el In a()
      If el > pivot Then
        naGreater = naGreater + 1
        ReDim Preserve aGreater(1 To naGreater)
        aGreater(naGreater) = el
      ElseIf el < pivot Then
        naLess = naLess + 1
        ReDim Preserve aLess(1 To naLess)
        aLess(naLess) = el
      Else
        naEq = naEq + 1
        ReDim Preserve aEq(1 To naEq)
        aEq(naEq) = el
      End If
    Next
    'sort arrays "less" and "greater"
    Quick aLess(), naLess
    Quick aGreater(), naGreater
    'concatenate
    P = 1
    For i = 1 To naLess
      a(P) = aLess(i): P = P + 1
    Next
    For i = 1 To naEq
      a(P) = aEq(i): P = P + 1
    Next
    For i = 1 To naGreater
      a(P) = aGreater(i): P = P + 1
    Next
End If
End Sub

Public Sub QuicksortTest()
Dim a(1 To 26) As Variant

 'populate a with numbers in descending order, then sort
 For i = 1 To 26: a(i) = 26 - i: Next
 Quick a(), 26
 For i = 1 To 26: Debug.Print a(i);: Next
 Debug.Print
 'now populate a with strings in descending order, then sort
 For i = 1 To 26: a(i) = Chr$(Asc("z") + 1 - i) & "-stuff": Next
 Quick a(), 26
 For i = 1 To 26: Debug.Print a(i); " ";: Next
 Debug.Print
End Sub
```

**Output:**

```
quicksorttest
 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 
a-stuff b-stuff c-stuff d-stuff e-stuff f-stuff g-stuff h-stuff i-stuff j-stuff k-stuff l-stuff m-stuff n-stuff o-stuff p-stuff q-stuff r-stuff s-stuff t-stuff u-stuff v-stuff w-stuff x-stuff y-stuff z-stuff 
```

Note: the "quicksort in place"

### VBScript

Translation of

:

BBC BASIC

```mw
Function quicksort(arr,s,n)
   If n < 2 Then
      Exit Function
   End If
   t = s + n - 1
   l = s
   r = t
   p = arr(Int((l + r)/2))
   Do Until l > r
      Do While arr(l) < p
         l = l + 1
      Loop
      Do While arr(r) > p
         r = r -1
      Loop
      If l <= r Then
         tmp = arr(l)
         arr(l) = arr(r)
         arr(r) = tmp
         l = l + 1
         r = r - 1
      End If
   Loop
   If s < r Then
      Call quicksort(arr,s,r-s+1)
   End If
   If l < t Then
      Call quicksort(arr,l,t-l+1)
   End If
   quicksort = arr
End Function

myarray=Array(9,8,7,6,5,5,4,3,2,1,0,-1)
m = quicksort(myarray,0,12)
WScript.Echo Join(m,",")
```

**Output:**

```
-1,0,1,2,3,4,5,5,6,7,8,9
```

### Visual Basic

Works with

:

Visual Basic

version 5

Works with

:

Visual Basic

version 6

QuickSort without swapping

```mw
Sub QuickSort(arr() As Integer, ByVal f As Integer, ByVal l As Integer)
    i = f 'First
    j = l 'Last
    Key = arr(i) 'Pivot
    Do While i < j
        Do While i < j And Key < arr(j)
            j = j - 1
        Loop
        If i < j Then arr(i) = arr(j): i = i + 1
        Do While i < j And Key > arr(i)
            i = i + 1
        Loop
        If i < j Then arr(j) = arr(i): j = j - 1
    Loop
    arr(i) = Key
    If i - 1 > f Then QuickSort arr(), f, i - 1
    If j + 1 < l Then QuickSort arr(), j + 1, l
End Sub
```

### XBasic

Translation of

:

ANSI BASIC

– Added functions for generating pseudorandom numbers.

**Note.** XBasic has also a standard function `XstQuickSort` in the *xst* library.

Works with

:

Windows XBasic

```mw
' Sorting algorithms/Quicksort
PROGRAM "quicksort"
VERSION "1.0"

IMPORT "xst"

DECLARE FUNCTION Entry ()
DECLARE FUNCTION QuickSort (@arr%[], l%%, r%%)
' Pseudo-random number generator
' Based on the rand, srand functions from Kernighan & Ritchie's book
' 'The C Programming Language'
DECLARE FUNCTION Rand()
DECLARE FUNCTION SRand(seed%%)

FUNCTION Entry ()
  DIM arr%[19]
  a%% = 0
  b%% = UBOUND(arr%[])
  XstGetSystemTime (@msec)
  SRand(INT(msec) MOD 32768)
  FOR i%% = a%% TO b%%
    arr%[i%%] = INT(Rand() / 32768.0 * 99.0)
  NEXT i%%
  PRINT "Unsorted:"
  FOR i%% = a%% TO b%%
    PRINT FORMAT$("## ", arr%[i%%]);
  NEXT i%%
  PRINT
  PRINT "Sorted:"
  QuickSort(@arr%[], a%%, b%%)
  FOR i%% = a%% TO b%%
    PRINT FORMAT$("## ", arr%[i%%]);
  NEXT i%%
  PRINT
END FUNCTION

FUNCTION QuickSort (@arr%[], l%%, r%%)
  leftIndex%% = l%%
  rightIndex%% = r%%
  IF r%% > l%% THEN
    pivot%% = (l%% + r%%) \ 2
    DO WHILE (leftIndex%% <= pivot%%) AND (rightIndex%% >= pivot%%)
      DO WHILE (arr%[leftIndex%%] < arr%[pivot%%]) AND (leftIndex%% <= pivot%%)
        INC leftIndex%%
      LOOP
      DO WHILE (arr%[rightIndex%%] > arr%[pivot%%]) AND (rightIndex%% >= pivot%%)
        DEC rightIndex%%
      LOOP
      SWAP arr%[leftIndex%%], arr%[rightIndex%%]
      INC leftIndex%%
      DEC rightIndex%%
      SELECT CASE TRUE
        CASE leftIndex%% - 1 = pivot%%:
          INC rightIndex%%
          pivot%% = rightIndex%%
        CASE rightIndex%% + 1 = pivot%%:
          DEC leftIndex%%
          pivot%% = leftIndex%%
      END SELECT
    LOOP
    QuickSort (@arr%[], l%%, pivot%% - 1)
    QuickSort (@arr%[], pivot%% + 1, r%%)
  END IF
END FUNCTION

' Return pseudo-random integer on 0..32767
FUNCTION Rand()
  #next&& = #next&& * 1103515245 + 12345
END FUNCTION USHORT(#next&& / 65536) MOD 32768

' Set seed for Rand()
FUNCTION SRand(seed%%)
  #next&& = seed%%
END FUNCTION
END PROGRAM
```

**Output:**

(example)

```
Unsorted:
18 37 79 14 23 13 64 37 84 37 22 64 25 43 26 13 12 83 21 41 
Sorted:
12 13 13 14 18 21 22 23 25 26 37 37 37 41 43 64 64 79 83 84  
```

### Yabasic

Rosetta Code problem: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort

by Jjuanhdez, 03/2023

```mw
dim array(15)
a = 0
b = arraysize(array(),1)

for i = a to b 
    array(i) = ran(1000)
next i

print "unsort ";
for i = a to b 
   print array(i) using("####"); 
   if i = b then print ""; else print ", "; : fi
next i

quickSort(array(), a, b)

print "\n  sort ";
for i = a to b 
    print array(i) using("####"); 
    if i = b then print ""; else print ", "; : fi
next i
print
end

sub quickSort(array(), l, r)
    local asize, i, j, pivot
    
    size = r - l +1
    if size < 2  return
    
    i = l
   j = r
    pivot = array(l + int(size / 2))
    
    repeat
        while array(i) < pivot
            i = i + 1
        wend
        while pivot < array(j)
            j = j - 1
        wend
        if i <= j then
            temp = array(i)
            array(i) = array(j)
            array(j) = temp
            i = i + 1
            j = j - 1
        fi
    until i > j
    
    if l < j  quickSort(array(), l, j)
    if i < r  quickSort(array(), i, r)
end sub
```

**Output:**

```
unsort  582,  796,  598,  478,   27,  125,  477,  679,  133,  513,  154,   93,  451,  463,   20
  sort   20,   27,   93,  125,  133,  154,  451,  463,  477,  478,  513,  582,  598,  679,  796
```


## BCPL

```mw
// This can be run using Cintcode BCPL freely available from www.cl.cam.ac.uk/users/mr10.

GET "libhdr.h"

LET quicksort(v, n) BE qsort(v+1, v+n)

AND qsort(l, r) BE
{ WHILE l+8<r DO
  { LET midpt = (l+r)/2
    // Select a good(ish) median value.
    LET val   = middle(!l, !midpt, !r)
    LET i = partition(val, l, r)
    // Only use recursion on the smaller partition.
    TEST i>midpt THEN { qsort(i, r);   r := i-1 }
                 ELSE { qsort(l, i-1); l := i   }
  }

  FOR p = l+1 TO r DO  // Now perform insertion sort.
   FOR q = p-1 TO l BY -1 TEST q!0<=q!1 THEN BREAK
                                        ELSE { LET t = q!0
                                               q!0 := q!1
                                               q!1 := t
                                             }
}

AND middle(a, b, c) = a<b -> b<c -> b,
                                    a<c -> c,
                                           a,
                             b<c -> a<c -> a,
                                           c,
                                    b

AND partition(median, p, q) = VALOF
{ LET t = ?
  WHILE !p < median DO p := p+1
  WHILE !q > median DO q := q-1
  IF p>=q RESULTIS p
  t  := !p
  !p := !q
  !q := t
  p, q := p+1, q-1
} REPEAT

LET start() = VALOF {
  LET v = VEC 1000
  FOR i = 1 TO 1000 DO v!i := randno(1_000_000)
  quicksort(v, 1000)
  FOR i = 1 TO 1000 DO
  { IF i MOD 10 = 0 DO newline()
    writef(" %i6", v!i)
  }
  newline()
}
```


## Beads

```mw
beads 1 program Quicksort

calc main_init
   var arr = [1, 3, 5, 1, 7, 9, 8, 6, 4, 2]
   var arr2 = arr
   quicksort(arr, 1, tree_count(arr))
   var tempStr : str
   loop across:arr index:ix
      tempStr = tempStr & ' ' & to_str(arr[ix])
   log tempStr

calc quicksort(
   arr:array of num
   startIndex
   highIndex
   )
   if (startIndex < highIndex)
      var partitionIndex = partition(arr, startIndex, highIndex)
      quicksort(arr, startIndex, partitionIndex - 1)
      quicksort(arr, partitionIndex+1, highIndex)

calc partition(
   arr:array of num
   startIndex
   highIndex
   ):num
   var pivot = arr[highIndex]
   var i = startIndex - 1
   var j = startIndex
   loop while:(j <= highIndex - 1)
      if arr[j] < pivot
         inc i
         swap arr[i] <=> arr[j]
      inc j
   swap arr[i+1] <=> arr[highIndex]
   return (i+1)
```

**Output:**

```
1 1 2 3 4 5 6 7 8 9
```


## Bracmat

Instead of comparing elements explicitly, this solution puts the two elements-to-compare in a sum. After evaluating the sum its terms are sorted. Numbers are sorted numerically, strings alphabetically and compound expressions by comparing nodes and leafs in a left-to right order. Now there are three cases: either the terms stayed put, or they were swapped, or they were equal and were combined into one term with a factor `2` in front. To not let the evaluator add numbers together, each term is constructed as a dotted list.

```mw
( ( Q
  =   Less Greater Equal pivot element
    .     !arg:%(?pivot:?Equal) %?arg
        & :?Less:?Greater
        &   whl
          ' ( !arg:%?element ?arg
            &   (.!element)+(.!pivot)               { BAD: 1900+90 adds to 1990,  GOOD: (.1900)+(.90) is sorted to (.90)+(.1900) }
              : (   (.!element)+(.!pivot)
                  & !element !Less:?Less
                |   (.!pivot)+(.!element)
                  & !element !Greater:?Greater
                | ?&!element !Equal:?Equal
                )
            )
        & Q$!Less !Equal Q$!Greater
      | !arg
  )
& out$Q$(1900 optimized variants of 4001/2 Quicksort (quick,sort) are (quick,sober) features of 90 languages)
);
```

**Output:**

```
  90
  1900
  4001/2
  Quicksort
  are
  features
  languages
  of
  of
  optimized
  variants
  (quick,sober)
  (quick,sort)
```


## Bruijn

```mw
:import std/Combinator .
:import std/Number .
:import std/List .

sort y [[0 [[[case-sort]]] case-end]]
   case-sort (4 lesser) ++ (2 : (4 greater))
      lesser (\lt? 2) <#> 1
      greater (\ge? 2) <#> 1
   case-end empty

:test (sort ((+3) : ((+2) : {}(+1)))) ((+1) : ((+2) : {}(+3)))
```


## C

```mw
#include <stdio.h>

void quicksort(int *A, int len);

int main (void) {
  int a[] = {4, 65, 2, -31, 0, 99, 2, 83, 782, 1};
  int n = sizeof a / sizeof a[0];

  int i;
  for (i = 0; i < n; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");

  quicksort(a, n);

  for (i = 0; i < n; i++) {
    printf("%d ", a[i]);
  }
  printf("\n");

  return 0;
}

void quicksort(int *A, int len) {
  if (len < 2) return;

  int pivot = A[len / 2];

  int i, j;
  for (i = 0, j = len - 1; ; i++, j--) {
    while (A[i] < pivot) i++;
    while (A[j] > pivot) j--;

    if (i >= j) break;

    int temp = A[i];
    A[i]     = A[j];
    A[j]     = temp;
  }

  quicksort(A, i);
  quicksort(A + i, len - i);
}
```

**Output:**

```
4 65 2 -31 0 99 2 83 782 1
-31 0 1 2 2 4 65 83 99 782
```

Randomized sort with separated components.

```mw
#include <stdlib.h>     // REQ: rand()

void swap(int *a, int *b) {
  int c = *a;
  *a = *b;
  *b = c;
}

int partition(int A[], int p, int q) {
  swap(&A[p + (rand() % (q - p + 1))], &A[q]);   // PIVOT = A[q]

  int i = p - 1;
  for(int j = p; j <= q; j++) {
    if(A[j] <= A[q]) {
      swap(&A[++i], &A[j]);
    }
  }

  return i;
}

void quicksort(int A[], int p, int q) {
  if(p < q) {
    int pivotIndx = partition(A, p, q);

    quicksort(A, p, pivotIndx - 1);
    quicksort(A, pivotIndx + 1, q);
  }
}
```


## C

```mw
//
// The Tripartite conditional enables Bentley-McIlroy 3-way Partitioning.
// This performs additional compares to isolate islands of keys equal to
// the pivot value.  Use unless key-equivalent classes are of small size.
//
#define Tripartite

namespace RosettaCode {
  using System;
  using System.Diagnostics;

  public class QuickSort<T> where T : IComparable {
    #region Constants
    public const UInt32 INSERTION_LIMIT_DEFAULT = 12;
    private const Int32 SAMPLES_MAX = 19;
    #endregion

    #region Properties
    public UInt32 InsertionLimit { get; }
    private T[] Samples { get; }
    private Int32 Left { get; set; }
    private Int32 Right { get; set; }
    private Int32 LeftMedian { get; set; }
    private Int32 RightMedian { get; set; }
    #endregion

    #region Constructors
    public QuickSort(UInt32 insertionLimit = INSERTION_LIMIT_DEFAULT) {
      this.InsertionLimit = insertionLimit;
      this.Samples = new T[SAMPLES_MAX];
    }
    #endregion

    #region Sort Methods
    public void Sort(T[] entries) {
      Sort(entries, 0, entries.Length - 1);
    }

    public void Sort(T[] entries, Int32 first, Int32 last) {
      var length = last + 1 - first;
      while (length > 1) {
        if (length < InsertionLimit) {
          InsertionSort<T>.Sort(entries, first, last);
          return;
        }

        Left = first;
        Right = last;
        var median = pivot(entries);
        partition(median, entries);
        //[Note]Right < Left

        var leftLength = Right + 1 - first;
        var rightLength = last + 1 - Left;

        //
        // First recurse over shorter partition, then loop
        // on the longer partition to elide tail recursion.
        //
        if (leftLength < rightLength) {
          Sort(entries, first, Right);
          first = Left;
          length = rightLength;
        }
        else {
          Sort(entries, Left, last);
          last = Right;
          length = leftLength;
        }
      }
    }

    /// <summary>Return an odd sample size proportional to the log of a large interval size.</summary>
    private static Int32 sampleSize(Int32 length, Int32 max = SAMPLES_MAX) {
      var logLen = (Int32)Math.Log10(length);
      var samples = Math.Min(2 * logLen + 1, max);
      return Math.Min(samples, length);
    }

    /// <summary>Estimate the median value of entries[Left:Right]</summary>
    /// <remarks>A sample median is used as an estimate the true median.</remarks>
    private T pivot(T[] entries) {
      var length = Right + 1 - Left;
      var samples = sampleSize(length);
      // Sample Linearly:
      for (var sample = 0; sample < samples; sample++) {
        // Guard against Arithmetic Overflow:
        var index = (Int64)length * sample / samples + Left;
        Samples[sample] = entries[index];
      }

      InsertionSort<T>.Sort(Samples, 0, samples - 1);
      return Samples[samples / 2];
    }

    private void partition(T median, T[] entries) {
      var first = Left;
      var last = Right;
#if Tripartite
      LeftMedian = first;
      RightMedian = last;
#endif
      while (true) {
        //[Assert]There exists some index >= Left where entries[index] >= median
        //[Assert]There exists some index <= Right where entries[index] <= median
        // So, there is no need for Left or Right bound checks
        while (median.CompareTo(entries[Left]) > 0) Left++;
        while (median.CompareTo(entries[Right]) < 0) Right--;

        //[Assert]entries[Right] <= median <= entries[Left]
        if (Right <= Left) break;

        Swap(entries, Left, Right);
        swapOut(median, entries);
        Left++;
        Right--;
        //[Assert]entries[first:Left - 1] <= median <= entries[Right + 1:last]
      }

      if (Left == Right) {
        Left++;
        Right--;
      }
      //[Assert]Right < Left
      swapIn(entries, first, last);

      //[Assert]entries[first:Right] <= median <= entries[Left:last]
      //[Assert]entries[Right + 1:Left - 1] == median when non-empty
    }
    #endregion

    #region Swap Methods
    [Conditional("Tripartite")]
    private void swapOut(T median, T[] entries) {
      if (median.CompareTo(entries[Left]) == 0) Swap(entries, LeftMedian++, Left);
      if (median.CompareTo(entries[Right]) == 0) Swap(entries, Right, RightMedian--);
    }

    [Conditional("Tripartite")]
    private void swapIn(T[] entries, Int32 first, Int32 last) {
      // Restore Median entries
      while (first < LeftMedian) Swap(entries, first++, Right--);
      while (RightMedian < last) Swap(entries, Left++, last--);
    }

    /// <summary>Swap entries at the left and right indicies.</summary>
    public void Swap(T[] entries, Int32 left, Int32 right) {
      Swap(ref entries[left], ref entries[right]);
    }

    /// <summary>Swap two entities of type T.</summary>
    public static void Swap(ref T e1, ref T e2) {
      var e = e1;
      e1 = e2;
      e2 = e;
    }
    #endregion
  }

  #region Insertion Sort
  static class InsertionSort<T> where T : IComparable {
    public static void Sort(T[] entries, Int32 first, Int32 last) {
      for (var next = first + 1; next <= last; next++)
        insert(entries, first, next);
    }

    /// <summary>Bubble next entry up to its sorted location, assuming entries[first:next - 1] are already sorted.</summary>
    private static void insert(T[] entries, Int32 first, Int32 next) {
      var entry = entries[next];
      while (next > first && entries[next - 1].CompareTo(entry) > 0)
        entries[next] = entries[--next];
      entries[next] = entry;
    }
  }
  #endregion
}
```

**Example**:

```mw
  using Sort;
  using System;

  class Program {
    static void Main(String[] args) {
      var entries = new Int32[] { 1, 3, 5, 7, 9, 8, 6, 4, 2 };
      var sorter = new QuickSort<Int32>();
      sorter.Sort(entries);
      Console.WriteLine(String.Join(" ", entries));
    }
  }
```

**Output:**

```
1 2 3 4 5 6 7 8 9
```

A very inefficient way to do qsort in C# to prove C# code can be just as compact and readable as any dynamic code

```mw
using System;
using System.Collections.Generic;
using System.Linq;

namespace QSort
{
    class QSorter
    {
        private static IEnumerable<IComparable> empty = new List<IComparable>();

        public static IEnumerable<IComparable> QSort(IEnumerable<IComparable> iEnumerable)
        {
            if(iEnumerable.Any())
            {
                var pivot = iEnumerable.First();
                return QSort(iEnumerable.Where((anItem) => pivot.CompareTo(anItem) > 0)).
                    Concat(iEnumerable.Where((anItem) => pivot.CompareTo(anItem) == 0)).
                    Concat(QSort(iEnumerable.Where((anItem) => pivot.CompareTo(anItem) < 0)));
            }
            return empty;
        }
    }
}
```


## CafeOBJ

There is no builtin list type in CafeOBJ, so a user written list module is included.

```mw
mod! SIMPLE-LIST(X :: TRIV){
[NeList < List ]
op [] : -> List
op [_] : Elt -> List 
op (_:_) : Elt List -> NeList  -- consr
op _++_ : List List -> List {assoc}  -- concatenate
var E : Elt
vars L L' : List
eq [ E ] = E : [] .
eq [] ++ L = L .
eq (E : L) ++ L' = E : (L ++ L') .
}

mod! QUICKSORT{
pr(SIMPLE-LIST(NAT))
op qsort_ : List -> List 
op smaller__ : List  Nat -> List
op larger__ : List Nat -> List

vars x y : Nat
vars xs ys : List

eq qsort []  = [] .
eq qsort (x : xs) = (qsort (smaller xs x)) ++ [ x ]  ++ (qsort (larger xs x)) .

eq smaller []  x = [] .
eq smaller (x : xs) y = if x <= y then  (x : (smaller xs y)) else (smaller xs y) fi .
eq larger []  x  = [] .
eq larger (x : xs) y = if x <= y then (larger xs  y) else (x : (larger xs y)) fi   .

}
open  QUICKSORT .
red qsort(5 : 4 : 3 : 2 : 1 : 0 : []) .
red qsort(5 : 5 : 4 : 3 : 5 : 2 : 1 : 1 : 0 : []) .
eof
```


## C++

The following implements quicksort with a median-of-three pivot. As idiomatic in C++, the argument last is a one-past-end iterator. Note that this code takes advantage of std::partition, which is O(n). Also note that it needs a random-access iterator for efficient calculation of the median-of-three pivot (more exactly, for O(1) calculation of the iterator mid).

```mw
#include <iterator>
#include <algorithm> // for std::partition
#include <functional> // for std::less

// helper function for median of three
template<typename T>
 T median(T t1, T t2, T t3)
{
  if (t1 < t2)
  {
    if (t2 < t3)
      return t2;
    else if (t1 < t3)
      return t3;
    else
      return t1;
  }
  else
  {
    if (t1 < t3)
      return t1;
    else if (t2 < t3)
      return t3;
    else
      return t2;
  }
}

// helper object to get <= from <
template<typename Order> struct non_strict_op:
  public std::binary_function<typename Order::second_argument_type,
                              typename Order::first_argument_type,
                              bool>
{
  non_strict_op(Order o): order(o) {}
  bool operator()(typename Order::second_argument_type arg1,
                  typename Order::first_argument_type arg2) const
  {
    return !order(arg2, arg1);
  }
private:
  Order order;
};

template<typename Order> non_strict_op<Order> non_strict(Order o)
{
  return non_strict_op<Order>(o);
}

template<typename RandomAccessIterator,
         typename Order>
 void quicksort(RandomAccessIterator first, RandomAccessIterator last, Order order)
{
  if (first != last && first+1 != last)
  {
    typedef typename std::iterator_traits<RandomAccessIterator>::value_type value_type;
    RandomAccessIterator mid = first + (last - first)/2;
    value_type pivot = median(*first, *mid, *(last-1));
    RandomAccessIterator split1 = std::partition(first, last, std::bind2nd(order, pivot));
    RandomAccessIterator split2 = std::partition(split1, last, std::bind2nd(non_strict(order), pivot));
    quicksort(first, split1, order);
    quicksort(split2, last, order);
  }
}

template<typename RandomAccessIterator>
 void quicksort(RandomAccessIterator first, RandomAccessIterator last)
{
  quicksort(first, last, std::less<typename std::iterator_traits<RandomAccessIterator>::value_type>());
}
```

A simpler version of the above that just uses the first element as the pivot and only does one "partition".

```mw
#include <iterator>
#include <algorithm> // for std::partition
#include <functional> // for std::less

template<typename RandomAccessIterator,
         typename Order>
 void quicksort(RandomAccessIterator first, RandomAccessIterator last, Order order)
{
  if (last - first > 1)
  {
    RandomAccessIterator split = std::partition(first+1, last, std::bind2nd(order, *first));
    std::iter_swap(first, split-1);
    quicksort(first, split-1, order);
    quicksort(split, last, order);
  }
}

template<typename RandomAccessIterator>
 void quicksort(RandomAccessIterator first, RandomAccessIterator last)
{
  quicksort(first, last, std::less<typename std::iterator_traits<RandomAccessIterator>::value_type>());
}
```


## Clojure

A very Haskell-like solution using list comprehensions and lazy evaluation.

```mw
(defn qsort [L]
  (if (empty? L) 
      '()
      (let [[pivot & L2] L]
           (lazy-cat (qsort (for [y L2 :when (<  y pivot)] y))
                     (list pivot)
                     (qsort (for [y L2 :when (>= y pivot)] y))))))
```

Another short version (using quasiquote):

```mw
(defn qsort [[pvt & rs]]
  (if pvt
    `(~@(qsort (filter #(<  % pvt) rs))
      ~pvt 
      ~@(qsort (filter #(>= % pvt) rs)))))
```

Another, more readable version (no macros):

```mw
(defn qsort [[pivot & xs]]
  (when pivot
    (let [smaller #(< % pivot)]
      (lazy-cat (qsort (filter smaller xs))
      [pivot]
      (qsort (remove smaller xs))))))
```

A 3-group quicksort (fast when many values are equal):

```mw
(defn qsort3 [[pvt :as coll]]
  (when pvt
    (let [{left -1 mid 0 right 1} (group-by #(compare % pvt) coll)]
      (lazy-cat (qsort3 left) mid (qsort3 right)))))
```

A lazier version of above (unlike group-by, filter returns (and reads) a lazy sequence)

```mw
(defn qsort3 [[pivot :as coll]]
  (when pivot
    (lazy-cat (qsort (filter #(< % pivot) coll))
              (filter #{pivot} coll)
              (qsort (filter #(> % pivot) coll)))))
```


## COBOL

Works with

:

Visual COBOL

```mw
       IDENTIFICATION DIVISION.
       PROGRAM-ID. quicksort RECURSIVE.
       
       DATA DIVISION.
       LOCAL-STORAGE SECTION.
       01  temp                   PIC S9(8).
       
       01  pivot                  PIC S9(8).
       
       01  left-most-idx          PIC 9(5).
       01  right-most-idx         PIC 9(5).
       
       01  left-idx               PIC 9(5).
       01  right-idx              PIC 9(5).
       
       LINKAGE SECTION.
       78  Arr-Length             VALUE 50.
       
       01  arr-area.
           03  arr                PIC S9(8) OCCURS Arr-Length TIMES.
           
       01  left-val               PIC 9(5).
       01  right-val              PIC 9(5).  
       
       PROCEDURE DIVISION USING REFERENCE arr-area, OPTIONAL left-val,
               OPTIONAL right-val.
           IF left-val IS OMITTED OR right-val IS OMITTED
               MOVE 1 TO left-most-idx, left-idx
               MOVE Arr-Length TO right-most-idx, right-idx
           ELSE
               MOVE left-val TO left-most-idx, left-idx
               MOVE right-val TO right-most-idx, right-idx
           END-IF
           
           IF right-most-idx - left-most-idx < 1
               GOBACK
           END-IF
       
           COMPUTE pivot = arr ((left-most-idx + right-most-idx) / 2)
       
           PERFORM UNTIL left-idx > right-idx
               PERFORM VARYING left-idx FROM left-idx BY 1
                   UNTIL arr (left-idx) >= pivot
               END-PERFORM
               
               PERFORM VARYING right-idx FROM right-idx BY -1
                   UNTIL arr (right-idx) <= pivot
               END-PERFORM
               
               IF left-idx <= right-idx
                   MOVE arr (left-idx) TO temp
                   MOVE arr (right-idx) TO arr (left-idx)
                   MOVE temp TO arr (right-idx)
                   
                   ADD 1 TO left-idx
                   SUBTRACT 1 FROM right-idx
               END-IF
           END-PERFORM
       
           CALL "quicksort" USING REFERENCE arr-area,
               CONTENT left-most-idx, right-idx
           CALL "quicksort" USING REFERENCE arr-area, CONTENT left-idx,
               right-most-idx
               
           GOBACK
           .
```


## CoffeeScript

```mw
quicksort = ([x, xs...]) ->
  return [] unless x?
  smallerOrEqual = (a for a in xs when a <= x)
  larger = (a for a in xs when a > x)
  (quicksort smallerOrEqual).concat(x).concat(quicksort larger)
```
