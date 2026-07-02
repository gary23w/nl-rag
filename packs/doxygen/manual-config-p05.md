---
title: "Doxygen: Configuration (part 5/5)"
source: https://www.doxygen.nl/manual/config.html
domain: doxygen
license: CC-BY-SA-4.0
tags: doxygen docs, documentation generator, api documentation, source comments
fetched: 2026-07-02
part: 5/5
---

# Configuration options related to diagram generator tools

**`HIDE_UNDOC_RELATIONS`**

If set to `YES` the inheritance and collaboration graphs will hide inheritance and usage relations if the target is undocumented or is not a class.

The default value is: `YES`.

**`HAVE_DOT`**

If you set the `HAVE_DOT` tag to `YES` then Doxygen will assume the `dot` tool is available from the `path`. This tool is part of Graphviz, a graph visualization toolkit from AT&T and Lucent Bell Labs. The other options in this section have no effect if this option is set to `NO`

The default value is: `NO`.

**`DOT_NUM_THREADS`**

The `DOT_NUM_THREADS` specifies the number of `dot` invocations Doxygen is allowed to run in parallel. When set to `0` Doxygen will base this on the number of processors available in the system. You can set it explicitly to a value larger than 0 to get control over the balance between CPU load and processing speed.

Minimum value: `0`, maximum value: `512`, default value: `0`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_BATCH_SIZE`**

The `DOT_BATCH_SIZE` specifies the number of `dot` graphs Doxygen is allowed to compile in a single invocation of `dot`. When set to `1` Doxygen will invoke `dot` for each graph separately, which can cause significant process creation overhead especially on systems with many CPU cores. Together with `DOT_NUM_THREADS` this setting can be used to optimise the dot processing speed for a particular system. Doxygen will try to give each thread a balanced batch of work. If the total number of graphs to process exceeds DOT_NUM_THREADS * DOT_BATCH_SIZE then additional batches will be created for `dot` to process.

Minimum value: `1`, maximum value: `1000`, default value: `50`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_COMMON_ATTR`**

`DOT_COMMON_ATTR` is common attributes for nodes, edges and labels of subgraphs. When you want a differently looking font in the dot files that Doxygen generates you can specify fontname, fontcolor and fontsize attributes. For details please see Node, Edge and Graph Attributes specification You need to make sure dot is able to find the font, which can be done by putting it in a standard location or by setting the `DOTFONTPATH` environment variable or by setting DOT_FONTPATH to the directory containing the font. Default graphviz fontsize is 14.

The default value is: `fontname=Helvetica,fontsize=10`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_EDGE_ATTR`**

`DOT_EDGE_ATTR` is concatenated with DOT_COMMON_ATTR. For elegant style you can add 'arrowhead=open, arrowtail=open, arrowsize=0.5'. Complete documentation about arrows shapes.

The default value is: `labelfontname=Helvetica,labelfontsize=10`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_NODE_ATTR`**

`DOT_NODE_ATTR` is concatenated with DOT_COMMON_ATTR. For view without boxes around nodes set 'shape=plain' or 'shape=plaintext' Shapes specification

The default value is: `shape=box,height=0.2,width=0.4`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_FONTPATH`**

You can set the path where `dot` can find font specified with fontname in DOT_COMMON_ATTR and others dot attributes.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`CLASS_GRAPH`**

If the `CLASS_GRAPH` tag is set to `YES` or `GRAPH` or `BUILTIN` then Doxygen will generate a graph for each documented class showing the direct and indirect inheritance relations. In case the `CLASS_GRAPH` tag is set to `YES` or `GRAPH` and HAVE_DOT is enabled as well, then dot will be used to draw the graph. In case the `CLASS_GRAPH` tag is set to `YES` and HAVE_DOT is disabled or if the `CLASS_GRAPH` tag is set to `BUILTIN`, then the built-in generator will be used. If the `CLASS_GRAPH` tag is set to `TEXT` the direct and indirect inheritance relations will be shown as texts / links. Explicit enabling an inheritance graph or choosing a different representation for an inheritance graph of a specific class, can be accomplished by means of the command \inheritancegraph. Disabling an inheritance graph can be accomplished by means of the command \hideinheritancegraph.

Possible values are: `NO`, `YES`, `TEXT`, `GRAPH` and `BUILTIN`.

The default value is: `YES`.

**`COLLABORATION_GRAPH`**

If the `COLLABORATION_GRAPH` tag is set to `YES` then Doxygen will generate a graph for each documented class showing the direct and indirect implementation dependencies (inheritance, containment, and class references variables) of the class with other documented classes. Explicit enabling a collaboration graph, when `COLLABORATION_GRAPH` is set to `NO`, can be accomplished by means of the command \collaborationgraph. Disabling a collaboration graph can be accomplished by means of the command \hidecollaborationgraph.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`GROUP_GRAPHS`**

If the `GROUP_GRAPHS` tag is set to `YES` then Doxygen will generate a graph for groups, showing the direct groups dependencies. Explicit enabling a group dependency graph, when `GROUP_GRAPHS` is set to `NO`, can be accomplished by means of the command \groupgraph. Disabling a directory graph can be accomplished by means of the command \hidegroupgraph.

See also the chapter Grouping in the manual.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`UML_LOOK`**

If the `UML_LOOK` tag is set to `YES`, Doxygen will generate inheritance and collaboration diagrams in a style similar to the OMG's Unified Modeling Language.

The default value is: `NO`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`UML_LIMIT_NUM_FIELDS`**

If the UML_LOOK tag is enabled, the fields and methods are shown inside the class node. If there are many fields or methods and many nodes the graph may become too big to be useful. The `UML_LIMIT_NUM_FIELDS` threshold limits the number of items for each type to make the size more manageable. Set this to 0 for no limit. Note that the threshold may be exceeded by 50% before the limit is enforced. So when you set the threshold to 10, up to 15 fields may appear, but if the number exceeds 15, the total amount of fields shown is limited to 10.

Minimum value: `0`, maximum value: `100`, default value: `10`.

This tag requires that the tag UML_LOOK is set to `YES`.

**`UML_MAX_EDGE_LABELS`**

If the UML_LOOK tag is enabled, field labels are shown along the edge between two class nodes. If there are many fields and many nodes the graph may become too cluttered. The `UML_MAX_EDGE_LABELS` threshold limits the number of items to make the size more manageable. Set this to 0 for no limit.

Minimum value: `0`, maximum value: `100`, default value: `10`.

This tag requires that the tag UML_LOOK is set to `YES`.

**`DOT_UML_DETAILS`**

If the `DOT_UML_DETAILS` tag is set to `NO`, Doxygen will show attributes and methods without types and arguments in the UML graphs. If the `DOT_UML_DETAILS` tag is set to `YES`, Doxygen will add type and arguments for attributes and methods in the UML graphs. If the `DOT_UML_DETAILS` tag is set to `NONE`, Doxygen will not generate fields with class member information in the UML graphs. The class diagrams will look similar to the default class diagrams but using UML notation for the relationships.

Possible values are: `NO`, `YES` and `NONE`.

The default value is: `NO`.

This tag requires that the tag UML_LOOK is set to `YES`.

**`DOT_WRAP_THRESHOLD`**

The `DOT_WRAP_THRESHOLD` tag can be used to set the maximum number of characters to display on a single line. If the actual line length exceeds this threshold significantly it will be wrapped across multiple lines. Some heuristics are applied to avoid ugly line breaks.

Minimum value: `0`, maximum value: `1000`, default value: `17`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`TEMPLATE_RELATIONS`**

If the `TEMPLATE_RELATIONS` tag is set to `YES` then the inheritance and collaboration graphs will show the relations between templates and their instances.

The default value is: `NO`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`INCLUDE_GRAPH`**

If the `INCLUDE_GRAPH`, ENABLE_PREPROCESSING and SEARCH_INCLUDES tags are set to `YES` then Doxygen will generate a graph for each documented file showing the direct and indirect include dependencies of the file with other documented files. Explicit enabling an include graph, when `INCLUDE_GRAPH` is is set to `NO`, can be accomplished by means of the command \includegraph. Disabling an include graph can be accomplished by means of the command \hideincludegraph.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`INCLUDED_BY_GRAPH`**

If the `INCLUDED_BY_GRAPH`, ENABLE_PREPROCESSING and SEARCH_INCLUDES tags are set to `YES` then Doxygen will generate a graph for each documented file showing the direct and indirect include dependencies of the file with other documented files. Explicit enabling an included by graph, when `INCLUDED_BY_GRAPH` is set to `NO`, can be accomplished by means of the command \includedbygraph. Disabling an included by graph can be accomplished by means of the command \hideincludedbygraph.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`CALL_GRAPH`**

If the `CALL_GRAPH` tag is set to `YES` then Doxygen will generate a call dependency graph for every global function or class method. Note that enabling this option will significantly increase the time of a run. So in most cases it will be better to enable call graphs for selected functions only using the \callgraph command. Disabling a call graph can be accomplished by means of the command \hidecallgraph.

The default value is: `NO`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`CALLER_GRAPH`**

If the `CALLER_GRAPH` tag is set to `YES` then Doxygen will generate a caller dependency graph for every global function or class method. Note that enabling this option will significantly increase the time of a run. So in most cases it will be better to enable caller graphs for selected functions only using the \callergraph command. Disabling a caller graph can be accomplished by means of the command \hidecallergraph.

The default value is: `NO`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`GRAPHICAL_HIERARCHY`**

If the `GRAPHICAL_HIERARCHY` tag is set to `YES` then Doxygen will graphical hierarchy of all classes instead of a textual one.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DIRECTORY_GRAPH`**

If the `DIRECTORY_GRAPH` tag is set to `YES` then Doxygen will show the dependencies a directory has on other directories in a graphical way. The dependency relations are determined by the `#include` relations between the files in the directories. Explicit enabling a directory graph, when `DIRECTORY_GRAPH` is set to `NO`, can be accomplished by means of the command \directorygraph. Disabling a directory graph can be accomplished by means of the command \hidedirectorygraph.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DIR_GRAPH_MAX_DEPTH`**

The `DIR_GRAPH_MAX_DEPTH` tag can be used to limit the maximum number of levels of child directories generated in directory dependency graphs by `dot`.

Minimum value: `1`, maximum value: `25`, default value: `1`.

This tag requires that the tag DIRECTORY_GRAPH is set to `YES`.

**`DOT_IMAGE_FORMAT`**

The `DOT_IMAGE_FORMAT` tag can be used to set the image format of the images generated by `dot`. For an explanation of the image formats see the section output formats in the documentation of the `dot` tool (Graphviz). Note the formats svg:cairo and svg:cairo:cairo cannot be used in combination with INTERACTIVE_SVG (the INTERACTIVE_SVG will be set to NO).

Possible values are: `png`, `jpg`, `gif`, `svg`, `png:gd`, `png:gd:gd`, `png:cairo`, `png:cairo:gd`, `png:cairo:cairo`, `png:cairo:gdiplus`, `png:gdiplus`, `png:gdiplus:gdiplus`, `svg:cairo`, `svg:cairo:cairo`, `svg:svg`, `svg:svg:core`, `gif:cairo`, `gif:cairo:gd`, `gif:cairo:gdiplus`, `gif:gdiplus`, `gif:gdiplus:gdiplus`, `gif:gd`, `gif:gd:gd`, `jpg:cairo`, `jpg:cairo:gd`, `jpg:cairo:gdiplus`, `jpg:gd`, `jpg:gd:gd`, `jpg:gdiplus` and `jpg:gdiplus:gdiplus`.

The default value is: `png`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`INTERACTIVE_SVG`**

If DOT_IMAGE_FORMAT is set to svg or svg:svg or svg:svg:core, then this option can be set to `YES` to enable generation of interactive SVG images that allow zooming and panning. Note that this requires a modern browser other than Internet Explorer. Tested and working are Firefox, Chrome, Safari, and Opera. Note This option will be automatically disabled when DOT_IMAGE_FORMAT is set to svg:cairo or svg:cairo:cairo.

The default value is: `NO`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_PATH`**

The `DOT_PATH` tag can be used to specify the path where the `dot` tool can be found. If left blank, it is assumed the `dot` tool can be found in the `path`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOTFILE_DIRS`**

The `DOTFILE_DIRS` tag can be used to specify one or more directories that contain dot files that are included in the documentation (see the \dotfile command).

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DIA_PATH`**

You can include diagrams made with dia in Doxygen documentation. Doxygen will then run dia to produce the diagram and insert it in the documentation. The DIA_PATH tag allows you to specify the directory where the dia binary resides. If left empty dia is assumed to be found in the default search path.

**`DIAFILE_DIRS`**

The `DIAFILE_DIRS` tag can be used to specify one or more directories that contain dia files that are included in the documentation (see the \diafile command).

**`PLANTUML_JAR_PATH`**

When using PlantUML, the `PLANTUML_JAR_PATH` tag should be used to specify the path where java can find the `plantuml.jar` file or to the filename of `jar` file to be used. If left blank, it is assumed PlantUML is not used or called during a preprocessing step. Doxygen will generate a warning when it encounters a \startuml command in this case and will not generate output for the diagram.

**`PLANTUML_CFG_FILE`**

When using PlantUML, the `PLANTUML_CFG_FILE` tag can be used to specify a configuration file for PlantUML.

**`PLANTUML_INCLUDE_PATH`**

When using PlantUML, the specified paths are searched for files specified by the `!include` statement in a PlantUML block.

**`PLANTUMLFILE_DIRS`**

The `PLANTUMLFILE_DIRS` tag can be used to specify one or more directories that contain PlantUml files that are included in the documentation (see the \plantumlfile command).

**`MERMAID_PATH`**

When using Mermaid diagrams with CLI rendering, the `MERMAID_PATH` tag should be used to specify the directory where the `mmdc` (Mermaid CLI) executable can be found. If left blank, CLI-based rendering is disabled. For HTML output, client-side rendering via JavaScript is used by default and does not require `mmdc`. For LaTeX/PDF output, `mmdc` is required to pre-generate images. Doxygen will generate a warning when CLI rendering is needed but `mmdc` is not available.

**`MERMAID_CONFIG_FILE`**

When using Mermaid diagrams, the `MERMAID_CONFIG_FILE` tag can be used to specify a JSON configuration file for the Mermaid CLI tool (`mmdc`). This file can contain theme settings and other Mermaid configuration options.

**`MERMAID_RENDER_MODE`**

The `MERMAID_RENDER_MODE` tag selects how Mermaid diagrams are rendered.

Possible values are: `AUTO` (use client-side rendering for HTML and `mmdc` for LaTeX/PDF and other formats. If `MERMAID_PATH` is not set, non-HTML diagrams will produce a warning), `CLI` (use the `mmdc` tool to pre-generate images (requires `Node.js` and `mermaid-js/mermaid-cli`). Works for all output formats) and `CLIENT_SIDE` (embed `mermaid.js` in HTML output for client-side rendering. Does not require `mmdc` but only works for HTML output).

The default value is: `AUTO`.

**`MERMAID_JS_URL`**

The `MERMAID_JS_URL` tag specifies the URL to load `mermaid.js` from when using client-side rendering (`MERMAID_RENDER_MODE` is `CLIENT_SIDE` or `AUTO`). The default points to the latest Mermaid v11 release on the jsDelivr CDN. The default CDN URL requires internet access when viewing the generated documentation. For offline use, download `mermaid.esm.min.mjs` and set this to a relative path, or use `MERMAID_RENDER_MODE=CLI` to pre-generate images instead.

**Examples:**

- Latest v11 (default): `'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs'`
- Pinned version: `'https://cdn.jsdelivr.net/npm/[email protected]/dist/mermaid.esm.min.mjs'`
- Local copy: `'`./mermaid.esm.min.mjs' (user must place file in HTML output directory)

The default value is: `https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs`.

**`MERMAIDFILE_DIRS`**

The `MERMAIDFILE_DIRS` tag can be used to specify one or more directories that contain Mermaid files that are included in the documentation (see the \mermaidfile command).

**`DOT_GRAPH_MAX_NODES`**

The `DOT_GRAPH_MAX_NODES` tag can be used to set the maximum number of nodes that will be shown in the graph. If the number of nodes in a graph becomes larger than this value, Doxygen will truncate the graph, which is visualized by representing a node as a red box. Note that if the number of direct children of the root node in a graph is already larger than `DOT_GRAPH_MAX_NODES` then the graph will not be shown at all. Also note that the size of a graph can be further restricted by MAX_DOT_GRAPH_DEPTH.

Minimum value: `0`, maximum value: `10000`, default value: `50`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`MAX_DOT_GRAPH_DEPTH`**

The `MAX_DOT_GRAPH_DEPTH` tag can be used to set the maximum depth of the graphs generated by `dot`. A depth value of 3 means that only nodes reachable from the root by following a path via at most 3 edges will be shown. Nodes that lay further from the root node will be omitted. Note that setting this option to 1 or 2 may greatly reduce the computation time needed for large code bases. Also note that the size of a graph can be further restricted by DOT_GRAPH_MAX_NODES. Using a depth of 0 means no depth restriction.

Minimum value: `0`, maximum value: `1000`, default value: `0`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`GENERATE_LEGEND`**

If the `GENERATE_LEGEND` tag is set to `YES` Doxygen will generate a legend page explaining the meaning of the various boxes and arrows in the dot generated graphs.

**Note**

This tag requires that

UML_LOOK

isn't set, i.e. the Doxygen internal graphical representation for inheritance and collaboration diagrams is used.

The default value is: `YES`.

This tag requires that the tag HAVE_DOT is set to `YES`.

**`DOT_CLEANUP`**

If the `DOT_CLEANUP` tag is set to `YES`, Doxygen will remove the intermediate files that are used to generate the various graphs. Note: This setting is not only used for dot files but also for msc temporary files.

The default value is: `YES`.

**`MSCGEN_TOOL`**

You can define message sequence charts within Doxygen comments using the \msc command. If the `MSCGEN_TOOL` tag is left empty (the default), then Doxygen will use a built-in version of mscgen tool to produce the charts. Alternatively, the `MSCGEN_TOOL` tag can also specify the name an external tool. For instance, specifying prog as the value, Doxygen will call the tool as prog -T <outfile_format> -o <outputfile> <inputfile>. The external tool should support output file formats "png", "eps", "svg", and "ismap".

**`MSCFILE_DIRS`**

The `MSCFILE_DIRS` tag can be used to specify one or more directories that contain msc files that are included in the documentation (see the \mscfile command).


# Examples

Suppose you have a simple project consisting of two files: a source file `example.cc` and a header file `example.h`. Then a minimal configuration file is as simple as:

```
INPUT            = example.cc example.h
```

Assuming the example makes use of Qt classes and `perl` is located in `/usr/bin`, a more realistic configuration file would be:

```
PROJECT_NAME     = Example
INPUT            = example.cc example.h
WARNINGS         = YES
TAGFILES         = qt.tag
SEARCHENGINE     = NO
```

To generate the documentation for the QdbtTabular package I have used the following configuration file:

```
PROJECT_NAME     = QdbtTabular
OUTPUT_DIRECTORY = html
WARNINGS         = YES
INPUT            = examples/examples.doc src
FILE_PATTERNS    = *.cc *.h
INCLUDE_PATH     = examples
TAGFILES         = qt.tag
SEARCHENGINE     = YES
```

To regenerate the Qt-1.44 documentation from the sources, you could use the following configuration file:

```
PROJECT_NAME         = Qt
OUTPUT_DIRECTORY     = qt_docs
HIDE_UNDOC_MEMBERS   = YES
HIDE_UNDOC_CLASSES   = YES
ENABLE_PREPROCESSING = YES
MACRO_EXPANSION      = YES
EXPAND_ONLY_PREDEF   = YES
SEARCH_INCLUDES      = YES
FULL_PATH_NAMES      = YES
STRIP_FROM_PATH      = $(QTDIR)/
PREDEFINED           = USE_TEMPLATECLASS Q_EXPORT= \
                       QArrayT:=QArray \
                       QListT:=QList \
                       QDictT:=QDict \
                       QQueueT:=QQueue \
                       QVectorT:=QVector \
                       QPtrDictT:=QPtrDict \
                       QIntDictT:=QIntDict \
                       QStackT:=QStack \
                       QDictIteratorT:=QDictIterator \
                       QListIteratorT:=QListIterator \
                       QCacheT:=QCache \
                       QCacheIteratorT:=QCacheIterator \
                       QIntCacheT:=QIntCache \
                       QIntCacheIteratorT:=QIntCacheIterator \
                       QIntDictIteratorT:=QIntDictIterator \
                       QPtrDictIteratorT:=QPtrDictIterator
INPUT                = $(QTDIR)/doc \
                       $(QTDIR)/src/widgets \
                       $(QTDIR)/src/kernel \
                       $(QTDIR)/src/dialogs \
                       $(QTDIR)/src/tools
FILE_PATTERNS        = *.cpp *.h q*.doc
INCLUDE_PATH         = $(QTDIR)/include
RECURSIVE            = YES
```

For the Qt-2.1 sources I recommend to use the following settings:

```
PROJECT_NAME          = Qt
PROJECT_NUMBER        = 2.1
HIDE_UNDOC_MEMBERS    = YES
HIDE_UNDOC_CLASSES    = YES
SOURCE_BROWSER        = YES
INPUT                 = $(QTDIR)/src
FILE_PATTERNS         = *.cpp *.h q*.doc
RECURSIVE             = YES
EXCLUDE_PATTERNS      = *codec.cpp moc_* */compat/* */3rdparty/*
ALPHABETICAL_INDEX    = YES
IGNORE_PREFIX         = Q
ENABLE_PREPROCESSING  = YES
MACRO_EXPANSION       = YES
INCLUDE_PATH          = $(QTDIR)/include
PREDEFINED            = Q_PROPERTY(x)= \
                        Q_OVERRIDE(x)= \
                        Q_EXPORT= \
                        Q_ENUMS(x)= \
                        "QT_STATIC_CONST=static const " \
                        _WS_X11_ \
                        INCLUDE_MENUITEM_DEF
EXPAND_ONLY_PREDEF    = YES
EXPAND_AS_DEFINED     = Q_OBJECT_FAKE Q_OBJECT ACTIVATE_SIGNAL_WITH_PARAM \
                        Q_VARIANT_AS
```

Here Doxygen's preprocessor is used to substitute some macro names that are normally substituted by the C preprocessor, but without doing full macro expansion.

Go to the next section or return to the index.
