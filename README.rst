=====================
 Running SPARQLginger
=====================

SPARQLginger is a utility to generate dynamic HTML sites from SPARQL queries.  Add some spice to your SPARQL!

Usage
-----

A typical workflow looks like:

* mkdir myGingerSite

* cd myGingerSite

* ginger new

This will generate the structure of your site -- a _config.yml file, a _templates folder and a _site folder where the built site will go.

To add/edit queries, open _config.yml and add a named query to the queries: section

To rebuild after changes, run 'ginger build'

'ginger serve' will serve the site on a simple HTTP server