from channels.routing import route
channel_routing = [
    route('http.request', 'myapp.consumers.http_request_consumer')
]