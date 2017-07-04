import unittest
from unittest.mock import Mock

from glowingoctofiesta import Broker

class BrokerTest(unittest.TestCase):
	def test_when_update_is_called_it_is_forwarded(self):
		mock = Mock()
		broker = Broker([mock.update])
		result = broker.update(3)
		mock.update.assert_called_with(3)

	def test_when_update_is_called_it_is_forwarded_to_all(self):
		mock = Mock()
		mock2 = Mock()
		broker = Broker([mock.update, mock2.update])
		result = broker.update(4)
		mock.update.assert_called_with(4)
		mock2.update.assert_called_with(4)
