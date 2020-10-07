# Dockerizing-a-Flask-Server-
A Flask Server for CRUD operations to a database on MongoDB Atlas. Finally, dockerizing this application.

### First create Cluster, Database and a Collection on MongoDB Atlas:
  - Upload a JSON file on the database if you have any
    ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Mongo%20db%20atlas.png)
    
### Deploy the docker container:
  - All one needs is Docker installed and a Docker file
  - In the repo, 'Dockerfile' is the file to build the image
  - To build the image:
    $ docker build .
  - Tag this image:
    $ docker tag <imageID> flaskimage
  - Now start a container using this image:
    $ docker run -dit --name flaskserver -p 5055:5055 flaskimage
  - Since port 5055 has been exposed, the flask server will be accessible via localhost:5055
  
### Access API on the localhost:
  - Start the flask server:
    ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Flask%20in%20the%20host%20machine.png)
    (Note : This is the screenshot of the flask server running in the host machine)
  - Browse this address 'https://localhost:5055/' , this will return Status:UP as response if you're using my code
  - For GET, PUT requests one can use Postman to check the connection. Here are the sceenshots of Postman while running my flask server:
    ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Flask%20Server%20Running.png)
    ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Create%20Query.png)
    ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Get%20Query.png)
  - A GUI can be deployed alongwith the server, it'll be a form to interact with the database through REST API
  
### Use this API to do CRUD operations (Using Postman):
  - To Read:
    ```yaml
    {
      "database": "greendeck",
      "collection": "records",
    }
    ```
  - To Create:
    ``` yaml
    {
      "database": "greendeck",
      "collection": "records",
      "Document": {
                    "name": "Jellycat Blossom Tulip Bunny Grabber, Pink",  
                    "brand_name": "jellycat", 
                    "regular_price_value": 12.0, 
                    "offer_price_value": 12.0, 
                    "currency": "GBP", 
                    "classification_l1": "baby & child", 
                    "classification_l2": "soft toys", 
                    "classification_l3": "", 
                    "classification_l4": "", 
                    "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
                    }
     }
     ```
    - To Update:
      ```yaml
      {
        "database": "greendeck",
        "collection": "records",
        "Filter": {
                    "name": "Jellycat Blossom Tulip Bunny Grabber, Pink"
                  },
        "NewValues": {
                            "brand_name": "jellydog",
                            "regular_price_value": 14.0
                           }
       }
       ```
    - To Delete:
      ```yaml
      {
        "database": "greendeck",
        "collection": "records",
        "Filter": {
                    "name": "Jellycat Blossom Tulip Bunny Grabber, Pink"
                  }
       }
       ```
       
 ### Important:
   - I am using docker in Ubuntu running inside WSL2 on Windows machine. Because of this I was facing some issue to connect to the internet.
   - Error I am getting
      ![alt text](https://github.com/sourabh-burnwal/Dockerizing-a-Flask-Server/blob/main/Screenshots/Error%20Because%20of%20WSL2.png)
   - I have found the issue, it's happening because WSL gives dynamic DNS nameservers and it gets copied in the containers. I changed the same to Google's. But, later found out       that the same needs to be done in the Ubuntu as well. I am sure the ones aren't using WSL won't get any errors. But if anyone gets, start a issue thread.
