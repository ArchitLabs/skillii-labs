# A stand-in for the shop's own software, so this lab changes nothing real.
# A real shop would call its order system, its returns system and its email service here.
import json

TOOLS = [
    {"name": "get_order", "description": "Look up an order: the item and how many days ago it was delivered.",
     "input_schema": {"type": "object", "properties": {"order_id": {"type": "string"}},
                      "required": ["order_id"]}},
    {"name": "create_return", "description": "Open a return for an order. Returns are free within 30 days.",
     "input_schema": {"type": "object", "properties": {"order_id": {"type": "string"}, "reason": {"type": "string"}},
                      "required": ["order_id", "reason"]}},
    {"name": "email_customer", "description": "Send the customer an email about their order.",
     "input_schema": {"type": "object", "properties": {"order_id": {"type": "string"}, "text": {"type": "string"}},
                      "required": ["order_id", "text"]}},
]


def run_tool(name, args):
    if name == "get_order":
        return json.dumps({"order_id": args["order_id"], "item": "linen shirt, size M", "delivered_days_ago": 6})
    if name == "create_return":
        return json.dumps({"return_id": "R-" + args["order_id"], "label": "ready to print"})
    if name == "email_customer":
        return json.dumps({"sent": True})
    return json.dumps({"error": f"unknown tool {name}"})
