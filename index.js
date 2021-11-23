const nodemailer = require('nodemailer');


 
let test = 0;
 
async function login(emailId){
 
    test = Math.floor(100000 + Math.random() * 900000);
  
  let transporter = nodemailer.createTransport({
    
   // true for 465, false for other ports
    service: 'gmail',
    auth: {
        user: 'rishabhbhai101@gmail.com', // generated ethereal user
        pass: 'yesyesyes3'  // generated ethereal password
    },
    tls:{
      rejectUnauthorized:false
    }
  });
 
  // setup email data with unicode symbols
  let mailOptions = {
      from: 'rishabhbhai101@gmail.com', // sender address
      to: emailId, // list of receivers
      subject: 'Node Contact Request', // Subject line
      text: test, // plain text body
      //html: output // html body
  };
 
  // send mail with defined transport object
  transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
          return console.log(error);
      }
      console.log('Message sent: %s', info.messageId);   
      console.log('Preview URL: %s', nodemailer.getTestMessageUrl(info));
 
      res.render('contact', {msg:'Email has been sent'});
  });
 
}
 
async function check(){
    var otp = document.getElementById("otp");
 
    console.log(otp);
}
 
login("nageshshukla1210@gmail.com");