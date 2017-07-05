from glowingoctofiesta.buildStatuses import BuildStatuses
from glowingoctofiesta.buildStatuses import BuildStatus

class GocdBuildStatusTransformer():
	def __init__(self, upstream):
		self.upstream = upstream

	def processBuildStatuses(self, buildStatuses):
		status = BuildStatus(buildStatuses['pipelines'][0]['name'])
		status2 = BuildStatus(buildStatuses['pipelines'][1]['name'])
		statuses = BuildStatuses([status,status2])

		self.upstream(statuses)
