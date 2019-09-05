# Wikidata Migration


After extracting instrument information from scientific articles, we need to migrate that info to Wikidata for interoperability.


A few things were done : 

1 - Create a little model for the hierarchy of gas chromatography instruments based on eagle-i 
2 - Migrate manually via quickstatements (https://tools.wmflabs.org/quickstatements/#/batch) a couple equipments to wikidata 
3 - Write a  code that takes info from a table containing equipments and papers that cite them and migrate to wikidata


Big picture:

In the end, matches of papers and equipment coming from automatic matching or crowdsourcing could be migrated to Wikidata.

This allows queries answering questions like "which equipments are used by my university"?