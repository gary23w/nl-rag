---
title: "Installation"
source: https://squidfunk.github.io/mkdocs-material/getting-started/
domain: mkdocs
license: CC-BY-SA-4.0
tags: mkdocs static, documentation generator, markdown docs, static site
fetched: 2026-07-02
---

# Getting started

Material for MkDocs is a powerful documentation framework on top of MkDocs, a static site generator for project documentation.1 If you're familiar with Python, you can install Material for MkDocs with `pip`, the Python package manager. If not, we recommend using `docker`.

## Installation

### with pip recommended

Material for MkDocs is published as a Python package and can be installed with `pip`, ideally by using a virtual environment. Open up a terminal and install Material for MkDocs with:

```sh
pip install mkdocs-material
```

```sh
pip install mkdocs-material=="9.*" # (1)!
```

1. Material for MkDocs uses semantic versioning2, which is why it's a good idea to limit upgrades to the current major version. This will make sure that you don't accidentally upgrade to the next major version, which may include breaking changes that silently corrupt your site. Additionally, you can use `pip freeze` to create a lockfile, so builds are reproducible at all times: `pip freeze > requirements.txt` Now, the lockfile can be used for installation: `pip install -r requirements.txt`

This will automatically install compatible versions of all dependencies: MkDocs, Markdown, Pygments and Python Markdown Extensions. Material for MkDocs always strives to support the latest versions, so there's no need to install those packages separately.

**How to set up Material for MkDocs** by @james-willett – 27m – Learn how to create and host a documentation site using Material for MkDocs on GitHub Pages in a step-by-step guide.

Tip

If you don't have prior experience with Python, we recommend reading Using Python's pip to Manage Your Projects' Dependencies, which is a really good introduction on the mechanics of Python package management and helps you troubleshoot if you run into errors.

### with docker

The official Docker image is a great way to get up and running in a few minutes, as it comes with all dependencies pre-installed. Open up a terminal and pull the image with:

```
docker pull squidfunk/mkdocs-material
```

```
docker pull squidfunk/mkdocs-material:9
```

The `mkdocs` executable is provided as an entry point and `serve` is the default command. If you're not familiar with Docker don't worry, we have you covered in the following sections.

The following plugins are bundled with the Docker image:

- mkdocs-minify-plugin
- mkdocs-redirects

Warning

The Docker container is intended for local previewing purposes only and is not suitable for deployment. This is because the web server used by MkDocs for live previews is not designed for production use and may have security vulnerabilities.

How to add plugins to the Docker image?

Material for MkDocs only bundles selected plugins in order to keep the size of the official image small. If the plugin you want to use is not included, you can add them easily. Create a `Dockerfile` and extend the official image:

Dockerfile

```dockerfile
FROM squidfunk/mkdocs-material
RUN pip install mkdocs-macros-plugin
RUN pip install mkdocs-glightbox
```

Next, build the image with the following command:

```
docker build -t squidfunk/mkdocs-material .
```

The new image will have additional packages installed and can be used exactly like the official image.

### with git

Material for MkDocs can be directly used from GitHub by cloning the repository into a subfolder of your project root which might be useful if you want to use the very latest version:

```
git clone https://github.com/squidfunk/mkdocs-material.git
```

Next, install the theme and its dependencies with:

```
pip install -e mkdocs-material
```

1. In 2016, Material for MkDocs started out as a simple theme for MkDocs, but over the course of several years, it's now much more than that – with the many built-in plugins, settings, and countless customization abilities, Material for MkDocs is now one of the simplest and most powerful frameworks for creating documentation for your project. ↩
2. Note that improvements of existing features are sometimes released as patch releases, like for example improved rendering of content tabs, as they're not considered to be new features. ↩
