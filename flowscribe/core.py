from typing import Any, Dict, Optional
import datetime

class Event:
	"""
	Represents a single event in the flowscribe system.
	"""
	def __init__(
		self,
		event_type: str,
		flow_id: Optional[str] = None,
		step: Optional[str] = None,
		evidence: Optional[Any] = None,
		data: Optional[Dict[str, Any]] = None,
		timestamp: Optional[datetime.datetime] = None,
	):
		self.event_type = event_type
		self.flow_id = flow_id
		self.step = step
		self.evidence = evidence
		self.data = data or {}
		self.timestamp = timestamp or datetime.datetime.utcnow()

	def to_dict(self) -> Dict[str, Any]:
		return {
			"event_type": self.event_type,
			"flow_id": self.flow_id,
			"step": self.step,
			"evidence": self.evidence,
			"data": self.data,
			"timestamp": self.timestamp.isoformat(),
		}
