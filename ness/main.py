from ness.view.dolphin import DolphinView


dv = DolphinView()
while True:
    image = dv.screenshot(duration=1)
    image.show()

