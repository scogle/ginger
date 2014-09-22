======
Ginger
======

Ginger is a utility for quickly generating data-driven static sites.


Usage
-----

To get started, just

```shell
$ cd some-project-directory
$ ginger new
```

This will create the barebones project template, which consists of:

* `_data` - where you store any local data files
* `_drafts` - where you keep any views you don't want in the final site
* `_includes` - where jinja2 partials live
* `_layouts` - where jinja2 site layouts live
* `_scss` - check out ginger's *super* minimal scss
* `_views` - this is where your view files will go
* `_css` - this is where the outputted css will go
* `js` - where scripts live
* `_config.yaml` - set site title, layout style, etc. here


Ginger includes several examples to give you a feel for how things work.
Edit these or nuke them and start from scratch.

**Note** - As a handy utility, we've included [Swag](https://github.com/elving/swag) by default.  Swag is a collection of super useful template helpers to use in constructing views.  Yeeeahhh!

For ginger to work properly, each view has to start with 'front matter'.  If you've used Jekyll you already know how it goes.  Basically, each view needs to start with a section like:

```
---
title: Top 20 Current NYTimes Best Sellers
id: best-sellers
description: The hardcover fiction list from the New York Times.
data_source: "/_data/nytimes_best_sellers.json"
---
```

All of the fields are **required**.

Once you've finished editing the view, run `ginger build` to generate your new site! Whoa! Or run `ginger serve` to build it and serve it locally! Even cooler!  If you're using local data sources (ie, files stored in the `_data` directory) you will probably need to use `ginger serve` to preven cross-site-origin-policy errors in your browser.


Installation
------------

To install Ginger, simply clone (or download the .zip) into a local directory
and run `python setup.py install`.  Voila!

About
-----

Ginger was inspired by [Github Jekyll](http://www.jekyllrb.com) and built by Scott Ogle and Nate Prewitt, using:

* Cliff
* Jinja2
* Handlebars
* Swag
* Bootstrap
* jQuery
* Lodash
* PyYAML
* and Bootstrap