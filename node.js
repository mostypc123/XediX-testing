const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Endpoint to handle migration
app.post('/migrate', (req, res) => {
    const migrationData = req.body;

    // Process and insert data into Node.js database (MongoDB, for example)
    // Assume you have a MongoDB connection and models for 'accounts', 'followers', and 'posts'

    // Example MongoDB insert (you need to implement your own logic)
    // const AccountsModel = require('./models/accounts');
    // const FollowersModel = require('./models/followers');
    // const PostsModel = require('./models/posts');

    // Insert accounts
    // AccountsModel.insertMany(migrationData.accounts);

    // Insert followers
    // FollowersModel.insertMany(migrationData.followers);

    // Insert posts
    // PostsModel.insertMany(migrationData.posts);

    res.send('Migration successful');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
