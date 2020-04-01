# Predictive Maintenance through MSET-SPRT 
This is a description to setup an environment to test Predictive Maintenance through MSET-SPRT on Oracle DBMS 20c in preview release.  

## Zeppelin setup:
Setup Apache Zeppelin environment for Oracle DB 20c using a docker image.

Install a Docker container in this way::
```
docker run -d -it -e GRANT_SUDO="yes" --user root -p 8080:8080  -v [YOUR_DIRECTORY]:/host  
          --name zeppelin apache/zeppelin:0.8.1
```
Get a copy of **ojdbc8.jar**, for example from SQLDeveloper, and save it in **/zeppelin/interpreter/jdbc/ojdbc8.jar**

## Create a new interpreter:
Connect to http://localhos:8080 and from menu:

<img src="Menu.png" alt="Menu" width="250"/>

push the create button:

<img src="Create.png" alt="Create" width="250"/>

and chooe an **Intepreter Name**, for example **osql** , and jdbc as **Interpreter Group**:

![Interpreter](Interpreter.jpg)

then complete as follow:

![Conf](Conf.jpg)

In this case it has been used a "Service" as DB Connection, non a SID.





