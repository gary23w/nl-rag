---
title: "Jsonnet"
source: https://jsonnet.org/
domain: jsonnet
license: Apache-2.0
tags: jsonnet language, data templating language, json config generation, google jsonnet
fetched: 2026-07-02
---

# Jsonnet

Jsonnet

|   | A configuration language for app and tool developers Generate config data Side-effect free Organize, simplify, unify Manage sprawling config |
|---|---|

| A simple extension of JSON Open source (Apache 2.0) Familiar syntax Reformatter, linter Editor & IDE integrations Formally specified |   |
|---|---|

Eliminate duplication with object-orientation:

// Edit me! { person1: { name: "Alice", welcome: "Hello " + self.name + "!", }, person2: self.person1 { name: "Bob" }, }

➡

output.json

{ "person1": { "name": "Alice", "welcome": "Hello Alice!" }, "person2": { "name": "Bob", "welcome": "Hello Bob!" } }

Or, use functions:

// A function that returns an object. local Person(name='Alice') = { name: name, welcome: 'Hello ' + name + '!', }; { person1: Person(), person2: Person('Bob'), }

➡

output.json

{ "person1": { "name": "Alice", "welcome": "Hello Alice!" }, "person2": { "name": "Bob", "welcome": "Hello Bob!" } }

Integrate with existing / custom applications. Generate JSON, YAML, INI, and other formats.

local application = 'my-app'; local module = 'uwsgi_module'; local dir = '/var/www'; local permission = 644; { 'uwsgi.ini': std.manifestIni({ sections: { uwsgi: { module: module, pythonpath: dir, socket: dir + '/uwsgi.sock', 'chmod-socket': permission, callable: application, logto: '/var/log/uwsgi/uwsgi.log', }, }, }), 'init.sh': ||| #!/usr/bin/env bash mkdir -p %(dir)s touch %(dir)s/initialized chmod %(perm)d %(dir)s/initialized ||| % {dir: dir, perm: permission}, 'cassandra.conf': std.manifestYamlDoc({ cluster_name: application, seed_provider: [ { class_name: 'SimpleSeedProvider', parameters: [{ seeds: '127.0.0.1' }], }, ], }), }

➡

cassandra.conf

init.sh

uwsgi.ini

"cluster_name": "my-app" "seed_provider": - "class_name": "SimpleSeedProvider" "parameters": - "seeds": "127.0.0.1"

#!/usr/bin/env bash mkdir -p /var/www touch /var/www/initialized chmod 644 /var/www/initialized

[uwsgi] callable = my-app chmod-socket = 644 logto = /var/log/uwsgi/uwsgi.log module = uwsgi_module pythonpath = /var/www socket = /var/www/uwsgi.sock

The name Jsonnet is a portmanteau of JSON and *sonnet*, pronounced "jay sonnet". It began life early 2014 as a 20% project and was launched on Aug 6. The design is influenced by several configuration languages internal to Google, and embodies years of experience configuring some of the world's most complex IT systems. Jsonnet is now used by many companies and projects. Jsonnet is not an official Google product (experimental or otherwise), it is just code that happens to be owned by Google.
