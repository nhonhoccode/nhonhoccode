#!/usr/bin/env python3
"""Generate an animated, camo-proof SVG hero banner with the avatar baked in as a data URI."""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
avatar_bytes = (ROOT / "assets" / "avatar.jpg").read_bytes()
avatar_b64 = base64.b64encode(avatar_bytes).decode()
data_uri = f"data:image/jpeg;base64,{avatar_b64}"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 300" role="img" aria-label="Vo Trong Nhon - DevOps Engineer" font-family="Segoe UI, Helvetica, Arial, sans-serif">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D1117"/>
      <stop offset="55%" stop-color="#0F2C4A"/>
      <stop offset="100%" stop-color="#16324F"/>
      <animate attributeName="x2" values="100%;80%;100%" dur="16s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2C9EF7" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#2C9EF7" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ring" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#58A6FF"/>
      <stop offset="100%" stop-color="#2C9EF7"/>
    </linearGradient>
    <clipPath id="av"><circle cx="170" cy="150" r="92"/></clipPath>
  </defs>

  <rect x="0" y="0" width="1200" height="300" fill="url(#bg)"/>
  <rect x="0" y="0" width="1200" height="300" fill="url(#glow)"/>

  <!-- drifting glow blobs -->
  <g opacity="0.6">
    <circle cx="980" cy="60" r="150" fill="url(#glow)">
      <animateTransform attributeName="transform" type="translate" values="0 0; 22 14; 0 0" dur="18s" repeatCount="indefinite"/>
    </circle>
    <circle cx="600" cy="270" r="120" fill="url(#glow)">
      <animateTransform attributeName="transform" type="translate" values="0 0; -18 -10; 0 0" dur="22s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- node-graph / circuit motif behind text -->
  <g stroke="#1E4A6B" stroke-width="1.2" fill="none" opacity="0.55">
    <line x1="430" y1="70" x2="560" y2="120"/>
    <line x1="560" y1="120" x2="700" y2="80"/>
    <line x1="700" y1="80" x2="860" y2="140"/>
    <line x1="860" y1="140" x2="1010" y2="100"/>
    <line x1="560" y1="120" x2="640" y2="220"/>
    <line x1="640" y1="220" x2="800" y2="245"/>
    <line x1="800" y1="245" x2="860" y2="140"/>
    <line x1="800" y1="245" x2="1010" y2="100"/>
    <line x1="1010" y1="100" x2="1120" y2="200"/>
    <line x1="860" y1="140" x2="1120" y2="200"/>
    <line x1="500" y1="205" x2="640" y2="220"/>
  </g>
  <g fill="#2C9EF7">
    <circle cx="430" cy="70" r="3.5"><animate attributeName="opacity" values="0.3;1;0.3" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="560" cy="120" r="4"><animate attributeName="opacity" values="1;0.3;1" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="700" cy="80" r="3.5"><animate attributeName="opacity" values="0.4;1;0.4" dur="6s" repeatCount="indefinite"/></circle>
    <circle cx="860" cy="140" r="4.5"><animate attributeName="opacity" values="1;0.4;1" dur="4.5s" repeatCount="indefinite"/></circle>
    <circle cx="1010" cy="100" r="3.5"><animate attributeName="opacity" values="0.3;1;0.3" dur="5.5s" repeatCount="indefinite"/></circle>
    <circle cx="640" cy="220" r="4"><animate attributeName="opacity" values="0.5;1;0.5" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="800" cy="245" r="3.5"><animate attributeName="opacity" values="1;0.4;1" dur="6.5s" repeatCount="indefinite"/></circle>
    <circle cx="1120" cy="200" r="4"><animate attributeName="opacity" values="0.4;1;0.4" dur="4.8s" repeatCount="indefinite"/></circle>
  </g>

  <!-- avatar -->
  <circle cx="170" cy="150" r="99" fill="none" stroke="url(#ring)" stroke-width="3" opacity="0.9"/>
  <image x="78" y="58" width="184" height="184" clip-path="url(#av)" preserveAspectRatio="xMidYMid slice" xlink:href="{data_uri}"/>
  <circle cx="170" cy="150" r="92" fill="none" stroke="#0D1117" stroke-width="2" opacity="0.6"/>

  <!-- text block -->
  <text x="310" y="128" fill="#FFFFFF" font-size="48" font-weight="800" letter-spacing="0.5">Vo Trong Nhon</text>
  <text x="312" y="168" fill="#58A6FF" font-size="21" font-weight="600">DevOps Engineer &#183; MLOps &#183; AI Apps &#183; Full-stack</text>
  <rect x="313" y="184" width="360" height="3" rx="1.5" fill="url(#ring)"/>
  <text x="313" y="232" fill="#5B7186" font-size="15" font-family="Consolas, Menlo, monospace">Docker &#183; Proxmox &#183; MLflow &#183; Airflow &#183; FastAPI &#183; Next.js &#183; Prometheus</text>
</svg>
'''

out = ROOT / "assets" / "banner.svg"
out.write_text(svg, encoding="utf-8")
print(f"wrote {out} ({len(svg)} chars, avatar {len(avatar_b64)} b64 chars)")
