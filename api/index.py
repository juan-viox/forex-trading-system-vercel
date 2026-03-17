from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        if self.path == '/api/health':
            response = {
                "status": "healthy",
                "service": "forex-trading-system",
                "agents": 8,
                "timestamp": "2026-03-18T00:20:00Z",
                "platform": "vercel",
                "ready_for_trading": True
            }
        elif self.path == '/api':
            response = {
                "service": "forex-trading-system",
                "status": "live",
                "message": "Forex Trading System deployed on Vercel",
                "endpoints": {
                    "health": "/api/health",
                    "ping": "/api/ping",
                    "analyze": "/api/analyze",
                    "signals": "/api/signals",
                    "execute": "/api/execute"
                },
                "agents": [
                    "market-analysis",
                    "prediction",
                    "risk-assessment",
                    "position-sizing",
                    "entry-exit-strategy",
                    "risk-management",
                    "performance-monitoring",
                    "adaptive-learning"
                ]
            }
        elif self.path == '/api/ping':
            response = {"message": "pong"}
        else:
            response = {
                "error": "Endpoint not found",
                "available_endpoints": ["/api", "/api/health", "/api/ping"]
            }
            self.send_response(404)
        
        self.wfile.write(json.dumps(response).encode())
        return