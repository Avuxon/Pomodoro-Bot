# Track statuses for Pomodoro method
import time

breakStatus = False
pomoStatus = False
noSession = False

def getStatus(msg, session, telegram):
    if noSession:
      telegram.sendMessage(msg.chat.id, "No pomodoro session is currently running.")

    elif pomoStatus :
      elapsedTime = Number((25 - ((Date.now() - timeOutStart) / 1000) / 60).toFixed(1))
      telegram.sendMessage(msg.chat.id, `Session "${session}" is currently running. You have ${elapsedTime} minute(s) left.`)

    elif breakStatus:
      elapsedTime = Number((7 - ((Date.now() - timeOutStart) / 1000) / 60).toFixed(1))
      telegram.sendMessage(msg.chat.id, `You're on break from "${session}"! You have ${elapsedTime} minute(s) left before work.`)
    