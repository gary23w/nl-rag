"""Popular Python libraries and their concepts."""

from .common import CC_BY_SA, wiki

DOMAINS = {
    "requests-http": {
        "tags": ["python requests", "http client python", "requests library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Requests_(software)",
            "Hypertext_Transfer_Protocol",
            "HTTP_client",
            "HTTP_cookie",
            "Percent-encoding",
        ) + [
            "https://requests.readthedocs.io/en/latest/user/quickstart/",
            "https://requests.readthedocs.io/en/latest/user/advanced/",
            "https://requests.readthedocs.io/en/latest/user/authentication/",
        ],
    },
    "httpx-client": {
        "tags": ["python httpx", "async http client", "httpx library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Hypertext_Transfer_Protocol_Secure",
            "HTTP/2",
            "Connection_pool",
            "Representational_state_transfer",
            "HTTP_message_body",
        ) + [
            "https://www.python-httpx.org/quickstart/",
            "https://www.python-httpx.org/async/",
            "https://www.python-httpx.org/api/",
        ],
    },
    "aiohttp-client": {
        "tags": ["python aiohttp", "asyncio http", "aiohttp library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Asynchronous_I/O",
            "Event_loop",
            "WebSocket",
            "HTTP_persistent_connection",
            "Web_server",
        ) + [
            "https://docs.aiohttp.org/en/stable/client_quickstart.html",
            "https://docs.aiohttp.org/en/stable/web_quickstart.html",
        ],
    },
    "pydantic-validation": {
        "tags": ["python pydantic", "data validation library", "pydantic models"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_validation",
            "Type_system",
            "Type_hint",
            "Serialization",
            "Data_type",
        ) + [
            "https://docs.pydantic.dev/latest/concepts/models/",
            "https://docs.pydantic.dev/latest/concepts/validators/",
        ],
    },
    "click-cli": {
        "tags": ["python click", "click cli", "command line parsing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_interface",
            "Command-line_argument_parsing",
            "Usability",
            "Getopt",
            "Standard_streams",
            "Exit_status",
        ) + [
            "https://click.palletsprojects.com/en/stable/quickstart/",
            "https://click.palletsprojects.com/en/stable/options/",
        ],
    },
    "typer-cli": {
        "tags": ["python typer", "typer cli", "type hint cli"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Command-line_interface",
            "Type_hint",
            "Command-line_argument_parsing",
            "Standard_streams",
            "Usability",
        ) + [
            "https://typer.tiangolo.com/tutorial/",
            "https://typer.tiangolo.com/tutorial/arguments/",
        ],
    },
    "rich-terminal": {
        "tags": ["python rich", "rich terminal library", "terminal formatting python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Terminal_emulator",
            "ANSI_escape_code",
            "Text-based_user_interface",
            "Computer_terminal",
            "Escape_sequence",
        ) + [
            "https://rich.readthedocs.io/en/stable/introduction.html",
            "https://rich.readthedocs.io/en/stable/markup.html",
        ],
    },
    "tqdm-progress": {
        "tags": ["python tqdm", "tqdm progress bar", "progress meter python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Progress_bar",
            "Terminal_emulator",
            "Command-line_interface",
            "Loop_(computing)",
            "Iterator",
        ) + [
            "https://tqdm.github.io/",
        ],
    },
    "pillow-imaging": {
        "tags": ["python pillow", "pillow imaging library", "pil image processing"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Digital_image_processing",
            "Raster_graphics",
            "Image_file_format",
            "Alpha_compositing",
            "Portable_Network_Graphics",
            "Color_space",
        ) + [
            "https://pillow.readthedocs.io/en/stable/handbook/tutorial.html",
        ],
    },
    "beautifulsoup-parsing": {
        "tags": ["python beautifulsoup", "beautiful soup html", "html parsing python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Beautiful_Soup_(HTML_parser)",
            "HTML",
            "Document_Object_Model",
            "Web_scraping",
            "CSS_selector",
        ) + [
            "https://www.crummy.com/software/BeautifulSoup/bs4/doc/",
        ],
    },
    "lxml-xml": {
        "tags": ["python lxml", "lxml xml parsing", "xpath python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "XML",
            "XPath",
            "XSLT",
            "Parsing",
            "XML_namespace",
            "Document_type_definition",
        ) + [
            "https://lxml.de/tutorial.html",
        ],
    },
    "scrapy-crawler": {
        "tags": ["python scrapy", "scrapy crawler", "web crawling framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Scrapy",
            "Web_crawler",
            "Web_scraping",
            "Data_scraping",
        ) + [
            "https://docs.scrapy.org/en/latest/intro/tutorial.html",
            "https://docs.scrapy.org/en/latest/topics/spiders.html",
        ],
    },
    "selenium-python": {
        "tags": ["python selenium", "selenium webdriver", "browser automation python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Selenium_(software)",
            "Test_automation",
            "WebDriver",
            "Headless_browser",
        ) + [
            "https://selenium-python.readthedocs.io/getting-started.html",
            "https://selenium-python.readthedocs.io/locating-elements.html",
        ],
    },
    "playwright-python": {
        "tags": ["python playwright", "playwright automation", "headless browser python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Headless_browser",
            "Test_automation",
            "WebDriver",
            "Web_browser",
            "JavaScript",
        ) + [
            "https://playwright.dev/python/docs/intro",
            "https://playwright.dev/python/docs/locators",
        ],
    },
    "celery-tasks": {
        "tags": ["python celery", "celery task queue", "distributed task python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Celery_(software)",
            "Task_queue",
            "Message_queue",
            "Distributed_computing",
        ) + [
            "https://docs.celeryq.dev/en/stable/getting-started/introduction.html",
            "https://docs.celeryq.dev/en/stable/userguide/tasks.html",
        ],
    },
    "rq-queue": {
        "tags": ["python rq", "redis queue library", "rq task worker"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Message_queue",
            "Redis",
            "Task_queue",
            "In-memory_database",
        ) + [
            "https://python-rq.org/",
            "https://python-rq.org/docs/",
            "https://python-rq.org/patterns/",
        ],
    },
    "dramatiq": {
        "tags": ["python dramatiq", "dramatiq task queue", "background task python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Message_queue",
            "RabbitMQ",
            "Advanced_Message_Queuing_Protocol",
            "Task_queue",
            "Producer%E2%80%93consumer_problem",
        ) + [
            "https://dramatiq.io/guide.html",
            "https://dramatiq.io/motivation.html",
        ],
    },
    "apscheduler": {
        "tags": ["python apscheduler", "advanced python scheduler", "cron job python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Scheduling_(computing)",
            "Cron",
            "Automation",
            "Job_scheduler",
            "Time_zone",
        ) + [
            "https://apscheduler.readthedocs.io/en/3.x/userguide.html",
        ],
    },
    "sqlalchemy-core": {
        "tags": ["python sqlalchemy", "sqlalchemy orm", "database toolkit python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "SQLAlchemy",
            "Object%E2%80%93relational_mapping",
            "SQL",
            "Relational_database",
            "Database_transaction",
        ) + [
            "https://docs.sqlalchemy.org/en/20/tutorial/index.html",
            "https://docs.sqlalchemy.org/en/20/orm/quickstart.html",
        ],
    },
    "alembic-migrations": {
        "tags": ["python alembic", "alembic migrations", "schema migration python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Schema_migration",
            "Database_schema",
            "Relational_database",
            "Data_definition_language",
            "Version_control",
        ) + [
            "https://alembic.sqlalchemy.org/en/latest/tutorial.html",
            "https://alembic.sqlalchemy.org/en/latest/autogenerate.html",
        ],
    },
    "peewee-orm": {
        "tags": ["python peewee", "peewee orm", "lightweight orm python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object%E2%80%93relational_mapping",
            "Active_record_pattern",
            "Foreign_key",
            "Database_index",
            "Query_language",
        ) + [
            "https://docs.peewee-orm.com/en/latest/peewee/quickstart.html",
            "https://docs.peewee-orm.com/en/latest/peewee/models.html",
        ],
    },
    "tortoise-orm": {
        "tags": ["python tortoise orm", "async orm python", "tortoise models"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Object%E2%80%93relational_mapping",
            "Asynchronous_I/O",
            "Data_model",
            "Data_mapper_pattern",
            "Relational_database",
        ) + [
            "https://tortoise.github.io/getting_started.html",
            "https://tortoise.github.io/models.html",
        ],
    },
    "marshmallow-serialize": {
        "tags": ["python marshmallow", "marshmallow serialization", "object schema python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Serialization",
            "Deserialization",
            "Data_validation",
            "Marshalling_(computer_science)",
            "JSON",
        ) + [
            "https://marshmallow.readthedocs.io/en/stable/quickstart.html",
            "https://marshmallow.readthedocs.io/en/stable/nesting.html",
        ],
    },
    "attrs-classes": {
        "tags": ["python attrs", "attrs classes library", "boilerplate class python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Class_(computer_programming)",
            "Boilerplate_code",
            "Immutable_object",
            "Object-oriented_programming",
            "Field_(computer_science)",
        ) + [
            "https://www.attrs.org/en/stable/examples.html",
            "https://www.attrs.org/en/stable/why.html",
        ],
    },
    "dataclasses-json": {
        "tags": ["python dataclasses", "dataclass json serialization", "data transfer object python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Data_transfer_object",
            "JSON",
            "Serialization",
            "Metaprogramming",
            "Record_(computer_science)",
            "Data_structure",
        ) + [
            "https://docs.python.org/3/library/dataclasses.html",
        ],
    },
    "pandas-dataframe": {
        "tags": ["python pandas", "pandas dataframe", "data analysis python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Pandas_(software)",
            "Data_model",
            "Comma-separated_values",
            "Table_(information)",
            "Pivot_table",
            "Missing_data",
        ) + [
            "https://pandas.pydata.org/docs/user_guide/10min.html",
            "https://pandas.pydata.org/docs/user_guide/merging.html",
        ],
    },
    "numpy-arrays": {
        "tags": ["python numpy", "numpy arrays", "numerical computing python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "NumPy",
            "Array_(data_structure)",
            "Array_programming",
            "Numerical_analysis",
            "Matrix_(mathematics)",
            "Row-_and_column-major_order",
        ) + [
            "https://numpy.org/doc/stable/user/absolute_beginners.html",
            "https://numpy.org/doc/stable/user/basics.broadcasting.html",
        ],
    },
    "matplotlib-plotting": {
        "tags": ["python matplotlib", "matplotlib plotting", "pyplot charts python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Matplotlib",
            "Plot_(graphics)",
            "Data_visualization",
            "Line_chart",
            "Scatter_plot",
        ) + [
            "https://matplotlib.org/stable/tutorials/pyplot.html",
            "https://matplotlib.org/stable/users/explain/quick_start.html",
        ],
    },
    "seaborn-viz": {
        "tags": ["python seaborn", "seaborn visualization", "statistical plots python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Statistical_graphics",
            "Data_visualization",
            "Ggplot2",
            "Histogram",
            "Box_plot",
            "Heat_map",
        ) + [
            "https://seaborn.pydata.org/tutorial/introduction.html",
            "https://seaborn.pydata.org/tutorial/relational.html",
        ],
    },
    "plotly-python": {
        "tags": ["python plotly", "plotly express", "interactive charts python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Plotly",
            "Interactive_visualization",
            "Data_visualization",
            "Bar_chart",
            "JavaScript",
        ) + [
            "https://plotly.com/python/plotly-express/",
        ],
    },
    "bokeh-viz": {
        "tags": ["python bokeh", "bokeh visualization", "interactive plots python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Bokeh",
            "Interactive_visualization",
            "Data_visualization",
            "Dashboard_(computing)",
            "Web_browser",
        ) + [
            "https://docs.bokeh.org/en/latest/docs/first_steps.html",
        ],
    },
    "altair-viz": {
        "tags": ["python altair", "altair declarative viz", "vega grammar python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Declarative_programming",
            "Data_visualization",
            "Statistical_graphics",
            "Scalable_Vector_Graphics",
            "JavaScript",
        ) + [
            "https://altair-viz.github.io/getting_started/overview.html",
        ],
    },
    "openpyxl-excel": {
        "tags": ["python openpyxl", "openpyxl excel", "xlsx spreadsheet python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Office_Open_XML",
            "Spreadsheet",
            "File_format",
            "Comma-separated_values",
        ) + [
            "https://openpyxl.readthedocs.io/en/stable/tutorial.html",
            "https://openpyxl.readthedocs.io/en/stable/charts/introduction.html",
        ],
    },
    "pyarrow-python": {
        "tags": ["python pyarrow", "apache arrow python", "columnar data python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Apache_Arrow",
            "Column-oriented_DBMS",
            "Data_model",
            "Apache_Parquet",
        ) + [
            "https://arrow.apache.org/docs/python/getstarted.html",
            "https://arrow.apache.org/docs/python/data.html",
            "https://arrow.apache.org/docs/python/csv.html",
        ],
    },
    "dask-parallel": {
        "tags": ["python dask", "dask parallel computing", "parallel dataframe python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Dask_(software)",
            "Parallel_computing",
            "Distributed_computing",
            "MapReduce",
        ) + [
            "https://docs.dask.org/en/stable/dataframe.html",
            "https://docs.dask.org/en/stable/array.html",
            "https://docs.dask.org/en/stable/best-practices.html",
        ],
    },
    "joblib-parallel": {
        "tags": ["python joblib", "joblib parallel", "task parallelism python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Parallel_computing",
            "Thread_(computing)",
            "Multiprocessing",
            "Thread_pool",
        ) + [
            "https://joblib.readthedocs.io/en/stable/parallel.html",
            "https://joblib.readthedocs.io/en/stable/memory.html",
        ],
    },
    "multiprocessing-python": {
        "tags": ["python multiprocessing", "process pool python", "global interpreter lock"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Global_interpreter_lock",
            "Process_(computing)",
            "Producer%E2%80%93consumer_problem",
            "Inter-process_communication",
        ) + [
            "https://docs.python.org/3/library/multiprocessing.html",
            "https://docs.python.org/3/library/concurrent.futures.html",
        ],
    },
    "asyncio-python": {
        "tags": ["python asyncio", "asyncio event loop", "async await python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Async/await",
            "Coroutine",
            "Event_loop",
            "Callback_(computer_programming)",
            "Futures_and_promises",
        ) + [
            "https://docs.python.org/3/library/asyncio.html",
        ],
    },
    "trio-async": {
        "tags": ["python trio", "trio structured concurrency", "async nursery python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Concurrent_computing",
            "Coroutine",
            "Futures_and_promises",
            "Synchronization_(computer_science)",
            "Deadlock_(computer_science)",
        ) + [
            "https://trio.readthedocs.io/en/stable/tutorial.html",
            "https://trio.readthedocs.io/en/stable/reference-core.html",
        ],
    },
    "uvloop": {
        "tags": ["python uvloop", "uvloop event loop", "fast asyncio loop"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Event_loop",
            "Asynchronous_I/O",
            "Non-blocking_algorithm",
            "Reactive_programming",
        ) + [
            "https://uvloop.readthedocs.io/",
            "https://uvloop.readthedocs.io/user/index.html",
        ],
    },
    "gunicorn-wsgi": {
        "tags": ["python gunicorn", "gunicorn wsgi server", "wsgi worker python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Gunicorn",
            "Web_Server_Gateway_Interface",
            "Server_(computing)",
            "Fork%E2%80%93exec",
            "Load_balancing_(computing)",
            "Reverse_proxy",
            "Web_server",
        ),
    },
    "uvicorn-asgi": {
        "tags": ["python uvicorn", "uvicorn asgi server", "asgi worker python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Uvicorn",
            "Asynchronous_Server_Gateway_Interface",
            "Event_loop",
            "Web_server",
            "Reverse_proxy",
        ) + [
            "https://asgi.readthedocs.io/en/latest/introduction.html",
            "https://asgi.readthedocs.io/en/latest/specs/main.html",
        ],
    },
    "starlette-framework": {
        "tags": ["python starlette", "starlette asgi framework", "async web framework python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Asynchronous_Server_Gateway_Interface",
            "Representational_state_transfer",
            "WebSocket",
            "Web_framework",
            "Middleware",
        ) + [
            "https://www.starlette.io/requests/",
            "https://www.starlette.io/applications/",
            "https://www.starlette.io/routing/",
        ],
    },
    "jinja2-templating": {
        "tags": ["python jinja2", "jinja2 template engine", "template rendering python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Jinja_(template_engine)",
            "Template_processor",
            "HTML",
            "Cross-site_scripting",
            "Template_(word_processing)",
        ) + [
            "https://jinja.palletsprojects.com/en/stable/templates/",
            "https://jinja.palletsprojects.com/en/stable/api/",
        ],
    },
    "pyyaml-parsing": {
        "tags": ["python pyyaml", "pyyaml parsing", "yaml config python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "YAML",
            "Serialization",
            "File_format",
            "Configuration_file",
            "Data_structure",
        ) + [
            "https://pyyaml.org/wiki/PyYAMLDocumentation",
        ],
    },
    "python-dotenv": {
        "tags": ["python dotenv", "dotenv env file", "environment variable python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Environment_variable",
            "Configuration_management",
            "Configuration_file",
            "Metadata",
        ) + [
            "https://saurabh-kumar.com/python-dotenv/",
            "https://saurabh-kumar.com/python-dotenv/reference/",
        ],
    },
    "loguru-logging": {
        "tags": ["python loguru", "loguru logging library", "structured logging python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Logging_(computing)",
            "Log_file",
            "Syslog",
            "Observability_(software)",
        ) + [
            "https://loguru.readthedocs.io/en/stable/overview.html",
            "https://loguru.readthedocs.io/en/stable/api/logger.html",
        ],
    },
    "structlog": {
        "tags": ["python structlog", "structlog structured logging", "json logging python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Logging_(computing)",
            "JSON",
            "Log_file",
            "Observability_(software)",
        ) + [
            "https://www.structlog.org/en/stable/getting-started.html",
            "https://www.structlog.org/en/stable/why.html",
        ],
    },
    "cryptography-pyca": {
        "tags": ["python cryptography", "pyca cryptography library", "encryption python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Cryptography",
            "Symmetric-key_algorithm",
            "Public-key_cryptography",
            "Block_cipher",
        ) + [
            "https://cryptography.io/en/latest/fernet/",
            "https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/",
            "https://cryptography.io/en/latest/x509/",
        ],
    },
    "paramiko-ssh": {
        "tags": ["python paramiko", "paramiko ssh client", "sftp python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Secure_Shell",
            "OpenSSH",
            "Public-key_cryptography",
            "SSH_File_Transfer_Protocol",
        ) + [
            "https://docs.paramiko.org/en/latest/api/client.html",
            "https://docs.paramiko.org/en/latest/api/sftp.html",
        ],
    },
    "fabric-deploy": {
        "tags": ["python fabric", "fabric deployment tool", "remote execution python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Secure_Shell",
            "Software_deployment",
            "Automation",
            "Configuration_management",
            "Provisioning_(technology)",
            "Infrastructure_as_code",
        ) + [
            "https://www.fabfile.org/",
            "https://www.fabfile.org/installing.html",
        ],
    },
    "boto3-aws": {
        "tags": ["python boto3", "boto3 aws sdk", "aws python client"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Amazon_Web_Services",
            "Amazon_S3",
            "Cloud_computing",
            "Object_storage",
            "Software_development_kit",
            "Amazon_Elastic_Compute_Cloud",
        ) + [
            "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html",
            "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html",
        ],
    },
    "pytest-fixtures-lib": {
        "tags": ["python pytest fixtures", "pytest fixture setup", "test fixture python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Test_fixture",
            "Software_testing",
            "Unit_testing",
            "Dependency_injection",
            "Test_double",
        ) + [
            "https://docs.pytest.org/en/stable/how-to/fixtures.html",
        ],
    },
    "hypothesis-property": {
        "tags": ["python hypothesis", "hypothesis property testing", "property based testing python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Property_testing",
            "QuickCheck",
            "Fuzzing",
            "Software_testing",
            "Edge_case",
        ) + [
            "https://hypothesis.readthedocs.io/en/latest/quickstart.html",
            "https://hypothesis.readthedocs.io/en/latest/data.html",
        ],
    },
    "faker-data": {
        "tags": ["python faker", "faker fake data", "synthetic test data python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Test_data",
            "Synthetic_data",
            "Pseudorandomness",
            "Data_anonymization",
            "Personal_data",
        ) + [
            "https://faker.readthedocs.io/en/master/index.html",
            "https://faker.readthedocs.io/en/master/providers.html",
        ],
    },
    "factory-boy": {
        "tags": ["python factory boy", "factory boy fixtures", "test object factory python"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Factory_method_pattern",
            "Builder_pattern",
            "Test_fixture",
            "Object-relational_mapping",
            "Regression_testing",
        ) + [
            "https://factoryboy.readthedocs.io/en/stable/introduction.html",
            "https://factoryboy.readthedocs.io/en/stable/orms.html",
        ],
    },
}
