from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Boolean, Numeric
from tsfresh.feature_extraction.feature_calculators import has_duplicate_max


class HasDuplicateMax(AggregationPrimitive):
    """Checks if the maximum value of x is observed more than once.

    Docstring source:
    https://tsfresh.readthedocs.io/en/latest/api/tsfresh.feature_extraction.html#tsfresh.feature_extraction.feature_calculators.has_duplicate_max
    """
    name = "has_duplicate_max"
    input_types = [Numeric]
    return_type = Boolean
    stack_on_self = False

    def get_function(self):
        return has_duplicate_max
