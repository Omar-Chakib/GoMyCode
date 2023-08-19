import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")  # Title of the game window
        
        self.player_score = 0
        self.computer_score = 0
        
        # Welcome message label
        self.welcome_label = tk.Label(root, text='Welcome to the Rock-Paper-Scissors Game', font=("Helvetica", 16))
        self.welcome_label.pack()
        
        self.label = tk.Label(root, text="Pick your move:", font=("Helvetica", 14))
        self.label.pack()
        
        self.rock_button = self.create_button("Rock", 1, font=("Helvetica", 12))
        self.paper_button = self.create_button("Paper", 2, font=("Helvetica", 12))
        self.scissors_button = self.create_button("Scissors", 3, font=("Helvetica", 12))
        
        self.score_label = tk.Label(root, text="Player: 0 | AI: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.status_label.pack()

        self.create_reset_button()  # Add the reset button creation here
        self.create_exit_button()

    def create_reset_button(self):
        reset_button = tk.Button(
            self.root,
            text="Reset everyones scores",
            command=self.reset_scores
        )
        reset_button.pack()

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.update_score_label()

    def create_button(self, text, choice, font):
        return tk.Button(
            self.root,
            text=text,
            command=lambda: self.play_game(choice),
            font=font
        ).pack()

    def play_game(self, player_choice):
        player_pick = {1: "Rock", 2: "Paper", 3: "Scissors"}
        
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        
        if "You win" in result:
            self.player_score += 1
        elif "AI wins" in result:
            self.computer_score += 1
        
        self.update_score_label()
        
        message = (
            f"You chose: {player_pick[player_choice]}\n"
            f"The computer chose: {player_pick[computer_choice]}\n"
            f"{result}"
        )
        messagebox.showinfo("Result", message)

    def get_computer_choice(self):
        return random.randint(1, 3)

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "You guys tied"
        elif (
            (player_choice == 1 and computer_choice == 3) or
            (player_choice == 2 and computer_choice == 1) or
            (player_choice == 3 and computer_choice == 2)
        ):
            return "You win this round!, AI lost"
        else:
            return "AI wins this round!, you lose"

    def update_score_label(self):
        self.score_label.config(text=f"Player: {self.player_score} | AI: {self.computer_score}")
        
        if self.player_score == self.computer_score:
            self.status_label.config(text="The scores are tied")
        elif self.player_score > self.computer_score:
            self.status_label.config(text="You are winning")
        else:
            self.status_label.config(text="AI is winning")
        
    def create_exit_button(self):
        exit_button = tk.Button(
            self.root,
            text="Leave game",
            command=self.exit_game
        )
        exit_button.pack()

    def exit_game(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
