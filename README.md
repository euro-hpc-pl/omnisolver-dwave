
![Logo](https://raw.githubusercontent.com/euro-hpc-pl/omnisolver/master/logo.png)
*D-Wave Plugin for [Omnisolver](https://github.com/euro-hpc-pl/omnisolver)*


## Installation 

To install the plugin run:

```shell
pip install omnisolver-dwave
```

## Configuration

Create a file `dwave.conf` in `~/.config/dwave` with the following minimal
contents
```ini
[defaults]
token = YOUR-TOKEN

[first-available-qpu]
solver = {"qpu": true}
```


## Command line usage

```text
usage: omnisolver dwave [-h] [--output OUTPUT] [--vartype {SPIN,BINARY}]
                     input

Parallel tempering sampler

positional arguments:
  input                 Path of the input BQM file in COO format. If not specified, stdin is used.

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT       Path of the output file. If not specified, stdout is used.
  --vartype {SPIN,BINARY}
                        Variable type
```

## Citing

If you used the Omnisolver package or one of its plugins, please cite:

```text
@misc{https://doi.org/10.48550/arxiv.2112.11131,
  doi = {10.48550/ARXIV.2112.11131},
  
  url = {https://arxiv.org/abs/2112.11131},
  
  author = {Jałowiecki, Konrad and Pawela, Łukasz},
  
  keywords = {Software Engineering (cs.SE), Quantum Physics (quant-ph), FOS: Computer and information sciences, FOS: Computer and information sciences, FOS: Physical sciences, FOS: Physical sciences},
  
  title = {Omnisolver: an extensible interface to Ising spin glass solvers},
  
  publisher = {arXiv},
  
  year = {2021},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```