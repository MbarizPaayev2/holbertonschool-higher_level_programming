#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if type(template) != str:
        raise TypeError("Invalid input types")

    if not isinstance(attendees, list):
        raise TypeError("Invalid input types")
    else:
        for attendee in attendees:
            if not isinstance(attendee, dict):
                raise TypeError("Invalid input types")

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        text = template  # template-in kopyası

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            text = text.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(text)
                print(f"Generated {output_filename}")
        except Exception as error:
            print(f"Error writing file {output_filename}: {error}")
