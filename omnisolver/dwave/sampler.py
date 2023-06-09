import dimod
from dwave.system.samplers import DWaveSampler as _DWaveSampler
from dwave.system import AutoEmbeddingComposite

class DWaveSampler(dimod.Sampler):
    """D-Wave annealer sampler."""

    def __init__(self, sampler):
        self.sampler = sampler
        self.embedded_sampler = AutoEmbeddingComposite(self.sampler)

    def sample(
        self,
        bqm,
        **parameters,
    ):
        """Sample `bqm` using the D-Wave anneler with autmoatic embedding.
        :returns: sample set solution found.
        """
        samples = self.embedded_sampler.sample(bqm, **parameters)

        return samples

    @property
    def parameters(self):
        return self.embedded_sampler.parameters

    @property
    def properties(self):
        return self.embedded_sampler.properties

def create_sampler(name: str) -> DWaveSampler:
    return DWaveSampler(_DWaveSampler(solver=name))