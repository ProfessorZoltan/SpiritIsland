import streamlit as st
import math

# Data for dropdown options
spirits = [
    "Lightning's Swift Strike", "River Surges in Sunlight", "Shadows Flicker Like Flame", "Vital Strength of the Earth",
    "A Spread of Rampant Green", "Thunderspeaker", "Bringer of Dreams and Nightmares", "Ocean's Hungry Grasp",
    "Keeper of the Forbidden Wilds", "Sharp Fangs Behind the Leaves", "Heart of the Wildfire", "Serpent Slumbering Beneath the Island",
    "Grinning Trickster Stirs Up Trouble", "Lure of the Deep Wilderness", "Many Minds Move as One", "Shifting Memory of Ages",
    "Stone's Unyielding Defiance", "Volcano Looming High", "Shroud of Silent Mist", "Vengeance as a Burning Plague",
    "Fractured Days Split the Sky", "Starlight Seeks Its Form", "Downpour Drenches the World", "Finder of Paths Unseen",
    "Devouring Teeth Lurk Underfoot", "Eyes Watch from the Trees", "Fathomless Mud of the Swamp", "Rising Heat of Stone and Sand",
    "Sun-Bright Whirlwind", "Ember-Eyed Behemoth", "Hearth-Vigil", "Towering Roots of the Jungle", "Breath of Darkness Down Your Spine",
    "Relentless Gaze of the Sun", "Wandering Voice Keens Delirium", "Wounded Waters Bleeding", "Dances Up Earthquakes"
]

scenarios = [
    "none", "Blitz", "Guard the Isle's Heart", "Rituals of Terror", "Dahan Insurrection", "Elemental Invocation", "Despicable Theft",
    "The Great River", "Powers Long Forgotten", "Ward the Shores", "Second Wave", "Surges of Colonization", "Destiny Unfolds"
]

adversaries = [
    "none", "The Kingdom of Brandenburg-Prussia", "The Kingdom of England", "The Kingdom of Sweden", "The Tsardom of Russia",
    "The Habsburg Monarchy (Livestock Colony)", "The Kingdom of France (Plantation Colony)", "Habsburg Mining Expedition"
]

adversary_levels = [0, 1, 2, 3, 4, 5, 6]

winOptions = ["Yes", "No"]

# Streamlit app layout
st.title("Spirit Island Score Calculator")
st.subheader("Complete all fields")

# Number of spirits input
num_spirits = st.number_input("Number of Spirits", min_value=1, max_value=6, step=1, value=1)

# Dynamic spirit selection
selected_spirits = []
for i in range(num_spirits):
    spirit = st.selectbox(f"Spirit {i+1}", spirits, key=f"spirit_{i}")
    selected_spirits.append(spirit)

scenario = st.selectbox("Scenario", scenarios)
adversary = st.selectbox("Adversary", adversaries)
adversary_level = st.selectbox("Adversary Level", adversary_levels)
winState = st.selectbox("Did You Win?", winOptions)

# Input fields for game stats
blight_remaining = st.number_input("Blight on Island", min_value=0, step=1)
dahan_surviving = st.number_input("Dahan Surviving", min_value=0, step=1)
invader_cards_left_deck = st.number_input("Invader Cards Left Facedown", min_value=0, step=1)
invader_cards_used = st.number_input("Invader Cards Faceup", min_value=0, step=1)

# Adversary difficulty lookup
adversary_lookup = {
    ("none", 0): 0,
    ("none", 1): 0,
    ("none", 2): 0,
    ("none", 3): 0,
    ("none", 4): 0,
    ("none", 5): 0,
    ("none", 6): 0,

    ("The Kingdom of Brandenburg-Prussia", 0): 1,
    ("The Kingdom of Brandenburg-Prussia", 1): 2,
    ("The Kingdom of Brandenburg-Prussia", 2): 4,
    ("The Kingdom of Brandenburg-Prussia", 3): 6,
    ("The Kingdom of Brandenburg-Prussia", 4): 7,
    ("The Kingdom of Brandenburg-Prussia", 5): 9,
    ("The Kingdom of Brandenburg-Prussia", 6): 10,

    ("The Kingdom of England", 0): 1,
    ("The Kingdom of England", 1): 3,
    ("The Kingdom of England", 2): 4,
    ("The Kingdom of England", 3): 6,
    ("The Kingdom of England", 4): 7,
    ("The Kingdom of England", 5): 9,
    ("The Kingdom of England", 6): 10,

    ("The Kingdom of Sweden", 0): 1,
    ("The Kingdom of Sweden", 1): 2,
    ("The Kingdom of Sweden", 2): 3,
    ("The Kingdom of Sweden", 3): 5,
    ("The Kingdom of Sweden", 4): 6,
    ("The Kingdom of Sweden", 5): 7,
    ("The Kingdom of Sweden", 6): 8,

    ("The Tsardom of Russia", 0): 1,
    ("The Tsardom of Russia", 1): 3,
    ("The Tsardom of Russia", 2): 4,
    ("The Tsardom of Russia", 3): 6,
    ("The Tsardom of Russia", 4): 7,
    ("The Tsardom of Russia", 5): 9,
    ("The Tsardom of Russia", 6): 11,

    ("The Habsburg Monarchy (Livestock Colony)", 0): 2,
    ("The Habsburg Monarchy (Livestock Colony)", 1): 3,
    ("The Habsburg Monarchy (Livestock Colony)", 2): 5,
    ("The Habsburg Monarchy (Livestock Colony)", 3): 6,
    ("The Habsburg Monarchy (Livestock Colony)", 4): 8,
    ("The Habsburg Monarchy (Livestock Colony)", 5): 9,
    ("The Habsburg Monarchy (Livestock Colony)", 6): 10,

    ("The Kingdom of France (Plantation Colony)", 0): 2,
    ("The Kingdom of France (Plantation Colony)", 1): 3,
    ("The Kingdom of France (Plantation Colony)", 2): 5,
    ("The Kingdom of France (Plantation Colony)", 3): 7,
    ("The Kingdom of France (Plantation Colony)", 4): 8,
    ("The Kingdom of France (Plantation Colony)", 5): 9,
    ("The Kingdom of France (Plantation Colony)", 6): 10,

    ("Habsburg Mining Expedition", 0): 1,
    ("Habsburg Mining Expedition", 1): 3,
    ("Habsburg Mining Expedition", 2): 4,
    ("Habsburg Mining Expedition", 3): 5,
    ("Habsburg Mining Expedition", 4): 7,
    ("Habsburg Mining Expedition", 5): 9,
    ("Habsburg Mining Expedition", 6): 10,
}

# Scenario difficulty lookup
scenario_lookup = {
    "none": 0,
    "Blitz": 0,
    "Guard the Isle's Heart": 0,
    "Rituals of Terror": 3,
    "Dahan Insurrection": 4,
    "Elemental Invocation": 1,
    "Despicable Theft": 2,
    "The Great River": 3,
    "Powers Long Forgotten": 1,
    "Ward the Shores": 2,
    "Second Wave": 1,
    "Surges of Colonization": 2,
    "Destiny Unfolds": -1,
}

# Get the difficulty for the selected adversary and level
difficulty_adversary = adversary_lookup.get((adversary, adversary_level), "Adversary not found")

# Get the difficulty for the selected scenario
difficulty_scenario = scenario_lookup.get(scenario, "Scenario not found")

# Calculate the total difficulty
difficulty = difficulty_adversary + difficulty_scenario

# Button to calculate the score
if st.button("Calculate Score"):
    difficulty = difficulty_adversary + difficulty_scenario  # Placeholder logic for difficulty
    if winState == "Yes":
        score = 10 + difficulty * 5 + math.floor(dahan_surviving / num_spirits) - math.floor(blight_remaining / num_spirits) + invader_cards_left_deck * 2
    else:
        score = 0 + difficulty * 2 + math.floor(dahan_surviving / num_spirits) - math.floor(blight_remaining / num_spirits) + invader_cards_used * 1
    st.success(f"Score: {score}")

# Compact display for screenshot
if st.button("Show Summary for Screenshot"):
    difficulty = difficulty_adversary + difficulty_scenario # Placeholder logic for difficulty
    if winState == "Yes":
        score = 10 + difficulty * 5 + math.floor(dahan_surviving / num_spirits) - math.floor(blight_remaining / num_spirits) + invader_cards_left_deck * 2
    else:
        score = 0 + difficulty * 2 + math.floor(dahan_surviving / num_spirits) - math.floor(blight_remaining / num_spirits) + invader_cards_used * 1
    st.write("### Game Summary")
    st.write(f"**Spirits:** {', '.join(selected_spirits)}")
    st.write(f"**Scenario:** {scenario}")
    st.write(f"**Adversary:** {adversary} (Level {adversary_level})")
    st.write(f"**Difficulty:** {difficulty}")
    st.write(f"**Win:** {winState}")
    st.write(f"**Blight on Island:** {blight_remaining}")
    st.write(f"**Dahan Surviving:** {dahan_surviving}")
    st.write(f"**Invader Cards Left Deck:** {invader_cards_left_deck}")
    st.write(f"**Invader Cards Faceup:** {invader_cards_used}")
    st.write(f"**Final Score:** {score}")
