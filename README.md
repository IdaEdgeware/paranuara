

# API Endpoints
| HTTP Method | URL | Action |
| --- | --- | --- |
| GET | http://[hostname:port]/paranuara/company/[company_name] | Retrieve list of all employees of the company.e.g http://localhost:8080/paranuara/company/BUGSALL |
| GET | http://[hostname:port]/paranuara/person/[person_name] | Given 1 people, provide a list of fruits and vegetables they like. e.g. http://localhost:8080/paranuara/person/Decker%20Mckenzie |
| GET | http://[hostname:port]/paranuara/people/?person1=[person1]&person2=[person2] | Given 2 people, retrieve information of both people and the list of their friends in common which have brown eyes and are still alive. e.g. http://localhost:8080/people/person1=Decker%20Mckenzie&person2=Rosemary%20Hayes|

# How to Install
1. Pull Docker image 
    - `docker pull idarahnama/paranuara`
2. Run docker container 
    - `docker run [--name <any_name>] -p <local_port>:5000 idarahnama/paranuara`
3. API would now be accessible on local port specified in previous command

# To-Do
1. Add test cases for all end points
2. Improve excpetion scenarios for different endpoints 