Episode Two And Three Present Codecasts
=======================================

Present Codecasts
-----------------

* given codecasts
    | title | published |
    |-------|-----------|
    | A     | 3/1/2014  |
    | B     | 3/2/2014  |
    | C     | 2/18/2014 |
* given user "U"
* with user "U" logged in
* and with license for "U" able to view "A"
* then the following codecasts will be presented for "U"
* ordered query of codecasts
    | title | publication_date | picture | description | viewable | downloadable |
    |-------|------------------|---------|-------------|----------|--------------|
    |  C    | 2/18/2014        | C       | C           | -        | -            |
    |  A    | 3/1/2014         | A       | A           | +        | -            |
    |  B    | 3/2/2014         | B       | B           | -        | -            |
