# -*- coding: utf-8 -*-
"""
Originally created on Fri Jan 20 16:24:08 2023

@author: gitTyler99
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

class Battle:
    def __init__(self):
        self.player_health = 100
        self.ai_health = 100
        self.player_charge = False
        self.ai_charge = False
        self.ai_boost = None
        self.player_history = []
        self.ai_history = []
        self.actions = ["Attack", "Heal", "Charge"]
        self.encoder = LabelEncoder()
        self.encoder.fit(self.actions)
        self.num_classes = len(self.encoder.classes_)
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(LSTM(64, input_shape=(None, self.num_classes), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(64))
        model.add(Dropout(0.2))
        model.add(Dense(self.num_classes, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def start_battle(self):
        player_health_history = []
        ai_health_history = []
        print("Welcome to RNN Battle!")
        print("Your moves are: Attack, Heal, or Charge")
        print("Attack = Causes flat damage of 10")
        print("Heal = Heals 15 health")
        print("Charge = Boosts power for next Attack")
        while self.player_health > 0 and self.ai_health > 0:
            self.player_move = input("Your move (Attack, Heal, Charge): ")
            self.player_history.append(self.player_move)
            self.execute_player_move(self.player_move)
            if self.player_health <= 0 or self.ai_health <= 0:
                break
            self.ai_move = self.encoder.classes_[np.argmax(self.model.predict(np_utils.to_categorical(self.encoder.transform(self.player_history), self.num_classes).reshape(1,-1,self.num_classes)))]
            self.ai_history.append(self.encoder.transform([self.ai_move])[0])
            self.execute_move(self.ai_move)
            print("End Round")
            print("Player health:", self.player_health)
            print("AI health:", self.ai_health)
            player_health_history.append(self.player_health)
            ai_health_history.append(self.ai_health)
            

        if self.player_health <= 0:
            print("You lost.")
        elif self.ai_health <= 0:
            print("You won!")
            
        #For troubleshooting if needed:    
        #print("Player history: ", self.player_history)
        #print("AI history: ", self.ai_history)
        
        #Plot Time-series Line graph of Player and AI actions
        plt.plot(player_health_history, label="Player Health")
        plt.plot(ai_health_history, label="AI Health")
        plt.legend()
        plt.show()
        plt.title("Player and AI Health Over Time")
        plt.xlabel("Time Step (Round Number)")
        plt.ylabel("Health")
        plt.grid()

    def execute_move(self, move):
        if move == "Attack":
            if self.ai_boost:
                self.player_health -= 10 * self.ai_boost
                print("AI attacked for " + str(10 * self.ai_boost))
                self.ai_boost = None
            else:
                self.player_health -= 10
                print("AI attacked for 10 damage")
        elif move == "Heal":
            self.ai_health += 15
            print("AI healed 15 hp")
        elif move == "Charge":
            self.ai_charge = True
            print("AI charged.")
            if self.ai_charge:
                self.ai_charge = False
                self.ai_boost = np.random.uniform(low=1.6, high=3.1)
                print("AI boost:", self.ai_boost)

    def execute_player_move(self, move):
        if move == "Attack":
            if self.player_charge:
                self.ai_health -= 10 * self.player_charge
                print("Player attacked with extra power for " + str(10 * self.player_charge) + " damage!")
                self.player_charge = False
            else:
                self.ai_health -= 10
                print("Player attacked for 10 damage.")
        elif move == "Heal":
            self.player_health += 15
            print("Player healed 15 hp")
        elif move == "Charge":
            self.player_charge = np.random.uniform(low=1.6, high=3.1)
            print("Player boost:", self.player_charge)
    
battle = Battle()
battle.start_battle()

