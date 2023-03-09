# ML PROJECT
Prerequisites:
1. Python language
2. Modular Programmimg
3. Machine learning
4. Deep Learning

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

   




