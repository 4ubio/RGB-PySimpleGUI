import PySimpleGUI as sg

#This function returns the RGB parameters of sliders to Hex
def rgb_hex(rgb):
    return "%02x%02x%02x" % rgb

sg.theme("Topanga")

layout = [[sg.Text(text="HEX: ", font=("Rockwell", 17)),
             sg.Text(text='#000000', key="codeHEX", font=("Rockwell", 17))],
            [sg.Canvas(size=(350,250), key="Canvas", background_color="#000000")],
            [sg.Text("Red",font=("Rockwell", 15))],
            [sg.Slider((0,255), font=("Rockwell", 17), key="sliderRED", orientation="horizontal",
                        enable_events=True, disable_number_display=False)],
            [sg.Text("Green", font=("Rockwell", 15))],
            [sg.Slider((0, 255), font=("Rockwell", 17), key="sliderGREEN", orientation="horizontal",
                        enable_events=True, disable_number_display=False)],
            [sg.Text("Blue", font=("Rockwell", 15))],
            [sg.Slider((0, 255), font=("Rockwell", 17), key="sliderBLUE", orientation="horizontal",
                        enable_events=True, disable_number_display=False)],
            [sg.Button("Close", font=("Rockwell", 15))]]

window = sg.Window("RGB", layout)
window.Finalize()

canvas = window["Canvas"]
#We need to create a rectangle of the same size as Canva in the layout with center in origin
rec = canvas.TKCanvas.create_rectangle(0, 0, 350, 250)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Close":
        break

#First, we need to save the int values of sliders
    red = int(values["sliderRED"])
    green = int(values["sliderGREEN"])
    blue = int(values["sliderBLUE"])
    hexcode = "#" + str(rgb_hex((red, green, blue))) #Call the function of above in order to get the hex value
    canvas.TKCanvas.itemconfig(rec, fill=hexcode) #Update the background color of the rectangle with the hex values that we get of the function
    window["codeHEX"].update(hexcode) #Update the hex value that is shown in display
window.close()