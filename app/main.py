from sanic import Sanic, json
from app.config import settings

app = Sanic(settings.app_name)

@app.route("/")
async def index(request):
    return json({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
