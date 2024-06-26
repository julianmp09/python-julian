from water_flow import water_column_height
from pytest import approx
import pytest

def test_water_column_height():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert water_column_height(0,0) == approx(0)
    assert water_column_height(0,10) == approx(7.5)
    assert water_column_height(25,0) == approx(25)
    assert water_column_height(48.3, 12.8) == approx(57.9)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])