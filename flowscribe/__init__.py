# flowscribe package

# Ensure required dependencies are installed
try:
	import yaml  # noqa: F401
except ImportError:
	raise ImportError(
		"Missing required dependency 'pyyaml'. Please install it with 'pip install pyyaml' before using flowscribe."
	)
