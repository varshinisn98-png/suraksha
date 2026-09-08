"""
Visualization utilities with ultra-premium dark glassmorphic styling & Plotly themes.
"""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DARK_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(15, 20, 32, 0.5)",
    font=dict(family="Plus Jakarta Sans, Inter, sans-serif", color="#e5e7eb", size=13),
    title_font=dict(size=16, color="#f9fafb"),
    xaxis=dict(
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.06)",
        zerolinecolor="rgba(255, 255, 255, 0.12)",
        tickfont=dict(color="#9ca3af"),
        title=dict(font=dict(color="#d1d5db")),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.06)",
        zerolinecolor="rgba(255, 255, 255, 0.12)",
        tickfont=dict(color="#9ca3af"),
        title=dict(font=dict(color="#d1d5db")),
    ),
    margin=dict(l=40, r=40, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#1e2436",
        bordercolor="rgba(255,255,255,0.15)",
        font=dict(family="Plus Jakarta Sans, sans-serif", size=13, color="#f9fafb"),
    ),
)


def crime_trend_line(df: pd.DataFrame, city: str) -> go.Figure:
    sub = df[df["city"] == city].sort_values("year")
    fig = go.Figure()

    # Main trend curve
    fig.add_trace(
        go.Scatter(
            x=sub["year"],
            y=sub["crime_rate"],
            mode="lines+markers",
            name="Crime Rate",
            line=dict(color="#6366f1", width=3.5, shape="spline"),
            marker=dict(size=7, color="#818cf8", line=dict(color="#ffffff", width=1.5)),
            hovertemplate="<b>Year %{x}</b><br>Crime Rate: %{y:.2f} per 100k<extra></extra>",
        )
    )

    # Add vertical line demarcating historical baseline and projection period
    fig.add_vline(
        x=2012, line_dash="dash", line_color="rgba(156, 163, 175, 0.6)",
        annotation_text="Historical NCRB Baseline", annotation_position="top left",
        annotation_font=dict(color="#9ca3af", size=11),
    )

    # Highlight 2026 forecast point
    row_2026 = sub[sub["year"] == 2026]
    if not row_2026.empty:
        rate_2026 = row_2026.iloc[0]["crime_rate"]
        fig.add_trace(
            go.Scatter(
                x=[2026],
                y=[rate_2026],
                mode="markers+text",
                marker=dict(symbol="star", size=16, color="#ef4444", line=dict(color="#ffffff", width=2)),
                text=[f"  2026 Forecast ({rate_2026:.1f})"],
                textposition="top left",
                name="2026 Forecast",
                hovertemplate="<b>2026 Projected Rate</b>: %{y:.2f} per 100k<extra></extra>",
            )
        )

    fig.update_layout(
        title=f"📈 Crime Rate Trend & 2026 Projection — {city}",
        xaxis_title="Year",
        yaxis_title="Crime Rate (per 100,000 population)",
        showlegend=False,
        hovermode="x unified",
        **DARK_LAYOUT,
    )
    return fig


def city_comparison_bar(df: pd.DataFrame, year: int, top_n: int = 25) -> go.Figure:
    sub = df[df["year"] == year].sort_values("crime_rate", ascending=False).head(top_n)
    
    color_map = {"LOW": "#10b981", "MEDIUM": "#f59e0b", "HIGH": "#ef4444"}
    bar_colors = [color_map.get(lbl, "#6b7280") for lbl in sub["risk_label"]]

    fig = go.Figure(
        go.Bar(
            x=sub["city"],
            y=sub["crime_rate"],
            marker=dict(color=bar_colors, cornerradius=6),
            text=[f"{v:.1f}" for v in sub["crime_rate"]],
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Crime Rate: %{y:.2f} per 100k<extra></extra>",
        )
    )

    fig.update_layout(
        title=f"📊 City/District Ranking — Reported Crime Rate ({year})",
        xaxis_title="City / District",
        yaxis_title="Crime Rate (per 100,000)",
        xaxis_tickangle=-45,
        **DARK_LAYOUT,
    )
    return fig


def category_distribution(df: pd.DataFrame, city: str, year: int) -> go.Figure:
    row = df[(df["city"] == city) & (df["year"] == year)]
    if row.empty:
        return go.Figure()
    
    share_cols = [c for c in df.columns if c.endswith("_share")]
    labels = [c.replace("_cases_share", "").replace("_", " ").title() for c in share_cols]
    values = row[share_cols].iloc[0].fillna(0).values

    neon_palette = ["#6366f1", "#ec4899", "#f59e0b", "#10b981", "#06b6d4", "#8b5cf6"]

    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.45,
            marker=dict(colors=neon_palette[: len(labels)], line=dict(color="#0e1322", width=2)),
            textinfo="percent+label",
            hovertemplate="<b>%{label}</b><br>Share: %{percent:.1%}<extra></extra>",
        )
    )

    fig.update_layout(
        title=f"🧩 Crime Category Breakdown — {city} ({year})",
        showlegend=False,
        **DARK_LAYOUT,
    )
    return fig


def state_trend_lines(df: pd.DataFrame, state: str) -> go.Figure:
    sub = df[df["state"] == state]
    fig = px.line(
        sub, x="year", y="crime_rate", color="city", markers=True,
        title=f"🌐 Crime Rate Trends Across Districts/Cities — {state} (2001–2026)",
    )
    fig.add_vline(
        x=2026, line_dash="dot", line_color="#ef4444",
        annotation_text="2026 Target", annotation_position="top right"
    )
    fig.update_layout(hovermode="x unified", **DARK_LAYOUT)
    return fig
