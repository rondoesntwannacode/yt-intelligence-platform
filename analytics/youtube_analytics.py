import pandas as pd


# --------------------------------------------------
# MAIN ANALYSIS ENGINE
# --------------------------------------------------

def analyze_creator(df):

    if df.empty:

        return {
            "error": "No creator data found."
        }

    # ----------------------------------------------
    # CLEAN DATA
    # ----------------------------------------------

    df["views"] = pd.to_numeric(
        df["views"],
        errors="coerce"
    ).fillna(0)

    total_videos = len(df)

    total_views = int(
        df["views"].sum()
    )

    average_views = int(
        df["views"].mean()
    )

    median_views = int(
        df["views"].median()
    )

    # ----------------------------------------------
    # TOP VIDEO
    # ----------------------------------------------

    top_video = df.sort_values(
        by="views",
        ascending=False
    ).iloc[0]

    # ----------------------------------------------
    # CONSISTENCY
    # ----------------------------------------------

    consistency_ratio = round(

        median_views / average_views,

        2

    ) if average_views > 0 else 0

    if consistency_ratio >= 0.8:

        consistency = "Highly Consistent"

    elif consistency_ratio >= 0.5:

        consistency = "Moderately Consistent"

    else:

        consistency = "Volatile"

    # ----------------------------------------------
    # MOMENTUM
    # ----------------------------------------------

    recent_avg = int(
        df.head(5)["views"].mean()
    )

    old_avg = int(
        df.tail(5)["views"].mean()
    )

    if recent_avg > old_avg * 1.3:

        momentum = "Strong Uptrend"

    elif recent_avg < old_avg * 0.7:

        momentum = "Declining"

    else:

        momentum = "Stable"

    # ----------------------------------------------
    # CREATOR SCORE
    # ----------------------------------------------

    creator_score = min(

        100,

        round(

            (
                (average_views / 150000)

                +

                (consistency_ratio * 35)

                +

                (total_videos * 1.2)

            ),

            2
        )
    )

    # ----------------------------------------------
    # PERFORMANCE TIER
    # ----------------------------------------------

    if creator_score >= 75:

        performance_tier = "Dominant"

    elif creator_score >= 50:

        performance_tier = "Established"

    elif creator_score >= 25:

        performance_tier = "Growing"

    else:

        performance_tier = "Emerging"

    # ----------------------------------------------
    # CREATOR ARCHETYPE
    # ----------------------------------------------

    titles = " ".join(

        df["video_title"]
        .astype(str)
        .tolist()

    ).lower()

    if any(word in titles for word in [

        "code",
        "python",
        "developer",
        "programming",
        "software",
        "ai",
        "tech"

    ]):

        creator_archetype = "Technical Educator"

    elif any(word in titles for word in [

        "vlog",
        "travel",
        "daily",
        "lifestyle"

    ]):

        creator_archetype = "Lifestyle Creator"

    elif any(word in titles for word in [

        "podcast",
        "interview",
        "conversation"

    ]):

        creator_archetype = "Podcast & Commentary"

    elif any(word in titles for word in [

        "gaming",
        "minecraft",
        "valorant",
        "pubg"

    ]):

        creator_archetype = "Gaming Creator"

    elif any(word in titles for word in [

        "funny",
        "comedy",
        "prank",
        "roast"

    ]):

        creator_archetype = "Entertainment Creator"

    else:

        creator_archetype = "General Digital Creator"

    # ----------------------------------------------
    # CONTENT STRENGTH
    # ----------------------------------------------

    high_performing = len(

        df[
            df["views"] >
            average_views
        ]

    )

    content_strength_ratio = round(

        high_performing / total_videos,

        2

    )

    if content_strength_ratio >= 0.7:

        content_strength = "Very Strong"

    elif content_strength_ratio >= 0.4:

        content_strength = "Strong"

    else:

        content_strength = "Inconsistent"

    # ----------------------------------------------
    # SUMMARY
    # ----------------------------------------------

    summary = f"""

    {top_video['channel_name']} is currently classified as a
    {performance_tier.lower()} creator with
    {momentum.lower()} momentum dynamics.

    The channel demonstrates
    {consistency.lower()} performance consistency
    across uploaded content.

    Average content performance is approximately
    {average_views:,} views per upload,
    with a total observed reach of
    {total_views:,} views.

    The creator primarily fits the
    {creator_archetype.lower()} archetype.

    Overall content quality appears
    {content_strength.lower()}
    based on relative video performance patterns.

    Current creator intelligence score:
    {creator_score}/100.
    """

    # ----------------------------------------------
    # FINAL OBJECT
    # ----------------------------------------------

    analysis = {

        "channel_name":
        top_video["channel_name"],

        "total_videos":
        total_videos,

        "total_views":
        total_views,

        "average_views":
        average_views,

        "median_views":
        median_views,

        "consistency":
        consistency,

        "content_strength":
        content_strength,

        "momentum":
        momentum,

        "creator_score":
        creator_score,

        "performance_tier":
        performance_tier,

        "creator_archetype":
        creator_archetype,

        "top_video":
        top_video["video_title"],

        "top_video_views":
        int(top_video["views"]),

        "summary":
        summary
    }

    return analysis


# --------------------------------------------------
# CREATOR DNA ENGINE
# --------------------------------------------------

def generate_creator_dna(analysis):

    average_views = analysis["average_views"]

    creator_score = analysis["creator_score"]

    if average_views >= 5_000_000:

        audience_reach = "Massive"

    elif average_views >= 1_000_000:

        audience_reach = "Very Large"

    elif average_views >= 300_000:

        audience_reach = "Large"

    elif average_views >= 100_000:

        audience_reach = "Growing"

    else:

        audience_reach = "Niche"

    if creator_score >= 80:

        viral_potential = "Extremely High"

    elif creator_score >= 60:

        viral_potential = "High"

    elif creator_score >= 40:

        viral_potential = "Moderate"

    else:

        viral_potential = "Emerging"

    dna = {

        "Audience Reach":
        audience_reach,

        "Viral Potential":
        viral_potential,

        "Consistency":
        analysis["consistency"],

        "Momentum":
        analysis["momentum"],

        "Content Style":
        analysis["creator_archetype"]
    }

    return dna