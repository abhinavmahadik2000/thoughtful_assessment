def sort(width, height, length, mass):
    """
    Determine the dispatch stack for a package.

    Parameters:
    - width (cm):  package width
    - height (cm): package height
    - length (cm): package length
    - mass (kg):   package mass

    Returns:
    - "STANDARD" if neither bulky nor heavy
    - "SPECIAL"  if either bulky or heavy (but not both)
    - "REJECTED" if both bulky and heavy
    """

    # Check bulky: volume >= 1,000,000 OR any dimension >= 150 cm
    volume = width * height * length
    if volume >= 1_000_000:
        is_bulky = True
    else:
        is_bulky = False

    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True

    # Check heavy: mass >= 20 kg
    if mass >= 20:
        is_heavy = True
    else:
        is_heavy = False

    # Both heavy and bulky
    if is_heavy and is_bulky:
        return "REJECTED"
    # Either heavy or bulky
    if is_heavy or is_bulky:
        return "SPECIAL"
    # Neither
    return "STANDARD"


# --- Unit tests ---
import unittest

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        # small light package
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")
        # volume just below threshold
        self.assertEqual(sort(99, 10, 10, 19.9), "STANDARD")

    def test_bulky_only(self):
        # volume exactly at threshold
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")
        # one dimension at threshold
        self.assertEqual(sort(150, 10, 10, 1), "SPECIAL")
        # volume huge but light
        self.assertEqual(sort(500, 500, 5, 0.5), "SPECIAL")

    def test_heavy_only(self):
        # heavy but small
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        # mass just above threshold
        self.assertEqual(sort(1, 1, 1, 20.0), "SPECIAL")

    def test_rejected(self):
        # both heavy and bulky by volume
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        # both heavy and bulky by dimension
        self.assertEqual(sort(200, 1, 1, 25), "REJECTED")
        # both criteria met
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

    def test_edge_cases(self):
        # zero dimensions or mass
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        # negative values (treat them normally)
        self.assertEqual(sort(-1, -1, -1, -1), "STANDARD")

if __name__ == "__main__":
    unittest.main()
