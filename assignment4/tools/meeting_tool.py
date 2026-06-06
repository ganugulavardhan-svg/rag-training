def get_meeting_notes(query: str):

    with open(
        "data/meeting_notes.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()