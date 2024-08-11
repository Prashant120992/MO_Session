# With the PIP command, we can install any 3rd party packages.
# Example: pip install selenium
# When we are doing API Testing, we need to request module. For that, we need to search as python requests.
# To use request module, we need request package. For that, we use pip install requests.
# We can also deploy module through pycharm terminal. Open the terminal in Pycharm and type as pip install requests.
import requests

res = requests.get("http://www.google.com")
# Calling request module with get() function.
print(res)
print(res.url)
print(res.cookies)
print(res.status_code)
print(res.text)
