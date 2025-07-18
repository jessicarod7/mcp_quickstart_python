"""Assisted by Gemini-2.5-Flash / Continue.dev"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

import httpx
from markdownify import markdownify as md
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("status.redhat.com")


async def retrieve_status_page() -> Element | None:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get("https://status.redhat.com/history.rss")
            resp.raise_for_status()
            return ET.fromstring(resp.text)
        except Exception:
            return None


def last_updated(feed: Element) -> str:
    return feed.find("./channel/pubDate").text


def format_maintenance_events(feed: Element) -> str:
    maintenance = [
        f"""\
Title: {m.find("title").text}
Start: {m.find("pubDate").text}
End: {m.find("maintenanceEndDate").text}
Link: {m.find("link").text}

Description: {md(m.find("description").text)}""".strip()
        for m in feed.findall("./channel/item")
        if m.find("maintenanceEndDate") is not None
    ]

    return "\n---\n".join(maintenance)


def format_incidents(feed: Element) -> str:
    incidents = [
        f"""\
Title: {m.find("title").text}
Timestamp: {m.find("pubDate").text}
Link: {m.find("link").text}

Description: {md(m.find("description").text)}""".strip()
        for m in feed.findall("./channel/item")
        if m.find("maintenanceEndDate") is None
    ]

    return "\n---\n".join(incidents)


def format_all_events(feed: Element) -> str:
    formatted_events = []
    for m in feed.findall("./channel/item"):
        if m.find("maintenanceEndDate") is not None:
            formatted_events.append(
                f"""\
Title: {m.find("title").text}
Start: {m.find("pubDate").text}
End: {m.find("maintenanceEndDate").text}
Link: {m.find("link").text}

Description: {md(m.find("description").text)}""".strip()
            )

        else:
            formatted_events.append(
                f"""\
Title: {m.find("title").text}
Timestamp: {m.find("pubDate").text}
Link: {m.find("link").text}

Description: {md(m.find("description").text)}""".strip()
            )

    return "\n---\n".join(formatted_events)


@mcp.tool()
async def get_last_updated() -> str:
    """Return when status.redhat.com was last updated."""
    status = await retrieve_status_page()
    if status is not None:
        return last_updated(status)
    else:
        return "Unable to retrieve most recently updated time."


@mcp.tool()
async def get_maintenance() -> str:
    """Get upcoming and current maintenance events from Red Hat Status."""
    status = await retrieve_status_page()
    if status is not None:
        return format_maintenance_events(status)
    else:
        return "Unable to retrieve maintenance events."


@mcp.tool()
async def get_incidents() -> str:
    """Get incidents reported to Red Hat Status."""
    status = await retrieve_status_page()
    if status is not None:
        return format_incidents(status)
    else:
        return "Unable to retrieve incidents."


@mcp.tool()
async def get_all_events() -> str:
    """Get all events (incidents and maintenance) reported to Red Hat Status."""
    status = await retrieve_status_page()
    if status is not None:
        return format_all_events(status)
    else:
        return "Unable to retrieve status page."
