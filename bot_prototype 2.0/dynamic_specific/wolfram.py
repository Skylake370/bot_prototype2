import wolframalpha

client = wolframalpha.Client('9XGKX3-XWR8U4YV69')
res = client.query(raw_input(""))

for pod in res.pods:
    for sub in pod.subpods:
        print(pod.subpods)
        
