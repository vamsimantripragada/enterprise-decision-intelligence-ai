from datetime import datetime
import uuid


class AuditLogger:
    """
    Lightweight audit logger.
    Can later be replaced with DB or external logging systems.
    """

    def log(self, event_type: str, payload: dict):
        log_entry = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }

        # For now, print logs (later: DB / CloudWatch / Splunk)
        print(log_entry)
