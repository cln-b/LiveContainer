import json
import plistlib
import re
import requests
import os
from datetime import datetime

def prepare_description(text):
    text = re.sub('<[^<]+?>', '', text) # Remove HTML tags
    text = re.sub(r'#{1,6}\s?', '', text) # Remove markdown header tags
    text = re.sub(r'\*{2}', '', text) # Remove all occurrences of two consecutive asterisks
    text = re.sub(r'(?<=\r|\n)-', '•', text) # Only replace - with • if it is preceded by \r or \n
    text = re.sub(r'`', '"', text) # Replace ` with "
    text = re.sub(r'\r\n\r\n', '\r \n', text) # Replace \r\n\r\n with \r \n (avoid incorrect display of the description regarding paragraphs)
    return text

def update_json_file_nightly(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        data = {"apps": []}
        raise

    app = data["apps"][0]

    with open("LiveContainer/Info.plist", 'rb') as infile:
        info_plist = plistlib.load(infile)
    full_version = info_plist["CFBundleVersion"]
    version = re.search(r"(\d+\.\d+\.\d+)", full_version).group(1)
    
    version_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    nightly_link = os.environ.get("NIGHTLY_LINK", "")
    commit_sha = os.environ.get("commit_sha", "")[:7]
    commit_msg = os.environ.get("commit_msg", "").strip()
    target_tag = os.environ.get("NIGHTLY_TAG", "nightly")
    target_repo = os.environ.get("GITHUB_REPOSITORY", "cln-b/LiveContainer")

    download_url = f"https://github.com/{target_repo}/releases/download/{target_tag}/LiveContainer.ipa"

    description = f"""\
Nightly build from [{commit_sha}](https://github.com/{target_repo}/commit/{commit_sha}):\
 {commit_msg}

This is a nightly release [created automatically with GitHub Actions workflow]({nightly_link}).
"""
    description = prepare_description(description)

    version_entry = {
        "version": version,
        "date": version_date,
        "localizedDescription": description,
        "downloadURL": download_url,
        "size": 4740733,
        "commit": commit_sha,
        "headline": commit_msg
    }

    app["versions"].clear()
    app["versions"].append(version_entry)

    app.update({
        "version": version,
        "versionDate": version_date,
        "versionDescription": description,
        "downloadURL": download_url,
        "commit": commit_sha,
        "headline": commit_msg
    })

    data["news"] = []

    try:
        with open(json_file, "w") as file:
            json.dump(data, file, indent=2)
        print("Nightly JSON updated successfully.")
    except IOError as e:
        print(f"Error writing to JSON file: {e}")
        raise

def update_json_file_release_ss_lc(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error reading local apps_ss_lc.json: {e}")
        return

    app = data["apps"][0]

    with open("LiveContainer/Info.plist", 'rb') as infile:
        info_plist = plistlib.load(infile)
    full_version = info_plist["CFBundleVersion"]
    version = re.search(r"(\d+\.\d+\.\d+)", full_version).group(1)
    version_date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    commit_sha = os.environ.get("commit_sha", "")[:7]
    commit_msg = os.environ.get("commit_msg", "").strip()
    target_repo = os.environ.get("GITHUB_REPOSITORY", "cln-b/LiveContainer")

    # Points directly to GitHub's 'latest' release endpoint
    download_url = f"https://github.com/{target_repo}/releases/latest/download/LiveContainer+SideStore.ipa"

    description = f"""\
Nightly build from [{commit_sha}](https://github.com/{target_repo}/commit/{commit_sha}):\
 {commit_msg}
    """

    version_entry = {
        "version": version,
        "date": version_date,
        "localizedDescription": description,
        "downloadURL": download_url,
        "size": 4232092
    }

    # Overwrite main app download link & release tracks to always resolve to 'latest'
    app["downloadURL"] = download_url
    app["version"] = version

    channels = app.get('releaseChannels', [])
    for channel in channels:
        channel['releases'] = [version_entry]

    try:
        with open(json_file, "w") as file:
            json.dump(data, file, indent=2)
        print("SideStore LC JSON updated successfully to point to latest release.")
    except IOError as e:
        print(f"Error writing to JSON file: {e}")
        raise

def main():
    try:
        update_json_file_nightly("./.github/apps_nightly.json")
        update_json_file_release_ss_lc("./.github/apps_ss_lc.json")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
    