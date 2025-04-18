import requests

def check_remote_status(url="https://example.com/version.json"):
    try:
        res = requests.get(url, timeout=5)
        info = res.json()
        return {
            "available": info.get("available", True),
            "maintenance": info.get("maintenance", False),
            "latest_version": info.get("latest_version", "")
        }
    except Exception as e:
        print("远程检查失败:", e)
        return {
            "available": True,
            "maintenance": False,
            "latest_version": ""
        }
