#!/usr/bin/env python3
"""Mira Bootcamp — dashboard builder v1.3.0 (HARDCODED for this machine).

Reads ROADMAP.md + STATUS.txt, queries AnkiConnect (live), and writes docs/index.html
for GitHub Pages. Run at the end of EVERY session (Rule 14).

Requires: python + requests (`pip install requests`). Anki must be RUNNING with
AnkiConnect enabled for live card stats (script degrades gracefully if not).

Usage:
    python scripts\\build_dashboard.py
"""
import os
import re
import json
import sys
from datetime import datetime

# --- HARDCODED FOR THIS MACHINE (set during setup — never ask again) ---
ROOT_PATH = r"A:\Ai-assisted-learning"
GITHUB_USERNAME = "Visakan-official"
REPO_NAME = "learning"                      # → https://visakan-official.github.io/learning/
ANKI_CONNECT_URL = "http://127.0.0.1:8765"  # AnkiConnect (FooSoft add-on 2055492159)
# -----------------------------------------------------------------------

OUTPUT_DIR = os.path.join(ROOT_PATH, "docs")
ROADMAP_PATH = os.path.join(ROOT_PATH, "ROADMAP.md")
STATUS_PATH = os.path.join(ROOT_PATH, "STATUS.txt")
INDEX_PATH = os.path.join(OUTPUT_DIR, "index.html")


def parse_roadmap():
    """Extract module topics + checked state from ROADMAP.md checkboxes."""
    modules = []
    try:
        with open(ROADMAP_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        for status, title in re.findall(r"[-*]\s+\[([ xX~])\]\s+(.+?)(?:\n|$)", content):
            completed = status.lower() == "x"
            modules.append({"title": title.strip(), "completed": completed})
    except Exception as e:
        print(f"[warn] Error reading roadmap: {e}")
    return modules


def get_anki_stats():
    """Live stats from AnkiConnect. Returns zeros if Anki is down."""
    stats = {"total_cards": 0, "due_today": 0, "new_today": 0}
    try:
        import requests
        def call(action, **params):
            r = requests.post(ANKI_CONNECT_URL,
                              json={"action": action, "version": 6, "params": params},
                              timeout=3)
            r.raise_for_status()
            return r.json().get("result")

        decks = call("deckNamesAndIds") or {}
        stats["decks"] = len(decks)
        # Total cards across all decks
        try:
            counts = call("getDeckStats", decks=decks) or {}
            stats["total_cards"] = sum(d.get("new_count", 0) + d.get("learn_count", 0)
                                       + d.get("review_count", 0)
                                       for d in counts.values())
        except Exception:
            pass
        # Due today: review + new
        try:
            due_ids = call("findCards", query="is:due") or []
            stats["due_today"] = len(due_ids)
        except Exception:
            pass
        try:
            new_ids = call("findCards", query="is:new") or []
            stats["new_today"] = len(new_ids)
        except Exception:
            pass
    except Exception:
        stats["anki_up"] = False
    else:
        stats["anki_up"] = True
    return stats


def read_status():
    try:
        with open(STATUS_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return "STATUS.txt missing"


def build_html(modules, stats, status_text):
    completion_count = sum(1 for m in modules if m["completed"])
    total_count = len(modules)
    pct = int((completion_count / total_count) * 100) if total_count > 0 else 0
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    anki_state = "🟢 live" if stats.get("anki_up") else "⚪ Anki offline"
    status_line = "✅ On Track" if pct > 20 else "⚡ Just Started"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mira's DevOps Bootcamp Dashboard</title>
<style>
* {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; box-sizing: border-box; }}
body {{ background: #0d1117; color: #c9d1d9; padding: 2rem; }}
.container {{ max-width: 1000px; margin: 0 auto; }}
h1 {{ color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 0.5rem; }}
.sub {{ color: #8b949e; margin: 0.5rem 0 1.5rem; }}
.stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.5rem; margin: 1.5rem 0; }}
.stat-card {{ background: #161b22; padding: 1.5rem; border-radius: 8px; border: 1px solid #30363d; text-align: center; }}
.stat-card h3 {{ color: #8b949e; font-weight: 400; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; }}
.stat-card .value {{ font-size: 2.2rem; font-weight: 700; color: #f0f6fc; margin-top: 0.5rem; }}
.progress-bar {{ background: #30363d; height: 2rem; border-radius: 1rem; overflow: hidden; margin: 1.5rem 0; }}
.progress-fill {{ background: linear-gradient(90deg, #238636, #2ea043); height: 100%; width: {pct}%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; }}
.module-list {{ background: #161b22; border-radius: 8px; border: 1px solid #30363d; overflow: hidden; margin: 1.5rem 0; }}
.module-item {{ display: flex; justify-content: space-between; padding: 0.6rem 1.5rem; border-bottom: 1px solid #21262d; }}
.module-item:last-child {{ border-bottom: none; }}
.module-item .status {{ font-weight: 700; }}
.done {{ color: #3fb950; }} .pending {{ color: #f0883e; }}
.status-box {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 1rem 1.5rem; margin: 1.5rem 0; white-space: pre-wrap; font-family: Consolas, monospace; font-size: 0.85rem; }}
.footer {{ margin-top: 2rem; color: #8b949e; font-size: 0.85rem; text-align: center; border-top: 1px solid #30363d; padding-top: 1rem; }}
</style>
</head>
<body>
<div class="container">
    <h1>🚀 Mira's DevOps Bootcamp — Progress Dashboard</h1>
    <p class="sub">Student: Visakan · Teacher: Mira · Last updated: {now} · Anki: {anki_state}</p>

    <div class="stats-grid">
        <div class="stat-card"><h3>Topics Completed</h3><div class="value">{completion_count}/{total_count}</div></div>
        <div class="stat-card"><h3>Overall Progress</h3><div class="value">{pct}%</div></div>
        <div class="stat-card"><h3>Anki Flashcards</h3><div class="value">{stats['total_cards']}</div></div>
        <div class="stat-card"><h3>Due Today</h3><div class="value">{stats['due_today']}</div></div>
        <div class="stat-card"><h3>Status</h3><div class="value" style="font-size:1.1rem;">{status_line}</div></div>
    </div>

    <div class="progress-bar"><div class="progress-fill" style="width:{pct}%;">{pct}%</div></div>

    <h2 style="margin:1.5rem 0 0.5rem;">📚 Topic Roadmap</h2>
    <div class="module-list">
        <div style="display:flex; justify-content:space-between; padding:0.5rem 1.5rem; background:#0d1117; font-weight:600; color:#8b949e; border-bottom:2px solid #30363d;">
            <span>Topic</span><span>Status</span>
        </div>
"""
    for mod in modules:
        cls = "done" if mod["completed"] else "pending"
        disp = "✅ Done" if mod["completed"] else "⏳ Pending"
        html += f"""        <div class="module-item"><span>{mod['title']}</span><span class="status {cls}">{disp}</span></div>
"""
    html += """    </div>

    <h2 style="margin:1.5rem 0 0.5rem;">🧭 Current Status</h2>
"""
    html += f'    <div class="status-box">{status_text}</div>\n'
    html += f"""    <div class="footer">
        Built automatically by Mira (Hermes Agent) · <a href="https://github.com/{GITHUB_USERNAME}/{REPO_NAME}" target="_blank" style="color:#58a6ff;">View on GitHub</a>
    </div>
</div>
</body>
</html>
"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Dashboard built at {INDEX_PATH} ({completion_count}/{total_count} topics, {pct}%)")


if __name__ == "__main__":
    modules = parse_roadmap()
    stats = get_anki_stats()
    status_text = read_status()
    build_html(modules, stats, status_text)
