import unittest
from unittest.mock import Mock

import json

from glowingoctofiesta import GocdBuildStatusTransformer

class GocdBuildStatusTransformerTest(unittest.TestCase):
	def test_transform(self):
		mock = Mock()
		transformer = GocdBuildStatusTransformer(mock.updateBuildStatus)

		with open('./test/pipelineFixture.json') as fixtureData:
			fixtureObj = json.loads(fixtureData.read())

		result = transformer.processBuildStatus(fixtureObj)
		mock.updateBuildStatus.assert_called_with(2)
