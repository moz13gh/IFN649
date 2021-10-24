from .models import Action, Peripheral

    # categories = (
    #     ("Air Purifier", "Air Purifier"),
    #     ("Dehumidifier", "Dehumidifier"),
    #     ("Air Conditioner", "Air Conditioner"),
    #     ("Fan", "Fan"),
    #     ("Window", "Window")
    # )

def controlWindows(action):

    # Get list of windows
    window_list = Peripheral.objects.filter(category="Window")
    # If there are windows to control, do the action
    if len(window_list) > 0:

        if action == "on":
            for item in window_list:
            
                action_entry = Action(name="Open Window", peripheral_id=item.id)

                action_entry.save()

        elif action == "off":
            for item in window_list:
                action_entry = Action(name="Close Window", peripheral_id=item.id)
                action_entry.save()
    
    else:
        pass

def controlFans(action):
    if action == "on":
        pass
    elif action == "off":
        pass

def controlAirConditioner(action):
    if action == "on":
        pass
    elif action == "off":
        pass

def controlAirPurifier(action):
    if action == "on":
        pass
    elif action == "off":
        pass

def controlDehumidifier(action):
    if action == "on":
        pass
    elif action == "off":
        pass

def controlFans(action):
    if action == "on":
        pass
    elif action == "off":
        pass
