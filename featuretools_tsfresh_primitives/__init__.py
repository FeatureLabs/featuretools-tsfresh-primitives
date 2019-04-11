# flake8: noqa
from .abs_energy import AbsEnergy
from .absolute_sum_of_changes import AbsoluteSumOfChanges
from .agg_autocorrelation import AggAutocorrelation
from .approximate_entropy import ApproximateEntropy
from .agg_linear_trend import AggLinearTrend
from .ar_coefficient import ArCoefficient
from .augmented_dickey_fuller import AugmentedDickeyFuller
from .autocorrelation import Autocorrelation
from .binned_entropy import BinnedEntropy
from .c3 import C3
from .cid_ce import CidCe
from .change_quantiles import ChangeQuantiles
from .count_below_mean import CountBelowMean
from .energy_ratio_by_chunks import EnergyRatioByChunks
from .spkt_welch_density import SpktWelchDensity
from .symmetry_looking import SymmetryLooking

primitives = {
    'AbsEnergy': AbsEnergy,
    'AbsoluteSumOfChanges': AbsoluteSumOfChanges,
    'AggAutocorrelation': AggAutocorrelation,
    'AggLinearTrend': AggLinearTrend,
    'ApproximateEntropy': ApproximateEntropy,
    'ArCoefficient': ArCoefficient,
    'AugmentedDickeyFuller': AugmentedDickeyFuller,
    'Autocorrelation': Autocorrelation,
    'BinnedEntropy': BinnedEntropy,
    'C3': C3,
    'CidCe': CidCe,
    'ChangeQuantiles': ChangeQuantiles,
    'CountBelowMean': CountBelowMean,
    'EnergyRatioByChunks': EnergyRatioByChunks,
    'SpktWelchDensity': SpktWelchDensity,
    'SymmetryLooking': SymmetryLooking,
}
