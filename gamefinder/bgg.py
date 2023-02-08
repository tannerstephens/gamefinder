import html
import xml.etree.ElementTree as ET

import requests

BGG_BASE_URL = "https://api.geekdo.com/xmlapi2"

IGNORED_TAGS = {
    "boardgameimplementation",
    "boardgamefamily",
    "boardgameexpansion",
    "boardgamecompilation",
    "boardgamepublisher",
    "boardgameartist",
}


def get_elements(root: ET.Element, element_names: list[str]):
    found = {}

    for element_name in element_names:
        element = root.find(element_name)

        if element is not None:
            data = element.text or element.get("value", "")

            if data.isdigit():
                data = int(data)

            found[element.tag] = data

    return found


def get_tags(game_root: ET.Element):
    tags = []

    for tag_xml in game_root.findall("link"):
        tag_type = tag_xml.get("type")

        if tag_type in IGNORED_TAGS:
            continue

        tag = {"type": tag_type, "value": tag_xml.get("value")}

        tags.append(tag)

    return tags


def search(query: str):
    params = {"query": query, "type": "boardgame"}
    resp = requests.get(f"{BGG_BASE_URL}/search", params=params)

    root = ET.fromstring(resp.content)

    games = []

    for item in root.iter("item"):
        game = get_elements(item, ["name", "yearpublished"])

        games.append(
            {
                "id": item.get("id"),
                "name": game.get("name"),
                "year": game.get("yearpublished"),
            }
        )

    return games


def thing(thing_id: int):
    params = {"id": thing_id}
    resp = requests.get(f"{BGG_BASE_URL}/thing", params=params)

    root = ET.fromstring(resp.content)

    game_xml = root.find(f"item[@id='{thing_id}']")

    if game_xml is None:
        return None

    suggested_players_poll = game_xml.find("poll[@name='suggested_numplayers']")
    poll_results = {}

    for response in suggested_players_poll.findall("results"):
        num_players = response.get("numplayers")
        votes = int(response.find("result[@value='Best']").get("numvotes"))

        poll_results[num_players] = votes

    elements = get_elements(
        game_xml,
        [
            "thumbnail",
            "image",
            "name[@type='primary']",
            "description",
            "yearpublished",
            "minplayers",
            "maxplayers",
            "minplaytime",
            "maxplaytime",
            "minage",
        ],
    )

    description: str = elements.get("description")

    if description:
        description = description.replace("&#10;", "<br>")

    return {
        "bgg_id": game_xml.get("id"),
        "name": elements.get("name"),
        "thumbnail": elements.get("thumbnail"),
        "image": elements.get("image"),
        "description": description,
        "year": elements.get("yearpublished"),
        "min_players": elements.get("minplayers"),
        "max_players": elements.get("maxplayers"),
        "best_players": max(poll_results, key=poll_results.get),
        "min_playtime": elements.get("minplaytime"),
        "max_playtime": elements.get("maxplaytime"),
        "min_age": elements.get("minage"),
        "tags": get_tags(game_xml),
    }
