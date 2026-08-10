#!/usr/bin/python3
"""This is a modul for Creating a Simple Templating Program"""

import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        output = template.replace("{name}", str(name))
        output = output.replace("{event_title}", str(event_title))
        output = output.replace("{event_date}", str(event_date))
        output = output.replace("{event_location}", str(event_location))

        filename = f"output_{index}.txt"

        try:
            if os.path.exists(filename):
                pass
            with open(filename, "w") as file:
                file.write(output)
        except OSError as error:
            print(f"Error writing {filename}: {error}")