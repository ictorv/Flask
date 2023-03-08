# POST REQUEST in Flask

Put ```methods=['POST']``` in route and accept input into route 
    
## Using

```javascript
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
```
where ```("first_name")``` is a variable name used for each input and accepting it as a same name which is then passed into ```render_template()``` of subscribe as a variable for using in ```form.html```

## subscribe.html
In subscribe.html ```<form action="/form" method="POST">```
here action redirect into form page and using ```POST``` request means it enables users to send HTML form data to server
