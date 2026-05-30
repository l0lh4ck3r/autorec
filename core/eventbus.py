from collections import defaultdict

from datetime import datetime


class EventBus:

    def __init__(self):

        self.subscribers = defaultdict(
            list
        )

        self.events = []

    def subscribe(
        self,
        event,
        callback
    ):

        self.subscribers[event].append(
            callback
        )

    async def publish(
        self,
        event,
        payload
    ):

        self.events.append(
            {
                "event": event,
                "payload": payload,
                "timestamp":
                datetime.utcnow()
                .isoformat()
            }
        )

        for callback in (
            self.subscribers[event]
        ):

            await callback(
                payload
            )