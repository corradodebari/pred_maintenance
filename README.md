# Predictive Maintenance through MSET-SPRT 
Predictive Maintenance through MSET-SPRT 

Setup Apache Zeppelin environment for Oracle DB 20c
Use a docker image
Zeppelin install:
```
docker run -d -it -e GRANT_SUDO="yes" --user root -p 8080:8080  -v /Users/cdb/:/host  --name zeppelin apache/zeppelin:0.8.1
```
Put a copy of **ojdbc8.jar** and save in **/zeppelin/interpreter/jdbc/ojdbc8.jar**

# Create a new interpreter
Chooes an **Intepreter Name**, for example **osql** , and jdbc as **Interpreter Group**:

![Interpreter](Interpreter.jpg)

then complete as follow:

![Conf](Conf.jpg)

In this case it has been used a "Service" as DB Connection, non a SID.

In [**test.py**](test.py)  file change:   



