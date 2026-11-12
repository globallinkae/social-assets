# Global Link social assets — rules for the automatic scheduler

- Channels (Buffer org 6aeb932a20f16df4a027d5db, timezone Asia/Dubai): Instagram 6aec22f9e29c69a1716b286c · LinkedIn 6aec237be29c69a1716b2bb7 · TikTok 6aec2410e29c69a1716b2f98.
- One post per channel per day at 09:00 Asia/Dubai (dueAt "YYYY-MM-DDT09:00:00+04:00", mode customScheduled, schedulingType automatic).
- Different content per channel on the same day. TikTok: video only, max 5 hashtags. Every video must contain music (all files in media/ do).
- Buffer free plan: max 10 scheduled posts at a time. Schedule only entries whose date is within the next 3 days, oldest first, and stop when the scheduled count reaches 10.
- Asset URL = https://raw.githubusercontent.com/globallinkae/social-assets/main/media/<asset>.
- Instagram image → metadata.instagram {type: "post", shouldShareToFeed: true}; Instagram video → {type: "reel", shouldShareToFeed: true}. TikTok video → metadata.tiktok {title}. LinkedIn: no metadata needed.
- After creating a post, set its plan.json entry status to "scheduled" and add "buffer_id"; commit and push plan.json.
- Never create, edit or delete anything not in plan.json. Never post prices, Al Falaj, Urdu, "we provide e-invoicing", mrcleaner.pk, the private office's name, or real client staff names.
- Posting continues until Abrar says stop.
- kind "pdf" (LinkedIn only): attach the PDF from media/ as a document post. kind "carousel" (Instagram): the entry carries "assets" (2–10 images, in order) → one post with all of them, metadata.instagram {type: "post", shouldShareToFeed: true}.
- Look 2 (from 16 Nov): assets under media/look2/ — Flow scenes with our real screens, number cards, Arabic day on Saturdays, pillars by weekday (Mon tip · Tue client story · Wed product screen · Thu industry · Fri behind the build · Sat Arabic · Sun proof number). People in the scenes are illustrative and are never described as clients or staff.
