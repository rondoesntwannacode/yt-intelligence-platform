import os
import pandas as pd

from dotenv import load_dotenv
from apify_client import ApifyClient


# -----------------------------------------
# LOAD ENV VARIABLES
# -----------------------------------------

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")


# -----------------------------------------
# CREATE APIFY CLIENT
# -----------------------------------------

client = ApifyClient(APIFY_TOKEN)


# -----------------------------------------
# FETCH CREATOR DATA
# -----------------------------------------

def fetch_creator_data(channel_name):

    run_input = {

        "searchQueries": [channel_name],

        "maxResults": 30,

        "sort": "views",

        "type": "video"
    }

    run = client.actor(

        "streamers/youtube-scraper"

    ).call(

        run_input=run_input

    )

    dataset_id = run["defaultDatasetId"]

    items = client.dataset(
        dataset_id
    ).iterate_items()

    videos = []

    for item in items:

       videos.append({

    "video_title":
    item.get("title", "Unknown"),

    "channel_name":
    item.get("channelName", "Unknown"),

    "views":
    item.get("viewCount", 0),

    "likes":
    item.get("likeCount", 0),

    "published_at":
    item.get("publishedTime")
    or "Unknown",

    "video_url":
    item.get("url", "")
})

    df = pd.DataFrame(videos)

    return df


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    creator = input(
        "Enter creator/channel name: "
    )

    df = fetch_creator_data(
        creator
    )

    print()

    print(df.head())