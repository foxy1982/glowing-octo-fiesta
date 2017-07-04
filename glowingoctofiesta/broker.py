class Broker():
	def __init__(self, upstreams = []):
		self.upstreams = upstreams

	def update(self, x):
		for upstream in self.upstreams:
			upstream(x)
