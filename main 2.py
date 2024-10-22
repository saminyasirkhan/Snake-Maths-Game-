#Initializiation
import pygame
import random
import sys
from pygame.math import Vector2
from pygame import mixer
import sqlite3 as sq

import sys

if "--username" in sys.argv:
    username_index = sys.argv.index("--username")
    if username_index + 1 < len(sys.argv):
        username = sys.argv[username_index + 1]
        print("Username:", username)
    else:
        print("No username provided.")
else:
    print("Username not found in command-line arguments.")


pygame.mixer.pre_init(22050, -16, 1, 1024)
pygame.init()
pygame.font.init()
from Button import Button


# Setting up the database
import sqlite3 as sq

db = sq.connect("database.db")

try:
    st = """
        CREATE TABLE Addition_table
        (Name1 TEXT, Score1 TEXT,Name2 TEXT, Score2 TEXT,Name3 TEXT, Score3 TEXT)
        """
    db.execute(st)
    db.commit()

        # Insert data only once
    insert = "INSERT INTO Addition_table(Name1, Score1,Name2, Score2,Name3, Score3) VALUES ('{}','{}','{}','{}','{}','{}')".format("-", 0,"-", 0,"-", 0)
    db.execute(insert)
    db.commit()

except Exception as e:
    print("Error:", e)

# Getting the info from the database
fetc = """SELECT * FROM Addition_table"""
data = db.execute(fetc)
Addition_elements = []
for row in data:
    # Appending each row as a tuple
    Addition_elements.append((row[0], row[1]))
    Addition_elements.append((row[2], row[3]))
    Addition_elements.append((row[4], row[5]))

print(Addition_elements)




try:
    st = """
        CREATE TABLE Subtract_table
        (Name1 TEXT, Score1 TEXT,Name2 TEXT, Score2 TEXT,Name3 TEXT, Score3 TEXT)
        """
    db.execute(st)
    db.commit()

        # Insert data only once
    insert = "INSERT INTO Subtract_table(Name1, Score1,Name2, Score2,Name3, Score3) VALUES ('{}','{}','{}','{}','{}','{}')".format("-", 0,"-", 0,"-", 0)
    db.execute(insert)
    db.commit()

except Exception as e:
    print("Error:", e)

# Getting the info from the database
fetc = """SELECT * FROM Subtract_table"""
data = db.execute(fetc)
Subtract_elements = []
for row in data:
    # Appending each row as a tuple
    Subtract_elements.append((row[0], row[1]))
    Subtract_elements.append((row[2], row[3]))
    Subtract_elements.append((row[4], row[5]))

print(Subtract_elements)



try:
    st = """
        CREATE TABLE Multiply_table
        (Name1 TEXT, Score1 TEXT,Name2 TEXT, Score2 TEXT,Name3 TEXT, Score3 TEXT)
        """
    db.execute(st)
    db.commit()

        # Insert data only once
    insert = "INSERT INTO Multiply_table(Name1, Score1,Name2, Score2,Name3, Score3) VALUES ('{}','{}','{}','{}','{}','{}')".format("-", 0,"-", 0,"-", 0)
    db.execute(insert)
    db.commit()

except Exception as e:
    print("Error:", e)

# Getting the info from the database
fetc = """SELECT * FROM Multiply_table"""
data = db.execute(fetc)
Multiply_elements = []
for row in data:
    # Appending each row as a tuple
    Multiply_elements.append((row[0], row[1]))
    Multiply_elements.append((row[2], row[3]))
    Multiply_elements.append((row[4], row[5]))

print(Multiply_elements)




try:
    st = """
        CREATE TABLE Divide_table
        (Name1 TEXT, Score1 TEXT,Name2 TEXT, Score2 TEXT,Name3 TEXT, Score3 TEXT)
        """
    db.execute(st)
    db.commit()

        # Insert data only once
    insert = "INSERT INTO Divide_table(Name1, Score1,Name2, Score2,Name3, Score3) VALUES ('{}','{}','{}','{}','{}','{}')".format("-", 0,"-", 0,"-", 0)
    db.execute(insert)
    db.commit()

except Exception as e:
    print("Error:", e)

# Getting the info from the database
fetc = """SELECT * FROM Divide_table"""
data = db.execute(fetc)
Divide_elements = []
for row in data:
    # Appending each row as a tuple
    Divide_elements.append((row[0], row[1]))
    Divide_elements.append((row[2], row[3]))
    Divide_elements.append((row[4], row[5]))

print(Divide_elements)



#Background, Screen, Icons  and images
Cell_size = 22
Cell_number = 22
OFFSET = 75
SCREEN = pygame.display.set_mode(((OFFSET + OFFSET) + Cell_number * Cell_size, (OFFSET + OFFSET) + Cell_number * Cell_size))
BackGroundImage = pygame.image.load("LineBG2.jpg")
BackGroundImage = pygame.transform.scale(BackGroundImage, (SCREEN.get_width(), SCREEN.get_height()))
ICON = pygame.image.load("snake_icon.png")
pygame.display.set_icon(ICON)
pygame.display.set_caption("snake Maths")
fruit_image = pygame.image.load("apple.png")
stone_image = pygame.image.load("stone.png")
bomb_image = pygame.image.load("bomb.png")
explode_image = pygame.image.load("explode.png")

Home = pygame.image.load("home.png")
Home = pygame.transform.scale(Home, (50, 50))


Reset = pygame.image.load("reset.png")
Reset = pygame.transform.scale(Reset, (50, 50))


speaker = pygame.image.load("speaker1.png")
speaker = pygame.transform.scale(speaker, (50, 50))

speaker2 = pygame.image.load("speaker2.png")
speaker2 = pygame.transform.scale(speaker2, (50, 50))



#RGB values and other constants
ORANGE = (251,153,2)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
snake_UPDATE = pygame.USEREVENT
pygame.time.set_timer(snake_UPDATE, 150)

QUESTION_FONT = pygame.font.Font(None, 30)
SCORE_FONT = pygame.font.Font(None, 20)

#-------------------------------------------------------------------------------------------
#Function for growing grid 
def draw_grid(screen, cell_size, cell_number, offset):
    WHITE = (255, 255, 255)
    for y in range(offset, offset + cell_size * cell_number + 1, cell_size):
        pygame.draw.line(screen, WHITE, (offset, y), (offset + cell_size * cell_number, y), 1)
    for x in range(offset, offset + cell_size * cell_number + 1, cell_size):
        pygame.draw.line(screen, WHITE, (x, offset), (x, offset + cell_size * cell_number), 1)
    pygame.draw.rect(screen, BLUE, (offset - 1, offset - 1, cell_size * cell_number + 2, cell_size * cell_number + 2), 2)

#------------------------------------------------------------------------------------------------------------------------

#Classes

class STONE:
    def __init__(self):
        self.position = self.random()

    def random(self):
        x = random.randint(0, Cell_number - 1)
        y = random.randint(0, Cell_number - 1)
        return Vector2(x, y)

    def draw(self):
        stone_rect = pygame.Rect(OFFSET + self.position.x * Cell_size, OFFSET + self.position.y * Cell_size, Cell_size, Cell_size)
        stone_image_scaled = pygame.transform.scale(stone_image, (Cell_size, Cell_size))
        SCREEN.blit(stone_image_scaled, stone_rect)

    def check_collision(self, snake_head):
        return snake_head == self.position
    


class Bomb:
    def __init__(self):
        self.position = self.random()
        self.explode = False

    def random(self):
        x = random.randint(0, Cell_number - 1)
        y = random.randint(0, Cell_number - 1)
        return Vector2(x, y)

    def draw(self):
        if self.explode:
            Bomb_rect = pygame.Rect(OFFSET + self.position.x * Cell_size, OFFSET + self.position.y * Cell_size, Cell_size, Cell_size)
            Bomb_image_scaled = pygame.transform.scale(explode_image, (Cell_size, Cell_size))
        else:
            Bomb_rect = pygame.Rect(OFFSET + self.position.x * Cell_size, OFFSET + self.position.y * Cell_size, Cell_size, Cell_size)
            Bomb_image_scaled = pygame.transform.scale(bomb_image, (Cell_size, Cell_size))
        SCREEN.blit(Bomb_image_scaled, Bomb_rect)

    def check_collision(self, snake_head):
        if snake_head == self.position:
            self.explode = True

      
        return snake_head == self.position
    


class FRUIT:
    def __init__(self, correct_answer = None, incorrect_answer = None):
        self.position = self.random()
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answer
        self.is_correct = random.choice([True, False])

    def random(self):
        x = random.randint(0, Cell_number - 1)
        y = random.randint(0, Cell_number - 1)
        return Vector2(x, y)
    
    def generate_answers(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2  # For addition questions, you can change this as needed
        incorrect_answer = correct_answer + random.randint(1, 5)  # Generate an incorrect answer
        return correct_answer, incorrect_answer

    def draw(self):
        fruit_rect = pygame.Rect(OFFSET + self.position.x * Cell_size, OFFSET + self.position.y * Cell_size, Cell_size, Cell_size)
        fruit_image_scaled = pygame.transform.scale(fruit_image, (Cell_size, Cell_size))
        SCREEN.blit(fruit_image_scaled, fruit_rect)

        value_text = str(self.correct_answer) if self.is_correct else str(self.incorrect_answer)
        value_surface = SCORE_FONT.render(value_text, True, (0, 0, 0))  # Black color
        value_rect = value_surface.get_rect(center=fruit_rect.center)  # Center the text on the fruit
        SCREEN.blit(value_surface, value_rect)

class Snake:
    def __init__(self):
        self.body = [Vector2(6,9) , Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_part = False
        self.chewing_sound = pygame.mixer.Sound("Sound/eat.mp3")
        self.mistake_sound = pygame.mixer.Sound("Sound/wall.mp3")
        self.growth_count = 0  # Keep track of how many parts the snake has grown

    
    def draw(self):
        for part in self.body:
            parts_rect = (OFFSET + part.x * Cell_size, OFFSET + part.y * Cell_size, Cell_size, Cell_size)
            pygame.draw.rect(SCREEN, ORANGE, parts_rect, 0, 7)

    def movement(self):
        self.body.insert(0,self.body[0] + self.direction)
        if self.add_part and self.growth_count < 14: #(For some reaoson when you set the growth count to 10 it only grows 8 parts)
            self.growth_count += 1
        else:
            # If the snake has reached the maximum growth, remove the last part
            self.body = self.body[:-1]
        self.add_part = False
           

    def grow(self):
        # Check if the snake can grow (up to a maximum of 10 parts)
        if self.growth_count < 14: #(For some reaoson when you set the growth count to 10 it only grows 8 parts)
            self.add_part = True
            self.growth_count += 1

    def reset_position(self):
        self.body = [Vector2(6,9) , Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.growth_count = 0
            
class GAME:
    initial_timer_duration = 10000  # Initial timer duration (10 seconds)
    def __init__(self,mode):
        self.SCREEN = SCREEN  
        self.fruit = FRUIT()
        self.fruit2 = FRUIT()
        self.snake = Snake()
        self.stone = STONE()  
        self.mode = mode
        self.bomb = Bomb()  
        self.name = username
        self.get_name = False
        self.home_rect = pygame.Rect(180,400,50,50)
        self.play_again_rect = pygame.Rect(280,400,50,50)
        self.mute_rect = pygame.Rect(380,400,50,50)
        
        
        
       
        self.SCREEN = SCREEN
        self.state = "ready"
        self.score = 0
        self.playing_music = False
        self.play_background_music()

        # Timer attributes
        self.initial_timer_duration = 11000  # Initial timer duration (10 seconds)
        self.time_left = self.initial_timer_duration  # Initial time for answer selection
        self.timer_start_time = pygame.time.get_ticks()
        self.timer_duration = self.initial_timer_duration  # Actual timer duration
        self.start_time = pygame.time.get_ticks()  # Record the start time when the game starts

        #Maths attributes 
        
        self.correct_answer = 0
        self.incorrect_answer = 0
        self.current_question = ""
        self.selected_operation = "addition"
        self.generate_question()
    
    #Displays time runnning    
        
    def draw_timer(self):
        time_remaining = self.update_timers()
        timer_text = f"Time left: {time_remaining // 1000} s"
        timer_surface = SCORE_FONT.render(timer_text, True, (255, 0, 0))
        timer_rect = timer_surface.get_rect(topright=(self.SCREEN.get_width() - 10, 20))
        self.SCREEN.blit(timer_surface, timer_rect)

    def update_timers(self):
        # Calculate the time elapsed since the timer started
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.timer_start_time

        # Calculate the time remaining
        time_remaining = max(0, self.timer_duration - elapsed_time)

        # Handle decreasing timer duration based on score
        if self.score >= 10:
            self.timer_duration = 9000  # Decrease by 1 second
        elif self.score >= 20:
            self.timer_duration = 8000 
        elif self.score >= 230:
            self.timer_duration = 7000 
        elif self.score >= 40:
            self.timer_duration = 6000  
        elif self.score >= 50:
            self.timer_duration = 5000  # Set to 5 seconds

        # Check if time is up
        if time_remaining == 0:
            self.game_over()  # Time's up, end the game

        return time_remaining

    def reset_timer(self):
        self.timer_start_time = pygame.time.get_ticks()
        self.timer_duration = self.initial_timer_duration

    def calculate_time_survived(self):
        current_time = pygame.time.get_ticks()  # Get the current time
        time_survived = current_time - self.start_time  # Calculate time survived
        return time_survived
    
    def draw_time_survived(self):
        time_survived = self.calculate_time_survived()
        time_text = f"Time Survived: {time_survived // 1000} s"
        time_surface = SCORE_FONT.render(time_text, True, (255, 0, 0))
        time_rect = time_surface.get_rect(topright=(self.SCREEN.get_width() - 10, 50))
        self.SCREEN.blit(time_surface, time_rect)


    # Maths Logic and functionality
    def generate_question(self):
       
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        self.incorrect_answer = self.generate_incorrect_answer(self.correct_answer)
        if self.mode != "":
            if self.mode =='addition':
                self.correct_answer = num1 + num2
            if self.mode =='subtract':
                self.correct_answer = num1 - num2

            if self.mode =='multiply':
                self.correct_answer = num1 * num2

            if self.mode =='divide':
                while num1 < num2 or num1 == 0 or num2 == 0 or num1 % num2 != 0:
                    num1 = random.randint(1, 40)
                    num2 = random.randint(1, 10)
                self.correct_answer = num1 // num2
            

            # Reset timer duration to initial value
            self.timer_duration = self.initial_timer_duration
            
            # Generate the first incorrect answer
            while True:
                self.incorrect_answer = self.generate_incorrect_answer(self.correct_answer)
                if self.incorrect_answer is not None and self.incorrect_answer != self.correct_answer:
                    break

            # Generate the second correct and incorrect answers
            while True:
                num1_2 = random.randint(1, 10)
                num2_2 = random.randint(1, 10)
                if self.mode =='addition':
                    self.correct_answer2 = num1_2 + num2_2
                if self.mode =='subtract':
                    self.correct_answer2 = num1_2 - num2_2

                if self.mode =='multiply':
                    self.correct_answer2 = num1_2 * num2_2

                if self.mode =='divide':
                    while num1_2 < num2_2  or num1_2  == 0 or num2_2  == 0 or num1_2  % num2_2  != 0:
                        num1_2  = random.randint(1, 40)
                        num2_2  = random.randint(1, 10)
                    self.correct_answer2 = num1_2 // num2_2




                self.incorrect_answer2 = self.generate_incorrect_answer(self.correct_answer2)

                if self.correct_answer2 != self.correct_answer and self.incorrect_answer2 != self.correct_answer:
                    break

            # Choose randomly which fruit will have the correct answer
            correct_fruit = random.choice([self.fruit, self.fruit2])
            correct_fruit.correct_answer = self.correct_answer
            correct_fruit.incorrect_answer = self.incorrect_answer
            correct_fruit.is_correct = True

            incorrect_fruit = self.fruit2 if correct_fruit is self.fruit else self.fruit
            incorrect_fruit.correct_answer = self.correct_answer2
            incorrect_fruit.incorrect_answer = self.incorrect_answer2
            incorrect_fruit.is_correct = False

            # Generate the current question string
            if self.mode =='addition':
                self.current_question = f"{num1} + {num2}"
            if self.mode =='subtract':
                self.current_question = f"{num1} - {num2}"

            if self.mode =='multiply':
                self.current_question = f"{num1} * {num2}"

            if self.mode =='divide':
                self.current_question = f"{num1} / {num2}"
            

            self.timer_start_time = pygame.time.get_ticks()


    def generate_incorrect_answer(self, correct_answer, other_incorrect_answer=None):
    # Generate an incorrect answer that is not equal to the correct answer
        while True:
            incorrect_answer = random.randint(1, 20)  # Adjust the range as needed
            if incorrect_answer != correct_answer and incorrect_answer != other_incorrect_answer:
                return incorrect_answer

    def load_background_music(self):
        pygame.mixer.music.load("Sound/bg_music_1.mp3")
     

    def play_background_music(self):
        
        if not self.playing_music:
            pygame.mixer.music.load("Sound/bg_music_1.mp3")  # Load the music file
            pygame.mixer.music.play(-1)  # Start playing
            self.playing_music = True

    def draw(self):
        self.snake.draw()
        self.fruit.draw()
    
        # Display the current question using an f-string
        question_text = f"Question: {self.current_question}"
        question_surface = QUESTION_FONT.render(question_text, True, (255, 0, 0))
        question_rect = question_surface.get_rect(topleft=(OFFSET + 10, 20))
        self.SCREEN.blit(question_surface, question_rect)

        question_surface = QUESTION_FONT.render('score: '+str(self.score), True, (255,0, 0))

        self.SCREEN.blit(question_surface,(500,600))
   
   
    def update(self):
        if self.state == "ready":
            self.play_background_music() 
            self.snake.movement()
            self.collision_with_fruit()
            self.boundary_check()
            self.collision_with_body()
            self.draw_time_survived()  # Draw the "Time Survived" on the screen
            self.collision_with_stone() # Handles the any collisions with the stone



    def collision_with_fruit(self):
        if self.snake.body[0] == self.fruit.position:
            if self.fruit.is_correct:  # Check if the fruit contains the correct answer
                self.snake.grow()
                self.score += 1
                self.fruit.position = self.fruit.random()  # Generate a new random position for the first fruit
                self.fruit2.position = self.fruit2.random()  # Generate a new random position for the second fruit
                self.generate_question()
                self.reset_timer()
                
            else:
                self.game_over()  # snake hit the incorrect answer
            self.fruit.position = self.fruit.random()  # Generate a new fruit position

        elif self.snake.body[0] == self.fruit2.position:
            if self.fruit2.is_correct:  # Check if the fruit2 contains the correct answer
                self.snake.grow()
                self.score += 1
                self.fruit.position = self.fruit.random()  # Generate a new random position for the first fruit
                self.fruit2.position = self.fruit2.random()  # Generate a new random position for the second fruit
                self.generate_question()
                self.reset_timer()
                # Respawn the stone randomly when the score goes up
                self.stone.position = self.stone.random()
                self.bomb.position = self.bomb.random()
            else:
                self.game_over()  # snake hit the incorrect answer

        

    def boundary_check(self):
        if self.snake.body[0].x == Cell_number or self.snake.body[0].x == -1:
            self.game_over()
            print("Boundary Check - Timer Start Time:", self.timer_start_time)
            print("Boundary Check - Time Left:", self.time_left)
            self.reset_timer()
       
        if self.snake.body[0].y == Cell_number or self.snake.body[0].y == -1:
            self.game_over()  
            print("Boundary Check - Timer Start Time:", self.timer_start_time)
            print("Boundary Check - Time Left:", self.time_left) 
            self.reset_timer()  # Reset timer when snake hits boundaries
            
    
    def collision_with_body(self):
        for part in self.snake.body[1:]:
            if self.snake.body[0] == part:
                self.reset_timer()  # Reset timer when snake hits itself
                self.game_over()
                print("Collision with Body - Timer Start Time:", self.timer_start_time)
                print("Collision with Body - Time Left:", self.time_left)

    def collision_with_stone(self):
        if self.snake.body[0] == self.stone.position or self.snake.body[0] == self.bomb.position:
            self.bomb.explode = True
            self.bomb.draw()

            
            self.game_over()  # snake collided with the stone
            self.reset_timer()
            self.stone.position = self.stone.random()
            self.bomb.position = self.bomb.random() 
            
            
     
    
    
    def reset_game(self):
        # Reset game attributes to their initial state
        self.fruit = FRUIT()
        self.snake = Snake()
        self.get_name = False
        self.state = "ready"
        self.play_background_music()
        self.bomb.explode = False
        # self.name= ''
        self.score = 0
        self.stone.position = self.stone.random() 
        self.bomb.position = self.bomb.random() 

        # Generate new question values for both fruits
        self.generate_question()
        self.fruit2.generate_answers()  # Generate answers for the second fruit
        self.reset_timer()  # Reset the timer

    def draw_score(self):
        score_text = f"Score: {self.score}"
        score_surface = SCORE_FONT.render(score_text, True, (255, 0, 0))
        score_rect = score_surface.get_rect(bottomleft=(OFFSET + 10, self.SCREEN.get_height() - 10))  # Display at the bottom left
        self.SCREEN.blit(score_surface, score_rect)

    def game_over(self):
        pygame.mixer.music.stop()  # Stop background music
        self.snake.reset_position()
        self.fruit.random()
        self.start_time = pygame.time.get_ticks()  # Reset the start time when the game is over
        self.state = "not ready" 
        final_score = self.score 
        self.playing_music = False
        
     
        print("Final Score:", self.score)

        font = pygame.font.Font(None, 48)
        text = font.render(f"Final Score: {self.score} ", True, (0,0,0))
        text_rect = text.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2))
        start_text = font.render("Better luck next time", True, (0,0,0))
        start_text_rect = start_text.get_rect(center=(self.SCREEN.get_width() // 2, self.SCREEN.get_height() // 2 + 50))
        self.SCREEN.blit(text, text_rect)
        self.SCREEN.blit(start_text, start_text_rect)
        SCREEN.blit(Home,(self.home_rect.x,self.home_rect.y))
        
       
        # pygame.draw.rect(SCREEN,'red',self.play_again_rect)
        SCREEN.blit(Reset,(self.play_again_rect.x,self.play_again_rect.y))
        if self.mode == 'addition':
            if self.score> int(Addition_elements[0][1]) or self.score> int(Addition_elements[1][1]) or self.score> int(Addition_elements[2][1]):
                self.get_name = True
                
        if self.mode == 'subtract':
            if self.score> int(Subtract_elements[0][1]) or self.score> int(Subtract_elements[1][1]) or self.score> int(Subtract_elements[2][1]):
                self.get_name = True


        if self.mode == 'multiply':
            if self.score> int(Multiply_elements[0][1]) or self.score> int(Multiply_elements[1][1]) or self.score> int(Multiply_elements[2][1]):
                self.get_name = True


        if self.mode == 'divide':
            if self.score> int(Divide_elements[0][1]) or self.score> int(Divide_elements[1][1]) or self.score> int(Divide_elements[2][1]):
                self.get_name = True
        
        


        pygame.display.update()

        self.reset_timer()  # Reset timer when the game is over

        waiting_for_input = True
        while waiting_for_input:
            if self.playing_music :
            
                SCREEN.blit(speaker2,(self.mute_rect.x,self.mute_rect.y))
            else:
                SCREEN.blit(speaker,(self.mute_rect.x,self.mute_rect.y))
            MOUSE_POS = pygame.mouse.get_pos()
            
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.mute_rect.collidepoint(MOUSE_POS[0],MOUSE_POS[1]):
                        if self.playing_music:
                            self.playing_music = False
                            
                        else:
                            self.playing_music = True

                   

                    if self.play_again_rect.collidepoint(MOUSE_POS[0],MOUSE_POS[1]) or self.home_rect.collidepoint(MOUSE_POS[0],MOUSE_POS[1]):
                        if True:
                           
                            if self.mode == 'addition':
                                if self.score> int(Addition_elements[0][1]):
                                    Insert=f'''UPDATE Addition_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Addition_elements[1][1]):
                                    Insert=f'''UPDATE Addition_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Addition_elements[2][1]):
                                    Insert=f'''UPDATE Addition_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name3 = '{self.name}' '''



                            if self.mode == 'subtract':
                                if self.score> int(Subtract_elements[0][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Subtract_elements[1][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Subtract_elements[2][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name3 = '{self.name}' '''


                            

                            if self.mode == 'multiply':
                                if self.score> int(Multiply_elements[0][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Multiply_elements[1][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Multiply_elements[2][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name3 = '{self.name}' '''





                            if self.mode == 'divide':
                                if self.score> int(Divide_elements[0][1]):
                                    Insert=f'''UPDATE Divide_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Divide_elements[1][1]):
                                    Insert=f'''UPDATE Divide_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Divide_elements[2][1]):
                                    Insert=f'''UPDATE Divide_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name3 = '{self.name}' '''
                            try:
                                db.execute(Insert)
                                db.commit()
                                db.execute(Insert2)
                                db.commit()
                            except:
                                pass

                        self.reset_game()  # Reset the game state
                        waiting_for_input = False
                    if self.home_rect.collidepoint(MOUSE_POS[0],MOUSE_POS[1]):
                        menu()

                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # Restart the game on spacebar press
                        if True:
                            if self.mode == 'addition':
                                if self.score> int(Addition_elements[0][1]):
                                    Insert=f'''UPDATE Addition_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Addition_elements[1][1]):
                                    Insert=f'''UPDATE Addition_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Addition_elements[2][1]):
                                    Insert=f'''UPDATE Addition_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Addition_table SET Name3 = '{self.name}' '''



                            if self.mode == 'subtract':
                                if self.score> int(Subtract_elements[0][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Subtract_elements[1][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Subtract_elements[2][1]):
                                    Insert=f'''UPDATE Subtract_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Subtract_table SET Name3 = '{self.name}' '''


                            

                            if self.mode == 'multiply':
                                if self.score> int(Multiply_elements[0][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Multiply_elements[1][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Multiply_elements[2][1]):
                                    Insert=f'''UPDATE Multiply_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Multiply_table SET Name3 = '{self.name}' '''





                            if self.mode == 'divide':
                                if self.score> int(Divide_elements[0][1]):
                                    Insert=f'''UPDATE Divide_table SET Score1={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name1 = '{self.name}' '''

                                elif self.score> int(Divide_elements[1][1]):
                                    Insert=f'''UPDATE Divide_table SET Score2={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name2 = '{self.name}' '''

                                elif self.score> int(Divide_elements[2][1]):
                                    Insert=f'''UPDATE Divide_table SET Score3={self.score}'''
                                    Insert2 = f'''UPDATE Divide_table SET Name3 = '{self.name}' '''
                            try:
                                db.execute(Insert)
                                db.commit()
                                db.execute(Insert2)
                                db.commit()
                            except:
                                pass

                        self.reset_game()  # Reset the game state
                        waiting_for_input = False
                        
                    if event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]

                    else:
                        self.name+=event.unicode
                        print(self.name)

            pygame.display.update()



# Create a function to display rows of text
def draw_rows():
    row_height = 33
    y = 100  # Adjust the starting position as needed
    pygame.draw.rect(SCREEN,'black',(SCREEN.get_width()// 2,100,5,100))

    pygame.draw.rect(SCREEN,'black',(SCREEN.get_width()// 2,235,5,100))

    pygame.draw.rect(SCREEN,'black',(SCREEN.get_width()// 2,367,5,100))

    pygame.draw.rect(SCREEN,'black',(SCREEN.get_width()// 2,497,5,100))
    for i in range(16):
        pygame.draw.rect(SCREEN,'black',(0,y,SCREEN.get_width(),5))
        if i<3:
            text = QUESTION_FONT.render(Addition_elements[i][0]+ '                       '+Addition_elements[i][1], True, 'red')
            text_rect = text.get_rect()
            text_rect.center = (SCREEN.get_width()// 2, y+25)  # Center the text horizontally in each row
            SCREEN.blit(text, text_rect)



            text = QUESTION_FONT.render(Subtract_elements[i][0]+ '                       '+Subtract_elements[i][1], True, 'red')
            text_rect = text.get_rect()
            text_rect.center = (SCREEN.get_width()// 2, y+155)  # Center the text horizontally in each row
            SCREEN.blit(text, text_rect)


            text = QUESTION_FONT.render(Multiply_elements[i][0]+ '                       '+Multiply_elements[i][1], True, 'red')
            text_rect = text.get_rect()
            text_rect.center = (SCREEN.get_width()// 2, y+285)  # Center the text horizontally in each row
            SCREEN.blit(text, text_rect)


            text = QUESTION_FONT.render(Divide_elements[i][0]+ '                       '+Divide_elements[i][1], True, 'red')
            text_rect = text.get_rect()
            text_rect.center = (SCREEN.get_width()// 2, y+415)  # Center the text horizontally in each row
            SCREEN.blit(text, text_rect)
            
        y += row_height
    
    text = QUESTION_FONT.render("Addition Highscores", True, 'red')
    text_rect = text.get_rect()
    text_rect.center = (SCREEN.get_width()// 2, 90)  # Center the text horizontally in each row
    SCREEN.blit(text, text_rect)

    text = QUESTION_FONT.render("Subtraction Highscores", True, 'red')
    text_rect = text.get_rect()
    text_rect.center = (SCREEN.get_width()// 2, 220)  # Center the text horizontally in each row
    SCREEN.blit(text, text_rect)

    text = QUESTION_FONT.render("Multiplication Highscores", True, 'red')
    text_rect = text.get_rect()
    text_rect.center = (SCREEN.get_width()// 2, 350)  # Center the text horizontally in each row
    SCREEN.blit(text, text_rect)

    text = QUESTION_FONT.render("Division Highscores", True, 'red')
    text_rect = text.get_rect()
    text_rect.center = (SCREEN.get_width()// 2, 480)  # Center the text horizontally in each row
    SCREEN.blit(text, text_rect)

# Main loop
def leader_score():
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill((255, 255, 255))  # Use a tuple for the color

        # Draw rows
        draw_rows()

        # Create a "Back" button
        Back = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-190,50)), pos=(80,40), 
                            text_input="Back", font=SCORE_FONT, base_color=(0, 0, 0), hovering_color=(0, 255, 0))
        
        for button in [Back]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back.checkForInput(MOUSE_POS):
                    menu()

        pygame.display.update()
#-----------------------------------------------------------------------------------------
#Game Loop
def menu():
    img = pygame.transform.scale(pygame.image.load('math_symbol.png'),(120,120))
    while True:
        SCREEN.fill('white')
        SCREEN.blit(img,(50,30))
        pygame.draw.rect(SCREEN,'black',(0,600,1000,5))
        pygame.draw.rect(SCREEN,'grey',(SCREEN.get_width()/2+10,190,280,335))
        MOUSE_POS = pygame.mouse.get_pos()
        Addition = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-80,70)), pos=(SCREEN.get_width()/2+150, SCREEN.get_height()/2-80), 
                            text_input="Addition", font=SCORE_FONT, base_color="black", hovering_color="green")
        
        Subtraction = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-80,70)), pos=(SCREEN.get_width()/2+150, SCREEN.get_height()/2), 
                            text_input="Subtraction", font=SCORE_FONT, base_color="black", hovering_color="green")
        
        Multiply = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-80,70)), pos=(SCREEN.get_width()/2+150, SCREEN.get_height()/2+80), 
                            text_input="Multiplication", font=SCORE_FONT, base_color="black", hovering_color="green")
        
        Divide = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-80,70)), pos=(SCREEN.get_width()/2+150, SCREEN.get_height()/2+160), 
                            text_input="Division", font=SCORE_FONT, base_color="black", hovering_color="green")
        
        Leaderboard = Button(image=pygame.transform.scale(pygame.image.load("Options Rect2.png"),(SCREEN.get_width()/2-80,70)), pos=(SCREEN.get_width()/2-150, SCREEN.get_height()/2+240), 
                            text_input="Leaderboard", font=SCORE_FONT, base_color="black", hovering_color="green")


        # Showing buttons
        for button in [Addition,Subtraction,Multiply,Divide,Leaderboard]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Addition.checkForInput(MOUSE_POS):
                    run_game('addition')

                if Subtraction.checkForInput(MOUSE_POS):
                    run_game('subtract')

                if Multiply.checkForInput(MOUSE_POS):
                    run_game('multiply')

                if Divide.checkForInput(MOUSE_POS):
                    run_game('divide')

                if Leaderboard.checkForInput(MOUSE_POS):
                    leader_score()
                

        pygame.display.update()


def run_game(mode):
    
    game = GAME(mode)
    FPS = 60
    RUN = True

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                sys.exit()
            if event.type == snake_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if game.state == "not ready" and event.key == pygame.K_SPACE:
                    game.state = "ready"  # Change the game state to "ready"
                    game.reset_game()
                    waiting_for_input = False
                elif game.state == "ready":
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if game.snake.direction != Vector2(0, 1):
                            game.snake.direction = Vector2(0, -1)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if game.snake.direction != Vector2(0, -1):
                            game.snake.direction = Vector2(0, 1)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if game.snake.direction != Vector2(1, 0):
                            game.snake.direction = Vector2(-1, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if game.snake.direction != Vector2(-1, 0):
                            game.snake.direction = Vector2(1, 0)

        SCREEN.blit(BackGroundImage, (0, 0))
        pygame.draw.rect(SCREEN, BLUE, (OFFSET - 5, OFFSET - 5, Cell_size * Cell_number + 10, Cell_size * Cell_number + 10), 5)
        game.snake.draw()
        game.fruit.draw()
        game.fruit2.draw()
        game.stone.draw()
        game.bomb.draw()
        game.draw()
        game.draw_timer()
        game.draw_time_survived()
        pygame.display.update()
        pygame.draw.rect(SCREEN, BLUE, (OFFSET - 5, OFFSET - 5, Cell_size * Cell_number + 10, Cell_size * Cell_number + 10), 5)

    pygame.quit()

if __name__ == '__main__':
    menu()


