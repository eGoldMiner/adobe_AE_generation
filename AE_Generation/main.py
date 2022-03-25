import pyautogui
import json
import time

#VARIABLES
#   count
id_begin = 0 #include
id_end = 2 #not include
#   intervals
interval_high = 1.5 #seconds
interval_low = 0.5 #seconds
#   coordinates buttons
first_hide_calque = 340, 120
selection_layer = 534, 372
btn_file = 24, 34
btn_export = 101, 354
btn_export_media_encoder = 544, 353
composition = 66, 444
rename_file = 155, 773

#add composition to Adobe Media Encoder Queue
def export_file():
    pyautogui.click(btn_file)
    time.sleep(interval_low)
    pyautogui.click(btn_export)
    time.sleep(interval_low)
    pyautogui.click(btn_export_media_encoder)
    time.sleep(interval_low)

#hide all layers of the composition
def hide_all_layers():
    pyautogui.click(selection_layer)
    time.sleep(interval_low)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(interval_low)
    pyautogui.click(first_hide_calque)
    time.sleep(interval_low)
    pyautogui.hotkey('ctrl', 'shift', 'a')

#rename the composition on AE
def rename_output(id):
    text = "ElrondMiners #" + id
    pyautogui.click(composition, button='right')
    pyautogui.click(rename_file)
    pyautogui.typewrite(text)
    time.sleep(1)
    pyautogui.hotkey('enter')

#translate id to string for filename
def translate_id_string(id):
    value = ""
    if id <= 9:
        value = '000' + str(id)
    elif id <= 99:
        value = '00' + str(id)
    elif id <= 999:
        value = '0' + str(id)
    else:
        value = str(id)
    return value


#get data miners
file = open("./json/data.json")
data_miners = json.load(file)
file.close()
#get data coordinates
file = open("./json/coordinates.json")
data_coord = json.load(file)
file.close()

#init variables
id_miner = id_begin
id_name = translate_id_string(id_miner)

for x in data_miners:
    if (x['id'] >= id_begin) and (x['id'] < id_end):
        #show generation
        print("Id : " + str(x['id']) + " -> "+ str(x['assets']) + " => ElrondMiners #" + id_name)
        #PROGRAM
        #   rename composition
        rename_output(id_name)
        time.sleep(interval_high)
        #   hide all layers
        hide_all_layers()
        time.sleep(interval_high)
        #   show layers
        for i in range(6):
            coord = data_coord['layers'][x['surname'][i]]
            pyautogui.click(coord)
        time.sleep(1)
        #   export file toAdobe Media Encoder
        export_file()
        time.sleep(interval_high)

        #increment id
        id_miner += 1
        id_name = translate_id_string(id_miner)