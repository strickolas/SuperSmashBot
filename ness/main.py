from ness.view.dolphin import DolphinView

x = 0
while x < 25:
    try:
        DolphinView().get_screenshot(duration=0.1).show()
        x = x + 1
    except:
        pass
