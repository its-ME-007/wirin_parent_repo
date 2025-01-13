from queue import Queue
import asyncio
from fastapi import Request
import json

class RequestQueueManager:
    def __init__(self):
        self.request_queue = Queue()
        self.is_processing = False
        self.processed_requests = []
        
    async def add_request(self, response_data: str):
        """Add a request to the queue"""
        try:
            # Parse the JSON string to dict
            if isinstance(response_data, str):
                response_dict = json.loads(response_data)
            else:
                response_dict = response_data
                
            self.request_queue.put(response_dict)
            print(f"Added to queue: {response_dict}")
            print(f"Current queue size: {self.get_queue_size()}")
        except json.JSONDecodeError as e:
            print(f"Error parsing response data: {e}")
        except Exception as e:
            print(f"Error adding to queue: {e}")
        
    def get_queue_size(self) -> int:
        """Get current size of the queue"""
        return self.request_queue.qsize()
    
    def get_queue_status(self) -> dict:
        """Get queue status information"""
        return {
            "queue_size": self.get_queue_size(),
            "is_processing": self.is_processing,
            "processed_requests": self.processed_requests
        }
        
    async def process_requests(self):
        """Process requests from the queue"""
        self.is_processing = True
        while self.is_processing:
            if not self.request_queue.empty():
                request = self.request_queue.get()
                await self._handle_request(request)
            await asyncio.sleep(0.1)
            
    async def _handle_request(self, response_data: dict):
        """Handle individual requests"""
        print(f"Processing request: {response_data}")
        self.processed_requests.append(response_data)

# Global instance of the queue manager
request_queue_manager = RequestQueueManager()