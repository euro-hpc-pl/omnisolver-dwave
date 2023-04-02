import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system import AutoEmbeddingComposite

class DWaveSampler(dimod.Sampler):
    """D-Wave annealer sampler."""

    def sample(
        self,
        bqm,
        **parameters,
    ):
        """Sample `bqm` using the D-Wave anneler with autmoatic embedding.
        :returns: sample set solution found.
        """
        sampler = DWaveSampler()
        embedded_sampler = AutoEmbeddingComposite(sampler)
        samples = embedded_sampler.sample(bqm, **parameters)

        return samples

    @property
    def parameters(self):
        return {}

    @property
    def properties(self):
        return {}
