from ingestion.youtube.apify_youtube import (
    fetch_creator_data
)

from analytics.youtube_analytics import (
    analyze_creator
)


creator = input(
    "Enter creator name: "
)

df = fetch_creator_data(
    creator
)

analysis = analyze_creator(df)

print()

for key, value in analysis.items():

    print(f"{key}: {value}")

    print()