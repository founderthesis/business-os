# Pass 2 frozen row list (8 Nov)

`pass2-frozen-ids.txt`: 503 Engagement page ids (no names, no contact data).

Filter: Kind is not Task; Status not in Parked, They declined, We declined, Form filled, Recorded; New, Contacted and Unresponsive rows with Direction Outbound excluded; empty Direction stays in (the first cut of 467 wrongly dropped 36 New/Contacted/Unresponsive rows with empty Direction; added back).

Status: no API spend yet. Waiting for a go in the API worker chat.
Plan: live 25-row chunks with a forced web-search instruction (batch under-searches), USD 80 cap (per CTO relay of Akshay, 8 Nov).
