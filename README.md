# RNN-Battle-ChatGPT
Short description: RPG-style text-based battle that utilizes a Recurrent Neural Network (RNN) for the AI, largely programmed with the assistance of ChatGPT

Original objective: Use ChatGPT to program a simple battle system with a machine learning algorithm for the AI.

Background: ChatGPT originally suggested a logistic regression algorithm and this was implemented with some succcess. When asking ChatGPT how we could improve the AI or make it harder, a RNN was one of the machine learning models suggested (Random Forest model was also implemented and suggested prior to the RNN implementation)

Future work: The initial version of this code features an UN-trained Recurrent Neural Network. Further work can pre-train the AI by logging and storing Player actions or through other method. The logging method would need the following work: 
1) Adding code to log player actions and save them to a file 
2) Train the model on the collected data 
3) Save the weights of the now trained model
4) Modify the original build model function to include weights
5) Initialize the build model function with the pre-trained weights
