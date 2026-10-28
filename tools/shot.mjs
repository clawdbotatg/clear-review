// shot.mjs <in.html> <out.png>: full-page screenshot, 860 px wide page
import { chromium } from "playwright-core";
import { readdirSync } from "node:fs";
import { homedir } from "node:os";
import { resolve } from "node:path";
const cache = homedir() + "/Library/Caches/ms-playwright";
const shell = readdirSync(cache).filter((d) => d.startsWith("chromium_headless_shell-")).sort().reverse()[0];
const b = await chromium.launch({ executablePath: `${cache}/${shell}/chrome-headless-shell-mac-arm64/chrome-headless-shell` });
const p = await b.newPage({ viewport: { width: 908, height: 400 }, deviceScaleFactor: 2 });
await p.goto("file://" + resolve(process.argv[2]));
await p.screenshot({ path: process.argv[3], fullPage: true });
await b.close();
