from datetime import datetime, time
from astral import LocationInfo
from astral.sun import sun

LOCATION = LocationInfo(
    name      = "North Augusta",
    region    = "USA",
    timezone  = "America/New_York",
    latitude  = 33.5018,
    longitude = -81.9652,
)
    

#Reccomendation Engine 
#Rule based
RULES = {
 
    # ── SPRING ──────────────────────────────────────────────────────────────
    "spring": {
        "cold": {
            "dawn":    {
                "species": ["Crappie", "Bass"],
                "baits":   [
                    {"bait": "Small Jig (1/16 oz)",    "reason": "slow cold water presentation"},
                    {"bait": "Live Minnow",             "reason": "hard to beat in cold spring water"},
                ],
                "tip": "Cold spring sunrise — crappie staging deep near brush piles."
            },
            "sunrise": {
                "species": ["Crappie"],
                "baits":   [
                    {"bait": "Small Jig (1/16 oz)",    "reason": "target suspended crappie"},
                    {"bait": "Live Minnow",             "reason": "crappie can't resist in cold water"},
                ],
                "tip": "Cold water slows everything down — find the school and stay on it."
            },
            "noon": {
                "species": ["Catfish", "Crappie"],
                "baits":   [
                    {"bait": "Nightcrawler",            "reason": "bottom fish in warmest water of the day"},
                    {"bait": "Small Jig (1/16 oz)",    "reason": "crappie hold deep in cold water"},
                ],
                "tip": "Warmest part of a cold day — fish the deepest structure you can find."
            },
            "dusk": {
                "species": ["Crappie", "Bass"],
                "baits":   [
                    {"bait": "Small Jig",               "reason": "crappie active near dusk"},
                    {"bait": "Jig (1/4 oz)",            "reason": "slow roll for sluggish bass"},
                ],
                "tip": "Temps dropping at dusk — fish are slowing down, slow your presentation too."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "best cold water catfish bait"},
                    {"bait": "Nightcrawler",            "reason": "reliable bottom bait at night"},
                ],
                "tip": "Cold night — catfish are your best bet, fish the bottom slow."
            },
        },
 
        "cool": {
            "dawn":    {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Jerkbait",                "reason": "cool water reaction bait at first light"},
                    {"bait": "Small Jig (1/16 oz)",    "reason": "crappie active near structure"},
                    {"bait": "Inline Spinner",          "reason": "bream hitting near surface at dawn"},
                ],
                "tip": "Cool spring dawn — pre-spawn bass and crappie are aggressive near cover."
            },
            "sunrise": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "reaction bait for active spring bass"},
                    {"bait": "Jig (1/4 oz)",            "reason": "slow roll through spawning areas"},
                    {"bait": "Crappie Jig",             "reason": "crappie staging near brush piles"},
                ],
                "tip": "Prime spring sunrise — bass moving shallow to spawn, very catchable."
            },
            "noon": {
                "species": ["Crappie", "Bream"],
                "baits":   [
                    {"bait": "Small Jig (1/16 oz)",    "reason": "vertical jigging for suspended crappie"},
                    {"bait": "Crickets",                "reason": "bream can't ignore a cricket noon"},
                ],
                "tip": "Bass slowing noon — switch to crappie and bream tactics."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "dusk feeding run for bass"},
                    {"bait": "Inline Spinner",          "reason": "bream active near surface at dusk"},
                ],
                "tip": "dusk cool down — bass back on the feed, target shallow structure."
            },
            "night": {
                "species": ["Catfish", "Crappie"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "top catfish bait at night"},
                    {"bait": "Small Jig",               "reason": "crappie feed after dark near lights"},
                ],
                "tip": "Cool spring night — catfish active, crappie near any dock lights."
            },
        },
 
        "prime": {
            "dawn":    {
                "species": ["Bass", "Bream", "Crappie"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "best topwater bite of the day at dawn"},
                    {"bait": "Buzzbait",                "reason": "explosive surface strikes in low light"},
                    {"bait": "Inline Spinner",          "reason": "bream crushing small spinners at dawn"},
                ],
                "tip": "Perfect spring dawn — best topwater bite of the year, don't miss it."
            },
            "sunrise": {
                "species": ["Bass", "Bream", "Crappie"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "prime reaction bait for spawning bass"},
                    {"bait": "Plastic Worm (6in)",      "reason": "bass on beds — slow worm right on them"},
                    {"bait": "Crickets",                "reason": "bream spawning in shallows, very aggressive"},
                ],
                "tip": "Spawn is on — bass, bream all bedding shallow, easy to find and catch."
            },
            "noon": {
                "species": ["Bream", "Crappie"],
                "baits":   [
                    {"bait": "Crickets",                "reason": "bream on beds all day during spawn"},
                    {"bait": "Small Jig (1/16 oz)",    "reason": "crappie holding near shade structure"},
                ],
                "tip": "Bass moving off beds noon — bream still active, easy limit in the shallows."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Buzzbait",                "reason": "post spawn bass chasing topwater"},
                    {"bait": "Frog",                    "reason": "great over shallow grass and pads"},
                    {"bait": "Inline Spinner",          "reason": "bream crushing spinners at dusk"},
                ],
                "tip": "Prime spring dusk — fish are everywhere and actively feeding."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish very active in warm spring nights"},
                    {"bait": "Dark Plastic Worm",       "reason": "bass hunt by vibration at night"},
                ],
                "tip": "Warm spring night — catfish and bass both active after dark."
            },
        },
 
        "warm": {
            "dawn":    {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Frog",           "reason": "warm water surface bite at first light"},
                    {"bait": "Buzzbait",                "reason": "fast moving bait before water heats up"},
                ],
                "tip": "Warm spring dawn — get topwater in early before the heat sets in."
            },
            "sunrise": {
                "species": ["Bass", "Catfish"],
                "baits":   [
                    {"bait": "Plastic Worm",            "reason": "bass retreating to shade and depth"},
                    {"bait": "Nightcrawler",            "reason": "catfish moving into feeding areas"},
                ],
                "tip": "Water warming up fast — work deeper structure as sunrise progresses."
            },
            "noon": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Cut Shad",                "reason": "catfish holding deep in warm water"},
                    {"bait": "Nightcrawler",            "reason": "slow bottom presentation for deep fish"},
                ],
                "tip": "Too warm noon — most fish deep or in shade. Catfish your best bet."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "surface bite returns as water cools"},
                    {"bait": "Inline Spinner",          "reason": "bream active again in dusk"},
                ],
                "tip": "Water cooling at dusk — fish coming back shallow, good dusk bite ahead."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Stink Bait",              "reason": "warm nights are best for catfish"},
                    {"bait": "Dark Swimbait",           "reason": "bass hunting by feel in warm water"},
                ],
                "tip": "Warm spring night — prime catfish conditions, bass also active after dark."
            },
        },
    },
 
    # ── SUMMER ──────────────────────────────────────────────────────────────
    "summer": {
        "prime": {
            "dawn":    {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "summer topwater at its best at dawn"},
                    {"bait": "Buzzbait",                "reason": "explosive strikes before sun hits water"},
                ],
                "tip": "Best window of the summer day — get on the water at first light."
            },
            "sunrise": {
                "species": ["Bass", "Bream", "Crappie"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "bass still active in sunrise cool"},
                    {"bait": "Crickets",                "reason": "bream active near shore structure"},
                ],
                "tip": "Good sunrise bite before noon heat — target shady structure."
            },
            "noon": {
                "species": ["Catfish", "Crappie"],
                "baits":   [
                    {"bait": "Deep Diving Crankbait",   "reason": "crappie suspended 10-15ft deep"},
                    {"bait": "Cut Shad",                "reason": "catfish holding in deepest holes"},
                ],
                "tip": "Bass shut down noon — go deep for crappie or bottom fish for catfish."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Frog",           "reason": "dusk surface bite over grass"},
                    {"bait": "Inline Spinner",          "reason": "bream very active at dusk"},
                ],
                "tip": "dusk bite turning on — fish moving shallow as water cools."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish most active summer nights"},
                    {"bait": "Dark Plastic Worm",       "reason": "bass hunt by vibration at night"},
                ],
                "tip": "Summer night fishing — catfish prime time, large bass also active."
            },
        },
 
        "warm": {
            "dawn":    {
                "species": ["Bass"],
                "baits":   [
                    {"bait": "Topwater Frog",           "reason": "only reliable surface window all day"},
                    {"bait": "Buzzbait",                "reason": "fast bait before heat shuts down bite"},
                ],
                "tip": "Hot summer — dawn is your only real window. Make it count."
            },
            "sunrise": {
                "species": ["Bass", "Catfish"],
                "baits":   [
                    {"bait": "Deep Plastic Worm",       "reason": "bass retreating fast in hot water"},
                    {"bait": "Nightcrawler",            "reason": "catfish moving into feeding zones"},
                ],
                "tip": "Heat shutting down the bite — go deep early or pack up by 10am."
            },
            "noon": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Cut Shad",                "reason": "only catfish tolerate noon heat"},
                    {"bait": "Stink Bait",              "reason": "strong scent finds fish in hot water"},
                ],
                "tip": "Too hot for most fish — anchor deep and soak catfish bait."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "surface bite finally coming back"},
                    {"bait": "Buzzbait",                "reason": "fast bait for aggressive dusk bass"},
                ],
                "tip": "Water cooling fast — best bite of a hot day is right now."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Stink Bait / Liver",      "reason": "peak catfish time in hot weather"},
                    {"bait": "Dark Swimbait",           "reason": "large bass active all night in summer"},
                ],
                "tip": "Hot summer night — best fishing of the day. Stay out late."
            },
        },
 
        "cold": {
            "dawn":    {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jerkbait",                "reason": "cold snap reaction bait for bass"},
                    {"bait": "Small Jig",               "reason": "crappie deeper than usual"},
                ],
                "tip": "Unusual cold snap in summer — fish confused, reaction baits work well."
            },
            "sunrise": {
                "species": ["Crappie", "Bass"],
                "baits":   [
                    {"bait": "Small Jig",               "reason": "crappie schooled up in cold water"},
                    {"bait": "Jig (1/4 oz)",            "reason": "slow presentation for sluggish bass"},
                ],
                "tip": "Cold summer sunrise — fish deeper than normal, they went down with the temp."
            },
            "noon": {
                "species": ["Crappie", "Catfish"],
                "baits":   [
                    {"bait": "Live Minnow",             "reason": "crappie school suspended mid-depth"},
                    {"bait": "Nightcrawler",            "reason": "catfish still feeding on bottom"},
                ],
                "tip": "Unusual conditions — find the thermocline and fish just above it."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "bass more active in cooler dusk"},
                    {"bait": "Crickets",                "reason": "bream taking advantage of cool water"},
                ],
                "tip": "Cool summer dusk — better than normal conditions for most species."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Nightcrawler",            "reason": "reliable cold water bottom bait"},
                    {"bait": "Chicken Liver",           "reason": "catfish always active at night"},
                ],
                "tip": "Cool summer night — comfortable fishing, catfish very active."
            },
        },
 
        "cool": {
            "dawn":    {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "cool surface temps bring fish up"},
                    {"bait": "Small Jig",               "reason": "crappie near structure at dawn"},
                ],
                "tip": "Cooler than normal summer sunrise — fish more active than usual."
            },
            "sunrise": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "bass chasing actively in cool water"},
                    {"bait": "Crappie Jig",             "reason": "crappie near submerged structure"},
                ],
                "tip": "Good summer sunrise — fish are more active in the cooler water."
            },
            "noon": {
                "species": ["Crappie", "Catfish"],
                "baits":   [
                    {"bait": "Small Jig",               "reason": "crappie suspended at mid depth"},
                    {"bait": "Cut Shad",                "reason": "catfish holding in deepest holes"},
                ],
                "tip": "Decent noon in cool water — better than a hot summer day."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Buzzbait",                "reason": "great surface bite in cool dusk"},
                    {"bait": "Inline Spinner",          "reason": "bream very active near shore"},
                ],
                "tip": "Cool summer dusk — prime conditions, fish are very active."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Stink Bait",              "reason": "catfish prime at night"},
                    {"bait": "Dark Worm",               "reason": "bass hunting shallow structure"},
                ],
                "tip": "Cool summer night — excellent all around conditions."
            },
        },
    },
 
    # ── FALL ────────────────────────────────────────────────────────────────
    "fall": {
        "prime": {
            "dawn":    {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "fall topwater bite is aggressive"},
                    {"bait": "Crankbait",               "reason": "bass chasing shad at surface"},
                ],
                "tip": "Fall feeding frenzy — bass loading up before winter, very aggressive."
            },
            "sunrise": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "match the fall shad migration"},
                    {"bait": "Spinnerbait",             "reason": "fast moving bait for active fall bass"},
                    {"bait": "Crappie Jig",             "reason": "crappie schooling near structure"},
                ],
                "tip": "Best fall sunrise bite — find the shad schools and bass are right behind them."
            },
            "noon": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Deep Crankbait",          "reason": "bass following shad to mid depth"},
                    {"bait": "Small Jig",               "reason": "crappie schools suspended midwater"},
                ],
                "tip": "Fall noon stays productive unlike summer — fish active all day."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "dusk surface feed in fall is epic"},
                    {"bait": "Buzzbait",                "reason": "aggressive fall bass love buzzbaits"},
                ],
                "tip": "Fall dusk — one of the best bites of the entire year right now."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish feeding heavily before winter"},
                    {"bait": "Dark Swimbait",           "reason": "big bass active all night in fall"},
                ],
                "tip": "Fall night fishing — catfish and big bass both very active."
            },
        },
 
        "cool": {
            "dawn":    {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jerkbait",                "reason": "cool water reaction bait at first light"},
                    {"bait": "Small Jig",               "reason": "crappie near structure at dawn"},
                ],
                "tip": "Cool fall dawn — fish active and feeding, great sunrise ahead."
            },
            "sunrise": {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "classic fall bass bait in cool water"},
                    {"bait": "Crappie Jig",             "reason": "crappie schooling near brush"},
                    {"bait": "Crickets",                "reason": "bream still active in cool fall temps"},
                ],
                "tip": "Great fall sunrise — all species active, pick your target and go."
            },
            "noon": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "fall noon bass chasing shad"},
                    {"bait": "Live Minnow",             "reason": "crappie can't resist live bait"},
                ],
                "tip": "Fall noon is productive — fish feeding actively to build fat for winter."
            },
            "dusk": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Topwater",                "reason": "surface bite returns strong at dusk"},
                    {"bait": "Crappie Jig",             "reason": "crappie very active near dusk"},
                ],
                "tip": "Cool fall dusk — excellent bite, one of the best times of year."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Nightcrawler",            "reason": "reliable fall catfish bait"},
                    {"bait": "Chicken Liver",           "reason": "catfish feeding heavily in fall"},
                ],
                "tip": "Cool fall night — catfish very active feeding up for winter."
            },
        },
 
        "cold": {
            "dawn":    {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jig (1/4 oz)",            "reason": "slow fall presentation in cold water"},
                    {"bait": "Small Jig",               "reason": "crappie schooled deep in cold water"},
                ],
                "tip": "Cold fall dawn — slow down your presentation, fish are lethargic."
            },
            "sunrise": {
                "species": ["Crappie", "Bass"],
                "baits":   [
                    {"bait": "Small Jig / Minnow",      "reason": "crappie holding near deep structure"},
                    {"bait": "Jig (1/4 oz)",            "reason": "slow bottom hop for cold bass"},
                ],
                "tip": "Cold fall sunrise — find structure and fish slow and deep."
            },
            "noon": {
                "species": ["Crappie", "Catfish"],
                "baits":   [
                    {"bait": "Live Minnow",             "reason": "warmest part of cold day — crappie active"},
                    {"bait": "Nightcrawler",            "reason": "catfish still hitting on bottom"},
                ],
                "tip": "Warmest window of a cold day — best fishing from 11am to 2pm."
            },
            "dusk": {
                "species": ["Crappie"],
                "baits":   [
                    {"bait": "Small Jig",               "reason": "crappie near structure at dusk"},
                    {"bait": "Live Minnow",             "reason": "hard to beat in cold water"},
                ],
                "tip": "Cold fall dusk — temps dropping fast, crappie your best target."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish most reliable cold night bait"},
                ],
                "tip": "Cold fall night — catfish only reliable target, fish deep and slow."
            },
        },
 
        "warm": {
            "dawn":    {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Frog",           "reason": "warm fall surface bite at dawn"},
                    {"bait": "Buzzbait",                "reason": "aggressive bass in warm fall water"},
                ],
                "tip": "Warm fall sunrise — almost summer-like conditions, topwater working."
            },
            "sunrise": {
                "species": ["Bass", "Bream", "Catfish"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "bass active in warm fall water"},
                    {"bait": "Crickets",                "reason": "bream still on crickets in warm temps"},
                ],
                "tip": "Warm fall conditions — extended season, fish still in summer patterns."
            },
            "noon": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Cut Shad",                "reason": "catfish deep in warm fall water"},
                    {"bait": "Deep Worm",               "reason": "bass retreating to deeper shade"},
                ],
                "tip": "Warm fall noon — similar to summer, go deep or go home."
            },
            "dusk": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater Popper",         "reason": "dusk surface bite in warm fall"},
                    {"bait": "Inline Spinner",          "reason": "bream active near shore at dusk"},
                ],
                "tip": "Warm fall dusk — great conditions, extended season still going."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Stink Bait",              "reason": "warm night prime catfish conditions"},
                    {"bait": "Dark Swimbait",           "reason": "large bass hunting at night"},
                ],
                "tip": "Warm fall night — like a summer night, catfish and bass very active."
            },
        },
    },
 
    # ── WINTER ──────────────────────────────────────────────────────────────
    "winter": {
        "cold": {
            "dawn":    {
                "species": ["Crappie"],
                "baits":   [
                    {"bait": "Small Jig (1/32 oz)",    "reason": "tiny slow presentation for cold crappie"},
                    {"bait": "Live Minnow",             "reason": "best cold water crappie bait"},
                ],
                "tip": "Cold winter dawn — crappie schooled deep, find the school and vertical jig."
            },
            "sunrise": {
                "species": ["Crappie", "Catfish"],
                "baits":   [
                    {"bait": "Live Minnow",             "reason": "irresistible to winter crappie"},
                    {"bait": "Nightcrawler",            "reason": "catfish still feeding slowly in cold"},
                ],
                "tip": "Winter sunrise — slow everything way down, fish are lethargic."
            },
            "noon": {
                "species": ["Crappie", "Bass"],
                "baits":   [
                    {"bait": "Small Jig",               "reason": "best window of a cold day for crappie"},
                    {"bait": "Jig (1/4 oz)",            "reason": "warmest water of day brings bass up slightly"},
                ],
                "tip": "Best winter fishing is noon when water is warmest — 11am to 2pm."
            },
            "dusk": {
                "species": ["Crappie"],
                "baits":   [
                    {"bait": "Small Jig / Minnow",      "reason": "crappie last feeding window before dark"},
                ],
                "tip": "Cold winter dusk — temps dropping fast, quick crappie session only."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish one of few species active at night in winter"},
                ],
                "tip": "Cold winter night — tough conditions, catfish your only realistic target."
            },
        },
 
        "cool": {
            "dawn":    {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jig (1/4 oz)",            "reason": "slow bottom presentation for winter bass"},
                    {"bait": "Small Jig",               "reason": "crappie near deep structure"},
                ],
                "tip": "Cool winter dawn — fish slow and deep, noon will be better."
            },
            "sunrise": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Blade Bait",              "reason": "winter bass react to blade baits"},
                    {"bait": "Live Minnow",             "reason": "crappie near brush piles and docks"},
                ],
                "tip": "Cool winter sunrise — fish getting active as water slowly warms."
            },
            "noon": {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Jig (1/4 oz)",            "reason": "best winter bass bait at warmest point"},
                    {"bait": "Small Jig / Minnow",      "reason": "crappie active in warmest noon window"},
                    {"bait": "Crickets",                "reason": "bream hitting in warmest part of day"},
                ],
                "tip": "Best winter fishing window — warm clothes, good bite from 11am to 2pm."
            },
            "dusk": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jig",                     "reason": "last bass feeding window before dark"},
                    {"bait": "Small Jig",               "reason": "crappie near structure at dusk"},
                ],
                "tip": "Cool winter dusk — decent bite but temps dropping fast."
            },
            "night": {
                "species": ["Catfish"],
                "baits":   [
                    {"bait": "Nightcrawler",            "reason": "reliable winter catfish bait"},
                    {"bait": "Chicken Liver",           "reason": "catfish active even in cool winter nights"},
                ],
                "tip": "Cool winter night — catfish best target, fish the deepest holes."
            },
        },
 
        "prime": {
            "dawn":    {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Jerkbait",                "reason": "warm winter dawn reaction bait"},
                    {"bait": "Small Jig",               "reason": "crappie near structure"},
                ],
                "tip": "Unusually warm winter sunrise — fish more active than normal, take advantage."
            },
            "sunrise": {
                "species": ["Bass", "Crappie", "Bream"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "warm winter water brings bass shallow"},
                    {"bait": "Crappie Jig",             "reason": "crappie active in warm winter water"},
                    {"bait": "Crickets",                "reason": "bream active in unseasonably warm conditions"},
                ],
                "tip": "Warm winter day — almost spring-like conditions, fish are confused but active."
            },
            "noon": {
                "species": ["Bass", "Bream", "Crappie"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "bass active and chasing in warm water"},
                    {"bait": "Crickets",                "reason": "bream taking advantage of warm day"},
                ],
                "tip": "Warm winter noon — rare opportunity, fish it hard while it lasts."
            },
            "dusk": {
                "species": ["Bass", "Crappie"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "dusk feed in warm winter water"},
                    {"bait": "Crappie Jig",             "reason": "crappie active near dock lights"},
                ],
                "tip": "Warm winter dusk — great conditions, enjoy it before temps drop."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Chicken Liver",           "reason": "catfish very active on warm winter nights"},
                    {"bait": "Dark Worm",               "reason": "bass surprisingly active in warm winter water"},
                ],
                "tip": "Warm winter night — unusual but excellent conditions for catfish and bass."
            },
        },
 
        "warm": {
            "dawn":    {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Spinnerbait",             "reason": "warm winter surface activity at dawn"},
                    {"bait": "Inline Spinner",          "reason": "bream active in warm winter water"},
                ],
                "tip": "Very warm for winter — fish behaving like early spring, fish shallow."
            },
            "sunrise": {
                "species": ["Bass", "Bream", "Crappie"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "bass chasing actively in warm water"},
                    {"bait": "Crickets",                "reason": "bream active like it's spring"},
                ],
                "tip": "Unseasonably warm winter sunrise — take advantage of these rare conditions."
            },
            "noon": {
                "species": ["Bass", "Bream"],
                "baits":   [
                    {"bait": "Topwater",                "reason": "warm enough for surface activity noon"},
                    {"bait": "Spinnerbait",             "reason": "active bass chasing in warm conditions"},
                ],
                "tip": "Warm winter noon — almost no different from fall conditions, fish are up."
            },
            "dusk": {
                "species": ["Bass", "Catfish"],
                "baits":   [
                    {"bait": "Crankbait",               "reason": "active dusk feed in warm winter water"},
                    {"bait": "Nightcrawler",            "reason": "catfish active in warm conditions"},
                ],
                "tip": "Warm winter dusk — fish it until dark, conditions won't last."
            },
            "night": {
                "species": ["Catfish", "Bass"],
                "baits":   [
                    {"bait": "Stink Bait",              "reason": "warm winter night prime for catfish"},
                    {"bait": "Dark Swimbait",           "reason": "bass active all night in warm water"},
                ],
                "tip": "Warm winter night — exceptional conditions, fish like it's summer."
            },
        },
    },
} 


#astral calculations
def get_time_of_day(target_dt): 
    sun_fun = sun(LOCATION.observer,date=target_dt.date(), tzinfo=LOCATION.timezone)

    dawn = sun_fun['dawn']
    sunrise = sun_fun['sunrise']
    noon = sun_fun['noon']
    dusk = sun_fun['dusk']
    night = sun_fun['night']

    if target_dt < dawn:
        return "night"
    if dawn<= target_dt < sunrise:
         return "dawn"
    if sunrise<= target_dt < noon:
        return "sunrise"
    if noon <= target_dt < dusk:
        return "noon"
    if dusk <= target_dt < night:
        return "dusk"
    else:
        return "night"
    


temp_f = sensor_data.get("water_temp", 68)#68 is a fallback value in case a temp doesn't exsist

def get_temp(temp_f):
    if temp_f < 50: 
        return "cold"
    elif temp_f < 60:
        return "cool"
    elif temp_f < 75:
        return "primetime"
    else: 
        return "warm"

def search_Rules(season,temp_f, target_dt):

    season_node = RULES.get(season,None)

    temp_range = get_temp(temp_f)

    time_of_day = get_time_of_day(target_dt)