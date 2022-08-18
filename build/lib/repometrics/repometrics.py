import os
import json
import pathlib



def repometrics(url):
    repo_path=url
   
    #repo_path = input("Please Enter The Repository/Folder path \n Eg /path/to/some/project :\n" ).strip()
    
    
    language_list = {
    (".abap",): "ABAP",
    (".asc", ".ash"): "AGS Script",
    (".ampl", ".mod"): "AMPL",
    (".g4",): "ANTLR",
    (".apib",): "API Blueprint",
    (".apl", ".dyalog"): "APL",
    (".asp", ".asax", ".ascx", ".ashx", ".asmx", ".aspx", ".axd"): "ASP",
    (".dats", ".hats", ".sats"): "ATS",
    (".as",): "ActionScript",
    (".adb", ".ada", ".ads"): "Ada",
    (".agda",): "Agda",
    (".als",): "Alloy",
    (".apacheconf", ".vhost"): "ApacheConf",
    (".cls",): "Apex",
    (".applescript", ".scpt"): "AppleScript",
    (".arc",): "Arc",
    (".ino",): "Arduino",
    (".asciidoc", ".adoc", ".asc"): "AsciiDoc",
    (".aj",): "AspectJ",
    (".asm", ".a51", ".inc", ".nasm"): "Assembly",
    (".aug",): "Augeas",
    (".ahk", ".ahkl"): "AutoHotkey",
    (".au3",): "AutoIt",
    (".awk", ".auk", ".gawk", ".mawk", ".nawk"): "Awk",
    (".bat", ".cmd"): "Batchfile",
    (".befunge",): "Befunge",
    (".bison",): "Bison",
    (".bb",): "BitBake",
    (".bb", ".decls"): "BlitzBasic",
    (".bmx",): "BlitzMax",
    (".bsv",): "Bluespec",
    (".boo",): "Boo",
    (".b", ".bf"): "Brainfuck",
    (".brs",): "Brightscript",
    (".bro",): "Bro",
    (".c", ".cats", ".h", ".idc", ".w"): "C",
    (".cs", ".cake", ".cshtml", ".csx"): "C#",
    (
        ".cpp",
        ".c  ",
        ".cc",
        ".cp",
        ".cxx",
        ".h",
        ".h  ",
        ".hh",
        ".hpp",
        ".hxx",
        ".inc",
        ".inl",
        ".ipp",
        ".tcc",
        ".tpp",
    ): "C  ",
    (".c-objdump",): "C-ObjDump",
    (".chs",): "C2hs Haskell",
    (".clp",): "CLIPS",
    (".cmake", ".cmake.in"): "CMake",
    (".cob", ".cbl", ".ccp", ".cobol", ".cpy"): "COBOL",
    (".css",): "CSS",
    (".csv",): "CSV",
    (".capnp",): "Cap'n Proto",
    (".mss",): "CartoCSS",
    (".ceylon",): "Ceylon",
    (".chpl",): "Chapel",
    (".ch",): "Charity",
    (".ck",): "ChucK",
    (".cirru",): "Cirru",
    (".clw",): "Clarion",
    (".icl", ".dcl"): "Clean",
    (".click",): "Click",
    (
        ".clj",
        ".boot",
        ".cl2",
        ".cljc",
        ".cljs",
        ".cljs.hl",
        ".cljscm",
        ".cljx",
        ".hic",
    ): "Clojure",
    (".coffee", "._coffee", ".cake", ".cjsx", ".cson", ".iced"): "CoffeeScript",
    (".cfm", ".cfml"): "ColdFusion",
    (".cfc",): "ColdFusion CFC",
    (".lisp", ".asd", ".cl", ".l", ".lsp", ".ny", ".podsl", ".sexp"): "Common Lisp",
    (".cp", ".cps"): "Component Pascal",
    (".cl",): "Cool",
    (".coq", ".v"): "Coq",
    (
        ".cppobjdump",
        ".c  -objdump",
        ".c  objdump",
        ".cpp-objdump",
        ".cxx-objdump",
    ): "Cpp-ObjDump",
    (".creole",): "Creole",
    (".cr",): "Crystal",
    (".feature",): "Cucumber",
    (".cu", ".cuh"): "Cuda",
    (".cy",): "Cycript",
    (".pyx", ".pxd", ".pxi"): "Cython",
    (".d", ".di"): "D",
    (".d-objdump",): "D-ObjDump",
    (".com",): "DIGITAL Command Language",
    (".dm",): "DM",
    (".zone", ".arpa"): "DNS Zone",
    (".d",): "DTrace",
    (".darcspatch", ".dpatch"): "Darcs Patch",
    (".dart",): "Dart",
    (".diff", ".patch"): "Diff",
    (".dockerfile",): "Dockerfile",
    (".djs",): "Dogescript",
    (".dylan", ".dyl", ".intr", ".lid"): "Dylan",
    (".E",): "E",
    (".ecl", ".eclxml"): "ECL",
    (".ecl",): "ECLiPSe",
    (".sch", ".brd"): "Eagle",
    (".epj",): "Ecere Projects",
    (".e",): "Eiffel",
    (".ex", ".exs"): "Elixir",
    (".elm",): "Elm",
    (".el", ".emacs", ".emacs.desktop"): "Emacs Lisp",
    (".em", ".emberscript"): "EmberScript",
    (".erl", ".es", ".escript", ".hrl", ".xrl", ".yrl"): "Erlang",
    (".fs", ".fsi", ".fsx"): "F#",
    (".fx", ".flux"): "FLUX",
    (".f90", ".f", ".f03", ".f08", ".f77", ".f95", ".for", ".fpp"): "FORTRAN",
    (".factor",): "Factor",
    (".fy", ".fancypack"): "Fancy",
    (".fan",): "Fantom",
    (".fs",): "Filterscript",
    (".for", ".eam.fs"): "Formatted",
    (".fth", ".4th", ".f", ".for", ".forth", ".fr", ".frt", ".fs"): "Forth",
    (".ftl",): "FreeMarker",
    (".fr",): "Frege",
    (".g", ".gco", ".gcode"): "G-code",
    (".gms",): "GAMS",
    (".g", ".gap", ".gd", ".gi", ".tst"): "GAP",
    (".s", ".ms"): "GAS",
    (".gd",): "GDScript",
    (
        ".glsl",
        ".fp",
        ".frag",
        ".frg",
        ".fs",
        ".fsh",
        ".fshader",
        ".geo",
        ".geom",
        ".glslv",
        ".gshader",
        ".shader",
        ".vert",
        ".vrx",
        ".vsh",
        ".vshader",
    ): "GLSL",
    (".gml",): "Graph Modeling Language",
    (".kid",): "Genshi",
    (".ebuild",): "Gentoo Ebuild",
    (".eclass",): "Gentoo Eclass",
    (".po", ".pot"): "Gettext Catalog",
    (".glf",): "Glyph",
    (".gp", ".gnu", ".gnuplot", ".plot", ".plt"): "Gnuplot",
    (".go",): "Go",
    (".golo",): "Golo",
    (".gs", ".gst", ".gsx", ".vark"): "Gosu",
    (".grace",): "Grace",
    (".gradle",): "Gradle",
    (".gf",): "Grammatical Framework",
    (".graphql",): "GraphQL",
    (".dot", ".gv"): "Graphviz (DOT)",
    (
        ".man",
        ".1",
        ".1in",
        ".1m",
        ".1x",
        ".2",
        ".3",
        ".3in",
        ".3m",
        ".3qt",
        ".3x",
        ".4",
        ".5",
        ".6",
        ".7",
        ".8",
        ".9",
        ".l",
        ".me",
        ".ms",
        ".n",
        ".rno",
        ".roff",
    ): "Groff",
    (".groovy", ".grt", ".gtpl", ".gvy"): "Groovy",
    (".gsp",): "Groovy Server Pages",
    (".hcl", ".tf"): "HCL",
    (".hlsl", ".fx", ".fxh", ".hlsli"): "HLSL",
    (".html", ".htm", ".html.hl", ".inc", ".st", ".xht", ".xhtml"): "HTML",
    (".mustache", ".jinja"): "HTML Django",
    (".eex",): "HTML EEX",
    (".erb", ".erb.deface"): "HTML ERB",
    (".phtml",): "HTML PHP",
    (".http",): "HTTP",
    (".hh", ".php"): "Hack",
    (".haml", ".haml.deface"): "Haml",
    (".handlebars", ".hbs"): "Handlebars",
    (".hb",): "Harbour",
    (".hs", ".hsc"): "Haskell",
    (".hx", ".hxsl"): "Haxe",
    (".hy",): "Hy",
    (".bf",): "HyPhy",
    (".pro", ".dlm"): "IDL",
    (".ipf",): "IGOR Pro",
    (".ini", ".cfg", ".prefs", ".pro", ".properties"): "INI",
    (".irclog", ".weechatlog"): "IRC log",
    (".idr", ".lidr"): "Idris",
    (".ni", ".i7x"): "Inform 7",
    (".iss",): "Inno Setup",
    (".io",): "Io",
    (".ik",): "Ioke",
    (".thy",): "Isabelle",
    (".ijs",): "J",
    (".flex", ".jflex"): "JFlex",
    (".json", ".geojson", ".lock", ".topojson"): "JSON",
    (".json5",): "JSON5",
    (".jsonld",): "JSONLD",
    (".jq",): "JSONiq",
    (".jsx",): "JSX",
    (".jade",): "Jade",
    (".j",): "Jasmin",
    (".java",): "Java",
    (".jsp",): "Java Server Pages",
    (
        ".js",
        "._js",
        ".bones",
        ".es",
        ".es6",
        ".frag",
        ".gs",
        ".jake",
        ".jsb",
        ".jscad",
        ".jsfl",
        ".jsm",
        ".jss",
        ".njs",
        ".pac",
        ".sjs",
        ".ssjs",
        ".sublime-build",
        ".sublime-commands",
        ".sublime-completions",
        ".sublime-keymap",
        ".sublime-macro",
        ".sublime-menu",
        ".sublime-mousemap",
        ".sublime-project",
        ".sublime-settings",
        ".sublime-theme",
        ".sublime-workspace",
        ".sublime_metrics",
        ".sublime_session",
        ".xsjs",
        ".xsjslib",
    ): "JavaScript",
    (".jl",): "Julia",
    (".ipynb",): "Jupyter Notebook",
    (".krl",): "KRL",
    (".sch", ".brd", ".kicad_pcb"): "KiCad",
    (".kit",): "Kit",
    (".kt", ".ktm", ".kts"): "Kotlin",
    (".lfe",): "LFE",
    (".ll",): "LLVM",
    (".lol",): "LOLCODE",
    (".lsl", ".lslp"): "LSL",
    (".lvproj",): "LabVIEW",
    (".lasso", ".las", ".lasso8", ".lasso9", ".ldml"): "Lasso",
    (".latte",): "Latte",
    (".lean", ".hlean"): "Lean",
    (".less",): "Less",
    (".l", ".lex"): "Lex",
    (".ly", ".ily"): "LilyPond",
    (".b", ".m"): "Limbo",
    (".ld", ".lds"): "Linker Script",
    (".mod",): "Modula-2",
    (".liquid",): "Liquid",
    (".lagda",): "Literate Agda",
    (".litcoffee",): "Literate CoffeeScript",
    (".lhs",): "Literate Haskell",
    (".ls", "._ls"): "LiveScript",
    (".xm", ".x", ".xi"): "Logos",
    (".lgt", ".logtalk"): "Logtalk",
    (".lookml",): "LookML",
    (".ls",): "LoomScript",
    (".lua", ".fcgi", ".nse", ".pd_lua", ".rbxs", ".wlua"): "Lua",
    (".mumps", ".m"): "M",
    (".m4",): "M4Sugar",
    (".ms", ".mcr"): "MAXScript",
    (".mtml",): "MTML",
    (".muf", ".m"): "MUF",
    (".mak", ".d", ".mk", ".mkfile"): "Makefile",
    (".mako", ".mao"): "Mako",
    (".md", ".markdown", ".mkd", ".mkdn", ".mkdown", ".ron"): "Markdown",
    (".mask",): "Mask",
    (
        ".mathematica",
        ".cdf",
        ".m",
        ".ma",
        ".mt",
        ".nb",
        ".nbp",
        ".wl",
        ".wlt",
    ): "Mathematica",
    (".matlab", ".m"): "Matlab",
    (".maxpat", ".maxhelp", ".maxproj", ".mxt", ".pat"): "Max",
    (".mediawiki", ".wiki"): "MediaWiki",
    (".m", ".moo"): "Mercury",
    (".metal",): "Metal",
    (".minid",): "MiniD",
    (".druby", ".duby", ".mir", ".mirah"): "Mirah",
    (".mo",): "Modelica",
    (".mms", ".mmk"): "Module Management System",
    (".monkey",): "Monkey",
    (".moo",): "Moocode",
    (".moon",): "MoonScript",
    (".myt",): "Myghty",
    (".ncl",): "NCL",
    (".nl",): "NL",
    (".nsi", ".nsh"): "NSIS",
    (".n",): "Nemerle",
    (".axs", ".axi"): "NetLinx",
    (".axs.erb", ".axi.erb"): "NetLinx ERB",
    (".nlogo",): "NetLogo",
    (".nl", ".lisp", ".lsp"): "NewLisp",
    (".nginxconf", ".vhost"): "Nginx",
    (".nim", ".nimrod"): "Nimrod",
    (".ninja",): "Ninja",
    (".nit",): "Nit",
    (".nix",): "Nix",
    (".nu",): "Nu",
    (".numpy", ".numpyw", ".numsc"): "NumPy",
    (".ml", ".eliom", ".eliomi", ".ml4", ".mli", ".mll", ".mly"): "OCaml",
    (".objdump",): "ObjDump",
    (".m", ".h"): "Objective-C",
    (".mm",): "Objective-C  ",
    (".j", ".sj"): "Objective-J",
    (".omgrofl",): "Omgrofl",
    (".opa",): "Opa",
    (".opal",): "Opal",
    (".cl", ".opencl"): "OpenCL",
    (".p", ".cls"): "OpenEdge ABL",
    (".scad",): "OpenSCAD",
    (".org",): "Org",
    (".ox", ".oxh", ".oxo"): "Ox",
    (".oxygene",): "Oxygene",
    (".oz",): "Oz",
    (".pwn", ".inc"): "PAWN",
    (
        ".php",
        ".aw",
        ".ctp",
        ".fcgi",
        ".inc",
        ".php3",
        ".php4",
        ".php5",
        ".phps",
        ".phpt",
    ): "PHP",
    (".pls", ".pck", ".pkb", ".pks", ".plb", ".plsql", ".sql"): "PLSQL",
    (".sql",): "PLpgSQL",
    (".pov", ".inc"): "POV-Ray SDL",
    (".pan",): "Pan",
    (".psc",): "Papyrus",
    (".parrot",): "Parrot",
    (".pasm",): "Parrot Assembly",
    (".pir",): "Parrot Internal Representation",
    (".pas", ".dfm", ".dpr", ".inc", ".lpr", ".pp"): "Pascal",
    (
        ".pl",
        ".al",
        ".cgi",
        ".fcgi",
        ".perl",
        ".ph",
        ".plx",
        ".pm",
        ".pod",
        ".psgi",
        ".t",
    ): "Perl",
    (
        ".6pl",
        ".6pm",
        ".nqp",
        ".p6",
        ".p6l",
        ".p6m",
        ".pl",
        ".pl6",
        ".pm",
        ".pm6",
        ".t",
    ): "Perl6",
    (".pkl",): "Pickle",
    (".l",): "PicoLisp",
    (".pig",): "PigLatin",
    (".pike", ".pmod"): "Pike",
    (".pod",): "Pod",
    (".pogo",): "PogoScript",
    (".pony",): "Pony",
    (".ps", ".eps"): "PostScript",
    (".ps1", ".psd1", ".psm1"): "PowerShell",
    (".pde",): "Processing",
    (".pl", ".pro", ".prolog", ".yap"): "Prolog",
    (".spin",): "Propeller Spin",
    (".proto",): "Protocol Buffer",
    (".asc", ".pub"): "Public Key",
    (".pp",): "Puppet",
    (".pd",): "Pure Data",
    (".pb", ".pbi"): "PureBasic",
    (".purs",): "PureScript",
    (
        ".py",
        ".pyc",
        ".bzl",
        ".cgi",
        ".fcgi",
        ".gyp",
        ".lmi",
        ".pyde",
        ".pyp",
        ".pyt",
        ".pyw",
        ".rpy",
        ".tac",
        ".wsgi",
        ".xpy",
    ): "Python",
    (".pytb",): "Python traceback",
    (".qml", ".qbs"): "QML",
    (".pro", ".pri"): "QMake",
    (".r", ".rd", ".rsx"): "R",
    (".raml",): "RAML",
    (".rdoc",): "RDoc",
    (".rbbas", ".rbfrm", ".rbmnu", ".rbres", ".rbtbar", ".rbuistate"): "REALbasic",
    (".rhtml",): "RHTML",
    (".rmd",): "RMarkdown",
    (".rkt", ".rktd", ".rktl", ".scrbl"): "Racket",
    (".rl",): "Ragel in Ruby Host",
    (".raw",): "Raw token data",
    (".reb", ".r", ".r2", ".r3", ".rebol"): "Rebol",
    (".red", ".reds"): "Red",
    (".cw",): "Redcode",
    (".rpy",): "Ren'Py",
    (".rs", ".rsh"): "RenderScript",
    (".robot",): "RobotFramework",
    (".rg",): "Rouge",
    (
        ".rb",
        ".builder",
        ".fcgi",
        ".gemspec",
        ".god",
        ".irbrc",
        ".jbuilder",
        ".mspec",
        ".pluginspec",
        ".podspec",
        ".rabl",
        ".rake",
        ".rbuild",
        ".rbw",
        ".rbx",
        ".ru",
        ".ruby",
        ".thor",
        ".watchr",
    ): "Ruby",
    (".rs", ".rs.in"): "Rust",
    (".sas",): "SAS",
    (".scss",): "SCSS",
    (".smt2", ".smt"): "SMT",
    (".sparql", ".rq"): "SPARQL",
    (".sqf", ".hqf"): "SQF",
    (".sql", ".cql", ".ddl", ".inc", ".prc", ".tab", ".udf", ".viw"): "SQL",
    (".sql", ".db2"): "SQLPL",
    (".ston",): "STON",
    (".svg",): "SVG",
    (".sage", ".sagews"): "Sage",
    (".sls",): "SaltStack",
    (".sass",): "Sass",
    (".scala", ".sbt", ".sc"): "Scala",
    (".scaml",): "Scaml",
    (".scm", ".sld", ".sls", ".sps", ".ss"): "Scheme",
    (".sci", ".sce", ".tst"): "Scilab",
    (".self",): "Self",
    (
        ".sh",
        ".bash",
        ".bats",
        ".cgi",
        ".command",
        ".fcgi",
        ".ksh",
        ".sh.in",
        ".tmux",
        ".tool",
        ".zsh",
    ): "Shell",
    (".sh-session",): "ShellSession",
    (".shen",): "Shen",
    (".sl",): "Slash",
    (".slim",): "Slim",
    (".smali",): "Smali",
    (".st", ".cs"): "Smalltalk",
    (".tpl",): "Smarty",
    (".sp", ".inc", ".sma"): "SourcePawn",
    (".nut",): "Squirrel",
    (".stan",): "Stan",
    (".ML", ".fun", ".sig", ".sml"): "Standard ML",
    (".do", ".ado", ".doh", ".ihlp", ".mata", ".matah", ".sthlp"): "Stata",
    (".styl",): "Stylus",
    (".sc", ".scd"): "SuperCollider",
    (".swift",): "Swift",
    (".sv", ".svh", ".vh"): "SystemVerilog",
    (".toml",): "TOML",
    (".txl",): "TXL",
    (".tcl", ".adp", ".tm"): "Tcl",
    (".tcsh", ".csh"): "Tcsh",
    (
        ".tex",
        ".aux",
        ".bbx",
        ".bib",
        ".cbx",
        ".cls",
        ".dtx",
        ".ins",
        ".lbx",
        ".ltx",
        ".mkii",
        ".mkiv",
        ".mkvi",
        ".sty",
        ".toc",
    ): "TeX",
    (".tea",): "Tea",
    (".t",): "Terra",
    (".txt", ".fr", ".nb", ".ncl", ".no"): "Text",
    (".textile",): "Textile",
    (".thrift",): "Thrift",
    (".t", ".tu"): "Turing",
    (".ttl",): "Turtle",
    (".twig",): "Twig",
    (".ts", ".tsx"): "TypeScript",
    (".upc",): "Unified Parallel C",
    (".anim", ".asset", ".mat", ".meta", ".prefab", ".unity"): "Unity3D Asset",
    (".uno",): "Uno",
    (".uc",): "UnrealScript",
    (".ur", ".urs"): "UrWeb",
    (".vcl",): "VCL",
    (".vhdl", ".vhd", ".vhf", ".vhi", ".vho", ".vhs", ".vht", ".vhw"): "VHDL",
    (".vala", ".vapi"): "Vala",
    (".v", ".veo"): "Verilog",
    (".vim",): "VimL",
    (".vb", ".bas", ".cls", ".frm", ".frx", ".vba", ".vbhtml", ".vbs"): "Visual Basic",
    (".volt",): "Volt",
    (".vue",): "Vue",
    (".owl",): "Web Ontology Language",
    (".webidl",): "WebIDL",
    (".x10",): "X10",
    (".xc",): "XC",
    (
        ".xml",
        ".ant",
        ".axml",
        ".ccxml",
        ".clixml",
        ".cproject",
        ".csl",
        ".csproj",
        ".ct",
        ".dita",
        ".ditamap",
        ".ditaval",
        ".dll.config",
        ".dotsettings",
        ".filters",
        ".fsproj",
        ".fxml",
        ".glade",
        ".gml",
        ".grxml",
        ".iml",
        ".ivy",
        ".jelly",
        ".jsproj",
        ".kml",
        ".launch",
        ".mdpolicy",
        ".mm",
        ".mod",
        ".mxml",
        ".nproj",
        ".nuspec",
        ".odd",
        ".osm",
        ".plist",
        ".pluginspec",
        ".props",
        ".ps1xml",
        ".psc1",
        ".pt",
        ".rdf",
        ".rss",
        ".scxml",
        ".srdf",
        ".storyboard",
        ".stTheme",
        ".sublime-snippet",
        ".targets",
        ".tmCommand",
        ".tml",
        ".tmLanguage",
        ".tmPreferences",
        ".tmSnippet",
        ".tmTheme",
        ".ts",
        ".tsx",
        ".ui",
        ".urdf",
        ".ux",
        ".vbproj",
        ".vcxproj",
        ".vssettings",
        ".vxml",
        ".wsdl",
        ".wsf",
        ".wxi",
        ".wxl",
        ".wxs",
        ".x3d",
        ".xacro",
        ".xaml",
        ".xib",
        ".xlf",
        ".xliff",
        ".xmi",
        ".xml.dist",
        ".xproj",
        ".xsd",
        ".xul",
        ".zcml",
    ): "XML",
    (".xsp-config", ".xsp.metadata"): "XPages",
    (".xpl", ".xproc"): "XProc",
    (".xquery", ".xq", ".xql", ".xqm", ".xqy"): "XQuery",
    (".xs",): "XS",
    (".xslt", ".xsl"): "XSLT",
    (
        ".xojo_code",
        ".xojo_menu",
        ".xojo_report",
        ".xojo_script",
        ".xojo_toolbar",
        ".xojo_window",
    ): "Xojo",
    (".xtend",): "Xtend",
    (
        ".yml",
        ".reek",
        ".rviz",
        ".sublime-syntax",
        ".syntax",
        ".yaml",
        ".yaml-tmlanguage",
    ): "YAML",
    (".yang",): "YANG",
    (".y", ".yacc", ".yy"): "Yacc",
    (".zep",): "Zephir",
    (".zimpl", ".zmpl", ".zpl"): "Zimpl",
    (".desktop", ".desktop.in"): "desktop",
    (".ec", ".eh"): "eC",
    (".edn",): "edn",
    (".fish",): "fish",
    (".mu",): "mupad",
    (".nc",): "nesC",
    (".ooc",): "ooc",
    (".rst", ".rest", ".rest.txt", ".rst.txt"): "reStructuredText",
    (".wisp",): "wisp",
    (".prg", ".ch", ".prw"): "xBase",
    }

    searched_language = {}
    result_json = {}
    result=[]
    summary = {}
    language_count={}
    output={}
    if not os.path.exists(repo_path):
        print("No such repository path exists!")
        return
    
    for subdir, dirs, files in os.walk(repo_path):
        if len(files)>0:
            for file in files:
                #print(os.path.abspath(os.path.join(subdir, file)))
                relative_path = os.path.relpath(os.path.join(subdir, file))
                file_dict={}
                extension = "."+file.split('.')[-1].strip()
                res = [v for k, v in language_list.items() if extension in k]
                if len(res)>0:
                    file_dict["path"]=relative_path
                    file_dict["language"]=res[0]
                    if not res[0] in language_count.keys():
                        language_count[res[0]]=1
                    else:
                        language_count[res[0]]=language_count[res[0]]+1
                if len(file_dict)>0:
                    result.append(file_dict)
                    
                   

    
    for lang_key, lang_val in language_count.items():
        summary[lang_key] = language_count[lang_key]/ len(result)
        

    
    output["summary"]=summary
    output["result"]=result

    #print("output json", json.dumps(output, indent=4))
    return json.dumps(output, indent=4)

   
   
     

#main(repo_path, language_list)
#download()










