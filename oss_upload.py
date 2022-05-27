import sys
import hashlib
import oss2
import yaml
import os

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

file = open("oss-config.yaml", "r")
config = yaml.safe_load(file)
file.close()
auth = oss2.Auth(config["accessKey"], config["accessSecret"])
bucket = oss2.Bucket(auth, config["endpoint"], config["bucket"])

manifest_file = open("oss-manifest.yaml", "w+")
manifest = yaml.safe_load(manifest_file)
if not manifest:
    manifest = dict()

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        sha1 = hashlib.sha1()
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
        return sha1.hexdigest()

def upload_file(file_path):
    file_hash = get_file_hash(file_path)
    file_key = f"{file_hash[0:2]}/{file_hash[2:4]}/{file_hash[4:]}"
    try:
        bucket.head_object(file_key)
        print("File exists. Skip.")
    except oss2.exceptions.NotFound:
        with open(file_path, 'rb') as f:
            bucket.put_object(file_key, f)
    return file_key

if __name__ == "__main__":

    games_dir = os.path.join("games")
    authors_dir = os.path.join("authors")
    assets_dir = os.path.join("assets")
    avatar_dir = os.path.join(assets_dir, "_avatar")

    for f in os.listdir(authors_dir):
        file_path = os.path.join(authors_dir, f)
        if not os.path.isfile(file_path):
            continue
        file_key = f.split(".")[0]
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            if not data["avatar"]:
                continue
            print("Uploading author avatar: %s %s" % (file_key, data["avatar"]))
            asset_path = os.path.join(avatar_dir, data["avatar"])
            if not os.path.isfile(asset_path):
                continue
            oss_key = upload_file(asset_path)
            manifest[asset_path] = oss_key

    for f in os.listdir(games_dir):
        file_path = os.path.join(games_dir, f)
        if not os.path.isfile(file_path):
            continue
        file_key = f.split(".")[0]
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            if not data["thumbnail"]:
                continue
            print("Uploading game thumbnail: %s %s" % (file_key, data["thumbnail"]))
            asset_path = os.path.join(assets_dir, file_key, data["thumbnail"])
            if not os.path.isfile(asset_path):
                continue
            oss_key = upload_file(asset_path)
            manifest[asset_path] = oss_key
    
    yaml.dump(manifest, manifest_file)
    manifest_file.close()

        
