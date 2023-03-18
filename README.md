# ML PROJECT
Prerequisites:
1. Python language
2. Modular Programmimg
3. Machine learning
4. Deep Learning


# Tutorials:

1. [GitHub and Environment setup](#agenda-tutorial-1)
2. [Project Structure, logging and exception](#agenda-tutorial-2---end-to-end-ml-project-with-deployment)
3. [Problem Statements, EDA and Modeling](#agenda-tutorial-3---end-to-end-ml-project-with-deployment)
4. [Data Ingestion](#agenda-tutorial-4---end-to-end-ml-project-with-deployment)
5. [Data Tranformation](#agenda-tutorial-5---end-to-end-ml-project-with-deployment)
6. [Model Training and Evaluation Component](#agenda-tutorial-6---end-to-end-ml-project-with-deployment)
7. [Model Hyperparameter Tuning](#agenda-tutorial-7---end-to-end-ml-project-with-deployment)
8. [Predictive Pipeleine using Flask Web app](#agenda-tutorial-8---end-to-end-ml-project-with-deployment)

## **End to End ML Project**
Setup Project with Github
1. Data Ingestion
2. Data Transformation
3. Model Trainer
4. Model Evaluation
5. Model Deployment

CI/CD Pipelines - GitHub Actions
Deployment

# AGENDA: TUTORIAL 1                                      
[back to top](#tutorials)

1. Setup the GitHub {Repository}
      a) new environment
      b) setup.py
      c) requirements.txt

2. src folder and build the package


## Steps to implement the project:

1. Create a GitHub Repository 
   1.1 Keep it public (as per project requirement)
   1.2 Name the project 'ml project'
2. Create a local repository 'mlproject' and open it in text editor like VS Code
3. Create and Activate an environment
   3.1 In terminal create environment
        ```python
        conda create -p venv python==3.8 -y
        ```
   3.2 In terminal activate environmnet 
        ```python
        conda activate venv/
        ```
4. Create a 'README.md' file in 'ml project' folder
5. Sync the GitHub and Local Repositories and push the code to GitHub Repo
    5.1 git init in the activated environmnet
    5.2 Check Git Configuration if not configured then configure it.
       ```python
       git config --global user.name "<Name>"
       git config --global user.email <email with GitHub Account>
       ```
       CHECK GIT CONFIGURATION
            ```python
            git config --global user.name 
            git config --global user.email
            ```
    5.3 Set Remote Repositories
       ```python
       git branch -M main
       git remote add origin <url>
       ```
       Check Remote Repo:
       ```python
       git remote -v
       ```
    5.4 Push README.md to GitHub
       ```python
       git status
       git add README.md
       git commit -m 'README.md added'
       git status
       git remote -v
       git push -u origin main
       ```

6. Create '.gitignore' file in Python in GitHub directly
   6.1 Want to use a .gitignore template? Python
7. Git Pull to make sure code is in sync between GitHub Repo and Base Repo
8. Create 'setup.py' file in 'ml project' folder
   8.1 with the setup.py we will be able to build our entire machine learning application 
   as a package and even deploy in PiPi
   8.2 Create a function 'get_requirements' 
9. Create 'requirements.txt' file
   9.1 Inside pandas numpy seaborn -e .
10. Create 'src' folder in 'ml project' folder
    10.1 Inside src folder create '__init__.py' file
11. In terminal 
    ```python
    pip install -r requirements.txt
    ```
12. 'mlproject.egg-info' indicated that your package is getting installed.
13. push all the files to GitHub.


## Files in "ml project" folders:
1. mlproject.egg-info
2. src
3. venv
4. .gitignore
6. README.md
7. requirements.txt
8. setup.py

   


# AGENDA: TUTORIAL 2 - End To End ML Project With Deployment
[back to top](#tutorials)
1. Project Structure
2. Logging
3. Exception Handling


Follow me for upcoming posts on:
LinkedIn: https://lnkd.in/dfgMwFGT
Code: https://lnkd.in/dG9YDXru


Entire project implementation will be happening inside the Source Folder.
1. Create the "component" folder inside the 'src' folder. Inside the "component" folder, create:
1.1 '__init__.py'
1.2 data_ingestion.py
1.3 data_tranformation.py
1.4 model_trainer.py
Here, we can add "data_validation.py" and "model_evaluation.py"

2. Create "pipeline" Folder inside "src" folder. Inside "pipeline" folder create:
2.1 __init__.py
2.2 train_pipeline.py
2.3 predict_pipeline.py

3. Create three important files inside "src" folder.
3.1 logger.py
3.2 exception.py: Create custom exception.
3.3 utils.py

4. Prepare the logging.py file to log the actions

5. utils.py file will be prepared in next part PART 3

6. Commit the changes in GitHub

Files in "ml project" folders:
1. mlproject.egg-info
2. src
3. venv
4. .gitignore
6. README.md
7. requirements.txt
8. setup.py



# AGENDA: TUTORIAL 3 - End To End ML Project With Deployment
[back to top](#tutorials)
1. Project Structure
2. Exploratory Data Analysis
3. Model Training

Upcoming Tutorial 4: Data Ingestion Implementation 


Learned from : Krish Naik sir



Steps followed in Tutorial 3:

1. Create the "notebook" folder in "mlproject"
Note: Make sure you are in the created environment "venv"



2. Inside "notebook" folder create two .ipynb files:
- EDA
- MODEL TRAINING
Note: Jupyter Notebook is the best for performing EDA. In upcoming tutorials modular programming will be performed for Model Training.


3. Undersatnd the problem statement and collect the data accordingly. 
Note: Here we have used the kaggle dataset for practicing. In real life, we need to collect data from scrapping or load data from databases like MongoDB.



4. Performed Exploratory Data Analysis on dataset
Note: Focus on the problem statement and accordingly perform the required checks on dataset in order to understand the data.
- We need to install the ipykernal, this package provides the IPython kernel for Jupyter. 



5. Performed Model Training
Note: Use .pynb file for ease later tutorials we will convert the code into the modular coding.


6. Make sure you have comment down the required libraries in the requirements.txt and install them in the created environment
Note: comment the .e in requirement.txt as we will create our package in the last then un-comment .e


7. Commit all the changes to the GitHub.


 
# AGENDA: TUTORIAL 4 - End To End ML Project With Deployment 
[back to top](#tutorials)
- Data Ingestion Implementation


# AGENDA: TUTORIAL 5 - End To End ML Project With Deployment 
[back to top](#tutorials)
- Data Tranformation Implementation


# AGENDA: TUTORIAL 6 - End To End ML Project With Deployment 
[back to top](#tutorials)
- Model Training and Evaluation Component

# AGENDA: TUTORIAL 7 - End To End ML Project With Deployment 
[back to top](#tutorials)
- Model Hyperparameter Tuning

# AGENDA: TUTORIAL 8 - End To End ML Project With Deployment 
[back to top](#tutorials)
- Predictive Pipeleine using Flask Web app



 





