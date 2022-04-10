from unittest import TestCase

import pt_at_qr_code

class TestFieldRegistry(TestCase):
    def setUp(self):
      self.registry = pt_at_qr_code.field_registry.FieldRegistry() 

    def test_getters(self):
      reg = self.registry 
      field_a = reg.get_field('A')
      self.assertTrue(field_a is not None)
      self.assertEqual(field_a['h'], 'seller_vat_number')

    def test_invalid_field(self):
      reg = self.registry 
      self.assertRaises(Exception, reg.get_field, 'XXX')
