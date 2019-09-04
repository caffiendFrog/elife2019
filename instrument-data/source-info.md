## Source
Instrument data as well as the list of instrument types has been provided by [eagle-i](https://www.eagle-i.net). This document notes the sparql queries that were executed to retrieve the data.

All queries are executed in the public sparql endpoint with the 'Published-Resources View'.
## Instruments only
[alaska-instruments](https://alaska.eagle-i.net/sparqler/query/)
[harvard-instruments](https://harvard.eagle-i.net/sparqler/query/)
```
select distinct ?name
  where {
    ?uri a <http://purl.obolibrary.org/obo/ERO_0000004> .
    ?uri rdfs:label ?name
  }
```
## Instrument to type
[alaska-instrument-type](https://alaska.eagle-i.net/sparqler/query/)
[harvard-instruments](https://harvard.eagle-i.net/sparqler/query/)
```
select ?name ?type_name
  where {
    ?uri a <http://purl.obolibrary.org/obo/ERO_0000004> .
    ?uri rdfs:label ?name . 
    ?uri a ?type .
    optional { ?type rdfs:label ?type_name } .

    # not root instrument type
    FILTER (!CONTAINS(str(?type), "ERO_0000004")) .

    # not thing type
    FILTER (!CONTAINS(str(?type), "owl#Thing")) .

    # not material entity BFO_0000040
    FILTER (!CONTAINS(str(?type), "BFO_0000040")) .

    # not independent continuant BFO_0000004
    FILTER (!CONTAINS(str(?type), "BFO_0000004")) .

    # not continuant BFO_0000002
    FILTER (!CONTAINS(str(?type), "BFO_0000002")) .

    # not entity BFO_0000001
    FILTER (!CONTAINS(str(?type), "BFO_0000001")) .

    # not processed material OBI_0000047
    FILTER (!CONTAINS(str(?type), "OBI_0000047")) .
  }
```
## Instrument types
Can be executed against either Harvard or Alaska.
```
select distinct ?name
where {
?uri rdfs:subClassOf <http://purl.obolibrary.org/obo/ERO_0000004> .
?uri rdfs:label ?name
}

```