# Non-Technical Run Down of Project

### Everything You Need to Know About the Backend

### Introduction

The 596E-S22 Backend is an independent, containerized service responsible for maintaining the history and integrity of the data associated with all (or at least the majority) of the projects of the Spring 2022 semester.

In plain english, the backend repository houses all recorded data inside and outside of the desktop app. This includes:

- Cases
- Workers (People who are on the case)
- Interviews
- License Plates (from recorded video surveillance)
- Objects (from recorded video surveillance (i.e. “white car” or “person”))
- Surveillance Video
- Messages

This allows the backend to be connected to and used by several services including:

- Interview Transcriber
- Dense Image Captioning
- License Plate Identifier
- and more

### How does it work?

At the heart of the backend repository is a PostgreSQL Database used for writing and reading all of the data associated with our application. SQL is a popular query language used for generating relational database, such as Postgres. 

A database on its own, however, is nothing without a proper infrastructure to write to it and read from it. In order to accomplish this feat, the entire database is wrapped in a FastAPI server. FastAPI is a popular networking interface that allows devices to execute ‘requests’ in which they ask for some data. To which FastAPI then contacts the backend, grabs the data, and returns it to the device. 

The same pipeline can be utulized to send data to the server. Should a device have some data they want to make available to everyone (let’s say a message of some kind) they can use the FastAPI server to ‘post’ some data, where the FastAPI Server will receive the data, save it to the backend, and return some information to the device detailing the success or failure of the process.

### Conceptual Example

A Library serves a useful analogy here. We can consider the services of our library the FastAPI Server (Operations such as the book return slot, the dewey decimal system, and the librarian) and we consider the books (technically the book shelves) our database:

At the heart of any library is the books, just like our database. Should a user want to retrieve a book, they first need to consult the dewey decimal system (Our FastAPI service). Here they can find where the book is located, and resultingly retrieve it as needed.

Should a user want to return some books (Send some data), they will bring their books to the book return slot and dump them in. From there, the librarian will take these books and bring them to their proper place in the library (Like saving them to the database). By doing so they are now available for everyone to consult and use.

### How do all the services talk to each other?

One of the most interesting problems of the backend was how to go about connecting all of our services together. While its very easy to just copy and paste the backend code into everyones repositories to use, this isn’t exactly good practice and can lead to tons of issues. Instead, we opted to utulize Github Packages and Docker to package up our backend repository into a service and make it available for everyone on the team to use in their own repos.

Github Packages is a service used to automate tasks. Since all of our repositories are hosted on Github, it made the most sense to use this service. Using github packages, we can automatically convert our service into a docker image that can be shared and distrubited amongst the team (explained below)

Docker is a service that allows the developer to abstract the computer they are using from the code pipeline. This is great for a lot of reasons, namely, not everyone has the same computer (and this can lead to really annoying and weird problems). Docker helps standardize the system everyone is running and thus, making a docker image, we are able to download and run these “images” of code without a hitch.

With the combination of these two services, we are able to push out new versions of the backend without even lifting a finger. Likewise, all of the services that rely on the backend are able to grab these new versions, download them, and use them in their repositories without any issues at all! The whole pipeline works really well and is denoted as Continous Deployment.

### Where to go from here

While the majority of ground work has been layed out to host a reliable and versatile backend, there is always more places to expand. One particular area that got relatievly no attention this semester was testing. Testing is a massively important consideration in any software package, and the backends alarmingly low percentage of tests is very concerning. If future development were to be continued on this project, that would be the top priority, in my opinion.

Secondly, another place for improvement would be the interview-analyzer pipeline. A really quick architecture thrown together by myself and Collette, it would be valuable to revisist this pipeline and improve the way data flows. Currently, there are some tasks handled by the backend that could be offloaded to the front end or another intermediatery service. I think, with more time, I would have liked to improve this pipeline and architecture more.

Finally, from there, the main improvement could be to add more support for other routes and entry points into the database. I think, for example, it would have been awesome to port over Smriti’s MongoDB code into the postgreSQL database so that all of our services existed in one place. Due to time, however, this did not happen.

### Summary

Overall, I was extremely pleased with the progress of our backend repository. This class not only taught me skills that I had been itching to learn, but it also allowed me to apply them in a really dynamic and goal-oriented work enviornment. Getting to work with others across multiple services in an agile development process was extremely rewarding and taught me a lot in all areas of software development. I am extremely grateful for the oppertunity to build up these skills and look forward to utulizing them in future projects and teams down the line.
