---
title: "RSpec documentation"
source: https://rspec.info/documentation/
domain: rspec
license: CC-BY-SA-4.0
tags: rspec ruby, ruby testing, behavior-driven development, spec framework
fetched: 2026-07-02
---

## Documentation

| Gem | RDoc | Examples (Relish / Gherkin) |
|---|---|---|
| rspec-core | 3.133.133.123.113.103.93.83.73.63.53.43.33.23.13.02.992.14 | 3.133.133.12 |
| rspec-expectations | 3.133.133.123.113.103.93.83.73.63.53.43.33.23.13.02.992.14 | 3.133.133.12 |
| rspec-mocks | 3.133.133.123.113.103.93.83.73.63.53.43.33.23.13.02.992.14 | 3.133.133.12 |
| rspec-rails | 8.08.07.17.06.16.05.04.14.03.93.83.73.63.53.43.33.23.13.02.992.14 | 8.08.07.17.06.16.0 |

RSpec is composed of multiple libraries, which are designed to work together, or can be used independently with other testing tools like Cucumber or Minitest. The parts of RSpec are:

- **rspec-core:**The spec runner, providing a rich command line program, flexible and customizable reporting, and an API to organize your code examples.
- **rspec-expectations:**Provides a readable API to express expected outcomes of a code example.
- **rspec-mocks:**Test double framework, providing multiple types of fake objects to allow you to tightly control the environment in which your specs run.
- **rspec-rails:**Supports using RSpec to test Ruby on Rails applications in place of Rails' built-in test framework.

The API documentation contains details about all public APIs supported by RSpec. We consider these the primary docs and will treat these APIs according to the policies of Semantic Versioning. We encourage you to use only public APIs as private APIs may change in any release without warning. If you have a use case not supported by the existing public APIs, please ask and we'll be glad to add an API for you or make an existing private API public.

## Gherkin Examples (e.g. RelishApp)

RSpec is also documented through executable examples written in Gherkin. The examples are written in an "end-to-end" style demonstrating the use of various RSpec features in the context of executable spec files. They are a good resource for getting a survey of what RSpec is capable of and seeing how the pieces can be used together, but for detailed documentation about a particular API or feature, we recommend the API docs.

These feature files are executed via Cucumber in our CI process to ensure they are always up-to-date with the current code base.

Previously our gherkin examples could be read on RelishApp but currently this service is unavailable. We thank Matt Wynne for his contribution hosting these over the years, and we now host these ourselves via the table above.
