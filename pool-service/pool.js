const express = require('express');

const app = express();
const port = "9090";

app.get('/', (req, res) => res.send("pool service works\n"));
app.listen(port, () => console.log(`pool service listening on ${port}`));