# Monty Hall Problem Simulation

This program simulates the **Monty Hall problem**, a probability puzzle based on a game show scenario. The game involves selecting one of three doors. Behind one door is a BMW (the prize), and behind the other two are goats. After making an initial choice, the host reveals a goat behind one of the remaining doors, and you are given the option to either **swap** your choice or **stay** with the original selection. The goal is to determine whether swapping or not swapping leads to a higher chance of winning the prize.

### **How It Works**
1. The player makes an initial choice of a door (0, 1, or 2).
2. The host opens a door with a goat behind it, excluding the player's choice.
3. The player is then given the option to swap to one of the remaining unopened doors or stay with their original choice.
4. The game is repeated for several rounds, and the program tracks the number of wins and losses for both strategies (swap and don't swap).

### **Key Observations**
- **Swapping doors** increases the chances of winning. After many rounds, the probability of winning when you swap is approximately **2/3**, while sticking with your initial choice gives you only a **1/3** chance.
- **Not swapping** results in a lower win rate since you are more likely to have picked a goat initially (2/3 probability).

### **Results Summary**
- **With swapping**: Out of 5 rounds, the player won **3 times**.
- **Without swapping**: Out of 5 rounds, the player won only **1 time**.

This simulation illustrates the counterintuitive nature of the Monty Hall problem: **always swap** for a higher chance of winning!

### **Example Output (Swapping)**

Enter your choice (0, 1, 2): 2
0
Do you want to swap? y/n: y
Player wins

Enter your choice (0, 1, 2): 1
0
Do you want to swap? y/n: y
Player wins

Enter your choice (0, 1, 2): 2
1
Do you want to swap? y/n: y
Player wins

Enter your choice (0, 1, 2): 0
1
Do you want to swap? y/n: y
Player lost

Enter your choice (0, 1, 2): 2
0
Do you want to swap? y/n: y
Player lost

### **Example Output (not Swapping)**
Enter your choice (0, 1, 2): 1
0
Do you want to swap? y/n: n
Player lost

Enter your choice (0, 1, 2): 1
2
Do you want to swap? y/n: n
Player wins

Enter your choice (0, 1, 2): 2
1
Do you want to swap? y/n: n
Player lost

Enter your choice (0, 1, 2): 0
2
Do you want to swap? y/n: n
Player lost

Enter your choice (0, 1, 2): 1
0
Do you want to swap? y/n: n
Player lost
