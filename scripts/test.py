import requests
import threading

def forward_request():
    response = requests.post(
        "https://localhost:3001/v1/chat/completions",
        headers={
            "Content-Type": "application/json"
        },
        json={
            "model": "default",
            "max_tokens": 8192,
            "messages": [
                {
                    "role": "user",
                    "content": "What is the Sokoban game?"
                }
            ],
            "stream": False,
            "sampling_params": {
                "ignore_eos": True
            }
        }
    )
    print(response.json())

thread_pool=[]
for i in range(48):
    t = threading.Thread(target=forward_request)
    t.start()
    thread_pool.append(t)

for t in thread_pool:
    t.join()
