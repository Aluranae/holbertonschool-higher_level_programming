#!/usr/bin/env python3
"""
Function to generate personalized invitation files based on a text template
and a list of attendee dictionaries.
"""

import logging


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return

    if not isinstance(attendees, list):
        logging.error("Attendees must be a list.")
        return

    for i, guest in enumerate(attendees):
        if not isinstance(guest, dict):
            logging.error(
                (
                    (
                        (
                            "Attendee at index {} is invalid: "
                            "expected dictionary, got {}"
                        )
                    )
                ).format(
                    i, type(guest).__name__
                )
            )
            return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for i, guest in enumerate(attendees, start=1):
        personalized_text = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = guest.get(key)
            if value is None:
                value = "N/A"
            personalized_text = personalized_text.replace("{{{}}}".format(key))

        file_name = f"output_{i}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(personalized_text)
