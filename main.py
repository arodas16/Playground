from tkinter import *

def notes_clip():
  print("\n" + "Notes have been copied to clipboard")

def email_clip():
  print("\n" + "Email has been copied to clipboard")

def submit_how_to():
  how_to_request = (how_to_entry.get())
  hca = (hca_entry.get())

  case_closed = ("I was happy to assist you on your recent call with Google Workspace support regarding how to " + how_to_request + ", this Help Center article best addresses the issue you called in for " + hca + "\n" *2 + "This case will be closed as the issue has been resolved. Should you require any further assistance on this topic, you can reopen this case within 30 days by replying to this email. You can also contact us by following one of the methods described at https://support.google.com/a/answer/1047213	")

  notes_out = ("**HANDLED BY GENERALIST**" + "\n" + "**  CCA INFORMATION	" + "\n" + "-Reason for the call: how to " + "\n" + "-Issue identification: doesnt know how to " + "\n" + "💬 Selected TAG reasoning: assisted cx with how to " + "\n" + "**  CASE RELEVANT INFORMATION	" + "\n" + "-Case origin: Inbound Call" + "\n" + "🔧 Issue Resolution: instructed cx on how to " + "\n" + "-Relevant information or secondary issues/questions:" + "\n" + "-Case status: Case Closed" + "\n" + "-Email verified as valid: SMTP test completed successfully" + "\n" + "Click2Call - No PIN	")


  print(case_closed)
  print("\n")
  print(notes_out)

def clear_how_to():
  how_to_entry.delete(0,END)
  hca_entry.delete(0,END)
  print("\n" + "Page has have been cleared")

def quit_clippy():
  print("\n" + "Clippy has been quit")

def insert_notes():
  print("\n" + "These are your notes")

root = Tk()
root.title("Clippy")
root.minsize(800,250)

# this is the menu

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit_clippy, accelerator="(Ctrl + Q)")

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy notes", command=notes_clip)
editMenu.add_command(label="Copy email", command=email_clip)


# this is the toolbar

toolbar = Frame(root)

how_to_label = Label(toolbar, text="How to: ")
how_to_label.pack(side=LEFT, padx=1, pady=1)