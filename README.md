# Hypergraph Resources

### Introduction
Below are links to hypergraph resource libraries for Python and MATLAB. To that end, the "Python x MATLAB Integration.pdf" contains an explanation for how to pass MATLAB variables to Python in order to generate hypergraph visualisations. The "xgi_test.py" file can be used to test passing an incidence matrix from MATLAB and generating a hypergraph visual and shortest path Python dictionary.

### Links to Code Resources
https://www.mathworks.com/matlabcentral/fileexchange/121013-hat-hypergraph-analysis-toolbox
MATLAB toolbox with a method for visualizing hypergraphs, creating incidence matrix, adjacency tensor, degree tensor, etc. There are a few analysis tools that have to do with similarity, correlation, centrality, etc. Found some issues with it when loading in a hypergraph with edge weights not equal to 1 and attempting to calculate average distance of nodes.

https://github.com/pnnl/HyperNetX
Python library with visualisation of hypergraphs. Contains some analysis tools such as centrality but I recommend its uses mainly for hypergraph plots.

https://xgi.readthedocs.io/en/stable/
Python library with visualisation of hypergraphs and some analysis. I recommend this package for visualisation. It also contains a shortest path algorithm, centralist, clustering.
