## Random Code Generator

### Specification

This repo will be for the 2nd Project of the DevOps GMCA Course. 

I will be creating a random code generator, where parts of the code are generated and sent as a micro-serviced flask app. The front-end will be service_1 and services_2/_3/_4 will generate a part of the code and send it to service_1. There it will be pieced together and added to a database and displayed on the screen through the HTML file.

### Contents

## Initial Planning

### Initial Planning

Trello was used to create an initial list plan of what I had to do. More tasks are added as the project progresses and it is an easy way to keep track of your tasks.

I have uploaded an image of the Trello board when I had started the project:

![quiz app wireframe](https://user-images.githubusercontent.com/55449689/107543761-70c8cc80-6bc1-11eb-9885-e79398e81961.jpeg)
<#trello board>

### Architecture

Below is the architecture of what my services will send:

<#architecture_1>

Below is the architecture of how my services will work with requests and queries:

<#architecture_2>

## Services

### Database

<#database diagram>

### Service 1

Service 1 has three jobs:

- The first is to request and receive code parts from services 2, 3 and 4.
- The second is to concatenate the string format code parts into one generated code.
- The third is to store the generated code into in the database.

Below are examples of the front end that is displayed with the generated values:

Example 1:

<#index_won>

Example 2:

<#index_lose>

Service one has also been tested and the test coverage is shown below:

<#test_cov>

### Services 2, 3 and 4

Service 2,3 and 4 will perform the same task: generating a code when requested and sending it to service 1.

one example of generating a random code is shown below:

```python
def code_part_example():
    # where the code is decided
    code_part = ""
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        code_part += str(choice[randrange(len(choice))])

    str(code_part)

    return code_part
```

## CI/CD pipeline

Below is the CI/CD pipeline that I am using:

<#pipeline>

## Conclusion

<#trello board 2>

As you can see by the trello board I ran out of time to complete the project.

The main issue was that on the weekend and on the last day I had other things going on that were conflicting with my time to work on the code. If I had That much time I believe I could have successfully deployed the application.

### Risk Assessment

<#risk_assessment_1>

<#risk_assessment_2>

As you can see from a contrast in the risk assessments; I mainly ran out of time and had issues with coping under the stress of the environment as well as the time constraints.

### Improvements

- add CSS
- finish Ansible
- finish Jenkins Pipeline
- Docker Stack Deploy from Jenkins
- Add web-hook to the GitHub repo through Jenkins
- Add more instances
- Add a larger selection of prizes
- Add a service 5 to concat the code parts from services 2, 3, 4
- Add Tests for services 2, 3 , 4

### Acknowledgements

This project was done in a GMCA DevOps Bootcamp and was taught by consultants at QA. Most of the work involved in this was taught at the academy virtually and were were provided resources to help us. 

I would like to thank the instructors of the course for the help they have provided in order to be able to complete this course.
