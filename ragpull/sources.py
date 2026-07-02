"""THE SOURCE REGISTRY — every knowledge domain a coding swarm might need to ground itself in.

Curation rules (mirrors the nl-veil atlas):
  1. official documentation first; encyclopedic (Wikipedia) for concepts that have no single owner
  2. every URL must serve real HTML to a plain GET (no JS-walled apps)
  3. concrete content pages over homepages — the normalizer turns ONE page into ONE clean pack file
  4. tags must survive word-bounded matching (never a bare common English word)

Domain names deliberately match nl-veil's src/worker/locs/atlas.zig entries so the packs
wire into the veil one-to-one.
"""

WIKI = "https://en.wikipedia.org/wiki/"

# license identifiers used in frontmatter; full attribution lives in SOURCES.md
PSF = "PSF-2.0"
MIT_APACHE = "MIT OR Apache-2.0"
CC_BY_SA = "CC-BY-SA-4.0"
CC_BY_SA_25 = "CC-BY-SA-2.5"  # MDN prose
GFDL = "GFDL-1.3"  # GNU manuals
GPL2 = "GPL-2.0"  # git docs, linux man-pages (varies per page)
BSD = "BSD-3-Clause"
PD = "Public-Domain"
OWASP = "CC-BY-SA-4.0"  # OWASP cheat sheet series
APACHE = "Apache-2.0"
PG = "PostgreSQL"

def _mdn(path):
    return "https://developer.mozilla.org/en-US/docs/" + path

def _man7(page):
    sec = page.rsplit(".", 1)[1]
    return f"https://man7.org/linux/man-pages/man{sec}/{page}.html"


DOMAINS = {
    # ------------------------------------------------------------------ languages
    "python": {
        "tags": ["python", "pytest", "cpython", "pip"],
        "license": PSF,
        "pages": [
            "https://docs.python.org/3/tutorial/introduction.html",
            "https://docs.python.org/3/tutorial/controlflow.html",
            "https://docs.python.org/3/tutorial/datastructures.html",
            "https://docs.python.org/3/tutorial/modules.html",
            "https://docs.python.org/3/tutorial/errors.html",
            "https://docs.python.org/3/tutorial/classes.html",
            "https://docs.python.org/3/library/functions.html",
            "https://docs.python.org/3/library/stdtypes.html",
            "https://docs.python.org/3/library/json.html",
            "https://docs.python.org/3/library/os.path.html",
            "https://docs.python.org/3/library/pathlib.html",
            "https://docs.python.org/3/library/re.html",
            "https://docs.python.org/3/library/sqlite3.html",
            "https://docs.python.org/3/library/asyncio-task.html",
            "https://docs.python.org/3/library/typing.html",
            "https://docs.python.org/3/library/unittest.html",
            "https://docs.python.org/3/library/http.server.html",
            "https://docs.python.org/3/library/urllib.request.html",
            "https://docs.python.org/3/library/itertools.html",
            "https://docs.python.org/3/library/functools.html",
            "https://docs.python.org/3/library/dataclasses.html",
            "https://docs.python.org/3/library/venv.html",
            "https://docs.python.org/3/library/logging.html",
            "https://docs.python.org/3/library/subprocess.html",
            "https://docs.python.org/3/library/threading.html",
            "https://docs.python.org/3/library/datetime.html",
            "https://docs.python.org/3/library/collections.html",
            "https://docs.pytest.org/en/stable/getting-started.html",
            "https://docs.pytest.org/en/stable/how-to/fixtures.html",
            "https://docs.pytest.org/en/stable/how-to/parametrize.html",
            "https://docs.pytest.org/en/stable/how-to/assert.html",
        ],
    },
    "rust": {
        "tags": ["rust", "cargo", "borrow checker", "rustc"],
        "license": MIT_APACHE,
        "pages": [
            "https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html",
            "https://doc.rust-lang.org/book/ch03-02-data-types.html",
            "https://doc.rust-lang.org/book/ch03-03-how-functions-work.html",
            "https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html",
            "https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html",
            "https://doc.rust-lang.org/book/ch04-03-slices.html",
            "https://doc.rust-lang.org/book/ch05-01-defining-structs.html",
            "https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html",
            "https://doc.rust-lang.org/book/ch08-01-vectors.html",
            "https://doc.rust-lang.org/book/ch08-02-strings.html",
            "https://doc.rust-lang.org/book/ch08-03-hash-maps.html",
            "https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html",
            "https://doc.rust-lang.org/book/ch10-02-traits.html",
            "https://doc.rust-lang.org/book/ch10-03-lifetime-syntax.html",
            "https://doc.rust-lang.org/book/ch13-02-iterators.html",
            "https://doc.rust-lang.org/book/ch16-01-threads.html",
            "https://doc.rust-lang.org/std/option/index.html",
            "https://doc.rust-lang.org/std/result/index.html",
            "https://doc.rust-lang.org/std/vec/struct.Vec.html",
            "https://doc.rust-lang.org/std/string/struct.String.html",
            "https://doc.rust-lang.org/std/collections/index.html",
            "https://doc.rust-lang.org/cargo/guide/dependencies.html",
            "https://doc.rust-lang.org/cargo/reference/manifest.html",
        ],
    },
    "ruby": {
        "tags": ["ruby", "rails", "rubygem"],
        "license": "Ruby-BSD / CC-BY-SA-4.0 (Rails guides)",
        "pages": [
            "https://ruby-doc.org/core/String.html",
            "https://ruby-doc.org/core/Array.html",
            "https://ruby-doc.org/core/Hash.html",
            "https://ruby-doc.org/core/Enumerable.html",
            "https://ruby-doc.org/core/File.html",
            "https://ruby-doc.org/core/Regexp.html",
            "https://guides.rubyonrails.org/getting_started.html",
            "https://guides.rubyonrails.org/active_record_basics.html",
            "https://guides.rubyonrails.org/routing.html",
            "https://guides.rubyonrails.org/action_controller_overview.html",
        ],
    },
    "golang": {
        "tags": ["golang", "goroutine", "go module", "go stdlib"],
        "license": BSD,
        "pages": [
            "https://go.dev/doc/effective_go",
            "https://go.dev/ref/spec",
            "https://go.dev/doc/tutorial/getting-started",
            "https://pkg.go.dev/net/http",
            "https://pkg.go.dev/fmt",
            "https://pkg.go.dev/encoding/json",
            "https://pkg.go.dev/errors",
            "https://pkg.go.dev/strings",
            "https://pkg.go.dev/os",
            "https://pkg.go.dev/context",
            "https://pkg.go.dev/sync",
        ],
    },
    "javascript": {
        "tags": ["javascript", "typescript", "node.js", "nodejs", "npm"],
        "license": CC_BY_SA_25 + " (MDN) / MIT (Node.js)",
        "pages": [
            _mdn("Web/JavaScript/Guide/Introduction"),
            _mdn("Web/JavaScript/Guide/Grammar_and_types"),
            _mdn("Web/JavaScript/Guide/Control_flow_and_error_handling"),
            _mdn("Web/JavaScript/Guide/Loops_and_iteration"),
            _mdn("Web/JavaScript/Guide/Functions"),
            _mdn("Web/JavaScript/Guide/Expressions_and_operators"),
            _mdn("Web/JavaScript/Guide/Working_with_objects"),
            _mdn("Web/JavaScript/Guide/Using_classes"),
            _mdn("Web/JavaScript/Guide/Using_promises"),
            _mdn("Web/JavaScript/Guide/Iterators_and_generators"),
            _mdn("Web/JavaScript/Reference/Global_Objects/Array"),
            _mdn("Web/JavaScript/Reference/Global_Objects/String"),
            _mdn("Web/JavaScript/Reference/Global_Objects/Promise"),
            _mdn("Web/JavaScript/Reference/Global_Objects/JSON"),
            _mdn("Web/JavaScript/Reference/Statements/async_function"),
            "https://nodejs.org/api/fs.html",
            "https://nodejs.org/api/http.html",
            "https://nodejs.org/api/path.html",
            "https://nodejs.org/api/process.html",
            "https://nodejs.org/api/events.html",
        ],
    },
    "web-platform": {
        "tags": ["html", "css", "dom", "frontend"],
        "license": CC_BY_SA_25,
        "pages": [
            _mdn("Web/HTML/Element/form"),
            _mdn("Web/HTML/Element/input"),
            _mdn("Web/HTML/Element/table"),
            _mdn("Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox"),
            _mdn("Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout"),
            _mdn("Web/CSS/CSS_selectors"),
            _mdn("Web/API/Document_Object_Model/Introduction"),
            _mdn("Web/API/Fetch_API/Using_Fetch"),
        ],
    },
    "zig": {
        "tags": ["zig", "comptime"],
        "license": "MIT",
        "pages": [
            "https://ziglang.org/documentation/master/",
            "https://ziglang.org/learn/overview/",
        ],
    },
    "c-cpp": {
        "tags": ["cpp", "c language", "c standard library", "clang"],
        "license": "CC-BY-SA-3.0 (cppreference)",
        "pages": [
            "https://en.cppreference.com/w/cpp/language/pointer",
            "https://en.cppreference.com/w/cpp/language/reference",
            "https://en.cppreference.com/w/cpp/language/classes",
            "https://en.cppreference.com/w/cpp/language/lambda",
            "https://en.cppreference.com/w/cpp/container/vector",
            "https://en.cppreference.com/w/cpp/string/basic_string",
            "https://en.cppreference.com/w/cpp/memory/unique_ptr",
            "https://en.cppreference.com/w/cpp/memory/shared_ptr",
            "https://en.cppreference.com/w/c/memory/malloc",
            "https://en.cppreference.com/w/c/io/fprintf",
        ],
    },
    # ------------------------------------------------------------------ web & protocols
    "http-rest": {
        "tags": ["http", "rest api", "endpoint", "cookie", "cors", "websocket"],
        "license": CC_BY_SA_25 + " / IETF-Trust (RFC)",
        "pages": [
            _mdn("Web/HTTP/Overview"),
            _mdn("Web/HTTP/Methods"),
            _mdn("Web/HTTP/Status"),
            _mdn("Web/HTTP/Headers"),
            _mdn("Web/HTTP/CORS"),
            _mdn("Web/HTTP/Cookies"),
            _mdn("Web/HTTP/Caching"),
            "https://www.rfc-editor.org/rfc/rfc9110.html",
        ],
    },
    "web-frameworks": {
        "tags": ["flask", "django", "expressjs", "express.js", "web framework"],
        "license": "BSD-3-Clause (Flask/Django) / CC-BY-SA-3.0 (Express)",
        "pages": [
            "https://flask.palletsprojects.com/en/stable/quickstart/",
            "https://flask.palletsprojects.com/en/stable/blueprints/",
            "https://expressjs.com/en/guide/routing.html",
            "https://expressjs.com/en/guide/using-middleware.html",
            "https://expressjs.com/en/starter/hello-world.html",
            "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
            "https://docs.djangoproject.com/en/stable/topics/db/models/",
        ],
    },
    # ------------------------------------------------------------------ data
    "sql-sqlite": {
        "tags": ["sql", "sqlite", "database schema"],
        "license": PD,
        "pages": [
            "https://sqlite.org/lang_select.html",
            "https://sqlite.org/lang_createtable.html",
            "https://sqlite.org/lang_insert.html",
            "https://sqlite.org/lang_update.html",
            "https://sqlite.org/lang_delete.html",
            "https://sqlite.org/lang_expr.html",
            "https://sqlite.org/lang_corefunc.html",
            "https://sqlite.org/lang_aggfunc.html",
            "https://sqlite.org/lang_transaction.html",
            "https://sqlite.org/datatype3.html",
            "https://sqlite.org/foreignkeys.html",
            "https://sqlite.org/queryplanner.html",
        ],
    },
    "databases": {
        "tags": ["postgres", "postgresql", "relational database", "transaction", "acid", "database index"],
        "license": CC_BY_SA + " / " + PG,
        "pages": [
            WIKI + "Relational_database",
            WIKI + "ACID",
            WIKI + "Database_index",
            WIKI + "Database_transaction",
            WIKI + "Database_normalization",
            WIKI + "NoSQL",
            "https://www.postgresql.org/docs/current/tutorial-table.html",
            "https://www.postgresql.org/docs/current/tutorial-select.html",
            "https://www.postgresql.org/docs/current/tutorial-join.html",
            "https://www.postgresql.org/docs/current/tutorial-agg.html",
        ],
    },
    "data-formats": {
        "tags": ["json", "yaml", "toml", "xml", "csv", "base64", "markdown"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "JSON",
            WIKI + "YAML",
            WIKI + "TOML",
            WIKI + "XML",
            WIKI + "Comma-separated_values",
            WIKI + "Base64",
            WIKI + "Markdown",
        ],
    },
    # ------------------------------------------------------------------ CS foundations
    "algorithms": {
        "tags": ["algorithm", "sorting", "complexity", "big-o", "dynamic programming"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Binary_search",
            WIKI + "Quicksort",
            WIKI + "Merge_sort",
            WIKI + "Sorting_algorithm",
            WIKI + "Hash_table",
            WIKI + "Dynamic_programming",
            WIKI + "Big_O_notation",
            WIKI + "Breadth-first_search",
            WIKI + "Depth-first_search",
            WIKI + "Dijkstra's_algorithm",
            WIKI + "Greedy_algorithm",
            WIKI + "Recursion_(computer_science)",
        ],
    },
    "data-structures": {
        "tags": ["data structure", "hash table", "binary tree", "linked list", "b-tree"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Array_(data_structure)",
            WIKI + "Linked_list",
            WIKI + "Stack_(abstract_data_type)",
            WIKI + "Queue_(abstract_data_type)",
            WIKI + "Binary_search_tree",
            WIKI + "B-tree",
            WIKI + "Heap_(data_structure)",
            WIKI + "Trie",
            WIKI + "Graph_(abstract_data_type)",
            WIKI + "Bloom_filter",
            WIKI + "Skip_list",
        ],
    },
    "software-design": {
        "tags": ["design pattern", "software architecture", "software design", "refactoring"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Software_design_pattern",
            WIKI + "SOLID",
            WIKI + "Singleton_pattern",
            WIKI + "Factory_method_pattern",
            WIKI + "Observer_pattern",
            WIKI + "Strategy_pattern",
            WIKI + "Adapter_pattern",
            WIKI + "Decorator_pattern",
            WIKI + "Model%E2%80%93view%E2%80%93controller",
            WIKI + "Dependency_injection",
            WIKI + "Domain-driven_design",
            WIKI + "Microservices",
        ],
    },
    "concurrency": {
        "tags": ["thread", "mutex", "deadlock", "race condition", "semaphore", "event loop", "concurrency"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Thread_(computing)",
            WIKI + "Process_(computing)",
            WIKI + "Mutual_exclusion",
            WIKI + "Deadlock_(computer_science)",
            WIKI + "Race_condition",
            WIKI + "Semaphore_(programming)",
            WIKI + "Event_loop",
            WIKI + "Futures_and_promises",
            WIKI + "Async/await",
            WIKI + "Producer%E2%80%93consumer_problem",
        ],
    },
    "machine-learning": {
        "tags": ["machine learning", "neural network", "llm", "embedding", "transformer model", "gradient descent"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Machine_learning",
            WIKI + "Artificial_neural_network",
            WIKI + "Transformer_(deep_learning_architecture)",
            WIKI + "Gradient_descent",
            WIKI + "Backpropagation",
            WIKI + "Large_language_model",
            WIKI + "Retrieval-augmented_generation",
            WIKI + "Word_embedding",
        ],
    },
    # ------------------------------------------------------------------ security
    "security": {
        "tags": ["security", "authentication", "password hashing", "session token", "tls", "owasp"],
        "license": OWASP + " (OWASP) / " + CC_BY_SA + " (Wikipedia)",
        "pages": [
            "https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html",
            "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html",
            WIKI + "PBKDF2",
            WIKI + "Transport_Layer_Security",
            WIKI + "OAuth",
            WIKI + "JSON_Web_Token",
            WIKI + "Cross-site_scripting",
        ],
    },
    "crypto": {
        "tags": ["cryptography", "encryption", "aes", "rsa", "hmac", "sha-256", "digital signature"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Advanced_Encryption_Standard",
            WIKI + "RSA_(cryptosystem)",
            WIKI + "SHA-2",
            WIKI + "HMAC",
            WIKI + "Public-key_cryptography",
            WIKI + "Diffie%E2%80%93Hellman_key_exchange",
            WIKI + "Digital_signature",
            WIKI + "Salt_(cryptography)",
        ],
    },
    # ------------------------------------------------------------------ tooling & ops
    "git": {
        "tags": ["git", "merge conflict", "version control"],
        "license": GPL2,
        "pages": [
            "https://git-scm.com/docs/git-commit",
            "https://git-scm.com/docs/git-merge",
            "https://git-scm.com/docs/git-rebase",
            "https://git-scm.com/docs/git-branch",
            "https://git-scm.com/docs/git-checkout",
            "https://git-scm.com/docs/git-log",
            "https://git-scm.com/docs/git-push",
            "https://git-scm.com/docs/git-pull",
            "https://git-scm.com/docs/git-reset",
            "https://git-scm.com/docs/git-stash",
            "https://git-scm.com/docs/git-diff",
            "https://git-scm.com/docs/git-remote",
            "https://git-scm.com/docs/gitglossary",
        ],
    },
    "shell-linux": {
        "tags": ["bash", "shell script", "linux command", "posix"],
        "license": GFDL + " (bash manual) / GPL-2.0 (man-pages)",
        "pages": [
            "https://www.gnu.org/software/bash/manual/bash.html",
            _man7("grep.1"),
            _man7("sed.1"),
            _man7("find.1"),
            _man7("xargs.1"),
            _man7("tar.1"),
            _man7("chmod.1"),
            _man7("ps.1"),
            _man7("kill.1"),
        ],
    },
    "sysadmin-ops": {
        "tags": ["systemd", "cron", "ssh", "rsync", "sysadmin", "devops"],
        "license": GPL2 + " / " + CC_BY_SA,
        "pages": [
            _man7("systemctl.1"),
            _man7("journalctl.1"),
            _man7("crontab.5"),
            _man7("rsync.1"),
            _man7("ip.8"),
            _man7("ss.8"),
            WIKI + "Cron",
            WIKI + "Systemd",
            WIKI + "Secure_Shell",
        ],
    },
    "docker-containers": {
        "tags": ["docker", "container", "dockerfile", "kubernetes", "docker compose"],
        "license": APACHE,
        "pages": [
            "https://docs.docker.com/get-started/docker-overview/",
            "https://docs.docker.com/reference/dockerfile/",
            "https://docs.docker.com/engine/network/",
            "https://docs.docker.com/engine/storage/volumes/",
            "https://docs.docker.com/build/building/best-practices/",
            WIKI + "Kubernetes",
        ],
    },
    "networking": {
        "tags": ["tcp", "udp", "dns", "ip address", "socket", "networking"],
        "license": CC_BY_SA + " / GPL-2.0 (man-pages)",
        "pages": [
            WIKI + "Transmission_Control_Protocol",
            WIKI + "User_Datagram_Protocol",
            WIKI + "Internet_Protocol",
            WIKI + "Domain_Name_System",
            WIKI + "IP_address",
            WIKI + "OSI_model",
            WIKI + "HTTPS",
            WIKI + "WebSocket",
            _man7("socket.2"),
            _man7("tcp.7"),
        ],
    },
    "build-systems": {
        "tags": ["makefile", "cmake", "build system", "compiler toolchain"],
        "license": GFDL + " / " + CC_BY_SA,
        "pages": [
            "https://www.gnu.org/software/make/manual/make.html",
            WIKI + "Make_(software)",
            WIKI + "CMake",
        ],
    },
    "testing": {
        "tags": ["unit test", "tdd", "integration test", "continuous integration", "code review"],
        "license": CC_BY_SA,
        "pages": [
            WIKI + "Unit_testing",
            WIKI + "Test-driven_development",
            WIKI + "Integration_testing",
            WIKI + "Continuous_integration",
            WIKI + "Code_review",
            WIKI + "Mock_object",
        ],
    },
    "regex": {
        "tags": ["regex", "regular expression"],
        "license": CC_BY_SA_25 + " / " + CC_BY_SA + " / " + PSF,
        "pages": [
            _mdn("Web/JavaScript/Guide/Regular_expressions"),
            _mdn("Web/JavaScript/Guide/Regular_expressions/Character_classes"),
            _mdn("Web/JavaScript/Guide/Regular_expressions/Quantifiers"),
            _mdn("Web/JavaScript/Guide/Regular_expressions/Groups_and_backreferences"),
            WIKI + "Regular_expression",
            "https://docs.python.org/3/howto/regex.html",
        ],
    },
}


def slug_for(url: str) -> str:
    """Stable filesystem slug for a page URL: last meaningful path segments, lowercased,
    [a-z0-9-] only. Distinct URLs in one domain never collide (verified at registry load)."""
    from urllib.parse import urlparse, unquote

    p = urlparse(url)
    path = unquote(p.path).strip("/")
    if not path:
        path = p.netloc.replace(".", "-")
    segs = [s for s in path.split("/") if s not in ("", "en-US", "en", "docs", "wiki", "w", "stable", "current", "master", "3")]
    tail = segs[-2:] if len(segs) >= 2 and len(segs[-1]) < 12 else segs[-1:]
    raw = "-".join(tail)
    for suf in (".html", ".1", ".2", ".5", ".7", ".8"):
        if raw.endswith(suf):
            raw = raw[: -len(suf)]
    out = []
    for c in raw.lower():
        out.append(c if c.isalnum() else "-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return s.strip("-")[:80] or "page"


def check_registry():
    """Fail fast on slug collisions inside a domain."""
    for name, d in DOMAINS.items():
        seen = {}
        for url in d["pages"]:
            s = slug_for(url)
            if s in seen:
                raise SystemExit(f"slug collision in {name}: {seen[s]} vs {url} -> {s}")
            seen[s] = url


check_registry()
