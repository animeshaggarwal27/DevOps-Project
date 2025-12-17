const express = require('express');
const path = require('path');

const app = express();

// Serve views
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Home → render form
app.get('/', (req, res) => {
  // IMPORTANT: action points to Flask service name from docker-compose ("backend")
  res.render('form', { actionUrl: 'http://backend:8000/submit' });
});

// Optional: a health route for checks
app.get('/healthz', (req, res) => res.status(200).send('OK'));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Express listening on ${PORT}`));
