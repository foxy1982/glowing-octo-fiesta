class GocdBuildStatusTransformer():
	def __init__(self, upstream):
		self.upstream = upstream

	def processBuildStatus(self, statuses = []):
		self.upstream(len(statuses))
