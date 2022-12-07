# CS-466-Final-Project
Nussinov Algorithm 

iakella2, psadat2, deeyab2, nidhisd2

Our motivation behind this project is that the Nussinov algorithm allows us to predict the 3D structure of an RNA molecule based on its sequence alone and can help us better understand the function of RNA molecules based on their structure. It is a dynamic programming algorithm that takes a string of nucleotides and a set of base pairings as an input and outputs the maximum amount of base pairings that can form loop structures within an RNA molecule. 

To run our algorithm, make sure you have this git repo cloned on you computer and Python installed. We ran our code on Python 3.7.10. Once you open the code in an editor, run the command 'python Nussinov_Backtrace.py' on your terminal to run the algorithm. The output of the algorithm will display in your terminal, however, if you would like to see it output to a text file simply run 'python Nussinov_Backtrace.py > output.txt'! To input a nucleotide of your choosing, you have to go to Nussinov.Backtrace.py and edit the strings in the main function. To clarify, your input should be given as a string of characters representing the nucelotide sequence and you pass the string into the 'nussinov()' call in the main function.