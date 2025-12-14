import requests
import json

def test_analyze():
    url = "http://localhost:8000/analyze"
    
    # Repo 1
    payload1 = {"url": "https://github.com/demo/repo-one"}
    print(f"Testing {payload1['url']}...")
    try:
        response1 = requests.post(url, json=payload1)
        data1 = response1.json()
        print(f"Repo 1 Score: {data1.get('score')}")
        print(f"Repo 1 Owner: {data1.get('owner')}")
    except Exception as e:
        print(f"Repo 1 Failed: {e}")
        return

    # Repo 2
    payload2 = {"url": "https://github.com/different/repo-two"}
    print(f"Testing {payload2['url']}...")
    try:
        response2 = requests.post(url, json=payload2)
        data2 = response2.json()
        print(f"Repo 2 Score: {data2.get('score')}")
        print(f"Repo 2 Owner: {data2.get('owner')}")
    except Exception as e:
        print(f"Repo 2 Failed: {e}")
        return

    if "Problem & Product Thinking" in data1.get("breakdown", {}):
        print("✅ SUCCESS: Found Recruiter Breakdown keys.")
    else:
        print("❌ FAIL: Old breakdown keys found.")
        print(data1.get("breakdown"))

    if "verdict" in data1:
        print(f"✅ SUCCESS: Verdict found: {data1['verdict']}")
    else:
        print("❌ FAIL: Verdict missing.")

    print("\n--- MIRROR OUTPUT CHECK ---")
    print(f"Summary: {data1.get('summary')}")
    print(f"Roadmap: {data1.get('roadmap')}")
    print("---------------------------\n")

if __name__ == "__main__":
    test_analyze()
