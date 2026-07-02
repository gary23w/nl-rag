---
title: "Sinatra (software)"
source: https://en.wikipedia.org/wiki/Sinatra_(software)
domain: sinatra
license: CC-BY-SA-4.0
tags: sinatra framework, ruby microframework, rack interface, ruby web dsl
fetched: 2026-07-02
---

# Sinatra (software)

**Sinatra** is a free and open source software web application library and domain-specific language written in Ruby. It is an alternative to other Ruby web application frameworks such as Ruby on Rails, Merb, Nitro, and Camping. It is dependent on the Rack web server interface. It is named after musician Frank Sinatra.

Designed and developed by Blake Mizerany, Sinatra is small and flexible. It does not follow the typical model–view–controller pattern used in other frameworks, such as Ruby on Rails. Instead, Sinatra focuses on "quickly creating web-applications in Ruby with minimal effort." Because of much smaller size compared to Ruby on Rails, it is also called *microframework*.

Some notable companies and institutions that use Sinatra include Apple, BBC, the British Government's Government Digital Service, LinkedIn, the National Security Agency, Engine Yard, Heroku, GitHub, Stripe, and Songbird. Travis CI provides much of the financial support for Sinatra's development.

Sinatra was created and open-sourced in 2007. It inspired multiple ports and similar projects in other programming languages, such as Express.js and Scalatra.

Mizerany and Heroku's Adam Wiggins introduced and discussed Sinatra at RubyConf 2008.

## Example

```mw
#!/usr/bin/env ruby
require 'sinatra'

get '/' do
  redirect to('/hello/World')
end

get '/hello/:name' do
  "Hello #{params[:name]}!"
end
```
