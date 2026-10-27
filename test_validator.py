# -*- coding: utf-8 -*-
import unittest
from vkn_validator.validator import validate_vkn, validate_tckn, validate_identity
from vkn_validator.generator import generate_valid_vkn, generate_valid_tckn
from vkn_validator.tax_offices import search_tax_office

class TestVKNTCKNValidator(unittest.TestCase):
    def test_vkn_generation_and_validation(self):
        for _ in range(10):
            vkn = generate_valid_vkn()
            self.assertEqual(len(vkn), 10)
            self.assertTrue(validate_vkn(vkn))

    def test_tckn_generation_and_validation(self):
        for _ in range(10):
            tckn = generate_valid_tckn()
            self.assertEqual(len(tckn), 11)
            self.assertNotEqual(tckn[0], "0")
            self.assertTrue(validate_tckn(tckn))

    def test_invalid_vkn(self):
        self.assertFalse(validate_vkn("1234567891"))
        self.assertFalse(validate_vkn("1111111111"))
        self.assertFalse(validate_vkn("123"))
        self.assertFalse(validate_vkn("abcdefghij"))

    def test_invalid_tckn(self):
        self.assertFalse(validate_tckn("01234567890"))  # Starts with 0
        self.assertFalse(validate_tckn("11111111111"))
        self.assertFalse(validate_tckn("12345678901"))

    def test_validate_identity_helper(self):
        vkn = generate_valid_vkn()
        res_vkn = validate_identity(vkn)
        self.assertTrue(res_vkn.is_valid)
        self.assertEqual(res_vkn.identity_type, "VKN")

        tckn = generate_valid_tckn()
        res_tckn = validate_identity(tckn)
        self.assertTrue(res_tckn.is_valid)
        self.assertEqual(res_tckn.identity_type, "TCKN")

    def test_tax_office_search(self):
        res = search_tax_office("Maslak")
        self.assertTrue(len(res) > 0)
        self.assertEqual(res[0]["code"], "034255")

if __name__ == "__main__":
    unittest.main()
