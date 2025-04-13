import json

# default names as of April/2025
FOLLOWING_FILE_NAME = "following.json"
FOLLOWERS_FILE_NAME = "followers_1.json"
# enter full path in case relative path is not working for you
FULL_PATH_FOLLOWING = "ENTER_FULL_PATH/following.json" 
FULL_PATH_FOLLOWERS = "ENTER_FULL_PATH/followers_1.json"

def extract_values(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    values = []

    def recursive_search(json_obj):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                if key == "value":
                    values.append(value)
                else:
                    recursive_search(value)
        elif isinstance(json_obj, list):
            for item in json_obj:
                recursive_search(item)


    recursive_search(data)

    return values

def main():
    
    print("       ▐ ▄ ▄▄▄ .    ▄▄▄▄▄                 ▐ ▄ ▄▄▄ .")
    print("▪     •█▌▐█▀▄.▀·    •██  ▪         ▪     •█▌▐█▀▄.▀·")
    print(" ▄█▀▄ ▐█▐▐▌▐▀▀▪▄     ▐█.▪ ▄█▀▄      ▄█▀▄ ▐█▐▐▌▐▀▀▪▄")
    print("▐█▌.▐▌██▐█▌▐█▄▄▌     ▐█▌·▐█▌.▐▌    ▐█▌.▐▌██▐█▌▐█▄▄▌")
    print(" ▀█▄▀▪▀▀ █▪ ▀▀▀      ▀▀▀  ▀█▄▀▪     ▀█▄▀▪▀▀ █▪ ▀▀▀ ")

    print("v. "+str(VERSION)+"\n")
    path_set = input("Using relative or fullpath? (r/f): \n").strip().lower()

    if(path_set == 'r'):
        following_values = extract_values(FOLLOWING_FILE_NAME)
        followers_values = extract_values(FOLLOWERS_FILE_NAME)
    elif(path_set == 'f'):
        following_values = extract_values(FULL_PATH_FOLLOWING)
        followers_values = extract_values(FULL_PATH_FOLLOWERS)
    else:
        print("Default use of relative path.")
        following_values = extract_values(FOLLOWING_FILE_NAME)
        followers_values = extract_values(FOLLOWERS_FILE_NAME)

    following_set = set(following_values)
    followers_set = set(followers_values)

    only_in_following = following_set - followers_set
    only_in_followers = followers_set - following_set

    print("\n--- Unique values in 'following.json' but not in '"+FOLLOWING_FILE_NAME+"' --- \n")
    for username in only_in_following:
        print(username)

    print("\n--- Unique values in 'followers.json' but not in '"+FOLLOWERS_FILE_NAME+"' --- \n")
    for username in only_in_followers:
        print(username)
    input("Press Enter to exit.")


if __name__ == "__main__":
    VERSION = 1.1
    main()