const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const morgan  = require('morgan');
const {sequelize} = require('./models');
const app = express();
const config = requere('./config/config')


app.use(bodyParser.json());
app.use(cors());
app.use(morgan('combined'));

app.post('/register', (req, res) => {
    res.send({
        message: `hello ${req.body.username}, register succesfull!`
    });
});

//ma voi conecta la bd inainte de a conecta server-ul
//voi folosi un file config pentru configurare serverului si a bd inclusiv introduc acolo portul pe care va sta site-ul
sequelize.sync()
    .then (() => {
        app.listen(config.port);
        console.log(`server upp)) here is port ${config.port}` )
})