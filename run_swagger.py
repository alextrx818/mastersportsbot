import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api.swagger_app:app", host="0.0.0.0", port=8000, reload=True)
