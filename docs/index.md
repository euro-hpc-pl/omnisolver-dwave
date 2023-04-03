# Welcome to omnisolver-dwave documentation!

The `omnisolver-dwave` is Omnisolver plugin implementing the sampling on the D-Wave annealer.

## Installation

Preferred method of installation is via pip:

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

## Documentation
```{toctree}
:maxdepth: 1
```