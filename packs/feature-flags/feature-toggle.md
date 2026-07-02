---
title: "Feature toggle"
source: https://en.wikipedia.org/wiki/Feature_toggle
domain: feature-flags
license: CC-BY-SA-4.0
tags: feature flag, feature toggle, progressive delivery, runtime configuration
fetched: 2026-07-02
---

# Feature toggle

A **feature toggle** in software development provides an alternative to maintaining multiple feature branches in source code. A condition within the code enables or disables a feature during runtime. In agile settings the toggle is used in production, to switch on the feature on demand, for some or all the users. Thus, feature toggles do make it easier to release often. Advanced roll out strategies such as canary roll out and A/B testing are easier to handle.

Continuous delivery is supported by feature toggles, even if new releases are not deployed to production continuously. The feature is integrated into the main branch even before it is completed. The version is deployed into a test environment once, the toggle allows to turn the feature on, and test it. Software integration cycles get shorter, and a version ready to go to production can be provided.

The third use of the technique is to allow developers to release a version of a product that has unfinished features. These unfinished features are hidden (toggled) so that they do not appear in the user interface. There is less effort to merge features into and out of the productive branch, and hence allows many small incremental versions of software.

A feature toggle is also called **feature switch**, **feature flag**, **feature gate**, **feature flipper**, or **conditional feature**.

## Implementation

Feature toggles are essentially variables that are used inside conditional statements. Therefore, the blocks inside these conditional statements can be toggled 'on or off' depending on the value of the feature toggle. This allows developers to control the flow of their software and bypass features that are not ready for deployment. A block of code behind a runtime variable is usually still present and can be conditionally executed, sometimes within the same application lifecycle; a block of code behind a preprocessor directive or commented out would not be executable. A feature flag approach could use any of these methods to separate code paths in different phases of development.

The main usage of feature toggles is to avoid conflict that can arise when merging changes in software at the last moment before release, although this can lead to toggle debt. Toggle debt arises due to the dead code present in software after a feature has been toggled on permanently and produces overhead. This portion of the code has to be removed carefully as to not disturb other parts of the code.

### Management and maintenance

Feature toggles usually require lifecycle management beyond the conditional statements used to implement them. A study of practitioner material and developers from 38 companies identified 17 practices for feature-toggle use, grouped into management, initialization, implementation, and clean-up practices. Commonly reported practices included recording metadata for each toggle, defining a default value, logging changes made to toggles, and using dedicated tools to manage them.

Research on Google Chrome found that feature toggles can support rapid releases, trunk-based development, and A/B testing, but also require additional maintenance when toggles remain in the codebase for long periods. Later work on feature-toggle structure similarly noted that toggles may increase code complexity, introduce dead code, and reduce maintainability if they are not removed or organized after their purpose has ended.

There are two main types of feature toggle. One is a release toggle, which the developer determines to either keep or remove before a product release depending on its working. The other is a business toggle, which is kept because it satisfies a different usage compared to that of the older code.

Feature toggles can be used in the following scenarios:

- Adding a new feature to an application.
- Enhancing an existing feature in an application.
- Hiding or disabling a feature.
- Extending an interface.

Feature toggles can be stored as:

- Row entries in a database
- A property in a configuration file
- An entry in an external feature flag service.

### Feature groups

Feature groups consist of feature toggles that work together. This allows the developer to easily manage a set of related toggles.

## Canary release

A **canary release** (or canary launch or canary deployment) allows developers to have features incrementally tested by a small set of users. Feature flags are an alternate way to do canary launches and allow targeting by geographic locations or even user attributes. If a feature's performance is not satisfactory, then it can be rolled back without any adverse effects. It is named after the use of canaries to warn miners of toxic gases.

## Adoption

Martin Fowler states that a release toggle, a specific type of feature toggle, "should be your last choice when you're dealing with putting features into production". Instead, it is best to break the feature into smaller parts that each can be implemented and safely introduced into the released product without causing other problems.

Feature-toggling is used by many large websites including Flickr, Disqus, Etsy, Reddit, Gmail and Netflix, as well as software such as Google Chrome Canary or Microsoft Office.
