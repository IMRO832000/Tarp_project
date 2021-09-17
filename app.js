const express = require('express')
const request = require('request');
var app=express();
const nodemailer = require('nodemailer');
var bodyparser=require('body-parser')
var metr = require('method-override')
app.use(bodyparser.urlencoded({extended:true}))
app.set("view engine","ejs")
app.use(express.static("public"))
app.use(metr("_method"));
let test = 0;
const PORT = 3000;

app.get('/log/:id', function(req, res){

obj={name:req.params.id}

res.render("login",{usr:obj})    
})


app.post('/log_verify', function(req,res){
    
    console.log("hello");
    
   
    var emailId =req.body.email;

      
    
    
    test = Math.floor(100000 + Math.random() * 900000);
    
    
    
    
    let transporter = nodemailer.createTransport({
    
                 service: 'gmail',
         auth: {
             user: '', // generated ethereal user , must be the same  gmail as below
             pass: 'yesyesyes3'  // generated ethereal password
         },
         tls:{
           rejectUnauthorized:false
         }
       });


       let mailOptions = {
        from: '', // sender address
        to: emailId, // list of receivers
        subject: 'Node Contact Request', // Subject line
        text: test.toString(), // plain text body
        //html: output // html body
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(error);
        }
        console.log('Message sent: %s', info.messageId);   
        console.log('Preview URL: %s', nodemailer.getTestMessageUrl(info));
   
        res.redirect('/otp');
    });





})


app.get('/otp', function(req,res){
res.render('otp')
})

app.post('/otp', function(req,res){
    var ch = req.body.otp;

    if(ch==test.toString()){
        res.redirect('http://127.0.0.1:5500/index.html')
    }
else{
    res.redirect('/otp');
}


    })
    

app.listen(PORT, function (){ 
    console.log('Listening on Port 3000');
});  