from os.path import exists
from modules import functions
from time import strftime
import PySimpleGUI as Gui

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter to-do")
add_button = Gui.Button("Add", button_color='yellow')

window = Gui.Window('To-do app', layout=[[label, input_box, add_button]])
window.read()
window.close()
