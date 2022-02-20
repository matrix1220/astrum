const express = require('express')
const path = require('path')

const app = express()

let songs = [
    'Accidents Will Happen',
    'Adeste Fideles',
    'All My Tomorrows',
    'All the Way',
    'Angel Eyes',
    'Anytime, Anywhere',
    'Around the World',
    'As Long as I Live',
    'Autumn Leaves',
    'A Baby Just Like You',
    'The Beautiful Strangers',
    'Be Careful, It\'s My Heart',
    'Before the Music Ends',
    'The Best I Ever Had',
    'The Best of Everything',
    'Bim Bam Baby',
    'Bonita',
    'Bop Goes My Heart',
    'The Boys Night Out',
    'The Brooklyn Bridge'
];

app.get('/', function (req, res) {
    res.send(songs[Math.floor(Math.random() * songs.length)])
})

app.get('/birth_date', function (req, res) {
    res.send('December 12, 1915')
})

app.get('/birth_city', function (req, res) {
    res.send('Noboken, NJ, USA')
})

app.get('/wives', function (req, res) {
    res.send('Nancy Sinatra, Ava Gardner, Mia Farrow, Barbara Marx')
})

app.get('/picture', function (req, res) {
    res.sendFile(path.join(__dirname, 'Frank_Sinatra_\'57.jpg'))
})

app.get('/public', function (req, res) {
    res.send('Everybody can see this page')
})

app.get('/protected', function (req, res) {
    if (req.headers.authorization !== `Basic ${btoa('admin:admin')}`)        
        return res.status(401).send('Not authorized')
    res.send('Welcome, authenticated client')
})

app.listen(8080)