import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = [
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtubepartner",
]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes
)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials
)


def subscribe(keyword):
    ids = getChannelId(keyword)
    for id in ids:
        try:
            request = (
                youtube.subscriptions()
                .insert(
                    part="snippet",
                    body=dict(snippet=dict(resourceId=dict(channelId=id))),
                )
                .execute()
            )
        except:
            print("already exist")


def unsubscribe(keyword):
    ids = getSubId(keyword)
    for id in ids:
        try:
            request = youtube.subscriptions().delete(id=id).execute()
        except Exception as e:
            print(e)


def getSubId(keyWord=""):
    keyWord = keyWord.lower()
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)
    response = request.execute()
    ids = []

    for item in response["items"]:
        if keyWord in item["snippet"]["title"].lower():
            ids.append(item["id"])
    nextPage = response["nextPageToken"]
    while nextPage != None:
        request = youtube.subscriptions().list(
            part="snippet", mine=True, maxResults=50, pageToken=nextPage
        )
        response = request.execute()
        for item in response["items"]:
            if keyWord in item["snippet"]["title"].lower():
                ids.append(item["id"])
        try:
            nextPage = response["nextPageToken"]
        except:
            break

    return ids


def getChannelId(keyWord=""):
    keyWord = keyWord.lower()
    request = youtube.subscriptions().list(part="snippet", mine=True, maxResults=50)
    response = request.execute()
    ids = []

    for item in response["items"]:
        if keyWord in item["snippet"]["title"].lower():
            ids.append(item["snippet"]["resourceId"]["channelId"])
    nextPage = response["nextPageToken"]
    while nextPage != None:
        request = youtube.subscriptions().list(
            part="snippet", mine=True, maxResults=50, pageToken=nextPage
        )
        response = request.execute()
        for item in response["items"]:
            if keyWord in item["snippet"]["title"].lower():
                ids.append(item["snippet"]["resourceId"]["channelId"])
        try:
            nextPage = response["nextPageToken"]
        except:
            break

    return ids


# print(getSubId(keyWord='asmr'))
unsubscribe("asmr")
