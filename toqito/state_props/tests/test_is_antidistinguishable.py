"""Test is_antidistinguishable."""
import numpy as np
import pytest

from toqito.states import bell, trine
from toqito.state_props import is_antidistinguishable


@pytest.mark.parametrize("states, expected_result", [
    # The Bell states are known to be antidistinguishable.
    ([bell(0), bell(1), bell(2), bell(3)], True),
    # The trine states are known to be antidistinguishable.
    ([trine()[0], trine()[1], trine()[2]], True),
])
def test_is_antidistinguishable(states, expected_result):
    np.testing.assert_equal(is_antidistinguishable(states), expected_result)
