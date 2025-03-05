# Recommendation System Course Project Code

This course's code consists of multiple repositories, all of which have been uploaded to the course Git server.  
To facilitate browsing, each code repository is divided into branches according to chapters.  

For example, the `recall-service` repository has two branches, `cp2` and `cp4`, which correspond to the project code for chapters 2 and 4, respectively. If a certain chapter does not have an updated version of the repository, students can use the previous chapter’s code to run the project.

## Repository List
- **dataset**  
  - Course project dataset  
- **recall-service**  
  - Recall service  
- **rank-service**  
  - Ranking service  
- **api-service**  
  - API service  
- **web-service**  
  - Front-end web page  
- **feature-engineer**  
  - Feature engineering-related code  
- **flink-realtime-feature**  
  - Flink real-time feature processing code  

## Running the Entire System
The system consists of multiple modules. To simplify the process, an entry script is provided to start the entire system with a single command.

**Note**: The course scripts are written for Linux/Mac systems. Windows users need to modify the scripts accordingly. **It is highly recommended that Windows users set up a virtual machine or use Linux for project development.**

### Setup Instructions
1. Download the `start.sh` file from this repository to your local machine.  
2. Clone the following repositories into the same directory as `start.sh`:
   - dataset
   - recall-service
   - rank-service
   - api-service
   - web-service  

The final project directory structure should look like this:
- concrec/
  - start.sh
  - dataset/
  - recall-service/
  - rank-service/
  - api-service/
  - web-service/

### Preparing the Environment
Before running the project, navigate into each of the four service directories, switch to the corresponding chapter branch (e.g., `cp2`), and set up a Python virtual environment (this step is only required once):

```sh
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```
Next, open the start.sh script in the root directory and set the absolute path of the dataset folder in the DATASET_PATH variable.
Running the Project
Once everything is set up, run the following command in the root directory: ./start.sh
After starting the project, visit http://localhost:8080 to check the running results.