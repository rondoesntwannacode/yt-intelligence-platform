# Neon Glassmorphism AI Creator Intelligence Dashboard


import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
import plotly.express as px

from ingestion.youtube.apify_youtube import (
    fetch_creator_data
)

from analytics.youtube_analytics import (
    analyze_creator,
    generate_creator_dna
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Creator Intelligence",
    page_icon="🚀",
    layout="wide"
)


# --------------------------------------------------
# CACHE
# --------------------------------------------------

CACHE_DIR = "cache"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)


@st.cache_data(show_spinner=False)
def get_cached_creator_data(creator_name):

    safe_name = (
        creator_name
        .lower()
        .replace(" ", "_")
    )

    cache_file = os.path.join(
        CACHE_DIR,
        f"{safe_name}.csv"
    )

    if os.path.exists(cache_file):

        return pd.read_csv(cache_file)

    df = fetch_creator_data(creator_name)

    if not df.empty:
        df.to_csv(cache_file, index=False)

    return df


# --------------------------------------------------
# GLASSMORPHISM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .stApp {

        background:
        linear-gradient(
            135deg,
            #020617,
            #0f172a,
            #111827
        );

        color: white;
    }

    h1, h2, h3, h4 {
        color: white !important;
        font-family: 'Segoe UI';
    }

    p, div {
        color: #e2e8f0;
    }

    .glass-card {

        background:
        rgba(255,255,255,0.05);

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius: 24px;

        padding: 24px;

        backdrop-filter: blur(18px);

        box-shadow:
        0px 8px 32px rgba(0,0,0,0.35);

        margin-bottom: 20px;
    }

    .hero-section {

        background:
        linear-gradient(
            135deg,
            rgba(0,245,255,0.18),
            rgba(139,92,246,0.18)
        );

        border:
        1px solid rgba(255,255,255,0.1);

        border-radius: 30px;

        padding: 40px;

        backdrop-filter: blur(25px);

        margin-bottom: 30px;
    }

    div[data-testid="metric-container"] {

        background:
        rgba(255,255,255,0.05);

        border:
        1px solid rgba(255,255,255,0.08);

        padding: 18px;

        border-radius: 20px;

        backdrop-filter: blur(12px);

        box-shadow:
        0px 4px 20px rgba(0,0,0,0.2);
    }

    .dna-card {

        background:
        rgba(255,255,255,0.05);

        border-left:
        4px solid #00f5ff;

        border-radius: 18px;

        padding: 18px;

        margin-bottom: 15px;

        backdrop-filter: blur(12px);
    }

    .stButton>button {

        background:
        linear-gradient(
            135deg,
            #00f5ff,
            #8b5cf6
        );

        color: white;

        border: none;

        border-radius: 18px;

        padding: 12px 24px;

        font-weight: bold;

        transition: 0.3s ease;
    }

    .stButton>button:hover {

        transform: scale(1.03);

        box-shadow:
        0px 0px 25px rgba(0,245,255,0.5);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown(
    """
    <div class="hero-section">

    <h1>
    🚀 AI Creator Intelligence Platform
    </h1>

    <p>
    Futuristic creator analytics, trend intelligence,
    and AI-powered behavioral insights.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SEARCH BAR
# --------------------------------------------------

search_col, button_col = st.columns([5, 1])

with search_col:

    creator_name = st.text_input(
        "",
        placeholder="Search creators like Fireship, Theo, Lex Fridman..."
    )

with button_col:

    st.markdown("<br>", unsafe_allow_html=True)

    analyze = st.button("Analyze")


# --------------------------------------------------
# HOME SCREEN
# --------------------------------------------------

if not analyze:

    st.subheader("🔥 Trending Searches")

    t1, t2, t3, t4 = st.columns(4)

    t1.metric("Trending", "Fireship")
    t2.metric("Trending", "Theo")
    t3.metric("Trending", "Lex Fridman")
    t4.metric("Trending", "DeepLearningAI")


    st.subheader("⚡ Platform Intelligence")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="glass-card">

            <h3>🧠 AI Insights</h3>

            <p>
            Generate creator intelligence summaries,
            trend analysis, and performance interpretation.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="glass-card">

            <h3>📈 Trend Analytics</h3>

            <p>
            Analyze creator momentum,
            audience reach,
            and content performance.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="glass-card">

            <h3>🧬 Creator DNA</h3>

            <p>
            Understand creator style,
            viral potential,
            and trend alignment.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# ANALYSIS SECTION
# --------------------------------------------------

if analyze and creator_name:

    with st.spinner(
        "Generating AI creator intelligence..."
    ):

        df = get_cached_creator_data(
            creator_name
        )

        analysis = analyze_creator(df)

        dna = generate_creator_dna(analysis)


    if "error" in analysis:

        st.error(
            analysis["error"]
        )

    else:

        # ----------------------------------------------
        # CREATOR HEADER
        # ----------------------------------------------

        st.markdown(
            f"""
            <div class="hero-section">

            <h1>
            📺 {analysis['channel_name']}
            </h1>

            <p>
            {analysis['performance_tier']} Creator •
            {analysis['momentum']} Momentum •
            AI Intelligence Profile
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # ----------------------------------------------
        # METRICS
        # ----------------------------------------------

        st.subheader("📊 Creator Intelligence")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric(
            "Creator Score",
            analysis["creator_score"]
        )

        m2.metric(
            "Performance Tier",
            analysis["performance_tier"]
        )

        m3.metric(
            "Momentum",
            analysis["momentum"]
        )

        m4.metric(
            "Consistency",
            analysis["consistency"]
        )


        m5, m6, m7 = st.columns(3)

        m5.metric(
            "Videos Indexed",
            analysis["total_videos"]
        )

        m6.metric(
            "Total Views",
            f"{analysis['total_views']:,}"
        )

        m7.metric(
            "Average Views",
            f"{analysis['average_views']:,}"
        )


        # ----------------------------------------------
        # TABS
        # ----------------------------------------------

        tab1, tab2, tab3, tab4 = st.tabs([
            "🧠 AI Insights",
            "🧬 Creator DNA",
            "📈 Performance",
            "🔥 Top Videos"
        ])


        # ==============================================
        # TAB 1
        # ==============================================

        with tab1:

            st.markdown(
                f"""
<div class="glass-card">

<h3>🧠 AI Creator Summary</h3>

<div style="line-height:1.9; font-size:17px; color:#e2e8f0;">

{analysis['summary']}

</div>

</div>
""",
                unsafe_allow_html=True
            )


            st.subheader("📌 Creator Archetype")

            st.info(
                analysis['creator_archetype']
            )


           


        # ==============================================
        # TAB 2
        # ==============================================

        with tab2:

            st.subheader("🧬 Creator DNA")

            d1, d2 = st.columns(2)

            items = list(dna.items())

            with d1:

                for key, value in items[:3]:

                    st.markdown(
                        f"""
                        <div class="dna-card">

                        <h4>{key}</h4>

                        <p>{value}</p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            with d2:

                for key, value in items[3:]:

                    st.markdown(
                        f"""
                        <div class="dna-card">

                        <h4>{key}</h4>

                        <p>{value}</p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


        # ==============================================
        # TAB 3
        # ==============================================

        with tab3:

            st.subheader("📈 Video Performance")

            chart_df = df.sort_values(
                by="views",
                ascending=False
            ).head(10)

            fig = px.bar(
                chart_df,
                x="views",
                y="video_title",
                orientation="h",
                color="views",
                title="Top Performing Videos"
            )

            fig.update_layout(
                template="plotly_dark",
                plot_bgcolor="#020617",
                paper_bgcolor="#020617",
                font_color="white",
                yaxis={
                    "categoryorder":
                    "total ascending"
                }
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


            scatter = px.scatter(
                df,
                x=df.index,
                y="views",
                size="views",
                hover_name="video_title",
                color="views",
                title="Audience Reach Distribution"
            )

            scatter.update_layout(
                template="plotly_dark",
                plot_bgcolor="#020617",
                paper_bgcolor="#020617",
                font_color="white"
            )

            st.plotly_chart(
                scatter,
                use_container_width=True
            )


        # ==============================================
        # TAB 4
        # ==============================================

        with tab4:

            st.subheader("🔥 Highest Performing Videos")

            top_videos = df.sort_values(
                by="views",
                ascending=False
            )

            st.dataframe(
                top_videos[
                    [
                        "video_title",
                        "views"
                    ]
                ],
                use_container_width=True,
                height=500
            )

