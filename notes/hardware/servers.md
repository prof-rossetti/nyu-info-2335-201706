# Servers

The responsibility of a "server" computer in client-server computer network architecture is to respond to requests issued by the "client" computer.

In a practical sense, a **server** often refers to a remote computer which we can operate in a similar way as our personal computers, but which in most cases doesn't have a monitor or keyboard, so we manage them using the command-line.

## Remote Servers (Cloud Computing)

### Major Providers of

  + [Amazon Web Services](https://aws.amazon.com/)
  + [Heroku](https://www.heroku.com/)

### Advantages of

  + Cost
  + Scalability
  + Efficiency
  + Security
  + Usability

## Types of Servers

  + Application Servers
  + Database Servers
  + Email Servers
  + etc.

### Application Servers

When we "deploy" an application to a server, we copy the application's source code onto the server. The server then runs the application just like we were running the application in development on our local machines.

#### Deployment Environments

Name | Description | Common Developer Tasks | Primary Audience | Level of Risk
--- | --- | --- | --- | ---
Development | The computer, often a personal computer, on which you produce, develop, and test an application's source code. | Running a local web server, editing code in a text-editor, and running tests. | One or more individual members of the software development team. | Low
Staging | The computer, often a remote server, onto which you deploy an application's source code to emulate as best as possible the production environment to get a sense for how code changes will affect the application running on the production environment. | Performing usability tests, monitoring server scalability and performance. | One or more collective members of the software development team. | Medium
Production | The computer, often a remote server, onto which you deploy your application's source code for "live" usage. | Monitoring server logs. | Users, customers, and the public at large. | Very High
