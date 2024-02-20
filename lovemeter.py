import tkinter
import PIL
from PIL import Image, ImageTk
from pygame import mixer
import random
import win32gui
import win32con
import win32api

def setupWindow(wind):
    wind.columnconfigure(0, weight=1)
    wind.columnconfigure(1, weight=1)
    wind.columnconfigure(2, weight=1)

    wind.rowconfigure(0, weight=1)
    wind.rowconfigure(1, weight=1)
    wind.rowconfigure(2, weight=1)

def changeImageInCanvas(canvas, button, name):
    newImg = ImageTk.PhotoImage(Image.open(assetsPath + name))
    canvas.newImg = newImg
    canvas.itemconfig(button, image = newImg)

def changeOnHover(canvas, button, imageOnHover, imageOnLeave):
    canvas.tag_bind(button, "<Enter>", func=lambda e: changeImageInCanvas(canvas, button, imageOnHover))
    canvas.tag_bind(button, "<Leave>", func=lambda e: changeImageInCanvas(canvas, button, imageOnLeave))

def changeBg(name):
    bgImg = ImageTk.PhotoImage(Image.open(assetsPath + name).resize((windowWidth, windowHeight), PIL.Image.Resampling.LANCZOS))
    bgElement.configure(image=bgImg)
    bgElement.bgImg = bgImg

def createBg(frame):
    bgImg = ImageTk.PhotoImage(Image.open(assetsPath + "bg.png").resize((windowWidth, windowHeight), PIL.Image.Resampling.LANCZOS))
    bgEl = tkinter.Label(frame, image=bgImg)
    bgEl.place(relx=0.5, rely=0.5, anchor='center')
    bgEl.bgImg = bgImg
    return bgEl

def createStartButton():
    canvas = tkinter.Canvas(window, width = 200, height = 80, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "start.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    canvas.tag_bind(object1, "<Button-1>", startGame)
    changeOnHover(canvas, object1, "start_d.png", "start.png")
    configureTransparency(canvas)
    return canvas

def createLogo():
    canvas = tkinter.Canvas(window, width = 1000, height = 400, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "logo.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    configureTransparency(canvas)
    return canvas

def createCheckButton():
    canvas = tkinter.Canvas(window, width = 250, height = 255, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "check.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    canvas.tag_bind(object1, "<Button-1>", startMetric)
    changeOnHover(canvas, object1, "check_d.png", "check.png")
    configureTransparency(canvas)
    return canvas

def createDisabledCheckButton():
    canvas = tkinter.Canvas(window, width = 250, height = 255, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "check_o.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    configureTransparency(canvas)
    return canvas

def createNameOneLabel():
    canvas = tkinter.Canvas(window, width = 200, height = 260, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "nameOne.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    configureTransparency(canvas)
    return canvas

def createNameTwoLabel():
    canvas = tkinter.Canvas(window, width = 200, height = 260, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "nameTwo.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    configureTransparency(canvas)
    return canvas

def createLoadingAnimation():
    canvas = tkinter.Canvas(window, width = 400, height = 300, bg='#000000', highlightthickness=0)
    img = tkinter.PhotoImage(file=assetsPath + "hearth.gif", format='gif -index 50')
    frames = [tkinter.PhotoImage(file=assetsPath + "hearth.gif", format='gif -index %i' %(i)) for i in range(120)]
    canvas.img = img
    canvas.frames = frames
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    configureTransparency(canvas)
    return [canvas , object1]

def createTryAgainButton():
    canvas = tkinter.Canvas(window, width = 200, height = 80, bg='#000000', highlightthickness=0)
    img = ImageTk.PhotoImage(Image.open(assetsPath + "tryAgain.png"))
    canvas.img = img
    object1 = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    canvas.tag_bind(object1, "<Button-1>", tryAgain)
    changeOnHover(canvas, object1, "tryAgain_d.png", "tryAgain.png")
    configureTransparency(canvas)
    return canvas

def createTestScoreLabel():
    canvas = tkinter.Canvas(window, width = 180, height = 80, bg='#000000', highlightthickness=0)
    object1 = canvas.create_text(90, 40, text="", fill="white", font=('Arial', 50))
    configureTransparency(canvas)
    return [canvas, object1]

def createTestScoreLabelDescription():
    canvas = tkinter.Canvas(window, width = 380, height = 80, bg='#000000', highlightthickness=0)
    object1 = canvas.create_text(190, 40, text="", fill="white", font=('Arial', 50))
    configureTransparency(canvas)
    return [canvas, object1]

def configureTransparency(canvas):
    window.configure(bg='yellow')
    hwnd = canvas.winfo_id()
    colorkey = win32api.RGB(0, 0, 0) 
    wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,new_exstyle)
    win32gui.SetLayeredWindowAttributes(hwnd, colorkey, 255, win32con.LWA_COLORKEY)

def update(ind):
    frame = loadingAnimation.frames[ind]
    ind += 1
    if ind == len(loadingAnimation.frames) - 1:
        loadingFinished()
        loadingAnimation.itemconfig(loadingAnimationImg, image = loadingAnimation.frames[0])
        return
    loadingAnimation.itemconfig(loadingAnimationImg, image = frame)
    window.after(16, update, ind)

def openMainMenuView():
    startButton.grid(column=1, row=1, sticky=tkinter.S)
    logo.grid(column=1, row=0)

def closeMainMenuView():
    startButton.grid_forget()
    logo.grid_forget()

def openNewGameView():
    checkButtonDisabled.grid(column=1, row=2)
    entryOne.grid(column=0, row=0, sticky=tkinter.W, padx=10)
    entryTwo.grid(column=2, row=0, sticky=tkinter.E, padx=10)
    entryLabelOne.grid(column=0, row=0, sticky=tkinter.W, padx=80)
    entryLabelTwo.grid(column=2, row=0, sticky=tkinter.E, padx=80)
    changeBg("bg2.png")

def closeNewGameView():
    checkButtonDisabled.grid_forget()
    checkButton.grid_forget()
    entryOne.grid_forget()
    entryTwo.grid_forget()
    entryLabelOne.grid_forget()
    entryLabelTwo.grid_forget()

def openMeterLoadingView():
    loadingAnimation.grid(column=1, row=1)
    update(0)

def closeMeterLoadingView():
    loadingAnimation.grid_forget()

def openResultView():
    testScoreLabel.itemconfig(testScoreLabelText, text = testScoreString.get())
    tryAgainButton.grid(column=1, row=2)
    testScoreLabel.grid(column=1, row=0)
    testScoreLabelDescription.grid(column=1, row=1)

def closeResultView():
    tryAgainButton.grid_forget()
    testScoreLabel.grid_forget()
    testScoreLabelDescription.grid_forget()

def startGame(e):
    closeMainMenuView()
    openNewGameView()

def startMetric(e):
    closeNewGameView()
    openMeterLoadingView()
    testScore = random.randint(0, 100)
    testScoreString.set(str(testScore) + "%")
    if testScore >= 0 and testScore <= 19:
        testScoreLabelDescription.itemconfig(testScoreLabelDescriptionText, text = "Awful match")
    elif testScore >= 20 and testScore <= 39:
        testScoreLabelDescription.itemconfig(testScoreLabelDescriptionText, text = "Bad match")
    elif testScore >= 40 and testScore <= 59:
        testScoreLabelDescription.itemconfig(testScoreLabelDescriptionText, text = "Friends")
    elif testScore >= 60 and testScore <= 79:
        testScoreLabelDescription.itemconfig(testScoreLabelDescriptionText, text = "Great match")
    elif testScore >= 80 and testScore <= 100:
        testScoreLabelDescription.itemconfig(testScoreLabelDescriptionText, text = "True love")


def loadingFinished():
    closeMeterLoadingView()
    openResultView()

def tryAgain(e):
    closeResultView()
    nameOne.set("")
    nameTwo.set("")
    openNewGameView()

def traceName(var, index, mode):
    if nameOne.get() != "" and nameTwo.get() != "":
        checkButtonDisabled.grid_forget()
        checkButton.grid(column=1, row=2)
    else:
        checkButton.grid_forget()
        checkButtonDisabled.grid(column=1, row=2)


assetsPath = "./Assets/"
window = tkinter.Tk()
window.title("Lovometr")
window.resizable(False, False)
window.iconbitmap(assetsPath + "icon.ico")

windowWidth = 1280
windowHeight = 720
window.geometry("{}x{}".format(windowWidth, windowHeight))
setupWindow(window)

bgElement = createBg(window)

startButton = createStartButton()

logo = createLogo()

checkButton = createCheckButton()
checkButtonDisabled = createDisabledCheckButton()

nameOne = tkinter.StringVar()
nameTwo = tkinter.StringVar()

nameOne.trace_add('write', traceName)
nameTwo.trace_add('write', traceName)

entryOne = tkinter.Entry(window, textvariable = nameOne, font=('Arial', 24))
entryTwo = tkinter.Entry(window, textvariable = nameTwo, font=('Arial', 24))
entryLabelOne = createNameOneLabel()
entryLabelTwo = createNameTwoLabel()

testScore = 0
testScoreString = tkinter.StringVar()

[loadingAnimation, loadingAnimationImg] = createLoadingAnimation()

tryAgainButton = createTryAgainButton()

[testScoreLabel, testScoreLabelText] = createTestScoreLabel()

[testScoreLabelDescription, testScoreLabelDescriptionText] = createTestScoreLabelDescription()

openMainMenuView()

mixer.init()
mixer.music.load(assetsPath + "bgMusic.mp3")
mixer.music.play(-1)

window.mainloop()
