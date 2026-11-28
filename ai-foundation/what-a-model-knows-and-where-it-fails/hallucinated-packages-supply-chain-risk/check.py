# Check each name an AI suggested against PyPI's public JSON API, before installing anything.
import json
import urllib.error
import urllib.request

# The suggested requirements. The last two names were made up for this lab.
suggested = ["requests", "flask", "skillii-made-up-csv-helper", "skillii-made-up-json-cleaner"]
missing = []

for name in suggested:
    url = f"https://pypi.org/pypi/{name}/json"
    try:
        with urllib.request.urlopen(url, timeout=30) as reply:
            project = json.load(reply)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        missing.append(name)
        print(f"{name:<29} not on PyPI (404)")
        continue
    uploads = [f["upload_time"] for files in project["releases"].values() for f in files]
    version = project["info"]["version"]
    print(f"{name:<29} on PyPI  latest {version}  first upload {min(uploads)[:10]}")

print(f"{len(missing)} of {len(suggested)} names are not on PyPI: {', '.join(missing)}")
