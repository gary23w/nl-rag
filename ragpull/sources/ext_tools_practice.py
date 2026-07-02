"""Testing frameworks, package managers, build tools, docs tooling, editors, and CLI utilities."""

from .common import CC_BY_SA, WIKI, wiki

DOMAINS = {
    # ---- testing frameworks --------------------------------------------------
    "pytest-testing": {
        "tags": ["pytest python", "test fixtures", "python testing", "parametrized tests"],
        "license": CC_BY_SA,
        "pages": wiki("Pytest", "Unit_testing", "Test_automation") + [
            "https://docs.pytest.org/en/stable/how-to/fixtures.html",
            "https://docs.pytest.org/en/stable/how-to/assert.html",
            "https://docs.pytest.org/en/stable/how-to/parametrize.html",
            "https://docs.pytest.org/en/stable/how-to/mark.html",
        ],
    },
    "jest-testing": {
        "tags": ["jest testing", "javascript testing", "test runner", "mock functions"],
        "license": CC_BY_SA,
        "pages": wiki("Test_automation", "JavaScript", "List_of_unit_testing_frameworks") + [
            "https://jestjs.io/docs/getting-started",
            "https://jestjs.io/docs/expect",
            "https://jestjs.io/docs/mock-functions",
        ],
    },
    "mocha-chai": {
        "tags": ["mocha javascript", "chai assertions", "javascript testing", "bdd assertions"],
        "license": CC_BY_SA,
        "pages": wiki("Mocha_(JavaScript_framework)", "Assertion_(software_development)", "Unit_testing") + [
            "https://mochajs.org/",
            "https://www.chaijs.com/guide/",
            "https://www.chaijs.com/api/bdd/",
        ],
    },
    "vitest": {
        "tags": ["vitest runner", "vite testing", "javascript testing", "test mocking"],
        "license": CC_BY_SA,
        "pages": wiki("Vite_(software)", "Test_automation", "JavaScript") + [
            "https://vitest.dev/guide/",
            "https://vitest.dev/guide/features",
            "https://vitest.dev/guide/mocking",
            "https://vitest.dev/api/",
        ],
    },
    "cypress-e2e": {
        "tags": ["cypress testing", "end-to-end testing", "web testing", "browser tests"],
        "license": CC_BY_SA,
        "pages": wiki("Cypress_(software)", "End-to-end_testing", "Web_testing") + [
            "https://docs.cypress.io/guides/overview/why-cypress",
            "https://docs.cypress.io/guides/core-concepts/writing-and-organizing-tests",
            "https://docs.cypress.io/api/table-of-contents",
        ],
    },
    "playwright-testing": {
        "tags": ["playwright testing", "browser automation", "end-to-end testing", "web locators"],
        "license": CC_BY_SA,
        "pages": wiki("Playwright_(software)", "Headless_browser", "End-to-end_testing") + [
            "https://playwright.dev/docs/intro",
            "https://playwright.dev/docs/writing-tests",
            "https://playwright.dev/docs/locators",
            "https://playwright.dev/docs/test-assertions",
        ],
    },
    "selenium": {
        "tags": ["selenium webdriver", "browser automation", "web testing", "headless browser"],
        "license": CC_BY_SA,
        "pages": wiki("Selenium_(software)", "Headless_browser", "Web_testing") + [
            "https://www.selenium.dev/documentation/",
            "https://www.selenium.dev/documentation/webdriver/",
            "https://www.selenium.dev/documentation/webdriver/waits/",
        ],
    },
    "junit": {
        "tags": ["junit java", "java testing", "unit testing", "xunit family"],
        "license": CC_BY_SA,
        "pages": wiki("JUnit", "XUnit", "Java_(programming_language)", "Unit_testing") + [
            "https://junit.org/junit5/",
            "https://junit.org/junit5/docs/current/user-guide/",
            "https://junit.org/junit5/docs/current/api/",
        ],
    },
    "testng": {
        "tags": ["testng java", "java testing", "test automation", "unit testing"],
        "license": CC_BY_SA,
        "pages": wiki("TestNG", "Java_(programming_language)", "Test_automation", "List_of_unit_testing_frameworks", "Behavior-driven_development", "Continuous_integration"),
    },
    "rspec": {
        "tags": ["rspec ruby", "ruby testing", "behavior-driven development", "spec framework"],
        "license": CC_BY_SA,
        "pages": wiki("RSpec", "Behavior-driven_development", "Ruby_(programming_language)") + [
            "https://rspec.info/documentation/",
            "https://rspec.info/features/3-13/rspec-core/",
            "https://rspec.info/features/3-13/rspec-expectations/",
            "https://rspec.info/features/3-13/rspec-mocks/",
        ],
    },
    "minitest": {
        "tags": ["minitest ruby", "ruby testing", "unit testing", "test framework"],
        "license": CC_BY_SA,
        "pages": wiki("Ruby_(programming_language)", "Unit_testing", "List_of_unit_testing_frameworks", "Test_automation", "Regression_testing", "Test_fixture"),
    },
    "phpunit": {
        "tags": ["phpunit php", "php testing", "unit testing", "test assertions"],
        "license": CC_BY_SA,
        "pages": wiki("PHPUnit", "PHP", "Unit_testing") + [
            "https://docs.phpunit.de/en/11.5/writing-tests-for-phpunit.html",
            "https://docs.phpunit.de/en/11.5/assertions.html",
            "https://phpunit.de/getting-started/phpunit-11.html",
        ],
    },
    "property-based-testing": {
        "tags": ["property-based testing", "generative testing", "test generation", "quickcheck style"],
        "license": CC_BY_SA,
        "pages": wiki("Property_testing", "QuickCheck", "Fuzzing", "Software_testing", "Regression_testing", "Unit_testing"),
    },
    "quickcheck": {
        "tags": ["quickcheck haskell", "property-based testing", "test generation", "functional testing"],
        "license": CC_BY_SA,
        "pages": wiki("QuickCheck", "Haskell", "Property_testing", "Domain-specific_language", "Software_testing", "Fuzzing"),
    },
    "hypothesis-testing": {
        "tags": ["hypothesis python", "property-based testing", "test strategies", "python testing"],
        "license": CC_BY_SA,
        "pages": wiki("Property_testing", "Python_(programming_language)", "Software_testing") + [
            "https://hypothesis.readthedocs.io/en/latest/",
            "https://hypothesis.readthedocs.io/en/latest/quickstart.html",
            "https://hypothesis.readthedocs.io/en/latest/details.html",
            "https://hypothesis.readthedocs.io/en/latest/data.html",
        ],
    },
    "mutation-testing": {
        "tags": ["mutation testing", "test effectiveness", "fault injection", "code coverage"],
        "license": CC_BY_SA,
        "pages": wiki("Mutation_testing", "Fault_injection", "Code_coverage", "Software_testing", "Unit_testing", "Regression_testing"),
    },
    "k6-load-testing": {
        "tags": ["k6 load", "load testing", "performance testing", "http requests"],
        "license": CC_BY_SA,
        "pages": wiki("K6_(software)", "Load_testing", "Software_performance_testing") + [
            "https://k6.io/docs/",
            "https://k6.io/docs/using-k6/http-requests/",
            "https://k6.io/docs/using-k6/metrics/",
        ],
    },
    "locust-load-testing": {
        "tags": ["locust python", "load testing", "performance testing", "distributed load"],
        "license": CC_BY_SA,
        "pages": wiki("Load_testing", "Software_performance_testing", "Stress_testing_(software)") + [
            "https://docs.locust.io/en/stable/",
            "https://docs.locust.io/en/stable/writing-a-locustfile.html",
            "https://locust.io/",
        ],
    },
    "jmeter": {
        "tags": ["jmeter apache", "load testing", "performance testing", "test plan"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_JMeter", "Load_testing", "Software_performance_testing") + [
            "https://jmeter.apache.org/usermanual/index.html",
            "https://jmeter.apache.org/usermanual/build-web-test-plan.html",
            "https://jmeter.apache.org/usermanual/get-started.html",
            "https://jmeter.apache.org/usermanual/component_reference.html",
        ],
    },
    "gatling": {
        "tags": ["gatling scala", "load testing", "performance testing", "simulation scripts"],
        "license": CC_BY_SA,
        "pages": wiki("Gatling_(software)", "Scala_(programming_language)", "Load_testing", "Software_performance_testing") + [
            "https://gatling.io/docs/",
            "https://gatling.io/docs/gatling/reference/current/core/simulation/",
        ],
    },
    "cucumber-bdd": {
        "tags": ["cucumber bdd", "behavior-driven development", "acceptance testing", "executable specifications"],
        "license": CC_BY_SA,
        "pages": wiki("Cucumber_(software)", "Behavior-driven_development", "Test_automation") + [
            "https://cucumber.io/docs/cucumber/",
            "https://cucumber.io/docs/gherkin/",
            "https://cucumber.io/docs/installation/",
        ],
    },
    "gherkin": {
        "tags": ["gherkin syntax", "given when then", "behavior-driven development", "specification language"],
        "license": CC_BY_SA,
        "pages": wiki("Behavior-driven_development", "Domain-specific_language", "Cucumber_(software)", "Test_automation") + [
            "https://cucumber.io/docs/gherkin/reference/",
            "https://cucumber.io/docs/gherkin/languages/",
        ],
    },
    "contract-testing": {
        "tags": ["contract testing", "consumer-driven contracts", "service virtualization", "api testing"],
        "license": CC_BY_SA,
        "pages": wiki("Service_virtualization", "Software_testing", "Regression_testing", "Web_testing", "Test_automation", "Continuous_integration"),
    },
    "snapshot-testing": {
        "tags": ["snapshot testing", "characterization test", "regression testing", "golden master"],
        "license": CC_BY_SA,
        "pages": wiki("Characterization_test", "Regression_testing", "Software_testing", "Unit_testing", "Test_automation") + [
            "https://jestjs.io/docs/snapshot-testing",
        ],
    },

    # ---- package managers ----------------------------------------------------
    "pnpm": {
        "tags": ["pnpm package", "node package manager", "javascript packages", "content-addressable store"],
        "license": CC_BY_SA,
        "pages": wiki("Npm", "Package_manager", "Node.js") + [
            "https://pnpm.io/motivation",
            "https://pnpm.io/workspaces",
            "https://pnpm.io/pnpm-cli",
        ],
    },
    "yarn-package": {
        "tags": ["yarn package", "node package manager", "javascript packages", "workspaces monorepo"],
        "license": CC_BY_SA,
        "pages": wiki("Yarn_(package_manager)", "Package_manager", "Node.js") + [
            "https://classic.yarnpkg.com/en/docs",
            "https://classic.yarnpkg.com/en/docs/cli/",
            "https://classic.yarnpkg.com/lang/en/docs/workspaces/",
        ],
    },
    "poetry-python": {
        "tags": ["poetry python", "python packaging", "dependency management", "pyproject toml"],
        "license": CC_BY_SA,
        "pages": wiki("Package_manager", "Python_(programming_language)", "Software_repository") + [
            "https://python-poetry.org/docs/",
            "https://python-poetry.org/docs/basic-usage/",
            "https://python-poetry.org/docs/managing-dependencies/",
            "https://python-poetry.org/docs/dependency-specification/",
        ],
    },
    "uv-python": {
        "tags": ["uv python", "python packaging", "dependency resolver", "pip replacement"],
        "license": CC_BY_SA,
        "pages": wiki("Package_manager", "Python_(programming_language)", "Software_repository") + [
            "https://docs.astral.sh/uv/",
            "https://docs.astral.sh/uv/guides/projects/",
            "https://docs.astral.sh/uv/concepts/projects/dependencies/",
            "https://docs.astral.sh/uv/pip/",
        ],
    },
    "conda-package": {
        "tags": ["conda package", "python environments", "package manager", "anaconda distribution"],
        "license": CC_BY_SA,
        "pages": wiki("Conda_(package_manager)", "Anaconda_(Python_distribution)", "Package_manager") + [
            "https://docs.conda.io/projects/conda/en/stable/",
            "https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html",
            "https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/environments.html",
        ],
    },
    "homebrew": {
        "tags": ["homebrew macos", "package manager", "formula cookbook", "unix packages"],
        "license": CC_BY_SA,
        "pages": wiki("Homebrew_(package_manager)", "Package_manager", "Linux") + [
            "https://docs.brew.sh/",
            "https://docs.brew.sh/Installation",
            "https://docs.brew.sh/Formula-Cookbook",
        ],
    },
    "apt-package": {
        "tags": ["apt package", "debian packages", "package manager", "advanced package tool"],
        "license": CC_BY_SA,
        "pages": wiki("APT_(software)", "Debian", "Package_manager") + [
            "https://manpages.debian.org/bookworm/apt/apt.8.en.html",
            "https://manpages.debian.org/bookworm/apt/apt-get.8.en.html",
            "https://manpages.debian.org/bookworm/apt/sources.list.5.en.html",
        ],
    },
    "dpkg": {
        "tags": ["dpkg debian", "debian packages", "package manager", "deb archive"],
        "license": CC_BY_SA,
        "pages": wiki("Dpkg", "Debian", "Package_manager", "APT_(software)") + [
            "https://manpages.debian.org/bookworm/dpkg/dpkg.1.en.html",
            "https://manpages.debian.org/bookworm/dpkg/dpkg-deb.1.en.html",
            "https://manpages.debian.org/bookworm/dpkg/dpkg-query.1.en.html",
        ],
    },
    "pacman-arch": {
        "tags": ["pacman arch", "arch linux packages", "package manager", "unix packages"],
        "license": CC_BY_SA,
        "pages": wiki("Arch_Linux", "Package_manager", "Linux") + [
            "https://wiki.archlinux.org/title/Pacman",
            "https://wiki.archlinux.org/title/Pacman/Rosetta",
            "https://man.archlinux.org/man/pacman.conf.5",
        ],
    },
    "vcpkg": {
        "tags": ["vcpkg cpp", "c++ packages", "package manager", "manifest mode"],
        "license": CC_BY_SA,
        "pages": wiki("Vcpkg", "Package_manager", "C%2B%2B") + [
            "https://learn.microsoft.com/en-us/vcpkg/get_started/get-started",
            "https://learn.microsoft.com/en-us/vcpkg/concepts/manifest-mode",
            "https://learn.microsoft.com/en-us/vcpkg/users/buildsystems/cmake-integration",
        ],
    },
    "conan-cpp": {
        "tags": ["conan cpp", "c++ packages", "package manager", "dependency management"],
        "license": CC_BY_SA,
        "pages": wiki("Package_manager", "C%2B%2B", "Software_repository") + [
            "https://docs.conan.io/2/",
            "https://docs.conan.io/2/tutorial/consuming_packages.html",
            "https://docs.conan.io/2/tutorial/creating_packages.html",
        ],
    },

    # ---- build tools ---------------------------------------------------------
    "meson-build": {
        "tags": ["meson build", "build system", "build automation", "ninja backend"],
        "license": CC_BY_SA,
        "pages": wiki("Meson_(software)", "Build_automation", "Software_build") + [
            "https://mesonbuild.com/Tutorial.html",
            "https://mesonbuild.com/Syntax.html",
            "https://mesonbuild.com/Reference-manual.html",
            "https://mesonbuild.com/Quick-guide.html",
        ],
    },
    "ninja-build": {
        "tags": ["ninja build", "build system", "build automation", "incremental builds"],
        "license": CC_BY_SA,
        "pages": wiki("Ninja_(build_system)", "Build_automation", "Software_build", "Make_(software)") + [
            "https://ninja-build.org/manual.html",
            "https://ninja-build.org/",
        ],
    },
    "gnu-autotools": {
        "tags": ["gnu autotools", "autoconf configure", "automake build", "build automation"],
        "license": CC_BY_SA,
        "pages": wiki("GNU_Autotools", "Build_automation", "Software_build") + [
            "https://www.gnu.org/software/autoconf/manual/autoconf.html",
            "https://www.gnu.org/software/automake/manual/automake.html",
            "https://www.gnu.org/software/libtool/manual/libtool.html",
        ],
    },

    # ---- editors -------------------------------------------------------------
    "vim-editor": {
        "tags": ["vim editor", "text editor", "modal editing", "terminal editor"],
        "license": CC_BY_SA,
        "pages": wiki("Vim_(text_editor)", "Text_editor", "Integrated_development_environment") + [
            "https://vimhelp.org/usr_02.txt.html",
            "https://vimhelp.org/quickref.txt.html",
            "https://www.vim.org/docs.php",
        ],
    },
    "neovim": {
        "tags": ["neovim editor", "text editor", "modal editing", "lua configuration"],
        "license": CC_BY_SA,
        "pages": wiki("Neovim", "Vim_(text_editor)", "Text_editor") + [
            "https://neovim.io/doc/user/",
            "https://neovim.io/doc/user/lua.html",
            "https://neovim.io/doc/user/quickref.html",
        ],
    },
    "emacs-editor": {
        "tags": ["emacs editor", "text editor", "elisp scripting", "extensible editor"],
        "license": CC_BY_SA,
        "pages": wiki("GNU_Emacs", "Emacs", "Lisp_(programming_language)") + [
            "https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html",
            "https://www.gnu.org/software/emacs/manual/html_node/elisp/index.html",
            "https://www.gnu.org/software/emacs/tour/",
        ],
    },

    # ---- docs tooling --------------------------------------------------------
    "sphinx-docs": {
        "tags": ["sphinx docs", "documentation generator", "restructuredtext source", "read the docs"],
        "license": CC_BY_SA,
        "pages": wiki("Sphinx_(documentation_generator)", "Read_the_Docs", "Comparison_of_documentation_generators") + [
            "https://www.sphinx-doc.org/en/master/",
            "https://www.sphinx-doc.org/en/master/usage/quickstart.html",
            "https://www.sphinx-doc.org/en/master/tutorial/index.html",
        ],
    },
    "mkdocs": {
        "tags": ["mkdocs static", "documentation generator", "markdown docs", "static site"],
        "license": CC_BY_SA,
        "pages": wiki("Markdown", "Comparison_of_documentation_generators", "Read_the_Docs") + [
            "https://www.mkdocs.org/",
            "https://www.mkdocs.org/user-guide/writing-your-docs/",
            "https://www.mkdocs.org/user-guide/configuration/",
            "https://squidfunk.github.io/mkdocs-material/getting-started/",
        ],
    },
    "doxygen": {
        "tags": ["doxygen docs", "documentation generator", "api documentation", "source comments"],
        "license": CC_BY_SA,
        "pages": wiki("Doxygen", "Comparison_of_documentation_generators", "Cross-reference") + [
            "https://www.doxygen.nl/manual/index.html",
            "https://www.doxygen.nl/manual/docblocks.html",
            "https://www.doxygen.nl/manual/commands.html",
            "https://www.doxygen.nl/manual/config.html",
        ],
    },
    "javadoc": {
        "tags": ["javadoc java", "documentation generator", "api documentation", "doc comments"],
        "license": CC_BY_SA,
        "pages": wiki("Javadoc", "Java_(programming_language)", "Comparison_of_documentation_generators", "Cross-reference") + [
            "https://docs.oracle.com/en/java/javase/21/javadoc/javadoc-tool.html",
            "https://docs.oracle.com/en/java/javase/17/docs/api/index.html",
        ],
    },
    "latex-typesetting": {
        "tags": ["latex typesetting", "tex document", "document preparation", "typeset math"],
        "license": CC_BY_SA,
        "pages": wiki("LaTeX", "TeX", "Typesetting") + [
            "https://www.latex-project.org/help/documentation/",
            "https://www.latex-project.org/help/documentation/usrguide.pdf",
            "https://www.tug.org/tutorials/tugindia/",
        ],
    },
    "pandoc": {
        "tags": ["pandoc converter", "document conversion", "markup converter", "markdown to pdf"],
        "license": CC_BY_SA,
        "pages": wiki("Pandoc", "Markup_language", "Lightweight_markup_language") + [
            "https://pandoc.org/MANUAL.html",
            "https://pandoc.org/getting-started.html",
            "https://pandoc.org/demos.html",
        ],
    },
    "asciidoc": {
        "tags": ["asciidoc markup", "lightweight markup", "asciidoctor docs", "text markup"],
        "license": CC_BY_SA,
        "pages": wiki("AsciiDoc", "Lightweight_markup_language", "Markup_language") + [
            "https://asciidoc.org/",
            "https://asciidoc.org/userguide.html",
            "https://docs.asciidoctor.org/asciidoc/latest/",
            "https://docs.asciidoctor.org/asciidoc/latest/document-structure/",
        ],
    },
    "restructuredtext": {
        "tags": ["restructuredtext markup", "docutils parser", "lightweight markup", "sphinx source"],
        "license": CC_BY_SA,
        "pages": wiki("ReStructuredText", "Lightweight_markup_language", "Markup_language") + [
            "https://docutils.sourceforge.io/rst.html",
            "https://docutils.sourceforge.io/docs/user/rst/quickstart.html",
            "https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html",
        ],
    },

    # ---- version control -----------------------------------------------------
    "mercurial-vcs": {
        "tags": ["mercurial vcs", "distributed version control", "hg repository", "changeset history"],
        "license": CC_BY_SA,
        "pages": wiki("Mercurial", "Distributed_version_control", "Version_control") + [
            "https://www.mercurial-scm.org/wiki/Tutorial",
            "https://www.mercurial-scm.org/wiki/UnderstandingMercurial",
            "https://www.mercurial-scm.org/wiki/GitConcepts",
        ],
    },
    "subversion": {
        "tags": ["subversion svn", "centralized version control", "apache subversion", "revision repository"],
        "license": CC_BY_SA,
        "pages": wiki("Apache_Subversion", "Version_control", "Repository_(version_control)") + [
            "https://subversion.apache.org/docs/",
            "https://svnbook.red-bean.com/en/1.7/svn.tour.html",
            "https://svnbook.red-bean.com/en/1.7/svn.branchmerge.html",
        ],
    },

    # ---- cli utilities -------------------------------------------------------
    "tmux": {
        "tags": ["tmux multiplexer", "terminal multiplexer", "terminal sessions", "pane splitting"],
        "license": CC_BY_SA,
        "pages": wiki("Tmux", "Terminal_multiplexer", "GNU_Screen") + [
            "https://github.com/tmux/tmux/wiki",
            "https://github.com/tmux/tmux/wiki/Getting-Started",
            "https://github.com/tmux/tmux/wiki/Advanced-Use",
        ],
    },
    "jq-json": {
        "tags": ["jq json", "json processor", "command-line json", "json filter"],
        "license": CC_BY_SA,
        "pages": wiki("Jq_(programming_language)", "JSON", "JSON_streaming") + [
            "https://jqlang.github.io/jq/manual/",
            "https://jqlang.github.io/jq/tutorial/",
            "https://man.archlinux.org/man/jq.1",
        ],
    },
    "ripgrep": {
        "tags": ["ripgrep search", "string searching", "recursive grep", "command-line search"],
        "license": CC_BY_SA,
        "pages": wiki("String-searching_algorithm", "Grep", "Command-line_interface") + [
            "https://github.com/BurntSushi/ripgrep",
            "https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md",
            "https://github.com/BurntSushi/ripgrep/blob/master/FAQ.md",
            "https://man.archlinux.org/man/rg.1",
        ],
    },
    "fzf": {
        "tags": ["fzf finder", "fuzzy finder", "command-line interface", "interactive filter"],
        "license": CC_BY_SA,
        "pages": wiki("Command-line_interface", "Interactive_computing", "String-searching_algorithm") + [
            "https://github.com/junegunn/fzf",
            "https://github.com/junegunn/fzf/blob/master/README.md",
            "https://github.com/junegunn/fzf/wiki/examples",
            "https://man.archlinux.org/man/fzf.1",
        ],
    },
    "curl-http-tool": {
        "tags": ["curl http", "http client", "data transfer", "command-line http"],
        "license": CC_BY_SA,
        "pages": wiki("CURL", "Hypertext_Transfer_Protocol", "Command-line_interface") + [
            "https://curl.se/docs/manual.html",
            "https://curl.se/docs/httpscripting.html",
            "https://curl.se/docs/tutorial.html",
            "https://curl.se/docs/manpage.html",
        ],
    },
    "wget": {
        "tags": ["wget download", "file download", "recursive download", "command-line http"],
        "license": CC_BY_SA,
        "pages": wiki("Wget", "Download", "File_Transfer_Protocol") + [
            "https://www.gnu.org/software/wget/manual/wget.html",
            "https://www.gnu.org/software/wget/manual/html_node/index.html",
            "https://www.gnu.org/software/wget/manual/html_node/Recursive-Download.html",
        ],
    },
}
