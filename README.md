# Testing Third-Party APIs with Mock Servers

**By Jason Parent**

Every popular product has an API that allows your app to use its services. I use external APIs in almost all of my projects and chances are good that you do too. So many useful services exist that it is difficult to have a great app without leveraging what they offer.

Despite being so useful, external APIs can be a pain to test. When you hit an actual API, your tests are at the mercy of the server. You will likely encounter one or more the following pain points:
- The request-response cycle can take several seconds. That might not seem like much at first, but the time compounds with each test. Imagine calling an API 10, 50, or 100 times when testing your entire application. 
- The API server may be unreachable. Maybe the server is down for maintenance. Maybe it failed with an error and a development team is working to get it functional again. Do you really want the success of your tests to rely on the health of a server you don't control? 

Your tests shouldn't assess whether an API server is running; they should test whether your code is operating as expected. This tutorial will teach you how to mock an API server to test your Python code that interacts with external services.

## Setup

Download and install a tool that lets you create isolated Python environments on your local machine. I prefer <a href="https://virtualenvwrapper.readthedocs.org/en/latest/install.html">virtualenvwrapper</a>. Make a virtual environment and install the required packages outlined below. Navigate to a directory where you keep your projects and start a new Django project.

```bash
local:~ user$ mkvirtualenv example
(example)local:~ user$ pip install mock nose requests
(example)local:~ user$ cd ~/Projects
(example)local:Projects user$ mkdir example-mock-server && cd example-mock-server
```

