import unittest

import json

from glowingoctofiesta import GocdBuildStatusTransformer

from glowingoctofiesta.buildStatuses import BuildStatuses
from glowingoctofiesta.buildStatuses import BuildStatus

class BuildStatusRecorder():
	def updateBuildStatuses(self, buildStatuses):
		self.buildStatuses = buildStatuses

class GocdBuildStatusTransformerTest(unittest.TestCase):
	def test_transform(self):
		recorder = BuildStatusRecorder()
		transformer = GocdBuildStatusTransformer(recorder.updateBuildStatuses)

		with open('./test/pipelineHistoryFixture.json') as fixtureData:
			fixtureObj = json.loads(fixtureData.read())

		result = transformer.processBuildStatuses(fixtureObj)

		expectedStatus = BuildStatus("pipeline1")
		expectedStatus2 = BuildStatus("pipeline2")
		expectedStatuses = BuildStatuses([expectedStatus, expectedStatus2])

		actualStatuses = recorder.buildStatuses

		self.assertEqual(actualStatuses.statuses[0].name, expectedStatuses.statuses[0].name)
		self.assertEqual(actualStatuses.statuses[1].name, expectedStatuses.statuses[1].name)
