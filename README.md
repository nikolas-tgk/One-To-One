[![Python](https://img.shields.io/badge/Python-3.9.5-blue.svg)](https://www.python.org/)

## Instagram followers vs following comparator.
So people won't use sketchy 3rd party apps! :,)

## Files Required

To use this script, you’ll need to download two specific files from your [Instagram Accounts Center](https://accountscenter.instagram.com/info_and_permissions/dyi/):
You can either request all your data or "some of your data", in the latter case make sure to select:
1. **Followers and Following**


> Make sure you also select:
> - **Date range: All time**
> - **Format: JSON**

Once downloaded, **extract the files** and place these two JSON files in the **same directory** as the Python script.

---

##  File Names

As of **April 2025**, Instagram names these files:

```python
FOLLOWING_FILE_NAME = "following.json"
FOLLOWERS_FILE_NAME = "followers_1.json"

# If you renamed the files or want to use full paths instead, you can customize:

FULL_PATH_FOLLOWING = "ENTER_FULL_PATH/following.json"
FULL_PATH_FOLLOWERS = "ENTER_FULL_PATH/followers_1.json"

# Notice: Use full paths if you're getting a FileNotFoundError (e.g. VSCode not running the script from the actual script location).
