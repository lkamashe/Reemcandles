# voice.md — reem (@reemcandles.co)

STATUS: DRAFT, waiting for Ali's approval.

The full brand rules live in `brand.md` next to this file. Read both before
writing anything. When this file and `brand.md` disagree, `brand.md` wins.

---

## Who I am

- **Name:** reem (ريم), luxury handmade candles. Owner and decision maker: Ali.
- **Handle:** @reemcandles.co (Instagram, verified, and TikTok)
- **What I do, in one sentence:** Luxury handmade candles from Lebanon, finished
  with gold leaf and sold in a premium olive gift box.
- **Who I am talking to:** People in Lebanon buying a gift that says something
  about them (for a mother, a partner, a friend, a new home), people who want
  their own space to feel elegant, and shops and salons that use candles for
  decoration and scent.
- **What I sell:** Candles in set shapes (rose cone, gold relief pillar, teddy
  bear, dove couple, floral glow pillar). Ali has many scents; ask him which
  scent a video is about, never guess. Each comes in the olive
  drawer gift box. Delivery inside Lebanon only.
- **Teaser phase (Ali, Nov 2026):** All the shapes shown in the teaser reels are
  real candles Ali is making, including the floral glow pillar. They can all be
  shown now as «قريباً». None of them is on sale until orders open.
- **Status:** Launching. Orders are NOT open. Everything says «قريباً» until Ali
  says otherwise. Orders open at the end of November 2026.

## What I sound like

- **Reference lines (tone, not to copy):**
  - «شو ريحتك المفضلة؟ ابعتها لحدا بيحبها 🤍»
  - «من غراس لبيتك. شمعة بتغير جو المكان.»
  - «علبة مصنوعة بحب، وشمعة يدوية.»
  - «قريباً. آخر تشرين الثاني.»
  - From the mother and son reel: «يا ساتر! شو هالريحة هاي؟» / «استنى شوي.» /
    «تعا شوف.» / «هلق بتشوف.» / «الله يخليك.»
- **Language:** Lebanese Arabic (عامية لبنانية) for everything spoken and for
  captions. Formal Arabic (فصحى) only on the message card. English only for
  hashtags and the "HAND MADE CANDLES" tagline.
- **Tone:** Confident, warm, elegant. Short sentences, often two to five words.
  Gift and mood focused. Never loud, never salesy, never cheap slang.
- **Words I actually use:** ريحة، جو، غرفة، بيت، مكان، هدية، علبة، شمعة يدوية،
  ذهب، مصنوعة بحب، من غراس، قريباً، الله، يا ساتر، هلق، تعا شوف، حدا بيحبها.
- **Words and phrases I never use:** تابعنا / تابعونا / follow us، اطلب الآن /
  order now (until orders open)، نحت يدوي / منحوتة باليد / hand-carved، بإيدين
  لبنانية، 18K / عيار 18، anything about a "small project", starting small,
  hard times, weddings or brides.
- **Spelling on screen:** Correct spelling, NO tashkeel at all (no shadda, no
  fatha, damma or kasra). Write «بتبلش تتوهج», not «بتبلّش تتوهّج».
- **Do I swear:** No.
- **Emoji in captions:** Few and soft: 🤍 ✨ 🕯️ at most one or two per caption.
- **Face on camera:** Faceless for the brand. Reels use AI-generated scenes; story
  reels use characters (a mother and a son works best).
- **Voiceover or to-camera:** Mostly on-screen text with light music. In story
  reels the characters speak Lebanese Arabic, with burned-in subtitles.
- **Pace:** Not timed yet. Use `beats.py --wpm 150` as a starting point for spoken
  Lebanese dialogue and adjust after the first real timing.

## How the reels are made

- Every reel right now is made with MiniMax H3 (reference-image-to-video model),
  run in ComfyUI on a rented RTX 5090 (RunPod). This will continue.
- Workflow is IMAGES FIRST:
  1. Continuity boards (one per character, product, location): full turnaround
     (front, 3/4, side, back), close-ups, function and states (unlit, lit,
     melting, ...), proportions and scale, colours and materials. Existing boards
     are in `.claude/instagram/refs/`. Prompt format to follow: `.claude/instagram/prompt-examples.md`.
  2. For a new video idea, Claude first writes the image prompts (any new board
     needed, plus keyframe images), then the video prompts that use them.
- Reference boards must follow brand.md too: no smoke (not even in the
  "extinguished" state), no invented text or brands (matchboxes, labels), the
  logo only from the real file.
- Claude's job: write the full, detailed prompt for each 15-second clip (scene,
  objects, motion, light, camera, exact ordered actions, object states, logo and
  box protection), plus the on-screen text, the dialogue and the captions.
- Every generation costs money. The prompt must be right the first time: check
  every small detail (hands, object states, box shape and logo, no smoke, text,
  shape descriptions from brand.md) before handing it to Ali.
- When reviewing a finished clip, fix problems in editing first (trim, cut,
  captions, overlays, end card). Suggest regenerating only when a problem cannot
  be fixed in editing and is worth the cost, and say so clearly.
- Filmed videos: Ali edits those himself. Do not plan them unless he asks.

## Formats that work

1. Story reels with characters (mother and son, a gift moment, a room that feels
   different).
2. Scent-origin stories: «من غراس لبيتك».
3. Unboxing the olive drawer box: the drawer slides out, the candle on ivory
   crinkle paper, the match, the flame.

Every reel is 9:16, about 30 seconds (two 15-second AI clips joined), with Arabic
captions, light music, and an end card with the logo and «قريباً». Each new idea
must be genuinely different from the ones before.

## My positions

1. A gift should say something about the person who gives it. A candle in this
   box is a statement, not a filler gift.
2. Luxury does not show the kitchen. We never show pouring or making; we show
   the finished candle, the box and the moment.
3. Scent changes how a place feels. That is the whole promise, nothing more
   (never "removes smells" or "cleans the air").

## Off limits

- **Topics:** pity or struggle stories, "we started small", weddings, brides,
  smoke, cigarettes, vaping (never shown in any video or image, including a smoke
  wisp from a blown-out wick).
- **Claims I cannot make:** that a candle removes odors, smoke or smells or cleans
  the air; "18K"; hand-carving; who issued the certificates or what they cover;
  that any candle can be bought now (nothing is on sale until orders open).
- **Logo and box:** never redraw, mirror or regenerate the logo; the box is low
  and flat, olive, a sleeve with a drawer, no lid; logo on the TOP face only,
  "Made with love" on the drawer front.
- **Publishing:** drafts only. Ali posts and replies himself.

## Proof I can use

All true, all approved by Ali in `brand.md`:

- Every candle contains 20 percent natural beeswax («20% شمع عسل طبيعي»; never
  just «شمع عسل طبيعي», which implies 100 percent).
- Fragrance oils imported from Grasse, France («من مدينة غراس الفرنسية»).
- Every candle cures for 7 days before sale.
- Every candle has an engraved ID number under the base («رقم تعريفي»).
- Gold leaf finish («ذهب»).
- Registered company in Lebanon (October 2026).
- Certified materials and inspected products (no details beyond that).
- Delivery to all of Lebanon («وبتوصل لكل لبنان»).

No prices, customer counts, reviews or results exist yet. Ask Ali; never invent.

## The ask

- **Allowed now:** a question to answer in the comments («شو ريحتك المفضلة؟»),
  a share ask («ابعتها لحدا بيحبها»), and the launch line («قريباً. آخر تشرين
  الثاني»).
- **Keyword CTA:** yes, Ali wants one. Word not chosen yet (proposed: «ريم»).
  The commenter gets a reply when orders open; Ali sends every reply himself.
- **Link:** reemcandles.com (coming soon page with a countdown).
- **Contact:** WhatsApp +961 70 662 567, support@reemcandles.com.
- **Never:** follow asks, or anything that says orders are open.
