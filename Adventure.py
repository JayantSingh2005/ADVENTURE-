import tkinter as tk
from tkinter import simpledialog, messagebox


class AdventureGameApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Adventure Game")

    self.label = tk.Label(root,
                          text="Welcome to this adventure game!",
                          font=("Arial", 12))
    self.label.pack(pady=10)

    self.start_button = tk.Button(root, text="Start", command=self.start_game)
    self.start_button.pack(pady=5)

  def start_game(self):
    name = simpledialog.askstring("Adventure Game", "Type your name:")
    if name:
      messagebox.showinfo("Adventure Game",
                          f"Welcome, {name}, to this adventure!")
      self.play_game()
    else:
      messagebox.showerror("Error", "Please enter your name.")

  def play_game(self):
    answer1 = simpledialog.askstring(
        "Adventure Game",
        "You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right)"
    ).lower()

    if answer1 == "left":
      answer2 = simpledialog.askstring(
          "Adventure Game",
          "You come to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across:"
      ).lower()

      if answer2 == "swim":
        messagebox.showinfo(
            "Adventure Game",
            "You swam across and were eaten by an alligator. Game Over.")
      elif answer2 == "walk":
        messagebox.showinfo(
            "Adventure Game",
            "You walked for many miles, ran out of water, and lost the game.")
      else:
        messagebox.showerror("Error", "Not a valid option. You lose.")

    elif answer1 == "right":
      answer3 = simpledialog.askstring(
          "Adventure Game",
          "You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back)"
      ).lower()

      if answer3 == "back":
        messagebox.showinfo("Adventure Game", "You go back and lose.")
      elif answer3 == "cross":
        answer4 = simpledialog.askstring(
            "Adventure Game",
            "You cross the bridge and meet a stranger. Do you talk to them? (yes/no)"
        ).lower()

        if answer4 == "yes":
          messagebox.showinfo(
              "Adventure Game",
              "You talk to the stranger and they give you gold. You WIN!")
        elif answer4 == "no":
          messagebox.showinfo(
              "Adventure Game",
              "You ignore the stranger and they are offended. You lose.")
        else:
          messagebox.showerror("Error", "Not a valid option. You lose.")
      else:
        messagebox.showerror("Error", "Not a valid option. You lose.")

    else:
      messagebox.showerror("Error", "Not a valid option. You lose.")

    messagebox.showinfo("Adventure Game", f"Thank you for playing, {name}!")


if __name__ == "__main__":
  root = tk.Tk()
  app = AdventureGameApp(root)
  root.mainloop()
