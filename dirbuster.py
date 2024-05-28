import os
try:
    import requests
except ImportError:
    os.system("pip install requests")

target = input("# Enter the URL target: ")
file_name = input("# Enter the file: ")

if not target.startswith("https://") and not target.startswith("http://"):
    try:
        requests.get("https://" + target)
    except requests.ConnectionError:
        target = "http://" + target

if "/" not in target.split(".")[1]:
    target = target + "/"

directories_found = []

print("\n$ ======= started ======= \n\n")

for directory in open(file_name, "r").read().splitlines():
    url = target + directory
    response = requests.get(url).status_code

    if response == 200:
        print("found       \t>>> \t" + url)
        directories_found.append(url)
    elif response >= 300 and response < 400:
        print("redir       \t>>> \t" + url)
    else:
        print("don't found \t>>> \t" + url)

print("\n\n$ ======= existing directories ======\n")
for directory in directories_found:
    print(directory)
