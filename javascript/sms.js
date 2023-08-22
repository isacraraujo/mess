const accountSid   = 'ACCOUNT_SID';
const authToken    = 'AUTH_TOKEN';
const mensagem     = 'Olá, isso é uma mensagem de teste via Twilio!';
const destinatario = '+DD_DDD_NUMERO';
const twilioURL    = `https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`;
const twilioNumber = '+NUMERO_TWILIO'

const headers = new Headers({
  'Authorization': 'Basic ' + Buffer.from(`${accountSid}:${authToken}`).toString('base64'),
  'Content-Type': 'application/x-www-form-urlencoded',
});

const formData = new URLSearchParams();
formData.append('To', destinatario);
formData.append('From', twilioNumber);
formData.append('Body', mensagem);

fetch(twilioURL, {
  method: 'POST',
  headers: headers,
  body: formData,
})
  .then(response => response.json())
  .then(data => {
    if (data.sid) {
      console.log('SMS enviado SID:', data.sid);
    } else {
      console.error('Erro ao enviar SMS:', data);
    }
  })
  .catch(error => console.error('Erro ao enviar SMS:', error));