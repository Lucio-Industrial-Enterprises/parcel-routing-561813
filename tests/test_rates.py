import unittest

from warehouse.rates import shipping_quote


class StandardRateTests(unittest.TestCase):
    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        # Passing service="standard" explicitly must behave identically.
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")


class ExpressRateTests(unittest.TestCase):
    """Express quotes must equal the standard quote plus a $7 surcharge."""

    def test_express_local(self):
        # standard local 2 kg = $8.00; express = $15.00
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional 2 kg = $11.00; express = $18.00
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # standard local 1.5 kg = 5.0 + 1.5*1.5 = 7.25; express = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    def test_express_matches_standard_plus_surcharge(self):
        for zone in ("local", "regional"):
            with self.subTest(zone=zone):
                standard = shipping_quote(3, zone, service="standard")
                express = shipping_quote(3, zone, service="express")
                self.assertAlmostEqual(express - standard, 7.0)


class InvalidServiceTests(unittest.TestCase):
    def test_unknown_service_raises(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")

    def test_unknown_service_message(self):
        with self.assertRaises(ValueError, msg="overnight"):
            shipping_quote(1, "regional", service="overnight")
