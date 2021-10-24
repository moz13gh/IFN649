from .models import Action, Peripheral

defined_actions = {
    "open": "Open",
    "close": "Close",
    "on": "Turn on",
    "off": "Turn off"
}

def controlWindows(action):
    # Get list of windows
    window_list = Peripheral.objects.filter(category="Window")
    print(window_list)
    # If there are windows to control, do the action
    if len(window_list) > 0:
        if action == "on":
            for item in window_list:
                action_entry = Action(action=defined_actions["open"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["open"]
                item.save()

        elif action == "off":
            for item in window_list:
                action_entry = Action(action=defined_actions["close"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["close"]
                item.save()
    # If not, do nothing
    else:
        pass

def controlFans(action):
    # Get list of windows
    fan_list = Peripheral.objects.filter(category="Fan")
    print(fan_list)
    # If there are windows to control, do the action
    if len(fan_list) > 0:
        if action == "on":
            for item in fan_list:
                action_entry = Action(action=defined_actions["on"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["on"]
                item.save()

        elif action == "off":
            for item in fan_list:
                action_entry = Action(action=defined_actions["off"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["off"]
                item.save()
    # If not, do nothing
    else:
        pass

def controlAirConditioner(action):
    # Get list of air conditioners
    air_conditioner_list = Peripheral.objects.filter(category="Air Conditioner")
    print(air_conditioner_list)
    # If there are ACs to control, do the action
    if len(air_conditioner_list) > 0:
        if action == "on":
            for item in air_conditioner_list:
                action_entry = Action(action=defined_actions["on"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["on"]
                item.save()

        elif action == "off":
            for item in air_conditioner_list:
                action_entry = Action(action=defined_actions["off"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["off"]
                item.save()
    # If not, do nothing
    else:
        pass

def controlAirPurifier(action):
    air_purifier_list = Peripheral.objects.filter(category="Air Purifier")
    print(air_purifier_list)
    if len(air_purifier_list) > 0:
        if action == "on":
            for item in air_purifier_list:
                action_entry = Action(action=defined_actions["on"], peripheral_id=item)
                action_entry.save()

        elif action == "off":
            for item in air_purifier_list:
                action_entry = Action(action=defined_actions["off"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["off"]
                item.save()
    else:
        pass

def controlDehumidifier(action):
    dehumidifier_list = Peripheral.objects.filter(category="Dehumidifier")
    print(dehumidifier_list)
    if len(dehumidifier_list) > 0:
        if action == "on":
            for item in dehumidifier_list:
                action_entry = Action(action=defined_actions["on"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["on"]
                item.save()

        elif action == "off":
            for item in dehumidifier_list:
                action_entry = Action(action=defined_actions["off"], peripheral_id=item)
                action_entry.save()

                item.current_action = defined_actions["off"]
                item.save()
    else:
        pass
