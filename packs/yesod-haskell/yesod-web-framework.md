---
title: "Yesod (web framework)"
source: https://en.wikipedia.org/wiki/Yesod_(web_framework)
domain: yesod-haskell
license: CC-BY-SA-4.0
tags: yesod haskell framework, type safe haskell web, haskell web framework, yesod template haskell
fetched: 2026-07-02
---

# Yesod (web framework)

**Yesod** (Hebrew pronunciation: [jeˈsod]; Hebrew: יְסוֺד, "Foundation") is a web framework based on the programming language Haskell for productive development of type-safe, representational state transfer (REST) model based (where uniform resource locators (URLs) identify resources, and Hypertext Transfer Protocol (HTTP) methods identify transitions), high performance web applications, developed by Michael Snoyman, et al. It is free and open-source software released under an MIT License.

Yesod is based on templates, to generate instances for listed entities, and dynamic content process functions, through Template Haskell constructs to host domain-specific language (eDSL) content templates called QuasiQuotes, where the content is translated into code expressions by metaprogramming instructions.

There are also web-like language snippet templates that admit code expression interpolations, making them fully type-checked at compile time.

Yesod divides its functions in separate libraries (database, html rendering, forms, etc.) so functions may used as needed.

## MVC architecture

Yesod uses the model–view–controller (MVC) software design pattern for its user interfaces.

### Controller

#### Server interface

Yesod uses a *Web application interface* (WAI), a type of *application programming interface* (API), to isolate servlets, aka web apps., from servers, with handlers for the server protocols Common Gateway Interface (CGI), FastCGI, Simple Common Gateway Interface (SCGI), Warp, *Launch* (open as local *URL* to the default browser, closing the server when the window is closed),

#### The *foundation* type

See ref. Yesod requires a data type that instantiates the model–view–controller classes. This is called the *foundation* type. In the example below, it is named "MyApp".

The REST model identifies a web resource with a web path. Here, REST resources are given names with an R suffix (like "HomeR") and are listed in a *parseRoutes* site map description template. From this list, route names and dispatch handler names are derived.

Yesod makes use of Template Haskell metaprogramming to generate code from templates at compile time, assuring that the names in the templates match and everything typechecks (e.g. web resource names and handler names).

By inserting a *mkYesod* call, this will call Template Haskell primitives to generate the code corresponding to the route type members, and the instances of the dispatch controller classes as to dispatch *GET* calls to route *HomeR* to a routine named composing them both as "getHomeR", expecting an existing handler that matches the name.

#### Hello World

"Hello, World!" program example based on a Common Gateway Interface (CGI) server interface (the handler types have changed, but the philosophy remains):

```mw
{- file wai-cgi-hello.hs -}
{-# LANGUAGE PackageImports, TypeFamilies, QuasiQuotes, MultiParamTypeClasses,
             TemplateHaskell, OverloadedStrings #-}
import "wai" Network.Wai
import "wai-extra" Network.Wai.Handler.CGI (run) -- interchangeable WAI handler

import "yesod" Yesod
import "yesod-core" Yesod.Handler (getRequest)
import "text" Data.Text (Text)
import "shakespeare" Text.Cassius (Color(..), colorBlack)

-- the Foundation type
data MyApp = MyApp

-- sitemap template, listing path, resource name and methods accepted
-- `mkYesod` takes the foundation type name as param. for name composition of dispatch functions
mkYesod "MyApp" [parseRoutes|
/ HomeR GET
|]

instance Yesod MyApp

-- indentation structured CSS template
myStyle :: [Text] → CssUrl url
myStyle paramStyle =
        [cassius|
.box
    border: 1px solid #{boxColor}
|]
        where
          boxColor = case paramStyle of
                        ["high-contrast"] → colorBlack
                        _ → Color 0 0 255

-- indentation structured HTML template
myHtml :: [(Text, Text)] → HtmlUrl url
myHtml params = [hamlet|
```

```mw
<!-- indentation, or lack of it, under starting tags or commands ('$' prefix) 
     describe the content or sequence tree structure -->
<!-- '.' or '#' prefixes in tags introduce css styled "class" or "id" attribute values -->
<!-- interpolation of haskell expressions follow the "shakespeare templates" #{expr} syntax -->

<p>Hello World! There are <span .box>#{length params} parameters</span>:
$if null params
    <p>Nothing to list 
$else
    <ul>
         $forall param <- params
             <li>#{fst param}: #{snd param}
|]
```

```mw
getHomeR :: Handler RepHtml
getHomeR = do
        req <- getRequest
        let params = reqGetParams req
        paramStyle <- lookupGetParams "style"
        
        defaultLayout $ do
            -- adding widgets to the Widget monad (a ''Writer'' monad)
            setTitle "Yesod example"
            toWidgetHead $ myStyle paramStyle
            toWidgetBody $ myHtml params

-- there are ''run'' function variants for different WAI handlers

main = toWaiApp MyApp >>= run
```

```mw
# cgi test
export REMOTE_ADDR=127.0.0.1
export REQUEST_METHOD=GET
export PATH_INFO=/
export QUERY_STRING='p1=abc;p2=def;style=high-contrast'
./wai-cgi-hello
```

#### Resources, routes, HTTP method handlers

See ref. Yesod follows the representational state transfer model of access to web documents, identifying docs. and directories as resources with a Route constructor, named with an uppercase R suffix (for example, HomeR).

**The routes table**

The parseRoutes template should list the resources specifying route pieces, resource name and dispatch methods to be accepted.

URL segment capture as parameter is possible specifying a '#' prefix for single segment capture or '*' for multisegment capture, followed by the parameter type.

```mw
-- given a MyApp foundation type

mkYesod "MyApp" [parseRoutes|
/                     HomeR      -- no http methods stated: all methods accepted
/blog                 BlogR      GET POST

-- the '#' prefix specify the path segment as a route handler parameter
/article/#ArticleId   ArticleR   GET PUT

-- the '*' prefix specify the parameter as a sequence of path pieces
/branch/*Texts        BranchR    GET

-- to simplify the grammar, compound types must use an alias, eg. type Texts for ''[Text]''
|]
```

- Applying the previous template generates the following route constructors:

```mw
data Route MyApp = 
    HomeR                    -- referenced in templates as: @{HomeR}
    | BlogR                  -- in templates: @{BlogR}
    | ArticleR ArticleId     -- in templates: @{ArticleR myArticleId}
    | BranchR Texts          -- in templates: @{BranchR myBranchSegments}
```

- For every supported HTTP method a handler function must be created to match the dispatch names generated by *mkYesod* from the *parseRoutes* template, by prefixing the method name (or the prefix "handler" if no method stated) to the resource, as described (actual versions handler types have changed, but the philosophy remains):

```mw
-- for "/ HomeR"        -- no http methods stated ⇒ only one handler with prefix ''handler''
handlerHomeR :: HasReps t ⇒ Handler t

-- for "/blog BlogR GET POST"
getBlogR :: HasReps t ⇒ Handler t
postBlogR :: HasReps t ⇒ Handler t

-- for "/article/#ArticleId ArticleR GET PUT"
getArticleR :: HasReps t ⇒ ArticleId → Handler t
putArticleR :: HasReps t ⇒ ArticleId → Handler t
```

#### Request data, parameters, cookies, languages, other header info

See ref.

#### Authentication, authorization

See ref. Authentication plugins: OpenID, BrowserID, Email, GoogleEmail, HashDB, RpxNow.

There is an important setting for automatic redirection after authentication.

#### Sessions

See ref. Session back-ends: ClientSession (it stores the session in a cookie), ServerSession (it stores most of the session data at the server)

>

>

To avoid undue bandwidth overhead, production sites can serve their static content from a separate domain name to avoid the overhead of transmitting the session cookie for each request

##### Session messages

A success, failure or indicative message can be stored (*setMessage*) in the Session and will be shown, if it exists, by the *default_layout* routine through the `default_layout.hamlet` template, being cleared on consultation.

#### Subsites

Common URL prefix subsites for workflows, file serving or site partitioning. See ref.

Built-in subsites: Static, Auth

#### Form processing, layout generation

See ref.

The *Form* type here is an object that is used in the *controller* to parse and process the form fields user input and produce a (FormResult, Widget) pair were the widget holds the layout of the next rendering of the form with error messages and marks. It can also be used to generate a new form with blanks or default values.

The form type takes the shape of a function of an html snippet to be embedded in the view, that will hold security purpose hidden fields.

A form object is generated from an Applicative – Monadic composition of fields for a combined, sequential parsing of field inputs.

There are three types of forms:

- Applicative (with tabular layout),
- Monadic (with free layout style), both in the Yesod.Form.Functions module,
- Input (for parsing only, no view generated) in the Yesod.Form.Input module.

The field generators, whose names are composed by the form type initial `(a|m|i)` *followed by* `(req|opt){- required or optional -}`, have a fieldParse component and a fieldView one.

- the function `runForm{Post|Get}` runs the field parsers against the form field inputs and generates a (FormResult, Widget) pair from the views offering a new form widget with the received form field values as defaults. The function suffix is the http method used in the form submission.
- while `generateForm{Post|Get}` ignores inputs from the client and generates a blank or defaults form widget.

The actual function parameters and types have changed through Yesod versions. Check the Yesod book and libraries signatures.

The magic is in the FormResult data type Applicative instance, where (<*>) collects the error messages for the case of `FormFailure [textErrMsg]` result values

Monadic forms permit free form layout and better treatment of hiddenField members.

A sample of an *Applicative* form:

```mw
-- a record for our form fields
data Person = Person {personName :: Text, personAge :: Int, personLikings :: Maybe Text}

-- the Form type has an extra parameter for an html snippet to be embedded, containing a CSRF token hidden field for security
type Form sub master x = Html → MForm sub master (FormResult x, Widget)

{-
-- for messages in validation functions:
  @param master: yesod instance to use in renderMessage (return from handler's getYesod)
  @param languages: page languages to use in renderMessage

-- optional defaults record:
  @param mbPersonDefaults: Just defaults_record, or Nothing for blank form
-}

personForm :: MyFoundationType → [Text] → Maybe Person → Form sub master Person
{- ''aopt'' (optional field AForm component) for "Maybe" fields,
   ''areq'' (required fld AForm comp.) will insert the "required" attribute
-}
personForm master languages mbPersonDefaults = renderTable $ 
  Person <$> areq textField            fldSettingsName    mbNameDefault 
         <*> areq customPersonAgeField fldSettingsAge     mbAgeDefault 
         <*> aopt textareaField        fldSettingsLikings mbLikingsDefault 
  where
    mbNameDefault    = fmap personName    mbPersonDefaults
    mbAgeDefault     = fmap personAge     mbPersonDefaults
    mbLikingsDefault = fmap personLikings mbPersonDefaults

    -- "fieldSettingsLabel" returns an initial fieldSettings record
    -- recently the "FieldSettings" record can be defined from a String label since it implements IsString
    fldSettingsName = (fieldSettingsLabel MsgName) {fsAttrs = [("maxlength","20")]}
    fldSettingsAge = fieldSettingsLabel MsgAge
    fldSettingsLikings = (fieldSettingsLabel MsgLikings) {fsAttrs = [("cols","40"),("rows","10")]}

    customPersonAgeField = check validateAge intField

    validateAge y
        | y < 18    = Left $ renderMessage master languages MsgUnderAge
        | otherwise = Right y
```

### View

The types shown correspond to an older version, but the philosophy remains.

The Handler monad returns content in one or more of several formats as components of types that implement the HasReps class {RepHtml, RepJson, RepXml, RepPlain, the dual RepHtmlJson, a pair or list of pairs `[(ContentType, Content)]`, ..}. Json examples:

The HasReps default implementation of chooseRep chooses the document representation to be returned according to the preferred content-type list of the client accept header.

- Widgets are HTML DOM code snippets made by specific commands (e.g. setTitle) or from templates of structure (HTML) / behaviour (JavaScript) / style (CSS), whose types instantiate the classes ToWidget, ToWidgetHead or ToWidgetBody.

A Widget monad, based on a Writer one and argument to defaultLayout, facilitate to piece the widgets together.

#### Indentation based templates for tree structured markup

- the hamlet quasiquoter (a parser to compile-time Template Haskell code) specified in the T.H. Oxford brackets syntax `[qq| ... |]` introduces an indentation based structured html template. (See doc.).

'$' prefixes lines of logic statements.

Automatic closing tags are generated only for the tag at line start position.

- the whamlet quasiquoter returns a Widget expression. (saves to Widget before [hamlet|..|]).

```mw
toWidget [hamlet|
$doctype 5
<html>
    <!-- only the tag at the beginning of the line will be automatically closed -->
    <!-- '.' or '#' prefixes in tags introduce class/id names, à la CSS -->
    <!-- ":boolVar:" prefix in attributes makes them conditionally generated -->
    <!-- interpolation of haskell expressions follow the "shakespearean templates"
         syntax introduced in the so named section -->

    <head>
        <title>#{pageTitle} - My Site
        <link rel=stylesheet href=@{Stylesheet_route}>
    <body>
        <header>
           ^{headerTemplate}
        <section #mySectionId>
          <p><span .titleClass>_{MsgArticleListTitle}</span>
          $if null articles
            <p :isRed:style="color:red">_{MsgSorryNoArticles}
          $else
            <ul>
                $forall art <- articles
                    <li>#{articleNumber art} .- #{articleTitle art}
        <footer>
          ^{footerTemplate}
|]
```

##### Template interpolation - *Shakespearean templates*

See ref. These are content view templates that follow a common substitution pattern of code expressions within curly brackets with different character prefix to refer to

**template expressions with `^{...}`**

refers to other templates of the same type, with given parameters as

^{template params}

,

**route expressions with `@{...}`**

safe (typed) urls as

@{HomeR}

,

**message expressions with `_{...}`**

i18n

message rendering as

_{MsgMessageLabel params}

**other Haskell expressions with `#{...}`**

haskell expression rendering as

#{haskell_expression}

which type must be convertible

  - in case of *hamlet* html templates, the expression type must be an instance of Text.Blaze.ToMarkup
  - in case of CSS templates, the expression type must be an instance of Text.Cassius.ToCss
  - in case of JavaScript templates, the expression type must be an instance of Text.Julius.ToJavascript
  - in case of i18n message definitions (in "`<isoLanguage>`.msg" files) with parameter interpolations, the expression type must be an instance of Text.Shakespeare.I18N.ToMessage
  - in case of text/plain templates (for use in emails), the expression type must be an instance of Text.Shakespeare.Text.ToText

Using non-English text in expressions requires use of the Unicode-aware type Text, since the Glasgow Haskell Compiler's (GHC's) show for the type String renders non-ASCII characters as escaped numerical codes.

**External file templates**

- at compile time: Template content can be loaded from external files using compile time splice calls as *$(expr)*.
- at run time: There is a *reload mode* for reparsing external template files at every service call, except for HTML hamlet templates: See doc.

##### Other templates

**for JavaScript, CoffeeScript, Roy**

the

julius

quasiquoter: introduces a JavaScript template.

JavaScript variants

CoffeeScript

and Roy-language

have also specific

quasiquoters

.

**for CSS**

- the cassius quasiquoter: introduces a css template with indentation based structuring.
- the lucius quasiquoter: introduces a css template with standard syntax plus shakespeare-template style substitutions.

**TypeScript and JSX templates**

the

tsc

and

tscJSX

quasiquoters. Only on

UNIX

derivatives (no

Windows

by now).

**text/plain templates**

for

e-mail

or

text/plain

http

content type

.

1. templates: lt: lazy text, st: strict text
2. templates for text with a left margin delimiter '|': lbt (lazy), sbt (strict)

#### Localizable messages

See ref.

Yesod app messages are localizable (i18n). They should be held within the messages folder, in files named based on ISO, as *<iso-language>.msg*

Message entries follow the EBNF pattern:

```mw
-- EBNF: identifier, {' ', parameter, '@', type}, ":", text with interpolations
ArticleUnexistent param@Int64 : unexistent article #{param}
```

- message constructors are formed prepending "Msg" to the message label identifier.
- the message datatype is formed appending "Message" to the foundation type name.

```mw
-- in code
myMsg :: MyAppMessage  -- datatype appending "Message" to the foundation type
myMsg = MsgArticleUnexistent myArticleId  -- constructor prepending "Msg" to the msg. label

-- in widget templates
  _{MsgArticleUnexistent myArticleId}
```

Actual i18n support is missing from the stack app template. The `mkMessage "MyApp" messagesFolder isoLangDefault` must be added to the "Foundation.hs" file to get the messages instantiated.

- Navigation breadcrumbs. A YesodBreadcrumbs instance must be provided for the site where the generator function breadcrumb should return for each route a title and parent one. Then, the query function breadcrumbs will return the present route title and the ancestors' (route, title) pairs.

- Search engines XML Sitemaps, where sitemap returns an XML Sitemap as http response, with the routes we want the search engines to crawl, and attributes to instruct the crawler, from a provided list of SitemapUrl records.

#### Web feed views

- Web feed views (RDF Site Summary (RSS) – Atom). Handlers return RepRss, RepAtom, or dual RepAtomRss content (to be selected on accept headers' preferred content-type list) from a given Feed structure.

### Model

#### Using in-memory mutable data (in the foundation datatype)

E.g. a visitor count. See ref.

#### The Database layer

- *persistent* is the name of the database access layer with templates for generating types for entities and keys as well as schema initialization.

There is first class support for PostgreSQL, SQLite, MongoDB, CouchDB and MySQL, with experimental support for Redis.

The Database layout is described in a template listing the entities, fields and constraints.

- For every entity listed, an integer key column "id" is generated with autoincrement and primary index attributes, with a type alias appending Id to the entity name
- For every entity listed, a record type named as the entity is generated were record fields names are composed prefixing the entity name to the field name like "personName". An EntityField type "PersonName" is also generated for foreign key referencing from other entities.
- There is an automatic *database schema migration* mechanism for DB schema updates, which, to succeed, requires, when adding columns to existent tables, to specify *Default-column-value constraints* with *sql level notation*.
- "At most one" cardinality has a special mechanism around the type Checkmark.
- Weak entities (childs in life constrained owner-child relationships) have no special support for cascade delete *triggers*, but there are functions to *deleteCascade* manually in the Database.Persist.Class module.

**automatic table creation, schema update and table migration**

Modifications of the entities template produces an schema update with automatic table creation, and migration for the

DBMS

's that support "ALTER TABLE"

SQL

commands in a

migrateAll

procedure, generated from the template content. See "Migrations" in ref.

to look for migration aware

DBMS

.

```mw
share [mkPersist sqlSettings,
       mkMigrate "migrateAll"   -- generates the migration procedure with the specified name
       ] [persist|

User   -- table name and entity record type
    -- implicit autoincrement column "id" as primary key, typed UserId
    ident Text             -- refers to db. table column "ident"; 
                     -- generates a record field prefixing the table name as  "userIdent"
    password Text Maybe         -- Maybe indicates Nullable field
    UniqueUser ident            -- unique constraint with space sep. field sequence

Email  -- table name and entity record type
    -- implicit autoincrement column "id" as primary key, typed EmailId
    email Text
    user UserId                 -- foreign key by specifying other tables EntityField types
    verkey Text Maybe

    newlyAddedColumn Text "default='sometext'::character varying"  -- sql level Default constraint

    UniqueEmail email     -- unique constraint
|]
```

- Esqueleto: is a haskell combinators layer to generate correct relational queries to *persistent*.

Example for *persistent rawSQL* and *Esqueleto* queries.

### E-mail

The following packages are part of the *yesod-platform*:

- email-validate: Validating an email address.
- mime-mail: Compose and send MIME email messages.

### Facebook

- Useful glue functions between the fb library and Yesod.

## Development cycle

New Yesod apps are generated from the HaskellStack tool templates, replacing previous command "yesod init"

*Stack* based app. template names are prefixed by yesod as "yesod-{minimal | postgres | sqlite | mysql | mongo | ...}"

- Since HaskellStack uses the *stackage* repo by default, extra packages from the *hackage* repo should be referred in the "stack.yaml" *extra-deps* section.
- Packages may be customized to a local subfolder. They must be referred in the "stack.yaml" *packages* section.

### The "Yesod helper" tool

- The *yesod* helper tool
  - `yesod devel` run from the project site, recompiles and restarts the project at every file tree modification.
  - `yesod add-handler` adds a new handler and module to the project, adding an *import* clause for the handler in the "Application" module.

### Deploying with Keter: A web app server monitor and reverse proxy server

See refs.

Keter is a process as a service that handles deployment and restart of Yesod web app servers, and, per *web app*, database creation for PostgreSQL.

The console command `yesod keter` packs the web app. as a keter bundle for uploading to a keter folder named "incoming".

Keter monitors the "incoming" folder and unpacks the app. to a temporary one, then assigns the web app a port to listen to, and starts it.

Initially it worked with Nginx as reverse proxy (keter version 0.1*), adding virtual server entries to its configuration and making Nginx reload it, but now Keter itself provides its own *reverse proxy* functionality, removing Nginx dependency and acting as the main web server.

Old documentation (Nginx based).

## Integration with JavaScript generated from functional languages

See ref.
