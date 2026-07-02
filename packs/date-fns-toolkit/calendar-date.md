---
title: "Calendar date"
source: https://en.wikipedia.org/wiki/Calendar_date
domain: date-fns-toolkit
license: CC-BY-SA-4.0
tags: date-fns, date utility functions, immutable date library, javascript date formatting
fetched: 2026-07-02
---

# Calendar date

A **calendar date** is a reference to a particular day, represented within a calendar system, enabling a specific day to be unambiguously identified. Simple math can be performed between dates; commonly, the number of days between two dates may be calculated, e.g., "25 July 2026" is ten days after "15 July 2026". The date of a particular event depends on the time zone used to record it. For example, the air attack on Pearl Harbor that began at 7:48 a.m. local Hawaiian time (HST) on 7 December 1941 is recorded equally as having happened on 8 December at 3:18 a.m. Japan Standard Time (JST).

A particular day may be assigned a different nominal date according to the calendar used. The de facto standard for recording dates worldwide is the Gregorian calendar, the world's most widely used civil calendar. Many cultures use religious calendars such as the Gregorian (Western Christendom, AD), the Julian calendar (Eastern Christendom, AD), Hebrew calendar (Judaism, AM), the Hijri calendars (Islam, AH), or any other of the many calendars used around the world. Regnal calendars (that record a date in terms of years since the beginning of the monarch's reign) are also used in some places, for particular purposes.

In most calendar systems, the date consists of three parts: the (numbered) *day of the month*, the *month*, and the (numbered) *year*. There may also be additional parts, such as the *day of the week*. Years are counted from a particular starting point called the *epoch*, with *era* referring to the span of time since that epoch. A date without the year may also be referred to as a *date* or *calendar date* (such as "2 July" rather than "2 July 2026"). As such, it is either shorthand for the current year, or else it defines the day of an annual event such as a birthday on 25 March or Christmas on 25 December.

## Date format

A large variety of formats for dates is in use in line with differing national or other convention, that differ according to the order of date element and separators. For example the date "25 March 1995" can be written as 25/03/1995 (DMY convention), 03/25/1995 (MDY convention), 1995/03/25 (YMD convention); using different types of separator (e.g., 25.03.1995, 25/03/1995, 25-03-1995, 25 03 1995), whether leading zeros are included (e.g. 25/3/1995 vs. 25/03/1995), whether all four digits of the year are written (e.g., 25.03.1995 vs. 25.03.95), and whether the month is represented in Arabic or Roman numerals or by name (e.g. 25.03.1995, 25.III.1995, 25 March 1995). The format chosen for display of the date can be location or user dependent and is sometimes called a **date mask** in database administration. Actual presentation in a given context is controlled by input masks and output masks. (The name comes from the metaphor that, just as the same person can look different superficially by putting on any of various masks in a masquerade, the underlying value representing a date can have different presentations.)

### Gregorian, day–month–year (DMY)

This little-endian sequence is used by a majority of the world and is the preferred form by the United Nations when writing the full date format in official documents. This date format originates from the custom of writing the date as "the Nth day of [month] in the year of our Lord [year]" in Western religious and legal documents. The format has shortened over time but the order of the elements has remained constant. The following examples use the date of 25 March 1995. In the case of two-digit years, care must be taken to ensure that they are not interpreted as belonging to a different century (e.g. "01" being interpreted as "1901" instead of "2001"). The dots function as ordinal dots.

- 25 March 1995
- 25/3/1995 or 25/03/1995
- 25.3.1995 or 25.03.1995
- 25. 3. 1995 or 25. 03. 1995
- 25-3-1995 or 25-03-1995
- 25-Mar-1995
- 25Mar95 – Used, including in the U.S., where space needs to be saved by skipping punctuation (often seen on the dateline of Internet news articles).
- [The] 25th [of] March 1995 – 'The' and 'of' are often spoken but generally omitted in all but the most formal writing such as legal documents.
- 25/Mar/1995 – used in the Common Log Format
- Saturday, 25 March 1995
- 25/iii/95, 25.iii.95, 25-iii.95, 25/iii-95, 25.III.1995, 25. III. 1995 or 25 III 1995 (using the Roman numeral for the month) – In the past, this was a common and typical way of distinguishing day from month and was widely used in many countries, but recently this practice has been affected by the general retreat from the use of Roman numerals. This is usually confined to handwriting only and is not put into any form of print. It is associated with a number of schools and universities. It has also been used by the Vatican as an alternative to using months named after Roman deities. It is used on Canadian postmarks as a bilingual form of the month. It was also commonly used in the Soviet Union, in both handwriting and print.
- 25 March 1995 CE or 25 March 1995 AD

### Gregorian, year–month–day (YMD)

In this format, the most significant data item is written before lesser data items i.e. the year before the month before the day. It is consistent with the big-endianness of the Hindu–Arabic numeral system, which progresses from the highest to the lowest order magnitude. That is, using this format textual orderings and chronological orderings are identical. This form is standard in East Asia, Iran, Lithuania, Hungary, and Sweden; and some other countries to a limited extent.

Examples for the 25th of March 1995:

- 1995-03-25: the standard Internet date/time format, a profile of the international standard ISO 8601, orders the components of a date like this, and additionally uses leading zeros, for example, 1995-03-25, to be easily read and sorted by computers. It is used with UTC in RFC 3339. This format is also favored in certain Asian countries, mainly East Asian countries, as well as in some European countries. The big-endian convention is also frequently used in Canada, but all three conventions are used there (both endians and the American MMDDYYYY format are allowed on Canadian bank cheques provided that the layout of the cheque makes it clear which style is to be used).
- 1995 March 25
- 1995Mar25
- 1995-Mar-25
- 1995-Mar-25, Saturday
- 1995. march 25. – The official format in Hungary, point after year and day, month name with small initial. Following shorter formats also can be used: 1995. mar. 25., 1995. 03. 25., 1995. III. 25.
- 1995.3.25 or 1995.03.25
- 1995/3/25 or 1995/03/25
- 95/3/25 or 95/03/25
- 19950325 : the "basic format" profile of ISO 8601, an 8-digit number providing monotonic date codes, common in computing and increasingly used in dated computer file names. It is used in the standard iCalendar file format defined in RFC 5545.

It is also extended through the universal big-endian format clock time: 1995 March 25, 18h 14m 12s, or 1995/03/25/18:14:12 or (ISO 8601) 1995-03-25T18:14:12.

### Gregorian, month–day–year (MDY)

This sequence is used primarily in the Philippines and the United States. It is also used to varying extents in Canada (though never in Quebec). This date format was commonly used alongside the little-endian form in the United Kingdom until the mid-20th century and can be found in both defunct and modern print media, such as the *London Gazette* and *The Times*, respectively. This format was also commonly used by several English-language print media in many former British colonies and also one of two formats commonly used in India during British Raj era until the mid-20th century.

- Saturday, March 25, 1995
- March 25, 1995
- Mar 25, 1995
- Mar-25-1995
- Mar-25-1995
- 3/25/1995 or 03/25/1995
- 3-25-1995 or 03-25-1995
- 3.25.1995 or 03.25.1995
- 3.25.95 or 03.25.95
- 3/25/95 or 03/25/95

Modern style guides recommend avoiding the use of the ordinal (e.g. 1st, 2nd, 3rd, 4th) form of numbers when the day follows the month (July 4), and that format is not included in ISO standards. The ordinal was common in the past and is still sometimes used ([the] 4th [of] July or July 4th).

### Gregorian, year–day–month (YDM)

This date format is used in Kazakhstan, Latvia, Nepal, and Turkmenistan. According to the official rules of documenting dates by governmental authorities, the long date format in Kazakh is written in the year–day–month order, e.g. 1995 25 March (Kazakh: 1995 жылғы 25 наурыз). However, both Latvia and Kazakhstan use the day-month-year format (DD.MM.YYYY or DD/MM/YYYY) for all-numeric dates. None of these four countries use the all-numeric date format YYYY.DD.MM

### Standards

There are several standards that specify date formats:

- ISO 8601 *Data elements and interchange formats – Information interchange – Representation of dates and times* specifies *YYYY-MM-DD* (the separators are optional, but only hyphens are allowed to be used), where all values are fixed length numeric, but also allows *YYYY-DDD*, where *DDD* is the ordinal number of the day within the year, e.g. 2001–365.
- RFC 3339 *Date and Time on the Internet: Timestamps* specifies *YYYY-MM-DD*, i.e. a particular subset of the options allowed by ISO 8601.
- RFC 5322 *Internet Message Format* specifies *day month year* where *day* is one or two digits, *month* is a three letter month abbreviation, and *year* is four digits.

### Difficulties

Many numerical forms can create confusion when used in international correspondence, particularly when abbreviating the year to its final two digits, with no context. For example, "07/08/06" could refer to either 7 August 2006 or July 8, 2006 (or 1906, or the sixth year of any century), or 2007 August 6.

The date format of YYYY-MM-DD in ISO 8601, as well as other international standards, have been adopted for many applications for reasons including reducing transnational ambiguity and simplifying machine processing.

An early U.S. Federal Information Processing Standard recommended 2-digit years. This is now widely recognized as extremely problematic, because of the year 2000 problem. Some U.S. government agencies now use ISO 8601 with 4-digit years.

When transitioning from one calendar or date notation to another, a format that includes both styles may be developed; for example Old Style and New Style dates in the transition from the Julian to the Gregorian calendar.

## Advantages for ordering in sequence

One of the advantages of using the ISO 8601 date format is that the lexicographical order (ASCIIbetical) of the representations is equivalent to the chronological order of the dates, assuming that all dates are in the same time zone. Thus dates can be sorted using simple string comparison algorithms, and indeed by any left to right collation. For example:

```
2003-02-28 (28 February 2003) sorts before
2006-03-01 (1 March 2006) which sorts before
2015-01-30 (30 January 2015)
```

The YYYY-MM-DD layout is the only common format that can provide this. Sorting other date representations involves some parsing of the date strings. This also works when a time in 24-hour format is included after the date, as long as all times are understood to be in the same time zone.

ISO 8601 is used widely where concise, human-readable yet easily computable and unambiguous dates are required, although many applications store dates internally as UNIX time and only convert to ISO 8601 for display. All modern computer Operating Systems retain date information of files outside of their titles, allowing the user to choose which format they prefer and have them sorted thus, irrespective of the files' names.

## Specialized usage

### Day and year only

The U.S. military sometimes uses a system, known to them as the "Julian date format", which indicates the year and the actual day out of the 365 days of the year (and thus a designation of the month would not be needed). For example, "11 December 1999" can be written in some contexts as "1999345" or "99345", for the 345th day of 1999. This system is most often used in US military logistics since it simplifies the process of calculating estimated shipping and arrival dates. For example: say a tank engine takes an estimated 35 days to ship by sea from the US to South Korea. If the engine is sent on 06104 (Friday, 14 April 2006), it should arrive on 06139 (Friday, 19 May). Outside of the US military and some US government agencies, including the Internal Revenue Service, this format is usually referred to as "ordinal date", rather than "Julian date".

Such ordinal date formats are also used by many computer programs (especially those for mainframe systems). Using a three-digit Julian day number saves one byte of computer storage over a two-digit month plus two-digit day, for example, "January 17" is 017 in Julian versus 0117 in month-day format. OS/390 or its successor, z/OS, display dates in yy.ddd format for most operations.

UNIX time stores time as a number in seconds since the beginning of the UNIX Epoch (1970-01-01).

Another "ordinal" date system ("ordinal" in the sense of advancing in value by one as the date advances by one day) is in common use in astronomical calculations and referencing and uses the same name as this "logistics" system. The continuity of representation of period regardless of the time of year being considered is highly useful to both groups of specialists. The astronomers describe their system as also being a "Julian date" system.

### Week number used

Companies in Europe often use year, week number, and day for planning purposes. So, for example, an event in a project can happen on `w43` (week 43) or `w43-1` (Monday, week 43) or, if the year needs to be indicated, on `w0643` (the year 2006, week 43; i.e., Monday 23 October–Sunday 29 October 2006).

An ISO week-numbering year has 52 or 53 full weeks. That is 364 or 371 days instead of the conventional Gregorian year of 365 or 366 days. These 53 week years occur on all years that have Thursday as 1 January and on leap years that start on Wednesday the 1 January. The extra week is sometimes referred to as a 'leap week', although ISO 8601 does not use this term.

### Expressing dates in spoken English

In English-language outside North America (mostly in Anglophone Europe and some countries in Australasia), full dates are written as *7 December 1941* (or *7th December 1941*) and spoken as "the seventh of December, nineteen forty-one" (exceedingly common usage of "the" and "of"), with the occasional usage of *December 7, 1941* ("December the seventh, nineteen forty-one"). In common with most continental European usage, however, all-numeric dates are invariably ordered dd/mm/yyyy.

In Canada and the United States, the usual written form is *December 7, 1941*, spoken as "December seventh, nineteen forty-one" or colloquially "December the seventh, nineteen forty-one". Ordinal numerals, however, are not always used when writing and pronouncing dates, and "December seven, nineteen forty-one" is also an accepted pronunciation of the date written *December 7, 1941*. A notable exception to this rule is the Fourth of July (U.S. Independence Day).
