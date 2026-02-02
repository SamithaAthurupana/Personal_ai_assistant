def input_guardrails(state):
    input_text = state["input"]
    blocked_words = [
        "bomb", "weapon", "drugs", "hack", "explosives"
    ]

    for word in blocked_words:
        if word in input_text:
            return {"blocked": True, "response": "Blocked - Detected Harmful content"}

    return {"blocked":False}
