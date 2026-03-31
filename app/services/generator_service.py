import random
from typing import List


# ---------------------------------------------------------------------------
# Caption generator
# ---------------------------------------------------------------------------

CAPTION_TEMPLATES = {
    "motivational": [
        "Every day is a new opportunity to {topic}. Keep pushing! 💪",
        "The secret to {topic}? Never stop. Never settle. 🔥",
        "Greatness in {topic} isn't born — it's built, rep by rep. ⚡",
        "Your {topic} journey is just beginning. Make it legendary. 🌟",
        "Consistency in {topic} beats talent every single time. 🏆",
    ],
    "cool": [
        "Yeah, I'm into {topic}. What about it? 😎",
        "{topic} hits different when you're built different. ✨",
        "Not everyone understands {topic}. That's okay. 🤷",
        "Living for {topic} and not apologizing for it. 🚀",
        "{topic} season. Always. No cap. 💯",
    ],
    "funny": [
        "Me pretending I know what I'm doing with {topic} 😂",
        "{topic}? More like {topic}-ing my patience 😅",
        "My therapist said I need a hobby. I chose {topic}. Still in therapy. 😭",
        "Warning: May spontaneously talk about {topic} at any time. 🤣",
        "{topic} by day, questioning my life choices by night. 😂",
    ],
    "professional": [
        "Dedicated to mastering {topic} one step at a time.",
        "Building expertise in {topic} through consistent effort and learning.",
        "Passionate about {topic} and its potential to create real impact.",
        "Today's focus: {topic}. Because growth never stops.",
        "Sharing insights on {topic} — because knowledge is meant to be shared.",
    ],
    "casual": [
        "just out here doing my {topic} thing 🙂",
        "low-key obsessed with {topic} rn",
        "{topic} and good vibes only ✌️",
        "another day, another {topic} moment",
        "simple life, big {topic} energy 🌿",
    ],
    "aesthetic": [
        "In the quiet spaces where {topic} lives. 🌸",
        "Soft mornings and {topic} thoughts. ☁️",
        "There's art in {topic} if you look close enough. 🎨",
        "Golden hour and {topic} feelings. 🌅",
        "A moment for {topic}. A moment for me. 🤍",
    ],
    "neutral": [
        "Exploring {topic} one post at a time.",
        "Sharing my {topic} journey with you all.",
        "All about {topic} — join the ride!",
        "Today's highlight: {topic}.",
        "Here's to {topic} and everything it brings.",
    ],
}


def generate_captions(topic: str, tone: str = "neutral", count: int = 5) -> List[str]:
    templates = CAPTION_TEMPLATES.get(tone, CAPTION_TEMPLATES["neutral"])
    pool = templates * ((count // len(templates)) + 1)
    selected = random.sample(pool, min(count, len(pool)))
    return [t.format(topic=topic) for t in selected]


# ---------------------------------------------------------------------------
# Hashtag generator
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Niche hashtag library — ordered by popularity (most popular first)
# ---------------------------------------------------------------------------

NICHE_HASHTAGS: dict[str, list[str]] = {
    "fitness": [
        "#fitness", "#gym", "#workout", "#fitlife", "#bodybuilding",
        "#fitnessmotivation", "#training", "#health", "#gains", "#strong",
        "#nopainnogain", "#gymlife", "#cardio", "#weightlifting", "#fit",
        "#personaltrainer", "#fitfam", "#exercise", "#strengthtraining", "#muscle",
        "#grind", "#healthylifestyle", "#fitnessinspiration", "#abs", "#gymrat",
        "#crossfit", "#running", "#yoga", "#nutrition", "#athleticperformance",
    ],
    "food": [
        "#food", "#foodie", "#foodporn", "#instafood", "#foodphotography",
        "#yummy", "#delicious", "#cooking", "#recipe", "#homemade",
        "#foodlover", "#chef", "#tasty", "#eat", "#foodblogger",
        "#foodstagram", "#healthyfood", "#dinner", "#lunch", "#breakfast",
        "#baking", "#dessert", "#vegetarian", "#vegan", "#streetfood",
        "#italianfood", "#asianfood", "#pasta", "#pizza", "#foodart",
    ],
    "travel": [
        "#travel", "#wanderlust", "#travelgram", "#instatravel", "#explore",
        "#adventure", "#travelblogger", "#vacation", "#trip", "#worldtravel",
        "#travelphotography", "#backpacking", "#nomad", "#passport", "#journey",
        "#discover", "#roadtrip", "#traveltheworld", "#solotravel", "#landscape",
        "#travelholic", "#tourism", "#holiday", "#getaway", "#globetrotter",
        "#traveladdict", "#nature", "#mountains", "#beach", "#travelinspiration",
    ],
    "fashion": [
        "#fashion", "#style", "#ootd", "#outfit", "#streetstyle",
        "#fashionblogger", "#instafashion", "#trendy", "#lookoftheday", "#fashionista",
        "#wiwt", "#clothing", "#model", "#outfitoftheday", "#styleinspo",
        "#fashionweek", "#luxury", "#streetwear", "#mensfashion", "#womensfashion",
        "#vintage", "#aesthetic", "#brand", "#designer", "#fashionphotography",
        "#chic", "#casual", "#collection", "#sustainable", "#fashiontrends",
    ],
    "beauty": [
        "#beauty", "#makeup", "#skincare", "#makeupartist", "#glam",
        "#beautyblogger", "#cosmetics", "#skincareroutine", "#selfcare", "#glow",
        "#makeuptutorial", "#foundation", "#eyeshadow", "#lips", "#beautytips",
        "#natural", "#gorgeous", "#skingoals", "#glowing", "#beautyhacks",
        "#crueltyfree", "#organicbeauty", "#antiaging", "#serum", "#moisturizer",
        "#glassskin", "#nofilter", "#makeuplover", "#beauty", "#selfcaresunday",
    ],
    "engineering": [
        "#engineering", "#engineer", "#engineeringlife", "#mechanicalengineering",
        "#civilengineering", "#electricalengineering", "#softwareengineering",
        "#engineerstudent", "#engineeringmemes", "#stem",
        "#technology", "#innovation", "#design", "#robotics", "#automation",
        "#coding", "#programming", "#tech", "#cad", "#construction",
        "#architecture", "#structural", "#aerospace", "#chemical", "#biomedical",
        "#engineeringdesign", "#maker", "#3dprinting", "#arduino", "#electronics",
    ],
    "technology": [
        "#technology", "#tech", "#coding", "#programming", "#developer",
        "#softwareengineer", "#ai", "#artificialintelligence", "#machinelearning",
        "#data", "#cybersecurity", "#startup", "#innovation", "#digital",
        "#python", "#javascript", "#webdev", "#webdevelopment", "#app",
        "#iot", "#blockchain", "#cloud", "#devops", "#opensource",
        "#techlife", "#gadgets", "#coding", "#computer", "#futuretech",
    ],
    "photography": [
        "#photography", "#photographer", "#photooftheday", "#photo", "#portrait",
        "#naturephotography", "#streetphotography", "#landscapephotography", "#lightroom", "#canon",
        "#nikon", "#sony", "#filmphotography", "#blackandwhite", "#golden",
        "#composition", "#shutterspeed", "#fstop", "#bokeh", "#exposure",
        "#photographylovers", "#instagood", "#pictureoftheday", "#capturethemoment", "#visualsoflife",
        "#rawphotography", "#analogphotography", "#mobilephotography", "#dronephotography", "#edit",
    ],
    "business": [
        "#business", "#entrepreneur", "#startup", "#marketing", "#success",
        "#digitalmarketing", "#leadership", "#mindset", "#motivation", "#hustle",
        "#smallbusiness", "#branding", "#growthhacking", "#socialmedia", "#ecommerce",
        "#ceo", "#workhard", "#goals", "#money", "#investment",
        "#businessowner", "#selfmade", "#passive income", "#financialfreedom", "#network",
        "#b2b", "#sales", "#consulting", "#productmanagement", "#agency",
    ],
    "music": [
        "#music", "#musician", "#song", "#musicproducer", "#hiphop",
        "#rap", "#rnb", "#pop", "#indie", "#rock",
        "#guitar", "#piano", "#drums", "#singer", "#songwriter",
        "#newmusic", "#musicvideo", "#spotify", "#studio", "#beats",
        "#musiclife", "#artist", "#concert", "#livemusic", "#dj",
        "#producer", "#mixtape", "#playlist", "#musiclover", "#vibes",
    ],
    "art": [
        "#art", "#artist", "#artwork", "#painting", "#drawing",
        "#illustration", "#digitalart", "#sketch", "#creative", "#design",
        "#contemporaryart", "#abstractart", "#watercolor", "#acrylic", "#oilpainting",
        "#artoftheday", "#artgallery", "#fineart", "#artstudio", "#instaart",
        "#artistsoninstagram", "#artcommunity", "#artlovers", "#modernart", "#streetart",
        "#graphicdesign", "#typography", "#poster", "#comics", "#animation",
    ],
    "nature": [
        "#nature", "#naturephotography", "#wildlife", "#landscape", "#outdoors",
        "#hiking", "#mountains", "#forest", "#ocean", "#sunset",
        "#earth", "#sky", "#trees", "#camping", "#nationalpark",
        "#wildlifephotography", "#green", "#flowers", "#macro", "#birds",
        "#conservation", "#ecotourism", "#sustainableliving", "#earthday", "#wilderness",
        "#waterfall", "#lake", "#river", "#beach", "#naturelover",
    ],
    "education": [
        "#education", "#learning", "#student", "#study", "#school",
        "#college", "#university", "#knowledge", "#teaching", "#teacher",
        "#studymotivation", "#studygram", "#edtech", "#elearning", "#onlinelearning",
        "#books", "#reading", "#science", "#math", "#history",
        "#studytips", "#campus", "#graduation", "#scholarship", "#research",
        "#homework", "#notes", "#studyabroad", "#acadmics", "#lifelonglearning",
    ],
    "motivation": [
        "#motivation", "#inspiration", "#mindset", "#positivity", "#success",
        "#goals", "#hustle", "#grind", "#nevergiveup", "#believe",
        "#motivationalquotes", "#dailymotivation", "#selfdevelopment", "#growth", "#winning",
        "#lifequotes", "#successmindset", "#discipline", "#focus", "#consistency",
        "#personaldevelopment", "#selfimprovement", "#positivevibes", "#blessed", "#grateful",
        "#mentalhealth", "#wellness", "#happy", "#mindfulness", "#abundance",
    ],
    "gaming": [
        "#gaming", "#gamer", "#videogames", "#game", "#ps5",
        "#xbox", "#pcgaming", "#twitch", "#streamer", "#esports",
        "#playstation", "#nintendo", "#fortnite", "#minecraft", "#cod",
        "#gamingcommunity", "#gamingsetup", "#gameplay", "#rpg", "#fps",
        "#retrogaming", "#mobilegaming", "#gamedev", "#indiegame", "#gaming",
        "#controller", "#gamedevelopment", "#gaminglife", "#mmorpg", "#gamers",
    ],
    "sports": [
        "#sports", "#athlete", "#sport", "#football", "#basketball",
        "#soccer", "#cricket", "#tennis", "#swimming", "#running",
        "#sportslife", "#sportsmotivation", "#teamwork", "#champion", "#winning",
        "#training", "#performance", "#competition", "#game", "#league",
        "#sportsmanship", "#playhard", "#dedication", "#fit", "#active",
        "#outdoorsports", "#extremesports", "#coaching", "#sportsnutrition", "#recovery",
    ],
}

# Trending general tags mixed in — only a handful, relevant to social growth
TRENDING_TAGS = [
    "#viral", "#trending", "#explore", "#reels", "#reelsvideo",
    "#content", "#creator", "#daily", "#instagood", "#instadaily",
]


def _slug(text: str) -> str:
    return text.lower().replace(" ", "")


def _match_niche(topic: str) -> str | None:
    topic_lower = topic.lower()
    keyword_map = {
        "fitness":     ["fitness", "gym", "workout", "exercise", "training", "bodybuilding", "crossfit", "weightlifting"],
        "food":        ["food", "cooking", "recipe", "eat", "chef", "baking", "restaurant", "cuisine", "meal", "diet"],
        "travel":      ["travel", "trip", "vacation", "journey", "explore", "adventure", "tourism", "holiday", "backpack"],
        "fashion":     ["fashion", "style", "outfit", "clothing", "wear", "dress", "ootd", "streetstyle"],
        "beauty":      ["beauty", "makeup", "skincare", "cosmetic", "glow", "skin", "glam", "lipstick"],
        "engineering": ["engineer", "engineering", "mechanical", "civil", "electrical", "structural", "cad", "robotics", "automation"],
        "technology":  ["tech", "technology", "coding", "programming", "software", "developer", "ai", "machine learning", "data", "cyber", "blockchain", "cloud"],
        "photography": ["photo", "photograph", "camera", "picture", "shot", "lens", "lightroom", "canon", "nikon"],
        "business":    ["business", "entrepreneur", "startup", "marketing", "brand", "sales", "ecommerce", "leadership"],
        "music":       ["music", "song", "singer", "guitar", "piano", "rap", "hiphop", "producer", "dj", "band"],
        "art":         ["art", "artist", "painting", "drawing", "illustration", "sketch", "design", "creative"],
        "nature":      ["nature", "outdoor", "landscape", "mountain", "ocean", "forest", "wildlife", "hiking", "camping"],
        "education":   ["education", "learning", "student", "study", "school", "college", "university", "teacher", "tutor"],
        "motivation":  ["motivation", "inspiration", "mindset", "positivity", "goals", "success", "discipline", "growth"],
        "gaming":      ["gaming", "gamer", "game", "videogame", "playstation", "xbox", "nintendo", "twitch", "esport"],
        "sports":      ["sport", "sports", "football", "basketball", "soccer", "cricket", "tennis", "athlete", "league"],
    }
    for niche, keywords in keyword_map.items():
        if any(kw in topic_lower for kw in keywords):
            return niche
    return None


def _build_topic_tags(topic: str) -> list[str]:
    """Generate topic-specific hashtag variations when no niche matches."""
    slug = _slug(topic)
    variations = [
        f"#{slug}",
        f"#{slug}life",
        f"#{slug}lover",
        f"#{slug}gram",
        f"#{slug}daily",
        f"#{slug}community",
        f"#{slug}tips",
        f"#{slug}motivation",
        f"#{slug}inspiration",
        f"#{slug}goals",
        f"#{slug}expert",
        f"#{slug}content",
        f"#{slug}creator",
        f"#{slug}101",
        f"#{slug}facts",
        f"#{slug}world",
        f"#{slug}culture",
        f"#{slug}learning",
        f"#{slug}skills",
        f"#{slug}journey",
    ]
    return variations


def generate_hashtags(topic: str, tone: str = "neutral", count: int = 30) -> list[str]:
    niche = _match_niche(topic)
    slug = _slug(topic)

    if niche:
        pool = NICHE_HASHTAGS[niche]
    else:
        # Build topic-specific tags — no generic Instagram filler
        pool = _build_topic_tags(topic)

    # Ensure the exact topic tag is always first
    exact_tag = f"#{slug}"
    result: list[str] = []
    if exact_tag in pool:
        result.append(exact_tag)
        pool = [t for t in pool if t != exact_tag]
    else:
        result.append(exact_tag)

    # Fill from pool (already ordered by popularity)
    for tag in pool:
        if tag not in result:
            result.append(tag)
        if len(result) >= count:
            break

    # Pad with trending tags only if still short (and they fit the count)
    if len(result) < count:
        for tag in TRENDING_TAGS:
            if tag not in result:
                result.append(tag)
            if len(result) >= count:
                break

    return result[:count]


# ---------------------------------------------------------------------------
# Bio generator
# ---------------------------------------------------------------------------

BIO_TEMPLATES = {
    "motivational": [
        "On a mission to master {topic} 💪 | Never giving up | DM for collabs",
        "Chasing greatness in {topic} every single day 🔥 | Coach | Creator",
        "{topic} enthusiast | Turning passion into purpose | Let's connect 🌟",
        "Built different. Powered by {topic}. 💯 | Helping others level up",
        "Your daily dose of {topic} motivation ⚡ | Follow the journey",
    ],
    "cool": [
        "{topic} by day. Dreams by night. 😎 | Just doing my thing",
        "Living the {topic} life unapologetically 🤟 | Not for everyone",
        "Into {topic}. Into vibes. Into life. ✨ | DMs open",
        "{topic} is my aesthetic. Deal with it. 💅 | Creator & storyteller",
        "lowkey obsessed with {topic} 🫶 | come vibe",
    ],
    "professional": [
        "{topic} professional | Sharing expertise daily | Open to partnerships",
        "Specialist in {topic} | Content creator | Helping brands grow",
        "Passionate about {topic} | 3+ years of experience | Let's work",
        "{topic} educator & creator | Knowledge is power | Link below",
        "Building in {topic} | Sharing the journey | Entrepreneur",
    ],
    "casual": [
        "just a person who loves {topic} 🙂 | vibes only",
        "here for {topic} and good times ✌️ | no pressure",
        "{topic} nerd. proud of it. | simple life",
        "really into {topic} lately | come say hi",
        "{topic} and coffee. that's the whole bio.",
    ],
    "aesthetic": [
        "∙ {topic} lover ∙ chasing light ∙ living slow 🌸",
        "soft life. {topic} moments. golden hours. 🌅",
        "finding beauty in {topic} every day 🤍",
        "{topic} | art | stillness | 🌿",
        "in love with {topic} and the quiet things ☁️",
    ],
    "neutral": [
        "Sharing my {topic} journey | Follow along!",
        "{topic} creator | Daily posts | DM for collabs",
        "All about {topic} | New post every day",
        "Passionate about {topic} | Let's connect",
        "{topic} content | Authentic & consistent",
    ],
}

BIO_SUFFIXES = [
    "📩 DM for collabs", "👇 Check the link", "🔗 Link in bio",
    "📍 Available worldwide", "✉️ Business: email@domain.com",
]


def generate_bios(topic: str, tone: str = "neutral", count: int = 5) -> List[str]:
    templates = BIO_TEMPLATES.get(tone, BIO_TEMPLATES["neutral"])
    pool = templates * ((count // len(templates)) + 1)
    selected = random.sample(pool, min(count, len(pool)))
    results = [t.format(topic=topic) for t in selected]
    # Add a random suffix to some bios
    for i in range(len(results)):
        if random.random() > 0.5:
            results[i] += f"\n{random.choice(BIO_SUFFIXES)}"
    return results[:count]
