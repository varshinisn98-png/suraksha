"""
Python HTTP Web Server for Custom Glassmorphic Women Safety Intelligence Web App.
Serves web/ on http://localhost:8502
"""
import http.server
import socketserver
import os
import json
import pandas as pd

PORT = 8502
DIRECTORY = "web"

def export_json():
    df_path = os.path.join("data", "processed", "featured_labeled_dataset.parquet")
    if os.path.exists(df_path):
        df = pd.read_parquet(df_path)
        records = df.to_dict(orient="records")
        out_json = os.path.join(DIRECTORY, "data.json")
        with open(out_json, "w") as f:
            json.dump(records, f)
        print(f"Exported {len(records)} dataset records to {out_json}")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    os.makedirs(DIRECTORY, exist_ok=True)
    export_json()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Women Safety Intelligence Custom Web App running at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
