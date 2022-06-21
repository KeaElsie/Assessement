Question 1

- In the question 1 script declare Counter global 
- Run $ python question.py in the command line
- This you produce results

#Question 2
- To install pytest, run the following in your terminal
 $ sudo apt install python3-pip
 $ sudo pip install -U pytest
- change the inc value to 4 
run the following in your terminal
 $ pytest question2.py
- The results should show a pass test

#Question3
- In Script start with the following
	Import os #To get environmental virables
	Import time #To calculate the time it takes to hit a website
- Add the times variable to the environmental variables
 $ export times=5

- After completing the script, run the following command
 $ python question3.py

#Question 4 
- Create the docker Image for the python script
    1. Create the Dockerfile
	2. Build the Docker Container
		e.g docker image build -t python:0.0.1 /home/roushan/Desktop/Assignment/al-assessemntdocker_assignment
		Allow it to install the dependencies defined/installed.
	3. Verify the container
		docker images


- From the list of images run the Docker which was just created above
	- Run $ docker run -e times=5 <image-name>
 
